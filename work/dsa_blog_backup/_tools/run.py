#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process a chunk of target files: transpile python ref -> target lang, verify, record."""
import os, ast, sys, json, re, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import remediate as R

PROGRESS = "/Users/Wang/Code/webfault-ai/dsa/_tools/scale_progress_chunk2.json"

def analyze_prob(prob_folder, sol_basename):
    """Return (func_node, classes, tests) for the primary solve function.
       Prefer the python file matching sol_basename; gather tests from all py files."""
    pydir = R.find_pydir(prob_folder)
    if not pydir:
        return None
    pyfiles = sorted(f for f in os.listdir(pydir) if f.endswith(".py"))
    # pick matching file
    match = None
    sol_base = os.path.splitext(sol_basename)[0]  # solution_3___3
    for f in pyfiles:
        if os.path.splitext(f)[0] == sol_base:
            match = f; break
    chosen = match or pyfiles[0]
    # parse chosen for func node and classes
    src = open(os.path.join(pydir, chosen), encoding="utf-8").read()
    tree = ast.parse(src)
    classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    # find primary solve from __main__ across all files
    result_map = {}
    for f in pyfiles:
        s2 = open(os.path.join(pydir, f), encoding="utf-8").read()
        try: t2 = ast.parse(s2)
        except Exception: continue
        main_body = None
        for n in t2.body:
            if isinstance(n, ast.If) and isinstance(n.test, ast.Compare) and isinstance(n.test.left, ast.Name) and n.test.left.id == "__name__":
                main_body = n.body; break
        if not main_body: continue
        fns = {n.name: n for n in t2.body if isinstance(n, ast.FunctionDef)}
        SOLVE_HELPERS = R.HELPER_NAMES | {"build", "to_list", "toList", "build_tree",
            "buildTree", "print_list", "list_to_arr", "traverse", "make_list", "gen",
            "create", "helper"}
        # identify top-level solve calls (statements that directly contain a solve call)
        solve_stmts = []
        for st in main_body:
            for node in ast.walk(st):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and \
                   node.func.id in fns and node.func.id not in SOLVE_HELPERS and not node.func.id.startswith("build"):
                    solve_stmts.append(st)
                    break
        ns = {}
        try: exec(compile(s2, f, "exec"), ns)
        except Exception: continue
        # build variables: execute all main statements except the solve-call statements
        for st in main_body:
            if st in solve_stmts: continue
            try: exec(compile(ast.Module([st], []), "<s>", "exec"), ns)
            except Exception: pass
        # now capture solve calls
        for st in solve_stmts:
            for node in ast.walk(st):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    sname = node.func.id
                    if sname not in fns or sname in SOLVE_HELPERS or sname.startswith("build"):
                        continue
                    live = ns.get(sname)
                    if live is None: continue
                    try: args = [eval(ast.unparse(a), ns) for a in node.args]
                    except Exception: continue
                    try: out = live(*args)
                    except Exception: continue
                    try:
                        args_ser = [R.py_serialize(a) for a in args]
                        inplace = (out is None)
                        if inplace:
                            post = R.py_serialize(args[0]) if args else ("none", None)
                            ret_ser = post
                        else:
                            ret_ser = R.py_serialize(out)
                    except R.SerError: continue
                    # skip degenerate cases where a structural arg is None
                    if any(t == "none" for t in [R.classify_type(a) for a in args]) and any(
                            R.classify_type(a) in ("listnode", "treenode", "list") for a in args):
                        continue
                    ptypes = [R.classify_type(a) for a in args]
                    rtype = R.classify_type(out) if not inplace else (R.classify_type(args[0]) if args else "none")
                    entry = (tuple(args_ser), ret_ser, tuple(ptypes), rtype, inplace)
                    key = json.dumps(args_ser, ensure_ascii=False)
                    if key in {json.dumps(e[0], ensure_ascii=False) for e in result_map.get(sname, [])}: continue
                    result_map.setdefault(sname, []).append(entry)
    if not result_map:
        return None
    # prefer the function defined in chosen file; else any
    sname = None
    for cand in result_map:
        if cand in funcs:
            sname = cand; break
    if sname is None:
        sname = next(iter(result_map))
    func_node = funcs.get(sname)
    if func_node is None:
        # find in any file
        for f in pyfiles:
            s2 = open(os.path.join(pydir, f), encoding="utf-8").read()
            t2 = ast.parse(s2)
            fn = [n for n in t2.body if isinstance(n, ast.FunctionDef) and n.name == sname]
            if fn: func_node = fn[0]; break
    return (func_node, classes, result_map[sname], sname)


def gen_target(lang, func_node, classes, tests):
    if lang == "ts":
        return R.build_ts(func_node.name, func_node, classes, tests)
    if lang == "go":
        return R.build_go(func_node.name, func_node, classes, tests)
    return R.build_java(func_node.name, func_node, classes, tests)


def process_file(rel):
    lang = os.path.splitext(rel)[1].lstrip(".")
    prob_folder = None
    for part in rel.split("/"):
        if part.startswith("lc_"):
            prob_folder = part; break
    if not prob_folder:
        return {"rel": rel, "status": "fail", "note": "no problem folder"}
    sol_basename = os.path.basename(rel)
    res = analyze_prob(prob_folder, sol_basename)
    if res is None:
        # distinguish missing python ref vs no extractable tests
        if R.find_pydir(prob_folder) is None:
            return {"rel": rel, "status": "skip", "note": "no python ref"}
        return {"rel": rel, "status": "fail", "note": "no tests extracted"}
    func_node, classes, tests, sname = res
    if not tests:
        return {"rel": rel, "status": "fail", "note": "no tests extracted"}
    # limit to 4 cases
    tests = tests[:4]
    try:
        code = gen_target(lang, func_node, classes, tests)
    except Exception as e:
        return {"rel": rel, "status": "fail", "note": "transpile: %s" % e}
    target_path = os.path.join(R.BASE, rel)
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix="." + lang)
    os.close(fd)
    open(tmp, "w", encoding="utf-8").write(code)
    rc, out, err = R.verify(lang, tmp)
    if rc == 0 and "PASS" in out:
        # write to real file
        open(target_path, "w", encoding="utf-8").write(code)
        os.remove(tmp)
        return {"rel": rel, "status": "done_pass", "note": "ok"}
    else:
        note = "verify fail: " + (err or out)[:300].replace("\n", " ")
        os.remove(tmp)
        return {"rel": rel, "status": "fail", "note": note}


def append_progress(rec):
    with open(PROGRESS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    chunk_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    j = json.load(open(os.path.join(R.BASE, "_tools", "scale_chunks.json")))
    chunk = j["chunks"][chunk_idx]
    only = sys.argv[2] if len(sys.argv) > 2 else None
    for rel in chunk:
        if only and only not in rel:
            continue
        rec = process_file(rel)
        append_progress(rec)
        print(rec["status"], rec["rel"], rec.get("note", "")[:80])


if __name__ == "__main__":
    main()
