"""一列存多值的反模式: 逗号拼接的查询代价与关联表改造"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE bad_articles (id INTEGER PRIMARY KEY, tags TEXT)")
c.execute("CREATE TABLE articles (id INTEGER PRIMARY KEY, title TEXT)")
c.execute("CREATE TABLE article_tags (article_id INTEGER, tag TEXT, "
          "PRIMARY KEY(article_id, tag))")
c.execute("CREATE INDEX idx_at_tag ON article_tags(tag, article_id)")

TAGS = ["python", "pythonic", "sql", "cache", "db", "ops"]
for i in range(1, 5001):
    ts = ",".join(TAGS[i % 6:] + TAGS[:i % 6])            # 反模式: 拼进一列
    c.execute("INSERT INTO bad_articles VALUES(?,?)", (i, ts))
    for t in TAGS[i % 6:] + TAGS[:i % 6]:                 # 正解: 关联表
        c.execute("INSERT INTO article_tags VALUES(?,?)", (i, t))
    c.execute("INSERT INTO articles VALUES(?,?)", (i, "a%d" % i))
conn.commit()

# 反模式的查询: LIKE 匹配既慢又错
t0 = time.perf_counter()
n_like = c.execute(
    "SELECT COUNT(*) FROM bad_articles WHERE tags LIKE '%python%'").fetchone()[0]
ms_like = (time.perf_counter() - t0) * 1000
print("LIKE '%%python%%' 命中 %d 行 耗时 %.1f ms, 但 pythonic 也被算进来 (语义错)" % (n_like, ms_like))

t0 = time.perf_counter()
n_idx = c.execute(
    "SELECT COUNT(*) FROM article_tags WHERE tag = 'python'").fetchone()[0]
ms_idx = (time.perf_counter() - t0) * 1000
print("关联表等值: %d 行 耗时 %.3f ms (精确 + 索引直达)" % (n_idx, ms_idx))

# 反模式想改精确, 只能求助于笨重的表达式
n_exact = c.execute(
    "SELECT COUNT(*) FROM bad_articles "
    "WHERE ',' || tags || ',' LIKE '%,python,%'").fetchone()[0]
print("拼接逗号再 LIKE: %d 行 (语义对了, 但依旧全表扫描)" % n_exact)

# 反模式还想聚合: 找出与 python 共现最多的 tag, 反范式下几乎写不动 SQL
pairs = c.execute("""SELECT b.tag, COUNT(*) n FROM article_tags a
    JOIN article_tags b ON a.article_id = b.article_id AND a.tag != b.tag
    WHERE a.tag = 'python' GROUP BY b.tag ORDER BY n DESC LIMIT 3""").fetchall()
print("关联表求共现 tag: %s (反模式列里这题要拉回应用层处理)" % pairs)
print("结论: 一列多值同时杀死了精确查询 索引与关系代数, 第一范式不是教条是性能底线")
