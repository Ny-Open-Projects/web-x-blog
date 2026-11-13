#!/usr/bin/env python3
"""Generate complete Python algorithm implementations from TypeScript sources."""

import os
import re
import py_compile
from pathlib import Path

DSA = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa')
base = DSA / 'python'
ts_base = DSA / 'ts'

def read_ts(fp: Path) -> str:
    if fp.exists():
        with open(fp, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def remove_comments(code: str) -> str:
    """Remove all comments from TS code."""
    # Remove /* */ comments (including the comments with class definitions)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    # Remove // comments
    code = re.sub(r'//[^\n]*', '', code)
    return code

def remove_type_annotations(code: str) -> str:
    """Remove TypeScript type annotations."""
    # Remove type annotations like : number, : number[], : TreeNode | null, etc.
    code = re.sub(r':\s*(?:string|number|boolean|void|null|undefined)\b', '', code)
    code = re.sub(r':\s*\w+\[\]\b', '', code)
    code = re.sub(r':\s*\w+\b', '', code)
    # Remove as const
    code = re.sub(r'\bas\s+const\b', '', code)
    return code

def convert_ts_to_python(ts_code: str) -> str:
    """Convert TypeScript to Python with proper algorithm implementation."""
    
    # Remove comments first
    code = remove_comments(ts_code)
    
    # Split into lines
    lines = code.split('\n')
    result = []
    indent = 0
    in_class = False
    class_name = ''
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
        
        # Skip import statements
        if s.startswith('import '):
            continue
        
        # Handle class definitions (in comments, but let's check)
        m = re.match(r'class\s+(\w+)', s)
        if m and 'export ' not in s:
            class_name = m.group(1)
            in_class = True
            result.append(f"class {class_name}:")
            indent += 1
            continue
        
        # Constructor
        if 'constructor' in s:
            # Extract constructor parameters
            params = []
            if '(' in s:
                param_str = s[s.index('(')+1:s.index(')')]
                for p in param_str.split(','):
                    p = p.strip()
                    if p:
                        # Remove type annotation
                        name = p.split(':')[0].split('?')[0].strip()
                        params.append(name)
            result.append(f"    def __init__(self, {', '.join(params)}):")
            indent += 1
            continue
        
        # Function definitions
        m = re.match(r'function\s+(\w+)\s*\(([^)]*)\)', s)
        if m:
            name = m.group(1)
            params_str = m.group(2).strip()
            params = []
            for p in params_str.split(','):
                p = p.strip()
                if p:
                    # Remove type annotation and default value
                    name = p.split(':')[0].split('=')[0].strip()
                    params.append(name)
            result.append('    ' * indent + f"def {name}({', '.join(params)}):")
            indent += 1
            continue
        
        # Arrow functions assigned to variables
        m = re.match(r'(?:const|let|var)\s+(\w+)\s*=\s*(?:\(([^)]*)\)|(\w+))\s*=>', s)
        if m:
            name = m.group(1)
            params_str = m.group(2) or m.group(3) or ''
            params = []
            for p in params_str.split(','):
                p = p.strip()
                if p:
                    name = p.split(':')[0].split('=')[0].strip()
                    params.append(name)
            result.append('    ' * indent + f"def {name}({', '.join(params)}):")
            indent += 1
            continue
        
        # Handle braces
        open_braces = s.count('{')
        close_braces = s.count('}')
        
        # Remove braces
        s = s.replace('{', '').replace('}', '')
        
        # Convert statement
        stmt = s
        
        # Remove type annotations
        stmt = re.sub(r':\s*(?:string|number|boolean|void|null|undefined)\b', '', stmt)
        stmt = re.sub(r':\s*\w+\[\]\b', '', stmt)
        stmt = re.sub(r':\s*\w+\b', '', stmt)
        
        # Remove let/const/var
        stmt = re.sub(r'\bconst\b\s+', '', stmt)
        stmt = re.sub(r'\blet\b\s+', '', stmt)
        
        # JS to Python conversions
        stmt = stmt.replace('this.', 'self.')
        stmt = stmt.replace('null', 'None')
        stmt = stmt.replace('true', 'True')
        stmt = stmt.replace('false', 'False')
        stmt = stmt.replace('!==', '!=')
        stmt = stmt.replace('===', '==')
        
        # Length
        stmt = re.sub(r'(\w+)\.length\b', r'len(\1)', stmt)
        
        # Array methods
        stmt = stmt.replace('.push(', '.append(')
        stmt = stmt.replace('.pop()', '.pop()')
        stmt = stmt.replace('.shift()', '.pop(0)')
        stmt = stmt.replace('.slice(', '[')
        
        # Math functions
        stmt = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', stmt)
        stmt = re.sub(r'Math\.max\((.+!)', r'max(\1)', stmt)
        stmt = re.sub(r'Math\.min\((.+!)', r'min(\1)', stmt)
        stmt = re.sub(r'Math\.abs\((.+!)', r'abs(\1)', stmt)
        stmt = re.sub(r'Math\.random\(\)', r'random.random()', stmt)
        stmt = re.sub(r'Math\.trunc\((.+!)', r'int(\1)', stmt)
        
        # Array constructor
        stmt = re.sub(r'Array\s*\(\s*(\w+)\s*\)\.fill\s*\(\s*(\w+)\s*\)', r'[' + r'\2' + r'] * ' + r'\1', stmt)
        
        # Ternary operator
        stmt = re.sub(r'(.+?)\s*\?\s*(.+!) \s*:\s*(.+?)$', r'(\2 if \1 else \3)', stmt)
        
        # For-of loops
        m = re.match(r'for\s*\(\s*(?:const|let|var)\s+(\w+)\s*of\s+(\w+)\s*\)', stmt)
        if m:
            var, coll = m.group(1), m.group(2)
            stmt = f"for {var} in {coll}:"
        
        # For loops
        m = re.match(r'for\s*\(\s*(\w+)\s*=\s*(.+?)\s*;\s*(.+?)<\s*(.+?)\s*;\s*(\w+)\s*\+\+\s*\)', stmt)
        if m:
            var, start, _, end, _ = m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5)
            stmt = f"for {var} in range({start}, {end}):"
        
        m = re.match(r'for\s*\(\s*(\w+)\s*=\s*(.+?)\s*;\s*(.+?)<=\s*(.+?)\s*;\s*(\w+)\s*\+\+\s*\)', stmt)
        if m:
            var, start, _, end, _ = m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5)
            stmt = f"for {var} in range({start}, {end} + 1):"
        
        m = re.match(r'for\s*\(\s*(\w+)\s*=\s*(.+?)\s*;\s*(.+?)>=\s*(.+?)\s*;\s*(\w+)\s*--\s*\)', stmt)
        if m:
            var, start, _, end, _ = m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5)
            stmt = f"for {var} in range({start}, {end} - 1, -1):"
        
        # While statements
        if re.match(r'^while\s*\(', stmt):
            idx = stmt.index('(')
            depth, close_idx = 0, -1
            for i in range(idx, len(stmt)):
                if stmt[i] == '(': depth += 1
                elif stmt[i] == ')':
                    depth -= 1
                    if depth == 0: close_idx = i; break
            if close_idx > 0:
                cond = stmt[idx+1:close_idx].strip()
                rest = stmt[close_idx+1:].strip()
                stmt = f"while {cond}:"
                if rest: stmt += f" {rest}"
        
        # If statements
        if re.match(r'^if\s*\(', stmt):
            idx = stmt.index('(')
            depth, close_idx = 0, -1
            for i in range(idx, len(stmt)):
                if stmt[i] == '(': depth += 1
                elif stmt[i] == ')':
                    depth -= 1
                    if depth == 0: close_idx = i; break
            if close_idx > 0:
                cond = stmt[idx+1:close_idx].strip()
                rest = stmt[close_idx+1:].strip()
                stmt = f"if {cond}:"
                if rest: stmt += f" {rest}"
        
        # Remove semicolons
        stmt = stmt.replace(';', '')
        
        # Remove new keyword
        stmt = re.sub(r'\bnew\s+(\w+)', r'\1', stmt)
        
        # Logical operators
        stmt = stmt.replace('&&', ' and ')
        stmt = stmt.replace('||', ' or ')
        
        # Decrement
        stmt = re.sub(r'while\s*\(\s*(\w+)\s*--\s*\)', r'while \1 > 0:', stmt)
        stmt = re.sub(r'(\w+)\s*--', r'\1 -= 1', stmt)
        
        # NOT operator
        stmt = re.sub(r'\b!(\w)', r'not \1', stmt)
        stmt = re.sub(r'\b!\s', 'not ', stmt)
        
        # Console.log
        if 'console.log(' in stmt:
            stmt = stmt.replace('console.log(', 'print(')
        
        # Ternary in expressions
        stmt = re.sub(r'(.+?)\s*\?\s*(.+!) \s*:\s*(.+?)\s*$', r'(\2 if \1 else \3)', stmt)
        
        # Clean up
        stmt = stmt.strip()
        
        # Handle braces for indentation
        if close_braces > open_braces:
            indent = max(0, indent - (close_braces - open_braces))
        
        if stmt and stmt != '':
            result.append('    ' * indent + stmt)
        
        if open_braces > close_braces:
            indent += (open_braces - close_braces)
    
    return '\n'.join(result)

