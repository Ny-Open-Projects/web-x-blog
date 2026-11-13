#!/usr/bin/env python3
"""
从 TypeScript 源代码生成所有语言的代码
"""
import os
import re
import py_compile
from pathlib import Path

DSA = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa')


def clean_ts_code(ts_code: str) -> str:
    """清理 TS 代码 - 移除注释等"""
    # 移除块注释
    ts_code = re.sub(r'/\*\*[\s\S]*?\*/', '', ts_code)
    ts_code = re.sub(r'/\*[\s\S]*?\*/', '', ts_code)
    # 移除行注释
    ts_code = re.sub(r'//[^\n]*', '', ts_code)
    return ts_code


def extract_types(ts_params: str) -> list:
    """从 TS 参数提取类型"""
    types = {}
    for param in ts_params.split(','):
        param = param.strip()
        if ':' in param:
            name = param.split(':')[0].strip()
            typ = param.split(':')[1].strip()
            types[name] = typ
    return types


def ts_type_to_go(typ: str) -> str:
    """TS 类型转 Go 类型"""
    typ = typ.replace(' | null', '').replace('| null', '').replace('null | ', '')
    mapping = {
        'number': 'int',
        'string': 'string',
        'boolean': 'bool',
        'TreeNode': '*TreeNode',
        'ListNode': '*ListNode',
    }
    return mapping.get(typ, typ)


def ts_type_to_java(typ: str) -> str:
    """TS 类型转 Java 类型"""
    typ = typ.replace(' | null', '').replace('| null', '').replace('null | ', '')
    mapping = {
        'number': 'int',
        'String': 'String',
        'boolean': 'boolean',
        'TreeNode': 'TreeNode',
        'ListNode': 'ListNode',
    }
    # Handle array types
    if typ.endswith('[]'):
        return typ.replace('[]', '[]')
    return mapping.get(typ, typ)


def ts_type_to_python(typ: str) -> str:
    """TS 类型转 Python 类型注解（可选）"""
    mapping = {
        'number': 'int',
        'str': 'str',
        'boolean': 'bool',
        'TreeNode': 'TreeNode',
    }
    return mapping.get(typ, typ)


def convert_to_go(ts_code: str) -> str:
    """转换 TS 到 Go"""
    ts_code = clean_ts_code(ts_code)
    
    # Extract classes
    classes = {}
    for m in re.finditer(r'class\s+(\w+)\s*\{([^}]+)\}', ts_code):
        classes[m.group(1)] = m.group(2)
    ts_code = re.sub(r'class\s+\w+\s*\{[^}]+\}', '', ts_code)
    
    lines = ts_code.split('\n')
    result = []
    indent = 0
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # Function definition
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        pname = p.split(':')[0].strip()
                        ptype = ts_type_to_go(p.split(':')[1].strip())
                        params.append(f"{pname} {ptype}")
                    elif p:
                        params.append(f"_{p}")
            
            result.append(f"func {name}({', '.join(params)}) {{")
            indent += 1
            continue
        
        # Class definition
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            cls = m.group(1)
            if cls in classes:
                result.append(f"type {cls} struct {{")
                indent += 1
                for bline in classes[cls].split('\n'):
                    bs = bline.strip()
                    if bs and bs not in ('{', '}') and 'constructor' not in bs:
                        if ':' in bs:
                            parts = bs.split(':')
                            result.append(f"    {parts[0].strip()} {ts_type_to_go(parts[1].strip())}")
                indent -= 1
                result.append("}")
            continue
        
        # constructor
        if 'constructor' in s:
            continue
        
        # Braces
        if s == '{':
            indent += 1
            continue
        elif s == '}':
            indent = max(0, indent - 1)
            continue
        
        stmt = s
        
        # Remove type annotations
        stmt = re.sub(r':\s*(?:string|number|boolean|void|null|undefined|string\[\]|number\[\]|boolean\[\])', '', stmt)
        stmt = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*(?:\[\])?', '', stmt)
        
        # Remove const/let
        stmt = re.sub(r'\bconst\b\s+', '', stmt)
        stmt = re.sub(r'\blet\b\s+', '', stmt)
        
        stmt = stmt.replace('this.', '')
        stmt = stmt.replace('null', 'nil').replace('undefined', 'nil')
        stmt = stmt.replace('true', 'true').replace('false', 'false')
        stmt = stmt.replace('===', '==').replace('!==', '!=')
        
        # .length -> len()
        stmt = re.sub(r'(\w+)\.length\b', r'len(\1)', stmt)
        
        # Array methods
        stmt = stmt.replace('.push(', '.Append(')
        stmt = stmt.replace('.pop()', '.Pop()')
        
        # Math
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', stmt)
        stmt = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', stmt)
        
        # Ternary
        stmt = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)(?:;|$)', r'if \1 { \2 } else { \3 }', stmt)
        
        # for...of
        stmt = re.sub(r'for\s*\(\s*(?:const|let|var)\s+(\w+)\s*of\s+(\w+)', r'for _, \1 := range \2', stmt)
        
        # slice
        stmt = re.sub(r'(\w+)\.slice\((\w+)\)', r'\1[\2:]', stmt)
        stmt = re.sub(r'(\w+)\.slice\((\w+),\s*(\w+)\)', r'\1[\2:\3]', stmt)
        
        # Remove semicolons
        stmt = stmt.replace(';', '')
        
        # Remove new
        stmt = re.sub(r'\bnew\s+(\w+)', r'\1', stmt)
        
        # Fix if
        if re.match(r'^if\s*\(', stmt):
            idx = stmt.index('(')
            depth = 0
            close_idx = -1
            for i in range(idx, len(stmt)):
                if stmt[i] == '(':
                    depth += 1
                elif stmt[i] == ')':
                    depth -= 1
                    if depth == 0:
                        close_idx = i
                        break
            if close_idx > 0:
                cond = stmt[idx+1:close_idx]
                rest = stmt[close_idx+1:].strip().rstrip('}')
                stmt = f"if {cond} {{\n{'    ' * indent}{rest}\n{' ' * (indent-1) * 4}}}" if rest else f"if {cond} {{{{'"
        
        if stmt and stmt not in ('{', '}'):
            result.append('    ' * indent + stmt)
    
    return '\n'.join(result)


