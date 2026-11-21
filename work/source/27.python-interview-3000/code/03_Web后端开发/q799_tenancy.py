import contextvars

current_tenant: contextvars.ContextVar = contextvars.ContextVar("tenant", default="public")

class TenantTable:
    def __init__(self):
        self.rows: list = []

    def insert(self, tenant: str, data: dict):
        self.rows.append({"tenant": tenant, **data})

    def scoped(self) -> list:
        t = current_tenant.get()
        return [r for r in self.rows if r["tenant"] == t]

orders = TenantTable()
orders.insert("acme", {"id": 1})
orders.insert("globex", {"id": 2})

token = current_tenant.set("acme")
print(orders.scoped())
current_tenant.reset(token)
