"""response_model 的字段裁剪语义: 多余字段丢弃, 缺字段报错(纯标准库模拟)。"""
try:
    from fastapi import FastAPI
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("[降级] 未安装 fastapi, 以下用纯函数模拟 response_model 的裁剪行为")

RESPONSE_MODEL = {"id": str, "title": str, "owner_uid": str}


def serialize(obj, model=RESPONSE_MODEL):
    """按 response_model 裁剪: 声明内字段必须齐, 未声明字段一律丢弃。"""
    out = {}
    for name, typ in model.items():
        if name not in obj:
            raise ValueError(f"响应缺少声明字段: {name}")     # 由调用处捕获
        if not isinstance(obj[name], typ):
            raise TypeError(f"字段 {name} 类型不符: 期望 {typ.__name__}")
        out[name] = obj[name]
    return out


user = {"id": "u1", "title": "笔记一", "owner_uid": "u9",
        "password_hash": "secret", "is_admin": True}         # 多出的敏感字段
print("裁剪后:", serialize(user))

try:
    serialize({"id": "u1", "title": "t"})
except ValueError as e:
    print("缺字段:", e)

try:
    serialize({"id": 123, "title": "t", "owner_uid": "u9"})
except TypeError as e:
    print("类型不符:", e)

print("要点: 返回对象可以比模型胖, 但契约以 response_model 为准; 缺声明字段在开发期就暴露")
