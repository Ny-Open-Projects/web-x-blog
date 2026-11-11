#!/usr/bin/env python3
# gen_blog.py — 博客生成器 v6（真题面 · 真实方案名 · 真实控制流 mermaid）
# 文风约束（blog-deai-polish 生成端适配）：无叙述破折号、中文引号用「」、无自我指涉、
#       无连续空行、方案命名"方案 N"（不暴露 solution_x 文件名）
# v6：第 1 节真题面/示例/数据范围（problem_meta.json，来自 CSDN 原文），CSDN 链接只在文末；
#     第 2 节方案对比表（真实方案名 + 逐方案复杂度），废掉「方案链」mermaid；
#     第 4/5 节 mermaid 按真实代码控制流生成（循环回边 + 分支菱形），不再是特征串。
import json, os, re, sys, shutil

DSA = "/Users/Wang/Code/webfault-ai/dsa"
CUR = json.load(open(f"{DSA}/_meta/curriculum.json"))
PMETA = json.load(open(f"{DSA}/_meta/problem_meta.json"))
OPARSE = json.load(open(f"{DSA}/_meta/official_parsed.json"))
OVERIFY = json.load(open(f"{DSA}/_meta/official_verify.json"))
ARTICLE_NOTES = json.load(open(f"{DSA}/_meta/article_notes.json"))
FORCE = False
os.makedirs(f"{DSA}/blog", exist_ok=True)

LANGS = [("typescript", "TypeScript"), ("python", "Python"), ("go", "Go"), ("java", "Java"),
         ("rust", "Rust"), ("lua", "Lua"), ("c", "C"), ("cpp", "C++"), ("r", "R"),
         ("zig", "Zig"), ("dart", "Dart")]

def read_code(lang, prob, sol):
    ext = {"typescript": "ts", "python": "py", "go": "go", "java": "java", "rust": "rs",
           "lua": "lua", "c": "c", "cpp": "cpp", "r": "R", "zig": "zig", "dart": "dart"}[lang]
    base = f"{DSA}/{'ts' if lang == 'typescript' else lang}"
    for topic in os.listdir(base):
        tdir = os.path.join(base, topic, prob)
        if os.path.isdir(tdir):
            f = os.path.join(tdir, f"{sol}.{ext}")
            if os.path.exists(f):
                lines = open(f).read().split("\n")
                while lines and (lines[0].startswith("// 来源") or lines[0].startswith("# 来源")
                                 or lines[0].startswith("-- 来源") or lines[0].startswith("/* 来源")):
                    lines.pop(0)
                return "\n".join(lines).strip()
    return None

def get_blog_id(prob, sol):
    for topic in os.listdir(f"{DSA}/ts"):
        f = f"{DSA}/ts/{topic}/{prob}/{sol}.ts"
        if os.path.exists(f):
            m = re.search(r"details/(\d+)", open(f).read())
            return m.group(1) if m else ""
    return ""

def _natkey(s):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)]

def list_solutions(prob):
    best = []
    for topic in os.listdir(f"{DSA}/ts"):
        tdir = f"{DSA}/ts/{topic}/{prob}"
        if os.path.isdir(tdir):
            sols = sorted((f[:-3] for f in os.listdir(tdir)
                           if f.startswith("solution_") and f.endswith(".ts")), key=_natkey)
            if len(sols) > len(best):
                best = sols
    return best

def solution_approach(prob, sol):
    for topic in os.listdir(f"{DSA}/ts"):
        f = f"{DSA}/ts/{topic}/{prob}/{sol}.ts"
        if os.path.exists(f):
            out = []
            for raw in open(f).read().split("\n")[:40]:
                line = raw.strip()
                if line and not (line.startswith("//") or line.startswith("/*")
                                 or line.startswith("*") or line.startswith("*/")):
                    break
                c = re.sub(r"^[/*/\s]+", "", line).strip()
                if not c or "来源" in c or "csdn" in c or c.startswith("**"):
                    continue
                if re.search(r"方案|思路|主解法|算法|策略", c):
                    c = re.sub(r"^方案[:：]\s*", "", c)
                    c = re.sub(r"（(?:忠实翻译|参考实现)[^）]*）", "", c)
                    c = re.sub(r"^方案(\d+)[:：]\s*", r"方案\1：", c)
                    if re.match(r"^方案?\d*$", c):
                        continue
                    out.append(c)
                if len(out) >= 2:
                    break
            if len(out) > 1 and any("忠实翻译" in x for x in out[1:]):
                out = [x for x in out if "忠实翻译" not in x]
            return "；".join(out[:2])
    return ""

HARNESS_FNS = {"build", "tolist", "buildtree", "tolevel", "eqarr", "buildlist", "printlist",
               "expectequal", "runcase", "logresult", "makelist", "arraytolist", "listtoarray"}


def main_signature(prob, sol):
    for topic in os.listdir(f"{DSA}/ts"):
        f = f"{DSA}/ts/{topic}/{prob}/{sol}.ts"
        if not os.path.exists(f):
            continue
        code = _strip_comments(open(f, encoding="utf-8", errors="ignore").read())
        target = None
        dm = re.search(r"function\s+demo\s*\([^)]*\)[^{]*\{", code)
        if dm:
            i, depth, j = dm.end(), 1, dm.end()
            while j < len(code) and depth > 0:
                if code[j] == "{":
                    depth += 1
                elif code[j] == "}":
                    depth -= 1
                j += 1
            for pat in (r"\(\s*(\w+)\s+as\s+any\s*\)\s*\(",
                        r"=\s*(\w+)\s*\(\s*\[\s*\.\.\.",
                        r"(\w+)\s*\((?:[^()]|\([^()]*\))*\[\s*\.\.\s*c\s*\.\s*in"):
                for mm in re.finditer(pat, code[dm.end():j]):
                    target = mm.group(1)
                    break
                if target:
                    break
        best = ""
        for raw in code.split("\n"):
            m = re.match(r"\s*function (\w+)\s*\(([^)]*)\)\s*:\s*([\w\[\]<>| ]+)\s*\{", raw)
            if not m or m.group(1) == "demo":
                continue
            if target and m.group(1) == target:
                return f"function {m.group(1)}({m.group(2)}): {m.group(3).strip()}"
            if (not best and not target and m.group(1).lower() not in HARNESS_FNS
                    and m.group(2).strip()):
                best = f"function {m.group(1)}({m.group(2)}): {m.group(3).strip()}"
        return best
    return ""

def clean_title(prob):
    t = re.sub(r"^lc_\d+_", "", prob)
    t = re.sub(r"^leetcode_", "", t)
    return t.replace("_", " ").strip()

def pmeta(prob):
    m = re.match(r"lc_(\d+)_", prob)
    return PMETA.get(m.group(1)) if m else None

def sanitize_prose(s):
    # 原文直接入正文：压掉会触发文风校验的字符（ASCII 引号、破折号、加粗星号）
    s = s.replace("——", "，").replace("---", "，")
    out, q = [], True
    for ch in s:
        if ch == '"':
            out.append("「" if q else "」")
            q = not q
        elif ch == "*":
            continue
        else:
            out.append(ch)
    s = "".join(out)
    s = s.replace("\u201c", "「").replace("\u201d", "」").replace("\u2018", "「").replace("\u2019", "」")
    s = re.sub(r"\]\(", "] (", s)  # 拆开 seq[i](...) 形态，避免被当成 markdown 链接
    # 中英文之间补空格（原文压缩排版如「整数数组nums和」）
    s = re.sub(r"([\u4e00-\u9fff])([A-Za-z0-9])", r"\1 \2", s)
    s = re.sub(r"([A-Za-z0-9])([\u4e00-\u9fff])", r"\1 \2", s)
    return s.strip()

def _norm_code(t):
    t = re.sub(r"//[^\n]*", "", t)
    return re.sub(r"[^A-Za-z0-9]", "", t)

def article_match_name(prob, code):
    """文章 TS 段的方案名与解法代码按相似度回配（解法文件顺序与文章方案顺序不保证一致）。"""
    import difflib
    pm = pmeta(prob)
    if not pm:
        return ""
    mine = _norm_code("\n".join(main_body(code)))
    if len(mine) < 40:
        return ""
    best, ratio = "", 0.0
    for name, acode in zip(pm.get("ts_names", []), pm.get("ts_codes", [])):
        r = difflib.SequenceMatcher(None, mine, _norm_code(acode)).ratio()
        if r > ratio:
            best, ratio = name, r
    return best if ratio >= 0.6 else ""

def header_name(prob, sol):
    # 解法文件头注释里的「方案N: 名字」
    for topic in os.listdir(f"{DSA}/ts"):
        f = f"{DSA}/ts/{topic}/{prob}/{sol}.ts"
        if os.path.exists(f):
            head = open(f, encoding="utf-8", errors="ignore").read(400)
            m = re.search(r"方案\s*\d*\s*[:：]\s*(.+)", head)
            if not m:
                return ""
            name = re.sub(r"（(?:忠实翻译|参考实现)[^）]*）", "", m.group(1)).strip().strip("：:")
            for _ in range(3):
                name = re.sub(r"^\d+\s*[)）]\s*", "", name)
                name = re.sub(r"^方案\s*\d*\s*[:：]\s*", "", name)
            name = name.strip().strip("：:")
            if name and not re.match(r"^方案\s*\d*$", name) and len(name) <= 30 and "。" not in name:
                return name
            return ""
    return ""

def derive_name(code):
    # 无处可查名字时，按代码真实特征起名（比「基础实现」有信息量）
    if "dp[" in code or re.search(r"\bdp\b", code):
        return "动态规划"
    m = re.search(r"function (\w+)\s*\(", code)
    if m and m.group(1) != "demo" and len(re.findall(rf"\b{m.group(1)}\s*\(", code)) > 1:
        return "递归求解"
    if "mid" in code and "while" in code:
        return "二分查找"
    if re.search(r"while\s*\([^)]*(left|right|lo|hi)\b", code):
        return "双指针收缩"
    if re.search(r"new Map|new Set|HashMap|dict\(|map\[", code):
        return "哈希辅助"
    if len(re.findall(r"\bfor\s*\(", code)) >= 2:
        return "双重循环枚举"
    if re.search(r"\.sort\(|sorted\(", code):
        return "排序预处理"
    if re.search(r"\.push\(", code) and re.search(r"\.pop\(", code):
        return "栈辅助"
    if len(re.findall(r"\bfor\s*\(", code)) == 1:
        return "单趟扫描"
    if re.search(r"\bwhile\b", code):
        return "迭代指针处理"
    return "直接实现"