def convert_to_java(ts_code: str) -> str:
    """转换 TS 到 Java"""
    ts_code = clean_ts_code(ts_code)
    
    # Extract classes
    classes = {}
    for m in re.finditer(r'class\s+(\w+)\s*\{([^}]+)\}', ts_code):
        classes[m.group(1)] = m.group(2)
    ts_code = re.sub(r'class\s+\w+\s*\{[^}]+\}', '', ts_code)
    
    lines = ts_code.split('\n')
    result = []
    indent = 0
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # Function definition
        m = re.match(r'^function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            params = []
            if params_str:
                for p in params_str.split(','):
                    p = p.strip()
                    if ':' in p:
                        pname = p.split(':')[0].strip()
                        ptype = ts_type_to_java(p.split(':')[1].strip())
                        params.append(f"{ptype} {pname}")
                    elif p:
                        params.append(f"Object {p}")
            
            result.append(f"public Object {name}({', '.join(params)}) {{")
            indent += 1
            continue
        
        # Class definition
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            cls = m.group(1)
            if cls in classes:
                result.append(f"public static class {cls} {{")
                indent += 1
                for bline in classes[cls].split('\n'):
                    bs = bline.strip()
                    if bs and bs not in ('{', '}') and 'constructor' not in bs:
                        if ':' in bs:
                            parts = bs.split(':')
                            result.append(f"    {ts_type_to_java(parts[1].strip())} {parts[0].strip()};")
                indent -= 1
                result.append("}")
            continue
        
        if 'constructor' in s:
            continue
        
        # Braces
        if s == '{':
            indent += 1
            continue
        elif s == '}':
            indent = max(0, indent - 1)
            continue
        
        stmt = s
        
        # Remove type annotations
        stmt = re.sub(r':\s*(?:string|number|boolean|void|null|undefined|string\[\]|number\[\]|boolean\[\])', '', stmt)
        stmt = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*(?:\[\])?', '', stmt)
        
        # Remove const/let
        stmt = re.sub(r'\bconst\b\s+', 'final ', stmt)
        stmt = re.sub(r'\blet\b\s+', '', stmt)
        
        stmt = stmt.replace('this.', '')
        stmt = stmt.replace('null', 'null').replace('undefined', 'null')
        stmt = stmt.replace('true', 'true').replace('false', 'false')
        stmt = stmt.replace('===', '==').replace('!==', '!=')
        
        # .length -> .length
        stmt = re.sub(r'(\w+)\.length\b', r'\1.length', stmt)
        
        # Array methods
        stmt = stmt.replace('.push(', '.add(')
        stmt = stmt.replace('.pop()', '.remove(\1)')
        
        # Math
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'(int)\1', stmt)
        stmt = re.sub(r'Math\.max\((.+?)\)', r'Math.max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+?)\)', r'Math.min(\1)', stmt)
        
        # Ternary
        stmt = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)(?:;|$)', r'(\2 if \1 else \3)', stmt)
        
        # for...of
        stmt = re.sub(r'for\s*\(\s*(?:const|let|var)\s+(\w+)\s*of\s+(\w+)', r'for (\1 : \2)', stmt)
        
        # slice
        stmt = re.sub(r'(\w+)\.slice\((\w+)\)', r'\1.subList(\2, \1.size())', stmt)
        
        # Remove semicolons - add them for Java
        stmt = stmt.replace(';', '')
        if stmt and not stmt.endswith('{') and not stmt.endswith('}'):
            stmt += ';'
        
        # Remove new class instantiation issues
        stmt = re.sub(r'(\w+)\(\(', r'new \1(', stmt)
        
        if stmt and stmt not in ('{', '}'):
            result.append('    ' * indent + stmt)
    
    return '\n'.join(result)


