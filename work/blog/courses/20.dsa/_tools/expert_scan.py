#!/usr/bin/env python3
# expert_scan.py — 数据结构专家视角的语义级扫描（上 LeetCode 会翻车的经典坑）
# 规则：
#   R1 比较器减法溢出（C/C++/Java int 减法比较器，值域 ±1e9 时 a-b 溢出）
#   R2 递归无深度保护（Python 递归解法，深输入会 RecursionError）
#   R3 Lua pairs 遍历数组（无序，依赖顺序处会错）
#   R4 R 1:n 裸降序（n=0 时 1:0 递减遍历）
#   R5 浮点相等比较（== 0.1 类）
#   R6 JS/TS 数组引用比较（=== 比数组恒 false）
#   R7 二分指针停滞（left = mid 无 +1，可能死循环）
#   R8 整除截断差异（C 系 / 与 python // 混用负数场景标记）
#   R9 charCodeAt 单码元遍历（含中文/emoji 输入会错，标记）
# 输出 _meta/expert_scan.json
import glob, json, re
from collections import Counter

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"

def code_of(t):
    out = []
    for ln in t.split("\n"):
        s = ln
        for cm in ("//", "#", "--"):
            k = s.find(cm)
            if k >= 0 and not (k > 0 and s[k - 1] == ":"):
                s = s[:k]
        out.append(s)
    return "\n".join(out)

def is_recursive(code, fname):
    return bool(re.search(rf"\b{re.escape(fname)}\s*\(", code[code.find(f"function {fname}") + 1:]
                          if f"function {fname}" in code else code))

