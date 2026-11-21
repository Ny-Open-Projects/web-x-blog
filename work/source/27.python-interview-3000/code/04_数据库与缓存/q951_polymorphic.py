"""多态关联: target_type + target_id + 复合索引"""
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE article (id INTEGER PRIMARY KEY, title TEXT);
        CREATE TABLE product (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE comment (
            id INTEGER PRIMARY KEY,
            target_type TEXT NOT NULL, target_id INT NOT NULL,
            content TEXT,
            UNIQUE (target_type, target_id, id)
        );
        CREATE INDEX idx_target ON comment (target_type, target_id);
        INSERT INTO article VALUES (1, 'python 调优');
        INSERT INTO product VALUES (10, '键盘');
        INSERT INTO comment (target_type, target_id, content)
          VALUES ('article', 1, '好文'), ('product', 10, '好用');
    """)
    for t, i in (("article", 1), ("product", 10)):
        rows = conn.execute(
            "SELECT content FROM comment WHERE target_type = ? AND target_id = ?",
            (t, i)).fetchall()
        print(f"{t}#{i} 的评论:", rows)
    print("方案一注意: 无库级外键, 删除对象时要级联清理评论")
