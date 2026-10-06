#!/usr/bin/env python3
# 监控一波博客 agent 的产出进度（保活用，不耗额度）
import re, time, subprocess, sys

ROOT = '/Users/Wang/Code/github/web-x-blog'
TARGETS = {'campus': 78, 'storage': 100, 'apm': 94}  # 波次目标落盘数（Wave5 完成后基线）
MAX_SEC = 540  # 最长保活 9 分钟


def done_counts():
    out = subprocess.run(['python3', 'ai/scripts/blog_coverage.py'],
                         cwd=ROOT, capture_output=True, text=True).stdout
    res = {}
    cur = None
    for line in out.splitlines():
        if line.startswith('=== '):
            cur = line.split('===')[1].strip().split(' ')[0]  # campus/storage/apm
        if 'done=' in line and cur:
            m = re.search(r'done=(\d+)', line)
            if m:
                res[cur] = int(m.group(1))
    return res


start = time.time()
while time.time() - start < MAX_SEC:
    d = done_counts()
    elapsed = int(time.time() - start)
    line = f'[{elapsed}s] ' + ', '.join(f'{k}={d.get(k, 0)}/{TARGETS[k]}' for k in TARGETS)
    print(line, flush=True)
    if all(d.get(k, 0) >= TARGETS[k] for k in TARGETS):
        print('>>> WAVE COMPLETE', flush=True)
        break
    time.sleep(30)
else:
    print('>>> TIMEOUT (9min) 未全部达标，部分仍在跑', flush=True)
