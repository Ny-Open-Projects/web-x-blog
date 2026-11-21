"""pymysql 演示二级索引查询与回表, 附 EXPLAIN 观察"""
TABLE_SQL = """
CREATE TABLE IF NOT EXISTS user_info (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(32) NOT NULL,
  age INT NOT NULL,
  KEY idx_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

QUERIES = {
    "回表查询": "SELECT id, name, age FROM user_info WHERE name = 'alice'",
    "覆盖索引查询": "SELECT id, name FROM user_info WHERE name = 'alice'",
    "看是否走索引": "EXPLAIN SELECT id, name, age FROM user_info WHERE name = 'alice'",
}

if __name__ == "__main__":
    try:
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="demo")
    except Exception as exc:
        print("无可用 MySQL, 仅说明:", exc)
        print("回表: idx_name 叶子只有 name+id, 取 age 必须回聚簇索引再查一次")
        print("覆盖: SELECT id, name 所需列全在二级索引里, EXPLAIN Extra 出现 Using index")
    else:
        with conn.cursor() as cur:
            cur.execute(TABLE_SQL)
            for label, sql in QUERIES.items():
                cur.execute(sql)
                print(label, "->", cur.fetchall())
        conn.close()
