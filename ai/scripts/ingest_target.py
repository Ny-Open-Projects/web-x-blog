#!/usr/bin/env python3
"""把 work/target/<course>/ 下 agent 产出的博客搬进 hexo 的 source/_posts/。

用法:
    python3 ai/scripts/ingest_target.py kcna k8stop cka k8sprod   # 只校验+搬运
    python3 ai/scripts/ingest_target.py kcna --dry-run             # 只校验不搬

硬性规则:
1. 只搬 `work/target/<course>/` 下非 `_` 开头的 .md（_INDEX/_PROGRESS/_GLOSSARY 等忽略）
2. 文件名加课程前缀（kcna-10.2-…），避免 4 个课程编号撞车
3. front-matter 里的 title 若含 `: ` 必须加双引号，否则 hexo 的 YAML 解析会 fail fast
4. 校验不通过的**不搬**，直接列出来
"""
import sys
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "work" / "target"
POSTS = ROOT / "work" / "blog" / "source" / "_posts"

TITLE_RE = re.compile(r'^title:\s*(.*)$', re.M)


def check(text: str):
    """返回问题列表，空列表 = 合格。"""
    bad = []
    if not text.startswith("---\n"):
        bad.append("缺 front-matter 开头")
        return bad
    end = text.find("\n---", 3)
    if end < 0:
        bad.append("front-matter 没闭合")
        return bad
    fm = text[4:end]
    body = text[end + 4:]

    m = TITLE_RE.search(fm)
    if not m:
        bad.append("front-matter 没有 title")
    else:
        raw = m.group(1).strip()
        # 值已被引号包住 -> 里面的冒号合法；没包住又出现 ": " -> YAML mapping 解析失败
        if raw[:1] not in ('"', "'") and (": " in raw or raw.endswith(":")):
            bad.append(f"title 含冒号未加引号: {raw}")
        # 已被引号包住时，**内部不能再出现同种直引号**，否则会把外层提前闭合 ->
        # js-yaml 报 "Process failed" 整篇被 hexo 静默跳过（kcna-6.6 真实踩过）。
        if raw[:1] == '"' and '"' in raw[1:].rstrip('"'):
            bad.append("title 内部有直双引号，会提前闭合外层引号 → 改用「」或单引号")
        if raw[:1] == "'" and "'" in raw[1:].rstrip("'"):
            bad.append("title 内部有直单引号，会提前闭合外层引号")

    if "## 纲要" not in body:
        bad.append("缺 `## 纲要`")
    if "```mermaid" not in body:
        bad.append("缺 mermaid 图")
    if not re.search(r"^\|[\s:|-]+\|", body, re.M):
        bad.append("缺 markdown 表格")
    if "├──" not in body and "└──" not in body:
        bad.append("缺 ASCII 目录树")
    if not re.search(r"^#{2,3}\s*总结\s*$", body, re.M):
        bad.append("缺 总结 栏目")
    # 注：相关度/是否需要继续/代码是否可运行 这行是流水线 QA 脚手架，发布前会剥离，
    # 不再作为入库门禁（见 review_state.json R3/R5 的 Blocker B 决议）。
    # 先把 ``` 代码块内容整块剥掉，再找行首的 '''（真正的 markdown 围栏）。
    # 代码块内部的 `sh ''' ... '''`（Groovy/Jenkinsfile 合法语法）必须忽略，否则误报。
    stripped = re.sub(r"```.*?```", "", body, flags=re.S)
    if re.search(r"^\s*'''", stripped, re.M):
        bad.append("残留 ''' 围栏（行首）")
    n = body.count("\n```")
    if n % 2:
        bad.append(f"``` 围栏数奇数（{n}）")
    return bad


def main():
    args = [a for a in sys.argv[1:]]
    dry = "--dry-run" in args
    courses = [a for a in args if a != "--dry-run"]
    if not courses:
        print(__doc__)
        return 1

    total_ok = total_skip = 0
    for course in courses:
        src = TARGET / course
        if not src.is_dir():
            print(f"[跳过] 目录不存在 {src}")
            continue
        ok = skip = 0
        for f in sorted(src.glob("*.md")):
            if f.name.startswith("_"):
                continue
            text = f.read_text(encoding="utf-8")
            bad = check(text)
            if bad:
                skip += 1
                print(f"[不搬] {course}/{f.name}")
                for b in bad:
                    print(f"        - {b}")
                continue
            dst = POSTS / f"{course}-{f.name}"
            if dry:
                ok += 1
                continue
            if dst.exists():
                print(f"[覆盖] {dst.name}")
            shutil.copy2(f, dst)
            ok += 1
        total_ok += ok
        total_skip += skip
        print(f"[结果] {course}: 搬 {ok} 篇，拦下 {skip} 篇")
    print(f"\n合计: 搬 {total_ok}，拦下 {total_skip}（dry-run={dry}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
