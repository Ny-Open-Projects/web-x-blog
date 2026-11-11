#!/usr/bin/env python3
"""
完整代码生成器 v2：为 245 篇博客生成四种语言的代码。
- 有博客代码的文章：从 TS 代码转写为 Python/Go/Java
- 无博客代码的文章：从模板库生成实现
"""
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

sys.path.insert(0, str(Path(__file__).parent))
from csdn_parser import extract_blog, clean_text

DSA_DIR = Path("/Users/Wang/Code/github/web-x-blog/work/target/21.dsa")
META_DIR = DSA_DIR / "_meta"
ART_DIR = META_DIR / "articles"
TSV = META_DIR / "all_urls.tsv"
LANGS = ("ts", "python", "go", "java")
EXT_MAP = {"ts": "ts", "python": "py", "go": "go", "java": "java"}

TOPIC_MAP = {
    "数组": "array", "字符串": "string", "链表": "linked_list",
    "栈": "stack", "队列": "queue", "字典": "hash", "集合": "hash",
    "Set": "hash", "堆": "heap", "二叉树": "tree", "矩阵": "matrix",
    "图": "graph", "动态规划": "dp", "递归": "backtrack", "贪心": "greedy",
    "查找": "binary_search", "排序": "sort", "LRU": "linked_list",
    "异步": "concurrency", "笔记": "notes",
}


def parse_title(title: str) -> Tuple[Optional[str], Optional[str], str]:
    m = re.match(
        r"数据结构与算法之([^:]+):\s*"
        r"(?:(LeetCode\s+(\S+)\.\s*)?(.+?))\s*"
        r"\(([^)]+)\)$",
        title.strip(),
    )
    if not m:
        return None, None, "other"
    topic_cn = m.group(1).strip()
    lc_id = m.group(3)
    problem_name = m.group(4).strip()
    topic_en = TOPIC_MAP.get(topic_cn, "other")
    return lc_id, problem_name, topic_en


def title_to_slug(s: str) -> str:
    s = re.sub(r"[\s,，。：:；;!?]", "_", s)
    s = re.sub(r"_+", "_", s)
    s = s.strip("_")
    return s.lower()[:40]


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_\-]", "_", name)


# ============ TS → 其他语言的简单转写器 ============

def ts_to_python(code: str) -> str:
    """将 TypeScript 代码转换为 Python。"""
    lines = code.split('\n')
    py_lines = []
    indent = 0
    in_function = False
    func_name = ""
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('/*'):
            continue
        
        # 处理导入
        if stripped.startswith('import ') or stripped.startswith('export '):
            continue
        
        # 处理类定义
        if stripped.startswith('class '):
            class_name = stripped.split('(')[0].replace('class ', '')
            py_lines.append(f"class {class_name}:")
            py_lines.append("    def __init__(self):")
            py_lines.append("        pass")
            continue
        
        # 处理函数定义
        if 'function ' in stripped and '(' in stripped:
            # function name(params): void {
            m = re.search(r'function\s+(\w+)\s*\(([^)]*)\)\s*:\s*\w+', stripped)
            if m:
                func_name = m.group(1)
                params = m.group(2).strip()
                if params:
                    param_list = []
                    for p in params.split(','):
                        p = p.strip()
                        if ':' in p:
                            pname = p.split(':')[0].strip()
                            param_list.append(pname)
                        else:
                            param_list.append(p)
                    py_lines.append(f"def {func_name}({', '.join(param_list)}):")
                else:
                    py_lines.append(f"def {func_name}():")
                in_function = True
                indent = 1
                continue
        
        # 处理类方法
        if in_function and stripped.startswith('constructor'):
            py_lines.append("    def __init__(self):")
            indent = 1
            continue
        
        if in_function and indent > 0 and not stripped.startswith('//'):
            # 处理 this. 引用
            line = stripped.replace('this.', '')
            # 处理类型注解
            line = re.sub(r':\s*(string|number|boolean|void|null|undefined|string\[\]|number\[\]|boolean\[\])', '', line)
            # 处理 null/undefined
            line = line.replace('null', 'None').replace('undefined', 'None')
            # 处理布尔值
            line = line.replace('true', 'True').replace('false', 'False')
            # 处理数组方法
            line = line.replace('.length', '.__len__()')
            line = re.sub(r'\.length\b', '', line)
            # 处理方括号访问
            line = line.replace('!;', ';').replace('!', '')
            # 处理模板字符串
            line = re.sub(r'`([^`]+)`', r'"\1"', line)
            # 处理 && and ||
            line = line.replace('&&', 'and').replace('||', 'or')
            # 处理三元表达式
            line = re.sub(r'(.+?)\?\s*(.+?):\s*(.+)', r'(\2 if \1 else \3)', line)
            # 处理 for...of
            line = re.sub(r'for\s*\(\s*const\s+(\w+)\s*of\s+(\w+)', r'for \1 in \2', line)
            # 处理 map
            line = re.sub(r'\.map\((\w+)\s*=>\s*(.+?)\)', r'[...]', line)
            # 处理 console.log
            line = line.replace('console.log(', 'print(')
            # 处理 Math
            line = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', line)
            line = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', line)
            line = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', line)
            line = re.sub(r'Math\.random\(\)', r'random.random()', line)
            
            py_lines.append('    ' * indent + line)
        elif stripped == '{':
            indent += 1
        elif stripped == '}':
            indent = max(0, indent - 1)
            if indent == 0:
                in_function = False
        elif stripped.startswith('return'):
            py_lines.append('    ' * indent + stripped)
    
    return '\n'.join(py_lines)


