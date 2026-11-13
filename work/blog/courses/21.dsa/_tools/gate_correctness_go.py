#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正确性门禁(go): 用 Python 参考的 demo 输出作为基准, 比对 go 文件运行输出。
仅对 gate_all_go 判定为 ok 的文件做正确性校验。"""
import os, re, subprocess, sys, json, glob
from concurrent.futures import ThreadPoolExecutor

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
GO = "/usr/local/go1.26.5/bin/go"
PY = "/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3"
TIMEOUT = 30

def prob_id(rel):
    m = re.search(r"(lc_\d+)_", rel)
    return m.group(1) if m else None

def find_py_ref(pid):
    # pid 形如 lc_1; 用 lc_1_* 精确匹配(尾随下划线锚定), 避免 lc_1 误匹配 lc_10/lc_11
    pat = os.path.join(BASE, "python", "**", pid + "_*", "solution_*.py")
    return sorted(glob.glob(pat, recursive=True))

def run_capture(cmd, cwd=None, env=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT,
                           env=env or os.environ)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return -1, str(e)

def norm(s):
    # 去掉首尾空白, 压缩内部连续空白, 便于比较
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s

def check_one(rel):
    pid = prob_id(rel)
    if not pid:
        return rel, "no_pid"
    go_fp = os.path.join(BASE, rel)
    py_refs = find_py_ref(pid)
    if not py_refs:
        return rel, "no_py_ref"
    # 取第一个 python 参考的 demo 输出作为基准
    rc, py_out = run_capture([PY, py_refs[0]])
    if rc != 0:
        return rel, "py_run_err:" + py_out[:80]
    rc, go_out = run_capture([GO, "run", os.path.basename(go_fp)],
                             cwd=os.path.dirname(go_fp),
                             env={**os.environ, "GO111MODULE": "off"})
    if rc != 0:
        return rel, "go_run_err:" + go_out[:80]
    if norm(py_out) == norm(go_out):
        return rel, "CORRECT"
    return rel, "MISMATCH|py=%s|go=%s" % (norm(py_out)[:60], norm(go_out)[:60])

def main():
    ok = json.load(open(os.path.join(BASE, "_tools", "go_stubs_all.json")))
    # go_stubs_all 是 stub 列表; 这里需要从全量里取 ok。改为读 gate_all_go 产生的 ok 集合:
    # 重新用 gate_all_go 的 ok 判定较慢, 改为: 读全量 go, 跳过 stub 列表中的。
    stubs = set(ok)
    all_go = []
    for root, _, fs in os.walk(os.path.join(BASE, "go")):
        for f in fs:
            if f.endswith(".go") and f != "README.md":
                rel = os.path.relpath(os.path.join(root, f), BASE)
                if rel not in stubs:
                    all_go.append(rel)
    all_go.sort()
    print(f"ok go files to correctness-check = {len(all_go)}", file=sys.stderr)
    res = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for rel, st in ex.map(check_one, all_go):
            res[rel] = st
    from collections import Counter
    c = Counter(v.split(":")[0].split("|")[0] for v in res.values())
    print("CORRECTNESS:", dict(c), file=sys.stderr)
    mism = [rel for rel, st in res.items() if st.startswith("MISMATCH")]
    print(f"MISMATCH_count={len(mism)}", file=sys.stderr)
    for rel in mism[:30]:
        print("  ", rel, "->", res[rel][:120], file=sys.stderr)
    json.dump(res, open(os.path.join(BASE, "_tools", "go_correctness.json"), "w"),
              ensure_ascii=False, indent=0)
    print("written _tools/go_correctness.json", file=sys.stderr)

if __name__ == "__main__":
    main()
