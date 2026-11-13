#!/usr/bin/env python3
"""
简单但有效的 TS → Python/Go/Java 转换器
"""
import os
import re
from pathlib import Path

DSA_DIR = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa')


def clean_ts(code: str) -> str:
    """清理 TypeScript 代码"""
    # 移除多行注释
    code = re.sub(r'/\*\*[\s\S]*?\*/', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    # 移除单行注释
    code = re.sub(r'//[^\n]*', '', code)
    return code


def to_python(ts: str) -> str:
    """TS → Python"""
    ts = clean_ts(ts)
    lines = ts.split('\n')
    result = []
    indent = 0
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # 函数定义
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params = []
            if m.group(2).strip():
                for p in m.group(2).split(','):
                    p = p.strip()
                    if ':' in p:
                        params.append(p.split(':')[0].strip())
                    else:
                        params.append(p)
            result.append(f"def {name}({', '.join(params)}):")
            indent = 1
            continue
        
        # class 定义
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            result.append(f"class {m.group(1)}:")
            indent = 1
            continue
        
        # constructor
        if 'constructor' in s:
            result.append("    def __init__(self):")
            continue
        
        # 大括号
        if s == '{':
            indent += 1
            continue
        elif s == '}':
            indent = max(0, indent - 1)
            continue
        
        # 转换语句
        line = s
        
        # 移除类型注解（复杂模式）
        line = re.sub(r':\s*(?:string|number|boolean|void|null|undefined|string\[\]|number\[\]|boolean\[\])', '', line)
        line = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*(?:\[\])?', '', line)
        
        # this. → 空
        line = line.replace('this.', '')
        
        # null/undefined → None
        line = line.replace('null', 'None').replace('undefined', 'None')
        
        # 布尔值
        line = line.replace('true', 'True').replace('false', 'False')
        line = line.replace('===', '==').replace('!==', '!=')
        
        # 数组长度
        line = re.sub(r'(\w+)\.length\b', r'len(\1)', line)
        
        # 数组方法
        line = line.replace('.push(', '.append(')
        line = line.replace('.pop()', '.pop()')
        line = line.replace('.shift()', '.pop(0)')
        
        # console.log
        line = line.replace('console.log(', 'print(')
        
        # Math
        line = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', line)
        line = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', line)
        line = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', line)
        line = line.replace('Math.random()', 'random.random()')
        
        # 三元表达式
        line = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)(?:;|$)', r'(\2 if \1 else \3)', line)
        
        # for...of
        line = re.sub(r'for\s*\(\s*const\s+(\w+)\s*of\s+(\w+)', r'for \1 in \2', line)
        
        # new Map/Set
        line = line.replace('new Map()', 'dict()')
        line = line.replace('new Set()', 'set()')
        
        # slice
        line = re.sub(r'(\w+)\.slice\((\w+)\)', r'\1[\2:]', line)
        line = re.sub(r'(\w+)\.slice\((\w+),\s*(\w+)\)', r'\1[\2:\3]', line)
        
        # return
        if line.startswith('return'):
            result.append('    ' * indent + line)
        elif line:
            result.append('    ' * indent + line)
    
    return '\n'.join(result)


def to_go(ts: str) -> str:
    """TS → Go"""
    ts = clean_ts(ts)
    lines = ts.split('\n')
    result = ['package main', '', 'import "fmt"', '']
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # 函数定义
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params = []
            ret = ''
            
            # 参数
            if m.group(2).strip():
                for p in m.group(2).split(','):
                    p = p.strip()
                    if ':' in p:
                        pname, ptype = p.split(':', 1)
                        ptype = ptype.strip()
                        if ptype == 'number': ptype = 'int'
                        elif ptype == 'string': ptype = 'string'
                        elif ptype == 'boolean': ptype = 'bool'
                        elif ptype.endswith('[]'):
                            ptype = ptype[:-2]
                            if ptype == 'number': ptype = 'int'
                            params.append(f"{pname.strip()} []{ptype}")
                        else:
                            params.append(f"{pname.strip()} {ptype}")
                    else:
                        params.append(p)
            
            # 返回类型
            ret_match = re.search(r':\s*(\w+(?:\[\]|\|[^\)]+)?)\s*$', s)
            if ret_match:
                ret_type = ret_match.group(1).strip()
                if ret_type != 'void':
                    if ret_type == 'number': ret = ' int'
                    elif ret_type == 'string': ret = ' string'
                    elif ret_type == 'boolean': ret = ' bool'
                    elif ret_type.endswith('[]'):
                        ret = f' []{ret_type[:-2]}'
            
            result.append(f"func {name}({', '.join(params)}){ret} {{")
            continue
        
        # class 定义
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            result.append(f"type {m.group(1)} struct {{")
            continue
        
        # 大括号
        if s == '{':
            continue
        elif s == '}':
            result.append('}')
            continue
        
        # 转换语句
        line = s
        line = line.replace('this.', '')
        line = line.replace('null', 'nil').replace('undefined', 'nil')
        line = line.replace('===', '==').replace('!==', '!=')
        line = re.sub(r'(\w+)\.length\b', r'len(\1)', line)
        line = re.sub(r'(\w+)\.push\((.+?)\)', r'append(\1, \2)', line)
        line = re.sub(r'(\w+)\.pop\(\)', r'\1[len(\1)-1]', line)
        line = line.replace('console.log(', 'fmt.Println(')
        line = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', line)
        line = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', line)
        line = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', line)
        line = re.sub(r'new\s+(\w+)', r'&\1{}', line)
        
        if line:
            result.append('    ' + line)
    
    result.append('')
    result.append('func main() {}')
    return '\n'.join(result)