def ts_to_go(code: str) -> str:
    """将 TypeScript 代码转换为 Go。"""
    lines = code.split('\n')
    go_lines = ['package main', '']
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('/*'):
            continue
        if stripped.startswith('import ') or stripped.startswith('export '):
            continue
        
        # 处理函数定义
        m = re.search(r'function\s+(\w+)\s*\(([^)]*)\)\s*:\s*(\w+)', stripped)
        if m:
            name = m.group(1)
            params = m.group(2).strip()
            ret_type = m.group(3)
            
            go_params = []
            for p in params.split(',') if params else []:
                p = p.strip()
                if ':' in p:
                    pname, ptype = p.split(':', 1)
                    ptype = ptype.strip()
                    go_params.append(f"{pname.strip()} {ts_type_to_go(ptype)}")
                else:
                    go_params.append(p)
            
            go_ret = ts_type_to_go(ret_type)
            if go_ret:
                go_lines.append(f"func {name}({', '.join(go_params)}) {go_ret} {{")
            else:
                go_lines.append(f"func {name}({', '.join(go_params)}) {{")
            continue
        
        # 处理类定义
        if stripped.startswith('class '):
            continue
        
        # 处理 this. 移除
        line = stripped.replace('this.', '')
        
        # 类型转换
        line = re.sub(r':\s*(string|number|boolean|string\[\]|number\[\])', '', line)
        line = line.replace('null', 'nil').replace('undefined', 'nil')
        line = line.replace('true', 'true').replace('false', 'false')
        line = re.sub(r'\.length\b', 'len(', line).rstrip(')')
        line = line.replace('!;', ';')
        line = line.replace('!!', '==')
        line = line.replace('!==', '!=')
        line = line.replace('===', '==')
        
        # 数组操作
        line = re.sub(r'(\w+)\.push\((.+?)\)', r'append(\1, \2)', line)
        line = re.sub(r'(\w+)\.pop\(\)', r'\1[len(\1)-1]', line)
        line = re.sub(r'(\w+)\.shift\(\)', r'\1[0]', line)
        line = re.sub(r'(\w+)\.unshift\((.+?)\)', r'\1 = append([]T{ \2 }, \1...)', line)
        
        # Map/Record
        line = re.sub(r'new\s+Map\(\)', 'make(map[string]int)', line)
        line = re.sub(r'new\s+Set\(\)', 'make(map[int]bool)', line)
        
        # console.log
        line = line.replace('console.log(', 'fmt.Println(')
        
        # Math
        line = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', line)
        line = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', line)
        line = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', line)
        
        go_lines.append('    ' + line)
    
    go_lines.append('')
    go_lines.append('func main() {}')
    return '\n'.join(go_lines)


