"""Exact construction checks for all branches of the pendant-pentagon proof."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib,json,random,sys
ROOT=Path(__file__).resolve().parent
import verify_families as vf

P=(0,1,3,7,8);Z=4;X=set(P)|{Z}
ASIDES=[]
for i in range(5):
    edge=tuple(sorted((P[i],P[(i+1)%5])))
    ASIDES.append(next(side for side,pairs in vf.SIDES if edge in pairs))
BSIDES=[tuple(v for v in range(16) if v not in a) for a in ASIDES]
assert [Z in a for a in ASIDES]==[False,True,True,True,False]

def check(w,x):
    n=sum(w)
    assert sum(x)==Q(n,2) and all(0<=x[v]<=w[v] for v in range(16))
    assert 50*vf.cost(x)<=n*n,(w,x,vf.cost(x))
    return x

def avoid_edge(b):
    b=list(map(Q,b));T=sum(b)
    if not T:return 1,[Q(0)]*5
    for j in range(5):
        k=(j+2)%5
        if b[j]+b[k]>=T/2:
            i=next(i for i in range(1,5) if {j,k}<={i,(i+1)%5,(i+3)%5})
            y=[Q(0)]*5;y[j]=min(b[j],T/2);y[k]=T/2-y[j]
            return i,y
    choices=[]
    for i,full in ((1,2),(4,4),(2,3),(3,3)):
        isolated=(i+3)%5
        other=i if full==(i+1)%5 else (i+1)%5
        y=[Q(0)]*5
        y[full]=b[full];y[isolated]=b[isolated]
        y[other]=T/2-y[full]-y[isolated]
        assert all(0<=y[j]<=b[j] for j in range(5))
        choices.append((i,y,sum(y[j]*y[(j+1)%5] for j in range(5))))
    avg=choices[0][2]/5+choices[1][2]/5+3*choices[2][2]/10+3*choices[3][2]/10
    U,V,W=b[0]+b[1],b[2]+b[4],b[3]
    assert T*T/50-avg==((2*U-3*V+2*W)**2+15*(V-2*W)**2)/200
    i,y,cost=min(choices,key=lambda row:row[2])
    assert cost<=T*T/50
    return i,y

def construct(w):
    w=list(map(Q,w));n=sum(w)
    if not n:return 'zero',[Q(0)]*16
    p=[w[v] for v in P];d=w[Z];c=w[2];W=sum(p);h=n/2
    for i,b in enumerate(BSIDES):
        mass=sum(w[v] for v in b)
        if mass>=h:
            x=[w[v]*h/mass if v in b else Q(0) for v in range(16)]
            assert 64*vf.cost(x)<=n*n
            return 'heavy_B',check(w,x)
    if d<=c:
        candidates=[]
        for i,a in enumerate(ASIDES):
            x=[Q(0)]*16
            for v in a:
                if v not in X:x[v]=c
            if i in (1,2,3):x[Z]=d
            k=(W+d)/2 if i in (0,4) else (W-d+2*c)/2
            x[P[i]]=p[i];x[P[(i+3)%5]]=p[(i+3)%5]
            x[P[(i+1)%5]]=k-p[i]-p[(i+3)%5]
            assert sum(x)==h
            assert all(0<=x[v]<=w[v] for v in range(16))
            candidates.append(x)
        bound=W*W/50+2*c*W/5-W*d/10+(8*c*c+2*c*d)/5
        average=sum(vf.cost(x) for x in candidates)/5
        assert average<=bound<=n*n/50
        assert n*n/50-bound==7*W*d/50+d*d/50+2*c*c/5
        return 'low_leaf_average',check(w,min(candidates,key=vf.cost))
    assert p[0]>d and p[1]>c and p[4]>c
    for vertex,side_i in ((2,1),(3,3)):
        if p[vertex]<=c:
            a=ASIDES[side_i];mass=sum(w[v] for v in a)
            x=[w[v]*h/mass if v in a else Q(0) for v in range(16)]
            assert mass>h and 64*vf.cost(x)<=n*n
            return 'straddling_edge',check(w,x)
    assert all(pj>=c for pj in p)
    b=[pj-c for pj in p];extra=d-c;T=sum(b)+extra
    virtual=b[:];virtual[1]+=extra
    i,y=avoid_edge(virtual)
    x=[c if v in ASIDES[i] else Q(0) for v in range(16)]
    for j,v in enumerate(P):
        if j!=1:x[v]+=y[j]
    first=min(y[1],b[1]);leaf=y[1]-first
    assert leaf<=extra
    x[P[1]]+=first;x[Z]+=leaf
    assert vf.cost(x)<=4*c*c+c*T/2+T*T/50<=n*n/50
    return 'nonnegative_increment_lift',check(w,x)

def run():
    branches={};ncase=0;odd=0
    for b in product(range(4),repeat=5):avoid_edge(b)
    vectors=[]
    for c,d,*p in product(range(3),range(5),*([range(3)]*5)):
        w=[c]*16
        for v,val in zip(P,p):w[v]=val
        w[Z]=d
        if sum(w):vectors.append(w)
    rng=random.Random(12820261026)
    for _ in range(500):
        w=[rng.randrange(20)]*16
        for v in X:w[v]=rng.randrange(200)
        vectors.append(w)
    for w in vectors:
        name,x=construct(w);ncase+=1;odd+=sum(w)%2
        branches[name]=branches.get(name,0)+1
        vf.round_selection(w,x)
    out={'date':'2026-10-23','c5_edge_avoidance_grid':4**5,
         'pendant_vectors':ncase,'odd_totals':odd,'branches':branches,
         'all_vectors_constructed_and_rounded':True,
         'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'exact finite implementation checks; universal claim uses the analytic proof'}
    Path(__file__).with_name('cycle_pendant_check_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
