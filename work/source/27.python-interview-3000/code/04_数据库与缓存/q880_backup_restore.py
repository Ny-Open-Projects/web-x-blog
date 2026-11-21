"""sqlite3 在线备份 + 重放操作日志, 模拟 PITR 恢复思路"""
import sqlite3

if __name__ == "__main__":
    src = sqlite3.connect("q880_src.db")
    src.execute("CREATE TABLE IF NOT EXISTS ops (id INTEGER PRIMARY KEY, cmd TEXT)")
    src.execute("DELETE FROM ops")
    src.commit()                          # 备份前提交, 避免备份与未决事务冲突

    dest = sqlite3.connect("q880_bak.db")
    src.backup(dest)                      # 全量快照, 期间源库仍可写
    src.execute("INSERT INTO ops (cmd) VALUES ('delete_user')")
    src.commit()
    print("备份后源库新增了一条危险操作")

    # 恢复: 不重放危险操作, 只恢复到备份点
    restored = sqlite3.connect("q880_bak.db")
    print("恢复库 ops 行数:", restored.execute("SELECT COUNT(*) FROM ops").fetchone()[0])
    print("源库 ops 行数:", src.execute("SELECT COUNT(*) FROM ops").fetchone()[0])
    src.close(); dest.close(); restored.close()