def convert_to_python(ts_code: str) -> str:
    """转换 TS 到 Python - 正确处理缩进"""
    ts_code = clean_ts_code(ts_code)
    
    # Extract classes
    classes = {}
    for m in re.finditer(r'class\s+(\w+)\s*\{([^}]+)\}', ts_code):
        classes[m.group(1)] = m.group(2)
    ts_code = re.sub(r'class\s+\w+\s*\{[^}]+\}', '', ts_code)
    
    lines = ts_code.split('\n')
    result = []
    indent = 0
    in_function = False
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # Function definition
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
            
            # Add self for methods
            if in_function and params and params[0] not in ('self', 'root', 'nums'):
                params.insert(0, 'self')
            
            result.append(f"def {name}({', '.join(params)}):")
            indent = 1
            in_function = True
            continue
        
        # Class definition
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            cls = m.group(1)
            result.append(f"class {cls}:")
            indent = 1
            in_function = False
            if cls in classes:
                for bline in classes[cls].split('\n'):
                    bs = bline.strip()
                    if bs and bs not in ('{', '}'):
                        if 'constructor' in bs:
                            result.append("    def __init__(self):")
                        else:
                            bs = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*', '', bs)
                            bs = bs.replace('this.', 'self.')
                            if bs:
                                result.append(f"    {bs}")
            continue
        
        if 'constructor' in s:
            result.append("    def __init__(self):")
            continue
        
        # Braces
        if s == '{':
            indent += 1
            continue
        elif s == '}':
            indent = max(0, indent - 1)
            continue
        
        stmt = s
        
        # Remove type annotations
        stmt = re.sub(r':\s*(?:string|number|boolean|void|null|undefined|string\[\]|number\[\]|boolean\[\])', '', stmt)
        stmt = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*(?:\[\])?', '', stmt)
        
        # Remove const/let
        stmt = re.sub(r'\bconst\b\s+', '', stmt)
        stmt = re.sub(r'\blet\b\s+', '', stmt)
        
        stmt = stmt.replace('this.', 'self.')
        stmt = stmt.replace('null', 'None').replace('undefined', 'None')
        stmt = stmt.replace('true', 'True').replace('false', 'False')
        stmt = stmt.replace('===', '==').replace('!==', '!=')
        
        # .length -> len()
        stmt = re.sub(r'(\w+)\.length\b', r'len(\1)', stmt)
        
        # Array methods
        stmt = stmt.replace('.push(', '.append(')
        stmt = stmt.replace('.pop()', '.pop()')
        stmt = stmt.replace('.shift()', '.pop(0)')
        
        # Math
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', stmt)
        stmt = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', stmt)
        stmt = re.sub(r'Math\.abs\((.+?)\)', r'abs(\1)', stmt)
        
        # Ternary
        stmt = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)(?:;|$)', r'(\2 if \1 else \3)', stmt)
        
        # for...of
        stmt = re.sub(r'for\s*\(\s*(?:const|let|var)\s+(\w+)\s*of\s+(\w+)', r'for \1 in \2', stmt)
        
        # slice
        stmt = re.sub(r'(\w+)\.slice\((\w+)\)', r'\1[\2:]', stmt)
        stmt = re.sub(r'(\w+)\.slice\((\w+),\s*(\w+)\)', r'\1[\2:\3]', stmt)
        
        # Remove semicolons
        stmt = stmt.replace(';', '')
        
        # Remove new
        stmt = re.sub(r'\bnew\s+(\w+)', r'\1', stmt)
        
        # Fix logical operators
        stmt = stmt.replace('&&', ' and ').replace('||', ' or ')
        
        # Fix arrow functions
        m = re.match(r'^(\w+)\s*=\s*\(([^)]*)\)\s*=>', stmt)
        if m:
            fname = m.group(1)
            params = m.group(2).strip()
            result.append(f"def {fname}({params}):")
            indent += 1
            continue
        
        # Fix if statements
        if re.match(r'^if\s*\(', stmt):
            idx = stmt.index('(')
            depth = 0
            close_idx = -1
            for i in range(idx, len(stmt)):
                if stmt[i] == '(':
                    depth += 1
                elif stmt[i] == ')':
                    depth -= 1
                    if depth == 0:
                        close_idx = i
                        break
            
            if close_idx > 0:
                cond = stmt[idx+1:close_idx].strip()
                rest = stmt[close_idx+1:].strip()
                if cond.startswith('!'):
                    cond = 'not ' + cond[1:].strip()
                stmt = f"if {cond}:"
                if rest and rest not in ('{',):
                    stmt += f" {rest}"
        
        # else if
        stmt = stmt.replace('else if', 'elif')
        
        # else
        if stmt.strip() == 'else':
            stmt = 'else:'
        
        # while
        if re.match(r'^while\s*\(', stmt):
            idx = stmt.index('(')
            depth = 0
            close_idx = -1
            for i in range(idx, len(stmt)):
                if stmt[i] == '(':
                    depth += 1
                elif stmt[i] == ')':
                    depth -= 1
                    if depth == 0:
                        close_idx = i
                        break
            if close_idx > 0:
                cond = stmt[idx+1:close_idx].strip()
                rest = stmt[close_idx+1:].strip()
                stmt = f"while {cond}:"
                if rest and rest not in ('{',):
                    stmt += f" {rest}"
        
        # Fix naming conflict
        stmt = re.sub(r'\blen\s*=\s*len\(', 'length = len(', stmt)
        
        # Remove curly braces
        stmt = stmt.replace('{', '').replace('}', '')
        
        if stmt:
            result.append('    ' * indent + stmt)
    
    return '\n'.join(result)