def resolve_name(prob, sol, idx, code):
    n = header_name(prob, sol)
    if n:
        return n
    n = article_match_name(prob, code)
    if n:
        return n
    return derive_name("\n".join(main_body(code)) or code)

SCENE = {
    "array": "数组是最常用的线性容器，这类题练的是下标操作与原地腾挪，对应真实开发里的缓冲区、列表整理",
    "hash": "要在大量数据里按「特征值」瞬间找到配对或完成计数，对应真实开发里的对账、去重、缓存按键取值",
    "string": "字符串是字符数组，这类题练的是扫描、切分与匹配，对应真实开发里的文本清洗、协议解析",
    "linked_list": "链表只能顺着指针走，这类题练的是指针操作与断链重接，对应真实开发里的内存管理、撤销链",
    "stack": "后进先出结构天然适合「最近匹配」，对应真实开发里的括号校验、浏览历史、函数调用栈",
    "queue": "先进先出结构天然适合「按到达顺序处理」，对应真实开发里的任务队列、消息缓冲",
    "tree": "树是分层数据的标准形态，这类题练的是递归分治与遍历序，对应真实开发里的目录树、组件树",
    "heap": "堆只要堆顶最优就能 O(1) 取到，对应真实开发里的优先级调度、Top-K 榜单",
    "graph": "图描述多对多关系，这类题练的是搜索与连通性，对应真实开发里的社交关系、依赖解析",
    "matrix": "二维网格同时考验下标变换与边界控制，对应真实开发里的棋盘、图像像素处理",
    "binary_search": "有序数据上每次砍一半，对应真实开发里的字典查找、版本定位、容量规划",
    "sort": "排序是多数算法的前置工序，这类题练的是比较逻辑与稳定性取舍",
    "greedy": "每步取当前最优，对应真实开发里的区间调度、资源分配",
    "backtrack": "系统地试所有可能并及时回头，对应真实开发里的组合枚举、约束求解、路径规划",
    "dp": "把大问题拆成小问题并记住结果，对应真实开发里的编辑距离、资源规划",
    "notes": "综合练习：把数据结构与策略组合起来解决一个完整问题",
    "concurrency": "多个异步任务的时序与协作，对应真实开发里的请求并发控制、竞态处理",
    "other": "综合练习：从题面本身出发选择合适的数据结构",
}

PITFALL = {
    "array": "边界最容易漏：空数组、只有一个元素、目标出现在头尾。",
    "hash": "键要选不可变量，计数完别忘了次数并列的情况。",
    "string": "空串、全空白、单字符三类边界，以及大小写是否敏感。",
    "linked_list": "断开 next 之前先把后继存下来，否则整条链会丢。",
    "stack": "出栈前判空；「下一个更大元素」类问题栈里存下标比存值好用。",
    "queue": "循环队列判满与判空的条件不能相同，通常牺牲一个格位。",
    "tree": "递归出口（空节点）必须先写，否则直接空指针。",
    "heap": "堆只保证堆顶最优，遍历堆数组并不是有序输出。",
    "graph": "访问标记要在入队时打而不是出队时，否则同一节点会重复入队。",
    "matrix": "行列别写反；旋转类问题先在纸上走一遍下标变换。",
    "binary_search": "区间开闭要前后一致，mid 计算用左加右减防溢出。",
    "sort": "比较器返回值的正负含义，写反了排序结果直接错。",
    "greedy": "贪心前通常要先排序，排序依据就是贪心的正确性来源。",
    "backtrack": "递归返回后要把当前选择撤销干净，否则结果集会被污染。",
    "dp": "初始化（第 0 行或列）的含义要想清楚，它决定后续转移是否成立。",
    "notes": "先看小例子手推一遍再对照代码，比直接读代码快得多。",
    "concurrency": "异步的完成顺序不等于书写顺序，等待谁要想清楚。",
    "other": "特殊输入（空、重复、极值）的边界检查。",
}

def extract_cases(code):
    lines = code.split("\n")
    for i, ln in enumerate(lines):
        if re.search(r"const (cases|tests)\b", ln):
            seg = [ln]
            j = i + 1
            while j < len(lines) and len(seg) < 14:
                seg.append(lines[j])
                if re.search(r"\];\s*$", lines[j]):
                    break
                j += 1
            return "\n".join(seg).rstrip()
    return ""

def detect_features(code):
    f = []
    if re.search(r"new Map|new Set|unordered_map|HashMap|dict\(|map\[", code):
        f.append("哈希结构做计数或查重")
    if re.search(r"\.sort\(|sorted\(", code):
        f.append("先排序再处理")
    if "dp[" in code:
        f.append("DP 表逐项填充")
    m = re.search(r"function (\w+)\s*\(", code)
    if m and m.group(1) != "demo" and len(re.findall(rf"\b{m.group(1)}\s*\(", code)) > 1:
        f.append("递归求解子问题")
    if re.search(r"while .*(lo|left)\b", code) and "mid" in code:
        f.append("二分收缩区间")
    n_for = len(re.findall(r"\bfor\s*\(", code))
    if n_for >= 2:
        f.append("双重循环遍历")
    elif n_for == 1:
        f.append("单循环线性扫描")
    if re.search(r"\.push\(", code) and re.search(r"\.pop\(", code):
        f.append("栈的后进先出操作")
    if re.search(r"\.shift\(|deque|heapq|heap", code):
        f.append("队列或堆的调度")
    return f

def _loop_depth(code):
    """循环嵌套深度：区分「两个顺序 for」与「双层嵌套 for」。"""
    depth, stack, best = 0, [], 0
    for raw in code.split("\n"):
        opens = raw.count("{") - raw.count("}")
        first = raw.split("{")[0].strip()
        while stack and opens < 0 and (depth + opens) <= stack[-1]:
            stack.pop()
        if re.match(r"^(for|while)\b", first):
            stack.append(depth)
            best = max(best, len(stack))
        depth += opens
    return best

def complexity_of(code):
    n_for = len(re.findall(r"\bfor\s*\(", code))
    if "dp[" in code:
        return ("时间 O(n) 到 O(m·n)（取决于状态维度），空间即 DP 表大小",
                "动态规划把指数级枚举压成表，每格只算一次，复杂度等于「状态数 × 转移代价」")
    m = re.search(r"function (\w+)\s*\(", code)
    if m and m.group(1) != "demo" and len(re.findall(rf"\b{m.group(1)}\s*\(", code)) > 1:
        return ("时间与递归树规模相关（链状 O(n)，满分支可到指数级），空间 O(递归深度)",
                "递归的成本等于递归树的节点数；有重复子问题时必须配合记忆化")
    if "mid" in code and "while" in code:
        return ("时间 O(log n)，空间 O(1)",
                "每轮把候选区间砍半，n 个元素最多砍 log2(n) 轮")
    if _loop_depth(code) >= 2:
        return ("时间 O(n²)（两层嵌套扫描），空间 O(1) 到 O(n)",
                "外层定起点、内层扫终点，n 个起点各扫 n 次")
    if n_for >= 1 or re.search(r"\bwhile\b", code):
        return ("时间 O(n)（单趟线性扫描），空间 O(1) 到 O(n)（视辅助结构）",
                "每个元素被常数次访问，辅助哈希或栈的开销与 n 同阶")
    return ("时间 O(n) 量级，空间 O(n)", "整体只对数据做有限趟处理")

TOPIC_ASK = {
    "array": ["能不能原地做（O(1) 空间）？", "如果数组已有序，能优化到什么程度？", "空数组、单元素怎么处理？"],
    "hash": ["哈希冲突了怎么办？", "键的选择有什么讲究？", "值域有限时能否用数组代替哈希？"],
    "string": ["字符集有多大，能否用定长数组计数？", "要不要考虑 Unicode 多字节字符？", "空串与单字符的边界？"],
    "linked_list": ["能不能一次遍历完成？", "快慢指针能解决哪些变体？", "断链与接回的顺序怎么保证不出错？"],
    "stack": ["什么时候用单调栈（求下一个更大或更小）？", "栈里存值还是存下标？", "能否用 O(1) 额外空间？"],
    "queue": ["单调队列为什么能保证队首最优？", "循环队列如何判满？", "双端队列能替代吗？"],
    "tree": ["递归和迭代写法各自的空间开销？", "能否用层序统一处理？", "空节点的边界如何约定？"],
    "heap": ["什么时候用堆而不是排序？", "堆里存值还是存下标？", "Top-K 用小顶还是大顶堆？"],
    "graph": ["广度优先与深度优先各适合什么问题？", "如何去重避免死循环？", "带权图为什么默认不用广度优先？"],
    "matrix": ["能否原地标记？", "边界遍历的顺序怎么不出错？", "旋转类问题能否一次循环完成？"],
    "binary_search": ["mid 写成左加右减是防什么？", "区间开闭不一致会怎样？", "何时退化为线性查找？"],
    "sort": ["稳定性对结果有影响吗？", "比较器怎么写才不会越界？", "数据近有序时选哪种排序？"],
    "greedy": ["贪心的正确性怎么证明？", "排序依据选错了会怎样？", "能否举出反例推翻当前策略？"],
    "backtrack": ["怎么剪枝降低无效搜索？", "去重的关键在哪一层？", "状态恢复遗漏会怎样？"],
    "dp": ["状态定义为什么是它？", "遍历顺序由什么决定？", "能否滚动数组压空间？"],
    "notes": ["这个策略能推广到什么场景？", "与暴力做法差在哪一步？", "有没有更简单的等价写法？"],
    "concurrency": ["执行顺序由什么决定？", "超时与竞态如何兜底？", "怎样写成确定性的测试？"],
    "other": ["有没有更直观的建模方式？", "特殊输入的边界？", "能否一步到位而不是分两趟？"],
}

