---
title: "[Q5149] ast.literal_eval 的安全边界与解析成本"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5149 · ast.literal_eval 的安全边界与解析成本

难度：P6 ｜ 标签：ast、安全、eval、配置解析

**问**：需要把存成字符串的"配置/参数"（如 `"(1, 2, 'fast')"`、`"{'retries': 3}"`）还原成 Python 对象。`eval` 为什么不能用？`ast.literal_eval` 安全吗、能防住所有攻击吗？它的解析成本和 JSON 比如何？

**答**：
结论：`eval` 执行任意代码，字符串来源不可信时就是 RCE（`__import__('os').system(...)` 一行即中招）。`ast.literal_eval` 先用 parser 生成 AST，再**只接受字面量节点**（str/bytes/num/tuple/list/dict/set/bool/None 与正负号组合），任何 Name/Call/BinOp 节点直接拒绝——所以 `__import__`、属性访问、运算表达式都会抛 `ValueError`。但它**不是沙箱**：① 超大输入会让 parser/编译器消耗大量内存 CPU（旧版 Python 甚至 `10**10**10**10` 会打满 CPU，3.x 已对 int 幂运算长度限制）；② 非法嵌套深度可触发 RecursionError。JSON 能覆盖的需求一律用 `json.loads`——更安全、更快（C 解析器）、无 Python 特有字面量歧义。

取舍：`literal_eval` 的独特价值是**非 JSON 的 Python 字面量**：tuple、bytes（`b"..."`）、set、True/False/None、混合数字（如 `(1, 2)` 无引号键）。若数据可以改造成 JSON，就迁移到 JSON 并保留 literal_eval 只读历史数据。

实战：成本账——literal_eval 走 Python 层 AST 遍历，比 C 实现的 `json.loads` 慢约一个数量级；批量解析历史列时先按"是否以 `[`/`{`/`\"` 开头"分流到 json，只有 fallback 才进 literal_eval。解析入口加长度上限（如 64KB）与调用频率限流。

```python
import ast, json, timeit

cases = {
    "tuple": "(1, 2, 'fast')",
    "dict":  "{'retries': 3, 'ssl': True}",
    "bytes": b"'raw-bytes-literal'".decode(),
    "set":   "{1, 2, 3}",
}
for name, s in cases.items():
    print(name, "->", ast.literal_eval(s))

# eval 的 RCE 面与 literal_eval 的拒绝面
evil = "__import__('os').getcwd()"      # 演示用无害函数
try:
    ast.literal_eval(evil)
except ValueError as e:
    print("literal_eval rejects:", e)

# 但它不是沙箱：资源型 DoS 仍需入口防护
try:
    ast.literal_eval("[" * 100 + "]" * 100)     # 深嵌套：能扛住小规模
    print("nested ok (small)")
except (ValueError, RecursionError, MemoryError) as e:
    print("nested rejected:", type(e).__name__)

# 成本对比：literal_eval vs json.loads（同构数据；注意 'x'*20 这类
# BinOp 表达式本身就是 literal_eval 拒绝的形态，输入必须是纯字面量）
py_str = "{'a': 1, 'b': [1, 2, 3], 'c': 'xxxxxxxxxxxxxxxxxxxx'}"
json_str = json.dumps({"a": 1, "b": [1, 2, 3], "c": "xxxxxxxxxxxxxxxxxxxx"})
t_le = timeit.timeit(lambda: ast.literal_eval(py_str), number=2000)
t_js = timeit.timeit(lambda: json.loads(json_str), number=2000)
print(f"literal_eval {t_le*1000:.1f}ms  json.loads {t_js*1000:.1f}ms")
```

**追问一**：literal_eval 内部怎么拒绝非字面量？——先 `compile(..., 'eval')` 得 AST，`ast.literal_eval` 递归检查节点类型白名单；遇到 BinOp 只允许数字 +/- 的有限形态（老版本对 `-1` 这类），其余节点直接抛 ValueError，不进入求值器。

**追问二**：为什么说"白名单 AST"思路比"过滤字符串"可靠？——字符串过滤可被编码技巧绕过（f-string、转义、装饰器语法）；AST 白名单在语法树层面无法表达调用，绕过面为零；这与 SQL 参数化优于字符串转义是同一设计哲学。

**追问三**：如果必须解析用户提交的"表达式"（如过滤规则 `price > 100`）怎么办？——literal_eval 表达不了比较运算；方案是自建受限 DSL → 白名单 AST 校验器（遍历允许的节点集），或干脆暴露结构化查询接口（JSON filter），讨论各自的实现成本。

## 背诵要点
- `eval` = RCE；`ast.literal_eval` 只收字面量 AST 节点，Call/Name/BinOp 一律 ValueError。
- literal_eval 不是沙箱：深嵌套/超长输入可 DoS，入口要限长限频；非 JSON 场景（tuple/bytes/set）才用它。
- 能 JSON 就 JSON：C 解析器快约一个数量级，语义无歧义；批量解析按前缀分流。

## 复盘追问
- 存量库里有 500 万行 Python 字面量字段，迁移到 JSON 的方案与风险？（双写 + 回读校验 + 按前缀兼容解析期，讨论 bytes/tuple 的 JSON 语义丢失如何处理）
- 若字符串来自内部同事（半可信），eval 是否可接受？（内部也不行：凭证泄露/供应链都会让内部输入变攻击面，讨论纵深防御）
