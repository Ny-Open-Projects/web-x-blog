---
title: [Q6048] OpenAPI 3.0 到 3.1 演进与 schema-first
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6048 · OpenAPI 3.0→3.1 演进与 schema-first 工作流

> 难度:★★★☆ | 标签:OpenAPI, 版本演进, Pydantic v2, schema

**问**：OpenAPI 3.1 相对 3.0 最关键的规范变化是什么（与 JSON Schema 2020-12 对齐）？`nullable` 与类型数组的表达差异会让旧工具链怎么坏？Pydantic v2 与 FastAPI 在这个演进里各扮演什么角色？schema-first 工作流如何落地？

**答**：3.1 的本质变化：OpenAPI Schema Object 不再是 JSON Schema 的"子集方言"，而是**直接采用 JSON Schema 2020-12**。最常踩的差异：1) 可空表达从 `type: [string, "null"]`（3.1）vs `nullable: true`（3.0）——旧代码生成器/文档工具不认数组形式就崩；2) 独占性从 `oneOf+nullable` 组合变为规范 JSON Schema 关键词；3) `$ref` 兄弟节点（3.0 禁止 `$ref` 旁写 description，3.1 允许）；4) 新增 `examples` 数组、`jsonSchemaDialect` 字段。Python 侧的分工：**Pydantic v2**（基线 2.x）内部就是 JSON Schema 2020-12 生成器（`model_json_schema()`），`Optional[str]` 自动生成 `anyOf: [string, null]` 的 3.1 风格；**FastAPI**（基线 0.100+，基于 Pydantic v2）`openapi()` 输出 3.1.0 版本文档。schema-first 落地：契约（YAML）先行 → 代码生成（datamodel-code-generator 基线 0.25+）→ CI 校验实现与契约一致（schemathesis/契约测试）；与 FastAPI 的 code-first（注解自动生成）相比，schema-first 适合多语言/多团队契约协作，code-first 开发快——常见折中是 code-first 生成 + 契约 diff 门禁。迁移注意：升级后旧客户端 SDK（3.0 生成器产物）要重新生成；网关/文档工具的 3.1 支持矩阵先核对。

```python
# file: code/03-Web后端开发/q6048_openapi31.py
import json
import sys

print("python:", sys.version_info[:3])

try:
    import pydantic
    from pydantic import BaseModel, Field
    HAVE_PYDANTIC_V2 = pydantic.VERSION.startswith("2")   # 仅 v2 按 2020-12 生成
except ImportError:
    HAVE_PYDANTIC_V2 = False

if HAVE_PYDANTIC_V2:
    class User(BaseModel):
        nickname: str | None = None            # 可空: 3.1 风格 anyOf
        age: int = Field(ge=0, le=150)

    schema = User.model_json_schema()
    print("Pydantic v2 (JSON Schema 2020-12):")
    print(json.dumps(schema["properties"]["nickname"], ensure_ascii=False))
    # -> anyOf: [{type: string}, {type: null}]  == OpenAPI 3.1 风格
else:
    print("缺 pydantic v2(降级): 手写 3.1 风格 schema 对照")

# 3.0 与 3.1 的可空表达对照(工具链兼容的坏点)
OPENAPI_30 = {"type": "string", "nullable": True}                    # 3.0 方言
OPENAPI_31 = {"anyOf": [{"type": "string"}, {"type": "null"}]}       # 3.1 = JSON Schema
print("3.0 可空:", json.dumps(OPENAPI_30))
print("3.1 可空:", json.dumps(OPENAPI_31))
print("旧 3.0 代码生成器看到 3.1 的 anyOf/null type 会直接报错 -> SDK 必须重新生成")

# $ref 兄弟节点: 3.0 禁止, 3.1 允许(文档注释可与 $ref 并存)
REF_31 = {"$ref": "#/components/schemas/User", "description": "下单用户"}
print("3.1 允许 $ref+description 并存:", json.dumps(REF_31, ensure_ascii=False))

# schema-first 契约 diff 门禁示例: 比较 nullable 表达是否等价
def nullable_31_to_30(s):
    if "anyOf" in s:
        non_null = [x for x in s["anyOf"] if x.get("type") != "null"]
        has_null = any(x.get("type") == "null" for x in s["anyOf"])
        if len(non_null) == 1 and has_null:
            return {**non_null[0], "nullable": True}
    return s

print("等价转换(3.1->3.0 兼容层):", json.dumps(nullable_31_to_30(OPENAPI_31)))
```

**追问**：1) 为什么 Pydantic v2 的 schema 生成被视作 3.1 迁移的加速器？——v1 时代生成的是带方言补丁的输出，v2 底层直接按 JSON Schema 2020-12（`core_schema` → JSON Schema），字段级控制（`json_schema_extra`/`examples`）与新关键词对齐，FastAPI 0.100+ 因此原生出 3.1 文档。2) `oneOf` 与 `anyOf` 在校验语义上的差异对 API 客户端意味着什么？——oneOf 要求恰好匹配一个分支（歧义即报错），anyOf 允许多分支匹配；客户端代码生成器对 oneOf 的 union 生成更保守，契约设计要明确选择并保持一致。3) 契约测试（schemathesis）怎么接进 CI？——从 openapi.json 属性化生成用例（含负例）打真实服务，断言响应符合 schema；配合契约 diff 门禁（ breaking change 检查，呼应 Q6012 的版本治理）。

## 背诵要点
- OpenAPI 3.1 = JSON Schema 2020-12 全量采用；可空从 nullable 变 anyOf/null，旧生成器必坏。
- Pydantic v2 原生按 2020-12 生成 schema；FastAPI 0.100+ 输出 3.1.0；升级后 SDK/网关要重新生成。
- schema-first（契约先行+CI diff 门禁）vs code-first（FastAPI 注解）按团队协作面选择，常见折中是生成+门禁。

## 复盘追问
- 升级到 3.1 文档后某个内部 SDK 生成失败，你如何快速区分"生成器太旧"与"契约真的破坏性变更"？（提示：用等价转换层或先出 3.0 兼容文档给旧工具，同时跑 diff 门禁判定语义变化）
- 多团队场景里 code-first 的 FastAPI 如何避免"文档即实现"漂移出契约？（提示：CI 生成 openapi.json 与已发布契约做 breaking-diff，禁止未经评审的破坏性变更合入）