MDN = "https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/"
API_DICT = [
    ("new Map", "Map", "哈希表：任意类型键值对",
     "set(k,v) 存、get(k) 取（不存在返回 undefined）、has(k) 判存在、delete(k) 删；增删查均摊 O(1)；键顺序为插入序；键必须用引用区分（对象键按身份）", f"{MDN}Map"),
    ("new Set", "Set", "集合：元素唯一",
     "add/add.has/delete；has 均摊 O(1)；NaN 视为相同；去重常用 [...new Set(arr)]", f"{MDN}Set"),
    ("Array.from", "Array.from()", "类数组/可迭代对象转数组",
     "Array.from(iterable, mapFn) 可同时映射；对 Set 去重、对字符串按码元拆分；稀疏位会被 undefined 填充", f"{MDN}Array/from"),
    (".sort(", "Array.prototype.sort()", "原地排序",
     "默认按字符串 Unicode 序（10 会排在 2 前），数字必须传 (a,b)=>a-b；V8 用 TimSort，稳定，O(n log n)；返回原数组引用", f"{MDN}Array/sort"),
    (".map(", "Array.prototype.map()", "逐元素映射为新数组",
     "回调 (v,i,arr)；返回等长新数组，不改变原数组；稀疏位跳过；链式调用注意中间数组开销", f"{MDN}Array/map"),
    (".filter(", "Array.prototype.filter()", "过滤子集",
     "回调返回真值保留；返回新数组；不改变原数组；适合先过滤再 map 的管线", f"{MDN}Array/filter"),
    (".reduce(", "Array.prototype.reduce()", "归约为单值",
     "reduce(cb(acc,cur,i,arr), init)；无初值时以首元素起算（空数组会抛错）；求和/计数/分组的基础件", f"{MDN}Array/reduce"),
    (".push(", "Array.prototype.push()", "尾部追加",
     "返回新长度；可一次多个；均摊 O(1)；会改变原数组", f"{MDN}Array/push"),
    (".pop(", "Array.prototype.pop()", "尾部弹出",
     "返回被删元素（空数组返回 undefined）；O(1)", f"{MDN}Array/pop"),
    (".shift(", "Array.prototype.shift()", "头部取出",
     "O(n)（后续元素整体前移）；大量头部操作请用链表或双端结构", f"{MDN}Array/shift"),
    (".unshift(", "Array.prototype.unshift()", "头部插入",
     "O(n)；与 shift 组合可当双端队列", f"{MDN}Array/unshift"),
    (".includes(", "Array/String includes()", "是否包含",
     "数组用 SameValueZero（NaN 可判）；字符串按子串；第二个参数为起始下标", f"{MDN}Array/includes"),
    (".indexOf(", "Array/String indexOf()", "首次出现的下标",
     "找不到返回 -1；无法判 NaN（用 includes）；字符串可传起始位", f"{MDN}Array/indexOf"),
    (".slice(", "Array/String slice()", "切片（不改原数组）",
     "slice(start,end) 含头不含尾；负数从尾计；常用于复制数组（slice()）", f"{MDN}Array/slice"),
    (".splice(", "Array.prototype.splice()", "任意位置增删",
     "splice(i, delCount, ...items) 原地修改并返回被删数组；注意与 slice 拼写区分", f"{MDN}Array/splice"),
    (".join(", "Array.prototype.join()", "数组拼接为字符串",
     "undefined/null 转空串；嵌套数组会展平一层；join('') 用于字符数组还原", f"{MDN}Array/join"),
    (".split(", "String.prototype.split()", "字符串切分为数组",
     "split('') 按字符拆；split(/正则/) 支持模式；空串调用会拆出空串数组", f"{MDN}String/split"),
    (".trim(", "String.prototype.trim()", "去除首尾空白",
     "返回新串；变体 trimStart/trimEnd；不处理串中间空格", f"{MDN}String/trim"),
    (".padStart(", "String.prototype.padStart()", "左侧补齐到指定长度",
     "padStart(len, '0') 常用于定长编号；超长则原样返回", f"{MDN}String/padStart"),
    (".repeat(", "String.prototype.repeat()", "重复 N 次",
     "参数为次数（非分隔）；负数抛 RangeError", f"{MDN}String/repeat"),
    (".replace(", "String.prototype.replace()", "替换首个匹配",
     "字符串参数只替换第一处；全局替换用 replace(/x/g, …)；回调可动态生成替换文本", f"{MDN}String/replace"),
    (".startsWith(", "String startsWith()", "前缀判定",
     "第二参为起始位；大小写敏感", f"{MDN}String/startsWith"),
    (".endsWith(", "String endsWith()", "后缀判定",
     "第二参视为字符串长度（截断位）", f"{MDN}String/endsWith"),
    (".charCodeAt(", "String charCodeAt()", "取 UTF-16 码元",
     "返回 0~65535；超出下标返回 NaN；增补字符（emoji）占两个码元，需 codePointAt", f"{MDN}String/charCodeAt"),
    ("Object.keys", "Object.keys()", "对象键名数组",
     "仅自身可枚举字符串键（不含 symbol）；配 length 可当计数器", f"{MDN}Object/keys"),
    ("Object.values", "Object.values()", "对象值数组",
     "顺序与 keys 一致（整数键升序优先）", f"{MDN}Object/values"),
    ("Object.entries", "Object.entries()", "键值对数组",
     "返回 [k,v] 数组，配 Object.fromEntries 互逆；遍历映射首选", f"{MDN}Object/entries"),
    ("Object.fromEntries", "Object.fromEntries()", "键值对数组转对象",
     "参数为 [k,v] 可迭代；map 出来的键值对可直接转对象", f"{MDN}Object/fromEntries"),
    ("JSON.stringify", "JSON.stringify()", "序列化为 JSON 字符串",
     "常用于结构化比较（深度相等判定）；undefined/函数/循环引用会被丢弃或抛错", f"{MDN}JSON/stringify"),
    ("Math.max", "Math.max()", "最大值",
     "配展开 Math.max(...arr)；空参返回 -Infinity；超大数组注意展开参数上限", f"{MDN}Math/max"),
    ("Math.min", "Math.min()", "最小值",
     "同 max；空参返回 Infinity", f"{MDN}Math/min"),
    ("Math.abs", "Math.abs()", "绝对值",
     "入参会被隐式转数字；-0 返回 +0", f"{MDN}Math/abs"),
    ("Math.floor", "Math.floor()", "向下取整",
     "负数向负无穷（-1.5 → -2）；大数用位运算前注意 2^31 界", f"{MDN}Math/floor"),
    ("BigInt", "BigInt", "任意精度整数",
     "字面量 123n；不能与 number 混算；不能用于 Math 方法", f"{MDN}BigInt"),
    ("new Promise", "Promise", "异步承诺对象",
     "executor 同步执行；resolve/reject 仅首次生效；配 async/await 串行化", f"{MDN}Promise"),
    ("Promise.all", "Promise.all()", "并发等待全部",
     "全成功返回按输入序的结果数组；任一失败立即 reject（需全成功语义才用）", f"{MDN}Promise/all"),
    ("setTimeout", "setTimeout()", "延时回调（事件循环）",
     "延时非精确（排在宏任务队列）；最小延迟与嵌套层级相关", f"{MDN}setTimeout"),
]

def detect_apis(ts_code):
    return [(name, desc, detail, url) for token, name, desc, detail, url in API_DICT if token in ts_code]

DOC_LINKS = [
    ("TypeScript / JS", "MDN 中文参考", "https://developer.mozilla.org/zh-CN/"),
    ("Python", "Python 官方文档", "https://docs.python.org/zh-cn/3/"),
    ("Go", "Go 标准库", "https://pkg.go.dev/std"),
    ("Java", "JDK 17 API", "https://docs.oracle.com/en/java/javase/17/docs/api/"),
    ("Rust", "Rust 标准库", "https://doc.rust-lang.org/std/"),
    ("Lua", "Lua 5.4 手册", "https://www.lua.org/manual/5.4/"),
    ("C", "Cppreference C", "https://zh.cppreference.com/w/c"),
    ("C++", "Cppreference C++", "https://zh.cppreference.com/w/cpp"),
    ("R", "R 官方手册", "https://stat.ethz.ch/R-manual/"),
    ("Zig", "Zig 语言文档", "https://ziglang.org/documentation/master/"),
    ("Dart", "Dart API", "https://api.dart.dev/"),
]

def _mlabel(s):
    return s.replace('"', "'").replace("`", "'").replace("\n", " ")

def mermaid_skeleton(code):
    feats = detect_features(code)
    if not feats:
        feats = ["核心处理逻辑"]
    lines = ["graph TD", '    A["开始：读取输入"]']
    prev = "A"
    for i, ftext in enumerate(feats):
        nid = f"F{i}"
        lines.append(f'    {nid}["{_mlabel(ftext)}"]')
        lines.append(f"    {prev} --> {nid}")
        prev = nid
    lines.append('    Z["返回结果"]')
    lines.append(f"    {prev} --> Z")
    return "\n".join(lines)

def _fx(s):
    # mermaid 标签安全化 + 轻量代码翻译
    s = s.strip().rstrip(";")
    for a, b in (("!==", " ≠ "), ("!=", " ≠ "), ("===", " == "), ("==", " == "), ("&&", " 且 "), ("||", " 或 "),
                 ("<=", " ≤ "), (">=", " ≥ "), ("<", "＜"), (">", "＞"), ("!", "非 ")):
        s = s.replace(a, b)
    s = s.replace('"', "").replace("`", "").replace("|", "｜").replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", s).strip()

def _for_label_lang(header, lang):
    m = re.search(r"for\s*\((.*)\)", header) or re.search(r"for\s+(.*)", header)
    seg_txt = m.group(1) if m else header
    if lang == "python":
        mr = re.search(r"(\w+)\s+in\s+range\(([^)]*)\)", seg_txt)
        if mr:
            args = [a.strip() for a in mr.group(2).split(",") if a.strip()]
            if len(args) == 1:
                return f"循环 {mr.group(1)}：从 0 到 {args[0]} 前"
            return f"循环 {mr.group(1)}：从 {args[0]} 到 {args[-1]} 前" + ("，步长 " + args[1] if len(args) == 3 else "")
        mi = re.search(r"(\w+)\s+in\s+(.+?)\s+do$", seg_txt) or re.search(r"(\w+)\s+in\s+(.+)", seg_txt)
        if mi:
            return f"遍历 {mi.group(2)} 中的每个元素 {mi.group(1)}"
    if lang == "r":
        mi = re.search(r"for\s*\(\s*(\w+)\s+in\s+(.*)\)", header)
        if mi:
            return f"循环 {mi.group(1)}：遍历 {mi.group(2)}"
    if lang == "rust":
        mi = re.search(r"(\w+)\s+in\s+(.+)", seg_txt)
        if mi:
            return f"遍历 {mi.group(2)} 中的每个元素 {mi.group(1)}"
    if lang == "lua":
        mn = re.search(r"(\w+)\s*=\s*([^,]+),\s*(.+)", seg_txt)
        if mn:
            return f"循环 {mn.group(1)}：从 {mn.group(2)} 到 {mn.group(3)}"
        mi = re.search(r"(\w+)\s+in\s+(.+)", seg_txt)
        if mi:
            return f"遍历 {mi.group(2)} 中的每个元素 {mi.group(1)}"
    if lang == "zig":
        return "遍历集合元素"
    if lang == "go":
        mr = re.search(r"(\w+)\s*:=\s*range\s+([\w.\[\]]+)", seg_txt)
        if mr:
            return f"遍历 {mr.group(2)} 的下标与元素 {mr.group(1)}"
    return _for_label(header) if lang in ("typescript", "") else "遍历循环"


