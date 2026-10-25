#!/usr/bin/env python3
"""数据课去 AI 味机械层：破折号收敛 + 引号统一为「」。围栏/行内代码感知，代码块内不动。"""
import re, glob, sys

D = "/Users/Wang/Code/github/web-x-blog/work/quant-site/content/data"

def polish_dash(ln):
    ln = re.sub(r'(\*\*[^*]+\*\*)\s*——', r'\1：', ln)   # **词**—— → **词**：
    ln = ln.replace('——', '，')                          # 其余 —— → ，
    return ln

def pair_quotes(ln):
    spans = []
    def mask(m):
        spans.append(m.group(0)); return f'\x00{len(spans)-1}\x00'
    masked = re.sub(r'`[^`]*`', mask, ln)                # 掩码行内代码
    masked = masked.replace('\u201c', '"').replace('\u201d', '"')  # 弯引号归一为 ascii
    out, open_ = [], True
    for ch in masked:
        if ch == '"':
            out.append('「' if open_ else '」'); open_ = not open_
        else:
            out.append(ch)
    masked = ''.join(out)
    return re.sub(r'\x00(\d+)\x00', lambda m: spans[int(m.group(1))], masked)

changed = 0
for f in sorted(glob.glob(D + "/*.md")):
    text = open(f, encoding="utf-8").read()
    lines = text.split("\n")
    in_code = False; out = []; fchanged = 0
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code; out.append(ln); continue
        if in_code:
            out.append(ln); continue
        n = polish_dash(ln); n = pair_quotes(n)
        if n != ln: fchanged += 1
        out.append(n)
    if fchanged:
        open(f, "w", encoding="utf-8").write("\n".join(out))
        changed += fchanged
        print(f"{f.split('/')[-1]}: {fchanged} 行")
print(f"合计修改 {changed} 行")
