"""长读事务与 WAL 膨胀: 一个挂起的读者挡住整个检查点"""
import os
import shutil
import sqlite3
import tempfile

tmp = tempfile.mkdtemp()
db = os.path.join(tmp, "wal.db")
try:
    w = sqlite3.connect(db, isolation_level=None)     # 自动提交模式, 手工控制事务
    w.execute("PRAGMA journal_mode=WAL")
    w.execute("PRAGMA wal_autocheckpoint=0")          # 关掉自动检查点, 便于观察
    w.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")

    r = sqlite3.connect(db, isolation_level=None)
    r.execute("BEGIN")                                # 长读事务开始
    r.execute("SELECT COUNT(*) FROM t").fetchone()    # 获得快照

    w.execute("BEGIN")
    w.executemany("INSERT INTO t(v) VALUES(?)", [("x" * 100,) for _ in range(20000)])
    w.execute("COMMIT")
    wal_grow = os.path.getsize(db + "-wal")
    print("读事务挂起时写入 2 万行: WAL 文件 %d 字节" % wal_grow)

    # 检查点被挡: 读事务钉住旧快照, 新页无法并入主库
    busy, log_pages, ckpt_pages = w.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    print("TRUNCATE 检查点: busy=%d (1 即被挡), 主库只推进 %d/%d 页"
          % (busy, ckpt_pages, log_pages))

    r.execute("COMMIT")                               # 读事务结束
    busy, log_pages, ckpt_pages = w.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    wal_after = os.path.getsize(db + "-wal")
    print("读者结束后: busy=%d, WAL 文件 %d 字节" % (busy, wal_after))
    print("结论: WAL 里被长读事务引用的旧版本页一个都不能删, 事务挂多久 WAL 涨多久;")
    print("      排查口诀: WAL 异常肥大 -> 先找最长事务, 再谈 checkpoint 参数")
finally:
    w.close()
    r.close()
    shutil.rmtree(tmp, ignore_errors=True)
