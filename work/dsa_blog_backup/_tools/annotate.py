#!/usr/bin/env python3
# annotate.py — 11 语言逐行中文注释引擎
# 原则：只在行尾追加注释，绝不改代码本身；无法给出有意义注释的行跳过
# 用法: python3 annotate.py <lang> <file> [more files...]
#       python3 annotate.py --all   （全库 11 语言）
import os, re, sys

DSA = "/Users/Wang/Code/webfault-ai/dsa"
COMMENT = {"typescript": "//", "java": "//", "c": "//", "cpp": "//", "zig": "//",
           "rust": "//", "go": "//", "dart": "//", "python": "#", "r": "#", "lua": "--"}
EXT = {"typescript": "ts", "python": "py", "go": "go", "java": "java", "rust": "rs",
       "lua": "lua", "c": "c", "cpp": "cpp", "r": "R", "zig": "zig", "dart": "dart"}

# 语义变量词典（把标识符翻成读者能懂的话）
SEM = {
    "seen": "已见集合", "visited": "已访问集合", "used": "已用标记", "dp": "DP 表", "memo": "记忆化表",
    "res": "结果", "result": "结果", "ans": "答案", "answer": "答案", "output": "输出",
    "count": "计数", "cnt": "计数", "sum": "累计和", "total": "总和", "acc": "累加器", "best": "当前最优",
    "stack": "栈", "stk": "栈", "queue": "队列", "heap": "堆", "pq": "优先队列",
    "left": "左边界", "right": "右边界", "lo": "左边界", "hi": "右边界", "l": "左指针", "r": "右指针",
    "mid": "中点", "cur": "当前值", "curr": "当前值", "prev": "前一个", "next": "下一个",
    "nums": "数组", "arr": "数组", "nums1": "数组1", "nums2": "数组2", "a": "数组", "arr1": "数组1", "arr2": "数组2",
    "s": "字符串", "t": "另一字符串", "target": "目标值", "n": "元素个数", "len": "长度", "length": "长度",
    "i": "下标 i", "j": "下标 j", "k": "下标 k", "slow": "慢指针", "fast": "快指针", "head": "头节点",
    "node": "节点", "p": "节点", "q": "节点", "val": "值", "depth": "深度", "path": "当前路径",
    "board": "棋盘", "grid": "网格", "matrix": "矩阵", "adj": "邻接表", "edges": "边集",
    "x": "x", "y": "y", "v": "值", "w": "权重", "u": "节点 u", "step": "步数", "diff": "差值",
    "tmp": "临时变量", "temp": "临时变量", "start": "起点", "end": "终点", "size": "大小",
    "root": "根节点", "child": "子节点", "ch": "字符", "c": "字符", "word": "单词", "words": "单词列表",
    "pattern": "模式串", "prices": "价格序列", "coins": "硬币面额", "amount": "目标金额",
    "candidates": "候选数组", "pre": "前缀和", "maxv": "最大值", "minv": "最小值", "maxlen": "最长长度",
    "buffer": "缓冲", "builder": "拼接器", "freq": "频次表", "map": "映射表", "m": "映射表", "rows": "行数",
    "cols": "列数", "m_": "行数", "n_": "列数", "list": "列表", "headA": "链表 A", "headB": "链表 B",
    "left_head": "左半段", "right_head": "右半段", "dummy": "哨兵节点", "tail": "尾节点",
}

