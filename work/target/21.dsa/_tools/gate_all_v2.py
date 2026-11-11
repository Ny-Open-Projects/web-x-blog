#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 v2 权威门禁(正确性驱动)全量审计某语言。subprocess 调用 remediate_gate.py, 并行。"""
import os, sys, json, subprocess
from concurrent.futures import ThreadPoolExecutor

BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
PY = "/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3"
GATE = os.path.join(BASE, "_tools", "remediate_gate.py")

def one(rel):
    fp = os.path.join(BASE, rel)
    rc = subprocess.run([PY, GATE, fp], capture_output=True, text=True, timeout=60).returncode
    return rel, ("PASS" if rc == 0 else "FAIL")

def main():
    lang = sys.argv[1]
    files = []
    for root, _, fs in os.walk(os.path.join(BASE, lang)):
        for f in fs:
            if f.endswith(".%s" % lang) and f != "README.md":
                files.append(os.path.relpath(os.path.join(root, f), BASE))
    files.sort()
    print(f"{lang} total={len(files)}", file=sys.stderr)
    res = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for rel, st in ex.map(one, files):
            res[rel] = st
    from collections import Counter
    c = Counter(res.values())
    print(f"V2({lang}):", dict(c), file=sys.stderr)
    json.dump(res, open(os.path.join(BASE, "_tools", "%s_v2_audit.json" % lang), "w"),
              ensure_ascii=False, indent=0)
    print(f"written _tools/{lang}_v2_audit.json", file=sys.stderr)

if __name__ == "__main__":
    main()
