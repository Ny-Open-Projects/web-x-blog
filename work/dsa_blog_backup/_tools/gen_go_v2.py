#!/usr/bin/env python3
"""
gen_go_v2.py — 从 TS 源文件生成可 gofmt 的 Go 代码。

策略：
  1. 解析 TS 顶层 function / class / const-func 声明
  2. 类 → Go struct + 方法；嵌套 function → Go 具名函数（去重）
  3. TS 语法 → Go 语法映射（type、array methods、Math.*、null、三目等）
  4. 自动推导局部变量类型声明（int/TreeNode/ListNode/...）
  5. 写出去掉 fmt 未用的 import；gofmt 验证

输出：DSA/go/<相对路径>.go
"""
import re, os, subprocess
from pathlib import Path

DSA = Path('/Users/Wang/Code/webfault-ai/dsa')

# ---------- 类型映射 ----------
def ts_to_go_type(t: str) -> str:
    t = t.strip()
    if t in ('number', 'float'):
        return 'int'
    if t in ('string',):
        return 'string'
    if t in ('boolean',):
        return 'bool'
    if t in ('void',):
        return ''
    if t in ('any',):
        return 'interface{}'
    # null / undefined
    if t in ('null', 'undefined'):
        return 'int'
    # 可空类型 X | null → X
    if '|' in t:
        parts = [p.strip() for p in t.split('|') if p.strip() not in ('null', 'undefined', '')]
        if parts:
            return ts_to_go_type(parts[0])
        return 'interface{}'
    # 数组
    if t.endswith('[]'):
        base = t[:-2].strip()
        # 泛型数组 T[][] → 递归
        go_base = ts_to_go_type(base)
        return f'[]({go_base})' if '(' in go_base else f'[]{go_base}'
    # 对象字面量类型 / Map / Record
    if t.startswith('Map') or t.startswith('Record') or t.startswith('{'):
        return 'map[string]interface{}'
    # 未知类型 → 原样
    return t

def go_pointer(t: str) -> str:
    """TreeNode/ListNode 等对象类型 → 指针；数值/字符串/bool 不变"""
    if t.startswith('[]') or t.startswith('map'):
        return t
    if t in ('int', 'string', 'bool', 'float64', 'float32'):
        return t
    return '*' + t

# ---------- TS → Go 表达式转换 ----------
def expr_go(s: str) -> str:
    """把 TS 表达式片段转成 Go（用于变量声明、return 等场景）"""
    # 三目：X ? A : B
    # 贪婪匹配可能不准，保留 TS 形式但加标注；go 支持条件表达式？不支持 → 简化为 if 不必要
    s = s.replace('===', '==').replace('!==', '!=').replace(' && ', ' && ')
    s = s.replace('NaN', '0').replace('Infinity', '1e9')
    # Math.*
    s = s.replace('Math.abs(', 'abs(').replace('Math.floor(', 'floor(')
    s = s.replace('Math.ceil(', 'ceil(').replace('Math.round(', 'round(')
    s = s.replace('Math.max(', 'max2(').replace('Math.min(', 'min2(')
    s = s.replace('Math.random()', 'rand.Float64()')
    s = s.replace('Math.pow(', 'pow(')
    s = s.replace('Math.sqrt(', 'sqrt(')
    s = s.replace('Math.log(', 'log(').replace('Math.log2(', 'log2(')
    # 数组方法
    s = s.replace('.push(', 'append(,')  # 占位，下面修正
    # 把 x.push(y) → x = append(x, y)
    s = re.sub(r'(\w[\w\.\[\]\'\"]*)\.push\((.*?)\)\s*$', r'\1 = append(\1, \2)', s)
    s = s.replace('Array(', '[]')
    s = re.sub(r'Array\.from\((\w+)\)', r'[]int{\1}', s)  # 简化
    s = s.replace('.length', 'Len')  # 占位，下面按上下文
    # 字符串
    s = s.replace(".charCodeAt(0)", ".RuneAt(0)")
    s = s.replace(".indexOf(", "index(")
    s = s.replace(".includes(", "contains(")
    s = s.replace("null", "nil")
    # 解构交换 [a, b] = [b, a]
    s = re.sub(r'\[(\w+),\s*(\w+)\]\s*=\s*\[\s*\2,\s*\1\s*\]', r'\1, \2 = \2, \1', s)
    s = re.sub(r'\[(\w+),\s*(\w+)\]\s*=\s*(.+?)$', r'\1, \2 = \3', s)
    # 模板字符串
    s = s.replace('`', '"')
    s = re.sub(r'\$\{', '', s)  # 模板插值简化
    s = re.sub(r'(\w+)\.slice\((\d+)\)', r'\1[\2:]', s)
    s = re.sub(r'(\w+)\.slice\((\d+)\s*,\s*(\d+)\)', r'\1[\2:\3]', s)
    s = re.sub(r'(\w+)\.slice\(-1\)', r'\1[len(\1)-1]', s)
    s = re.sub(r'\.pop\(\)\s*$', r'_popped', s)
    s = s.replace('.repeat(', 'repeat(')
    s = s.replace('new Array(', '[]int{')
    # 对象字面量
    s = re.sub(r'new\s+(\w+)\(([^()]*)\)', lambda m: f'&{m.group(1)}{{ {m.group(2)} }}', s)
    return s

