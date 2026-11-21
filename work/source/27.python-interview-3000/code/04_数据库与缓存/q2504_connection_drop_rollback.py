"""连接中断后的事务命运: 没有提交, 就等于没有发生"""
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile

CHILD = """
import sqlite3, os, sys
db, mode = sys.argv[1], sys.argv[2]
conn = sqlite3.connect(db, isolation_level=None)
conn.execute("BEGIN IMMEDIATE")
conn.execute("INSERT INTO t(v) VALUES('from-child')")
if mode == "crash":
    os._exit(9)                # 模拟进程被杀: 没有任何清理机会
conn.execute("COMMIT")
print("child committed")
"""

tmp = tempfile.mkdtemp()
db = os.path.join(tmp, "crash.db")
try:
    setup = sqlite3.connect(db)
    setup.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
    setup.commit()
    setup.close()

    # 一次性: 事务内插入后被杀
    r = subprocess.run([sys.executable, "-c", CHILD, db, "crash"],
                       capture_output=True, text=True)
    after = sqlite3.connect(db)
    n = after.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    print("子进程在事务内被杀 (exit=%d): 库里行数=%d -> 未提交的写随连接消亡" % (r.returncode, n))
    assert n == 0

    # 对照: 正常提交
    r = subprocess.run([sys.executable, "-c", CHILD, db, "commit"],
                       capture_output=True, text=True)
    n = after.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    print("子进程正常提交 (exit=%d): 库里行数=%d" % (r.returncode, n))
    assert n == 1
    after.close()
    print("结论: 事务的原子性以连接生命周期兜底, 崩溃/断连/被杀都是隐式回滚;")
    print("      反过来说, 想让写入落袋必须显式 COMMIT, '没报错'不等于'已提交'")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
