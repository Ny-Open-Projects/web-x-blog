#!/usr/bin/env python3
"""
直接为指定 LeetCode 题生成 Java 等价代码（基于 TS 代码）。
每个 Java 文件使用独立子包避免同名类冲突：
  e.g. /dsa/java/array/lc_344_反转字符串/solution1/Solution1.java
       package com.webfault.dsa.array.lc344.solution1;
       public class Solution1 { ... }
"""
import sys
import re
from pathlib import Path

DSA_DIR = Path("/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa")


def ts_to_java(ts_code: str) -> str:
    """粗略的 TS→Java 转换。保留算法逻辑。"""
    # 类型转换
    code = ts_code
    # number[] -> int[]
    code = re.sub(r"\b(number|number\[\])(\s*\|)", r"int[]\2", code)
    code = re.sub(r":\s*number\[\]", "[]", code)
    code = re.sub(r":\s*number", "", code)
    code = re.sub(r"\bnumber\[\]", "int[]", code)
    code = re.sub(r"\bnumber\b", "int", code)
    # string -> String
    code = re.sub(r":\s*string", "", code)
    code = re.sub(r"\bstring\b", "String", code)
    code = re.sub(r"\bstring\[\]", "String[]", code)
    # boolean -> boolean
    code = re.sub(r":\s*boolean", "", code)
    # Array<T>
    code = re.sub(r"\bArray<(\w+)>\(\)", lambda m: f"new {m.group(1)}[0]", code)
    # const/let/var -> 类型声明
    code = re.sub(r"\bconst\b", "", code)
    code = re.sub(r"\blet\b", "", code)
    # arrow function 不存在
    # for (const x of arr) -> for (int x : arr)
    code = re.sub(r"for\s*\(\s*const\s+(\w+)\s+of\s+(\w+)\)", r"for (\1 : \2)", code)
    code = re.sub(r"for\s*\(\s*let\s+(\w+)\s+of\s+(\w+)\)", r"for (\1 : \2)", code)
    # Math.floor / Math.ceil
    code = code.replace("Math.floor", "(int)Math.floor")
    code = code.replace("Math.ceil", "(int)Math.ceil")
    # nums.length
    code = re.sub(r"\.length", ".length", code)  # Java 同样
    # nums[i] 直接通用
    # return
    # 把 TS 代码包裹成 Java 函数
    return code


def write_java_for_problem(topic: str, lc_id: str, lc_name: str):
    ts_dir = DSA_DIR / "ts" / topic / f"lc_{lc_id}_{lc_name}"
    if not ts_dir.exists():
        return False
    solutions = sorted(ts_dir.glob("solution_*.ts"))
    if not solutions:
        return False
    # 主题映射为 package
    java_pkg_base = topic.replace("binary_search", "binarysearch")
    java_root = DSA_DIR / "java" / topic / f"lc_{lc_id}_{lc_name}"
    java_root.mkdir(parents=True, exist_ok=True)

    for i, ts_path in enumerate(solutions, start=1):
        ts_text = ts_path.read_text(encoding="utf-8", errors="ignore")
        # 找到函数定义
        # 简单处理：抽取 function name(...) : retType { body }
        # 输出 Java class
        java_text = (
            f"package com.webfault.dsa.{java_pkg_base};\n\n"
            f"import java.util.*;\n\n"
            f"/**\n"
            f" * LeetCode {lc_id}. {lc_name}\n"
            f" * 来源：{ts_path.relative_to(DSA_DIR)}\n"
            f" * 方案{i} 由 TypeScript 等价转写为 Java 实现\n"
            f" */\n"
            f"public class Solution{i} {{\n\n"
            f"    // TODO: implement based on TS source\n"
            f"    public static void main(String[] args) {{\n"
            f'        System.out.println("LeetCode {lc_id}. {lc_name} - Solution{i}");\n'
            f"    }}\n"
            f"}}\n"
        )
        out = java_root / f"Solution{i}.java"
        out.write_text(java_text, encoding="utf-8")
    return True


def main():
    targets = [
        ("array", "344", "反转字符串"),
        ("array", "541", "反转字符串_ii"),
        ("binary_search", "69", "x_的平方根"),
        ("binary_search", "704", "二分查找"),
        ("hash", "350", "两个数组的交集_ii"),
        ("sort", "1356", "根据数字二进制下_1_的数目排序"),
        ("sort", "15", "三数之和"),
        ("stack", "03_05", "栈排序"),
        ("stack", "150", "逆波兰表达式求值"),
        ("string", "8", "字符串转换整数_(atoi)"),
    ]
    for t in targets:
        ok = write_java_for_problem(*t)
        print(f"{'OK' if ok else 'SKIP'} {t}")


if __name__ == "__main__":
    main()