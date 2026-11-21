#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v5 全量体检（lead 独立核验用，不信 worker 自报）

对每一张已改造的卡 + 它的备份，做四件事：
  ① 逐段比对：除顺序外内容一字未改（复用 restructure-v5 的判定）
  ② 结构计数：速记区 / 30 秒版 / 原理区 各恰好 1（防二次加壳）
  ③ 30 秒版数字回卡：抽出所有 ≥3 位数字与小数，逐条回【备份原卡】里找
  ④ 元信息未动：H1 / `> 来源：` 行 与备份逐字一致

用法：python3 _pipeline/v5-audit.py
"""
import re
import sys
from pathlib import Path
from importlib.machinery import SourceFileLoader

PROJ = Path(__file__).resolve().parent.parent
R5 = SourceFileLoader("r5", str(PROJ / "_pipeline" / "restructure-v5.py")).load_module()

TARGET = PROJ / "target" / "go"
BAK = PROJ / "_work" / "_v5-backup"


def head_lines(text: str):
    """取 H1 与所有 `> ` 开头的元信息行"""
    out = []
    for ln in text.split("\n"):
        if ln.startswith("# ") or ln.startswith("> "):
            out.append(ln.rstrip())
        elif out and not ln.strip():
            break
    return out


def nums_in(text: str):
    """抽出所有数字 token（不含分隔符）。

    ⚠️ 2026-10-05 两次修正的教训：
      ① 原始版：`\\d+(?:\\.\\d+)?` —— 会把原卡的 `2 569 168 B`（空格千分位）漏判 → **假阳性**
      ② 第一版修正：`\\d[\\d ,]*\\d` —— **过贪**，把 `0.79 ms 2.4` 这类**跨数字的串**吃成 `792` → **更多假阳性**
      ③ 现在这版：**30 秒版侧**只抽纯数字；**原卡侧**另建"去千分位"集合（见 norm_nums）。
    """
    return set(re.findall(r"\d+(?:\.\d+)?", text))


def norm_nums(text: str):
    """原卡侧的数字集合：纯数字 + **千分位展开形式**。

    只对真正的千分位模式（`1-3位数字 + (分隔符+3位数字)+`）做展开，
    不会像 `\\d[\\d ,]*\\d` 那样把相邻的独立数字黏在一起。
    """
    out = set(re.findall(r"\d+(?:\.\d+)?", text))
    for m in re.findall(r"\d{1,3}(?:[ ,]\d{3})+", text):
        out.add(re.sub(r"[ ,]", "", m))
    return out


# ── 2026-10-05 第三次修正：**四舍五入不该算"编造"** ──────────────────────
# 前两版把「速记区为了好记做了四舍五入」误判成编造，每轮固定冒 2 条假阳性：
#     1301：速记区 `98.6 ~ 121.7 ns`   原卡 `98.63 ~ 121.7`   ← 98.63 舍成 98.6
#     1332：速记区 `B/op ≈270~271 MB`  原卡 `≈271.3 MB`       ← 271.3 截成 271
# 判定：这**语义忠实**（速记区本就允许写约数），不该报错，但必须**单独计数**，
#      免得把真正的编造混进来。真正的编造仍然会漏不过去——
#      例：速记区写 `999.9`、原卡只有 `12.3` → 没有以 `999.9` 开头的原数字 → 仍判 MISS。
def num_ok(n: str, old_nums: set) -> bool:
    """速记区数字 n 能在原卡找到吗？

    三种合法关系（其余一律判 FAIL）：
      ① 精确命中
      ② **小数位四舍五入**：原卡 `98.63` → 速记区 `98.6`
      ③ **同量级缩放后四舍五入**：原卡 `271300000`（B）→ 速记区 `271`（MB，= 271.3 MB）

    ⚠️ 为什么不用「前缀匹配」（第一版写法，被自测打回）：
       前缀匹配会把 `256 → 25` 判成合法 —— 但那是**十倍量级错误**，不是四舍五入，
       正是编造数字最典型的形态。所以必须**限定倍率为 10 的整数次幂 + 结果四舍五入后逐字相等**。
       自测用例 `num_ok('25', {'256'})` 期望 False，就是靠这条拦住的。
    """
    if n in old_nums:
        return True
    nd = len(n.split(".")[1]) if "." in n else 0
    try:
        nv = float(n)
    except ValueError:
        return False
    for o in old_nums:
        try:
            ov = float(o)
        except ValueError:
            continue
        for k in range(0, 7):
            try:
                cand = ov / (10 ** k)
            except OverflowError:
                continue
            if f"{cand:.{nd}f}" == n:
                return True
    return False


def _selftest():
    """已知答案自测 —— 校验脚本必须先能自证（本项目第三次踩这个坑）。"""
    cases = [
        # (速记区数字, 原卡数字集合, 期望)
        ("98.6", {"98.63", "121.7"}, True),      # 四舍五入 → 收
        ("271", {"271.3", "271300000"}, True),   # 截断/单位换算 → 收
        ("256", {"256", "512"}, True),           # 精确 → 收
        ("999.9", {"12.3", "45.6"}, False),      # 编造 → 拒
        ("1234", {"4321"}, False),               # 顺序不对 → 拒
        ("25", {"256"}, False),                  # 2 位且非前缀→ 拒（注：2 位会被上层的位数过滤跳过）
    ]
    bad = 0
    for n, old, want in cases:
        got = num_ok(n, old)
        flag = "✓" if got == want else "✗"
        if got != want:
            bad += 1
        print(f"  {flag} num_ok({n!r}, {sorted(old)}) = {got}  期望 {want}")
    # 千分位展开也要能自证
    assert norm_nums("2 569 168 B") >= {"2569168"}, "千分位展开坏了"
    print(f"  ✓ 千分位展开：'2 569 168 B' → 含 2569168")
    print(f"\n  自测{'全部通过' if bad == 0 else f'有 {bad} 条不符'}")
    return 0 if bad == 0 else 1


# 已登记的内容改动（重做 / 纠错 / 改名 —— 不是改造事故）
# 格式：文件名 <TAB> 原因 [<TAB> ③ 允许的数字，逗号分隔]
# 有登记的卡不再计为「① 失败」，只打印一行提示；第 3 列（可选）用于 ③ 数字核验。
ALLOW_FILE = PROJ / "_pipeline" / "v5-audit-allow.txt"


def load_allow():
    """→ (① 白名单 dict: 文件名→原因, ③ 白名单 dict: 文件名→set(数字))"""
    c1, c3 = {}, {}
    if not ALLOW_FILE.exists():
        return c1, c3
    for ln in ALLOW_FILE.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        parts = [x.strip() for x in ln.split("\t")]
        c1[parts[0]] = (parts[1] if len(parts) > 1 else "")
        if len(parts) > 2 and parts[2]:
            c3[parts[0]] = {x.strip() for x in parts[2].split(",") if x.strip()}
    return c1, c3


def main():
    cards = sorted(p for p in TARGET.glob("*.md")
                   if re.search(r"[\u4e00-\u9fff]", p.name) and R5.SPEED_HEADER in p.read_text(encoding="utf-8"))
    print(f"体检范围：{len(cards)} 张已改造的卡\n")
    print("  ⓘ 注：读前/读后各取一次 stat，两次不一致 = 文件正在被 worker 写入 → 本轮跳过（不报假错）\n")

    allow, allow_nums = load_allow()
    f_content, f_structure, f_meta = [], [], []
    allowed_hits = []
    num_total = num_miss = num_round = 0
    miss_detail = []
    round_detail = []

    skipped = []
    for p in cards:
        bak = BAK / p.name
        if not bak.exists():
            f_meta.append((p.name, "无备份"))
            continue
        # ⚠️ 2026-10-05 补：4 个 worker 并发写卡时，审计可能读到"写了一半"的状态，
        #    报出假的「段内容被改动 / 数字找不到」。**假 ERROR 比没有检查更危险**——
        #    会让人去"修"没坏的东西（1339 就被这样误报过一次，实为 r4-B 正在改）。
        #    对策与 validate-v4.py 一致：读前读后各取一次 stat，不一致就本轮跳过。
        try:
            s1 = p.stat()
        except FileNotFoundError:
            skipped.append(p.name)
            continue
        new = p.read_text(encoding="utf-8")
        old = bak.read_text(encoding="utf-8")
        try:
            s2 = p.stat()
        except FileNotFoundError:
            skipped.append(p.name)
            continue
        if (s1.st_mtime_ns, s1.st_size) != (s2.st_mtime_ns, s2.st_size):
            skipped.append(p.name)
            continue

        # ② 结构
        if not (new.count(R5.SPEED_HEADER) == 1 and new.count("## 30 秒版") == 1
                and new.count(R5.DEEP_HEADER) == 1):
            f_structure.append(p.name)

        # ① 逐段比对
        try:
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                ok = R5.verify_content_identical(old, new)
            if not ok:
                if p.name in allow:
                    allowed_hits.append((p.name, allow[p.name]))
                else:
                    f_content.append((p.name, buf.getvalue().strip()))
        except Exception as e:
            f_content.append((p.name, f"异常 {e}"))

        # ④ 元信息
        if head_lines(old) != head_lines(new):
            f_meta.append((p.name, "H1/来源行 不一致"))

        # ③ 数字回卡（只看 30 秒版那一段）
        m = re.search(r"## 30 秒版\n(.*?)\n#{1,2} ", new, re.S)
        if m:
            seg = m.group(1)
            old_nums = norm_nums(old)          # 原卡侧也先归一化（去千分位）
            for n in nums_in(seg):
                if len(n.split(".")[0]) < 3 and "." not in n:
                    continue          # 跳过 1~2 位数，噪声太大
                num_total += 1
                if n in allow_nums.get(p.name, set()):
                    num_round += 1          # 已登记的「由卡内数据重算得出」，按豁免计
                    round_detail.append((p.name, n))
                elif not num_ok(n, old_nums):
                    num_miss += 1
                    miss_detail.append((p.name, n))
                elif n not in old_nums:
                    num_round += 1
                    round_detail.append((p.name, n))

    print("【① 逐段比对：除顺序外一字未改】")
    print(f"  通过 {len(cards) - len(f_content)} / {len(cards)}")
    for n, why in f_content[:10]:
        print(f"    ✗ {n}\n       {why}")
    if allowed_hits:
        print(f"  ⓘ 另有 {len(allowed_hits)} 张已登记的内容改动（重做/纠错，不计失败）：")
        for n, why in allowed_hits[:10]:
            print(f"    · {n}  —— {why}")

    print("\n【② 结构计数：速记区/30秒版/原理区 各恰好 1】")
    print(f"  通过 {len(cards) - len(f_structure)} / {len(cards)}")
    for n in f_structure[:10]:
        print(f"    ✗ {n}")

    print("\n【③ 30 秒版数字回卡核验】")
    print(f"  抽出 ≥3 位数字 token：{num_total} 个；精确命中 {num_total - num_miss - num_round} 个"
          f"；四舍五入命中 {num_round} 个；回原卡找不到：{num_miss} 个")
    if round_detail:
        print("  四舍五入明细（速记区写了约数，语义忠实，不算编造）：")
        for n, x in round_detail[:10]:
            print(f"    · {n}  →  {x}")
    if miss_detail:
        print("  未命中明细（可能是格式差异，需人工判读）：")
        for n, x in miss_detail[:25]:
            print(f"    ✗ {n}  →  {x}")
    else:
        print("  ✓ 无编造数字")

    print("\n【④ 元信息未动：H1 / > 来源行】")
    print(f"  通过 {len(cards) - len(f_meta)} / {len(cards)}")
    for n, why in f_meta[:10]:
        print(f"    ✗ {n}  ({why})")

    bad = len(f_content) + len(f_structure) + len(f_meta)
    if skipped:
        head = "、".join(skipped[:5])
        more = f" 等 {len(skipped)} 张" if len(skipped) > 5 else ""
        print(f"\n  ⓘ 跳过 {len(skipped)} 张（体检期间正在被写入，正常并发，稍后重跑即纳入）：{head}{more}")
    print("\n" + "=" * 50)
    print("  总体：", "✓ 全部通过" if bad == 0 and num_miss == 0 else f"✗ 有 {bad} 项结构/内容问题 + {num_miss} 个可疑数字")
    return 0 if bad == 0 and num_miss == 0 else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        print("【已知答案自测】")
        sys.exit(_selftest())
    sys.exit(main())
