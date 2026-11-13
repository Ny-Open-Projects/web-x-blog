#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Driver: for a given python reference file, generate go/java/ts solution files
with embedded assertions. Ground truth computed via run_ref2.py.
Usage: gen.py <pyfile> <out_dir> <base_name> [--mode auto|plain|tree|list]
Emits: <out_dir>/<base_name>.go/.java/.ts  (only for langs requested)
Writes a JSON line to stdout: {file, status, note}
"""
import sys, os, ast, json, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import tp

REPO="/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
HELPERS=tp.HELPERS

def find_solve(src):
    return tp.find_solve(src)

def extract_main_cases(src, fname):
    """Return list of arg-tuples (lists) from solve(...) calls in __main__."""
    tree=ast.parse(src); cases=[]
    mb=None
    for n in tree.body:
        if isinstance(n, ast.If): mb=n.body; break
    if not mb: return cases
    for n in mb:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
            f=n.value.func
            if isinstance(f, ast.Name) and f.id==fname:
                try:
                    args=[ast.literal_eval(a) for a in n.value.args]
                    cases.append(args)
                except Exception:
                    pass
    return cases

def synth_cases(fn, params):
    """Synthesize plain representative inputs from REQUIRED param types (memo excluded)."""
    ndef=len(fn.args.defaults) if hasattr(fn.args,'defaults') else 0
    req=params[:len(params)-ndef]
    cases=[]
    if all(t=='int' for _,t in req):
        cases=[[5],[0],[1],[10]]
    elif all(t=='list' for _,t in req):
        cases=[[[3,1,2]],[[1]],[[]],[[5,3,8,1,2]]]
    else:
        def one(t): return [3,1,2] if t=='list' else (5 if t=='int' else [1,2])
        cases=[[one(t) for _,t in req] for _ in range(3)]
    return cases[:4]

def fmt_expected(lang, valstr, ret):
    """Convert python repr string to target literal."""
    # valstr is python repr e.g. '[1, 2, 3]' or 'True' or '3' or "['a','b']"
    if ret in ('list',):
        # parse as python list
        try:
            v=ast.literal_eval(valstr)
            if lang=='go': return "[]int{"+", ".join(str(x) for x in v)+"}"
            if lang=='java': return "new int[]{"+", ".join(str(x) for x in v)+"}"
            return "["+", ".join(str(x) for x in v)+"]"
        except Exception:
            return "/*bad*/"
    if ret=='bool':
        if valstr=='True': return 'true' if lang!='go' else 'true'
        return 'false'
    if ret=='str':
        return valstr  # already quoted-ish? python repr of str is '...'; convert
    # int/num
    return valstr

def mode_of(params, ret, fnbody_src):
    if any(t=='tree' for _,t in params): return 'tree'
    if any(t=='listnode' for _,t in params): return 'list'
    return 'plain'

def main():
    pyfile=sys.argv[1]; outdir=sys.argv[2]; base=sys.argv[3]
    langs=sys.argv[4].split(',') if len(sys.argv)>4 else ['go','java','ts']
    src=open(pyfile, encoding='utf-8').read()
    fname=find_solve(src)
    if not fname:
        print(json.dumps({"file":base,"status":"fail","note":"no solve func"})); return
    tree=ast.parse(src)
    fn=None
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name==fname: fn=n
    if not fn:
        print(json.dumps({"file":base,"status":"fail","note":"solve not found"})); return
    params=tp.infer_params(fn)
    ret=tp.infer_return(fn)
    mode=mode_of(params, ret, src)
    # cases
    if mode in ('tree','list'):
        pool=[[1,2,3],[1,None,2,None,3],[5,4,8,None,None,6,9],[1],[],[2,3,None,4],[1,2,2,3,None,None,3,4,5]]
        def variant(t): return [(x*2 if isinstance(x,int) else None) for x in t]
        nfields=len(params)
        cases=[]
        for t in pool:
            cases.append([t]+[t]*(nfields-1))           # identical
            if nfields>1:
                cases.append([t]+[variant(t)]+[t]*(nfields-2))  # same shape, diff values
            if len(cases)>=8: break
        cases=cases[:8]
    else:
        cases=extract_main_cases(src, fname)
        if not cases:
            cases=synth_cases(fn, params)
    if not cases:
        print(json.dumps({"file":base,"status":"fail","note":"no cases"})); return
    # ground truth
    try:
        out=subprocess.check_output(["python3", os.path.join(REPO,"_tools/run_ref2.py"),
            pyfile, mode, json.dumps(cases)], cwd=REPO, timeout=30).decode().splitlines()
    except Exception as e:
        print(json.dumps({"file":base,"status":"fail","note":"gt err "+str(e)[:80]})); return
    if not out or out[0].startswith("NOFUNC"):
        print(json.dumps({"file":base,"status":"fail","note":"gt nofunc"})); return
    got=out[1:]
    # filter out ERRCASE cases (python ref crashed) - drop in/out pair
    good=[(cin, g) for cin, g in zip(cases, got) if g!="ERRCASE" and "ERRCASE" not in g]
    if not good:
        print(json.dumps({"file":base,"status":"fail","note":"all cases crashed in python ref"})); return
    cases=[c for c,_ in good]; got=[g for _,g in good]
    # generate per lang
    results=[]
    for lang in langs:
        exps=[fmt_expected(lang, g, ret) for g in got]
        try:
            code=tp.build(lang, src, fname, fn, mode, cases, exps)
        except tp.TP as e:
            results.append({"file":base+"."+lang,"status":"fail","note":"transpile "+str(e)[:60]}); continue
        ext={'go':'go','java':'java','ts':'ts'}[lang]
        outp=os.path.join(outdir, base+"."+ext)
        open(outp,"w").write(code)
        results.append({"file":outp,"status":"done_pass?","note":"generated"})
    print(json.dumps(results))

if __name__=="__main__":
    main()
