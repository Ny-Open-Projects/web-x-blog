"""同一条登录查询: 拼接被注入绕过, 参数化安全"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE user (name TEXT, pwd TEXT)")
        conn.execute("INSERT INTO user VALUES ('admin', 's3cret')")

        evil = "' OR '1'='1"          # 攻击payload

        # 反面教材: f-string 拼接
        unsafe = f"SELECT * FROM user WHERE name='{evil}' AND pwd='x'"
        print("拼接查询返回:", conn.execute(unsafe).fetchall(), "<- 全表绕过")

        # 正确: 参数化
        safe = "SELECT * FROM user WHERE name = ? AND pwd = ?"
        print("参数化查询返回:", conn.execute(safe, (evil, "x")).fetchall(), "<- 当作普通字符串查无此人")
