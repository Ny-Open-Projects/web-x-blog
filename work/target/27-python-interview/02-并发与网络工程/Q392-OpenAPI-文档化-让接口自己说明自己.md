---
title: [Q392] OpenAPI 文档化:让接口自己说明自己
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q392 · OpenAPI 文档化:让接口自己说明自己

> 难度:★★☆ | 标签:OpenAPI, FastAPI, 文档

**问**:什么是 OpenAPI 规范?如何避免"文档和代码不一致"?

**答**:OpenAPI(Swagger)是描述 HTTP API 的 YAML/JSON 规范:路径、方法、参数、请求/响应 schema、认证方式,可生成 Swagger UI 文档、客户端 SDK 和 mock。避免不一致的核心是"代码即文档":①FastAPI 基于 Pydantic 类型注解自动生成 OpenAPI(`/docs`、`/openapi.json`);②Flask 用 flask-smorest/apispec 从 marshmallow schema 生成;③CI 里校验 schema diff 和示例可运行。文档三要素:准确的状态码、字段含义与示例、错误响应结构。

```python
# file: code/02_并发与网络工程/q392_openapi.py
"""用 Pydantic 描述 API schema,并演示 OpenAPI 文档的核心结构。
真实项目: FastAPI(app) 自动在 /docs 生成同构文档, 此处标准库演示 schema 组装。
"""
from dataclasses import dataclass, field, asdict


@dataclass
class ItemIn:
    name: str
    price: float


@dataclass
class ItemOut:
    id: int
    name: str
    price: float


def build_openapi_spec() -> dict:
    """手工组装一个最小 OpenAPI 3.1 文档, 与 FastAPI 自动生成的结构同构。"""
    return {
        "openapi": "3.1.0",
        "info": {"title": "Item API", "version": "1.0.0"},
        "paths": {
            "/items": {
                "post": {
                    "summary": "创建商品",
                    "requestBody": {
                        "content": {"application/json": {
                            "schema": {"$ref": "#/components/schemas/ItemIn"}}}
                    },
                    "responses": {
                        "201": {"description": "创建成功",
                                "content": {"application/json": {
                                    "schema": {"$ref": "#/components/schemas/ItemOut"}}}},
                        "422": {"description": "参数校验失败"},
                    },
                }
            }
        },
        "components": {"schemas": {
            "ItemIn": {"type": "object",
                       "properties": {"name": {"type": "string"},
                                      "price": {"type": "number"}},
                       "required": ["name", "price"]},
            "ItemOut": {"type": "object",
                        "properties": {"id": {"type": "integer"},
                                       "name": {"type": "string"},
                                       "price": {"type": "number"}},
                        "required": ["id", "name", "price"]},
        }},
    }


if __name__ == "__main__":
    import json
    spec = build_openapi_spec()
    print("paths:", list(spec["paths"]))
    print("示例请求:", json.dumps(asdict(ItemIn("键盘", 199.0)), ensure_ascii=False))
```

**追问**:
- 为什么 422 而不是 400 表示校验失败?FastAPI 沿用社区惯例用 422 Unprocessable Entity 表示"语法正确但语义校验失败",两者都可接受,关键是全团队一致。
- 文档里的示例值怎么定制?FastAPI 用 Pydantic 的 `Field(example=...)` 或 `model_config["json_schema_extra"]` 提供 examples。
