"""分页游标编码: 排序键加 tie-breaker 的 base64 载荷(纯标准库)。"""
import base64
import json


class CursorError(Exception):
    pass


def encode_cursor(values):
    """values: [排序键值, tie-breaker], 紧凑 JSON 加 URL 安全 base64。"""
    raw = json.dumps({"v": values}, separators=(",", ":"), ensure_ascii=False)
    return base64.urlsafe_b64encode(raw.encode("utf-8")).decode("ascii")


def decode_cursor(cursor):
    try:
        payload = json.loads(base64.urlsafe_b64decode(cursor.encode("ascii")).decode("utf-8"))
        values = payload["v"]
        if not isinstance(values, list) or len(values) != 2:
            raise CursorError("游标应携带排序键与 tie-breaker 两个值")
        return values
    except CursorError:
        raise
    except (ValueError, KeyError, TypeError) as exc:
        raise CursorError("游标无法解析: {}".format(exc))


def paginate(rows, cursor=None, limit=2):
    """rows 预先按 created_at,id 升序排好; 游标指向上一页最后一行。"""
    data = rows
    if cursor:
        created, rid = decode_cursor(cursor)
        data = [r for r in rows if (r["created_at"], r["id"]) > (created, rid)]
    items = data[:limit]
    next_cursor = None
    if len(data) > limit:
        last = items[-1]
        next_cursor = encode_cursor([last["created_at"], last["id"]])
    return items, next_cursor


rows = [
    {"id": 0, "created_at": "2026-11-05T08:00"}, {"id": 1, "created_at": "2026-11-05T08:00"},
    {"id": 2, "created_at": "2026-11-05T09:00"}, {"id": 3, "created_at": "2026-11-05T09:00"},
    {"id": 4, "created_at": "2026-11-05T10:00"},
]
cursor, pages = None, []
while True:
    items, cursor = paginate(rows, cursor, limit=2)
    pages.append([r["id"] for r in items])
    if not cursor:
        break
print("三页结果:", pages)
assert pages == [[0, 1], [2, 3], [4]]
sample = encode_cursor(["2026-11-05T09:00", 3])
print("游标样例:", sample, "| 解码:", decode_cursor(sample))
try:
    decode_cursor("###bad###")
except CursorError as exc:
    print("伪造游标 -> 400:", exc)
print("要点: 载荷是排序键加唯一 tie-breaker, 解码即校验, 校验失败回 400 而不是 500")