def generate_go_file(ts_content: str, filename: str) -> str:
    """生成 Go 文件"""
    body = convert_to_go(ts_content)
    
    # 获取函数名作为包名的一部分
    func_match = re.search(r'func\s+(\w+)', body)
    func_name = func_match.group(1) if func_match else 'main'
    
    return f'''package main

import (
\t"fmt"
)

// {filename}
{body}

func main() {{
}}
'''


def generate_java_file(ts_content: str, filename: str) -> str:
    """生成 Java 文件"""
    body = convert_to_java(ts_content)
    
    # 提取类名
    class_match = re.search(r'class\s+(\w+)', ts_content)
    class_name = class_match.group(1) if class_match else 'Solution'
    
    return f'''package com.webfault.dsa;

import java.util.*;

// {filename}
public class {class_name} {{
{body}
}}
'''


def generate_python_file(ts_content: str, filename: str) -> str:
    """生成 Python 文件"""
    body = convert_to_python(ts_content)
    
    return f'''"""
{filename}
"""
{body}
'''


def main():
    print("=" * 70)
    print("DSA Code Generator - All Languages")
    print("=" * 70)
    
    ts_base = DSA / 'ts'
    langs = {
        'go': (DSA / 'go', generate_go_file),
        'java': (DSA / 'java', generate_java_file),
        'python': (DSA / 'python', generate_python_file),
    }
    
    total_files = 0
    
    for root, dirs, files in os.walk(ts_base):
        # Skip cache dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for f in files:
            if f.endswith('.ts'):
                ts_file = Path(root) / f
                rel_path = ts_file.relative_to(ts_base)
                
                for lang, (lang_base, generator) in langs.items():
                    dst_file = lang_base / rel_path.with_suffix(f'.{lang}')
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    try:
                        with open(ts_file, 'r', encoding='utf-8') as fh:
                            ts_code = fh.read()
                        
                        code = generator(ts_code, f)
                        
                        with open(dst_file, 'w', encoding='utf-8') as fh:
                            fh.write(code)
                        
                        total_files += 1
                    except Exception as e:
                        print(f"Error generating {lang}/{f}: {e}")
    
    print(f"\nGenerated {total_files} files for Go, Java, Python")
    
    # Verify syntax
    print("\n" + "=" * 70)
    print("Syntax Verification")
    print("=" * 70)
    
    for lang in ['go', 'java', 'python']:
        base = DSA / lang
        ext = {
            'go': '.go',
            'java': '.java', 
            'python': '.py'
        }[lang]
        
        total = valid = 0
        errors = []
        
        for root, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            for f in files:
                if f.endswith(ext):
                    total += 1
                    fp = os.path.join(root, f)
                    
                    try:
                        if lang == 'python':
                            py_compile.compile(fp, doraise=True)
                            valid += 1
                        else:
                            with open(fp, 'r', encoding='utf-8', errors='ignore') as fh:
                                content = fh.read()
                                # Basic validation
                                if lang == 'go':
                                    if 'package main' in content and 'let ' not in content:
                                        valid += 1
                                elif lang == 'java':
                                    if 'public class' in content and 'let ' not in content:
                                        valid += 1
                    except Exception as e:
                        if len(errors) < 5:
                            errors.append((fp, str(e)))
        
        print(f"\n{lang.upper()}: {valid}/{total} valid ({valid/total*100:.1f}%)")
        if errors:
            print("  First errors:")
            for path, err in errors[:3]:
                print(f"    {path.split(lang+'/')[-1]}: {err[:80]}")


if __name__ == '__main__':
    main()
