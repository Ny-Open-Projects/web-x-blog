"""软删除端点语义: DELETE 只打标记, 读取路径默认过滤(纯标准库)。"""
import time


class Store:
    def __init__(self):
        self.rows = {}                              # id -> row, 含 deleted_at

    def delete(self, row_id):
        row = self.rows.get(row_id)
        if row is None or row.get("deleted_at"):
            return 404
        row["deleted_at"] = time.time()
        return 204

    def get(self, row_id, include_deleted=False):
        row = self.rows.get(row_id)
        if row is None:
            return 404, None
        if row.get("deleted_at") and not include_deleted:
            return 404, None                        # 软删后对默认读取不可见
        return 200, row

    def list_rows(self, include_deleted=False):
        return [r for r in self.rows.values()
                if include_deleted or not r.get("deleted_at")]


store = Store()
store.rows = {"a1": {"id": "a1", "title": "Alive"},
              "d1": {"id": "d1", "title": "Doomed"}}

print("DELETE d1     ->", store.delete("d1"))
print("DELETE d1 重复 ->", store.delete("d1"))
print("GET  d1 默认  ->", store.get("d1")[0])
print("GET  d1 全量  ->", store.get("d1", include_deleted=True)[0])
print("列表默认      :", [r["id"] for r in store.list_rows()])
print("列表含已删    :", [r["id"] for r in store.list_rows(True)])
assert store.get("d1")[0] == 404 and store.get("d1", True)[0] == 200
print("要点: 软删除改变的是读路径的默认过滤, DELETE 的对外语义不变; 全量视图必须显式打开且只给管理端")
