#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用修复后门禁扫全部 go 文件，量化真实 stub 余量（含空壳 main 探测）。"""
import os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

BASE = "/Users/Wang/Code/webfault-ai/dsa"
GO = "/usr/local/go1.26.5/bin/go"
TIMEOUT = 30

def run_go(path):
    d = os.path.dirname(path)
    try:
        r = subprocess.run([GO, "run", os.path.basename(path)], cwd=d,
                           capture_output=True, text=True, timeout=TIMEOUT,
                           env={**os.environ, "GO111MODULE": "off"})
        return r.returncode
    except Exception:
        return -1

def classify(path):
    src = open(path, encoding="utf-8", errors="ignore").read()
    if "TODO: solution not implemented" in src:
        return path, "TODO_stub"
    m = re.search(r"func main\(\)\s*\{(.*?)\n\}", src, re.S)
    if m:
        body = re.sub(r"\b(?:fmt\.)?(?:Println|Print|Printf|println|print)\b", "", m.group(1))
        if not re.search(r"[A-Za-z_]\w*\s*\(", body):
            return path, "empty_main_stub"
    rc = run_go(path)
    return path, ("ok" if rc == 0 else "compile_run_fail")

def main():
    files = []
    for root, _, fs in os.walk(os.path.join(BASE, "go")):
        for f in fs:
            if f.endswith(".go") and f != "README.md":
                files.append(os.path.join(root, f))
    files.sort()
    print(f"total go files = {len(files)}", file=sys.stderr)
    res = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for path, cls in ex.map(classify, files):
            res[path] = cls
    from collections import Counter
    c = Counter(res.values())
    print("CLASS_COUNTS:", dict(c), file=sys.stderr)
    print(f"TODO_stub={c.get('TODO_stub',0)} empty_main_stub={c.get('empty_main_stub',0)} "
          f"compile_run_fail={c.get('compile_run_fail',0)} ok={c.get('ok',0)}", file=sys.stderr)
    # 输出 stub 列表供后续 rewrite
    stubs = [os.path.relpath(p, BASE) for p, cls in res.items()
             if cls in ("TODO_stub", "empty_main_stub", "compile_run_fail")]
    json.dump(stubs, open(os.path.join(BASE, "_tools", "go_stubs_all.json"), "w"),
              ensure_ascii=False, indent=0)
    print(f"stub_total={len(stubs)} -> written _tools/go_stubs_all.json", file=sys.stderr)

import json
if __name__ == "__main__":
    main()
