#!/usr/bin/env python3
"""v4 门禁：按 SPEC-v4 校验（中文命名 / 讲解式 / 不限字数）

与 v3 的区别：
  - **不查字数**（v4 不限字数）
  - 查**中文文件名**
  - 查 **7 段式结构**
  - 查围栏闭合、代码可运行标记
  - 对 v3 遗留的元标签给 warn（用于重做时定位）

用法：
    python3 validate-v4.py            # 全库
    python3 validate-v4.py --file X   # 单文件
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(os.environ.get("MT_ROOT", Path(__file__).resolve().parent.parent)).resolve()
TARGET = ROOT / "target" / "go"

# v4 七段式（顺序即要求的存在性，不强制顺序）
SECTIONS = ["先说结论", "完整代码", "逐行讲透", "实测验证", "原文哪里错了", "面试怎么答", "面试官可能接着问"]

# 允许「同号分卡」的编号（**同号 + 不同主题**才算合法分卡，不是撞号）。
# 与 checkdup.py 的 ALLOWED_SAME_NUM 保持一致 —— 两处都要维护，别只改一边。
ALLOWED_SAME_NUM = {
    "126": "lazy-singleton(DCL 单例) / singleflight(请求合并) —— 同源不同主题",
}

# v3 遗留元标签（warn，用于重做定位）
V3_LABELS = [
    (r"P5\s*[/／|、]", "v3 的 P5/P6/P7 分档"),
    (r"\*\*红旗\*\*", "v3 的红旗标签"),
    (r"\*\*惊艳点\*\*", "v3 的惊艳点标签"),
    (r"\*\*反直觉\*\*", "v3 的反直觉标签"),
    (r"^\|\s*L[1-5]\s*\|", "v3 的追问链表"),
]

# Go 里 "..." 的三种**合法**用法（用于把省略号占位检查里的误报摘掉）
#   ① 变参声明  func f(a ...T)
#   ② 展开      f(xs...)     —— 必须紧贴，`f(xs ...)` 本身才是语法错
#   ③ 数组长度  a := [...]int{1,2,3}
_ELL_VARARG = re.compile(r"\.\.\.\s*[A-Za-z_\[\]\*]")
_ELL_EXPAND = re.compile(r"[A-Za-z_0-9\)\]]\.\.\.")
_ELL_ARRLEN = re.compile(r"\[\s*\.\.\.\s*\]")

# 字符串字面量（里面的 "..." 是输出文本，不是代码占位）← 2026-10-04 补
_STR_DQ = re.compile(r'"(?:[^"\\]|\\.)*"')      # 双引号字符串（含转义）
_STR_RAW = re.compile(r"`[^`]*`")               # 反引号原始字符串


class Report:
    def __init__(self, name):
        self.name = name
        self.errs = []
        self.warns = []
        self.oks = []

    def err(self, kind, msg):
        self.errs.append((kind, msg))

    def warn(self, kind, msg):
        self.warns.append((kind, msg))

    def ok(self):
        self.oks.append(1)


def check(path: Path, strict=False):
    r = Report(path.name)
    raw = path.read_text(encoding="utf-8")

    # --- 1. 文件名：编号 + 中文 ---
    stem = path.stem
    # 2026-10-04：编号段已扩展到 4 位（901~1004、1101+），故 3~4 位都接受。
    m = re.match(r"^(\d{3,4})-(.+)$", stem)
    if not m:
        r.err("命名", "文件名不含编号前缀（应为 `NNN-中文标题.md` 或 `NNNN-中文标题.md`）")
    else:
        title = m.group(2)
        num = m.group(1)          # 编号，供下面的「编号唯一性」检查用
        title = re.sub(r"\.deep$|-深挖$", "", title)
        if not re.search(r"[\u4e00-\u9fff]", title):
            r.err("命名", f"标题「{title}」不含中文（v4 要求中文命名）")
        elif len(title) > 24:
            r.warn("命名", f"中文标题 {len(title)} 字，建议 ≤24 字")
        else:
            r.ok()
        # ⚠️ 2026-10-04：文件名不许含 `%` `#` 空格 —— shell 里要转义、不便检索。
        # 踩过：`373-%v %+v %#v 的区别（二）.md` 改过后压成无意义的 `vvv`，
        # 正解是**换一个有语义的中文标题**（如「格式化输出进阶Stringer与百分号转义」）。
        if re.search(r"[%#]", title) or " " in title:
            r.err("命名", f"标题「{title}」含 %/#/空格 —— 换一个有语义的中文标题，不要做符号替换")

        # --- 1b. 编号唯一性（2026-10-04 新增：三次撞车后的「机制性」修复）---
        # 背景：worker 连续三次把卡写进别人的号段（901 撞 901、902 撞 902 …）。
        # 原因不是 worker 不听话，而是**号段约定的传达通道不可靠**：
        #   - 只发「更正」消息 → worker 的上下文里旧任务书权重更高，会忽略
        #   - 只改 TODO-worker.md → worker 不一定每批都重读
        # 而**门禁是每张卡都必须跑、且必须看到 PASS 的东西** —— 把检查放这里才拦得住。
        # deep/深挖 变体不算撞号（同一张卡的展开版）。
        # v3 英文 slug 老卡**不算撞号** —— 它们是迁移遗留（例：v4 的 `166-判断两棵二叉树是否相等.md`
        # 与 v3 的 `166-binary-tree-equality-nil-branches.md` 同号），属已知的「待重构清单」，
        # 不由本门禁负责；本门禁只管 **v4 中文卡之间** 不许撞号。
        if not stem.endswith(".deep") and "-深挖" not in stem:
            siblings = sorted(
                p.name for p in path.parent.glob(f"{num}-*.md")
                if p.name != path.name
                and not p.name.endswith(".deep.md")
                and "-深挖" not in p.name
                and re.search(r"[\u4e00-\u9fff]", p.name)   # 只把「中文卡」当同类比较
            )
            if siblings and num not in ALLOWED_SAME_NUM:
                r.err(
                    "撞号",
                    f"编号 {num} 已被占用：{', '.join(siblings)} —— "
                    f"本卡请改用你号段内的下一个空闲编号（号段表见 _pipeline/TODO-worker.md），"
                    f"改完重跑本门禁",
                )
            elif not siblings:
                r.ok()

    # --- 1c. 元信息块：`> 来源：` 行必须是规范格式（2026-10-04 新增）---
    # 背景：有 worker 把来源行写成了**原始文件路径**
    #   x 不规范：> 来源：`source/12/12-48 谈谈SQL优化的经验（一）-迅捷文字转语音-1790923709485zh.txt`
    #   v 规范  ：> 来源：`12-48 谈谈SQL优化的经验（一）`
    # 危害：① 卡头元信息是「引用」，不是文件路径，读者要的是"源自哪一讲"；
    #       ② 按 `> 来源：`NN-MM` 反查「任务↔卡片」映射的脚本会匹配不上 → 台账失真。
    src_line = re.search(r"^>\s*来源：`([^`]*)`", raw, re.M)
    if src_line:
        sv = src_line.group(1)
        if re.match(r"^\d{1,2}-\d{1,2}\s+\S", sv):
            r.ok()
        elif sv.startswith("source/"):
            r.err("来源行", "来源行写成了原始文件路径 —— 规范格式是 `> 来源：`NN-MM <源标题>``（不要带 source/ 路径与 -迅捷文字转语音- 后缀）")
        else:
            r.warn("来源行", f"来源行「{sv[:40]}」不是 `NN-MM <标题>` 形式，请核对")

    # --- 2. 七段式结构 ---
    missing = [s for s in SECTIONS if not re.search(rf"^##+\s*{re.escape(s)}", raw, re.M)]
    # 深挖卡只查部分段
    if path.name.endswith(("-深挖.md", ".deep.md")):
        missing = [s for s in missing if s not in ("面试怎么答", "面试官可能接着问")]
    if missing:
        r.err("结构", f"缺小节：{' / '.join(missing)}")
    else:
        r.ok()

    # --- 3. 围栏闭合 ---
    if raw.count("```") % 2 != 0:
        r.err("围栏", "代码围栏未闭合")
    else:
        r.ok()

    # --- 4. 至少一个可执行代码块（go / sql / bash …）---
    # ⚠️ 2026-10-04 放宽：原版只认 ```go，但第 12 章（MySQL，64 篇）主代码块是 SQL、
    #    第 18 章（Linux，53 篇）会有 shell 片段。规则的目的（**完整可运行**）不变，
    #    只是不再限定语言。
    # ⚠️ 2026-10-05 再放宽（gpN 1237 指出）：只认词法白名单是**修不完的** ——
    #    第 18 章（Linux/IO）会写 ```c（read/write 系统调用就是 C 原型），
    #    后续章节还会有 cpp / rust / k8s yaml / toml / ini。
    #    每加一门语言就改一次白名单 = 打地鼠 → 改成**黑名单**：
    #    只把明显的「非代码」标记（空标记 / 纯中文 / 纯符号）排除，其余一律放行。
    code_blocks = [(m.group(1), m.group(2))
                   for m in re.finditer(r"```([A-Za-z0-9_+#.\-]*)\n(.*?)```", raw, re.S)
                   if m.group(1).lower() not in ("", "无", "none", "n/a", "none.")]
    if not code_blocks:
        r.err("代码", "没有代码块（支持 ```go / ```sql / ```bash 等）")
    else:
        # 不许有省略号占位
        # ⚠️ 2026-10-04 修误报（worker 指出，166 卡从第一天就挂着 2 条假告警）：
        #   `"..." in b` 太宽——Go 里 "..." 有三种**合法**用法，全被误判成占位：
        #     ① 变参声明  func f(a ...T)
        #     ② 展开      f(xs...)      （注意：... 必须紧贴，`f(xs ...)` 才是语法错）
        #     ③ 数组长度  a := [...]int{1,2,3}
        #   先把这三种摘掉，再看剩余是否还有裸的 "..."。
        #   已用 15 条用例回归（合法 8 条 / 占位 7 条），全对。
        #
        # ⚠️ 2026-10-04 再修（放宽语言后引入 9 条误报）：
        #   **省略号检查只对 ```go 块生效** —— 那套「三种合法用法」是 Go 特有的，
        #   套到 bash/text/yaml 块上会把正常内容误判（实测全库冒 9 条假告警）。
        #   其他语言没有对应的合法性规则，一律跳过。
        for i, (lang, b) in enumerate(code_blocks, 1):
            if lang != "go":
                continue
            t = re.sub(r"`[^`]*`", "", b)                 # 去掉行内 code 引用
            t = _STR_DQ.sub("", t)                        # 去掉双引号字符串 ← 2026-10-04 补
            t = _STR_RAW.sub("", t)                       # 去掉反引号原始字符串
            t = _ELL_VARARG.sub("", t)                    # ① 变参声明
            t = _ELL_EXPAND.sub("", t)                    # ② 展开（紧贴）
            t = _ELL_ARRLEN.sub("", t)                    # ③ 数组长度推断
            if re.search(r"^\s*//\s*(\.\.\.|省略)", b, re.M) or "..." in t:
                r.warn("代码", f"第 {i} 个代码块含省略号，v4 要求完整可运行")
        r.ok()

    # --- 5. 标题独立成行（v3 踩过的坑）---
    for s in SECTIONS:
        if s in raw and not re.search(rf"^##+\s*\S*{re.escape(s)}", raw, re.M):
            ln = next((i + 1 for i, l in enumerate(raw.splitlines()) if s in l), 0)
            r.err("标题", f"「{s}」未独立成行（第 {ln} 行）—— Markdown 不会渲染成标题")

    # --- 6. v3 元标签残留（warn，重做时定位用）---
    for pat, desc in V3_LABELS:
        if re.search(pat, raw, re.M):
            r.warn("v3残留", f"含 {desc}（v4 应删）")

    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="只检查单个文件")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if args.file:
        files = [Path(args.file)]
    else:
        # 只管中文名卡（v4）；英文名是 v3 遗留，由 validate.py 负责
        files = [f for f in sorted(TARGET.glob("*.md"))
                 if re.search(r"[\u4e00-\u9fff]", f.name)]

    nerr = 0
    nwarn = 0
    npass = 0
    fails = []
    skipped = []
    for f in files:
        # ⚠️ 2026-10-05 修「并发写导致的假 ERROR」：
        #   4 个 worker 同时在写卡，门禁扫到「正在被写」的文件会读到半截内容
        #   → 报一堆 error（"没有七段式""没有代码块"），但那张卡其实没问题，
        #   落盘后重跑就 PASS。**假 ERROR 比没有检查更危险**：会让人去"修"没坏的东西。
        #   对策：读之前、读之后各取一次 stat；两次不一致 = 文件正在被写 → 本轮跳过，不计 error。
        try:
            s1 = f.stat()
        except FileNotFoundError:
            skipped.append(f.name)      # 正在被 write-to-temp-then-rename 替换
            continue
        r = check(f, args.strict)
        try:
            s2 = f.stat()
        except FileNotFoundError:
            skipped.append(f.name)
            continue
        if (s1.st_mtime_ns, s1.st_size) != (s2.st_mtime_ns, s2.st_size):
            skipped.append(f.name)
            continue

        nerr += len(r.errs)
        nwarn += len(r.warns)
        if r.errs:
            fails.append(r)
            if not args.quiet:
                print(f"[FAIL] {f.name}  (✓{len(r.oks)} ✗{len(r.errs)} ⚠{len(r.warns)})")
                for k, m in r.errs:
                    print(f"     ✗ {k}: {m}")
        else:
            npass += 1
            if not args.quiet:
                tag = f"⚠{len(r.warns)}" if r.warns else "⚠0"
                print(f"[PASS] {f.name}  (✓{len(r.oks)} ✗0 {tag})")
                for k, m in r.warns:
                    print(f"     ⚠ {k}: {m}")

    print("=" * 54)
    print(f"  通过 {npass}/{len(files)} 张   error {nerr}   warn {nwarn}")
    if skipped:
        head = "、".join(skipped[:5])
        more = f" 等 {len(skipped)} 张" if len(skipped) > 5 else ""
        print(f"  ⓘ 跳过 {len(skipped)} 张（检查期间正在被写入，正常并发，稍后重跑即纳入）：{head}{more}")
    if nerr:
        print("有 error，必须修完再进下一批。")
        return 1
    print("可以进下一批。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
