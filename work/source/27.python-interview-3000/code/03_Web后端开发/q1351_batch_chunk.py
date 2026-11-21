"""批量接口的上限与内部分片(纯标准库)。"""

MAX_BODY_ITEMS = 1000      # 单请求条数上限,超出 413
CHUNK_SIZE = 100           # 服务端内部再分片的大小


def chunked(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def handle_batch(ids):
    if len(ids) > MAX_BODY_ITEMS:
        return 413, {"error": "BATCH_TOO_LARGE",
                     "message": f"单请求最多 {MAX_BODY_ITEMS} 条,请分批提交"}
    return 200, {"chunks": [len(c) for c in chunked(ids, CHUNK_SIZE)]}


print(handle_batch(list(range(260))))
print(handle_batch(list(range(1500))))