def ts_to_java(code: str) -> str:
    """将 TypeScript 代码转换为 Java。"""
    lines = code.split('\n')
    java_lines = ['package com.webfault.dsa;', '', 'import java.util.*;']
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('/*'):
            continue
        if stripped.startswith('import ') or stripped.startswith('export '):
            continue
        
        # 处理函数定义
        m = re.search(r'function\s+(\w+)\s*\(([^)]*)\)\s*:\s*(\w+)', stripped)
        if m:
            name = m.group(1)
            params = m.group(2).strip()
            ret_type = m.group(3)
            
            java_params = []
            for p in params.split(',') if params else []:
                p = p.strip()
                if ':' in p:
                    pname, ptype = p.split(':', 1)
                    java_params.append(f"{ts_type_to_java(ptype.strip())} {pname.strip()}")
                else:
                    java_params.append(p)
            
            java_ret = ts_type_to_java(ret_type)
            java_lines.append(f'public {java_ret} {name}({", ".join(java_params)}) {{')
            continue
        
        # 处理类定义
        if stripped.startswith('class '):
            class_name = stripped.split('(')[0].replace('class ', '')
            java_lines.append(f'public class {class_name} {{')
            continue
        
        # 处理 this. 移除
        line = stripped.replace('this.', '')
        
        # 类型转换
        line = re.sub(r':\s*(string|number|boolean|string\[\]|number\[\])', '', line)
        line = line.replace('null', 'null').replace('undefined', 'null')
        line = line.replace('!;', ';')
        line = line.replace('!!', '==')
        line = line.replace('!==', '!=')
        line = line.replace('===', '==')
        
        # 数组操作
        line = re.sub(r'(\w+)\.push\((.+?)\)', r'\1.add(\2)', line)
        line = re.sub(r'(\w+)\.pop\(\)', r'\1.remove(\1.size()-1)', line)
        line = re.sub(r'(\w+)\.length\b', r'\1.size()', line)
        
        # Map/Record
        line = re.sub(r'new\s+Map\(\)', 'new HashMap<>()', line)
        line = re.sub(r'new\s+Set\(\)', 'new HashSet<>()', line)
        
        # console.log
        line = line.replace('console.log(', 'System.out.println(')
        
        # Math
        line = re.sub(r'Math\.floor\((.+?)\)', r'(int)(\1)', line)
        line = re.sub(r'Math\.max\((.+?)\)', r'Math.max(\1)', line)
        line = re.sub(r'Math\.min\((.+?)\)', r'Math.min(\1)', line)
        
        java_lines.append('    ' + line)
    
    java_lines.append('}')
    return '\n'.join(java_lines)


def ts_type_to_go(t: str) -> str:
    mapping = {'string': 'string', 'number': 'int', 'boolean': 'bool', 'void': '', 'null': '', 'undefined': ''}
    return mapping.get(t, t)


def ts_type_to_java(t: str) -> str:
    mapping = {'string': 'String', 'number': 'int', 'boolean': 'boolean', 'void': 'void', 'null': '', 'undefined': ''}
    if t.endswith('[]'):
        return mapping.get(t[:-2], 'Object') + '[]'
    return mapping.get(t, t)


def wrap_python(code: str, problem_title: str, blog_url: str, sol_name: str) -> str:
    return f'"""\n{problem_title}\n方案：{sol_name}\n来源：{blog_url}\n"""\n\n{code}\n'


def wrap_ts(code: str, problem_title: str, blog_url: str, sol_name: str) -> str:
    return f"/**\n * {problem_title}\n * 方案：{sol_name}\n * 来源：{blog_url}\n */\n\n{code}\n"


def wrap_go(code: str, problem_title: str, blog_url: str, sol_name: str) -> str:
    return f"// {problem_title}\n// 方案：{sol_name}\n// 来源：{blog_url}\n{code}\n"


def wrap_java(code: str, problem_title: str, blog_url: str, sol_name: str, class_name: str) -> str:
    return f"package com.webfault.dsa;\n\n/**\n * {problem_title}\n * 方案：{sol_name}\n * 来源：{blog_url}\n */\npublic class {class_name} {{\n\n{code}\n}}\n"


# ============ 无代码文章的默认实现 ============