def sem_expr(expr):
    """把表达式粗译为中文语义串"""
    e = expr.strip()
    if not e:
        return ""
    e = re.sub(r"\[\.\.\.(\w+)\]", r" 复制的 \1 ", e)   # TS 展开 [...a]
    e = re.sub(r"(\w+)\[:\]", r"复制 \1", e)                # python 全切片 digits[:]
    e = re.sub(r"\.sort\(\(\w+, ?\w+\) => \w+ - \w+\)", "（按数值升序排序）", e)
    e = re.sub(r"\.map\(\(", " 逐项映射（", e)
    e = re.sub(r"=>", " 生成 ", e)
    # 字符串字面量原样保留内容
    strs = re.findall(r'"([^"]*)"', e)
    e = re.sub(r'"[^"]*"', '「' + (strs[0] if strs else "") + '」', e) if strs else e
    for lit in strs:
        e = re.sub(r'"[^"]*"', f'「{lit}」', e, count=1)
    # 标识符 → 语义词（长词优先）
    for k in sorted(SEM, key=len, reverse=True):
        e = re.sub(rf"\b{re.escape(k)}\b", SEM[k], e)
    # 常见成员调用
    e = re.sub(r"\.size\(\)|\.length\b|\.len\b", " 的长度", e)
    e = re.sub(r"\.empty\(\)|\.is_empty\(\)", " 是否为空", e)
    e = re.sub(r"\.push_back\(|\.push\(|\.append\(|\.add\(", " 追加 ", e)
    e = re.sub(r"\.pop_back\(|\.pop\(|\.remove\(", " 弹出 ", e)
    e = re.sub(r"\.find\(|\.get\(|\.indexOf\(", " 查找 ", e)
    e = re.sub(r"\.count\(", " 统计 ", e)
    e = re.sub(r"\.sort\(", " 排序 ", e)
    e = re.sub(r"\.contains\(|\.includes\(", " 是否包含 ", e)
    e = re.sub(r"\.substring\(|\.substr\(|\.slice\(", " 截取 ", e)
    e = re.sub(r"\.charAt\(|\bcharAt\b", " 取字符 ", e)
    e = re.sub(r"\.insert\(", " 插入 ", e)
    e = re.sub(r"\.erase\(|\.removeValue\(", " 删除 ", e)
    e = re.sub(r"\.begin\(\)|\.end\(\)", " 迭代位置 ", e)
    e = re.sub(r"\bswap\(", "交换 ", e)
    e = re.sub(r"\bmax\(", "取较大值 ", e)
    e = re.sub(r"\bmin\(", "取较小值 ", e)
    e = re.sub(r"\babs\(", "取绝对值 ", e)
    e = re.sub(r"\bMath\.max\b", "取较大值", e)
    e = re.sub(r"\bMath\.min\b", "取较小值", e)
    e = re.sub(r"\bMath\.abs\b", "取绝对值", e)
    e = re.sub(r"\bMath\.floor\b", "向下取整", e)
    e = re.sub(r"\bparseInt\b", "转整数", e)
    e = re.sub(r"\bprint\(|\bprintf\(|\bprintln\b|\bcout\b|\bconsole\.log\b|\bdebug\.print\b", "输出", e)
    # 运算符
    for op, cn in [("&&", " 且 "), ("||", " 或 "), ("===", " 全等于 "), ("!==", " 不等于 "),
                   (">=", " 不低于 "), ("<=", " 不超过 "),
                   ("==", " 等于 "), ("!=", " 不等于 "), (">", " 超过 "), ("<", " 小于 "),
                   ("+=", " 累加 "), ("-=", " 累减 "), ("*=", " 乘上 "), ("/=", " 除以 "),
                   ("++", " 加一 "), ("--", " 减一 "), ("=", " 赋值为 "),
                   ("+", " 加 "), ("-", " 减 "), ("*", " 乘 "), ("/", " 除以 "), ("%", " 对…取模 "),
                   ("!", "取反 "), ("&", " 按位与 "), ("|", " 按位或 "), ("^", " 按位异或 "),
                   ("<<", " 左移 "), (">>", " 右移 ")]:
        e = e.replace(op, cn)
    # 清理
    e = re.sub(r"\s+", " ", e).strip(" ；,. ")
    e = re.sub(r"( 且| 或| 的)$", "", e)
    return e

def var_of(s):
    """从 for/声明里猜主变量语义"""
    m = re.findall(r"\b(\w+)\b", s)
    for w in m:
        if w in SEM and w not in ("i", "j", "k", "n", "len", "length"):
            return SEM[w]
    return ""