def scan_file(f):
    ext = f.rsplit(".", 1)[-1]
    t = open(f, encoding="utf-8", errors="ignore").read()
    code = code_of(t)
    issues = []

    if ext in ("cpp", "c", "java"):
        # R1: 比较器 a-b 形态（返回 int 的减法比较）
        for m in re.finditer(r"int\s+(\w+)\s*\(\s*const?\s*\w+\s*\*?\s*(\w+)\s*,\s*const?\s*\w+\s*\*?\s*(\w+)\s*\)\s*\{[^}]{0,120}?return\s+(\w+)\s*-\s*(\w+)\s*;", code):
            a, b = m.group(4), m.group(5)
            if {a, b} == {m.group(2), m.group(3)}:
                issues.append(("R1-比较器溢出", f"{f.split('/')[-1]}: {m.group(0)[:60]}"))
        if ext == "java":
            for m in re.finditer(r"\(\s*(\w+),\s*(\w+)\s*\)\s*->\s*(\w+)\s*-\s*(\w+)", code):
                if m.group(3) != "0" and {m.group(3), m.group(4)} == {m.group(1), m.group(2)}:
                    issues.append(("R1-比较器溢出", f"{f.split('/')[-1]}: {m.group(0)[:60]}"))

    if ext == "py":
        # R2: 递归函数（自调用）且文件无 setrecursionlimit
        recs = set()
        for m in re.finditer(r"def\s+(\w+)\s*\(([^)]*)\)\s*:", code):
            name = m.group(1)
            if name in ("demo", "main"):
                continue
            body_start = m.end()
            seg = code[body_start:body_start + 4000]
            if re.search(rf"\b{name}\s*\(", seg):
                recs.add(name)
        if recs and "setrecursionlimit" not in t:
            issues.append(("R2-递归深度", f"{f.split('/')[-1]}: 递归 {sorted(recs)[:3]} 无深度保护"))

    if ext == "lua":
        # pairs 用于聚合表（计数/映射）无碍；只有对「顺序数组」用 pairs 才有风险
        ordered = re.search(r"(#\s*\w+|table\.insert\(|ipairs\()", code)
        for m in re.finditer(r"for\s+([\w,\s]+)\s+in\s+pairs\((\w+)\)", code):
            tbl = m.group(2)
            if re.search(rf"\b{tbl}\s*=\s*\{{\s*\}}", code) and "ipairs(" not in code:
                issues.append(("R3-lua pairs", f"{f.split('/')[-1]}: pairs({tbl}) 疑似顺序数组"))

    # R10 Python 可变默认参数
    if ext == "py":
        for m in re.finditer(r"def\s+\w+\s*\([^)]*=[\s]*(\[\]|\{\})[^)]*\)\s*:", code):
            issues.append(("R10-可变默认参数", f"{f.split('/')[-1]}: {m.group(0)[:60]}"))

    # R11 JS/TS 数字数组 sort() 无比较器（字典序陷阱）
    if ext == "ts":
        for m in re.finditer(r"\.sort\(\s*\)", code):
            seg = code[max(0, m.start() - 150):m.start()]
            # 同文件中出现明显的数字数组字面量 + 纯数字输入提示才标记
            if re.search(r":\s*number\[\]", seg) or re.search(r"=\s*\[\s*\d+", seg):
                issues.append(("R11-sort无比较器", f"{f.split('/')[-1]}: {m.group(0)}"))
                break

    # R16 Java 字符串/字符引用比较
    if ext == "java":
        for m in re.finditer(r'\b\w+\s*(==|!=)\s*"[^"]*"', code):
            issues.append(("R16-引用比较", f"{f.split('/')[-1]}: {m.group(0)[:40]}"))
            break

    # R17 二分中点溢出（lo+hi 在 int 域相加，值域 1e9 时溢出）
    if ext in ("java", "c", "cpp"):
        for m in re.finditer(r"\(\s*(\w+)\s*\+\s*(\w+)\s*\)\s*/\s*2", code):
            a, b = m.group(1), m.group(2)
            if a in ("lo", "left", "l", "low") or b in ("hi", "right", "r", "high"):
                issues.append(("R17-中点溢出", f"{f.split('/')[-1]}: {m.group(0)}"))
                break

    # R18 parseInt 缺 radix
    if ext == "ts":
        for m in re.finditer(r"parseInt\s*\(\s*([^(]*(?:\([^()]*\))?[^()]*)\)", code):
            if "," not in m.group(1):  # 单参数才是缺 radix
                issues.append(("R18-parseInt", f"{f.split('/')[-1]}: {m.group(0)[:40]}"))
                break

    # R19 Python is 比较数字/字符串
    if ext == "py":
        for m in re.finditer(r'\bis\s+(?!not\b)(\d+|["\'][^"\']*["\'])', code):
            issues.append(("R19-is比较", f"{f.split('/')[-1]}: {m.group(0)[:40]}"))
            break

    if ext == "R":
        for m in re.finditer(r"(?:for\s*\(\s*\w+\s+in\s+|seq\()1:(\w+)", code):
            var = m.group(1)
            if var.isdigit():
                continue  # 常量上界无 n=0 风险
            if not re.search(rf"if\s*\(?\s*{var}\s*>=?\s*1|if\s*\(?\s*{var}\s*>\s*0|length\(\s*{var}\)|{var}\s*>=\s*1", code):
                issues.append(("R4-R降序", f"{f.split('/')[-1]}: 1:{var} 无守卫"))

    for pat, tag in ((r"==\s*0\.5\b|R5", None),):
        pass
    for m in re.finditer(r"[=!]=\s*\d+\.\d+", code):
        issues.append(("R5-浮点相等", f"{f.split('/')[-1]}: {m.group(0)}"))
        break

    if ext in ("ts",):
        for m in re.finditer(r"(\w+)\s*(={2,3})\s*(\w+)\s*[;)\n]", code):
            a, b = m.group(1), m.group(3)
            for v in (a, b):
                if re.match(r"^(res|result|ans|out|arr|nums|list|levels|levelsArr)$", v) and "JSON.stringify" not in code[max(0, m.start() - 80):m.start()]:
                    issues.append(("R6-引用比较", f"{f.split('/')[-1]}: {m.group(0)[:50]}"))
                    break
            else:
                continue
            break

    if ext in ("ts", "javascript"):
        for m in re.finditer(r"(left|lo)\s*=\s*mid\s*;", code):
            seg = code[max(0, m.start() - 200):m.start()]
            if "mid - 1" not in code[m.start():m.start() + 200] and "mid+1" not in code[m.start():m.start() + 200].replace("mid + 1", "mid+1"):
                issues.append(("R7-二分停滞", f"{f.split('/')[-1]}: {m.group(0)}"))

    if ext == "lua":
        for m in re.finditer(r"math\.floor\s*\(\s*\w+\s*/\s*\w+\s*\)", code):
            pass  # lua 5.4 // 已可用；floor(/) 对负数同为向负无穷，一致
    if ext in ("c", "cpp", "java", "go", "dart", "zig"):
        for m in re.finditer(r"/\s*2\b", code):
            pass  # 正数场景 /2 无碍；负数除法标记成本过高，跳过
    return issues


def main():
    files = []
    for ext in ("ts", "py", "go", "java", "rs", "lua", "c", "cpp", "R", "zig", "dart"):
        files += glob.glob(f"{DSA}/*/*/*/solution_*.{ext}")
    report = {"scanned": len(files), "findings": {}}
    counter = Counter()
    for f in sorted(files):
        try:
            issues = scan_file(f)
        except Exception as e:
            issues = [("scan-error", str(e)[:60])]
        if issues:
            report["findings"][f.split("dsa/")[-1]] = issues
            for kind, _ in issues:
                counter[kind] += 1
    report["summary"] = dict(counter)
    json.dump(report, open(f"{DSA}/_meta/expert_scan.json", "w"), ensure_ascii=False, indent=1)
    print(f"专家扫描 {report['scanned']} 文件，发现 {len(report['findings'])} 个文件带标记")
    for k, n in counter.most_common():
        print(f"  {k}: {n}")


if __name__ == "__main__":
    main()