def to_java(ts: str) -> str:
    """TS → Java"""
    ts = clean_ts(ts)
    lines = ts.split('\n')
    result = ['package com.webfault.dsa;', '', 'import java.util.*;', '']
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # 函数定义
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params = []
            ret = 'void'
            
            # 参数
            if m.group(2).strip():
                for p in m.group(2).split(','):
                    p = p.strip()
                    if ':' in p:
                        pname, ptype = p.split(':', 1)
                        ptype = ptype.strip()
                        if ptype == 'number': ptype = 'int'
                        elif ptype == 'string': ptype = 'String'
                        elif ptype == 'boolean': ptype = 'boolean'
                        elif ptype.endswith('[]'):
                            base = ptype[:-2]
                            if base == 'number': base = 'int'
                            ptype = base + '[]'
                        params.append(f"{ptype} {pname.strip()}")
                    else:
                        params.append(p)
            
            # 返回类型
            ret_match = re.search(r':\s*(\w+(?:\[\]|\|[^\)]+)?)\s*$', s)
            if ret_match:
                ret_type = ret_match.group(1).strip()
                if ret_type != 'void':
                    if ret_type == 'number': ret = 'int'
                    elif ret_type == 'string': ret = 'String'
                    elif ret_type == 'boolean': ret = 'boolean'
                    elif ret_type.endswith('[]'):
                        base = ret_type[:-2]
                        if base == 'number': base = 'int'
                        ret = base + '[]'
            
            result.append(f'public {ret} {name}({", ".join(params)}) {{')
            continue
        
        # class 定义
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            result.append(f'public class {m.group(1)} {{')
            continue
        
        # 大括号
        if s == '{':
            continue
        elif s == '}':
            result.append('}')
            continue
        
        # 转换语句
        line = s
        line = line.replace('this.', '')
        line = line.replace('null', 'null').replace('undefined', 'null')
        line = line.replace('===', '==').replace('!==', '!=')
        line = re.sub(r'(\w+)\.length\b', r'\1.length', line)
        line = line.replace('.push(', '.add(')
        line = re.sub(r'(\w+)\.pop\(\)', r'\1.remove(\1.size()-1)', line)
        line = line.replace('console.log(', 'System.out.println(')
        line = re.sub(r'Math\.floor\((.+?)\)', r'(int)(\1)', line)
        line = re.sub(r'Math\.max\((.+?)\)', r'Math.max(\1)', line)
        line = re.sub(r'Math\.min\((.+?)\)', r'Math.min(\1)', line)
        line = re.sub(r'new\s+(\w+)', r'new \1()', line)
        
        if line:
            result.append('    ' + line)
    
    return '\n'.join(result)


def main():
    print("=== Simple Robust Converter ===\n")
    
    ts_base = DSA_DIR / 'ts'
    converters = {
        'python': ('.py', to_python),
        'go': ('.go', to_go),
        'java': ('.java', to_java)
    }
    
    for lang, (ext, converter) in converters.items():
        dst_base = DSA_DIR / "code" / lang
        count = 0
        errors = 0
        
        for root, dirs, files in os.walk(ts_base):
            dst_root = dst_base / Path(root).relative_to(ts_base)
            if not dst_root.exists():
                dst_root.mkdir(parents=True, exist_ok=True)
            
            for f in files:
                if f.endswith('.ts'):
                    src_file = Path(root) / f
                    dst_file = dst_root / f.replace('.ts', ext)
                    
                    try:
                        with open(src_file, 'r', encoding='utf-8') as fh:
                            ts_code = fh.read()
                        
                        converted = converter(ts_code)
                        
                        with open(dst_file, 'w', encoding='utf-8') as fh:
                            fh.write(converted)
                        
                        count += 1
                    except Exception as e:
                        errors += 1
                        print(f"Error: {lang}/{f}: {e}")
        
        print(f"{lang}: generated {count} files, {errors} errors")
    
    print("\nDone!")


if __name__ == '__main__':
    main()
