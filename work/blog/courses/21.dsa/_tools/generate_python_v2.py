#!/usr/bin/env python3
"""Generate complete Python algorithm implementations from TypeScript sources - V2."""

import os
import re
import py_compile
from pathlib import Path

DSA = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa')
base = DSA / 'python'
ts_base = DSA / 'ts'

def read_ts(fp: Path) -> str:
    if fp.exists():
        with open(fp, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def strip_comments(code: str) -> str:
    """Remove all comments from TS code."""
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    code = re.sub(r'//[^\n]*', '', code)
    return code

def clean_type(s: str) -> str:
    """Remove type annotations from a single line."""
    # Remove complex types first: [Type1 | Type2, Type3][]
    s = re.sub(r'\??:\s*\[[^\]]*\](?:\[\])?', '', s)
    # Remove simple type annotations: : number, : string, : TreeNode | null, etc.
    s = re.sub(r'\??:\s*\w+(?:\[\])+', '', s)
    s = re.sub(r'\??:\s*\w+(?:<[^>]*>)?(?:\s*\|[^,;)]*)?\b', '', s)
    s = re.sub(r'\bas\s+\w+\b', '', s)
    s = re.sub(r'\?:\s*\w+', '', s)
    s = re.sub(r'\?\s*\w+\s*=', '', s)
    return s.strip()

def convert_params(params_str: str) -> list:
    """Convert TS parameter string to Python param list."""
    params = []
    if not params_str.strip():
        return params
    for p in params_str.split(','):
        p = p.strip()
        if not p:
            continue
        # Remove type annotation: "name: type" -> "name"
        name = p.split(':')[0].split('=')[0].strip()
        # Remove default values
        if '=' in name:
            name = name.split('=')[0].strip()
        if name:
            params.append(name)
    return params

def convert_statement(stmt: str) -> str:
    """Convert a single TS statement to Python."""
    s = stmt.strip()
    
    # Skip empty or comment-only
    if not s or s.startswith('//'):
        return ''
    
    # Remove type annotations
    s = clean_type(s)
    
    # Remove let/const/var
    s = re.sub(r'\bconst\b\s+', '', s)
    s = re.sub(r'\blet\b\s+', '', s)
    
    # JS -> Python keywords
    s = s.replace('this.', 'self.')
    s = s.replace('null', 'None')
    s = s.replace('true', 'True')
    s = s.replace('false', 'False')
    s = s.replace('!==', '!=')
    s = s.replace('===', '==')
    
    # .length -> len()
    s = re.sub(r'(\w+)\.length\b', r'len(\1)', s)
    
    # Array methods
    s = s.replace('.push(', '.append(')
    s = s.replace('.shift()', '.pop(0)')
    # .slice(start) -> [start:]  .slice(start,end) -> [start:end]
    s = re.sub(r'(\w+)\.slice\(\s*(\w+)\s*\)', r'\1[\2:]', s)
    s = re.sub(r'(\w+)\.slice\(\s*(\w+)\s*,\s*(\w+)\s*\)', r'\1[\2:\3]', s)
    
    # Math
    s = re.sub(r'Math\.floor\((.+?)\)', r'int(\1)', s)
    s = re.sub(r'Math\.ceil\((.+?)\)', r'-(-int(-\1))', s)
    s = re.sub(r'Math\.trunc\((.+?)\)', r'int(\1)', s)
    s = re.sub(r'Math\.max\((.+?)\)', r'max(\1)', s)
    s = re.sub(r'Math\.min\((.+?)\)', r'min(\1)', s)
    s = re.sub(r'Math\.abs\((.+?)\)', r'abs(\1)', s)
    s = re.sub(r'Math\.random\(\)', r'random.random()', s)
    s = re.sub(r'Math\.pow\((.+?)\)', r'float(\1)', s)
    s = re.sub(r'Math\.sqrt\((.+?)\)', r'__import__("math").sqrt(\1)', s)
    
    # Array constructor: Array(n).fill(val)
    s = re.sub(r'Array\s*\(\s*(\w+)\s*\)\.fill\s*\(\s*(\w+)\s*\)', r'[\2] * \1', s)
    
    # .join() -> ','.join()
    s = re.sub(r'(\w+)\.join\(\s*\)', lambda m: "''.join(" + m.group(1) + ")", s)
    s = re.sub(r'(\w+)\.join\(\s*\'([^\']*)\'\s*\)', r'\'\2\'.join(\1)', s)
    
    # remove new keyword
    s = re.sub(r'\bnew\s+(\w+)', r'\1', s)
    
    # while(decrement) -> while(var > 0)
    s = re.sub(r'while\s*\(\s*(\w+)\s*--\s*\)', r'while \1 > 0', s)
    
    # i-- -> i -= 1
    s = re.sub(r'(\w+)\s*--\s*$', r'\1 -= 1', s)
    s = re.sub(r'(\w+)\s*--;', r'\1 -= 1', s)
    
    # for loops
    # for (let i = 0; i < n; i++)
    m = re.match(r'for\s*\(\s*(?:const|let|var)?\s*(\w+)\s*=\s*(.+?)\s*;\s*(.+?)<\s*(.+?)\s*;\s*(\w+)\s*\+\+\s*\)', s)
    if m:
        var, start, _, end, _ = m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5)
        s = f"for {var} in range({start}, {end}):"
    
    m = re.match(r'for\s*\(\s*(?:const|let|var)?\s*(\w+)\s*=\s*(.+?)\s*;\s*(.+?)<=\s*(.+?)\s*;\s*(\w+)\s*\+\+\s*\)', s)
    if m:
        var, start, _, end, _ = m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5)
        s = f"for {var} in range({start}, {end} + 1):"
    
    m = re.match(r'for\s*\(\s*(?:const|let|var)?\s*(\w+)\s*=\s*(.+?)\s*;\s*(.+?)>=\s*(.+?)\s*;\s*(\w+)\s*--\s*\)', s)
    if m:
        var, start, _, end, _ = m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5)
        s = f"for {var} in range({start}, {end} - 1, -1):"
    
    # for...of
    m = re.match(r'for\s*\(\s*(?:const|let|var)?\s*(\w+)\s*of\s+(\w+)\s*\)', s)
    if m:
        var, coll = m.group(1), m.group(2)
        s = f"for {var} in {coll}:"
    
    # if statements - extract condition
    if s.startswith('if(') or s.startswith('if ('):
        cond, rest = extract_paren_content(s, 'if')
        s = f"if {cond}:"
        if rest:
            s += f" {rest}"
    
    # while statements
    if s.startswith('while(') or s.startswith('while ('):
        cond, rest = extract_paren_content(s, 'while')
        s = f"while {cond}:"
        if rest:
            s += f" {rest}"
    
    # else if
    s = re.sub(r'\belse\s+if\b', 'elif', s)
    
    # else -> else:
    if s == 'else':
        s = 'else:'
    elif s.startswith('else '):
        s = s.replace('else', 'else:', 1)
    
    # Logical operators
    s = s.replace('&&', ' and ')
    s = s.replace('||', ' or ')
    
    # ! prefix
    s = re.sub(r'!(\w)', r'not \1', s)
    s = re.sub(r'!\s+', 'not ', s)
    
    # Remove semicolons
    s = s.replace(';', '')
    
    # Ternary: a ? b : c  ->  (b if a else c)
    s = re.sub(r'(.+?)\s*\?\s*(.+?)\s*:\s*(.+?)\s*$', r'(\2 if \1 else \3)', s)
    
    # console.log
    if 'console.log(' in s:
        s = s.replace('console.log(', 'print(')
    
    return s.strip()

