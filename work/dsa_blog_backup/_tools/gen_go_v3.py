#!/usr/bin/env python3
"""
gen_go_v3.py — 从修复后的 TS 源生成 gofmt 通过的 Go 代码。

设计要点（ponytail）：
  * 保留原 Go 代码结构（package main + helper funcs + 主函数 + main/demo）
  * 只把 TS 专有语法翻译成 Go，不再做过度重写
  * 顶层 function/class/const 分别处理；嵌套 function 提升为顶层具名函数
  * gofmt 验证；若通过则写盘，失败则保留原 Go 内容（不再污染）
"""
import re, os, subprocess
from pathlib import Path

DSA = Path('/Users/Wang/Code/webfault-ai/dsa')

# ---------- 类型映射 ----------
TYPE_MAP = {
    'number': 'int', 'float': 'float64', 'string': 'string',
    'boolean': 'bool', 'void': '', 'any': 'interface{}',
    'null': 'interface{}', 'undefined': 'interface{}',
}

def ts_type_go(t: str) -> str:
    t = t.strip()
    if t in TYPE_MAP:
        return TYPE_MAP[t]
    # X | null / X | undefined
    if '|' in t:
        parts = [p.strip() for p in t.split('|') if p.strip() not in ('null', 'undefined', '')]
        if parts:
            return ts_type_go(parts[0])
        return 'interface{}'
    # 数组
    m = re.match(r'^(\w+)\s*\[\](\[\])?$', t)
    if m:
        base = ts_type_go(m.group(1))
        return f'[]{base}{m.group(2) or ""}'
    # [][]X
    m = re.match(r'^(\w+)\s*(\[\])(\[\])$', t)
    if m:
        return f'[][]{ts_type_go(m.group(1))}'
    # 可空对象
    if t.startswith('Array<'):
        return '[]interface{}'
    # 已知结构体
    if t in ('TreeNode', 'ListNode', 'NestedInteger', 'PQ', 'Status', 'MaxHeap', 'MinHeap', 'MedianFinder', 'Bitset', 'SortedStack'):
        return t
    return t

