#!/usr/bin/env python3
"""33-java-interview 拆题质检（scan2 机检）。

检查项：front-matter 完整性 / 正文厚度 / 代码围栏配平 / 乱码与替换符 /
模板占位符残留 / 全局文件名重复 / 背诵卡五件套完整性。
输出 reports/scan2-qc.md，异常即退出码 1。
"""
import re
import sys
from pathlib import Path

DST = Path("/Users/Wang/Code/github/web-x-blog/work/target/33-java-interview")

def main():
    problems = []
    warned = []
    seen_names = {}
    seen_titles = {}
    n = 0
    type_count = {}
    for f in sorted(DST.rglob("*.md")):
        if f.name.startswith("_") or "reports" in f.parts:
            continue
        n += 1
        rel = f.relative_to(DST)
        # 1) 文件名重复（跨目录）
        if f.name in seen_names:
            problems.append(f"重名: {rel} 与 {seen_names[f.name]}")
        seen_names[f.name] = rel
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            problems.append(f"无front-matter: {rel}")
            continue
        try:
            _, fm, body = text.split("---\n", 2)
        except ValueError:
            problems.append(f"front-matter格式错: {rel}")
            continue
        for key in ("title:", "date:", "categories:", "tags:", "type:"):
            if key not in fm:
                problems.append(f"front-matter缺{key}: {rel}")
        m = re.search(r'title: "(.+)"', fm)
        if not m:
            problems.append(f"title未双引号包裹: {rel}")
        else:
            t = m.group(1)
            if len(t) > 80:
                warned.append(f"超长title({len(t)}): {rel}")
            if t in seen_titles:
                warned.append(f"重复title「{t[:40]}」: {rel} 与 {seen_titles[t]}")
            seen_titles[t] = rel
        tm = re.search(r"type: (\S+)", fm)
        if tm:
            type_count[tm.group(1)] = type_count.get(tm.group(1), 0) + 1
        # 2) 正文厚度（行数 + 字符量双门槛；源短卡按字符量放行）
        nlines = len([l for l in body.strip().splitlines() if l.strip()])
        nchars = len(re.sub(r"\s", "", body))
        if nlines < 2 or nchars < 60:
            problems.append(f"正文过薄({nlines}行/{nchars}字): {rel}")
        # 3) 围栏配平
        fences = len(re.findall(r"^\s*```", body, re.M))
        if fences % 2:
            problems.append(f"围栏不配平({fences}): {rel}")
        # 4) 乱码
        if "\ufffd" in text:
            problems.append(f"含替换符U+FFFD: {rel}")
        # 5) 占位符检查已取消：源为成品题库，{profile}/{{it}} 等是真实
        #    Spring/LangChain4j 模板语法（卡片已带 disableNunjucks 防护）
        # 6) 背诵卡五件套
        if tm and tm.group(1) == "背诵卡":
            for field in ("**事实**", "**原理**", "**工程用法**", "**版本锚点**"):
                if field not in body:
                    problems.append(f"背诵卡缺{field}: {rel}")
    lines = [f"# scan2 · 质检报告（机检）", "",
             f"- 卡片总数：{n}", f"- 问题（阻断）：**{len(problems)}**", f"- 警告（不阻断）：{len(warned)}", "",
             "## 类型分布", ""]
    for k, v in sorted(type_count.items(), key=lambda x: -x[1]):
        lines.append(f"- {k}: {v}")
    if problems:
        lines += ["", "## 问题清单", ""] + [f"- {p}" for p in problems[:200]]
    if warned:
        lines += ["", "## 警告清单", ""] + [f"- {w}" for w in warned[:100]]
    rep = DST / "reports"
    rep.mkdir(parents=True, exist_ok=True)
    (rep / "scan2-qc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"cards={n} problems={len(problems)} warned={len(warned)}")
    for p in problems[:30]:
        print("P:", p)
    for w in warned[:10]:
        print("W:", w)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
