#!/usr/bin/env python3
"""把 target 下所有课程 bash/shell/sh 代码块里残留的尖括号占位符 <word>
替换成 shell 变量 ${WORD}，避免运行时被 bash 当成输入重定向去读不存在的文件。

- 仅处理 ```bash/shell/sh 块（与 qc_articles 口径一致）。
- <none> 是 kubectl 真实输出值（如 STATUS: <none>），绝对不替换。
- 每个被修改的块首插入一行注释，提示先给占位变量赋值。
"""
import re
from pathlib import Path

ROOT = Path("/Users/Wang/Code/github/web-x-blog")
TARGET = ROOT / "work" / "target"
PAT = re.compile(r"<([A-Za-z][A-Za-z0-9_-]*)>")
FENCE = re.compile(r"^```(bash|shell|sh)\s*$")
END = re.compile(r"^```\s*$")
SKIP = {"none"}

total_files = 0
total_hits = 0
for f in sorted(TARGET.rglob("*.md")):
    lines = f.read_text(encoding="utf-8").splitlines()
    out = []
    inb = False
    hint_added = False
    changed = False
    for ln in lines:
        s = ln.rstrip("\n")
        if FENCE.match(s):
            inb = True
            hint_added = False
            out.append(ln)
            continue
        if END.match(s) and inb:
            inb = False
            out.append(ln)
            continue
        if inb and not s.strip().startswith("#"):
            def repl(m):
                tok = m.group(1)
                if tok.lower() in SKIP:
                    return m.group(0)
                return "${" + tok.upper().replace("-", "_") + "}"
            if PAT.search(s):
                s2 = PAT.sub(repl, s)
                hits = [t for t in PAT.findall(s) if t.lower() not in SKIP]
                if s2 != s and hits:
                    changed = True
                    total_hits += len(hits)
                    if not hint_added:
                        out.append('    # 执行前先给下面的占位变量赋值，如 NODE_NAME=node1，否则变量为空会导致命令行为不符合预期')
                        hint_added = True
                    s = s2
        out.append(s)
    if changed:
        f.write_text("\n".join(out) + "\n", encoding="utf-8")
        total_files += 1

print(f"fixed files={total_files} placeholder_hits={total_hits}")