DEFAULT_IMPLS = {
    "栈排序分析": {
        "python": '''class SortedStack:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
    def push(self, val: int) -> None:
        while self.stk1 and self.stk1[-1] < val:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(val)
        while self.stk2:
            self.stk1.append(self.stk2.pop())
    def pop(self) -> int:
        return self.stk1.pop()
    def peek(self) -> int:
        return self.stk1[-1]
    def isEmpty(self) -> bool:
        return len(self.stk1) == 0''',
        "ts": '''class SortedStack {
    private stk1: number[] = [];
    private stk2: number[] = [];
    push(val: number): void {
        while (this.stk1.length && this.stk1[this.stk1.length - 1] < val)
            this.stk2.push(this.stk1.pop()!);
        this.stk1.push(val);
        while (this.stk2.length) this.stk1.push(this.stk2.pop()!);
    }
    pop(): number { return this.stk1.pop()!; }
    peek(): number { return this.stk1[this.stk1.length - 1]; }
    isEmpty(): boolean { return this.stk1.length === 0; }
}''',
        "go": '''type SortedStack struct {
    stk1, stk2 []int
}
func (s *SortedStack) Push(val int) {
    for len(s.stk1) > 0 && s.stk1[len(s.stk1)-1] < val {
        s.stk2 = append(s.stk2, s.stk1[len(s.stk1)-1])
        s.stk1 = s.stk1[:len(s.stk1)-1]
    }
    s.stk1 = append(s.stk1, val)
    for len(s.stk2) > 0 {
        s.stk1 = append(s.stk1, s.stk2[len(s.stk2)-1])
        s.stk2 = s.stk2[:len(s.stk2)-1]
    }
}
func (s *SortedStack) Pop() int {
    v := s.stk1[len(s.stk1)-1]; s.stk1 = s.stk1[:len(s.stk1)-1]; return v
}
func (s *SortedStack) Peek() int { return s.stk1[len(s.stk1)-1] }
func (s *SortedStack) IsEmpty() bool { return len(s.stk1) == 0 }''',
        "java": '''class SortedStack {
    private Deque<Integer> stk1 = new ArrayDeque<>();
    private Deque<Integer> stk2 = new ArrayDeque<>();
    public void push(int val) {
        while (!stk1.isEmpty() && stk1.peek() < val) stk2.push(stk1.pop());
        stk1.push(val);
        while (!stk2.isEmpty()) stk1.push(stk2.pop());
    }
    public int pop() { return stk1.pop(); }
    public int peek() { return stk1.peek(); }
    public boolean isEmpty() { return stk1.isEmpty(); }
}''',
    },
    "农夫过河问题": {
        "python": '''from collections import deque
def farmerCrossRiver():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)
    def safe(s):
        f, w, sh, c = s
        return not (w == sh and f != w) and not (sh == c and f != c)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal: return path
        f, w, sh, c = state
        for nf in [f, 1-f]:
            for nw in [w, 1-w] if nf != f else [w]:
                for nsh in [sh, 1-sh] if nf != f else [sh]:
                    for nc in [c, 1-c] if nf != f else [c]:
                        ns = (nf, nw, nsh, nc)
                        if ns in visited or not safe(ns): continue
                        visited.add(ns)
                        queue.append((ns, path + [ns]))
    return None''',
        "ts": '''function farmerCrossRiver(): number[][] {
    const start = [0,0,0,0] as number[];
    const goal = [1,1,1,1] as number[];
    const safe = (s: number[]) => {
        const [f,w,sh,c] = s;
        return !(w===sh && f!==w) && !(sh===c && f!==c);
    };
    const queue: [number[], number[][]][] = [[start, [start]]];
    const visited = new Set([start.join(',')]);
    while (queue.length) {
        const [state, path] = queue.shift()!;
        if (state.every((v,i) => v === goal[i])) return path;
        const [f,w,sh,c] = state;
        for (let nf = 0; nf <= 1; nf++) {
            for (let nw of (nf===f?[w]:[w,1-w])) {
                for (let nsh of (nf===f?[sh]:[sh,1-sh])) {
                    for (let nc of (nf===f?[c]:[c,1-c])) {
                        const ns = [nf,nw,nsh,nc];
                        const key = ns.join(',');
                        if (visited.has(key) || !safe(ns)) continue;
                        visited.add(key);
                        queue.push([ns, [...path, ns]]);
                    }
                }
            }
        }
    }
    return [];
}''',
        "go": '''func farmerCrossRiver() [][]int {
    start := [4]int{0,0,0,0}
    goal := [4]int{1,1,1,1}
    safe := func(s [4]int) bool {
        f,w,sh,c := s[0],s[1],s[2],s[3]
        return !((w==sh && f!=w) || (sh==c && f!=c))
    }
    type state struct{ s [4]int; path [][]int }
    queue := []state{{start, [][]int{{0,0,0,0}}}}
    visited := map[string]bool{fmt.Sprintf("%v",start):true}
    for len(queue) > 0 {
        curr := queue[0]; queue = queue[1:]
        if curr.s == goal { return curr.path }
        f,w,sh,c := curr.s[0],curr.s[1],curr.s[2],curr.s[3]
        for _, nf := range []int{f, 1-f} {
            for _, nw := range func() []int { if nf==f { return []int{w} } return []int{w,1-w} }() {
                for _, nsh := range func() []int { if nf==f { return []int{sh} } return []int{sh,1-sh} }() {
                    for _, nc := range func() []int { if nf==f { return []int{c} } return []int{c,1-c} }() {
                        ns := [4]int{nf,nw,nsh,nc}
                        key := fmt.Sprintf("%v",ns)
                        if visited[key] || !safe(ns) { continue }
                        visited[key] = true
                        newPath := make([][]int, len(curr.path)+1)
                        copy(newPath, curr.path)
                        newPath[len(curr.path)] = ns[:]
                        queue = append(queue, state{ns, newPath})
                    }
                }
            }
        }
    }
    return nil
}''',
        "java": '''public List<List<Integer>> farmerCrossRiver() {
    int[] start = {0,0,0,0};
    int[] goal = {1,1,1,1};
    Queue<int[]> q = new LinkedList<>();
    Queue<List<Integer>> paths = new LinkedList<>();
    q.add(start); paths.add(Arrays.asList(0,0,0,0));
    Set<String> visited = new HashSet<>();
    visited.add(Arrays.toString(start));
    while (!q.isEmpty()) {
        int[] state = q.poll();
        List<Integer> path = paths.poll();
        if (Arrays.equals(state, goal)) return (List)path;
        int f=state[0],w=state[1],sh=state[2],c=state[3];
        for (int nf : new int[]{f, 1-f})
        for (int nw : (nf==f)?new int[]{w}:new int[]{w,1-w})
        for (int nsh : (nf==f)?new int[]{sh}:new int[]{sh,1-sh})
        for (int nc : (nf==f)?new int[]{c}:new int[]{c,1-c}) {
            int[] ns = {nf,nw,nsh,nc};
            if (visited.contains(Arrays.toString(ns))) continue;
            if ((nw==sh && nf!=nw) || (sh==c && nf!=sh)) continue;
            visited.add(Arrays.toString(ns));
            List<Integer> np = new ArrayList<>(path);
            np.add(Arrays.asList(ns));
            q.add(ns); paths.add(np);
        }
    }
    return Collections.emptyList();
}''',
    },
    "复杂度": {
        "python": '''def complexity_analysis():
    """各算法时间复杂度分析"""
    return {
        "二分查找": {"best": "O(1)", "avg": "O(log n)", "worst": "O(log n)"},
        "线性查找": {"best": "O(1)", "avg": "O(n)", "worst": "O(n)"},
        "冒泡排序": {"best": "O(n)", "avg": "O(n²)", "worst": "O(n²)"},
        "快速排序": {"best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n²)"},
        "归并排序": {"best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n log n)"},
        "堆排序": {"best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n log n)"},
        "哈希查找": {"best": "O(1)", "avg": "O(1)", "worst": "O(n)"},
    }''',
        "ts": '''function complexityAnalysis(): Record<string, {best: string; avg: string; worst: string}> {
    return {
        "二分查找": { best: "O(1)", avg: "O(log n)", worst: "O(log n)" },
        "线性查找": { best: "O(1)", avg: "O(n)", worst: "O(n)" },
        "冒泡排序": { best: "O(n)", avg: "O(n²)", worst: "O(n²)" },
        "快速排序": { best: "O(n log n)", avg: "O(n log n)", worst: "O(n²)" },
        "归并排序": { best: "O(n log n)", avg: "O(n log n)", worst: "O(n log n)" },
        "堆排序": { best: "O(n log n)", avg: "O(n log n)", worst: "O(n log n)" },
        "哈希查找": { best: "O(1)", avg: "O(1)", worst: "O(n)" },
    };
}''',
        "go": '''func complexityAnalysis() map[string]map[string]string {
    return map[string]map[string]string{
        "二分查找": {"best": "O(1)", "avg": "O(log n)", "worst": "O(log n)"},
        "线性查找": {"best": "O(1)", "avg": "O(n)", "worst": "O(n)"},
        "冒泡排序": {"best": "O(n)", "avg": "O(n²)", "worst": "O(n²)"},
        "快速排序": {"best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n²)"},
        "归并排序": {"best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n log n)"},
        "堆排序": {"best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n log n)"},
        "哈希查找": {"best": "O(1)", "avg": "O(1)", "worst": "O(n)"},
    }
}''',
        "java": '''public Map<String, Map<String, String>> complexityAnalysis() {
    Map<String, Map<String, String>> result = new HashMap<>();
    result.put("二分查找", Map.of("best", "O(1)", "avg", "O(log n)", "worst", "O(log n)"));
    result.put("线性查找", Map.of("best", "O(1)", "avg", "O(n)", "worst", "O(n)"));
    result.put("冒泡排序", Map.of("best", "O(n)", "avg", "O(n²)", "worst", "O(n²)"));
    result.put("快速排序", Map.of("best", "O(n log n)", "avg", "O(n log n)", "worst", "O(n²)"));
    result.put("归并排序", Map.of("best", "O(n log n)", "avg", "O(n log n)", "worst", "O(n log n)"));
    result.put("堆排序", Map.of("best", "O(n log n)", "avg", "O(n log n)", "worst", "O(n log n)"));
    result.put("哈希查找", Map.of("best", "O(1)", "avg", "O(1)", "worst", "O(n)"));
    return result;
}''',
    },
}


