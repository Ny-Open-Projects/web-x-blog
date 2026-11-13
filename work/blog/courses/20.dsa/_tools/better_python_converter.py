#!/usr/bin/env python3
"""
更好的 TS → Python 转换器
"""
import re
from pathlib import Path

DSA_DIR = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa')


def clean_ts_code(code: str) -> str:
    """清理 TypeScript 代码"""
    # 移除注释
    code = re.sub(r'/\*\*[\s\S]*?\*/', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    code = re.sub(r'//[^\n]*', '', code)
    return code


def convert_to_python(ts_code: str) -> str:
    """TS → Python 转换"""
    ts_code = clean_ts_code(ts_code)
    
    # 提取类定义
    classes = {}
    class_pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(class_pattern, ts_code):
        classes[m.group(1)] = m.group(2)
    ts_code = re.sub(class_pattern, '', ts_code)
    
    lines = ts_code.split('\n')
    result = []
    indent = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        i += 1
        
        if not s:
            continue
        
        # 函数定义（处理箭头函数）
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
        
        # 箭头函数转换为普通函数
        m = re.match(r'const\s+(\w+)\s*=\s*\(([^)]*)\)\s*=>', s)
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
            class_name = m.group(1)
            result.append(f"class {class_name}:")
            indent = 1
            # 添加类体
            if class_name in classes:
                for body_line in classes[class_name].split('\n'):
                    body_s = body_line.strip()
                    if body_s and body_s != '{' and body_s != '}':
                        if 'constructor' in body_s:
                            result.append("    def __init__(self):")
                        else:
                            body_s = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*', '', body_s)
                            body_s = body_s.replace('this.', '')
                            if body_s:
                                result.append(f"    {body_s}")
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
        
        # 移除 new
        stmt = re.sub(r'\bnew\s+(\w+)', r'\1', stmt)
        
        if stmt:
            result.append('    ' * indent + stmt)
    
    return '\n'.join(result)


def main():
    print("=== Better Python Converter ===\n")
    
    ts_base = DSA_DIR / 'ts'
    count = 0
    errors = 0
    
    for root, dirs, files in os.walk(ts_base):
        dst_root = DSA_DIR / 'python' / Path(root).relative_to(ts_base)
        if not dst_root.exists():
            dst_root.mkdir(parents=True, exist_ok=True)
        
        for f in files:
            if f.endswith('.ts'):
                src_file = Path(root) / f
                dst_file = dst_root / f.replace('.ts', '.py')
                
                try:
                    with open(src_file, 'r', encoding='utf-8') as fh:
                        ts_code = fh.read()
                    
                    python_code = convert_to_python(ts_code)
                    
                    with open(dst_file, 'w', encoding='utf-8') as fh:
                        fh.write(python_code)
                    
                    count += 1
                except Exception as e:
                    errors += 1
                    print(f"Error: {f}: {e}")
    
    print(f"Generated {count} Python files, {errors} errors")
    
    # Verify
    import py_compile
    valid = 0
    error_list = []
    for root, dirs, files in os.walk(DSA_DIR / 'python'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for f in files:
            if f.endswith('.py'):
                filepath = os.path.join(root, f)
                try:
                    py_compile.compile(filepath, doraise=True)
                    valid += 1
                except py_compile.PyCompileError as e:
                    error_list.append((filepath, str(e)))
    
    print(f"Python syntax check: {valid} valid, {len(error_list)} errors")
    if error_list[:5]:
        print("\nFirst 5 errors:")
        for path, err in error_list[:5]:
            print(f"  {path.split('python/')[-1]}: {err[:100]}")


if __name__ == '__main__':
    import os
    main()
