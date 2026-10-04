#!/usr/bin/env python3
"""抽取 markdown 里所有 ```bash 块，逐个跑 `bash -n` 语法校验。

用法:
    python3 ai/scripts/check_bash_blocks.py work/target/kcna/xxx.md
    python3 ai/scripts/check_bash_blocks.py work/target/kcna/          # 整个目录

背景：入库校验 ingest_target.py 只管格式契约（纲要/mermaid/表格/目录树/总结），
**不管 bash 块能不能跑**。标着 ```bash 却 `bash -n` 报错的块会原样进站，读者照抄就出错。
这类问题靠人工扫会漏，必须脚本化。

常见不合格形态（都真实出现过）：
- 尖括号占位符 `<pod>` `<svc>` -> bash -n 报 syntax error（应改 $POD / $SVC）
- SQL 语句塞进 ```bash 块          -> 应改 ```sql
- ASCII 目录树塞进 ```bash 块      -> 应改 ```text
- 命令后跟裸 `# 说明`              -> 说明要单独提行
- 复合命令（for/while）引号没闭合、续行符 \\ 后有空格

注意：heredoc 定界符 `<<'EOF'` 和 kubectl 输出里的 `<none>` 是**合法的**，不算占位符，别误改。
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FENCE = re.compile(r"^```(bash|sh|shell)\s*$", re.M)


def blocks(text: str):
    """返回 (语言, 内容, 起始行号) 列表。"""
    out = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^```(bash|sh|shell)\s*$", lines[i])
        if not m:
            i += 1
            continue
        lang, start = m.group(1), i + 1
        j = i + 1
        while j < len(lines) and not re.match(r"^```\s*$", lines[j]):
            j += 1
        out.append((lang, "\n".join(lines[i + 1:j]), start))
        i = j + 1
    return out


def check_file(path: Path):
    text = path.read_text(encoding="utf-8")
    bs = blocks(text)
    if not bs:
        return 0, []
    fails = []
    for idx, (lang, code, start) in enumerate(bs, 1):
        if not code.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".sh", delete=False,
                                         encoding="utf-8") as f:
            f.write(code + "\n")
            tmp = f.name
        r = subprocess.run(["bash", "-n", tmp], capture_output=True, text=True)
        Path(tmp).unlink(missing_ok=True)
        if r.returncode != 0:
            err = (r.stderr or "").strip().split("\n")[0]
            fails.append((idx, start, err))
    return len(bs), fails


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    target = Path(sys.argv[1])
    files = ([target] if target.is_file()
             else sorted(p for p in target.glob("*.md") if not p.name.startswith("_")))
    total_blocks = total_fails = 0
    bad_files = 0
    for p in files:
        n, fails = check_file(p)
        total_blocks += n
        if fails:
            bad_files += 1
            print(f"[FAIL] {p.name}  ({n} 个块)")
            for idx, start, err in fails:
                print(f"       块{idx} @第{start}行: {err}")
        total_fails += len(fails)
    print(f"\n文件 {len(files)} 个，bash 块 {total_blocks} 个，"
          f"失败 {total_fails} 处，涉及文件 {bad_files} 个")
    return 1 if total_fails else 0


if __name__ == "__main__":
    sys.exit(main())