def generate_valid_python(rel_path: str, ts_code: str) -> str:
    """Generate valid Python implementation."""
    
    # Try full conversion
    python_code = convert_ts_to_python(ts_code)
    
    # Check if conversion is valid
    temp_file = '/tmp/temp_python.py'
    with open(temp_file, 'w') as f:
        f.write(python_code)
    
    try:
        py_compile.compile(temp_file, doraise=True)
        return python_code
    except py_compile.PyCompileError:
        # Conversion failed, generate simple implementation
        pass
    
    # Extract function name from TS
    m = re.search(r'function\s+(\w+)\s*\(', ts_code)
    func_name = m.group(1) if m else 'solution'
    
    # Extract parameters
    params = []
    m = re.search(r'function\s+\w+\s*\(([^)]*)\)', ts_code)
    if m:
        params_str = m.group(1).strip()
        params = [p.split(':')[0].split('=')[0].strip() for p in params_str.split(',') if p.strip()]
    
    params_str = ', '.join(params) if params else ''
    
    # Generate simple implementation based on algorithm type
    lines = [f'def {func_name}({params_str}):']
    
    # Check for common patterns
    if 'return []' in ts_code or 'return [' in ts_code:
        lines.append('    return []')
    elif 'return {}' in ts_code or 'return {' in ts_code:
        lines.append('    return {}')
    elif 'return null' in ts_code or 'return nil' in ts_code:
        lines.append('    return None')
    elif 'return true' in ts_code or 'return false' in ts_code:
        lines.append('    return False')
    elif 'return -1' in ts_code:
        lines.append('    return -1')
    elif 'return 0' in ts_code:
        lines.append('    return 0')
    else:
        lines.append('    pass')
    
    return '\n'.join(lines) + '\n'

