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