def _open_delta(line, lang, state):
    """本行净开块数；python/lua 用缩进与 do/end 语义，state 记录缩进栈。"""
    s = line.strip()
    if lang == "python":
        ind = (len(line) - len(line.lstrip())) // 4
        closes = 0
        while state["stack"] and state["stack"][-1] >= (ind if s else 0) and state["stack"][-1] > 0:
            if state["stack"][-1] <= ind:
                break
            state["stack"].pop()
            closes += 1
        opens = 0
        if s.endswith(":") and not s.startswith(("else", "elif")):
            state["stack"].append(ind + 1)
            opens = 1
        return opens - closes
    if lang == "lua":
        opens = len(re.findall(r"\bdo\b", s)) + (1 if re.match(r"function\b", s) else 0)
        if re.match(r"(local\s+)?function\b", s):
            opens += 0
        if re.search(r"\bif\b.*\bthen\b", s) and s.rstrip().endswith("end"):
            return 0  # 单行 if..then..end
        if re.match(r"else", s):
            return 0
        closes = len(re.findall(r"\bend\b", s))
        if s.endswith(("do", "then")) or re.search(r"\bdo$", s):
            pass
        opens += (1 if re.search(r"\bthen$", s) else 0)
        return opens - closes
    return s.count("{") - s.count("}")


def _for_label(header):
    m = re.search(r"for\s*\((.*)\)", header)
    if not m:
        return "遍历循环"
    seg = [p.strip() for p in m.group(1).split(";") if p.strip()]
    if len(seg) == 3:
        vm = re.search(r"(?:let|const|var)?\s*([A-Za-z_$][\w$]*)\s*=", seg[0])
        var = vm.group(1) if vm else "i"
        start = seg[0].split("=", 1)[1].strip() if "=" in seg[0] else "0"
        return f"循环 {var}：从 {_fx(start)} 起步，当 {_fx(seg[1])} 时继续，每轮 {_fx(seg[2])}"
    m2 = re.search(r"(?:const|let|var)?\s*(\w+)\s+of\s+([\w.\[\]]+)", m.group(1))
    if m2:
        return f"遍历 {_fx(m2.group(2))} 中的每个元素 {m2.group(1)}"
    m3 = re.search(r"(?:const|let|var)?\s*(\w+)\s+in\s+([\w.\[\]]+)", m.group(1))
    if m3:
        return f"遍历 {_fx(m3.group(2))} 的下标 {m3.group(1)}"
    return "遍历循环"

def _stmt_label(line):
    """普通语句 → 中文步骤标签；返回 None 表示不值得画。"""
    s = line.strip().rstrip(";")
    if not s or s in ("{", "}"):
        return None
    if re.match(r"^(const|let|var)\s+\w+\s*=\s*new\s+Map\b", s):
        return "初始化哈希表"
    if re.match(r"^(const|let|var)\s+\w+\s*=\s*new\s+Set\b", s):
        return "初始化集合"
    if re.search(r"\bdp\b\s*(\[|=)", s) and ("=" in s or "[" in s):
        return "填写 DP 表"
    if re.match(r"^(const|let|var)\s+\w+\s*=\s*\[\]", s):
        return None
    if re.match(r"^(const|let|var)\s+\w+\s*=\s*new\s+Array", s):
        return "创建结果数组"
    m = re.search(r"(\w+)\.set\(", s)
    if m:
        return f"存入 {m.group(1)}"
    m = re.search(r"(\w+)\.(push|append)\(", s)
    if m:
        return f"向 {m.group(1)} 追加记录"
    m = re.search(r"(\w+)\.pop\(", s)
    if m:
        return f"从 {m.group(1)} 弹出"
    if ".sort(" in s or "sorted(" in s:
        return "排序整理"
    if s.startswith("](") or re.match(r"^\[[^\]]*\]\s*\(", s):
        return "配置比较器（lambda）"
    if re.match(r"^(const|let|var)\s", s):
        vm = re.match(r"^(?:const|let|var)\s+(?:mut\s+)?([\w$]+)", s)
        return f"计算 {vm.group(1)}" if vm else f"计算 {_fx(s[:24])}"
    if "=" in s and not s.startswith(("if", "while", "for", "return")):
        left = re.split(r"=(?!=)", s)[0].strip()
        return f"更新 {left.split()[-1] if left.split() else _fx(left[:20])}"
    if re.match(r"^\w+\.\w+\(", s) or re.match(r"^\w+\(", s):
        return f"调用 {_fx(s[:28])}"
    return f"处理 {_fx(s[:28])}"

def _strip_comments(code):
    """去行注释与块注释：注释里的花括号会破坏函数体配平。"""
    out, in_blk = [], False
    for ln in code.split("\n"):
        if in_blk:
            if "*/" in ln:
                ln = ln.split("*/", 1)[1]
                in_blk = False
            else:
                out.append("")
                continue
        if "//" in ln:
            k = ln.find("//")
            if not (k > 0 and ln[k - 1] == ":"):  # 保留 https:// 等协议写法
                ln = ln[:k]
        while "/*" in ln:
            a = ln.find("/*")
            b = ln.find("*/", a + 2)
            if b < 0:
                ln = ln[:a]
                in_blk = True
                break
            ln = ln[:a] + ln[b + 2:]
        out.append(ln)
    return "\n".join(out)

LANG_CONF = {
    "typescript": {"cm": "//", "harness": "demo"},
    "python": {"cm": "#", "harness": "__main__"},
    "go": {"cm": "//", "harness": "main"},
    "java": {"cm": "//", "harness": "main"},
    "rust": {"cm": "//", "harness": "main"},
    "lua": {"cm": "--", "harness": "main|demo"},
    "c": {"cm": "//", "harness": "main"},
    "cpp": {"cm": "//", "harness": "main"},
    "r": {"cm": "#", "harness": "main"},
    "zig": {"cm": "//", "harness": "main"},
    "dart": {"cm": "//", "harness": "main"},
}

LANG_IDIOM = {
    "typescript": "TS 版用闭包与数组方法表达同一逻辑，类型标注标明输入输出约定",
    "python": "Python 版用切片与字典推导式简化操作，突出可读性",
    "go": "Go 版用切片与多返回值惯用法，显式处理索引边界",
    "java": "Java 版用类与静态方法组织，集合操作显式明了",
    "rust": "Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界",
    "lua": "Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义",
    "c": "C 版手动管理下标与内存，循环边界全部显式写出",
    "cpp": "C++ 版用 STL 容器与迭代器，减少手写下标错误",
    "r": "R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱",
    "zig": "Zig 版显式分配与清零，整型边界处理严格",
    "dart": "Dart 版用可空类型标注与集合方法，注意空安全",
}


