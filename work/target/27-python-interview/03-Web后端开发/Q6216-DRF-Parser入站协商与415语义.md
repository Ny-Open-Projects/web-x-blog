---
title: "[Q6216] DRF Parser：入站内容协商与 renderer 的对称面"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6216 · DRF Parser：入站内容协商与 renderer 的对称面

难度：P6 ｜ 标签：DRF、parser_classes、内容协商、415、JSONParser、FormParser、MultiPart

**问**：DRF 的 `parser_classes` 和 `renderer_classes` 分别管请求的哪一段？客户端 POST 一个 `text/csv` 的 body，会得到什么状态码？`multipart/form-data` 与 `application/x-www-form-urlencoded` 各由谁解析、怎么选？为什么"只配 JSONParser"的服务对表单提交天然免疫（还是天然不兼容）？解析失败和解析器缺失的错误结构一样吗？

**答**：
结论：DRF 在**入站**用 `parser_classes` 按 `Content-Type` 请求头分发解析器（JSONParser / FormParser / MultiPartParser / FileUploadParser...），在**出站**用 `renderer_classes` 按 `Accept` 头协商渲染器——两个独立的协商面，一个管进一个管出。请求的 Content-Type 没有任何已配置解析器支持时返回 **415 Unsupported Media Type**（`{"detail": "Unsupported media type ..."}`），而 body **解析失败**（JSON 语法坏）返回 **400**，错误结构是字段级字典（DRF 的 parse error 映射到 detail 或字段结构）——415 与 400 的区分让客户端能分辨"我发错了类型"与"我发错了内容"。选择：`urlencoded`（FormParser）管简单键值（表单默认），`multipart`（MultiPartParser）管**文件上传**（multipart 流式解析与临时文件策略见 Q6080）；纯 API 服务只配 JSONParser 时，HTML 表单/文件上传直接 415——这既是"天然不兼容"，也可以说是"明确的契约拒绝"。解析器列表还决定 OpenAPI 文档的 requestBody 媒体类型——parser 配置直接写进接口契约。

取舍：a) API-only 服务：`parser_classes = [JSONParser]` 收紧面——不支持的类型明确 415，比"啥都收然后 400"契约清晰；b) 混合服务（页面 + API）：JSON + Form + MultiPart，但注意 MultiPartParser 的内存/临时文件成本，超大上传走独立端点或直传（Q6064）；c) 自定义解析器（CSV、Protobuf）：实现 `BaseParser.parse(stream, media_type, parser_context)` 返回数据结构，流式解析大 CSV 时注意 DRF 默认把整个 body 读进内存——上限控制（Q6152）先于解析器；d) Content-Type 缺失的兼容：DRF 默认无头时按第一个 parser 或当 form 处理，显式配 JSONParser-only 后无头请求也会 415——移动端老版本不带头的要先排查；e) 渲染协商失败（Accept 不可满足）是 **406**，与 415 对称——客户端能力与服务端能力的双向探测都要有明确失败语义。

实战：事故形态是"运营后台用一个 HTML 表单直连 API 建数据，接口 parser 只配了 JSON，415 没被前端处理，表现为'提交没反应'；修复为该端点加 FormParser 并在文档标注，同时给 415/406 增加监控维度（客户端能力漂移的可观测信号）"。下面实现协商分发器。

```python
PARSERS = {
    "application/json": "JSONParser",
    "application/x-www-form-urlencoded": "FormParser",
    "multipart/form-data": "MultiPartParser",
}


def parse_in(content_type: str, body: str):
    base = content_type.split(";")[0].strip().lower()
    parser = PARSERS.get(base)
    if parser is None:
        return {"status": 415, "error": f"Unsupported media type: {base or '(none)'}"}
    if parser == "JSONParser":
        return {"status": 200, "parser": parser, "data": {"echo": body}}
    if parser == "FormParser":
        data = dict(p.split("=", 1) for p in body.split("&") if "=" in p)
        return {"status": 200, "parser": parser, "data": data}
    return {"status": 200, "parser": parser, "data": {"files": "streamed-to-tempfile"}}


print("[1] JSON:", parse_in("application/json; charset=utf-8", '{"a":1}'))
print("[2] 表单:", parse_in("application/x-www-form-urlencoded", "a=1&b=2"))
print("[3] 未支持的类型:", parse_in("text/csv", "x,y"))
print("[4] 无 Content-Type:", parse_in("", "a=1"), "——JSON-only 服务将 415, 客户端必须带头")

print("[5] 语义矩阵: 类型不支持=415 / 内容解析坏=400 / Accept 不满足=406")
```

**追问一**：415、400、406 三者怎么构成完整的协商语义闭环？—— 415（入站类型不支持）与 406（出站类型不可满足）是**能力面**错误：客户端该修正 Content-Type/Accept 而不是重试相同请求；400 是**内容面**错误：类型对了但 body 语法或语义非法。闭环的意义在排障：监控按这三个码分类，415 激增 = 客户端版本能力漂移（新 SDK 改了默认类型），400 激增 = 契约破坏（字段改名），406 激增 = 网关/中间层改写了 Accept 头。没有这三类区分的 API，所有协商问题都混在 400 里，永远查不清。

**追问二**：自定义 CSV 解析器要注意什么内存问题？—— DRF 默认的 `JSONParser`/自定义解析器拿到的是 `request.stream`（可流式读），但常见实现是 `stream.read()` 一把梭——大 CSV 直接 OOM（Q6051 一族）。正确姿势：在 parse 里逐行读 stream、边读边校验边产出（生成器或分块列表），并把**字节上限**放在解析器之前（Content-Length 校验或流式累计计数）。另一个坑是 DRF 的 MultiPartParser 对大文件的临时文件策略（Q6080）：写盘路径与清理时机要确认，否则磁盘被临时文件填满。解析器的契约是"把流变成结构"，流控与上限是调用方（框架）与解析器共同的责任，单独靠任何一方都会漏。

## 背诵要点
- parser_classes 按 Content-Type 管入站，renderer_classes 按 Accept 管出站；两个独立协商面。
- 语义闭环：类型不支持 415 / 内容解析坏 400 / Accept 不满足 406——监控按三类分开，各自指向不同客户端病因。
- API-only 收紧到 JSONParser 让不兼容明确化；自定义解析器必须流式 + 上限前置，否则 OOM。

## 复盘追问
- HTML 表单提交"没反应"，为什么是 415 而不是 400？（parser 不支持该 Content-Type；415/400/406 的区分与监控）
- 自定义 CSV 解析器的 OOM 风险在哪？（stream 一把梭；逐行流式 + 上限前置 + 临时文件策略）
