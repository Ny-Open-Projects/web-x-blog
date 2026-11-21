"""计数列与实时聚合: 读得快与数得对的取舍"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT, like_count INTEGER NOT NULL DEFAULT 0)")
c.execute("CREATE TABLE likes (post_id INTEGER NOT NULL, user_id INTEGER NOT NULL, "
          "PRIMARY KEY(post_id, user_id))")
c.execute("INSERT INTO posts(id, title) VALUES(1, '设计复盘')")
likes = [(1, u) for u in range(1, 1001)]
c.executemany("INSERT INTO likes VALUES(?,?)", likes)
c.execute("UPDATE posts SET like_count = like_count + 1 WHERE id = 1")
conn.commit()

# 读路径对比: 计数列 O(1) vs 实时聚合 O(n)
t = c.execute("SELECT like_count FROM posts WHERE id=1").fetchone()[0]
real = c.execute("SELECT COUNT(*) FROM likes WHERE post_id=1").fetchone()[0]
print("读路径: 计数列=%d 实时聚合=%d (一致, 但聚合要扫 likes 索引)" % (t, real))

# 一致性窗口: 计数列的更新若与明细不在同一事务, 就会漂移
c.execute("INSERT INTO likes VALUES(1, 9999)")          # 只写明细, 忘了同步计数
print("漏同步后: 计数列=%d 实时聚合=%d (漂移了 1)" %
      (c.execute("SELECT like_count FROM posts WHERE id=1").fetchone()[0],
       c.execute("SELECT COUNT(*) FROM likes WHERE post_id=1").fetchone()[0]))

# 修复: 以明细为准重算, 并规定计数列只允许'同事务内'变更
c.execute("UPDATE posts SET like_count = (SELECT COUNT(*) FROM likes WHERE post_id = likes.post_id) "
          "WHERE id = 1")
c.execute("INSERT INTO likes VALUES(1, 8888)")          # 正确姿势: 同一事务里两件事一起做
c.execute("UPDATE posts SET like_count = like_count + 1 WHERE id = 1")
t2 = c.execute("SELECT like_count FROM posts WHERE id=1").fetchone()[0]
real2 = c.execute("SELECT COUNT(*) FROM likes WHERE post_id=1").fetchone()[0]
print("重算后再同事务写入: 计数列=%d 聚合=%d 重新一致" % (t2, real2))
print("结论: 计数列是读写权衡的缓存, 收益是 O(1) 读, 代价是必须用事务纪律和定期对账偿还")
