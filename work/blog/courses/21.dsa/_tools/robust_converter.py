#!/usr/bin/env python3
"""
鲁棒的 TS → Python/Go/Java 转换器
"""
import os
import re
from pathlib import Path

DSA_DIR = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa')


def remove_ts_comments(code: str) -> str:
    """移除 TypeScript 注释"""
    # 移除多行注释
    code = re.sub(r'/\*\*[\s\S]*?\*/', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    # 移除单行注释（但保留代码中的 //）
    code = re.sub(r'//[^\n]*', '', code)
    return code


def ts_type_to_py(t: str) -> str:
    """TypeScript 类型 → Python"""
    mapping = {
        'number': '', 'string': '', 'boolean': '',
        'void': '', 'null': '', 'undefined': '',
        'number[]': '', 'string[]': '', 'boolean[]': ''
    }
    return mapping.get(t.strip(), '')


def ts_type_to_go(t: str) -> str:
    """TypeScript 类型 → Go"""
    mapping = {
        'number': 'int', 'string': 'string', 'boolean': 'bool',
        'void': '', 'null': '', 'undefined': '',
    }
    if t.strip().endswith('[]'):
        base = t.strip()[:-2]
        return mapping.get(base, base) + '[]'
    return mapping.get(t.strip(), t.strip())


def ts_type_to_java(t: str) -> str:
    """TypeScript 类型 → Java"""
    mapping = {
        'number': 'int', 'string': 'String', 'boolean': 'boolean',
        'void': 'void', 'null': '', 'undefined': '',
    }
    if t.strip().endswith('[]'):
        base = t.strip()[:-2]
        return mapping.get(base, base) + '[]'
    return mapping.get(t.strip(), t.strip())


def convert_to_python(ts_code: str) -> str:
    """TS → Python"""
    ts_code = remove_ts_comments(ts_code)
    
    # 提取类定义
    class_defs = {}
    class_pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(class_pattern, ts_code):
        class_name = m.group(1)
        class_body = m.group(2)
        class_defs[class_name] = class_body
    
    # 移除类定义块
    ts_code = re.sub(class_pattern, '', ts_code)
    
    lines = ts_code.split('\n')
    py_lines = []
    indent = 0
    in_function = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # 处理函数定义
        m = re.search(r'^function\s+(\w+)\s*\(([^)]*)\)\s*(?::\s*(\w+(?:\[\]|\|[^\)]+)?))?\s*$', stripped)
        if m:
            func_name = m.group(1)
            params_str = m.group(2).strip()
            
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        pname = p.split(':')[0].strip()
                        params.append(pname)
                    else:
                        params.append(p)
            
            py_lines.append(f"def {func_name}({', '.join(params)}):")
            indent = 1
            in_function = True
            continue
        
        # 处理大括号
        if stripped == '{':
            indent += 1
            continue
        elif stripped == '}':
            indent = max(0, indent - 1)
            in_function = False
            continue
        
        # 转换语句
        line = stripped
        
        # 移除类型注解
        line = re.sub(r':\s*\w+(?:\[\]|\|[^\)]+)?', '', line)
        line = re.sub(r'\s*:\s*\w+(\s*\|\s*\w+)*\s*$', '', line)
        
        # 处理 this.
        line = line.replace('this.', '')
        
        # 处理 null/undefined
        line = line.replace('null', 'None').replace('undefined', 'None')
        
        # 处理布尔值
        line = line.replace('true', 'True').replace('false', 'False')
        line = line.replace('===', '==').replace('!==', '!=')
        
        # 处理数组长度
        line = re.sub(r'(\w+)\.length\b', r'len(\1)', line)
        
        # 处理数组方法
        line = line.replace('.push(', '.append(')
        line = line.replace('.pop()', '.pop()')
        line = line.replace('.shift()', '.pop(0)')
        
        # 处理 console.log
        line = line.replace('console.log(', 'print(')
        
        # 处理 Math
        line = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', line)
        line = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', line)
        line = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', line)
        line = line.replace('Math.random()', 'random.random()')
        
        # 处理三元表达式
        line = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)(?:;|$)', r'(\2 if \1 else \3)', line)
        
        # 处理 for...of
        line = re.sub(r'for\s*\(\s*const\s+(\w+)\s*of\s+(\w+)', r'for \1 in \2', line)
        
        # 处理 new Map/Set
        line = line.replace('new Map()', 'dict()')
        line = line.replace('new Set()', 'set()')
        
        # 处理 slice
        line = re.sub(r'(\w+)\.slice\((\w+)\)', r'\1[\2:]', line)
        line = re.sub(r'(\w+)\.slice\((\w+),\s*(\w+)\)', r'\1[\2:\3]', line)
        
        # 处理 return
        if line.startswith('return'):
            py_lines.append('    ' * indent + line)
        elif line:
            py_lines.append('    ' * indent + line)
    
    return '\n'.join(py_lines)


