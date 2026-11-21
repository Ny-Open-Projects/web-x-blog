---
title: [Q146] 事务 ACID 与 InnoDB 的实现
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q146 · 事务 ACID 与 InnoDB 的实现

> 难度:★★★ | 标签:MySQL, 事务

**问**:请解释事务的 ACID 四个特性,并说明 InnoDB 分别靠什么机制实现?

**答**:原子性靠 undo log,事务失败时按回滚日志逆向补偿;持久性靠 redo log 与 WAL 机制,先写日志再刷数据页,宕机后可重放恢复;隔离性靠锁 + MVCC 共同实现;一致性是最终目的,由前三者加上主键、外键等约束共同保证。面试时强调"一致性是结果,其余三个是手段"是加分项。

```python
# file: code/04_数据库与缓存/q146_acid_transaction.py
"""用 pymysql 演示转账事务:任一步失败整体回滚,保证原子性"""
import contextlib

TRANSFER_OUT = "UPDATE account SET balance = balance - %s WHERE id = %s AND balance >= %s"
TRANSFER_IN = "UPDATE account SET balance = balance + %s WHERE id = %s"


def get_conn():
    import pymysql  # pip install pymysql
    return pymysql.connect(
        host="127.0.0.1", user="root", password="", database="demo",
        autocommit=False, charset="utf8mb4",
    )


@contextlib.contextmanager
def transaction(conn):
    """标准事务上下文:正常提交,异常回滚并向上抛出"""
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def transfer(conn, src: int, dst: int, amount: int) -> None:
    with transaction(conn), conn.cursor() as cur:
        n = cur.execute(TRANSFER_OUT, (amount, src, amount))
        if n == 0:
            raise ValueError("余额不足或账户不存在, 主动抛出触发回滚")
        cur.execute(TRANSFER_IN, (amount, dst))


if __name__ == "__main__":
    try:
        conn = get_conn()
    except Exception as exc:  # 本地无 MySQL 时给出提示, 逻辑本身自洽
        print("无可用 MySQL, 仅演示:", exc)
    else:
        try:
            transfer(conn, src=1, dst=2, amount=100)
            print("转账成功")
        except Exception as exc:
            print("转账失败已回滚:", exc)
        finally:
            conn.close()
```

**追问**:
- 为什么不能用两条独立 UPDATE 代替事务?——两条语句之间宕机或失败会造成钱"凭空消失",只有事务能保证原子性。
- autocommit=True 时还用显式开启事务吗?——需要,用 `START TRANSACTION` 或框架的 transaction 上下文,把多条语句绑定成一个原子单元。

---
