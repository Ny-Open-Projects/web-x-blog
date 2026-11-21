"""大结果外置句柄:完整结果落盘,上下文只放句柄与预览,按需取回并校验归属。"""
import hashlib
import json


class ArtifactStore:
    """外置存储桩:put 返回轻量句柄,fetch 按 ref 与租户归属取回片段。"""

    def __init__(self, preview_len=40):
        self.blobs = {}
        self.preview_len = preview_len

    def put(self, tenant, payload):
        raw = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False, sort_keys=True)
        ref = "art-" + hashlib.md5(raw.encode("utf-8")).hexdigest()[:8]
        self.blobs[ref] = {"tenant": tenant, "raw": raw}
        handle = {"ref": ref, "size": len(raw),
                  "preview": raw[:self.preview_len] + "...[已外置,按需取回]"}
        return handle

    def fetch(self, tenant, ref, offset=0, limit=80):
        blob = self.blobs.get(ref)
        if blob is None:
            raise KeyError(ref)
        if blob["tenant"] != tenant:
            raise PermissionError("跨租户取回被拒绝")
        return blob["raw"][offset:offset + limit]

    def cleanup(self, tenant):
        doomed = [r for r, b in self.blobs.items() if b["tenant"] == tenant]
        for r in doomed:
            del self.blobs[r]
        return len(doomed)


if __name__ == "__main__":
    store = ArtifactStore()
    big = "账单明细:" + ",".join("item-%04d" % i for i in range(300))
    handle = store.put("tenant-a", big)

    assert handle["size"] > 2000 and len(handle["preview"]) <= 60, "句柄必须足够轻"
    got = store.fetch("tenant-a", handle["ref"], offset=0, limit=20)
    assert got == big[:20], "按需取回与原文对齐"

    blocked = False
    try:
        store.fetch("tenant-b", handle["ref"])
    except PermissionError:
        blocked = True
    assert blocked, "跨租户取回必须被拒绝"

    assert store.cleanup("tenant-a") == 1
    gone = False
    try:
        store.fetch("tenant-a", handle["ref"])
    except KeyError:
        gone = True
    assert gone, "回收后句柄失效"
    print("外置句柄通过:大结果落盘只留句柄,取回校验租户,回收后句柄失效")