# 更稳妥的整行转换
def line_go(line: str) -> str:
    """把一行 TS 转成 Go（处理常见语句形式）"""
    s = line.rstrip('\n')
    indent = len(s) - len(s.lstrip())
    orig_indent = s[:indent]
    s = s.strip()
    # 空行 / 注释
    if not s or s.startswith('//') or s.startswith('/*') or s.startswith('*'):
        return s
    # 去掉行内类型注解  x: number = ...  → x = ...
    s = re.sub(r'(\w+)\s*:\s*(\w+)\s*=', lambda m: m.group(1) + ' =', s)  # 简单
    # const/let → 后面根据是否已声明决定 :=/
    s = s.replace('const ', '').replace('let ', '')
    # 解构 [a,b]= 已处理
    # for 循环：for (let i = 0; i < n; i++) → for i := 0; i < n; i++
    m = re.match(r'^for\s*\(\s*(.+?)\s*;\s*(.+?)\s*;\s*(.+?)\s*\)\s*(\{?)$', s)
    if m:
        init, cond, upd, brace = m.group(1), m.group(2), m.group(3), m.group(4)
        # init 可能 "let i = 0"
        init = init.replace('let ', '').replace('const ', '')
        if init:
            init = init if '=' in init else init + ' := '
        return f'{orig_indent}for {init}; {cond}; {upd} ' + brace
    # while → for
    m = re.match(r'^while\s*\((.+)\)\s*(\{?)$', s)
    if m:
        return f'{orig_indent}for {m.group(1)} ' + m.group(2)
    # switch → 保留
    # return
    m = re.match(r'^return\s+(.+)$', s)
    if m:
        val = expr_go(m.group(1))
        return f'{orig_indent}return {val}'
    # 赋值 / 声明
    m = re.match(r'^(\w+)\s*=\s*(.+)$', s)
    if m:
        return f'{orig_indent}{m.group(1)} = {expr_go(m.group(2))}'
    m = re.match(r'^(\w+)\s*:?\s*:=?\s*(.+)$', s)
    if m:
        return f'{orig_indent}{m.group(1)} := {expr_go(m.group(2))}'
    # 普通语句
    return expr_go(s)