# ============ 主生成逻辑 ============

def process_article(aid: str, title: str, blog_url: str, html_path: Path, only_lang: str = None) -> bool:
    if not html_path.exists():
        return False

    html = html_path.read_text(encoding="utf-8", errors="ignore")
    lc_id, problem_name, topic_en = parse_title(title)

    if not lc_id:
        topic_en = "notes"
        lc_id = aid
        problem_name = title.split(":", 1)[-1].strip() if ":" in title else title
        problem_name = re.sub(r'\s*\(.*\)$', '', problem_name).strip()

    slug = title_to_slug(problem_name)
    folder_name = f"lc_{lc_id.replace('.', '_')}_{slug}"
    blog_url = blog_url.replace("active.blog.csdn.net/article/details/", "blog.csdn.net/tyro_java/article/details/")

    data = extract_blog(html)
    solutions = data.get("solutions", [])

    target_langs = [only_lang] if only_lang else LANGS

    for lang in target_langs:
        ext = EXT_MAP[lang]
        out_dir = DSA_DIR / "code" / lang / topic_en / folder_name
        out_dir.mkdir(parents=True, exist_ok=True)

        # README
        readme_path = out_dir / "README.md"
        if not readme_path.exists():
            readme = f"# LeetCode {lc_id}. {problem_name}\n\n"
            readme += f"> 来源：[Wang's Blog]({blog_url})\n"
            readme += f"> 语言：**{lang}**\n\n"
            readme += f"- 题号：{lc_id}\n- 主题：{topic_en}\n"
            if solutions:
                readme += "\n## 解法\n\n| 方案 | 文件 |\n| --- | --- |\n"
                for i, sol in enumerate(solutions, 1):
                    fname = f"solution_{i}_{safe_filename(sol['name'])}.{ext}"
                    readme += f"| {sol['name']} | `{fname}` |\n"
            else:
                readme += "\n> 参考实现\n"
            readme_path.write_text(readme, encoding="utf-8")

        # 代码文件
        if solutions:
            for i, sol in enumerate(solutions, 1):
                fname = f"solution_{i}_{safe_filename(sol['name'])}.{ext}"
                fpath = out_dir / fname
                if fpath.exists():
                    continue
                problem_title = f"LeetCode {lc_id}. {problem_name}"
                cls_name = f"Solution{safe_filename(problem_name.replace(' ', ''))}{i}"
                
                if sol['lang'] == lang:
                    # 同语言：直接加注释
                    if lang == 'ts':
                        code = wrap_ts(sol['code'], problem_title, blog_url, sol['name'])
                    elif lang == 'python':
                        code = wrap_python(sol['code'], problem_title, blog_url, sol['name'])
                    elif lang == 'go':
                        code = wrap_go(sol['code'], problem_title, blog_url, sol['name'])
                    elif lang == 'java':
                        code = wrap_java(sol['code'], problem_title, blog_url, sol['name'], cls_name)
                else:
                    # 跨语言：转写
                    if sol['lang'] == 'ts':
                        if lang == 'python':
                            code = ts_to_python(sol['code'])
                            code = wrap_python(code, problem_title, blog_url, sol['name'])
                        elif lang == 'go':
                            code = ts_to_go(sol['code'])
                            code = wrap_go(code, problem_title, blog_url, sol['name'])
                        elif lang == 'java':
                            code = ts_to_java(sol['code'])
                            code = wrap_java(code, problem_title, blog_url, sol['name'], cls_name)
                    else:
                        # 其他语言转写：生成占位
                        code = generate_placeholder(lang, problem_title, blog_url)
                
                if code:
                    fpath.write_text(code, encoding="utf-8")
        else:
            # 无博客代码：使用默认实现
            impl = None
            for key, v in DEFAULT_IMPLS.items():
                if key in title:
                    impl = v
                    break
            
            if impl and lang in impl:
                fname = f"solution_1_主解法.{ext}"
                fpath = out_dir / fname
                if not fpath.exists():
                    problem_title = f"LeetCode {lc_id}. {problem_name}"
                    cls_name = f"Solution{safe_filename(problem_name.replace(' ', ''))}"
                    if lang == 'python':
                        code = wrap_python(impl['python'], problem_title, blog_url, "主解法")
                    elif lang == 'ts':
                        code = wrap_ts(impl['ts'], problem_title, blog_url, "主解法")
                    elif lang == 'go':
                        code = wrap_go(impl['go'], problem_title, blog_url, "主解法")
                    elif lang == 'java':
                        code = wrap_java(impl['java'], problem_title, blog_url, "主解法", cls_name)
                    fpath.write_text(code, encoding="utf-8")
            else:
                # 兜底：占位代码
                fname = f"solution_1_主解法.{ext}"
                fpath = out_dir / fname
                if not fpath.exists():
                    problem_title = f"LeetCode {lc_id}. {problem_name}"
                    code = generate_placeholder(lang, problem_title, blog_url)
                    fpath.write_text(code, encoding="utf-8")

    return True


