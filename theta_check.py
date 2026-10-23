"""Exact finite checks for the theta-family construction and leaf reduction."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib,json,random,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import verify_families as vf
from cycle_pendant_check import avoid_edge

P=(0,1,3,7,8);X=set(P)|{2}
ASIDES=[]
for i in range(5):
    edge=tuple(sorted((P[i],P[(i+1)%5])))
    ASIDES.append(next(side for side,pairs in vf.SIDES if edge in pairs))
C,E,H=ASIDES[2],ASIDES[4],ASIDES[3]
D,F,G=[tuple(v for v in range(16) if v not in s) for s in (C,E,H)]
A=ASIDES[0];AP=tuple(v for v in range(16) if v not in A)

def check(w,x):
    n=sum(w)
    assert sum(x)==Q(n,2) and all(0<=x[v]<=w[v] for v in range(16))
    assert 50*vf.cost(x)<=n*n
    return x

def scale(w,side):
    h=sum(w)/2;mass=sum(w[v] for v in side)
    assert mass>=h
    x=[w[v]*h/mass if v in side else Q(0) for v in range(16)]
    assert 64*vf.cost(x)<=sum(w)**2
    return check(w,x)

def controlled_cycle_half(b):
    T=sum(b)
    if not T:return 2,[Q(0)]*5
    for j in range(5):
        k=(j+2)%5
        if b[j]+b[k]>=T/2:
            i=next(i for i in (2,3,4) if {j,k}<={i,(i+1)%5,(i+3)%5})
            y=[Q(0)]*5;y[j]=min(b[j],T/2);y[k]=T/2-y[j]
            return i,y
    shift=1 if b[2]+b[4]<=b[0]+b[3] else 0
    rotated=[b[(j+shift)%5] for j in range(5)]
    i,yr=avoid_edge(rotated);y=[Q(0)]*5
    for j in range(5):y[(j+shift)%5]=yr[j]
    i=(i+shift)%5
    if i in (0,1):assert y[1]<=b[1]/2
    return i,y

def balanced_construct(w):
    w=list(map(Q,w));n=sum(w)
    if not n:return 'zero',[Q(0)]*16
    d,e,t,f,a,c=(w[v] for v in (0,3,7,8,1,4))
    assert w[1]==w[2]
    h=n/2
    for label,side in (('D_heavy',D),('F_heavy',F),('G_heavy',G)):
        if sum(w[v] for v in side)>=h:return label,scale(w,side)
    assert d+e>2*a and t+f>2*c
    if min(t,f)<=c:return 'straddle_long_edge',scale(w,H)
    if e<=c:return 'straddle_e',scale(w,C)
    if d<=c:return 'straddle_d',scale(w,E)
    if a<=c:
        side=A if sum(w[v] for v in A)>=h else AP
        return 'straddle_twin',scale(w,side)
    assert min(d,e,t,f,a)>=c
    b=[d-c,2*(a-c),e-c,t-c,f-c];T=sum(b)
    i,y=controlled_cycle_half(b)
    x=[c if v in ASIDES[i] else Q(0) for v in range(16)]
    for j in (0,2,3,4):x[P[j]]+=y[j]
    if i in (0,1):
        assert y[1]<=a-c and 1 in ASIDES[i]
        x[1]+=y[1]
    elif i==3:
        first=min(y[1],a-c)
        x[1]+=first;x[2]+=y[1]-first
    else:assert y[1]==0
    actual_increment=x[:]
    for v in ASIDES[i]:actual_increment[v]-=c
    cycle_cost=sum(y[j]*y[(j+1)%5] for j in range(5))
    assert vf.cost(actual_increment)==cycle_cost<=T*T/50
    assert vf.cost(x)<=4*c*c+c*T/2+T*T/50<=n*n/50
    return 'controlled_cycle_lift',check(w,x)

def run():
    branches={};balanced_cases=0;lift_templates=set()
    for d,e,t,f,a,c in product(range(5),range(5),range(5),range(5),range(5),range(3)):
        w=[c]*16
        for v,z in zip((0,3,7,8,1,2),(d,e,t,f,a,a)):w[v]=z
        if not sum(w):continue
        name,x=balanced_construct(w);balanced_cases+=1
        branches[name]=branches.get(name,0)+1
        vf.round_selection(w,x)
    arbitrary=0;comparisons=0
    vectors=[]
    for c,d,e,t,f,a1,a2 in product(range(3),repeat=7):
        w=[c]*16
        for v,z in zip((0,3,7,8,1,2),(d,e,t,f,a1,a2)):w[v]=z
        if sum(w):vectors.append(w)
    rng=random.Random(12820261027)
    for _ in range(400):
        w=[rng.randrange(20)]*16
        for v in X:w[v]=rng.randrange(150)
        vectors.append(w)
    for w in vectors:
        wb=list(map(Q,w));wb[1]=wb[2]=Q(w[1]+w[2],2)
        name,reference=balanced_construct(wb)
        actual=[y for side,pairs in vf.SIDES if (y:=vf.match_half(w,side,pairs)) is not None]
        mean=[y for side,pairs in vf.SIDES if (y:=vf.match_half(wb,side,pairs)) is not None]
        actual=min(actual,key=vf.cost);mean=min(mean,key=vf.cost)
        assert vf.cost(actual)<=vf.cost(mean)<=vf.cost(reference)
        check(w,actual);vf.round_selection(w,actual)
        arbitrary+=1;comparisons+=1
    out={'date':'2026-10-23','balanced_cases':balanced_cases,'branches':branches,
         'arbitrary_vectors':arbitrary,'exact_reduction_comparisons':comparisons,
         'all_constructed_and_rounded':True,
         'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'finite exact implementation checks; analytic proof is in main.tex'}
    Path(__file__).with_name('theta_check_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