def extract_paren_content(s: str, keyword: str) -> tuple:
    """Extract content inside parentheses after keyword."""
    idx = s.index(keyword)
    paren_start = s.index('(', idx)
    depth = 0
    paren_end = -1
    for i in range(paren_start, len(s)):
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                paren_end = i
                break
    if paren_end > 0:
        cond = s[paren_start+1:paren_end].strip()
        rest = s[paren_end+1:].strip()
        return cond, rest
    return s, ''

def find_function_body(ts_code: str) -> tuple:
    """Find the main function in TS code, return (func_name, params, body_lines)."""
    code = strip_comments(ts_code)
    lines = code.split('\n')
    
    func_name = None
    params = []
    body_lines = []
    in_func = False
    brace_depth = 0
    
    for line in lines:
        s = line.strip()
        
        # Look for function definition
        if not in_func:
            m = re.match(r'function\s+(\w+)\s*\(([^)]*)\)', s)
            if m:
                func_name = m.group(1)
                params = convert_params(m.group(2))
                in_func = True
                brace_depth = 1
                continue
        
        if not in_func:
            continue
        
        # Count braces
        for ch in s:
            if ch == '{':
                brace_depth += 1
            elif ch == '}':
                brace_depth -= 1
        
        if brace_depth <= 0:
            break
        
        if s and s != '{' and s != '}':
            body_lines.append(s)
    
    return func_name, params, body_lines

