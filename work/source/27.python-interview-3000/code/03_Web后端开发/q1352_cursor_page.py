"""不透明游标:base64 排序键 + HMAC 签名防篡改(纯标准库)。"""
import base64
import hashlib
import hmac
import json

SECRET = b"change-me-from-env"
PAGE_SIZE = 3


def make_cursor(sort_key, secret=SECRET):
    payload = base64.urlsafe_b64encode(json.dumps({"k": sort_key}).encode()).decode().rstrip("=")
    sig = hmac.new(secret, payload.encode(), hashlib.sha256).hexdigest()[:16]
    return payload + "." + sig


def parse_cursor(cursor, secret=SECRET):
    """返回排序键;签名不符或格式非法返回 None,调用方回 400。"""
    try:
        payload, sig = cursor.rsplit(".", 1)
        expect = hmac.new(secret, payload.encode(), hashlib.sha256).hexdigest()[:16]
        if not hmac.compare_digest(sig, expect):
            return None
        pad = "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload + pad))["k"]
    except (ValueError, KeyError):
        return None


rows = [{"id": i, "score": 90 - i} for i in range(1, 9)]


def page_after(rows, cursor):
    key = parse_cursor(cursor) if cursor else None
    if cursor and key is None:
        return None, None                      # 伪造游标:400
    start = 0 if key is None else next(i for i, r in enumerate(rows) if r["id"] == key) + 1
    window = rows[start:start + PAGE_SIZE]
    has_more = start + PAGE_SIZE < len(rows)
    next_cursor = make_cursor(window[-1]["id"]) if has_more else None
    return {"items": window, "next_cursor": next_cursor, "has_more": has_more}, None


cursor = None
for _ in range(4):
    page, err = page_after(rows, cursor)
    if err is not None:
        print("400 拒绝伪造游标")
        break
    print([r["id"] for r in page["items"]], "next:", page["next_cursor"])
    if not page["has_more"]:
        break
    cursor = page["next_cursor"]

tampered = make_cursor(2)
tampered = tampered[:-1] + ("0" if tampered[-1] != "0" else "1")
print("篡改游标解析结果:", parse_cursor(tampered))
