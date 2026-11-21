"""软删除的恢复端点与保留期: restore 动作的状态码语义(纯标准库)。"""
import time


class RecoverableStore:
    RETENTION = 30 * 86400                          # 保留 30 天

    def __init__(self):
        self.rows = {}

    def soft_delete(self, rid):
        row = self.rows.get(rid)
        if row and not row.get("deleted_at"):
            row["deleted_at"] = time.time()
            return 204
        return 404

    def restore(self, rid, now=None):
        row = self.rows.get(rid)
        if row is None:
            return 404, None
        if not row.get("deleted_at"):
            return 409, {"error": "not_deleted"}
        now = now if now is not None else time.time()
        if now - row["deleted_at"] > self.RETENTION:
            return 410, {"error": "retention_expired"}
        row.pop("deleted_at")
        return 200, row

    def purge_expired(self, now=None):
        now = now if now is not None else time.time()
        gone = [rid for rid, r in self.rows.items()
                if r.get("deleted_at") and now - r["deleted_at"] > self.RETENTION]
        for rid in gone:
            del self.rows[rid]
        return gone


store = RecoverableStore()
store.rows = {"a1": {"id": "a1"},
              "old": {"id": "old", "deleted_at": time.time() - 40 * 86400}}
print("软删 a1     ->", store.soft_delete("a1"))
print("恢复 a1     ->", store.restore("a1")[0])
print("恢复未删 a1 ->", store.restore("a1"))               # 409
print("恢复过期 old->", store.restore("old"))               # 410
print("到期清理    ->", store.purge_expired())
print("清理后 old  ->", store.restore("old")[0])            # 真 404
print("要点: 恢复是显式动作而非改实现字段, 409 表达状态冲突, 410 表达超过保留期不可恢复")
