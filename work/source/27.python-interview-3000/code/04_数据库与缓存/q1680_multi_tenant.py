"""多租户行级隔离: 统一入口注入 tenant_id 与越权防线"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE invoice(id INTEGER PRIMARY KEY, tenant_id INTEGER, no TEXT, amount REAL);
INSERT INTO invoice VALUES(1, 1, 'INV-001', 100), (2, 1, 'INV-002', 200), (3, 2, 'INV-003', 300);
CREATE UNIQUE INDEX uq_no ON invoice(tenant_id, no);
""")

class TenantRepo:
    """所有读写强制带 tenant_id: 越权的第一道防线是入口收敛"""

    def __init__(self, conn, tenant_id):
        self.conn, self.t = conn, tenant_id

    def list(self):
        return self.conn.execute(
            "SELECT id, no, amount FROM invoice WHERE tenant_id=?", (self.t,)).fetchall()

    def get(self, invoice_id):
        row = self.conn.execute(
            "SELECT id, no, amount FROM invoice WHERE id=? AND tenant_id=?",
            (invoice_id, self.t)).fetchone()
        if row is None:
            raise LookupError(f"invoice {invoice_id} 不存在")  # 不区分不存在与无权, 防探测
        return row

    def add(self, no, amount):
        self.conn.execute(
            "INSERT INTO invoice(tenant_id, no, amount) VALUES(?,?,?)", (self.t, no, amount))
        self.conn.commit()

tenant1 = TenantRepo(conn, 1)
tenant2 = TenantRepo(conn, 2)
print("租户1列表:", tenant1.list())
try:
    tenant1.get(3)                      # 租户2的单据
except LookupError as e:
    print("跨租户读取被拒:", e)
tenant2.add("INV-001", 9.9)             # 同单号不同租户: 联合唯一放行
print("租户2可有自己的 INV-001:", conn.execute(
    "SELECT tenant_id, no FROM invoice WHERE no='INV-001' ORDER BY tenant_id").fetchall())
print("要点: 唯一索引必须包含 tenant_id; ORM 侧用全局查询过滤器兜底, 裸 SQL 绕过入口即是事故;")
print("      越权响应不区分'不存在'与'无权', 避免给攻击者 enumeration 信号")
