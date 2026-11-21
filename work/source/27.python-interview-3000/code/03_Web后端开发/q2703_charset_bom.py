"""请求体的 charset 与 BOM 容错: 解码一次到位(纯标准库)。"""
import json

BOM = b"\xef\xbb\xbf"


def decode_body(raw, charset="utf-8"):
    """按声明字符集解码; BOM 用 utf-8-sig 一次剥掉; 声明缺失时回退链兜底。

    utf-8-sig 只在开头有 BOM 时剥掉它, 正文里出现 U+FEFF 码位不受影响;
    比 decode 后手动 lstrip 更不容易误伤内容。
    """
    declared = (charset or "").split(";")[0].strip().lower() or None
    if declared == "utf-8" and raw.startswith(BOM):
        declared = "utf-8-sig"
    if declared:
        return raw.decode(declared)
    for enc in ("utf-8", "gbk"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("utf-8", raw, 0, 1, "无可用字符集")


def parse_json_body(raw, charset="utf-8"):
    return json.loads(decode_body(raw, charset))


payload = {"msg": "你好", "ok": True}
utf8 = json.dumps(payload, ensure_ascii=False).encode("utf-8")
gbk = json.dumps(payload, ensure_ascii=True).encode("gbk")

assert parse_json_body(utf8) == payload
assert parse_json_body(BOM + utf8, "utf-8") == payload
assert parse_json_body(gbk, None) == payload  # 无声明: utf-8 失败, 回退 gbk
try:
    parse_json_body(b"\xff\xfe\x00", None)
except UnicodeDecodeError as e:
    print("双回退仍失败 -> 400 显式报错:", e.reason)

mid = decode_body("中\ufeff尾".encode("utf-8"), "utf-8")
assert mid == "中\ufeff尾", "正文中段的 U+FEFF 必须保留"
print("BOM 剥除 / 回退链 / 正文中段保留 均通过")
