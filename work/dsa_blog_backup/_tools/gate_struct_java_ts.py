#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""结构扫描(java/ts): 编译/运行 + stub 探测, 不做 python 比对(oracle 无关, 可信)。"""
import os, sys, json, subprocess
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import remediate_check as RC

def one(rel):
    fp = os.path.join(RC.BASE, rel)
    ext = os.path.splitext(rel)[1]
    if ext == ".java":
        rc, out = RC.check_java(fp)
    else:
        rc, out = RC.check_ts(fp)
    # check_java/ts 在 rc==0 时 out 是运行输出(可能空), 用 out 是否含 STUB 标记判定
    if rc != 0:
        return rel, "FAIL:" + out[:60]
    if "STUB" in out:
        return rel, "STUB"
    return rel, "ok"

def main():
    lang = sys.argv[1]
    files = []
    for root, _, fs in os.walk(os.path.join(RC.BASE, lang)):
        for f in fs:
            if f.endswith(".%s" % lang) and f != "README.md":
                files.append(os.path.relpath(os.path.join(root, f), RC.BASE))
    files.sort()
    print(f"{lang} total={len(files)}", file=sys.stderr)
    res = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for rel, st in ex.map(one, files):
            res[rel] = st
    from collections import Counter
    c = Counter(res.values())
    print(f"STRUCT({lang}):", dict(c), file=sys.stderr)
    json.dump(res, open(os.path.join(RC.BASE, "_tools", "%s_struct.json" % lang), "w"),
              ensure_ascii=False, indent=0)
    print(f"written _tools/{lang}_struct.json", file=sys.stderr)

if __name__ == "__main__":
    main()
