import json

try:
    from jsonschema import validate, ValidationError  # 演示用,pip install jsonschema
except ImportError:
    print("该题演示需要第三方库 jsonschema:pip install jsonschema,原理见正文")
    raise SystemExit(0)

USER_CONTRACT = {
    "type": "object",
    "required": ["id", "email"],     # 消费方只依赖这两个字段
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
    },
}


def provider_get_user() -> dict:
    """模拟提供方响应,新版本把 email 改成了 mail —— 契约测试应抓住。"""
    return {"id": 1, "mail": "a@x.com", "name": "alice"}


def consumer_uses(resp: dict) -> str:
    return f"send to {resp['email']}"


def test_provider_honors_contract():
    try:
        validate(instance=provider_get_user(), schema=USER_CONTRACT)
        print("contract ok")
    except ValidationError as e:
        print(f"contract broken: {e.message}")
        raise


if __name__ == "__main__":
    try:
        test_provider_honors_contract()
    except ValidationError:
        pass  # 演示:捕获后展示契约破坏