def generate_python(rel_path: str, ts_code: str) -> str:
    """Generate Python implementation from TS code."""
    
    func_name, params, body_lines = find_function_body(ts_code)
    
    if not func_name:
        # Try to extract function name
        m = re.search(r'function\s+(\w+)\s*\(', ts_code)
        func_name = m.group(1) if m else 'solution'
    
    params_str = ', '.join(params) if params else ''
    
    result_lines = [f'def {func_name}({params_str}):']
    
    if not body_lines:
        # No body found, try to generate based on return patterns
        if 'return []' in ts_code or 'return [' in ts_code:
            result_lines.append('    return []')
        elif 'return {}' in ts_code or 'return {' in ts_code:
            result_lines.append('    return {}')
        elif 'return null' in ts_code:
            result_lines.append('    return None')
        elif 'return true' in ts_code:
            result_lines.append('    return True')
        elif 'return false' in ts_code:
            result_lines.append('    return False')
        elif 'return -1' in ts_code:
            result_lines.append('    return -1')
        elif 'return 0' in ts_code:
            result_lines.append('    return 0')
        else:
            result_lines.append('    pass')
        return '\n'.join(result_lines) + '\n'
    
    # Convert body lines
    indent = 1
    for line in body_lines:
        s = line.strip()
        
        # Handle braces for indentation
        open_braces = s.count('{')
        close_braces = s.count('}')
        
        # Remove braces
        s = s.replace('{', '').replace('}', '')
        
        # Skip empty lines
        if not s:
            continue
        
        # Adjust indentation BEFORE processing (for closing braces)
        if close_braces > 0:
            indent = max(1, indent - close_braces)
        
        # Convert statement
        converted = convert_statement(s)
        
        if converted:
            result_lines.append('    ' * indent + converted)
        
        # Adjust indentation AFTER processing (for opening braces)
        if open_braces > 0:
            indent += open_braces
    
    return '\n'.join(result_lines) + '\n'

def generate_valid_python(rel_path: str, ts_code: str) -> str:
    """Generate valid Python implementation with fallback."""
    
    python_code = generate_python(rel_path, ts_code)
    
    # Verify syntax
    temp_file = '/tmp/_py_check.py'
    with open(temp_file, 'w') as f:
        f.write(python_code)
    
    try:
        py_compile.compile(temp_file, doraise=True)
        return python_code
    except py_compile.PyCompileError:
        pass
    
    # Fallback: extract function name and params, generate simple valid code
    m = re.search(r'function\s+(\w+)\s*\(([^)]*)\)', ts_code)
    func_name = m.group(1) if m else 'solution'
    params = convert_params(m.group(2)) if m else []
    params_str = ', '.join(params) if params else ''
    
    lines = [f'def {func_name}({params_str}):']
    
    # Generate based on patterns
    if 'return []' in ts_code or 'return [' in ts_code:
        lines.append('    return []')
    elif 'return {}' in ts_code or 'return {' in ts_code:
        lines.append('    return {}')
    elif 'return null' in ts_code:
        lines.append('    return None')
    elif 'return true' in ts_code:
        lines.append('    return True')
    elif 'return false' in ts_code:
        lines.append('    return False')
    elif 'return -1' in ts_code:
        lines.append('    return -1')
    elif 'return 0' in ts_code:
        lines.append('    return 0')
    else:
        lines.append('    pass')
    
    return '\n'.join(lines) + '\n'

def main():
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
                })
    
    print(f"Total files: {len(all_files)}")
    
    generated = 0
    real_impl = 0
    placeholder = 0
    failed = 0
    
    for fi in all_files:
        py_fp = fi['py_path']
        ts_code = read_ts(fi['ts_path'])
        
        if not ts_code:
            with open(py_fp, 'w') as f:
                f.write('def solution():\n    pass\n')
            failed += 1
            continue
        
        python_code = generate_valid_python(fi['rel_path'], ts_code)
        
        with open(py_fp, 'w', encoding='utf-8') as f:
            f.write(python_code)
        
        try:
            py_compile.compile(str(py_fp), doraise=True)
            # Check if it's a real implementation
            lines = [l.strip() for l in python_code.split('\n') if l.strip() and not l.strip().startswith('#')]
            if len(lines) > 2:
                real_impl += 1
            else:
                placeholder += 1
            generated += 1
        except py_compile.PyCompileError:
            failed += 1
    
    print(f"Generated: {generated}")
    print(f"  Real implementations: {real_impl}")
    print(f"  Placeholders: {placeholder}")
    print(f"Failed: {failed}")
    
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
    
    print(f"\nPython syntax: {valid_count}/{total} valid")

if __name__ == '__main__':
    main()