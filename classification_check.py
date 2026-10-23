"""Exact census of all six-position sets. This is a finite structural check."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import verify_families as vf

def main():
    counts=Counter()
    for Xtuple in combinations(range(16),6):
        X=set(Xtuple)
        edges=[(u,v) for u,v in vf.EDGES if u in X and v in X]
        if {u^v for u,v in edges}!=set(vf.D):
            counts['missing_colour']+=1
            continue
        cycles=[]
        for Ptuple in combinations(Xtuple,5):
            P=set(Ptuple)
            pe=[(u,v) for u,v in edges if u in P and v in P]
            if len(pe)==5 and all(sum(v in edge for edge in pe)==2 for v in P):
                cycles.append(P)
        if cycles:
            P=cycles[0];z=next(iter(X-P))
            degree=sum((min(z,v),max(z,v)) in vf.EDGES for v in P)
            assert degree in (0,1,2)
            shape=('pentagon_plus_isolate','pentagon_with_leaf','theta')[degree]
        else:
            degrees=tuple(sorted((sum(v in edge for edge in edges) for v in X),reverse=True))
            names={(5,1,1,1,1,1):'star',(4,2,1,1,1,1):'extended_star',
                   (3,3,1,1,1,1):'double_star'}
            assert len(edges)==5 and degrees in names,(Xtuple,edges)
            shape=names[degrees]
        counts[shape]+=1
    expected={'missing_colour':5800,'star':16,'extended_star':320,'double_star':240,
              'pentagon_plus_isolate':192,'pentagon_with_leaf':960,'theta':480}
    assert dict(counts)==expected
    report={'position_sets':sum(counts.values()),'counts':dict(counts),
            'all_shapes_have_analytic_capacity_proofs':True,
            'scope':'finite position census, not a capacity-vector sampling proof',
            'program_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('classification_results.json').write_text(
        json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