def annotate_line(lang, ln, ctx):
    """返回该行的行尾注释（不含注释符），无意义返回 None。ln 为原始行。"""
    s = ln.strip()
    if lang in ("python", "r"):
        s_ns = re.sub(r"^#.*$", "", s)  # 去行首注释
    else:
        s_ns = re.sub(r"//.*$", "", s)
    core = s_ns.strip()
    if not core:
        return None
    T = core

    # 闭合/结构噪音
    if re.fullmatch(r"\}+;?", T) or re.fullmatch(r"\)+;?", T) or re.fullmatch(r"\];?", T):
        return None
    if T.endswith(("(", ",", "[", "&&", "||", "\\")):
        return None
    if re.match(r"^[@#]\[|@Override|@Deprecated", T):
        return None
    if re.fullmatch(r"[* ]+|/\*|\*/", T):
        return None

    # 引入
    if re.match(r"#include", T): return "引入头文件"
    if re.match(r"(import |package |using |use std|use crate|#import|library\(|require)", T):
        return "引入依赖"

    # 函数/类定义
    if lang == "python":
        m = re.match(r"(?:async )?def (\w+)\s*\(([^)]*)\)", T)
        if m:
            if m.group(1) == "__init__": return "构造函数：初始化成员"
            params = m.group(2)
            return f"定义函数 {m.group(1)}（参数：{sem_expr(params) or '无'}）"
        if re.match(r"class ", T): return "定义类"
    if lang == "r":
        m = re.match(r"(\w+)\s*<-\s*function\s*\(([^)]*)\)", T)
        if m: return f"定义函数 {m.group(1)}（参数：{sem_expr(m.group(2)) or '无'}）"
        m = re.match(r"(\w+)\s*<-\s*", T)
        if m and "=" not in T and "c(" not in T:
            return f"把 {sem_expr(T.split('<-',1)[1])} 存入 {SEM.get(m.group(1), m.group(1))}"
    if lang in ("typescript", "go", "dart", "java", "cpp", "rust", "zig", "c"):
        m = re.search(r"\bfunction\s+(\w+)\s*\(", T) or re.search(r"\bfn\s+(\w+)\s*\(", T) \
            or re.search(r"\bfunc\s+(?:\([^)]*\)\s*)?(\w+)\s*\(", T) \
            or re.match(r"\s*(?:public|private|static|final|synchronized)*\s*[\w<>\[\]]+\s+(\w+)\s*\([^;]*\)\s*\{?$", T) \
            or re.search(r"\bpub\s+fn\s+(\w+)\s*\(", T)
        if m:
            name = m.group(1)
            if name in ("main", "demo"): return "程序入口：跑内嵌自测用例"
            if re.match(r"(is|check)\w*", name): return f"定义判定函数 {name}"
            return f"定义函数/方法 {name}"
        if re.match(r"(class|struct|interface|enum|type)\s+\w+", T): return "定义类型"
        if re.match(r"impl\s+", T) and lang == "rust": return "实现块"

    # 控制流
    if lang == "python":
        m = re.match(r"for (\w+) in range\(([^,]+),\s*(-?\w+),\s*-(\d+)\)", T)
        if m:
            stop = sem_expr(m.group(2).strip())
            return f"让 {SEM.get(m.group(1), m.group(1))} 从 {stop} 倒数回去（每步减 {m.group(4)}）"
        m = re.match(r"for (\w+) in range\(([^)]*)\)", T)
        if m:
            rng = m.group(2).replace(",", " 到 ")
            return f"让 {SEM.get(m.group(1), m.group(1))} 从 {sem_expr(rng)} 遍历"
        m = re.match(r"for (\w+), (\w+) in (?:enumerate|\.items|sorted)\(?", T)
        if m: return f"同时取 {SEM.get(m.group(1), m.group(1))} 与 {SEM.get(m.group(2), m.group(2))} 遍历"
        m = re.match(r"for (\w+) in (reversed\(.+\)|\w+)\s*[:?]?", T)
        if m: return f"逐个取出 {sem_expr(m.group(2))} 的元素（{SEM.get(m.group(1), m.group(1))}）"
    if lang == "r":
        m = re.match(r"for (\w+) in (\d+):(\w+)", T)
        if m: return f"让 {SEM.get(m.group(1), m.group(1))} 从 {m.group(2)} 走到 {sem_expr(m.group(3))}"
        m = re.match(r"for (\w+) in ", T)
        if m: return f"逐个取出元素（{SEM.get(m.group(1), m.group(1))}）"
    if lang == "go":
        m = re.match(r"for (\w+) := (\d+);.*", T)
        if m: return f"让 {SEM.get(m.group(1), m.group(1))} 从 {m.group(2)} 开始计数"
        m = re.match(r"for (\w+), (\w+) := range ", T)
        if m: return f"同时取 {SEM.get(m.group(1), m.group(1))} 与 {SEM.get(m.group(2), m.group(2))} 遍历"
        m = re.match(r"for _, (\w+) := range (\w+)", T)
        if m: return f"逐个取出 {SEM.get(m.group(2), m.group(2))} 的元素（{SEM.get(m.group(1), m.group(1))}）"
        if re.match(r"for .*err != nil", T): return "逐行扫描（含错误检查）"
    if lang == "zig":
        m = re.match(r"for \(0\.\.(\w+)\) \|(\w+)\|", T)
        if m: return f"让 {SEM.get(m.group(2), m.group(2))} 从 0 走到 {sem_expr(m.group(1))} 减一"
        m = re.match(r"for \((\w[\w.]*)\) \|(\w+)\|", T)
        if m: return f"逐个取出 {sem_expr(m.group(1))} 的元素（{SEM.get(m.group(2), m.group(2))}）"
    if lang == "rust":
        m = re.match(r"for (\w+) in (?:&)?(\w+)", T)
        if m: return f"逐个取出 {SEM.get(m.group(2), m.group(2))} 的元素（{SEM.get(m.group(1), m.group(1))}）"
        if re.match(r"while let Some", T): return "边取边处理，取空即停"
        if T.startswith("match "): return "按情况匹配处理"
    if lang == "lua":
        m = re.match(r"for (\w+) = (\d+), (\w+)", T)
        if m: return f"让 {SEM.get(m.group(1), m.group(1))} 从 {m.group(2)} 走到 {sem_expr(m.group(3))}（Lua 1 基）"
        m = re.match(r"for (\w+), (\w+) in (?:pairs|ipairs)\(", T)
        if m: return f"遍历取 {SEM.get(m.group(2), m.group(2))}"
    # C 系 for
    m = re.match(r"for\s*\(\s*(?:const |let |var |int |size_t |usize |auto |i32 |i64 |long long )?(\w+)\s*=\s*([^;]+);([^;]*);", T)
    if m:
        var = SEM.get(m.group(1), m.group(1))
        cond = sem_expr(m.group(3).strip())
        return f"让 {var} 从 {sem_expr(m.group(2).strip())} 开始计数，{cond} 就继续"
    m = re.search(r"for\s*\(\s*(?:auto|const auto|var|let)?\s*&?(\w+)\s*:\s*([\w.\[\]>-]+)\s*\)", T)
    if m:
        return f"逐个取出 {sem_expr(m.group(2))} 的元素（{SEM.get(m.group(1), m.group(1))}）"
    if re.match(r"(}?\s*else\s+if\b|elif\b)", T):
        cond = re.sub(r"^(}?\s*else\s+if|elif)\s*\(?", "", T).rstrip("):{ ")
        return f"否则，若 {sem_expr(cond)}"
    if re.match(r"}?\s*else\b", T): return "否则"
    m = re.match(r"if\s*\((.+?)\)\s*return\s+(.+?);?$", T)
    if m:
        return f"若 {sem_expr(m.group(1))}，直接返回 {sem_expr(m.group(2))}"
    if "=>" in T:
        return None  # 箭头函数行语义复杂，不强行注释
    m = re.match(r"if\s*\(?(.*?)\)?\s*\{?$", T)
    if m and re.match(r"if\b", T):
        cond = re.sub(r"^if\s*\(?", "", T).rstrip("):{ ").rstrip("{").strip()
        return f"若 {sem_expr(cond)}"
    if re.match(r"while\s*\(", T) or (lang == "python" and T.startswith("while ")):
        cond = re.sub(r"^while\s*\(?", "", T).rstrip("):{ ").strip()
        return f"循环，直到不满足「{sem_expr(cond)}」"
    if re.match(r"(break;?|break)$", T): return "跳出循环"
    if re.match(r"continue;?$", T): return "跳过本轮，进入下一次"
    m = re.match(r"return\s+(.+?);?$", T)
    if m and lang != "r":
        return f"返回 {sem_expr(m.group(1))}"
    if lang == "r" and T.startswith("return("):
        return f"返回 {sem_expr(T[7:].rstrip(')'))}"

    # 自增自减 / 复合赋值
    m = re.fullmatch(r"(\w+)(\+\+|--);?", T)
    if m: return f"{SEM.get(m.group(1), m.group(1))}{' 加一' if m.group(2) == '++' else ' 减一'}"
    m = re.fullmatch(r"([\w\[\].]+)\s*(\+=|-=)\s*([^;]+);?", T)
    if m:
        op = "累加" if m.group(2) == "+=" else "累减"
        return f"{SEM.get(m.group(1), m.group(1))}{op} {sem_expr(m.group(3))}"
    m = re.fullmatch(r"swap\(([^,]+),\s*([^)]+)\);?", T)
    if m: return f"交换 {sem_expr(m.group(1))} 与 {sem_expr(m.group(2))}"
    m = re.fullmatch(r"std::swap\(([^,]+),\s*([^)]+)\);?", T)
    if m: return f"交换 {sem_expr(m.group(1))} 与 {sem_expr(m.group(2))}"

    # 声明赋值
    m = re.fullmatch(r"(?:const|let|var|final|auto|int|long long|usize|i32|i64|f64|double|float|Integer|Long|String|bool)\s+(\w+)\s*=\s*(.+?);?", T)
    if m:
        rhs = sem_expr(m.group(2))
        lhs = SEM.get(m.group(1), m.group(1))
        return f"把 {rhs} 存入 {lhs}" if rhs else f"声明 {lhs}"
    m = re.fullmatch(r"(?:let|var|const)?\s*(\w+)\s*=\s*(.+?);?$", T)
    if m and lang in ("python", "r", "lua", "typescript", "javascript", "dart"):
        return f"把 {sem_expr(m.group(2))} 存入 {SEM.get(m.group(1), m.group(1))}"
    if lang == "r":
        m = re.fullmatch(r"(\S+)\s*<-+\s*(.+)", T)
        if m: return f"把 {sem_expr(m.group(2))} 存入 {SEM.get(m.group(1), m.group(1))}"

    if "__main__" in T: return "仅直接运行本文件时执行自测"
    if re.match(r"(?:}?\s*)?elif\b", T): return "其余情况分支"
    # 输出与断言
    if re.search(r"printf|cout|println|console\.log|print\(|cat\(|debug\.print|fmt\.Print", T):
        if "PASS" in T: return "全部用例通过，输出 PASS"
        return "打印输出"
    if "stopifnot" in T or "assert" in T: return "断言校验"

    # 方法调用链
    m = re.search(r"\.push\(([^)]*)\)", T)
    if m: return f"把 {sem_expr(m.group(1))} 压入栈/数组尾部"
    m = re.search(r"\.append\(([^)]*)\)", T)
    if m: return f"把 {sem_expr(m.group(1))} 追加到列表尾部"
    if re.search(r"\.pop\(\)|\.pop_back\(\)", T): return "弹出栈顶元素"
    if re.search(r"\.shift\(\)", T): return "取出队首元素"
    if re.search(r"\.sort\(", T): return "排序"
    if re.search(r"\.reverse\(", T): return "反转"
    if re.search(r"\.join\(", T): return "拼接为字符串"
    if re.search(r"\.charAt\(", T): return "逐字符处理"

    # 带等号的其它赋值（结构体字段等）
    if "=" in T and not T.startswith("if") and "==" not in T.split("=")[0]:
        lhs, rhs = T.split("=", 1)
        lhs = lhs.strip().rstrip(".")
        rhs_c = sem_expr(rhs)
        lhs_c = SEM.get(lhs.split(".")[-1].strip(), lhs.strip())
        return f"把 {rhs_c} 写入 {lhs_c}"

    # 兜底：整句语义
    t = sem_expr(T)
    if len(t) >= 2:
        return t
    return None

