#!/usr/bin/env python3
"""
TS → Python 翻译器
"""
import re

def transpile(ts_code: str) -> str:
    """将 TypeScript 代码翻译为 Python"""
    
    # 步骤 1: 移除注释
    ts_code = re.sub(r'/\*\*[\s\S]*?\*/', '', ts_code)
    ts_code = re.sub(r'/\*[\s\S]*?\*/', '', ts_code)
    ts_code = re.sub(r'//[^\n]*', '', ts_code)
    
    # 步骤 2: 提取并处理类定义
    classes = {}
    class_pattern = r'class\s+(\w+)\s*\{([^}]+)\}'
    for m in re.finditer(class_pattern, ts_code):
        class_name = m.group(1)
        class_body = m.group(2)
        classes[class_name] = class_body
    
    # 移除类定义
    ts_code = re.sub(class_pattern, '', ts_code)
    
    # 步骤 3: 逐行处理
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
        
        # class 定义（从提取的类中恢复）
        m = re.match(r'^class\s+(\w+)', s)
        if m:
            class_name = m.group(1)
            if class_name in classes:
                result.append(f"class {class_name}:")
                indent = 1
                # 添加类体
                for body_line in classes[class_name].split('\n'):
                    body_s = body_line.strip()
                    if body_s and body_s != '{' and body_s != '}':
                        if 'constructor' in body_s:
                            result.append("    def __init__(self):")
                        else:
                            # 清理类型注解
                            body_s = re.sub(r':\s*\w+(?:\s*\|\s*\w+)*', '', body_s)
                            body_s = body_s.replace('this.', '')
                            if body_s:
                                result.append(f"    {body_s}")
                continue
            else:
                result.append(f"class {class_name}:")
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
        
        # 移除 new
        stmt = re.sub(r'\bnew\s+(\w+)', r'\1', stmt)
        
        if stmt:
            result.append('    ' * indent + stmt)
    
    return '\n'.join(result)


# 测试
if __name__ == '__main__':
    test_ts = '''
function sortedArrayToBST(nums: number[]): TreeNode | null {
    if(!nums.length) return null
    const mid = Math.floor(nums.length / 2)
    const root = new TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums.slice(0,mid))
    root.right = sortedArrayToBST(nums.slice(mid+1))
    return root
}
'''
    print(transpile(test_ts))
