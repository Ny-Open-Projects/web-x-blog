"""sqlite 触发器写审计日志, 并与应用层显式审计对照"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript("""
            CREATE TABLE acct (id INTEGER PRIMARY KEY, bal INT);
            CREATE TABLE audit (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                acct_id INT, old_bal INT, new_bal INT);
            CREATE TRIGGER trg_audit AFTER UPDATE ON acct
            BEGIN
              INSERT INTO audit (acct_id, old_bal, new_bal)
              VALUES (old.id, old.bal, new.bal);
            END;
            INSERT INTO acct VALUES (1, 100);
        """)
        conn.execute("UPDATE acct SET bal = bal - 30 WHERE id = 1")
        conn.commit()
        print("触发器审计:", conn.execute(
            "SELECT acct_id, old_bal, new_bal FROM audit").fetchall())
        print("取舍: 触发器任何入口都生效, 但逻辑隐于库内; 应用层审计更显式可测")
