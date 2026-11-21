#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v5 结构改造工具：把 v4 卡重排为「速记区（上）+ 原理区（下）」，**单文件**。

设计约定（2026-10-05 定稿）
─────────────────────────────────────────
上半 · 速记区（考前 3 分钟只看这里）
    ## 30 秒版          ← 新增（若提供）
    ## 面试怎么答        ← 原有段，上移

下半 · 原理区（要搞懂再往下）
    ## 先说结论
    ## 完整代码
    ## 逐行讲透
    ## 实测验证
    ## 原文哪里错了
    ## 面试官可能接着问   ← 原有段，保持在下

硬约束
─────────────────────────────────────────
1. **除段落顺序外，不改动任何一个字** —— 可用「逐字 diff」验证（见 --verify）
2. 文件名 / 编号 / H1 / `> 来源：` 行 **一律不动**
3. 七段一个都不能少，缺段即报错退出（不做"尽力而为"）

用法
─────────────────────────────────────────
  # 试运行（输出到 stdout 之外的临时文件，不动原卡）
  python3 _pipeline/restructure-v5.py target/go/1253-xxx.md --out /tmp/pilot.md

  # 带 30 秒版（单独一个小文件，只有正文，不要标题）
  python3 _pipeline/restructure-v5.py target/go/1253-xxx.md \
        --seconds30 _pipeline/speed30/1253.md --out /tmp/pilot.md

  # 逐字校验：确认除顺序外没改内容
  python3 _pipeline/restructure-v5.py target/go/1253-xxx.md --out /tmp/pilot.md --verify

  # 就地改（**会先自动备份到 _work/_v5-backup/**）
  python3 _pipeline/restructure-v5.py target/go/1253-xxx.md --inplace
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent

# 上半：速记区（按此顺序）
TOP_SECTIONS = ["面试怎么答"]
# 下半：原理区（按此顺序）
BOTTOM_SECTIONS = ["先说结论", "完整代码", "逐行讲透", "实测验证", "原文哪里错了", "面试官可能接着问"]

SPEED_HEADER = "# 🎯 速记区（考前只看这里）"
DEEP_HEADER = "# 📖 原理区（要搞懂原理再往下）"
DIVIDER = "\n---\n"


def split_card(text: str):
    """把卡拆成 (头部, {段名: 段文本})。段名 = `## ` 后面的标题原文。"""
    lines = text.split("\n")
    # 找第一个 `## ` 的位置
    idxs = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    if not idxs:
        raise SystemExit("✗ 没有找到任何 `## ` 段")
    head = "\n".join(lines[: idxs[0]]).rstrip("\n")
    secs = {}
    order = []
    for j, start in enumerate(idxs):
        end = idxs[j + 1] if j + 1 < len(idxs) else len(lines)
        title = lines[start][3:].strip()
        body = "\n".join(lines[start:end]).rstrip("\n")
        secs[title] = body
        order.append(title)
    return head, secs, order


def build(head: str, secs: dict, seconds30: str | None) -> str:
    # --- 硬约束：七段必须齐全 ---
    need = TOP_SECTIONS + BOTTOM_SECTIONS
    missing = [s for s in need if s not in secs]
    if missing:
        raise SystemExit(f"✗ 缺段，拒绝改造：{missing}\n  实际段：{list(secs)}")
    extra = [s for s in secs if s not in need]
    if extra:
        print(f"  ⚠ 发现了计划外的段（按原样追加到原理区末尾）：{extra}", file=sys.stderr)

    parts = [head.rstrip("\n"), ""]

    # ── 上半 速记区 ──
    parts += [SPEED_HEADER, ""]
    if seconds30:
        parts += ["## 30 秒版", "", seconds30.strip(), ""]
    for s in TOP_SECTIONS:
        parts += [secs[s], ""]

    # ── 分隔 ──
    parts += [DIVIDER.strip("\n"), ""]

    # ── 下半 原理区 ──
    parts += [DEEP_HEADER, ""]
    for s in BOTTOM_SECTIONS:
        parts += [secs[s], ""]
    for s in extra:
        parts += [secs[s], ""]

    return "\n".join(parts).rstrip("\n") + "\n"


