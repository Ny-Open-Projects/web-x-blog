#!/usr/bin/env python3
"""从 TS 源文件生成正确的 Java 代码"""

import os
import re
from pathlib import Path

DSA = Path('/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa')

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

def convert_ts_type_to_java(ts_type: str) -> str:
    """将 TS 类型转换为 Java 类型"""
    type_map = {
        'number': 'int',
        'string': 'String',
        'boolean': 'boolean',
        'void': 'void',
        'null': 'null',
        'undefined': 'null',
        'number[]': 'int[]',
        'string[]': 'String[]',
        'boolean[]': 'boolean[]',
        'TreeNode': 'TreeNode',
        'ListNode': 'ListNode',
    }
    
    # 处理可空类型
    if '|' in ts_type:
        parts = ts_type.split('|')
        for part in parts:
            part = part.strip()
            if part != 'null' and part != 'undefined':
                return type_map.get(part, part)
        return 'Object'
    
    # 处理数组类型
    if '[]' in ts_type:
        base_type = ts_type.split('[]')[0].strip()
        java_base = type_map.get(base_type, base_type)
        return f'{java_base}[]'
    
    return type_map.get(ts_type, ts_type)

def convert_ts_params_to_java(params_str: str) -> str:
    """将 TS 参数转换为 Java 参数"""
    if not params_str:
        return ''
    
    java_params = []
    for param in params_str.split(','):
        param = param.strip()
        if not param:
            continue
        
        # 分离参数名和类型
        if ':' in param:
            parts = param.split(':')
            name = parts[0].strip()
            ts_type = ':'.join(parts[1:]).strip()
            java_type = convert_ts_type_to_java(ts_type)
            java_params.append(f'{java_type} {name}')
        else:
            java_params.append(param)
    
    return ', '.join(java_params)

def convert_ts_body_to_java(body: str) -> str:
    """将 TS 函数体转换为 Java 函数体"""
    lines = body.split('\n')
    result = []
    
    for line in lines:
        # 移除注释
        line = re.sub(r'//.*', '', line)
        
        # 转换类型
        line = line.replace('number[]', 'int[]')
        line = line.replace('string[]', 'String[]')
        
        # 转换数组方法
        line = line.replace('.length', '.length')  # Java 也是 .length
        line = re.sub(r'\.slice\((\d+)\)', r'Arrays.copyOfRange(nums, \1, nums.length)', line)
        line = re.sub(r'\.slice\((\d+),\s*(\d+)\)', r'Arrays.copyOfRange(nums, \1, \2)', line)
        
        # 转换对象字面量
        line = re.sub(r'new\s+(\w+)\(([^)]+)\)', r'new \1(\2)', line)
        
        # 转换变量声明
        line = re.sub(r'\bconst\b\s+', '', line)
        line = re.sub(r'\blet\b\s+', '', line)
        line = re.sub(r'(\w+)\s*=\s*', r'\1 = ', line)
        
        # 转换三元表达式
        line = re.sub(r'(\w+)\s*\?\s*(\w+)\s*:\s*(\w+)', r'\1 ? \2 : \3', line)
        
        # 转换 Math 方法
        line = line.replace('Math.floor(', '(int)(')
        line = line.replace('Math.ceil(', '(int)(')
        line = line.replace('Math.max(', 'Math.max(')
        line = line.replace('Math.min(', 'Math.min(')
        line = line.replace('Math.random()', 'Math.random()')
        
        # 转换 null 检查
        line = line.replace('=== null', '== null')
        line = line.replace('!== null', '!= null')
        line = re.sub(r'!([\w.]+)', r'\1 == null', line)
        
        result.append(line)
    
    return '\n'.join(result)

def generate_java_code(ts_code: str, filename: str) -> str:
    """从 TS 代码生成 Java 代码"""
    functions = extract_ts_functions(ts_code)
    
    # 提取类名（从文件名）
    class_name = filename.replace('.ts', '').replace('_solution_', '').replace('_', '')
    if not class_name:
        class_name = 'Solution'
    
    if not functions:
        # 如果没有找到函数，返回简单模板
        return f"""package com.webfault.dsa;

import java.util.*;

public class {class_name} {{
    public static void main(String[] args) {{
        // Demo: {filename}
        System.out.println("TODO");
    }}
}}
"""
    
    # 生成 Java 代码
    java_code = f"""package com.webfault.dsa;

import java.util.*;

public class {class_name} {{
    """
    
    for func_info in functions:
        name = func_info['name']
        params = convert_ts_params_to_java(func_info['params'])
        return_type = convert_ts_type_to_java(func_info['return_type'])
        
        # 处理返回类型
        java_func = f"    public {return_type} {name}({params}) {{\n"
        
        # 转换函数体
        body = convert_ts_body_to_java(func_info['body'])
        
        java_code += java_func + body + "\n    }\n\n"
    
    # 添加 main 函数
    java_code += f"""    public static void main(String[] args) {{
        // Demo: {filename}
        {class_name} obj = new {class_name}();
        obj.{functions[0]['name']}(new int[]{{1, 2, 3}});
    }}
}}
"""
    
    return java_code

def main():
    ts_base = DSA / 'ts'
    java_base = DSA / 'java'
    
    total = 0
    generated = 0
    
    print("=== 从 TS 生成 Java 代码 ===")
    
    for root, dirs, files in os.walk(ts_base):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for filename in files:
            if not filename.endswith('.ts'):
                continue
            
            total += 1
            ts_fp = Path(root) / filename
            rel_path = ts_fp.relative_to(ts_base)
            java_fp = java_base / str(rel_path).replace('.ts', '.java')
            
            try:
                ts_code = ts_fp.read_text(encoding='utf-8')
                
                # 生成 Java 代码
                java_code = generate_java_code(ts_code, filename)
                
                # 写入文件
                java_fp.write_text(java_code, encoding='utf-8')
                generated += 1
            except Exception as e:
                print(f"Error: {ts_fp}: {e}")
    
    print(f"Total: {total}, Generated: {generated}")

if __name__ == '__main__':
    main()