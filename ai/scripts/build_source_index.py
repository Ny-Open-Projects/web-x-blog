#!/usr/bin/env python3
"""
扫描 work/source/<course>/ 下的机翻转写稿，洗掉文件名噪音，按「标题相似」分组，
产出 work/target/<course>/_INDEX.md 清单。

用法:
    python3 ai/scripts/build_source_index.py es 1.es-go
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # 仓库根
# 文件名噪音：课程推广邮箱/公众号、转写工具痕迹。
# 【】里可能是「海量资源：ubkz.com」「微信号：itcodeba」，一律整块吃掉；
# 半角括号里的「更多IT教程 微信xxxxxxx」同理。
NOISE = re.compile(
    r"【[^】]*】"                                   # 【海量资源：…】【微信号：…】
    r"|\[\d+\]"                                    # 文件名里的 [16] 这类序号
    r"|（\s*更多IT教程[^）]*）"                      # （更多IT教程 微信352852792）
    r"|\(更多IT教程[^)]*\)"
    r"|\b更多IT教程\b"
    r"|微信号[：:]?\s*[一-龥]{0,6}\s*\d+"
    r"|-\s*迅捷文字转语音-\d+zh"                     # -迅捷文字转语音-1760531260029zh
    r"|-?\s*迅捷文字转语音"
)
# 标题尾部的「第X部分」后缀
PART = re.compile(
    r"[\s]*[（(]\s*[一二三四五六七八九十]\s*[)）][\s]*$"
    r"|[\s]*[（(]\s*\d+\s*[)）][\s]*$"
    r"|\s+[（(][一二三四五六七八九十][)）]\s*$"
)
# 形如 11-2 / 10.10 / [10.4] / --10-10 的编号前缀，允许重复出现（课程目录有的写两遍）
NUM_PREFIX = re.compile(r"^[\s\[]*(\d+(?:\.\d+)*(?:[-–—]\d+)*)[\].)\s\-–—]*")


def clean_name(name: str):
    """从文件名里拆出 (编号, 标题)。"""
    base = name[: -len(".txt")] if name.endswith(".txt") else name
    base = NOISE.sub("", base)
    base = base.strip(" --–—_")

    nums, rest = [], base
    for _ in range(3):  # 最多吃三轮，覆盖 [10.10]--10-10 这种重复编号
        m = NUM_PREFIX.match(rest)
        if not m:
            break
        nums.append(m.group(1))
        rest = rest[m.end():]
    num = "-".join(nums)
    title = rest.rstrip(",，、 ").strip()
    return num, title


def group_key(title: str):
    """标题相似 -> 同一个 key：去掉尾部 (一)/(二) 之类的分组后缀。"""
    return PART.sub("", title).strip() or title


def main():
    course = sys.argv[1] if len(sys.argv) > 1 else "es"
    folder = sys.argv[2] if len(sys.argv) > 2 else "1.es-go"
    src = ROOT / "work" / "source" / folder
    if not src.is_dir():
        sys.exit(f"源目录不存在: {src}")

    items = []
    for f in sorted(src.glob("*.txt")):
        num, title = clean_name(f.name)
        text = f.read_text(encoding="utf-8", errors="ignore")
        items.append(
            {
                "file": f.name,
                "num": num,
                "title": title,
                "key": group_key(title),
                "bytes": len(text.encode("utf-8")),
                "chars": len(text),
            }
        )

    groups: dict[str, list] = {}
    for it in items:
        groups.setdefault(it["key"], []).append(it)

    out_dir = ROOT / "work" / "target" / course
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "_INDEX.md"
    single = [it for it in items if len(groups[it["key"]]) == 1]
    merged = {k: v for k, v in groups.items() if len(v) > 1}

    lines = [
        f"# {folder} 素材清单",
        "",
        f"- 总文件数：{len(items)}",
        f"- 独立标题（分组后）：{len(groups)}",
        f"- 需合并的相似标题组：{len(merged)}",
        f"  - 合并后文章数：{len(groups)}（一组一篇）",
        f"  - 直接单篇：{len(single)}",
        "",
        "## 相似标题分组（合并成一篇）",
        "",
    ]
    for key, g in merged.items():
        nums = ", ".join(x["num"] for x in sorted(g, key=lambda x: x["num"]))
        lines.append(f"- **{key}** ← {len(g)} 个文件 {nums}")
        for x in sorted(g, key=lambda x: x["num"]):
            lines.append(f"  - `{x['num']}` {x['title']}（{x['chars']} 字）")

    lines += ["", "## 全部清单", "", "| # | 编号 | 标题 | 字数 | 文件 |", "| --- | --- | --- | --- | --- |"]
    for i, it in enumerate(sorted(items, key=lambda x: x["num"]), 1):
        mark = " **（已合并）**" if len(groups[it["key"]]) > 1 else ""
        lines.append(f"| {i} | {it['num']} | {it['title']}{mark} | {it['chars']} | `{it['file'][:40]}…` |")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"清单已生成: {out}")

    # 进度文件：只在首次生成，之后由 agent 手工更新状态（重跑本脚本不会覆盖进度）
    prog = out_dir / "_PROGRESS.md"
    if not prog.exists():
        pl = [
            f"# {folder} → 博客 转换进度",
            "",
            "状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（导学、课程总结、本章未完结）",
            "**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**",
            "",
            "| 状态 | # | 组名 | 文件数 | 总字数 | 产出博客 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for i, (key, g) in enumerate(sorted(groups.items(), key=lambda kv: min(x["num"] for x in kv[1])), 1):
            nums = sorted(g, key=lambda x: x["num"])
            total = sum(x["chars"] for x in nums)
            st = "skip" if any(w in key for w in ("章节导学", "课程导学", "课程总结", "未完结")) else "pending"
            first_num = nums[0]["num"]
            pl.append(f"| {st} | {i} | {key} | {len(g)} | {total} | `{first_num}` 起 |")
        pl += [
            "",
            "## 节流约定（防 429）",
            "",
            "- 一次只推进**一组**，不并发、不一次读多个大文件",
            "- 每写完一篇 `sleep 45~60`；每 6 篇 `sleep 300`",
            "- 中断随时可从 `pending` 行续跑，不重跑全量",
            "",
            "## 已落盘产物",
            "",
        ]
        prog.write_text("\n".join(pl), encoding="utf-8")
        print(f"进度文件已生成: {prog}")

    print(f"文件 {len(items)} → 分组 {len(groups)}（合并 {len(merged)} 组）")
    for key, g in merged.items():
        print(f"  合并: {key} ({len(g)} 个)")


if __name__ == "__main__":
    main()
