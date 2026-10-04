#!/usr/bin/env python3
"""文章机械质检：机翻术语残留 + 格式要素完整性 + 疑似注水。

这是给「专业复核」提供**机械证据**的：人工/agent 评审容易凭感觉，
脚本能给出全量数字。

用法:
    python3 ai/scripts/qc_articles.py work/target/k8stop
    python3 ai/scripts/qc_articles.py work/blog/source/_posts --top 20
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# 机翻/语音转写的错误术语 -> 正确写法（抽自 ai/memory/*-MT-GLOSSARY.md）
MT_BAD = [
    (r"加\s*PC|加\s*Pc|假\s*PC", "gRPC"),
    (r"\binteress\b|engresh|incress|ingressive|integress|ineress", "ingress"),
    (r"\bcontrollermanager\b|controlmanager|controller\s*manger", "kube-controller-manager"),
    (r"\bconfimap\b|configmep|\bcmaps\b", "ConfigMap"),
    (r"\bkbox\b|\bkboss\b|\bk八x\b|\bk8x\b|kubx", "Kubernetes"),
    (r"\bATTP\b|\bALLP\b|\bAGTPS\b|\bAPTS\b", "HTTP/HTTPS"),
    (r"服务帐号", "ServiceAccount"),
    (r"八零端口|八连端口", "80 端口"),
    (r"四十三端口", "443 端口"),
    (r"边卡车|副车", "sidecar"),
    (r"污辱", "污点容忍(toletration)"),
    (r"\bhostaliases\b", "hostAliases"),
    (r"云原生容器编排工具 k8s集群", "Kubernetes 集群"),
]

# 必须在正文里出现的要素 -> 从 SKILL.md 格式契约来
ESSENTIAL = {
    "纲要":       lambda t: "## 纲要" in t,
    "API 速览":   lambda t: "## API 速览" in t,
    "总结":       lambda t: "### 总结" in t or "## 总结" in t,
    "mermaid":    lambda t: "```mermaid" in t,
    "markdown表格": lambda t: bool(re.search(r"^\|.*\|.*\|", t, re.M)),
    "ASCII目录树": lambda t: "├──" in t or "└──" in t,
    "代码块":     lambda t: bool(re.search(r"^```(bash|yaml|json|go|text)\b", t, re.M)),
}

NOISE = r"^(微信|公众号|扫码|关注|更多|二维码|itcodeba|微信号)"


def analyse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    # front-matter
    fm_end = None
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end = i
                break
    fm = "\n".join(lines[1:fm_end]) if fm_end else ""
    body = "\n".join(lines[fm_end + 1:]) if fm_end else text

    miss = [k for k, fn in ESSENTIAL.items() if not fn(body)]
    hits = []
    for pat, right in MT_BAD:
        m = re.search(pat, body)
        if m:
            hits.append({"found": m.group(0), "should": right})

    # 围栏成对
    fences = len(re.findall(r"^```", text, re.M))
    unb = fences % 2 != 0

    # 尖括号占位符 —— 只认 ```bash/shell/sh 块里的。
    # ```text 块里写 `<res>` 是说明性的，不是给读者复制执行的，不算问题。
    placeholders = []
    open_line = lines if fm_end is None else lines[fm_end + 1:]
    inb = False
    for ln in open_line:
        s = ln.rstrip("\n")
        if re.match(r"^```(bash|shell|sh)\s*$", s):
            inb = True
            continue
        if re.match(r"^```\s*$", s) and inb:
            inb = False
            continue
        if inb and not s.strip().startswith("#"):
            # 在 bash 块里，任何独立的 <word> 占位符（含连字符/赋值式 POD=<pod>）
            # 都会让命令运行时读不存在的文件。真实重定向是 `> file` / `< file`（尖括号后带空格），
            # 不会命中此正则（要求 < 紧跟字母、以 > 闭合）。
            m = re.search(r"<[A-Za-z][A-Za-z0-9_-]*>", s)
            if m:
                placeholders.append(m.group(0).strip()[:70])

    return {
        "file": path.name,
        "lines": len(lines),
        "code_blocks": len(re.findall(r"^```(bash|yaml|json|go|text)\b", text, re.M)),
        "missing": miss,
        "mt_residue": hits,
        "front_matter_ok": fm_end is not None and "title:" in fm and "categories:" in fm,
        "title_has_raw_quote": bool(re.search(r'^title:.*(?<!")"(?! *$)(?!.*").*(?<!")"', fm, re.M)),
        "odd_fence": unb,
        "placeholder": placeholders[:3],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()

    d = Path(args.dir)
    files = sorted(d.glob("*.md"))
    files = [f for f in files if not f.name.startswith("_")]
    res = [analyse(f) for f in files]

    total = len(res)
    no_fm = [r for r in res if not r["front_matter_ok"]]
    odd = [r for r in res if r["odd_fence"]]
    rawq = [r for r in res if r["title_has_raw_quote"]]
    mt = [r for r in res if r["mt_residue"]]
    ph = [r for r in res if r["placeholder"]]
    missmap = {}
    for r in res:
        for m in r["missing"]:
            missmap.setdefault(m, []).append(r["file"])

    print(f"扫描 {total} 篇 ({d})")
    print(f"  front-matter 不完整        : {len(no_fm)}")
    print(f"  代码围栏不配对             : {len(odd)}")
    print(f"  title 含裸双引号(会炸 yaml): {len(rawq)}")
    print(f"  有机翻术语残留             : {len(mt)}")
    print(f"  bash 尖括号占位符          : {len(ph)}")
    print("  缺要素统计:")
    for k, v in sorted(missmap.items(), key=lambda x: -len(x[1])):
        print(f"    {k:<14} {len(v)} 篇")
    if not missmap:
        print("    （无缺失，全要素齐备）")

    if ph:
        print("\n  [占位符样例]")
        for r in ph[:5]:
            print(f"    {r['file'][:60]}  {r['placeholder']}")
    if mt:
        print("\n  [术语残留样例]")
        for r in mt[:5]:
            print(f"    {r['file'][:55]}  {r['mt_residue']}")

    avg = sum(r["lines"] for r in res) / max(total, 1)
    short = sorted(res, key=lambda r: r["lines"])[:args.top]
    print(f"\n  平均行数 {avg:.0f} | 最短 {short[0]['lines']} 行")
    print("  [最短的几篇]")
    for r in short[:8]:
        flag = ("缺:" + ",".join(r["missing"])) if r["missing"] else "齐"
        print(f"    {r['lines']:>4} 行  {r['file'][:52]:<54} {flag}")

    if args.json:
        print(json.dumps(res, ensure_ascii=False))
    # 门禁必须覆盖真实出过的两类问题：机翻术语残留 + bash 尖括号占位符，
    # 否则自动卡口对这些命中直接返回 0（放行），等于没卡。
    return 1 if (no_fm or odd or rawq or mt or ph) else 0


if __name__ == "__main__":
    sys.exit(main())
