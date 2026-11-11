#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Leader 独立复现：重跑 chunk2 进度里 status=skipped 且 rel 以 go/ 开头的文件。"""
import json, os, subprocess, sys

BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
CHK = os.path.join(BASE, "_tools", "remediate_check.py")
PY = "/Users/Wang/.workbuddy/binaries/python/envs/default/bin/python"

prog = json.load(open(os.path.join(BASE, "_tools", "remediate_progress_chunk2.json")))
skipped_go = [p["rel"] for p in prog if p.get("status") == "skipped" and p["rel"].startswith("go/")]
print(f"chunk2 skipped go 文件数 = {len(skipped_go)}", file=sys.stderr)

pass_n = fail_n = 0
fail_samples = []
for rel in skipped_go:
    fp = os.path.join(BASE, rel)
    rc = subprocess.run([PY, CHK, fp]).returncode
    if rc == 0:
        pass_n += 1
    else:
        fail_n += 1
        if len(fail_samples) < 20:
            fail_samples.append(rel)

print(f"RESULT: PASS={pass_n} FAIL={fail_n} total={len(skipped_go)}", file=sys.stderr)
if fail_samples:
    print("FAIL_SAMPLES:", file=sys.stderr)
    for s in fail_samples:
        print("  " + s, file=sys.stderr)