def convert_to_go(ts_code: str) -> str:
    """TS → Go"""
    ts_code = remove_ts_comments(ts_code)
    
    # 提取类定义
    class_defs = {}
    class_pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(class_pattern, ts_code):
        class_name = m.group(1)
        class_body = m.group(2)
        class_defs[class_name] = class_body
    
    ts_code = re.sub(class_pattern, '', ts_code)
    
    lines = ts_code.split('\n')
    go_lines = ['package main', '', 'import "fmt"', '']
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # 处理函数定义
        m = re.search(r'^function\s+(\w+)\s*\(([^)]*)\)\s*(?::\s*(\w+(?:\[\]|\|[^\)]+)?))?\s*$', stripped)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            ret_type = m.group(3)
            
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        pname, ptype = p.split(':', 1)
                        params.append(f"{pname.strip()} {ts_type_to_go(ptype)}")
                    else:
                        params.append(p)
            
            ret = ''
            if ret_type and ret_type != 'void':
                ret = f" {ts_type_to_go(ret_type)}"
            
            go_lines.append(f"func {name}({', '.join(params)}){ret} {{")
            continue
        
        # 处理大括号
        if stripped == '{':
            continue
        elif stripped == '}':
            go_lines.append('}')
            continue
        
        # 转换语句
        line = stripped
        
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
            go_lines.append('    ' + line)
    
    go_lines.append('')
    go_lines.append('func main() {}')
    return '\n'.join(go_lines)


def convert_to_java(ts_code: str) -> str:
    """TS → Java"""
    ts_code = remove_ts_comments(ts_code)
    
    # 提取类定义
    class_defs = {}
    class_pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(class_pattern, ts_code):
        class_name = m.group(1)
        class_body = m.group(2)
        class_defs[class_name] = class_body
    
    ts_code = re.sub(class_pattern, '', ts_code)
    
    lines = ts_code.split('\n')
    java_lines = ['package com.webfault.dsa;', '', 'import java.util.*;', '']
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # 处理函数定义
        m = re.search(r'^function\s+(\w+)\s*\(([^)]*)\)\s*(?::\s*(\w+(?:\[\]|\|[^\)]+)?))?\s*$', stripped)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            ret_type = m.group(3)
            
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        pname, ptype = p.split(':', 1)
                        params.append(f"{ts_type_to_java(ptype.strip())} {pname.strip()}")
                    else:
                        params.append(p)
            
            ret = 'void'
            if ret_type and ret_type != 'void':
                ret = ts_type_to_java(ret_type)
            
            java_lines.append(f'public {ret} {name}({", ".join(params)}) {{')
            continue
        
        # 处理大括号
        if stripped == '{':
            continue
        elif stripped == '}':
            java_lines.append('}')
            continue
        
        # 转换语句
        line = stripped
        
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
            java_lines.append('    ' + line)
    
    return '\n'.join(java_lines)


def main():
    print("=== Robust Language Converter ===\n")
    
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