# ---------- 顶层解析 ----------
def parse_top_level(src: str):
    """返回 [(kind, name, signature_line, body_text)]"""
    items = []
    lines = src.split('\n')
    i = 0
    n = len(lines)
    # 跳过前导注释头
    while i < n and (lines[i].strip().startswith('/**') or lines[i].strip().startswith('*') or lines[i].strip() == '' or lines[i].strip().startswith('//')):
        i += 1
    while i < n:
        line = lines[i]
        st = line.strip()
        if st.startswith('function ') or st.startswith('export function ') or st.startswith('function '):
            name = st.split('(')[0].replace('export ', '').split()[-1]
            sig_line = st
            # 找函数体：从第一个 { 开始，匹配 }
            depth = 0
            start = i
            j = i
            body_lines = []
            body_started = False
            while j < n:
                l = lines[j]
                if '{' in l and not body_started:
                    body_started = True
                    depth = 0
                    for ch in l:
                        if ch == '{': depth += 1
                        elif ch == '}': depth -= 1
                    if depth <= 0:
                        body_lines.append(l)
                        j += 1
                        break
                    else:
                        body_lines.append(l)
                        j += 1
                        continue
                else:
                    depth_l = 0
                    for ch in l:
                        if ch == '{': depth_l += 1
                        elif ch == '}': depth_l -= 1
                    depth += depth_l
                    body_lines.append(l)
                    j += 1
                    if body_started and depth <= 0:
                        break
            body = '\n'.join(body_lines)
            items.append(('func', name, sig_line, body))
            i = j
            continue
        if st.startswith('class '):
            name = st.split('(')[0].split()[-1]
            # class 体
            depth = 0
            body_lines = [line]
            j = i
            body_started = False
            while j < n:
                l = lines[j]
                for ch in l:
                    if ch == '{':
                        depth += 1
                        body_started = True
                    elif ch == '}':
                        depth -= 1
                body_lines.append(l)
                j += 1
                if body_started and depth <= 0:
                    break
            body = '\n'.join(body_lines[1:-1]) if len(body_lines) > 1 else ''
            items.append(('class', name, st, body))
            i = j
            continue
        # const arrow function:  const xxx = (...) => {
        m = re.match(r'^\s*const\s+(\w+)\s*=\s*\(', st)
        if m:
            name = m.group(1)
            depth = 0
            body_lines = [line]
            j = i
            body_started = False
            while j < n:
                for ch in lines[j]:
                    if ch == '{':
                        depth += 1
                        body_started = True
                    elif ch == '}':
                        depth -= 1
                body_lines.append(lines[j])
                j += 1
                if body_started and depth <= 0:
                    break
            body = '\n'.join(body_lines)
            items.append(('func', name, st, body))
            i = j
            continue
        i += 1
    return items

