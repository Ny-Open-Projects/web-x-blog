#!/usr/bin/env python3
"""数据课去 AI 味·语义层：删导航句(下一课/下一章)、删跨篇引用(见量化实战第X课)、去模板标签(小结/说明/量化迁移)。围栏感知。"""
import re, glob

D = "/Users/Wang/Code/github/web-x-blog/work/quant-site/content/data"

for f in sorted(glob.glob(D + "/*.md")):
    text = open(f, encoding="utf-8").read()
    lines = text.split("\n")
    in_code = False; out = []; n = 0
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code; out.append(ln); continue
        if in_code:
            out.append(ln); continue
        orig = ln
        ln = re.sub(r'下一[课章][^。\n]*。?', '', ln)                      # 删导航句
        ln = re.sub(r'（见量化实战第\s*\d+\s*课[^）\n]*）', '', ln)        # 删跨篇引用
        ln = re.sub(r'(^>+\s*)(小结|说明|量化迁移|注意|导读)[:：]\s*', r'\1', ln)  # 去模板标签(保留 >)
        ln = re.sub(r'[ \t]{2,}', ' ', ln).rstrip()                       # 收敛多余空白
        if ln != orig: n += 1
        out.append(ln)
    if n:
        open(f, "w", encoding="utf-8").write("\n".join(out))
        print(f"{f.split('/')[-1]}: {n} 行")
print("done")
