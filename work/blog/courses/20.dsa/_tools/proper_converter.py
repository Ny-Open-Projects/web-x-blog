#!/usr/bin/env python3
"""
Proper TS → Python/Go/Java Converter
"""
import os
import re
from pathlib import Path

DSA_DIR = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa')


def remove_comments(code: str) -> str:
    """移除所有注释"""
    # 移除多行注释
    code = re.sub(r'/\*\*[\s\S]*?\*/', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    # 移除单行注释
    code = re.sub(r'//[^\n]*', '', code)
    return code


def extract_class_definitions(code: str) -> dict:
    """提取类定义"""
    classes = {}
    pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(pattern, code):
        classes[m.group(1)] = m.group(2)
    return classes


def convert_to_python(ts_code: str) -> str:
    """TS → Python"""
    ts_code = remove_comments(ts_code)
    
    # 提取并移除类定义
    classes = extract_class_definitions(ts_code)
    for class_name, body in classes.items():
        py_lines = [f"class {class_name}:"]
        for line in body.split('\n'):
            s = line.strip()
            if 'constructor' in s:
                py_lines.append("    def __init__(self):")
            elif s and s != '{' and s != '}':
                # 清理类型注解
                s = re.sub(r'\s*=\s*[^,}]+', '', s)
                s = s.replace('this.', '')
                if s:
                    py_lines.append(f"    {s}")
        ts_code = ts_code.replace(f'class {class_name} {{{body}}}', '\n'.join(py_lines))
    
    lines = ts_code.split('\n')
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
            params_str = m.group(2).strip()
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        params.append(p.split(':')[0].strip())
                    elif p:
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
        stmt = s
        
        # 移除类型注解
        stmt = re.sub(r':\s*(?:string|number|boolean|void|null|undefined|string\[\]|number\[\]|boolean\[\])', '', stmt)
        stmt = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*(?:\[\])?', '', stmt)
        stmt = re.sub(r'\?:\s*(?:string|number|boolean|void|null|undefined)', '', stmt)
        
        # 移除 const/let
        stmt = re.sub(r'\bconst\b\s*', '', stmt)
        stmt = re.sub(r'\blet\b\s*', '', stmt)
        
        # this. → 空
        stmt = stmt.replace('this.', '')
        
        # null/undefined → None
        stmt = stmt.replace('null', 'None').replace('undefined', 'None')
        
        # true/false → True/False
        stmt = stmt.replace('true', 'True').replace('false', 'False')
        
        # === / !== → == / !=
        stmt = stmt.replace('===', '==').replace('!==', '!=')
        
        # .length → len()
        stmt = re.sub(r'(\w+)\.length\b', r'len(\1)', stmt)
        
        # 数组方法
        stmt = stmt.replace('.push(', '.append(')
        stmt = stmt.replace('.pop()', '.pop()')
        stmt = stmt.replace('.shift()', '.pop(0)')
        
        # console.log → print
        stmt = stmt.replace('console.log(', 'print(')
        
        # Math
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', stmt)
        stmt = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', stmt)
        stmt = stmt.replace('Math.random()', 'random.random()')
        
        # 三元表达式
        stmt = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)(?:;|$)', r'(\2 if \1 else \3)', stmt)
        
        # for...of
        stmt = re.sub(r'for\s*\(\s*(?:const|let|var)\s+(\w+)\s*of\s+(\w+)', r'for \1 in \2', stmt)
        
        # new Map/Set
        stmt = stmt.replace('new Map()', 'dict()')
        stmt = stmt.replace('new Set()', 'set()')
        
        # slice
        stmt = re.sub(r'(\w+)\.slice\((\w+)\)', r'\1[\2:]', stmt)
        stmt = re.sub(r'(\w+)\.slice\((\w+),\s*(\w+)\)', r'\1[\2:\3]', stmt)
        
        # 移除分号
        stmt = stmt.replace(';', '')
        
        # 移除 !
        stmt = stmt.replace('!', '')
        
        if stmt:
            result.append('    ' * indent + stmt)
    
    return '\n'.join(result)


def convert_to_go(ts_code: str) -> str:
    """TS → Go"""
    ts_code = remove_comments(ts_code)
    
    lines = ts_code.split('\n')
    result = ['package main', '', 'import "fmt"', '']
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # 函数定义
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        pname, ptype = p.split(':', 1)
                        ptype = ptype.strip()
                        if ptype == 'number': ptype = 'int'
                        elif ptype == 'string': ptype = 'string'
                        elif ptype == 'boolean': ptype = 'bool'
                        elif ptype.endswith('[]'):
                            base = ptype[:-2]
                            if base == 'number': base = 'int'
                            ptype = f'[]{base}'
                        params.append(f"{pname.strip()} {ptype}")
                    elif p:
                        params.append(p)
            result.append(f"func {name}({', '.join(params)}) {{")
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
        stmt = s
        
        stmt = stmt.replace('this.', '')
        stmt = stmt.replace('null', 'nil').replace('undefined', 'nil')
        stmt = stmt.replace('===', '==').replace('!==', '!=')
        stmt = re.sub(r'(\w+)\.length\b', r'len(\1)', stmt)
        stmt = re.sub(r'(\w+)\.push\((.+?)\)', r'append(\1, \2)', stmt)
        stmt = re.sub(r'(\w+)\.pop\(\)', r'\1[len(\1)-1]', stmt)
        stmt = stmt.replace('console.log(', 'fmt.Println(')
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', stmt)
        stmt = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', stmt)
        stmt = re.sub(r'new\s+(\w+)', r'&\1{}', stmt)
        stmt = stmt.replace(';', '')
        
        if stmt:
            result.append('    ' + stmt)
    
    result.append('')
    result.append('func main() {}')
    return '\n'.join(result)


def convert_to_java(ts_code: str) -> str:
    """TS → Java"""
    ts_code = remove_comments(ts_code)
    
    lines = ts_code.split('\n')
    result = ['package com.webfault.dsa;', '', 'import java.util.*;', '']
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # 函数定义
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            params = []
            if params_str:
                for p in params_str.split(','):
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
                            ptype = f'{base}[]'
                        params.append(f"{ptype} {pname.strip()}")
                    elif p:
                        params.append(p)
            result.append(f'public void {name}({", ".join(params)}) {{')
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
        stmt = s
        
        stmt = stmt.replace('this.', '')
        stmt = stmt.replace('null', 'null').replace('undefined', 'null')
        stmt = stmt.replace('===', '==').replace('!==', '!=')
        stmt = re.sub(r'(\w+)\.length\b', r'\1.length', stmt)
        stmt = stmt.replace('.push(', '.add(')
        stmt = re.sub(r'(\w+)\.pop\(\)', r'\1.remove(\1.size()-1)', stmt)
        stmt = stmt.replace('console.log(', 'System.out.println(')
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'(int)(\1)', stmt)
        stmt = re.sub(r'Math\.max\((.+?)\)', r'Math.max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+?)\)', r'Math.min(\1)', stmt)
        stmt = re.sub(r'new\s+(\w+)', r'new \1()', stmt)
        stmt = stmt.replace(';', '')
        
        if stmt:
            result.append('    ' + stmt)
    
    return '\n'.join(stmt)


def main():
    print("=== Proper Language Converter ===\n")
    
    ts_base = DSA_DIR / 'ts'
    converters = {
        'python': ('.py', convert_to_python),
        'go': ('.go', convert_to_go),
        'java': ('.java', convert_to_java)
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
