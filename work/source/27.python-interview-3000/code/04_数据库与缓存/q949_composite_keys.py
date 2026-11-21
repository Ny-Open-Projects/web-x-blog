"""复合主键中间表 + 联合唯一约束 + 冲突处理"""
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE enrollment (
            student_id INT, course_id INT, grade TEXT,
            PRIMARY KEY (student_id, course_id)
        );
        CREATE TABLE cart (
            id INTEGER PRIMARY KEY,
            user_id INT, sku TEXT, active INT DEFAULT 1,
            UNIQUE (user_id, sku, active)
        );
    """)
    conn.execute("INSERT INTO enrollment VALUES (1, 100, NULL)")
    try:
        conn.execute("INSERT INTO enrollment VALUES (1, 100, 'A')")
    except sqlite3.IntegrityError:
        print("复合主键阻止重复选课")

    conn.execute("INSERT INTO cart (user_id, sku) VALUES (7, 'A')")
    try:
        conn.execute("INSERT INTO cart (user_id, sku) VALUES (7, 'A')")
    except sqlite3.IntegrityError:
        print("联合唯一阻止重复加购")
    conn.execute("UPDATE cart SET active = 0 WHERE user_id = 7 AND sku = 'A'")
    conn.execute("INSERT INTO cart (user_id, sku) VALUES (7, 'A')")
    print("删除后可重新加入:", conn.execute(
        "SELECT count(*) FROM cart WHERE user_id = 7").fetchone()[0], "行")
