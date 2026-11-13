#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正确性门禁(java/ts): 与 Python 参考 demo 输出比对。"""
import os, re, subprocess, sys, json, glob
from concurrent.futures import ThreadPoolExecutor

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"
PY = "/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3"
TIMEOUT = 30

def prob_id(rel):
    m = re.search(r"(lc_\d+)_", rel)
    return m.group(1) if m else None

def find_py_ref(pid):
    # pid 形如 lc_1; 用 lc_1_* 精确匹配(尾随下划线锚定), 避免 lc_1 误匹配 lc_10/lc_11
    return sorted(glob.glob(os.path.join(BASE, "python", "**", pid + "_*", "solution_*.py"), recursive=True))

def run_capture(cmd, cwd=None, env=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT, env=env or os.environ)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return -1, str(e)

def norm(s):
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s

def py_expected(pid):
    refs = find_py_ref(pid)
    if not refs:
        return None, "no_py_ref"
    rc, out = run_capture([PY, refs[0]])
    if rc != 0:
        return None, "py_err"
    return norm(out), None

def check_java(rel):
    pid = prob_id(rel)
    exp, err = py_expected(pid)
    if err:
        return rel, "SKIP:" + err
    fp = os.path.join(BASE, rel)
    src = open(fp, encoding="utf-8", errors="ignore").read()
    m = re.search(r"(?:public\s+)?class\s+(\w+)", src)
    if not m:
        return rel, "no_class"
    cls = m.group(1)
    import tempfile
    tmp = tempfile.mkdtemp()
    rc, _ = run_capture([JAVAC, "-d", tmp, fp])
    if rc != 0:
        return rel, "compile_fail"
    rc, out = run_capture([JAVA, "-cp", tmp, "com.webfault.dsa." + cls])
    if rc != 0:
        return rel, "run_fail"
    return rel, ("CORRECT" if norm(out) == exp else "MISMATCH|go=%s" % norm(out)[:60])

def check_ts(rel):
    pid = prob_id(rel)
    exp, err = py_expected(pid)
    if err:
        return rel, "SKIP:" + err
    fp = os.path.join(BASE, rel)
    rc, out = run_capture([NODE, "--experimental-strip-types", "-e",
        "import('%s').then(m=>m.demo()).catch(e=>{console.error(e);process.exit(1)})" % fp.replace("\\","/")])
    if rc != 0:
        # 退回直接运行
        rc, out = run_capture([NODE, "--experimental-strip-types", fp])
        if rc != 0:
            return rel, "run_fail"
    return rel, ("CORRECT" if norm(out) == exp else "MISMATCH|ts=%s" % norm(out)[:60])

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "java"
    files = []
    for root, _, fs in os.walk(os.path.join(BASE, target)):
        for f in fs:
            if f.endswith(".%s" % ("java" if target=="java" else "ts")) and f != "README.md":
                files.append(os.path.relpath(os.path.join(root, f), BASE))
    files.sort()
    print(f"{target} files = {len(files)}", file=sys.stderr)
    fn = check_java if target == "java" else check_ts
    res = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for rel, st in ex.map(fn, files):
            res[rel] = st
    from collections import Counter
    c = Counter(v.split(":")[0].split("|")[0] for v in res.values())
    print("CORRECTNESS(%s):" % target, dict(c), file=sys.stderr)
    json.dump(res, open(os.path.join(BASE, "_tools", "%s_correctness.json" % target), "w"), ensure_ascii=False, indent=0)
    print("written _tools/%s_correctness.json" % target, file=sys.stderr)

if __name__ == "__main__":
    main()