def strip_trailing_scaffold(body: str) -> str:
    """剥掉段尾被"吃掉"的脚手架行（分隔线 / 区块标题 / 空行）。

    为什么需要：`split_card` 按 `## ` 切段，所以"上一段的尾巴"会包含
    我插入的 `---` 与 `# 📖 原理区…`。校验时要把它们去掉才能逐字比对。
    **只从尾部剥**，不会碰到正文中间任何内容。
    """
    lines = body.split("\n")
    while lines:
        t = lines[-1].strip()
        if t == "" or t == "---" or t in (SPEED_HEADER, DEEP_HEADER):
            lines.pop()
        else:
            break
    return "\n".join(lines)


def verify_content_identical(old: str, new: str) -> bool:
    """除顺序外内容是否一字未改：按段比对（段名 + 段正文逐字相等）。"""
    _, s_old, _ = split_card(old)
    _, s_new, _ = split_card(new)
    s_new = {k: strip_trailing_scaffold(v) for k, v in s_new.items()}
    if set(s_old) - {"30 秒版"} != set(s_new) - {"30 秒版"}:
        print("  ✗ 段集合不一致")
        print("    旧:", sorted(s_old))
        print("    新:", sorted(s_new))
        return False
    ok = True
    for k in sorted(set(s_old) - {"30 秒版"}):
        if s_old[k] != s_new[k]:
            print(f"  ✗ 段内容被改动：{k}  (旧 {len(s_old[k])} 字 / 新 {len(s_new[k])} 字)")
            ok = False
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("card")
    ap.add_argument("--seconds30", help="30 秒版正文文件（纯正文，无标题）")
    ap.add_argument("--out", help="输出到该路径（不就地改）")
    ap.add_argument("--inplace", action="store_true", help="就地改，自动备份")
    ap.add_argument("--verify", action="store_true", help="校验除顺序外内容未变")
    ap.add_argument("--refresh", action="store_true", help="若已是 v5 卡：先从 _work/_v5-backup/ 还原再改造（防二次加壳）")
    args = ap.parse_args()

    p = Path(args.card)
    if not p.exists():
        p = PROJ / args.card
    old = p.read_text(encoding="utf-8")

    # ── 防「二次加壳」（2026-10-05，v5-A 踩到并规避，这里做成硬保护）──
    # 症状：改了 speed30/*.md 之后直接重跑 --inplace，会把「速记区」再套一层，
    #       变成 2 个速记区 + 2 个 30 秒版，而且 --verify 检不出来（旧卡也有 30 秒版，比对能过）。
    # 根因：脚本不区分「v4 原卡」与「已改造的 v5 卡」。
    bak = PROJ / "_work" / "_v5-backup" / p.name
    if SPEED_HEADER in old:
        if args.refresh and bak.exists():
            old = bak.read_text(encoding="utf-8")
            print(f"  ⓘ --refresh：已从备份还原为 v4 原卡再改造（{bak.name}）")
        else:
            raise SystemExit(
                "✗ 这张卡已经是 v5（含「🎯 速记区」），拒绝重复加壳。\n"
                f"  要重新生成 30 秒版 → 加 --refresh（会先从 _work/_v5-backup/{p.name} 还原）\n"
                f"  备份不存在 → 手工处理，别硬跑。"
            )

    s30 = None
    if args.seconds30:
        s30 = Path(args.seconds30).read_text(encoding="utf-8")

    head, secs, _ = split_card(old)
    new = build(head, secs, s30)

    if args.verify:
        ok = verify_content_identical(old, new)
        print("  ✓ 除顺序外内容一字未改" if ok else "  ✗ 校验失败")
        if not ok:
            sys.exit(1)

    if args.inplace:
        bak = PROJ / "_work" / "_v5-backup" / p.name
        bak.parent.mkdir(parents=True, exist_ok=True)
        # 🔴 2026-10-05 修：--refresh 模式下 **绝对不能覆盖备份**
        #    备份里放的是 v4 原件（唯一退路）。refresh 时 old 就是从备份读的，
        #    此时再 shutil.copy2(p, bak) 会把「当前 v5 卡」写进备份 → v4 原件永久丢失。
        #    （lead 自己在 916 上踩到过一次，已重建）
        if args.refresh and bak.exists():
            print(f"  ⓘ --refresh 模式：保留原备份不动（{bak.name}）")
        else:
            shutil.copy2(p, bak)
        p.write_text(new, encoding="utf-8")
        print(f"  ✓ 已就地改（备份 {bak.relative_to(PROJ)}）")
    elif args.out:
        Path(args.out).write_text(new, encoding="utf-8")
        print(f"  ✓ 输出 {args.out}")
    else:
        sys.stdout.write(new)


if __name__ == "__main__":
    main()