def param_type_go(t: str) -> str:
    """参数位置：对象/结构体用指针，数值/字符串/bool 原样"""
    g = ts_type_go(t)
    if g in ('int', 'string', 'bool', 'float64', 'float32', 'byte', 'uint', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64'):
        return g
    if g.startswith('[]') or g.startswith('map'):
        return g
    return '*' + g if g else 'interface{}'

# ---------- 表达式翻译 ----------
def expr_go(s: str) -> str:
    """把 TS 表达式片段翻译成 Go。只做最保守的替换。"""
    if not s:
        return s
    # 简化：把 TS 表达式片段翻译成 Go（保守替换）
    s = s.replace('===', '==').replace('!==', '!=')
    # Math.*
    s = s.replace('Math.abs(', 'abs(')
    s = s.replace('Math.floor(', 'floor(')
    s = s.replace('Math.ceil(', 'ceil(')
    s = s.replace('Math.round(', 'round(')
    s = s.replace('Math.max(', 'max2(')
    s = s.replace('Math.min(', 'min2(')
    s = s.replace('Math.pow(', 'pow2(')
    s = s.replace('Math.sqrt(', 'sqrt(')
    s = s.replace('Math.log(', 'log(')
    s = s.replace('Math.random()', 'rand.Float64()')
    # 数字转换
    s = s.replace('Number(', 'toNum(')
    s = s.replace('String(', 'toStr(')
    s = s.replace('parseInt(', 'toInt(')
    s = s.replace('parseFloat(', 'toFloat(')
    s = s.replace('NaN', '0')
    # 三目 a ? b : c → tern(cond, b, c)
    s = re.sub(r'(\w+)\s*\?\s*([^:]+?)\s*:\s*(\w+)\b',
               lambda m: f'tern({m.group(1)}, {m.group(2)}, {m.group(3)})', s)
    # null → nil
    s = s.replace('null', 'nil')
    s = s.replace('undefined', 'nil')
    # 模板字符串：先用引号包裹整段（保守），去掉 ${}
    if '`' in s:
        s = s.replace('`', '').replace('`${', '').replace('}', '').replace('${', '').replace('}', '')
        s = s.strip()
    # 数组方法（Go 里没有这些内置，保守保留为注释占位）
    # 字符串方法（保留原样，靠 helper 不支持时也至少语法合法）
    s = s.replace('charCodeAt(', 'CharCode(')
    s = s.replace('charAt(', 'CharAt(')
    s = s.replace('toUpperCase(', 'ToUpper(')
    s = s.replace('toLowerCase(', 'ToLower(')
    s = s.replace('trim()', 'Trim()')
    s = s.replace('trimStart()', 'TrimLeft()')
    s = s.replace('trimEnd()', 'TrimRight()')
    s = s.replace('startsWith(', 'HasPrefix(')
    s = s.replace('endsWith(', 'HasSuffix(')
    s = s.replace('indexOf(', 'Index(')
    s = s.replace('includes(', 'Contains(')
    s = s.replace('concat(', 'Concat(')
    s = s.replace('substring(', 'Substr(')
    s = s.replace('substr(', 'Substr(')
    # 数组/Map 方法（保留原样作为 TODO 占位）
    return s

# ---------- 整行翻译 ----------
def line_go(line: str) -> str:
    s = line.rstrip('\n')
    # 保留缩进
    m = re.match(r'^(\s*)(.*)$', s)
    indent = m.group(1) if m else ''
    body = m.group(2).strip() if m else s.strip()
    # 空行/注释
    if not body or body.startswith('//') or body.startswith('/*') or body.startswith('*') or body.startswith('*/'):
        return s.rstrip()
    # 去掉 const/let/var（TS 关键字）
    body2 = re.sub(r'^\s*(const|let|var)\s+', '', body)
    # 去掉 类型注解  x: number = ...
    body2 = re.sub(r'(\w+)\s*:\s*([\w\[\]\s|]+?)\s*=', lambda m: m.group(1) + ' =', body2)
    body2 = re.sub(r'(\w+)\s*:\s*(\w+)\s*$', lambda m: m.group(1), body2)
    # for 循环
    m = re.match(r'^for\s*\(\s*([^;]*?);\s*([^;]*?);\s*([^)]*)\)\s*(\{?)$', body2)
    if m:
        init = m.group(1).strip()
        cond = m.group(2).strip()
        upd = m.group(3).strip()
        brace = m.group(4)
        # 初始化声明
        if '=' in init:
            var, val = init.split('=', 1)
            init_g = f'{var.strip()} := {expr_go(val.strip())}'
        elif init:
            init_g = expr_go(init)
        else:
            init_g = ''
        cond_g = expr_go(cond) if cond else ''
        upd_g = expr_go(upd) if upd else ''
        # 单行 if cond 不带 { 的情况
        return f'{indent}for {init_g}; {cond_g}; {upd_g} {brace}' if brace else f'{indent}for {init_g}; {cond_g}; {upd_g}'
    # while → for
    m = re.match(r'^while\s*\((.+)\)\s*(\{?)$', body2)
    if m:
        cond = expr_go(m.group(1))
        brace = m.group(2)
        return f'{indent}for {cond} {brace}' if brace else f'{indent}for {cond}'
    # return
    m = re.match(r'^return\s*(.*)$', body2)
    if m:
        val = m.group(1).strip()
        return f'{indent}return {expr_go(val)}' if val else f'{indent}return'
    # 普通赋值
    m = re.match(r'^([A-Za-z_]\w*)\s*=\s*(.+)$', body2)
    if m:
        var = m.group(1)
        val = expr_go(m.group(2))
        # 如果值里有函数调用，可能已声明过 → 用 = 而不是 :=
        return f'{indent}{var} = {val}'
    # 带 := 的声明
    m = re.match(r'^([A-Za-z_]\w*)\s*:=\s*(.+)$', body2)
    if m:
        return f'{indent}{m.group(1)} := {expr_go(m.group(2))}'
    # 函数调用 / 其他语句
    return f'{indent}{expr_go(body2)}'

# ---------- 顶层解析 ----------
def parse_top_level(src: str):
    """解析 TS 顶层的 function / class / const-arrow 声明。
    返回 (funcs, classes)：
      funcs: [(name, params_str, return_type_str, body_str)]
      classes: [(name, body_str)]
    body_str 保留原始（带内部嵌套 function）。
    """
    lines = src.split('\n')
    n = len(lines)
    funcs = []
    classes = []
    i = 0
    while i < n:
        line = lines[i]
        s = line.strip()
        # 普通 function
        if s.startswith('function ') or s.startswith('export function '):
            # 找到函数体：从首个 { 到匹配 }
            depth = 0
            started = False
            j = i
            body_lines = []
            while j < n:
                for ch in lines[j]:
                    if ch == '{':
                        depth += 1
                        started = True
                    elif ch == '}':
                        depth -= 1
                body_lines.append(lines[j])
                j += 1
                if started and depth == 0:
                    break
            sig = ' '.join(lines[i:i+1])
            m = re.match(r'(?:export\s+)?function\s+(\w+)\s*\(([^)]*)\)\s*[:\s]*(.*)\{', sig)
            if m:
                name = m.group(1)
                params = m.group(2)
                ret = (m.group(3) or '').strip()
                body = '\n'.join(body_lines[1:-1]) if len(body_lines) > 1 else ''
                funcs.append((name, params, ret, body))
            i = j
            continue
        # class
        if s.startswith('class '):
            m = re.match(r'class\s+(\w+)', s)
            name = m.group(1) if m else 'Unknown'
            depth = 0
            started = False
            j = i
            body_lines = []
            while j < n:
                for ch in lines[j]:
                    if ch == '{':
                        depth += 1
                        started = True
                    elif ch == '}':
                        depth -= 1
                body_lines.append(lines[j])
                j += 1
                if started and depth == 0:
                    break
            body = '\n'.join(body_lines[1:-1]) if len(body_lines) > 1 else ''
            classes.append((name, body))
            i = j
            continue
        # const arrow：const xxx = (...) => {
        m = re.match(r'^\s*const\s+(\w+)\s*=\s*(\([^)]*\))\s*=>\s*\{?', s)
        if m:
            name = m.group(1)
            params = m.group(2).strip('()')
            # 找函数体
            depth = 0
            started = False
            j = i
            body_lines = []
            while j < n:
                for ch in lines[j]:
                    if ch == '{':
                        depth += 1
                        started = True
                    elif ch == '}':
                        depth -= 1
                body_lines.append(lines[j])
                j += 1
                if started and depth == 0:
                    break
            body = '\n'.join(body_lines[1:-1]) if len(body_lines) > 1 else ''
            funcs.append((name, params, '', body))
            i = j
            continue
        i += 1
    return funcs, classes

def convert_params_go(params_str: str) -> str:
    if not params_str or not params_str.strip():
        return ''
    out = []
    # 拆分参数（处理嵌套括号，简单按 top-level 逗号切）
    parts = split_top(params_str)
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if ':' in p:
            name, typ = p.split(':', 1)
            g = param_type_go(typ.strip())
            out.append(f'{name.strip()} {g}')
        else:
            out.append(p)
    return ', '.join(out)

def split_top(s: str):
    """按顶层逗号切分（忽略括号内的逗号）"""
    parts = []
    depth = 0
    cur = ''
    for ch in s:
        if ch in '([{':
            depth += 1
            cur += ch
        elif ch in ')]}':
            depth -= 1
            cur += ch
        elif ch == ',' and depth == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += ch
    if cur:
        parts.append(cur)
    return parts

# 简单：把 TS 函数体 → Go 函数体（逐行翻译，保留嵌套 function 调用）
def convert_body(body: str) -> str:
    out = []
    # 把内部嵌套的 function xxx(...) 提取为顶层（记录名字）
    # 做法：找出所有 "function NAME(" 嵌套声明，把它们从 body 中移除并加入顶层
    nested = []
    body_lines = body.split('\n')
    new_lines = []
    i = 0
    while i < len(body_lines):
        ln = body_lines[i]
        m = re.match(r'^\s*function\s+(\w+)\s*\(', ln)
        if m:
            name = m.group(1)
            depth = 0
            started = False
            j = i
            block = []
            while j < len(body_lines):
                for ch in body_lines[j]:
                    if ch == '{':
                        depth += 1
                        started = True
                    elif ch == '}':
                        depth -= 1
                block.append(body_lines[j])
                j += 1
                if started and depth == 0:
                    break
            nested.append('\n'.join(block))
            i = j
            continue
        new_lines.append(ln)
        i += 1
    body2 = '\n'.join(new_lines)
    # 逐行翻译
    out_lines = []
    for ln in body2.split('\n'):
        out_lines.append(line_go(ln))
    body_go = '\n'.join(out_lines)
    return body_go, nested

def gen_file(ts_code: str, ts_name: str, go_name: str) -> str:
    funcs, classes = parse_top_level(ts_code)
    # 收集顶层嵌套
    all_nested = []
    go_blocks = []

    # 类 → Go struct + 方法
    for cname, cbody in classes:
        # 提取字段
        fields = []
        methods = []
        # 简化：class 体里 const/let 字段
        for ln in cbody.split('\n'):
            m = re.match(r'^\s*(?:private|public|readonly|protected)?\s*(\w+)\s*[:=]', ln)
            if m:
                name = m.group(1)
                # 字段类型推断
                if '=' in ln:
                    val = ln.split('=', 1)[1].strip()
                    fields.append((name, infer_field_type(val)))
                elif ':' in ln:
                    typ = ln.split(':', 1)[1].split(';')[0].strip()
                    fields.append((name, ts_type_go(typ)))
        # 方法
        method_pat = re.compile(r'(?:public\s+|private\s+|readonly\s+|protected\s+)?(\w+)\s*\(([^)]*)\)\s*(?::\s*[\w\s\[\]]*\s*)?\{')
        for m in method_pat.finditer(cbody):
            mname = m.group(1)
            if mname in ('constructor',):
                continue
            mparams = convert_params_go(m.group(2))
            # 提取方法体（简化：找匹配的 }）
            start = m.end()
            depth = 1
            j = start
            while j < len(cbody) and depth > 0:
                if cbody[j] == '{':
                    depth += 1
                elif cbody[j] == '}':
                    depth -= 1
                j += 1
            mbody = cbody[start:j-1]
            methods.append((mname, mparams, mbody))
        # 构造器
        cm = re.search(r'constructor\s*\(([^)]*)\)', cbody)
        cparams = convert_params_go(cm.group(1)) if cm else ''
        # 生成 struct
        go_blocks.append(f'type {cname} struct {{')
        for fname, ftype in fields:
            go_blocks.append(f'\t{fname} {ftype}')
        go_blocks.append('}')
        go_blocks.append('')
        # 构造器
        go_blocks.append(f'func New{cname}({cparams}) *{cname} {{')
        go_blocks.append(f'\treturn &{cname}{{}}')
        go_blocks.append('}')
        go_blocks.append('')
        # 方法
        for mname, mparams, mbody in methods:
            go_blocks.append(f'func (r *{cname}) {mname}({mparams}) {{')
            mbody_go, nested2 = convert_body(mbody)
            go_blocks.append(mbody_go)
            go_blocks.append('}')
            go_blocks.append('')
            all_nested.extend(nested2)

    # 函数
    for fname, fparams, fret, fbody in funcs:
        params_go = convert_params_go(fparams)
        ret_go = ts_type_go(fret) if fret else ''
        sig = f'func {fname}({params_go})'
        if ret_go:
            sig += f' {ret_go}'
        go_blocks.append(sig + ' {')
        body_go, nested2 = convert_body(fbody)
        go_blocks.append(body_go)
        go_blocks.append('}')
        go_blocks.append('')
        all_nested.extend(nested2)

    # 嵌套函数（提升为顶层）
    for nblock in all_nested:
        go_blocks.append(nblock_go(nblock))
        go_blocks.append('')

    # main 函数（demo）
    go_blocks.append('func main() {')
    go_blocks.append(f'\t// Demo: {go_name}')
    if funcs:
        go_blocks.append(f'\t_ = {funcs[0][0]}')
    elif classes:
        go_blocks.append(f'\t_ = New{classes[0][0]}')
    go_blocks.append('}')
    go_blocks.append('')

    # 类型定义
    go_blocks.append('type TreeNode struct {')
    go_blocks.append('\tVal int')
    go_blocks.append('\tLeft, Right *TreeNode')
    go_blocks.append('}')
    go_blocks.append('')
    go_blocks.append('type ListNode struct {')
    go_blocks.append('\tVal int')
    go_blocks.append('\tNext *ListNode')
    go_blocks.append('}')
    go_blocks.append('')

    # helper funcs（所有 import 放文件顶部，函数体内不能 import）
    go_blocks.append('func abs(x int) int { if x < 0 { return -x }; return x }')
    go_blocks.append('func floor(x int) int { return x }')
    go_blocks.append('func ceil(x int) int { return x }')
    go_blocks.append('func round(x int) int { return x }')
    go_blocks.append('func max2(a, b int) int { if a > b { return a }; return b }')
    go_blocks.append('func min2(a, b int) int { if a < b { return a }; return b }')
    go_blocks.append('func pow2(a, b int) int { r := 1; for i := 0; i < b; i++ { r *= a }; return r }')
    go_blocks.append('func sqrt(x int) int { return int(math.Sqrt(float64(x))) }')
    go_blocks.append('func log(x int) float64 { return math.Log(float64(x)) }')
    go_blocks.append('func toNum(s string) int { i, _ := strconv.Atoi(s); return i }')
    go_blocks.append('func toStr(v int) string { return strconv.Itoa(v) }')
    go_blocks.append('func toInt(s string) int { i, _ := strconv.Atoi(s); return i }')
    go_blocks.append('func toFloat(s string) float64 { f, _ := strconv.ParseFloat(s, 64); return f }')
    go_blocks.append('func tern(cond bool, a, b int) int { if cond { return a }; return b }')
    go_blocks.append('')

    text = 'package main\n\nimport (\n\t"math"\n\t"math/rand"\n\t"strconv"\n)\n\n' + '\n'.join(go_blocks)
    return text

def nblock_go(nblock: str) -> str:
    """把嵌套的 function xxx(...) 块转成 Go 顶层函数"""
    m = re.match(r'^\s*function\s+(\w+)\s*\(([^)]*)\)', nblock)
    if not m:
        return nblock  # 原样
    name = m.group(1)
    params = m.group(2)
    # 找函数体
    depth = 0
    started = False
    j = 0
    lines = nblock.split('\n')
    for k, ln in enumerate(lines):
        for ch in ln:
            if ch == '{':
                depth += 1
                started = True
            elif ch == '}':
                depth -= 1
        if started and depth == 0:
            j = k
            break
    sig_params = convert_params_go(params)
    out = [f'func {name}({sig_params}) {{']
    body = '\n'.join(lines[1:j])
    body_go, _ = convert_body(body)
    out.append(body_go)
    out.append('}')
    return '\n'.join(out)

def infer_field_type(val: str) -> str:
    v = val.strip()
    if v in ('[]', '[]int{}'):
        return '[]int'
    if v.startswith('new '):
        return 'struct{}'
    if v in ('null', 'undefined'):
        return 'interface{}'
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
        return 'map[string]interface{}'
    if v.startswith('new '):
        return 'struct{}'
    return 'interface{}'

# ---------- 主流程 ----------
def main():
    ts_base = DSA / 'ts'
    go_base = DSA / 'go'
    total = 0
    gofmt_ok = 0
    gofmt_fail = 0
    fails = []
    for root, _, files in os.walk(ts_base):
        for filename in sorted(files):
            if not filename.endswith('.ts'):
                continue
            total += 1
            ts_fp = Path(root) / filename
            rel = ts_fp.relative_to(ts_base)
            go_fp = go_base / str(rel).replace('.ts', '.go')
            ts_code = ts_fp.read_text(encoding='utf-8')
            go_code = gen_file(ts_code, filename, filename)
            # gofmt 验证
            try:
                r = subprocess.run(['gofmt'], input=go_code, capture_output=True, text=True)
                if r.returncode == 0:
                    gofmt_ok += 1
                    go_fp.write_text(r.stdout, encoding='utf-8')
                else:
                    gofmt_fail += 1
                    fails.append((str(rel), r.stderr[:200]))
            except Exception as e:
                gofmt_fail += 1
                fails.append((str(rel), str(e)[:100]))
    print(f'Total: {total}, gofmt OK: {gofmt_ok}, Fail: {gofmt_fail}')
    for f, err in fails[:30]:
        print(f'  {f}: {err}')

if __name__ == '__main__':
    main()
