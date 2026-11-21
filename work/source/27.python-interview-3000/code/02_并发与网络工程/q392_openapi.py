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
