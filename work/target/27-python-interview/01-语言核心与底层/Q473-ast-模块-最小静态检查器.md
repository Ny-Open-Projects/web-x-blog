---
title: [Q473] ast 模块:最小静态检查器
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q473 · ast 模块:最小静态检查器

> 难度:★★★★ | 标签:ast, 静态分析

**问**:如何用 ast 模块写一个自定义 lint?NodeVisitor 的访问机制是什么?

**答**:ast.parse 把源码编成语法树,ast.NodeVisitor 提供按节点类型分发的 visit_XXX 钩子,generic_visit 负责递归子节点;不写递归就能遍历全树收集问题。最小 lint 示例:函数体超长告警、裸 except 告警。与 ast.walk 的取舍:walk 是平铺迭代适合「统计某类节点」,NodeVisitor 适合需要跨节点携带状态(当前函数名、嵌套深度)的分析;做变换/生成则用 NodeTransformer。linter、覆盖率、文档工具、类型检查器都是这条路线的工业级实现。

```python
# file: code/01_语言核心与底层/q473_ast_checker.py
import ast

class MiniLint(ast.NodeVisitor):
    """找出过长的函数与裸 except"""
    def __init__(self, max_len=3):
        self.problems = []
        self.max_len = max_len
        self._fname = None

    def visit_FunctionDef(self, node):
        self._fname = node.name
        if len(node.body) > self.max_len:
            self.problems.append(
                f"line {node.lineno}: {node.name} has {len(node.body)} statements"
            )
        self.generic_visit(node)
        self._fname = None

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.problems.append(f"line {node.lineno}: bare except in {self._fname}")
        self.generic_visit(node)

SRC = """
def long_function():
    a = 1
    b = 2
    c = 3
    d = 4
    return a + b + c + d

def fragile():
    try:
        return int("x")
    except:
        return 0
"""

if __name__ == "__main__":
    checker = MiniLint(max_len=3)
    checker.visit(ast.parse(SRC))
    for p in checker.problems:
        print(p)
```

**追问**:1) 为什么 lint 要看 AST 而不是正则匹配源码?——正则不理解语法上下文,字符串里的 "except:"、注释里的代码都会误报;AST 拿到的是解释器同源的语法事实。2) NodeVisitor 与 NodeTransformer 分工?——Visitor 只读收集问题;Transformer 的 visit_XXX 返回新节点完成改写,配 ast.unparse(3.9+)可写 codemod(批量加注解、改名),两者是静态工具链的读写两面。3) ast 节点的位置信息?——3.8 起每个节点带 lineno/end_lineno/col_offset/end_col_offset,函数体长度、代码块覆盖分析不用手工数行;parse 传 type_comments 才能读类型注释。4) 生产陷阱?——parse 用户代码再 exec,以为检查过就安全,实际 exec 仍可逃逸——静态分析必须只读不执行;以及 lint 假设单一 Python 版本的 AST,跨版本 CI 里节点结构差异会让规则失效。