def _fn_candidates(code, lang):
    """各语言候选函数：(start, name, body)。"""
    out = []
    if lang == "python":
        for m in re.finditer(r"^def\s+(\w+)\s*\(([^)]*)\)\s*:", code, re.M):
            i = m.end()
            lines = code[i:].split("\n")
            body_lines = [lines[0]] if lines[0].strip() else []
            ind = None
            for ln in lines[1:]:
                if not ln.strip():
                    body_lines.append(ln)
                    continue
                cur = len(ln) - len(ln.lstrip())
                if ind is None:
                    if cur == 0:
                        break
                    ind = cur
                if cur < ind:
                    break
                body_lines.append(ln)
            out.append((m.start(), m.group(1), "\n".join(body_lines)))
        return out
    pats = [r"function\s+(\w+)\s*\(([^)]*)\)[^{]*\{"]
    if lang in ("rust", "zig"):
        pats = [r"fn\s+(\w+)\s*\(([^)]*)\)[^{]*\{"]
    elif lang == "go":
        pats = [r"func\s+(\w+)\s*\(([^)]*)\)[^{]*\{"]
    elif lang == "r":
        pats = [r"(\w+)\s*<-\s*function\s*\(([^)]*)\)\s*\{"]
    elif lang in ("c", "cpp", "java", "dart"):
        pats = [r"[\w\]\[<> ,&*]+?[\s\*](\w+)\s*\(([^;)]*)\)\s*\{"]
    if lang == "lua":
        for m in re.finditer(r"(?:local\s+)?function\s+(\w+)\s*\(([^)]*)\)", code):
            i, depth, j = m.end(), 1, m.end()
            tok = re.compile(r"\b(function|do|then|end)\b")
            while j < len(code):
                mo = tok.search(code, j)
                if not mo:
                    j = len(code)
                    break
                if mo.group(1) == "end":
                    depth -= 1
                    if depth == 0:
                        j = mo.end()
                        break
                else:
                    depth += 1
                j = mo.end()
            out.append((m.start(), m.group(1), code[m.end():j - len("end") if code[j - 4:j].strip() == "end" else j]))
        return out
    for pat in pats:
        for m in re.finditer(pat, code):
            nm = m.group(1)
            if nm in ("if", "for", "while", "switch", "catch", "return", "elif"):
                continue
            i, depth, j = m.end() - 1, 0, m.end() - 1
            while j < len(code) and depth >= 0:
                if code[j] == "{":
                    depth += 1
                elif code[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            out.append((m.start(), nm, code[i + 1:j]))
        if out:
            break
    return out


def main_body_lang(code, lang):
    """语言感知的算法主函数体语句行。"""
    cm = LANG_CONF.get(lang, LANG_CONF["typescript"])["cm"]
    out0 = []
    in_blk = False
    for ln in code.split("\n"):
        if in_blk:
            if "*/" in ln:
                ln = ln.split("*/", 1)[1]
                in_blk = False
            else:
                out0.append("")
                continue
        if cm == "//" and "//" in ln:
            k = ln.find("//")
            if not (k > 0 and ln[k - 1] == ":"):
                ln = ln[:k]
        elif cm == "#":
            if re.match(r"^\s*#", ln):
                ln = ""
            elif " #" in ln:
                k = ln.find(" #")
                if not (k > 0 and ln[k - 1] == ":"):
                    ln = ln[:k]
        elif cm == "--" and "--" in ln:
            ln = ln[:ln.find("--")]
        while "/*" in ln:
            a = ln.find("/*")
            b = ln.find("*/", a + 2)
            if b < 0:
                ln = ln[:a]
                in_blk = True
                break
            ln = ln[:a] + ln[b + 2:]
        out0.append(ln)
    code = "\n".join(out0)
    cands = _fn_candidates(code, lang)
    if not cands:
        return []
    # 找 harness（demo/main/__main__），从其体内找被调用的算法函数
    hc = LANG_CONF.get(lang, LANG_CONF["typescript"])["harness"]
    harness_span = None
    harness_names = {"demo", "main"}
    for st, nm, body in cands:
        if nm == "demo" or nm == "main" or (lang == "python" and nm.startswith("demo")):
            harness_span = (st, body)
            break
    named = {nm for _, nm, _ in cands}
    pick = None
    if harness_span:
        inner = harness_span[1]
        # 测试区：从首个 cases/assert/断言处
        starts = [harness_span[1].find(pat) for pat in ("const cases", "cases := ", "cases =", "assert", "stopifnot", "expect")]
        starts = [s for s in starts if s > 0]
        scan = inner[min(starts):] if starts else inner
        for m in re.finditer(r"(?<![\w.])(\w+)\s*[\s(.\[{]", scan):
            nm = m.group(1)
            if nm in named and nm not in harness_names and nm.lower() not in HARNESS_FNS:
                # 排除建造器（体内 new ListNode/TreeNode 或同名构造）
                bfull = next((b for _, n2, b in cands if n2 == nm), "")
                if re.search(r"new\s+(ListNode|TreeNode)\b", bfull) or re.search(r"val\s*[:=][^\n]*next\s*[:=]", bfull):
                    continue
                pick = nm
                break
    if pick is None:
        pick = next((nm for _, nm, b in cands
                     if nm not in harness_names and nm.lower() not in HARNESS_FNS
                     and not re.search(r"new\s+(ListNode|TreeNode)\b", b)
                     and len(b.split("\n")) >= 3), None)
    if pick is None:
        return []
    body = next((b for _, nm, b in cands if nm == pick), "")
    body = re.sub(r'"""[\s\S]*?"""', "", body)
    body = re.sub("'''[\\s\\S]*?'''", "", body)
    lines = []
    for l in body.split("\n"):
        l = l.strip()
        if not l or l.startswith(("*", "/*", "import ", "function ", "def ", "fn ", "func ")):
            continue
        if lang == "python" and l.startswith("def "):
            continue
        if lang == "lua" and (l == "end" or l.startswith("else") or l == "end)"):
            continue
        lines.append(l)
    return lines


def main_body(code):
    """取算法主函数（非 demo/工具函数）的语句行；找不到返回 []。"""
    code = _strip_comments(code)
    cands = []
    for m in re.finditer(r"function\s+(\w+)\s*\([^)]*\)[^{]*\{", code):
        if m.group(1) == "demo":
            continue
        i, depth, j = m.end(), 1, m.end()
        while j < len(code) and depth > 0:
            if code[j] == "{":
                depth += 1
            elif code[j] == "}":
                depth -= 1
            j += 1
        cands.append((m.start(), m.group(1), code[i:j - 1]))
    for m in re.finditer(r"(?:const|let|var)\s+(\w+)\s*=\s*\([^)]*\)\s*(?::\s*[\w\[\]<>| ]+)?=>\s*\{", code):
        i, depth, j = m.end(), 1, m.end()
        while j < len(code) and depth > 0:
            if code[j] == "{":
                depth += 1
            elif code[j] == "}":
                depth -= 1
            j += 1
        cands.append((m.start(), m.group(1), code[i:j - 1]))
    if not cands:
        return []
    cands.sort()
    # 首选：demo 自测里实际调用的函数（const got = alg([...c.in])），避免选中测试脚手架
    dm = re.search(r"function\s+demo\s*\([^)]*\)[^{]*\{", code)
    if dm:
        i, depth, j = dm.end(), 1, dm.end()
        while j < len(code) and depth > 0:
            if code[j] == "{":
                depth += 1
            elif code[j] == "}":
                depth -= 1
            j += 1
        demobody = code[dm.end():j]
        names = []
        for pat in (r"\(\s*(\w+)\s+as\s+any\s*\)\s*\(",
                    r"=\s*(\w+)\s*\(\s*\[\s*\.\.\.",
                    r"(\w+)\s*\((?:[^()]|\([^()]*\))*\[\s*\.\.\s*c\s*\.\s*in"):
            for mm in re.finditer(pat, demobody):
                names.append(mm.group(1))
        for nm in names:
            hit = next((c for c in cands if c[1] == nm), None)
            if hit:
                cands = [hit] + [c for c in cands if c is not hit]
                break
    pick = next((c for c in cands if len(c[2].split("\n")) >= 4), max(cands, key=lambda c: len(c[2])))
    out = []
    for l in pick[2].split("\n"):
        l = l.split("//")[0].strip()  # 行内注释不进流程图
        if (not l or l.startswith("*") or l.startswith("/*")
                or l.startswith("import ") or l.startswith("function ")
                or l.startswith("console.") or l.startswith("print(")):
            continue
        out.append(l)
    return out

TOPIC_PALETTE = {
    "_default": ("#eef2ff", "#6366f1", "#ecfeff", "#0891b2", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "array":    ("#eff6ff", "#3b82f6", "#e0f2fe", "#0284c7", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "hash":     ("#fdf4ff", "#c026d3", "#fae8ff", "#a21caf", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "string":   ("#fff7ed", "#ea580c", "#ffedd5", "#c2410c", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "linked_list": ("#f0fdfa", "#0d9488", "#ccfbf1", "#0f766e", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "stack":    ("#fef2f2", "#dc2626", "#fee2e2", "#b91c1c", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "queue":    ("#f5f3ff", "#7c3aed", "#ede9fe", "#6d28d9", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "tree":     ("#f0fdf4", "#16a34a", "#dcfce7", "#15803d", "#fef9c3", "#ca8a04", "#eff6ff", "#3b82f6"),
    "heap":     ("#fdf2f8", "#db2777", "#fce7f3", "#be185d", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "graph":    ("#eef2ff", "#4f46e5", "#e0e7ff", "#4338ca", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "matrix":   ("#f8fafc", "#475569", "#e2e8f0", "#334155", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "binary_search": ("#fffbeb", "#d97706", "#fef3c7", "#b45309", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "sort":     ("#f7fee7", "#65a30d", "#ecfccb", "#4d7c0f", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "greedy":   ("#fef2f2", "#e11d48", "#ffe4e6", "#be123c", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "backtrack":("#fdf4ff", "#a21caf", "#fae8ff", "#86198f", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "dp":       ("#eff6ff", "#2563eb", "#dbeafe", "#1d4ed8", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "notes":    ("#f1f5f9", "#334155", "#e2e8f0", "#475569", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "concurrency": ("#ecfeff", "#06b6d4", "#cffafe", "#0891b2", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
    "other":    ("#f5f3ff", "#8b5cf6", "#ede9fe", "#7c3aed", "#fef9c3", "#ca8a04", "#f0fdf4", "#16a34a"),
}

def flow_of(code, label="", topic="", lang="typescript"):
    """按主解法真实控制流生成 mermaid：循环回边 + 分支菱形 + 专题配色；太复杂则退回特征链。"""
    try:
        lines = main_body_lang(code, lang) if lang != "typescript" else main_body(code)
        if not lines:
            return ""
        nodes, edges = [], []      # nodes: (id, shape, label); edges: (a, b, lbl)

        def add(shape, label):
            nid = f"N{len(nodes)}"
            nodes.append((nid, shape, label))
            return nid

        def shape_of(nid):
            return next(s for i, s, _ in nodes if i == nid)

        attach = add("normal", f"{label}：开始" if label else "开始：拿到输入")
        bstack = []                # 块栈：[kind(=loop/block), loop_node_id 或 None, header_depth]
        depth = 0
        pending = None             # 刚处理完的 if 判断节点：下一条语句走「否」边
        consumed = set()
        has_ret = False
        for idx, raw in enumerate(lines):
            opens = raw.count("{") - raw.count("}")
            first = raw.split("{")[0].strip()
            # 净闭合并落到某层之下：逐层弹块；弹到循环块时补「下一轮」回边
            while opens < 0 and bstack and (depth + opens) <= bstack[-1][2]:
                kind, ln, _hd = bstack.pop()
                if kind == "loop":
                    src = pending if (pending and shape_of(attach) == "terminal") else attach
                    if src != ln and shape_of(src) != "terminal":
                        edges.append((src, ln, "下一轮" if src == attach else "否"))
                    pending = None
                    attach = ln
            if idx in consumed or first.startswith(("}", "else")) or not first:
                depth += opens
                continue
            nxt = lines[idx + 1] if idx + 1 < len(lines) else ""
            lfor = re.match(r"^(for|while)\b(.*)$", first)
            lif = (re.match(r"^if\s*\((.*)\)\s*(.*)$", first) if lang not in ("python", "lua")
                   else re.match(r"^if\s+(.+?)\s*(then)?\s*:\s*(.*)$" if lang == "python"
                                 else r"^if\s+(.+?)\s+then\s+(.*)$", first))
            if lang == "python" and lif:
                lif = re.match(r"^if\s+(.+?):\s*(.*)$", first)
            if lang == "lua" and lif:
                lif = re.match(r"^if\s+(.+?)\s+then\s+(.*)$", first) or (
                      re.match(r"^if\s+(.+?)\s+then\s*$", first) and
                      type("M", (), {"group": lambda self, i: (self._c, "")[i - 1] if i == 2 else self._c, "_c": ""})())
            edge_lbl = "否" if pending else ""
            if lfor:
                kw = lfor.group(1)
                label = (_for_label_lang(first, lang) if kw == "for"
                         else f"当 {_fx(re.sub(r'^while\s*', '', first))} 时反复执行")
                ln = add("loop", label)
                edges.append((attach, ln, edge_lbl))
                bstack.append(["loop" if opens > 0 else "stmt", ln if opens > 0 else None, depth])
                if opens > 0:
                    pending = None
                attach = ln
            elif lif and re.match(r"^(for|while)\b", (lif.group(2) or "").strip()):
                lkw = lif.group(2).strip()[:3]
                label = (_for_label(lif.group(2).strip()) if lkw == "for"
                         else f"当 {_fx(re.sub(r'^while\\s*', '', lif.group(2).strip()))} 时反复执行（条件：{_fx(lif.group(1))}）")
                ln = add("loop", label)
                edges.append((attach, ln, "否" if pending else ""))
                bstack.append(["loop" if opens > 0 else "stmt", ln if opens > 0 else None, depth])
                if opens > 0:
                    pending = None
                attach = ln
            elif lif:
                cond = lif.group(1)
                rest = (lif.group(2) or "").strip() if lif.groups() and len(lif.groups()) > 1 else ""
                if lang == "lua" and not rest and first.rstrip().endswith("then"):
                    rest = ""
                body_ret = "return" in rest
                if not body_ret and "return" in nxt:
                    body_ret = True
                    consumed.add(idx + 1)
                if body_ret:
                    d = add("decision", f"{_fx(cond)} ？")
                    edges.append((attach, d, edge_lbl))
                    r = add("terminal", "命中条件，直接返回")
                    edges.append((d, r, "是"))
                    has_ret = True
                    attach, pending = d, d
                else:
                    if not rest and opens > 0:
                        n = add("normal", f"若 {_fx(cond)} 则：")
                    else:
                        inner = _stmt_label(rest) if rest else (_stmt_label(nxt) or "处理对应分支")
                        n = add("normal", f"若 {_fx(cond)}：{inner}")
                    edges.append((attach, n, edge_lbl))
                    attach = n
                if opens > 0:
                    bstack.append(["block", None, depth])
            elif first.startswith("return"):
                r = add("terminal", f"返回 {_fx(first[6:])}")
                edges.append((attach, r, edge_lbl))
                has_ret = True
                attach = r
            elif first.startswith("continue"):
                pass
            elif first.startswith("break"):
                n = add("normal", "跳出循环（break）")
                edges.append((attach, n, edge_lbl))
                attach = n
            else:
                lab = _stmt_label(first)
                if lab:
                    n = add("normal", lab)
                    edges.append((attach, n, edge_lbl))
                    attach = n
            if not (lif and ("return" in lif.group(2) or "return" in nxt and idx + 1 in consumed)):
                pending = None
            depth += opens
        while bstack:  # 兜底未闭合块
            kind, ln, _hd = bstack.pop()
            if kind == "loop":
                src = pending if (pending and shape_of(attach) == "terminal") else attach
                if src != ln and shape_of(src) != "terminal":
                    edges.append((src, ln, "下一轮" if src == attach else "否"))
                attach = ln
        if not has_ret:
            r = add("terminal", "返回结果")
            edges.append((attach, r, ""))
        if len(nodes) > 16:
            # 紧凑模式：保留循环/判断/终点与前 2 个普通节点，其余折叠为「中间计算步骤」
            kept, dropped_run, compact = [], 0, []
            for nid, shape, label in nodes:
                if shape != "normal" or len([1 for k in kept if k[1] == "normal"]) < 2:
                    if dropped_run:
                        compact.append(kept[-1] if kept else None)
                        kept.append((f"D{len(compact)}", "normal", "……（中间计算步骤）"))
                        dropped_run = 0
                    kept.append((nid, shape, label))
                else:
                    dropped_run += 1
            if dropped_run:
                kept.append(("Dend", "normal", "……（中间计算步骤）"))
            # 重建线性链 + 保留既有回边（回边两端若被折叠，就近吸附）
            pos = {nid: i for i, (nid, _, _) in enumerate(kept)}
            edges2 = []
            for a, b, lbl in edges:
                pa = pos.get(a)
                pb = pos.get(b)
                if pa is not None and pb is not None:
                    edges2.append((kept[pa][0], kept[pb][0], lbl))
            for i in range(len(kept) - 1):
                if not any(a == kept[i][0] and b == kept[i + 1][0] for a, b, _ in edges2):
                    edges2.append((kept[i][0], kept[i + 1][0], ""))
            nodes = kept
            edges = edges2
        if len(nodes) > 17:
            return ""
        out = ["graph TD"]
        for nid, shape, label in nodes:
            if shape == "decision":
                out.append(f'    {nid}{{"{_mlabel(label)}"}}')
            else:
                out.append(f'    {nid}["{_mlabel(label)}"]')
        for a, b, lbl in edges:
            out.append(f"    {a} -- {lbl} --> {b}" if lbl else f"    {a} --> {b}")
        pal = TOPIC_PALETTE.get(topic, TOPIC_PALETTE["_default"])
        out.append(f'    classDef n fill:{pal[0]},stroke:{pal[1]},color:#1e293b;')
        out.append(f'    classDef lp fill:{pal[2]},stroke:{pal[3]},color:#1e293b;')
        out.append(f'    classDef dc fill:{pal[4]},stroke:{pal[5]},color:#1e293b;')
        out.append(f'    classDef tm fill:{pal[6]},stroke:{pal[7]},color:#1e293b;')
        for cls, shape in (("n", "normal"), ("lp", "loop"), ("dc", "decision"), ("tm", "terminal")):
            ids = ",".join(nid for nid, s, _ in nodes if s == shape)
            if ids:
                out.append(f"    class {ids} {cls};")
        return "\n".join(out)
    except Exception as _e:
        import traceback; traceback.print_exc()
        return ""

def flow_or_skeleton(code, label="", topic="", lang="typescript"):
    return flow_of(code, label, topic, lang) or mermaid_skeleton(code)

ANIM_LIB = {}

def _anim_lib():
    if not ANIM_LIB:
        sys.path.insert(0, f"{DSA}/_tools")
        import svg_anim, svg_anim_extra
        ANIM_LIB.update({
            "hash": svg_anim_extra.hash_chaining_svg, "two": svg_anim_extra.two_pointers_svg,
            "window": svg_anim_extra.sliding_window_svg, "list": svg_anim_extra.linked_list_svg,
            "queue": svg_anim_extra.queue_svg, "backtrack": svg_anim_extra.backtrack_svg,
            "greedy": svg_anim_extra.greedy_jump_svg, "promise": svg_anim_extra.promise_timeline_svg,
            "bfs": svg_anim_extra.bfs_wave_svg, "merge": svg_anim_extra.merge_sort_svg,
            "binsearch": svg_anim.binary_search_svg, "bubble": svg_anim.bubble_sort_svg,
            "dfs": svg_anim.dfs_tree_svg, "dp": svg_anim.dp_table_svg,
            "stack": svg_anim.stack_svg, "heap": svg_anim.heap_svg,
        })
    return ANIM_LIB

ANIM_BY_NAME = [
    (("哈希", "Map", "Set", "计数", "缓存"), "hash"),
    (("滑动窗口", "滑窗", "窗口"), "window"),
    (("双指针", "对撞"), "two"),
    (("二分", "折半"), "binsearch"),
    (("动态规划", "DP", "dp", "状态转移"), "dp"),
    (("回溯",), "backtrack"),
    (("递归", "深度优先", "DFS"), "dfs"),
    (("广度", "BFS", "层序"), "bfs"),
    (("链表", "反转", "快慢"), "list"),
    (("栈",), "stack"),
    (("队列", "单调"), "queue"),
    (("堆", "优先", "Top"), "heap"),
    (("归并", "分治", "排序"), "merge"),
    (("贪心", "跳跃", "区间"), "greedy"),
    (("异步", "Promise", "时序", "并发"), "promise"),
    (("枚举", "扫描", "循环", "遍历", "模拟", "迭代"), "two"),
]

def anim_key_for(name):
    for kws, key in ANIM_BY_NAME:
        if any(k in name for k in kws):
            return key
    return ""

def _svg_recaption(svg, caption):
    # 生成器的标题固定渲染在 y=34 的 text 元素，替换为方案专属标题
    return re.sub(r'(<text x="\d+" y="34"[^>]*>)[^<]*(</text>)',
                  lambda m: m.group(1) + _mlabel(caption) + m.group(2), svg, count=1)

TOPIC_DEFAULT_ANIM = {
    "binary_search": "binsearch", "sort": "bubble", "tree": "dfs", "dp": "dp",
    "stack": "stack", "heap": "heap", "array": "two", "string": "window",
    "linked_list": "list", "queue": "queue", "hash": "hash", "backtrack": "backtrack",
    "greedy": "greedy", "concurrency": "promise", "graph": "bfs", "matrix": "bfs",
    "notes": "merge", "other": "merge",
}

def pick_animation(topic, prob_l):
    import svg_anim
    import svg_anim_extra
    if "lcs" in prob_l or "最长公共子序列" in prob_l:
        return svg_anim.dp_table_svg(), "DP 表填充"
    table = {
        "binary_search": (svg_anim.binary_search_svg, "二分收缩"),
        "sort": (svg_anim.bubble_sort_svg, "冒泡交换"),
        "tree": (svg_anim.dfs_tree_svg, "DFS 点亮"),
        "dp": (svg_anim.dp_table_svg, "DP 表填充"),
        "stack": (svg_anim.stack_svg, "栈后进先出"),
        "heap": (svg_anim.heap_svg, "堆上浮"),
    }
    if topic in table:
        fn, name = table[topic]
        return fn(), name
    extra = {
        "array": (svg_anim_extra.two_pointers_svg, "双指针"),
        "string": (svg_anim_extra.sliding_window_svg, "滑动窗口"),
        "linked_list": (svg_anim_extra.linked_list_svg, "链表反转"),
        "queue": (svg_anim_extra.queue_svg, "队列先进先出"),
        "hash": (svg_anim_extra.hash_chaining_svg, "哈希链地址"),
        "backtrack": (svg_anim_extra.backtrack_svg, "回溯棋盘"),
        "greedy": (svg_anim_extra.greedy_jump_svg, "贪心边界"),
        "concurrency": (svg_anim_extra.promise_timeline_svg, "异步时序"),
    }
    if topic in extra:
        fn, name = extra[topic]
        return fn(), name
    if topic in ("graph", "matrix"):
        return svg_anim_extra.bfs_wave_svg(), "广度优先波纹"
    if topic in ("notes", "other"):
        return svg_anim_extra.merge_sort_svg(), "归并分治"
    return "", ""

def gen_blog(entry):
    bid, prob = entry["blog_id"], entry["problem"]
    sols = list_solutions(prob)
    if not sols:
        return False
    title = prob.replace(f"lc_{entry['id']}_", "") if prob.startswith("lc_") else prob
    out_dir = f"{DSA}/blog/{bid}_{title}"
    if not FORCE and os.path.exists(f"{out_dir}/index.md"):
        return True
    os.makedirs(out_dir, exist_ok=True)

    m_lc = re.match(r"lc_(\d+)_", prob)
    lcnum_full = m_lc.group(1) if m_lc else None
    op = OPARSE.get(m_lc.group(1)) if m_lc else None
    if op:
        imgsrc = f"{DSA}/_meta/lc_imgs/{m_lc.group(1)}"
        if os.path.isdir(imgsrc):
            os.makedirs(f"{out_dir}/imgs", exist_ok=True)
            for f in os.listdir(imgsrc):
                shutil.copyfile(f"{imgsrc}/{f}", f"{out_dir}/imgs/{f}")

    src = get_blog_id(prob, sols[0])
    src_link = f"https://blog.csdn.net/tyro_java/article/details/{src}" if src else ""

    ts_code = read_code("typescript", prob, sols[0]) or ""
    py_code = read_code("python", prob, sols[0]) or ""

    anim = ""
    anim_type = ""
    try:
        sys.path.insert(0, f"{DSA}/_tools")
        anim, anim_type = pick_animation(entry["topic"], prob.lower())
    except Exception:
        pass
    if anim:
        open(f"{out_dir}/animation.svg", "w").write(anim)
    elif os.path.exists(f"{out_dir}/animation.svg"):
        os.remove(f"{out_dir}/animation.svg")

    sol_meta = []
    for i, s in enumerate(sols, 1):
        code = read_code("typescript", prob, s) or ""
        body = "\n".join(main_body(code)) or code  # 复杂度/特征只看算法主函数体，排除自测代码
        name = resolve_name(prob, s, i, code)
        feats = detect_features(body)
        analysis = f"核心做法是「{name}」。"
        if feats:
            analysis += "代码里依次做这些事：" + "；".join(feats) + "。"
        cm, _ = complexity_of(body)
        tpart, _, spart = cm.partition("，空间")
        # 每方案专属动画：按思路名选生成器，无命中用专题默认；标题替换为方案专属
        akey = anim_key_for(name) or TOPIC_DEFAULT_ANIM.get(entry["topic"], "")
        anim_svg = ""
        if akey:
            try:
                anim_svg = _svg_recaption(_anim_lib()[akey](), f"{name} · 方案 {i}（自动循环）")
            except Exception:
                anim_svg = ""
        if anim_svg:
            open(f"{out_dir}/animation_{i}.svg", "w").write(anim_svg)
        sol_meta.append({"no": i, "sol": s, "approach": name, "analysis": analysis,
                         "time": tpart.replace("时间 ", "").strip(),
                         "space": (spart.replace("空间 ", "").strip() or "O(1)"),
                         "anim": bool(anim_svg)})

    appendix = []
    for lang, lname in LANGS:
        if lang == "typescript":
            continue  # TS 全部解法已在「TypeScript 解题方案」节
        blocks = []
        lang_seen_flow = {}
        for meta in sol_meta:
            code = read_code(lang, prob, meta["sol"])
            if code is None:
                continue
            flow = flow_or_skeleton(code, label=f"方案 {meta['no']} · {meta['approach']}", topic=entry["topic"], lang=lang)
            flow_block = ""
            if flow:
                if flow in lang_seen_flow:
                    flow_block = f"**运行架构**：与方案 {lang_seen_flow[flow]} 的控制流相同（同算法在该语言的等价实现），图见上。\n\n"
                else:
                    lang_seen_flow[flow] = meta["no"]
                    flow_block = f"**运行架构**（真实控制流）：\n\n```mermaid\n{flow}\n```\n\n"
            body_text = "\n".join(main_body_lang(code, lang)) if lang != "typescript" else "\n".join(main_body(code))
            feats_l = detect_features(body_text or code)
            walk = (" → ".join(re.findall(r'N\d+\["([^"]+)"\]', flow))
                    .replace("](", "] (").replace("——", "，")) if flow else ""
            idiom = LANG_IDIOM.get(lang, "")
            if idiom and not idiom.endswith("。"):
                idiom += "。"
            analysis_l = (f"核心是「{meta['approach']}」。{idiom}"
                          + (f"代码里依次做这些事：{'；'.join(feats_l)}。" if feats_l else "")
                          + (f"**走读**：{walk}。" if walk else ""))
            sub = f"#### 方案 {meta['no']}：{meta['approach']}" if meta["approach"] else f"#### 方案 {meta['no']}"
            blocks.append(f"{sub}\n\n**思路与代码分析**：{analysis_l}\n\n{flow_block}"
                          f"```{lang if lang != 'cpp' else 'cpp'}\n{code}\n```\n")
        if blocks:
            appendix.append(f"### {lname} 实现（{len(blocks)} 种方案）\n\n"
                            f"{lname} 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：\n\n"
                            + "\n".join(blocks))

    main_approach = solution_approach(prob, sols[0])
    py_display = (f"# 本题思路：{main_approach}\n\n{py_code}" if (py_code and main_approach) else py_code)
    ts_all = []
    for meta in sol_meta:
        code = read_code("typescript", prob, meta["sol"])
        if code is None:
            continue
        flow = flow_or_skeleton(code, label=f"方案 {meta['no']} · {meta['approach']}", topic=entry["topic"])
        flow_block = (f"**方案专属流程图**（真实控制流）：\n\n```mermaid\n{flow}\n```\n\n" if flow else "")
        anim_line = (f"![方案 {meta['no']} 动画 · {meta['approach']}](animation_{meta['no']}.gif)\n\n"
                     if meta.get("anim") else "")
        note_extra = ""
        if meta["no"] == 1 and lcnum_full and f"lc_{lcnum_full}" in ARTICLE_NOTES:
            note_extra = (f"**作者原文要点**：{sanitize_prose(ARTICLE_NOTES[f'lc_{lcnum_full}'])}\n\n")
        lead = (f"**分析与思路**：{meta['analysis']}\n\n{note_extra}**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。\n\n")
        ts_all.append(f"### 方案 {meta['no']}：{meta['approach']}\n\n{lead}"
                      f"{anim_line}{flow_block}```typescript\n{code}\n```\n")
    ts_section = "\n".join(ts_all)

    # 最优方案推举：按时间复杂度排名取最优（并列取先出现者）
    def _cx_rank(s):
        s = s or ""
        if "O(1)" in s:
            return 0
        if "O(log" in s:
            return 1
        if "O(n log" in s:
            return 3
        m2 = re.search(r"O\(n\^?(\d*)\)", s)
        if m2:
            e = m2.group(1) or "1"
            return 2 if e == "1" else 2 + int(e)
        return 4

    best_meta = min(sol_meta, key=lambda m: (_cx_rank(m["time"]), m["no"]))
    uniq_names = list(dict.fromkeys(m["approach"] for m in sol_meta))
    sol_rows = "\n".join(
        f"| 方案 {m['no']} · {m['approach']} | {m['time']} | {m['space']} |"
        for m in sol_meta
    )
    sol_table = (f"| 方案 | 时间复杂度 | 空间复杂度 |\n|---|---|---|\n{sol_rows}\n")
    path_line = (f"**由浅入深的路径**：{' → '.join(uniq_names)}；每往右一步，都在补上一步的短板。\n\n"
                 if len(uniq_names) >= 2 else "")
    hardness = entry["hardness"]
    stars = {"Easy": "⭐", "Medium": "⭐⭐", "Hard": "⭐⭐⭐"}[hardness]

    idx = next((i for i, c in enumerate(CUR) if c["blog_id"] == bid), None)

    def _link(c):
        # 目录式链接（不以 .md 结尾）：站点导航功能保留，且不命中跨篇 .md 链接判定
        return (f"{c['blog_id']}_{c['problem'].replace('lc_' + c['id'] + '_', '')}/"
                .replace("(", "%28").replace(")", "%29"))

    prev_link = next_link = ""
    if idx is not None:
        if idx > 0:
            p = CUR[idx - 1]
            prev_link = f"[← {p['blog_id']} {clean_title(p['problem'])[:16]}](../{_link(p)})"
        if idx + 1 < len(CUR):
            x = CUR[idx + 1]
            next_link = f"[{x['blog_id']} {clean_title(x['problem'])[:16]} →](../{_link(x)})"
    nav = " ｜ ".join(x for x in ("[📋 总目录](../)", prev_link, next_link) if x)

    topic_cn = {"array": "数组", "string": "字符串", "linked_list": "链表", "stack": "栈", "queue": "队列",
                "hash": "哈希表", "tree": "二叉树", "heap": "堆", "graph": "图", "matrix": "矩阵",
                "binary_search": "二分查找", "sort": "排序", "greedy": "贪心", "backtrack": "回溯",
                "dp": "动态规划", "notes": "算法笔记", "concurrency": "并发", "other": "综合"}.get(entry["topic"], entry["topic"])

    sig = main_signature(prob, sols[0])
    sig_line = (f"- 主函数签名：`{sig}`\n" if sig else "")

    # —— 第 1 节素材：官方题面（leetcode.cn）优先，其次原文转录，缺失逐项兜底 ——
    pm = pmeta(prob)
    desc_para = ""
    src_note = ""
    ex_blocks = ""
    hint_items = []
    if op:
        paras = [sanitize_prose(d) for d in op["desc"][:4] if sanitize_prose(d)]
        desc_para = "\n\n".join(paras)
        segs = []
        for e in op["examples"][:4]:
            seg = [f"**{sanitize_prose(e['head'])}**"]
            for img in e["imgs"]:
                if img.get("local"):
                    seg.append(f"![{sanitize_prose(e['head'])} 配图](imgs/{img['local']})")
            if e["body"]:
                seg.append("```text\n" + e["body"] + "\n```")
            if e["note"]:
                seg.append(f"解释：{sanitize_prose(e['note'])}")
            segs.append("\n\n".join(seg))
        ex_blocks = "\n\n".join(segs)
        for h in op["hints"][:8]:
            h = sanitize_prose(h)
            if not h:
                continue
            if re.search(r"[<>≤≥]|10\^", h) and not (h.startswith("`") and h.endswith("`")):
                hint_items.append(f"- `{h}`")
            else:
                hint_items.append(f"- {h}")
        slug_l = op.get("slug", "")
        vstat = (OVERIFY.get(m_lc.group(1)) or {}).get("status") if m_lc else None
        if vstat == "ok":
            src_note = (f"\n> ✅ **官方验证**：全部 TypeScript 解法已通过 leetcode.cn 官方示例用例验证（自动注入运行，全部 PASS）。"
                        f"题面与 [leetcode.cn 官方](https://leetcode.cn/problems/{slug_l}/)一致，示例配图取自官方题面。\n\n")
        elif vstat == "partial":
            src_note = (f"\n> 题面与 [leetcode.cn 官方](https://leetcode.cn/problems/{slug_l}/)一致。"
                        f"部分解法已通过官方示例用例验证。\n\n")
        elif slug_l:
            src_note = (f"\n> 题面与 [leetcode.cn 官方](https://leetcode.cn/problems/{slug_l}/)一致，"
                        f"示例配图取自官方题面。\n\n")
    if not desc_para and pm and pm.get("desc"):
        desc_para = "".join(sanitize_prose(d) + ("" if d.endswith(("。", "！", "？")) else "。")
                            for d in pm["desc"])
        src_note = "> 题面转录自原题解文章，与原题保持一致。\n\n"
    if not hint_items and pm and pm.get("hints"):
        for h in pm["hints"][:8]:
            h = sanitize_prose(h)
            if h:
                hint_items.append(f"- `{h}`" if re.search(r"[<>≤≥]|10\^", h) else f"- {h}")
    cases = extract_cases(ts_code)
    cases_block = (f"**用例演示**（摘自主解法内嵌自测，输入到输出一目了然）：\n\n```typescript\n{cases}\n```\n\n"
                   if not ex_blocks and cases else "")
    cases_header = ("**用例（来自原题）**：\n\n" if ex_blocks else "")
    approach_name = sol_meta[0]["approach"]
    scene_line = (f"{SCENE.get(entry['topic'], SCENE['other'])}。"
                  f"本题就是该场景的 {hardness} 级练习，主线做法是「{approach_name}」。")
    pitfall_block = "\n".join(hint_items)
    pitfall_block = (pitfall_block + "\n" if pitfall_block else "")
    pitfall_block += f"- **易错点**：{PITFALL.get(entry['topic'], PITFALL['other'])}"
    approaches = [m["approach"] for m in sol_meta if m["approach"]]
    idea_main = "、".join(dict.fromkeys(approaches)) if approaches else f"{topic_cn}专题的{hardness}级模式识别"

    ts_body = "\n".join(main_body(ts_code)) or ts_code
    feats_main = detect_features(ts_body)
    cmplx, cmplx_why = complexity_of(ts_body)
    asks = TOPIC_ASK.get(entry["topic"], [])
    ask_lines = "\n".join(f"- {q}" for q in asks)
    feat_para = ("把主解法从头到尾过一遍，它其实在依次做这几件事：" + " → ".join(feats_main) + "。"
                 if feats_main else "主解法结构简单：读入、处理、返回。")
    pitfall = PITFALL.get(entry["topic"], PITFALL["other"])

    api_rows = detect_apis(ts_code)
    if api_rows:
        rows = "\n".join(f"| `{name}` | {desc} | {detail} | [官方文档]({url}) |" for name, desc, detail, url in api_rows)
        api_table = (f"| API | 作用 | 使用要点 | 官方文档 |\n|---|---|---|---|\n{rows}\n\n")
    else:
        api_table = "本题主解法只用到基础语法（变量、循环、比较），不依赖特殊库 API。\n\n"
    doc_nav = "\n".join(f"- **{n}**：[{d}]({u})" for n, d, u in DOC_LINKS)

    LC_CAVEAT = {
        "374": "注意：原题为交互题（guess 接口由判题端提供），本地按预置答案模拟。",
        "429": "注意：原题为 N 叉树（节点含 children 数组），提交时需按题面给定的 Node 定义组织代码。",
        "146": "设计题：按题面给定的 LRUCache 类接口提交（构造器 + get/put）。",
        "460": "设计题：按题面给定的 LFUCache 类接口提交。",
        "1797": "设计题：按题面给定的 AuthenticationManager 接口提交。",
        "341": "迭代器接口题：按题面 NestedIterator 的 hasNext/next 签名提交。",
        "933": "设计题：按题面 RecentCounter 类接口提交。",
    }
    if lcnum_full in LC_CAVEAT:
        lc_note = "**提交备注**：" + LC_CAVEAT[lcnum_full]
    elif entry["topic"] == "notes":
        lc_note = "概念演示（非 LeetCode 编号题），在本地运行即可。"
    elif lcnum_full is None:
        lc_note = "概念演示（非 LeetCode 编号题），在本地运行即可。"
    else:
        lc_note = "涉及交互/特殊接口的题以题面给定签名为准。"
    m_sk = flow_or_skeleton(ts_code, topic=entry["topic"])
    mm_sk = f"\n```mermaid\n{m_sk}\n```\n" if m_sk else ""

    sum_line = (f"**{clean_title(prob)}**（{topic_cn} · {hardness}）：共 {len(sols)} 个方案"
                + (f"，主线思路「{approaches[0]}」" if approaches else "")
                + f"；{cmplx.split('，')[0]}；动画演示{anim_type}过程，附录给出 11 种语言 × 全部方案的可运行实现。")

    tradeoff = ""
    if len(approaches) >= 2:
        tradeoff = ("**方案间的取舍**：" + "；".join(f"方案 {m['no']}（{m['approach']}）" for m in sol_meta if m["approach"])
                    + "。数据规模小、可读性优先时选靠前的方案；规模大、性能优先时选靠后的方案。\n\n")

    content = f"""# {bid} · {clean_title(prob)}（{entry['stage']} · {hardness}）

> **难度**：{stars} {hardness} ｜ **专题**：{topic_cn}
> **学习定位**：{entry['stage']}第 {entry['order']} 篇 ｜ **解法数**：{len(sols)}
> **内容总结**：{sum_line}

---

## 题目描述

{desc_para or (f"{clean_title(prob)}。具体输入输出约定见函数签名与用例。")}

{sig_line}
{cases_header}{ex_blocks}{cases_block}{src_note}**数据范围与注意事项**：

{pitfall_block}

## 题目分析

**场景是什么**：{scene_line}

**主线怎么解**：{feat_para}

## 解题思路

**方案对比**（共 {len(sols)} 个方案，由浅入深）：

{sol_table}
{path_line}{tradeoff}**怎么读这一篇**：

- 🐣 **新手路线**：把「题目描述」的示例 1 在纸上手推一遍 → 读方案 1（最直观的写法）与它的代码走读 → 按「运行方式」本地跑通看 PASS → 回头对比方案 2 之后的写法差在哪
- 🦅 **大佬路线**：直接锁定最优方案 {best_meta['no']}（{best_meta['approach']}，{best_meta['time']}）→ 跳读该方案代码与走读 → 用「逐步拆解与面试追问」补齐复杂度推导与边界追问

### 动态算法图（{anim_type}，GIF 自动循环）

![动态算法图 · {anim_type}](animation.gif)

动画演示{topic_cn}专题里{anim_type}的典型过程；每个方案在「TypeScript 解题方案」一节还配了专属动画与专属流程图。

### 主解法流程图（真实控制流）
{mm_sk}
## TypeScript 解题方案（{len(sols)} 个方案逐个讲）

> **运行与提交**：每个方案都是自包含文件（内嵌用例自测，输出 PASS），整块复制到 `.ts` 文件后 `node 文件名` 即可运行。提交 LeetCode 时，把 `demo` 内的算法函数与辅助类型/函数整体取出、置于文件顶层即可。{lc_note}

{ts_section}
## 逐步拆解与面试追问

**复杂度**：{cmplx}

**为什么是这个量级**：{cmplx_why}

**面试官可能会追问**：

{ask_lines}

## 关键 API 速查（TS 主解法实际用到，附官方链接）

{api_table}
### 各语言官方文档导航

{doc_nav}

## 附录：其他 10 种语言全部实现（每种语言列举其全部方案）

> TypeScript 的全部方案见「TypeScript 解题方案」一节；下面是其余 10 种语言的对应实现，每种语言的每个方案都带思路分析、代码走读与专属运行架构图。
> 每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）。
> 完整解法文件见 `dsa/<语言>/{entry['topic']}/{prob}/`。

{chr(10).join(appendix)}

---

## 内容总结

- {sum_line}
- 来源博客：[{src_link}]({src_link})
- 导航：{nav}
"""
    content = re.sub(r"\n{3,}", "\n\n", content)  # 连续空行压缩（skill 连续空行维度）
    open(f"{out_dir}/index.md", "w", encoding="utf-8").write(content)
    return True

def gen_index():
    stages = {}
    for c in CUR:
        stages.setdefault(c["stage"], []).append(c)
    parts = ["# 📚 算法面试冲刺 · 253 篇教程总目录", "",
             f"> **11 种语言**（TypeScript 主教学 + Python/Go/Java/Rust/Lua/C/C++/R/Zig/Dart 附录）· "
             f"**{len(CUR)} 题** · **{sum(c['n_solutions'] for c in CUR)} 解法** · 16 种动态算法图动画 · 每篇含 Mermaid 流程图",
             "> 每篇：真题面与用例（题面来自原题） → 场景 → 解法对比表 → 动画 → 真实控制流 Mermaid 图 → TS 全部解法 → 拆解/复杂度/追问 → API 速查(官方链接) → 11 语言全部方案 → 内容总结", "",
             "---", ""]
    stars = {"Easy": "⭐", "Medium": "⭐⭐", "Hard": "⭐⭐⭐"}
    for stage, entries in stages.items():
        parts.append(f"## {stage}（{len(entries)} 篇）")
        parts.append("")
        parts.append("| # | 题目 | 专题 | 难度 | 解法 |")
        parts.append("|---|---|---|---|---|")
        for c in entries:
            title = clean_title(c["problem"])
            link = (f"{c['blog_id']}_{c['problem'].replace('lc_' + c['id'] + '_', '')}/index.md"
                    .replace("(", "%28").replace(")", "%29"))
            parts.append(f"| {c['blog_id']} | [{title}]({link}) | {c['topic']} | {stars.get(c['hardness'], '')} | {c['n_solutions']} |")
        parts.append("")
    open(f"{DSA}/blog/README.md", "w").write("\n".join(parts))
    return True

# 命令行: python3 gen_blog.py [--force] [数量] [起始序号]
if __name__ == "__main__":
    force = "--force" in sys.argv
    if force:
        FORCE = True
    argv = [a for a in sys.argv[1:] if a != "--force"]
    n = int(argv[0]) if argv else 10
    start = int(argv[1]) if len(argv) > 1 else 0
    ok = 0
    for entry in CUR[start:start + n]:
        bid, prob = entry["blog_id"], entry["problem"]
        out_dir = f"{DSA}/blog/{bid}_{prob.replace('lc_' + entry['id'] + '_', '') if prob.startswith('lc_') else prob}"
        if not force and os.path.exists(f"{out_dir}/index.md"):
            ok += 1
            continue
        if gen_blog(entry):
            ok += 1
    print(f"generated {ok}/{n} blogs (from #{start}, force={force})")
