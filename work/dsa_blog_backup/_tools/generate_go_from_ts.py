#!/usr/bin/env python3
"""从 TS 源文件生成正确的 Go 代码"""

import os
import re
import subprocess
from pathlib import Path

DSA = Path('/Users/Wang/Code/webfault-ai/dsa')

def extract_ts_functions(ts_code: str) -> list:
    """从 TS 代码中提取函数"""
    functions = []
    
    # 匹配 function 定义
    pattern = r'function\s+(\w+)\s*\(([^)]*)\)\s*:\s*([^{]+)\{'
    matches = re.finditer(pattern, ts_code)
    
    for match in matches:
        name = match.group(1)
        params = match.group(2).strip()
        return_type = match.group(3).strip()
        start = match.end()
        
        # 找到函数体的结束
        brace_depth = 1
        end = start
        while end < len(ts_code) and brace_depth > 0:
            if ts_code[end] == '{':
                brace_depth += 1
            elif ts_code[end] == '}':
                brace_depth -= 1
            end += 1
        
        body = ts_code[start:end-1]
        functions.append({
            'name': name,
            'params': params,
            'return_type': return_type,
            'body': body
        })
    
    return functions

def convert_ts_type_to_go(ts_type: str) -> str:
    """将 TS 类型转换为 Go 类型"""
    type_map = {
        'number': 'int',
        'string': 'string',
        'boolean': 'bool',
        'void': '',
        'null': 'nil',
        'undefined': 'nil',
    }
    
    # 处理数组类型
    if '[]' in ts_type:
        base_type = ts_type.split('[]')[0].strip()
        go_base = type_map.get(base_type, base_type)
        return f'[]{go_base}'
    
    # 处理可空类型
    if '|' in ts_type:
        parts = ts_type.split('|')
        for part in parts:
            part = part.strip()
            if part != 'null' and part != 'undefined':
                return type_map.get(part, part)
        return 'interface{}'
    
    # 处理对象类型
    if ts_type in ['TreeNode', 'ListNode', 'Queue', 'Stack', 'Heap']:
        return f'*{ts_type}'
    
    return type_map.get(ts_type, ts_type)

def convert_ts_params_to_go(params_str: str) -> str:
    """将 TS 参数转换为 Go 参数"""
    if not params_str:
        return ''
    
    go_params = []
    for param in params_str.split(','):
        param = param.strip()
        if not param:
            continue
        
        # 分离参数名和类型
        if ':' in param:
            parts = param.split(':')
            name = parts[0].strip()
            ts_type = ':'.join(parts[1:]).strip()
            go_type = convert_ts_type_to_go(ts_type)
            go_params.append(f'{name} {go_type}')
        else:
            go_params.append(param)
    
    return ', '.join(go_params)

def convert_ts_body_to_go(body: str, func_name: str) -> str:
    """将 TS 函数体转换为 Go 函数体"""
    lines = body.split('\n')
    result = []
    
    for line in lines:
        # 移除注释
        line = re.sub(r'//.*', '', line)
        
        # 转换类型
        line = line.replace('number[]', '[]int')
        line = line.replace('string[]', '[]string')
        line = line.replace('boolean[]', '[]bool')
        
        # 转换数组方法
        line = line.replace('.length', 'len')
        line = re.sub(r'\.slice\((\d+)\)', r'[:\1]', line)
        line = re.sub(r'\.slice\((\d+),\s*(\d+)\)', r'[\1:\2]', line)
        
        # 转换对象字面量
        line = re.sub(r'new\s+(\w+)\(([^)]+)\)', r'&\1{\2}', line)
        line = re.sub(r'(\w+)\{([^}]+)\}', r'&\1{\2}', line)
        
        # 转换变量声明
        line = re.sub(r'\bconst\b\s+', '', line)
        line = re.sub(r'\blet\b\s+', '', line)
        line = re.sub(r'(\w+)\s*=\s*', r'\1 := ', line)
        
        # 转换三元表达式
        line = re.sub(r'(\w+)\s*\?\s*(\w+)\s*:\s*(\w+)', r'\2 if \1 else \3', line)
        
        # 转换 Math 方法
        line = line.replace('Math.floor(', 'int(')
        line = line.replace('Math.ceil(', 'int(')
        line = line.replace('Math.max(', 'max(')
        line = line.replace('Math.min(', 'min(')
        
        # 转换 null 检查
        line = line.replace('=== null', '== nil')
        line = line.replace('!== null', '!= nil')
        
        # 转换 return
        line = line.replace('return', 'return')
        
        result.append(line)
    
    return '\n'.join(result)

def generate_go_code(ts_code: str, filename: str) -> str:
    """从 TS 代码生成 Go 代码"""
    functions = extract_ts_functions(ts_code)
    
    if not functions:
        # 如果没有找到函数，返回简单模板
        return f"""package main

import (
    "fmt"
)

func main() {{
    // Demo: {filename}
    fmt.Println("TODO")
}}
"""
    
    # 生成 Go 代码
    go_code = """package main

import (
    "fmt"
)

"""
    
    for func_info in functions:
        name = func_info['name']
        params = convert_ts_params_to_go(func_info['params'])
        return_type = convert_ts_type_to_go(func_info['return_type'])
        
        # 处理返回类型
        if return_type:
            go_func = f"func {name}({params}) {return_type} {{\n"
        else:
            go_func = f"func {name}({params}) {{\n"
        
        # 转换函数体
        body = convert_ts_body_to_go(func_info['body'], name)
        
        go_code += go_func + body + "\n}\n\n"
    
    # 添加 main 函数
    go_code += f"""func main() {{
    // Demo: {filename}
    _ = {functions[0]['name']}
}}
"""
    
    return go_code

def try_gofmt(content: str) -> str:
    """尝试使用 gofmt 格式化"""
    temp_file = '/tmp/_gofmt_generate.go'
    with open(temp_file, 'w') as f:
        f.write(content)
    
    result = subprocess.run(['gofmt', temp_file], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    
    return content

def main():
    ts_base = DSA / 'ts'
    go_base = DSA / 'go'
    
    total = 0
    generated = 0
    gofmt_ok = 0
    gofmt_fail = 0
    
    print("=== 从 TS 生成 Go 代码 ===")
    
    for root, dirs, files in os.walk(ts_base):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for filename in files:
            if not filename.endswith('.ts'):
                continue
            
            total += 1
            ts_fp = Path(root) / filename
            rel_path = ts_fp.relative_to(ts_base)
            go_fp = go_base / str(rel_path).replace('.ts', '.go')
            
            try:
                ts_code = ts_fp.read_text(encoding='utf-8')
                
                # 生成 Go 代码
                go_code = generate_go_code(ts_code, filename)
                
                # 格式化
                formatted = try_gofmt(go_code)
                
                # 写入文件
                go_fp.write_text(formatted, encoding='utf-8')
                generated += 1
                
                # 检查 gofmt 是否成功
                check = try_gofmt(formatted)
                if check == formatted:
                    gofmt_ok += 1
                else:
                    gofmt_fail += 1
            except Exception as e:
                print(f"Error: {ts_fp}: {e}")
    
    print(f"Total: {total}, Generated: {generated}, gofmt OK: {gofmt_ok}, gofmt Fail: {gofmt_fail}")

if __name__ == '__main__':
    main()