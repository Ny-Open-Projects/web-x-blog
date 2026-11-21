---
title: [Q472] eval/exec 的风险与 ast.literal_eval
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q472 · eval/exec 的风险与 ast.literal_eval

> 难度:★★★★ | 标签:安全, eval

**问**:eval("2+3") 看起来无害,为什么生产环境禁用?安全的替代路径是什么?

**答**:eval/exec 在运行时执行任意 Python:配合 `__import__('os').system(...)` 就是远程代码执行,即使传受限 globals,`().__class__.__bases__` 式的逃逸链也防不胜防;编译期还会解析并缓存表达式,构成 DoS 面。替代分三层:纯字面量(数字/字符串/容器)用 ast.literal_eval——它只接受字面量节点、不做名字查找与调用;算术表达式用 ast.parse 后白名单遍历节点求值;规则引擎类需求干脆用领域 DSL(如简单的操作符映射表)。exec 唯一合理场景是自己写 REPL/调试工具,且必须隔离执行环境。

```python
# file: code/01_语言核心与底层/q472_eval_safety.py
import ast

SAFE_OPS = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}

def safe_calc(expr: str):
    """AST 白名单求值:只允许二元算术"""
    node = ast.parse(expr, mode="eval").body
    if not isinstance(node, ast.BinOp):
        raise ValueError("only binary operations allowed")
    op_name = {ast.Add: "add", ast.Sub: "sub", ast.Mult: "mul"}.get(type(node.op))
    if op_name is None:
        raise ValueError(f"operator {type(node.op).__name__} not allowed")
    a = ast.literal_eval(node.left)
    b = ast.literal_eval(node.right)
    return SAFE_OPS[op_name](a, b)

if __name__ == "__main__":
    print(safe_calc("2 + 3"))
    print(safe_calc("10 * 4"))
    for bad in ("__import__('os').system('ls')", "2 ** 8"):
        try:
            safe_calc(bad)
        except ValueError as e:
            print("blocked:", e)
```

**追问**:1) ast.literal_eval 绝对安全吗?——它不执行代码但没限制资源:超深嵌套或超长字符串仍可能耗尽内存/栈,彻底安全要配合输入长度与 AST 深度上限。2) literal_eval 与 eval 的实现差异?——literal_eval 在 ast.parse 结果上只接受字面量节点(容器/数字/字符串/字节,及复数的 +/- BinOp),名字、调用、属性访问一律 ValueError;全程无名字查找,攻击面只剩资源耗尽。3) eval 的执行链为什么防不住?——compile+eval 把字符串编成代码对象再执行;即使注入受限 globals,dunder 探索链(().__class__.__bases__)可以拿到危险类型,历史上所有「安全 eval 沙箱」都被攻破过。4) 生产陷阱?——用 eval 做配置/规则「灵活性」,配置被注入即 RCE;正确路径是白名单操作符 DSL、JSON schema 校验或显式解释器,eval/exec 只留给 REPL 类工具。
