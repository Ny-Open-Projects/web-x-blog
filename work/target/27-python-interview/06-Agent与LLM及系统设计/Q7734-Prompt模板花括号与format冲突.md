---
title: "[Q7734] Prompt 里的 JSON 示例被 format 吃掉：KeyError: '\"name\"'"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7734 · Prompt 里的 JSON 示例被 format 吃掉：KeyError: '"name"'

难度：P6 ｜ 标签：prompt 模板、str.format、string.Template、转义

基线：Python 3.12；`str.format`、`string.Template.substitute`；渲染后 JSON 校验。

**问**：prompt 模板用 `str.format()` 渲染，里面写了一段输出格式示例 `{"name": "...", "age": 0}`，渲染时直接 `KeyError: '"name"'`。有的模板更隐蔽：渲染"成功"了，但模型收到的示例变成残缺 JSON，输出也跟着坏。怎么既保留 JSON 示例又用模板变量？

**答**：
- **结论**：`str.format()` 把 `{}` 当占位符，JSON 的花括号必须写成 `{{` / `}}` 转义。忘了转义就抛 `KeyError`（花括号里的内容被当字段名）或 `IndexError`（空 `{}`）。更危险的是**部分转义**：一半 `{{` 一半 `{`，渲染不报错但 JSON 已经坏了，模型照着坏示例输出。
- **取舍**：三条路：① `.format()` + 严格转义，功能全但人肉易错；② `string.Template`（`$var`），JSON 安全，但 `safe_substitute` 遇到未定义变量会**静默保留变量名**；③ 模板引擎（Jinja2 `{{ }}` / `{% %}`），功能强但引入依赖与注入面（模板内容来自用户时要沙箱）。JSON 重的 prompt 首选 `string.Template` + `substitute`（未定义就报错）。
- **实战**：① 渲染后对"示例段"做一次 `json.loads` 校验；② 用 `Template.substitute` 而不是 `safe_substitute`，让缺变量 fail-fast；③ 单测覆盖变量里含 `{}`、`$`、引号、换行的注入用例；④ 模板与变量分离存放（配置中心/文件），别在代码里拼字符串。

```python
"""format 的花括号冲突、Template 的安全替换、渲染后 JSON 校验。"""
import json
from string import Template

PROMPT = """你是数据抽取助手。请按以下 JSON 结构输出：
{{"name": "...", "age": 0}}
用户输入：{user_input}
只输出 JSON。"""

TEMPLATE = """你是数据抽取助手。请按以下 JSON 结构输出：
{"name": "...", "age": 0}
用户输入：$user_input
只输出 JSON。"""


def validate_example(rendered: str) -> dict:
    """取出示例那一行做 JSON 校验。"""
    for line in rendered.splitlines():
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            return json.loads(line)
    raise ValueError("模板里找不到 JSON 示例")


if __name__ == "__main__":
    # 1) 忘记转义：JSON 的花括号被当占位符
    unescaped = '{"name": "...", "age": 0}\n用户输入：{user_input}'
    try:
        unescaped.format(user_input="张三 28 岁")
    except KeyError as e:
        print("未转义:", type(e).__name__, e)

    # 2) 正确转义后渲染
    rendered = PROMPT.format(user_input="张三 28 岁")
    print("转义后示例行:", [l for l in rendered.splitlines() if l.startswith("{")][0])
    print("示例合法:", validate_example(rendered))

    # 3) 变量值里带花括号：不会被二次解析（format 只看模板）
    tricky = PROMPT.format(user_input='{"name": "李四"}')
    print("变量含括号也安全:", tricky.splitlines()[2])

    # 4) Template：JSON 不用转义，但漏传变量会炸
    t = Template(TEMPLATE)
    print("Template 渲染:", t.substitute(user_input="张三 28 岁").splitlines()[2])
    try:
        t.substitute()
    except KeyError as e:
        print("缺变量:", e)

    # 5) safe_substitute 静默保留，模型会看到变量名
    print("safe_substitute:", t.safe_substitute().splitlines()[2],
          "-> 占位符原样进了 prompt")

    # 6) 模板转义对了，但值里有引号：示例 JSON 被破坏
    broken = '{{"name": "{value}"}}'
    out = broken.format(value='他说"你好"')
    print("值未转义:", out)
    try:
        validate_example(out)
    except json.JSONDecodeError as e:
        print("校验拦住了:", e)
    safe = json.dumps({"name": '他说"你好"'}, ensure_ascii=False)
    print("用 json.dumps 生成:", safe, "| 校验:", validate_example(safe))

    print("结论：JSON 示例要么全转义要么换 Template；渲染后必须校验示例段")
```

**追问一**：`safe_substitute` 为什么危险？
→ 解析：未定义的占位符原样保留（`$missing` 留在 prompt 里），模型看到的是变量名不是值，而且**不报错**，问题会以"模型答非所问"的形式出现在线上。`substitute` 抛 `KeyError`，在渲染阶段就暴露，生产环境应该用它。

**追问二**：f-string 生成的模板有什么问题？
→ 解析：f-string 在**定义时**求值，变量必须已经存在，无法做成"模板 + 运行期填充"；`{{` / `}}` 的转义规则与 `.format` 完全一样，JSON 示例依旧要转义，人肉维护成本更高。
