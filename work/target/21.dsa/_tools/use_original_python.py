#!/usr/bin/env python3
"""
从博客原文提取 Python 代码，如果没有则使用 TS 转换
"""
import os
import sys
import re
from pathlib import Path

sys.path.insert(0, '/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools')
from csdn_parser import extract_blog

DSA_DIR = Path('/Users/Wang/Code/github/web-x-blog/work/target/21.dsa')
ARTICLES_DIR = DSA_DIR / '_meta' / 'articles'


def extract_python_from_blog(article_id: str) -> list:
    """从博客 HTML 提取 Python 代码"""
    article_file = ARTICLES_DIR / f"{article_id}.html"
    if not article_file.exists():
        return []
    
    with open(article_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    parsed = extract_blog(content)
    python_solutions = []
    
    for sol in parsed.get('solutions', []):
        if sol.get('lang') == 'python':
            python_solutions.append({
                'name': sol.get('name', '方案1'),
                'code': sol.get('code', '')
            })
    
    return python_solutions


def simple_ts_to_python(ts_code: str) -> str:
    """简单的 TS → Python 转换"""
    # 移除注释
    ts_code = re.sub(r'/\*\*[\s\S]*?\*/', '', ts_code)
    ts_code = re.sub(r'/\*[\s\S]*?\*/', '', ts_code)
    ts_code = re.sub(r'//[^\n]*', '', ts_code)
    
    # 提取类定义
    classes = {}
    class_pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(class_pattern, ts_code):
        classes[m.group(1)] = m.group(2)
    ts_code = re.sub(class_pattern, '', ts_code)
    
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
    print("=== Using Original Python Code from Blogs ===\n")
    
    # Read article URLs
    urls_file = DSA_DIR / '_meta' / 'all_urls.tsv'
    articles = []
    with open(urls_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('id\t'):
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                articles.append({'id': parts[0], 'title': parts[1], 'url': parts[2]})
    
    print(f"Total articles: {len(articles)}")
    
    # Track statistics
    stats = {
        'python_from_blog': 0,
        'python_from_ts': 0,
        'no_code': 0
    }
    
    # Process each article
    for article in articles:
        article_id = article['id']
        
        # Find article directory in Python
        python_base = DSA_DIR / 'python'
        ts_base = DSA_DIR / 'ts'
        
        # Find matching directory
        py_dir = None
        ts_dir = None
        
        for root, dirs, files in os.walk(python_base):
            for d in dirs:
                if d.startswith('lc_') and article_id in d:
                    py_dir = Path(root) / d
                    break
            if py_dir:
                break
        
        for root, dirs, files in os.walk(ts_base):
            for d in dirs:
                if d.startswith('lc_') and article_id in d:
                    ts_dir = Path(root) / d
                    break
            if ts_dir:
                break
        
        if not py_dir or not ts_dir:
            continue
        
        # Extract Python code from blog
        python_solutions = extract_python_from_blog(article_id)
        
        if python_solutions:
            # Use original Python code
            stats['python_from_blog'] += 1
            for i, sol in enumerate(python_solutions):
                # Find matching TS solution file
                for ts_file in ts_dir.glob('solution_*.ts'):
                    sol_num = f"solution_{i+1}_"
                    if sol_num in ts_file.name or (i == 0 and 'solution_1_' in ts_file.name):
                        # Write Python code
                        py_file = ts_dir / ts_file.name.replace('.ts', '.py')
                        with open(py_file, 'w', encoding='utf-8') as f:
                            f.write(sol['code'])
                        break
        else:
            # Convert from TS
            stats['python_from_ts'] += 1
            for ts_file in ts_dir.glob('solution_*.ts'):
                with open(ts_file, 'r', encoding='utf-8') as f:
                    ts_code = f.read()
                
                python_code = simple_ts_to_python(ts_code)
                
                py_file = ts_dir / ts_file.name.replace('.ts', '.py')
                with open(py_file, 'w', encoding='utf-8') as f:
                    f.write(python_code)
    
    print(f"\nResults:")
    print(f"  Python from blog: {stats['python_from_blog']}")
    print(f"  Python from TS: {stats['python_from_ts']}")
    
    # Verify Python syntax
    import py_compile
    valid = 0
    errors = []
    for root, dirs, files in os.walk(DSA_DIR / 'python'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for f in files:
            if f.endswith('.py'):
                filepath = os.path.join(root, f)
                try:
                    py_compile.compile(filepath, doraise=True)
                    valid += 1
                except py_compile.PyCompileError as e:
                    errors.append((filepath, str(e)))
    
    print(f"\nPython syntax check: {valid} valid, {len(errors)} errors")


if __name__ == '__main__':
    main()