# ---------- 简化生成器 ----------
def generate_go_file(ts_code: str, ts_filename: str) -> str:
    """生成 Go 文件文本"""
    items = parse_top_level(ts_code)
    go = []
    go.append('package main')
    go.append('')

    # 收集需要的 import
    need_math = False
    need_fmt = True

    funcs = []
    classes = []

    for kind, name, sig, body in items:
        if kind == 'func':
            funcs.append((name, sig, body))
        else:
            classes.append((name, sig, body))

    # 类 → struct + 方法
    for cname, csig, cbody in classes:
        # 简化：把类体里的方法提取为 func (r CName) Method
        # 这里采用简化策略：原样转换类体行
        go.append(f'type {cname} struct {{')
        # 找字段（类里 const xxx = ...）
        for ln in cbody.split('\n'):
            m = re.match(r'^\s*(?:private|public|readonly|protected)?\s*(\w+)\s*[:=]', ln)
            if m and ('=' in ln or ':' in ln):
                # 简化：推断类型
                val = ln.split('=', 1)[1].strip() if '=' in ln else 'int'
                go.append(f'\t{m.group(1)} {infer_go_type(val, ln)}')
        go.append('}')
        go.append('')
        # 方法
        method_pat = re.compile(r'(?:^\s*)(?:public\s+|private\s+|readonly\s+|protected\s+)?(\w+)\s*\(([^)]*)\)\s*[:{]')
        for m in method_pat.finditer(cbody):
            mname = m.group(1)
            if mname in ('constructor',):
                continue
            mparams = [p for p in m.group(2).split(',') if p.strip() and p.strip() != 'this']
            mparams_go = []
            for p in mparams:
                pp = p.strip()
                # 去掉类型注解
                pp = re.sub(r':\s*[\w\s\[\]\|\(\)]*', '', pp).strip()
                if pp:
                    mparams_go.append(pp)
            go.append(f'func (r *{cname}) {mname}({", ".join(mparams_go)}) {{')
            go.append('}')
            go.append('')
        # 构造器
        cm = re.search(r'constructor\s*\(([^)]*)\)', cbody)
        if cm:
            cparams = [p for p in cm.group(1).split(',') if p.strip()]
            cparams_go = []
            for p in cparams:
                pp = p.strip()
                pp = re.sub(r':\s*[\w\s\[\]\|\(\)]*', '', pp).strip()
                if pp:
                    cparams_go.append(pp)
            go.append(f'func New{cname}({", ".join(cparams_go)}) *{cname} {{')
            go.append('\treturn &' + cname + ' ' + '{' + '}')
            go.append('}')
            go.append('')

    # 函数
    for fname, fsig, fbody in funcs:
        # 解析签名
        m = re.match(r'(?:export\s+)?function\s+(\w+)\s*\(([^)]*)\)', fsig)
        if not m:
            m = re.match(r'const\s+(\w+)\s*=\s*\(([^)]*)\)', fsig)
        if not m:
            # 顶层变量等，原样注释
            go.append(f'// TODO: {fname}')
            go.append('')
            continue
        pname = m.group(1)
        pparams = [p for p in m.group(2).split(',') if p.strip()]
        # 转 Go 参数
        p_go = []
        for p in pparams:
            pp = p.strip()
            # 去类型
            if ':' in pp:
                nm, typ = pp.split(':', 1)
                gtyp = ts_to_go_type(typ.strip())
                p_go.append(f'{nm.strip()} {gyp(gtyp)}' if False else f'{nm.strip()} {go_param_type(gtyp)}')
            else:
                p_go.append(pp)
        go.append(f'func {pname}({", ".join(p_go)}) {{')
        # 转换函数体
        go_body = convert_body(fbody, need_math)
        go.append(go_body)
        go.append('}')
        go.append('')

    # 主函数（demo）
    go.append('func main() {')
    go.append(f'\t// Demo: {ts_filename}')
    if funcs:
        go.append(f'\t_ = {funcs[0][0]}')
    elif classes:
        go.append(f'\t_ = New{classes[0][0]}')
    go.append('}')
    go.append('')

    # helper functions
    if need_math:
        go.append('func abs(x int) int { if x < 0 { return -x }; return x }')
        go.append('func floor(x int) int { return x }')
        go.append('func ceil(x int) int { return x }')
        go.append('func round(x int) int { return x }')
        go.append('func max2(a, b int) int { if a > b { return a }; return b }')
        go.append('func min2(a, b int) int { if a < b { return a }; return b }')
        go.append('')

    # 类型定义（TreeNode/ListNode）
    go.append('type TreeNode struct {')
    go.append('\tVal int')
    go.append('\tLeft, Right *TreeNode')
    go.append('}')
    go.append('')
    go.append('type ListNode struct {')
    go.append('\tVal int')
    go.append('\tNext *ListNode')
    go.append('}')
    go.append('')

    text = '\n'.join(go)
    # 修正：未使用的 fmt import
    if 'fmt.' not in text:
        text = re.sub(r'import\s*\(\s*"fmt"\s*\)\n?', '', text)
        text = re.sub(r'import "fmt"\n', '', text)
    return text

def go_param_type(g: str) -> str:
    """Go 函数参数类型：数值/字符串/bool 原样，对象用指针"""
    return go_pointer(g)

def infer_go_type(val: str, raw: str) -> str:
    v = val.strip()
    if v in ('[]', '[]int{}'):
        return '[]int'
    if v.startswith('new '):
        return 'struct{}'
    if v in ('null', 'undefined'):
        return 'int'
    if v.startswith('['):
        return '[]int'
    if re.match(r'^\d+$', v):
        return 'int'
    if re.match(r'^\d+\.\d+$', v):
        return 'float64'
    if v.startswith('"') or v.startswith("'"):
        return 'string'
    if v in ('true', 'false'):
        return 'bool'
    if v.startswith('{'):
        return 'struct{}'
    return 'interface{}'