OPEN_BRACKETS = {"(": ")", "[": "]", "{": "}"}

def annotate_file(lang, path):
    com = COMMENT[lang]
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    in_block = False        # /* */ 或 lua --[[ ]] 或 python 三引号
    triple = None           # python 三引号定界符
    in_template = False     # ts 反引号
    n_annotated = n_total = 0
    for ln in lines:
        stripped = ln.strip()
        # 块注释状态
        if lang in ("python",) and (triple or re.search(r"('''|\"\"\")", ln)):
            q = triple or (re.search(r"('''|\"\"\")", ln).group(1))
            cnt = ln.count(q)
            if triple:
                if cnt >= 1 and ln.rstrip().endswith(q):
                    triple = None
                out.append(ln); continue
            if cnt == 1:
                triple = q
            out.append(ln); continue
        if lang == "lua" and in_block:
            if "]]" in ln: in_block = False
            out.append(ln); continue
        if lang != "python" and lang != "lua":
            if in_block:
                out.append(ln)
                if "*/" in ln: in_block = False
                continue
            # 不对整行 /* 开头的块注释行加注释
            if stripped.startswith("/*") and "*/" not in stripped:
                in_block = True
                out.append(ln); continue
        if "'''" in ln or '"""' in ln:
            out.append(ln); continue
        if lang == "typescript" or lang == "dart":
            if in_template:
                if ln.count("`") >= 1: in_template = False
                out.append(ln); continue
            if ln.count("`") % 2 == 1:
                in_template = True
                out.append(ln); continue
        # 反引号出现的行（模板字符串/命令）跳过注释
        if "`" in ln:
            out.append(ln); continue
        # 行内已有注释（行首或行尾）→ 不重复
        already = (stripped.startswith(com) or stripped.startswith("/*") or stripped.startswith("*") or
                   (lang not in ("python", "r", "lua") and "//" in ln and not re.search(r'"[^"]*//[^"]*"', ln)) or
                   (lang in ("python", "r") and "#" in ln) or
                   (lang == "lua" and "--" in ln))
        # 字符串内引号不平衡 → 可能在跨行字符串，跳过
        qcount = len(re.findall(r'(?<!\\)"', ln)) + len(re.findall(r"(?<!\\)'", ln))
        n_total += 1
        if already or in_block or qcount % 2 == 1 or stripped.endswith("\\"):
            out.append(ln); continue
        note = annotate_line(lang, ln, None)
        if note and len(note) <= 60:
            sep = "  "
            out.append(f"{ln.rstrip()}{sep}{com} {note}")
            n_annotated += 1
        else:
            out.append(ln)
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return n_annotated, n_total

def all_files(lang):
    ext = EXT[lang]
    base = "{DSA}/".format(DSA=DSA) + ("ts" if lang == "typescript" else lang)
    for topic in sorted(os.listdir(base)):
        tdir = base + "/" + topic
        if not os.path.isdir(tdir):
            continue
        for prob in sorted(os.listdir(tdir)):
            pdir = tdir + "/" + prob
            if not os.path.isdir(pdir):
                continue
            for f in sorted(os.listdir(pdir)):
                if f.startswith("solution_") and f.endswith(ext):
                    yield pdir + "/" + f

def main():
    if sys.argv[1] == "--all":
        total_a = total_t = 0
        for lang in COMMENT:
            a = t = 0
            for f in all_files(lang):
                x, y = annotate_file(lang, f)
                a += x; t += y
            print(f"{lang}: {a}/{t} 行已注释")
            total_a += a; total_t += t
        print(f"TOTAL: {total_a}/{total_t}")
    else:
        lang = sys.argv[1]
        for f in sys.argv[2:]:
            a, t = annotate_file(lang, f)
            print(f"{os.path.basename(f)}: {a}/{t}")

if __name__ == "__main__":
    main()
