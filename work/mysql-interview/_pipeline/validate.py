#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate.py — 面试卡质量门禁（把 SPEC v3 的 14 条检查项变成可执行断言）

用法：
  python3 validate.py                      # 校验 target/ 下全部卡
  python3 validate.py --file <path>        # 校验单张
  python3 validate.py --dir <dir>          # 校验指定目录
  python3 validate.py --strict             # 有任何 error 就非零退出（CI 用）

退出码：0 = 通过（可能有 warn）；1 = 有 error
模型无关：任何 agent 跑完一批后都应执行一次
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "target"

# 机翻残留黑名单 —— 必须带上下文，避免误伤
# 教训：裸缩写 "uin" 会命中 uint64；"max" 会命中 max_connections
BLACKLIST = [
    r"构语言", r"构元", r"购语言", r"护士锁", r"自选锁", r"妈妈引擎", r"引诺DB",
    r"锐度log", r"费得流", r"派森", r"CQ语句", r"格空带", r"sate格外", r"hastgrim",
    r"maxs点", r"maxk\b", r"\buin的", r"u一，六十四", r"float六十四",
    r"裸体", r"首时穿着", r"小r留下",
    # 刻板印象 / 有害内容
    r"HR.{0,6}年轻女性", r"女性.{0,10}穿着.{0,6}印象",
]
# 只扫正文，代码块/表格中的同形词不算
STRIP_TARGETS = ("go", "python", "java", "sql", "lua", "text", "mermaid", "bash", "json", "yaml", "md")

# 允许 .deep.md：SPEC 第 3 节规定的深挖卡命名
FILENAME_RE = re.compile(r"^\d{3}-[a-z0-9]+(-[a-z0-9]+)*(\.deep)?\.md$")
# 001-float-or-slice-as-map-key.md
MAIN_SUFFIX = ".deep.md"


class Result:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warns = []
        self.oks = 0

    def err(self, rule, msg):
        self.errors.append((rule, msg))

    def warn(self, rule, msg):
        self.warns.append((rule, msg))

    def ok(self):
        self.oks += 1

    @property
    def name(self):
        return self.path.name


def strip_code(text):
    """剥掉代码块，避免误报；顺便返回代码块列表"""
    blocks = []
    out = []
    in_block = False
    cur_lang, cur = "", []
    for line in text.splitlines():
        if line.startswith("```"):
            if in_block:
                blocks.append((cur_lang, "\n".join(cur)))
                in_block, cur_lang, cur = False, "", []
            else:
                in_block, cur_lang, cur = True, line[3:].strip(), []
            continue
        if in_block:
            cur.append(line)
        else:
            out.append(line)
    return "\n".join(out), blocks


def fence_issues(raw):
    """用开/闭状态机校验围栏配对 + 开围栏带语言标识
    教训：grep '^```$' 会命中闭合围栏，必须状态机判定"""
    errs = []
    n, opened_lang = 0, None
    for i, line in enumerate(raw.splitlines(), 1):
        if line.startswith("```"):
            if n % 2 == 0:
                opened_lang = line[3:].strip()
                if not opened_lang:
                    errs.append((i, "开围栏缺语言标识"))
            n += 1
    if n % 2 == 1:
        errs.append((0, "代码块未闭合（围栏总数为奇数）"))
    return errs


def cjk_count(text):
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def strip_section(text, section_name):
    """把指定小节整段移除（用于不计入体量统计）。
    从 '## <含 section_name 的标题>' 移除到下一个 '## ' 之前。"""
    out, skipping = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            skipping = section_name in line
        if not skipping:
            out.append(line)
    return "\n".join(out)


