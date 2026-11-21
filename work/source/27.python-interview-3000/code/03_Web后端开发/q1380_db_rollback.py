"""迁移 SQL 的可逆性审计:破坏性操作拦截(纯标准库演示)。"""

DESTRUCTIVE = ("drop table", "drop column", "rename column", "truncate", "delete from")


def audit_migration(sql):
    findings = []
    for i, line in enumerate(sql.splitlines(), 1):
        low = line.strip().lower()
        for op in DESTRUCTIVE:
            if low.startswith(op):
                findings.append((i, op, "不可逆:请改为前向兼容两阶段"))
        if low.startswith("add column") and "not null" in low and "default" not in low:
            findings.append((i, "add column not null", "需带默认值,否则全表重写或失败"))
    return findings


sql = """add column nickname varchar(64)
add column level int not null default 0
drop column legacy_flag
truncate table logs"""
for row in audit_migration(sql):
    print(row)
print("审计结论:有不可逆操作,禁止在回滚窗口内执行")