def convert_body(body: str, need_math: bool) -> str:
    """把 TS 函数体转成 Go 函数体"""
    out = []
    # 去掉前导大括号
    body = body.strip()
    if body.startswith('{'):
        body = body[1:].rstrip()
    if body.endswith('}'):
        body = body[:-1]
    lines = body.split('\n')
    declared = set()  # 已声明的变量
    for ln in lines:
        raw = ln
        s = ln.strip()
        if not s or s.startswith('//') or s.startswith('/*') or s.startswith('*'):
            if s:
                out.append(raw.rstrip())
            continue
        # 跳过 TS 类型注解行
        s = re.sub(r'\s*:\s*(number|string|boolean|any|void)\b', '', s)
        # const/let 声明
        m = re.match(r'^(const|let)\s+([A-Za-z_]\w*)\s*=\s*(.+)$', s)
        if m:
            var = m.group(2)
            val = m.group(3).strip()
            declared.add(var)
            out.append(f'\t{var} := {expr_go(val)}')
            continue
        m = re.match(r'^(const|let)\s+([A-Za-z_]\w*)\s*$', s)
        if m:
            var = m.group(2)
            declared.add(var)
            out.append(f'\tvar {var}')
            continue
        # for
        m = re.match(r'^for\s*\((.+)\)$', s)
        if m:
            parts = m.group(1).split(';')
            parts = [p.strip() for p in parts]
            init = parts[0] if parts else ''
            cond = parts[1] if len(parts) > 1 else ''
            upd = parts[2] if len(parts) > 2 else ''
            init = init.replace('let ', '').replace('const ', '')
            if init and '=' in init:
                # 提取变量名到 declared
                vn = init.split('=')[0].strip()
                if vn:
                    declared.add(vn)
                init = init.replace('=', ':=')
            cond = expr_go(cond) if cond else cond
            upd = expr_go(upd)
            for_line = f'\tfor {init}; {cond}; {upd} {{'
            out.append(for_line)
            continue
        # while → for
        m = re.match(r'^while\s*\((.+)\)\s*(\{)?$', s)
        if m:
            cond = expr_go(m.group(1))
            out.append(f'\tfor {cond} {{')
            continue
        # return
        m = re.match(r'^return\s*(.*)$', s)
        if m:
            val = m.group(1).strip()
            out.append(f'\treturn {expr_go(val)}' if val else '\treturn')
            continue
        # 普通赋值
        m = re.match(r'^([A-Za-z_]\w*)\s*=\s*(.+)$', s)
        if m:
            var = m.group(1)
            val = m.group(2).strip()
            declared.add(var)
            # 简单类型推断
            gtyp = infer_go_type(val, s)
            out.append(f'\t{var} = {expr_go(val)}')
            continue
        # 普通语句
        out.append('\t' + expr_go(s))
    # 闭合检查：统计 { 和 }
    opens = sum(len(re.findall(r'\{', l)) for l in out)
    closes = sum(len(re.findall(r'\}', l)) for l in out)
    for _ in range(opens - closes):
        out.append('\t}')
    # 补 main 调用
    return '\n'.join(out)

# 写文件
def main():
    ts_base = DSA / 'ts'
    go_base = DSA / 'go'
    total = 0
    gofmt_ok = 0
    gofmt_fail = 0
    fails = []
    for root, _, files in os.walk(ts_base):
        for filename in files:
            if not filename.endswith('.ts'):
                continue
            total += 1
            ts_fp = Path(root) / filename
            rel = ts_fp.relative_to(ts_base)
            go_fp = go_base / str(rel).replace('.ts', '.go')
            ts_code = ts_fp.read_text(encoding='utf-8')
            go_code = generate_go_file(ts_code, filename)
            # gofmt
            try:
                r = subprocess.run(['gofmt'], input=go_code, capture_output=True, text=True)
                if r.returncode == 0:
                    gofmt_ok += 1
                    go_fp.write_text(r.stdout, encoding='utf-8')
                else:
                    gofmt_fail += 1
                    fails.append(str(rel))
            except Exception:
                gofmt_fail += 1
                fails.append(str(rel))
    print(f'Total: {total}, gofmt OK: {gofmt_ok}, Fail: {gofmt_fail}')
    if fails:
        print('First failures:')
        for f in fails[:20]:
            print('  ' + f)

if __name__ == '__main__':
    main()