def validate_card(path: Path, is_deep: bool) -> Result:
    """校验单张卡片。is_deep=True 时走深挖卡分支（不校验主卡项）。"""
    r = Result(path)
    raw = path.read_text(encoding="utf-8")
    body, blocks = strip_code(raw)

    # 规则 1：围栏配对与语言标识
    fence_errs = fence_issues(raw)
    if fence_errs:
        for ln, msg in fence_errs:
            r.err("围栏", f"第 {ln} 行 {msg}" if ln else msg)
    else:
        r.ok()

    # 规则 2：文件名
    if not FILENAME_RE.match(path.name):
        r.err("文件名", f"不符合 <三位编号>-<英文短横线>.md：{path.name}")
    else:
        r.ok()

    # 深挖附录：文件名应为 xxx.deep.md
    if is_deep:
        if not path.name.endswith(MAIN_SUFFIX):
            r.err("文件名", f"深挖卡应以 .deep.md 结尾：{path.name}")
        for need in ("思路与架构", "方案取舍", "答题技巧"):
            if need not in raw:
                r.warn("深挖", f"缺小节「{need}」")
        return r   # 深挖卡不校验主卡项

    # 规则 3：主卡体量（≤700 汉字，不含代码、不含「⚠️ 原文纠错」小节）
    #
    # 历史（三次调整，都是被实测打脸后改的）：
    #   400 → 物理不可达。逐节统计：101 的 6 个必填小节就 505 字、102 是 538 字。
    #        继续压会逼出两种坏结果：① 砍掉停档判据/版本栅栏 → 卡片变口号
    #                              ② 无视硬约束 → 规则被当建议
    #   650 → 仍偏紧。53 张卡里 17 张精确卡在 648~650（占 32%），
    #        说明上限在制造"挤字数"行为，而不是在约束篇幅。
    #   700 → 当前值。6 个必填节 + P5/P6/P7 判据 + 停档列 + 版本表，
    #        在不删信息的前提下能写完。
    #
    # 「⚠️ 原文纠错」不计入主卡字数 —— 它是补充证据不是必填内容，
    # 但单节应 ≤150 字；超了应精简措辞，不是整节搬进主卡。
    #
    # ⚠️ 注意：上限只约束主卡。**超限的唯一解法是拆卡**
    #    （L3+ 拆 .deep.md；L1/L2 拆成多张主卡），不是删内容。
    # 「关键代码」节里的实测输出说明本质是**代码的附件**（展示这段代码跑出什么），
    # 不是可背的知识点。worker 报告 144 初稿 1361 字压到 694 用了 20 轮，
    # 且"删代码注释 0 收益"——挤到最后只能砍「依据」与机制铺陈，那是在损害质量。
    # 实测各节平均字数：主问答 156 / 面试官视角 120 / 追问链 103 / 版本 65 / 总结 48 / 总述 38
    #   → 6 个必填节合计约 530 字，700 上限的余量主要被代码附件吃掉。故排除该节。
    n = cjk_count(strip_section(strip_section(body, "⚠️ 原文纠错"), "关键代码"))
    if n > 700:
        r.err("体量",
              f"主卡 {n} 汉字，超出 700 字上限。"
              f"压到 700 的正确做法是拆卡（L3+ 拆到 .deep.md；L1/L2 拆成多张主卡）；"
              f"**禁止**为凑字数砍掉追问链停档判据、版本栅栏或验证数据")
    else:
        r.ok()

    # 规则 3b：「⚠️ 原文纠错」小节必须存在且 ≤250 汉字
    #
    # 阈值演进（每调整都有实测数据支撑，不是拍脑袋）：
    #   无检查 → 150 → 200 → 250
    #   250：worker 报告 151 的 226 字已是「再压就要动依据列」，
    #   而依据（源码行号 + 实测输出）是这张卡不可替代的价值。宁可略超也不删依据。
    #
    # ⚠️ 2026-10-03 补一个真漏网：**纠错节「缺失」原先不报错** ——
    #   worker 2 的小节重排脚本把 158 的纠错节整节删了，validate 仍 PASS，
    #   因为规则是「有节才查字数」。它靠逐节统计字数才抓到。
    #   现在：**缺节直接 error**，不再静默放过。
    if "## ⚠️ 原文纠错" not in body:
        r.err("纠错节",
              "缺「## ⚠️ 原文纠错」小节 —— 本流水线每张卡都必须列出原文的技术错误与实际值。"
              "**若原文确实无错，写一行『未发现技术错误』并说明核对范围，不要整节删掉**")
    else:
        # ⚠️ 只统计**本节本体**（到下一个 `## ` 为止）。
        # 2026-10-03 worker 6 指出：原实现用 `body[idx:]` 截到**文末**，
        # 把后面「关键代码」节的实测输出说明（209 卡约 110 字）也算进纠错节，
        # **报 344 字而真实只有 124 字**，虚高 220 字 → 误报 warn。
        # 依据：「关键代码」节与「原文纠错」节**同级**（都是 `##`），不该串算。
        _i = body.index("## ⚠️ 原文纠错")
        _rest = body[_i:]
        _m = re.search(r"\n## ", _rest[10:])
        err_text = _rest[:10 + _m.start()] if _m else _rest
        ne = cjk_count(err_text)
        if ne > 250:
            r.warn("纠错节", f"「⚠️ 原文纠错」{ne} 汉字，超出 250 字建议线"
                            f"（可压：合并同类项、去掉重复的原文引述；**不要删「依据」列**）")
        else:
            r.ok()

    # 规则 4：必须有的小节，且**标题必须独立成行**
    for need in ("一句话总述", "面试官视角", "主问答", "追问链", "版本与兼容性", "总结"):
        if need not in raw:
            r.err("小节", f"缺「{need}」")
    # ⚠️ 2026-10-03 worker 3 报的真盲区：
    #   「## 主问答」被**粘在上一行 bullet 的尾巴上**（同一行）时，
    #   `need in raw` 照样命中（子串存在），`re.search(r"## 主问答...")` 也能匹配 ——
    #   **门禁完全查不出**，但 Markdown 不会把它当标题，
    #   浏览器里整个「主问答」小节直接消失。
    # ⚠️ 第一版我写成 `^##\s*{need}\s*$`（要求结尾即行尾）—— **误报了**：
    #   真实卡片写的是 `## 总结与追问预判`、`## 一句话总述（...）` 这类**带后缀**的标题。
    #   正确判据：**必须是行首 `## ` 开头**（后面带什么都行），只要不在行首就说明被粘在别处。
    for need in ("一句话总述", "面试官视角", "主问答", "追问链", "版本与兼容性", "总结"):
        if need in raw and not re.search(rf"^##\s+\S*{re.escape(need)}", raw, re.M):
            # 找出它实际出现在哪一行，报出行号帮定位
            ln = next((i + 1 for i, l in enumerate(raw.splitlines()) if need in l), 0)
            r.err("小节", f"「{need}」标题未独立成行（第 {ln} 行）—— "
                         f"被粘在上一段文字尾巴上时 Markdown 不会渲染成标题，该小节会整节消失。"
                         f"**必须让它单独占一行**")
    if not r.errors:
        r.ok()

    # 规则 5：答案骨架 ≥3 点且以 **加粗** 开头
    m = re.search(r"## 主问答(.*?)(?=\n## |\Z)", raw, re.S)
    if m:
        numbered = re.findall(r"^\d+\.\s+\*\*", m.group(1), re.M)
        if len(numbered) < 3:
            r.err("答案骨架", f"「主问答」下的加粗要点只有 {len(numbered)} 条，应 ≥3")
        else:
            r.ok()
    else:
        r.err("小节", "缺「主问答」")

    # 规则 6：追问链应覆盖 L1~L5 且有停档
    m = re.search(r"## 追问链(.*?)(?=\n## |\Z)", raw, re.S)
    if m:
        blk = m.group(1)
        missing = [lv for lv in ("L1", "L2", "L3", "L4", "L5") if f"| {lv} " not in blk and f"|{lv}" not in blk]
        if missing:
            r.warn("追问链", f"未覆盖层级：{', '.join(missing)}")
        elif "停在哪档" not in blk and "停" not in blk:
            r.warn("追问链", "缺「答不出停在哪档」列")
        else:
            r.ok()
    else:
        r.err("小节", "缺「追问链」")

    # 规则 7：版本与兼容性非空
    m = re.search(r"## 版本与兼容性(.*?)(?=\n## |\Z)", raw, re.S)
    if m and len(m.group(1).strip()) < 20:
        r.err("版本栅栏", "「版本与兼容性」为空或过短——必填项")
    elif m:
        r.ok()

    # 规则 8：原文锚点
    if "原文锚点" not in raw:
        r.err("原文锚点", "头部缺「原文锚点」")
    else:
        r.ok()

    # 规则 9：补充分级标记存在性（至少要有一处标记）
    marks = re.findall(r"\[(实测|源码|经验|存疑)\]", body)
    if not marks:
        r.warn("补充分级", "全文无 [实测]/[源码]/[经验]/[存疑] 标记——若全为原文可忽略")

    # 规则 10：[实测] 附近必须有代码或命令
    # 搜索区间必须**包含标记所在行本身** —— 常见写法是
    #   「…验证：`mergo.Merge(...)` 返回 xxx `[实测]`。」
    # 验证方式就在标记同行的前文里。原实现从下一行开始找，导致这类合规写法被误报。
    lines = body.splitlines()
    for i, line in enumerate(lines, 1):
        if "[实测]" in line:
            # 从标记行往前 1 行、往后 4 行，覆盖"同行前文"与"后续验证块"两种写法
            lo = max(0, i - 1)
            tail = "\n".join(lines[lo:i + 4])
            if not re.search(r"`[^`]+`|\$\s|验证|实测|输出|结果|返回", tail):
                r.err("补充分级",
                      f"「[实测]」所在行及后 4 行内无验证方式（命令/代码/输出）"
                      f"—— 验证方式可写在标记同行前文，或下一行单独写「> 验证：…」")
                break
    else:
        r.ok()

    # 规则 11：禁止说法黑名单（只在正文扫，已剥代码块）
    for pat in BLACKLIST:
        for m2 in re.finditer(pat, body):
            ctx = body[max(0, m2.start() - 12):m2.end() + 12].replace("\n", " ")
            r.err("机翻残留", f"命中「{m2.group(0)}」：…{ctx}…")
            break

    # 规则 12：深挖门槛反查——L1/L2 不该有 .deep.md（同目录存在同名 deep 即违规）
    deep = path.parent / (path.stem + ".deep.md")
    if deep.exists():
        dm = re.search(r"难度[:：]\s*(L[1-4])", raw)
        if dm and dm.group(1) in ("L1", "L2"):
            r.err("深挖门槛", f"难度 {dm.group(1)} 却存在 {deep.name}——L1/L2 默认不出深挖")
        elif not dm:
            r.warn("深挖门槛", f"存在 {deep.name}，但读不到难度标注，请确认命中四个条件之一")
        else:
            r.ok()   # L3/L4 出深挖合规

    # 规则 13：mermaid 节点语法（禁括号/引号/斜杠）
    for lang, blk in blocks:
        if lang != "mermaid":
            continue
        for line in blk.splitlines():
            if re.search(r"\[\"[^\"]*\"|\['", line):
                r.err("mermaid", f"节点文案带引号：{line.strip()[:50]}")
                break
        for m3 in re.finditer(r"\w+\[([^\]]{16,})\]", blk):
            r.warn("mermaid", f"节点文案过长（>12 字）：{m3.group(1)[:30]}")
            break

    # 规则 14：代码块存在性
    if not any(lang in ("go", "python", "java", "sql", "lua") for lang, _ in blocks):
        r.warn("代码", "未见可运行语言的代码块")
    else:
        r.ok()

    return r