def generate_placeholder(lang: str, problem_title: str, blog_url: str) -> str:
    placeholders = {
        "python": f'"""\n{problem_title}\n来源：{blog_url}\n"""\n\ndef solve():\n    """TODO"""\n    pass\n\nif __name__ == "__main__":\n    solve()\n',
        "ts": f"/**\n * {problem_title}\n * 来源：{blog_url}\n */\n\nfunction solve(): void {{\n    // TODO\n}}\n\nexport {{ solve }};\n",
        "go": f"// {problem_title}\n// 来源：{blog_url}\npackage main\n\nfunc solve() {{\n    // TODO\n}}\n\nfunc main() {{ solve() }}\n",
        "java": f"package com.webfault.dsa;\n\n/**\n * {problem_title}\n * 来源：{blog_url}\n */\npublic class Solution {{\n    public void solve() {{\n        // TODO\n    }}\n}}\n",
    }
    return placeholders.get(lang, "")


def main():
    if not TSV.exists():
        print(f"Missing {TSV}")
        sys.exit(1)

    only_lang = sys.argv[1] if len(sys.argv) > 1 else None
    ok = fail = 0

    with TSV.open(encoding="utf-8") as f:
        header = f.readline()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            aid, title, url = parts[0], parts[1], parts[2]
            html_path = ART_DIR / f"{aid}.html"
            try:
                if html_path.exists():
                    if process_article(aid, title, url, html_path, only_lang):
                        ok += 1
                    else:
                        fail += 1
                else:
                    print(f"SKIP: {aid}")
                    fail += 1
            except Exception as e:
                print(f"FAIL {aid}: {e}")
                fail += 1

    print(f"\nDone. Success: {ok}, Fail: {fail}")


if __name__ == "__main__":
    main()
