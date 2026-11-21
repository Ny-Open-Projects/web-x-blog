---
title: [Q2703] 请求体的 charset 与 BOM 容错
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2703 · 请求体的 charset 与 BOM 容错

> 难度:★★☆☆ | 标签:编码, 请求解析

**问**:客户端发的 JSON 有时带 BOM,有时 charset 声明缺失,解析层怎么容错?

**答**:解码一次到位,三层策略:声明了 charset 就按声明来,utf-8 且开头有 BOM 时换 utf-8-sig 一次性剥掉——它只认开头的 BOM,正文里出现 U+FEFF 码位不受影响,比 decode 后手动 lstrip 稳;声明缺失走回退链,utf-8 失败再试 gbk,这是对接历史系统的现实;回退仍失败就显式 400,绝不猜到乱码为止。配套纪律:响应永远带 charset=utf-8 从源头减少歧义;GBK 回退只保留在明确允许老客户端的接口,新接口一律 utf-8 硬校验,防止回退链掩盖真正的编码 bug。json.loads 遇到带 BOM 的 str 会直接抛 Unexpected UTF-8 BOM,所以 BOM 处理必须在 loads 之前。

```python
# file: code/03_Web后端开发/q2703_charset_bom.py
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
```

**追问**:
- 为什么不用 errors='replace' 兜底?——替换字符会静默篡改数据,订单备注与姓名里的坏字节必须显式失败让客户端修,而不是入库后不可追。
- BOM 在正文中段出现怎么办?——那不是 BOM 是零宽字符,原样保留;utf-8-sig 只剥开头,正是这个语义。