def collect(root: Path):
    # ⚠️ 2026-10-04：v4 改用中文命名，本门禁（v3 规则：6 小节 + 700 字）不再适用。
    # 双轨分工：
    #   validate.py    → 只管英文名卡（v3 遗留，待重做）
    #   validate-v4.py → 只管中文名卡（v4 新产出）
    # 否则 v3 门禁会把 v4 卡全部报错，噪声淹没真问题。
    out = []
    for p in sorted(root.rglob("*.md")):
        if not p.is_file():
            continue
        if re.search(r"[\u4e00-\u9fff]", p.name):
            continue          # v4 中文名卡，交给 validate-v4.py
        out.append(p)
    return out


def report(r: Result, verbose=False):
    tag = "PASS" if not r.errors else "FAIL"
    print(f"[{tag}] {r.name}  (✓{r.oks}  ✗{len(r.errors)}  ⚠{len(r.warns)})")
    for rule, msg in r.errors:
        print(f"     ✗ {rule}: {msg}")
    for rule, msg in r.warns:
        if verbose or True:
            print(f"     ⚠ {rule}: {msg}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--dir")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if args.file:
        paths = [Path(args.file)]
    elif args.dir:
        paths = collect(Path(args.dir))
    else:
        paths = collect(TARGET) if TARGET.exists() else []

    if not paths:
        print("没有可校验的卡片")
        return 0

    results = []
    for p in paths:
        is_deep = p.name.endswith(MAIN_SUFFIX)
        try:
            r = validate_card(p, is_deep)
        except Exception as e:
            r = Result(p)
            r.err("异常", f"解析失败：{e}")
        results.append(r)
        if not args.quiet:
            report(r)

    n_err = sum(len(r.errors) for r in results)
    n_warn = sum(len(r.warns) for r in results)
    n_ok = sum(1 for r in results if not r.errors)
    print(f"\n{'='*54}")
    print(f"  通过 {n_ok}/{len(results)} 张   error {n_err}   warn {n_warn}")
    print(f"{'='*54}")
    if n_err:
        print("有 error，必须修完再进下一批。")
        return 1 if args.strict else 0
    print("可以进下一批。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