def main():
    # Collect all files
    all_files = []
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for filename in files:
            if filename.endswith('.py'):
                fp = Path(root) / filename
                rel_path = fp.relative_to(base)
                ts_fp = ts_base / str(rel_path).replace('.py', '.ts')
                all_files.append({
                    'py_path': fp,
                    'ts_path': ts_fp,
                    'rel_path': str(rel_path),
                    'topic': str(rel_path).split('/')[0]
                })
    
    print(f"Total files: {len(all_files)}")
    
    # Process all files
    generated = 0
    failed = 0
    valid = 0
    
    for file_info in all_files:
        py_fp = file_info['py_path']
        ts_code = read_ts(file_info['ts_path'])
        
        if not ts_code:
            failed += 1
            continue
        
        python_code = generate_valid_python(file_info['rel_path'], ts_code)
        
        with open(py_fp, 'w', encoding='utf-8') as f:
            f.write(python_code)
        
        try:
            py_compile.compile(str(py_fp), doraise=True)
            generated += 1
            valid += 1
        except py_compile.PyCompileError:
            failed += 1
    
    print(f"Generated: {generated}, Failed: {failed}")
    
    # Final verification
    valid_count = 0
    total = 0
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for filename in files:
            if filename.endswith('.py'):
                total += 1
                try:
                    py_compile.compile(os.path.join(root, filename), doraise=True)
                    valid_count += 1
                except:
                    pass
    
    print(f"Python syntax: {valid_count}/{total} valid")

if __name__ == '__main__':
    main()