"""identity map 与缓存污染: 会话内主键唯一对象 与 外部直改造成的脏读"""
import sqlite3

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
    HAS_SQLA = True
except ImportError:
    HAS_SQLA = False

def demo_pure():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users VALUES(1, 'alice')")
    conn.commit()
    identity_map = {}

    def get(pk):
        if pk not in identity_map:
            row = conn.execute("SELECT id, name FROM users WHERE id=?", (pk,)).fetchone()
            identity_map[pk] = {"id": row[0], "name": row[1]}
        return identity_map[pk]

    a, b = get(1), get(1)
    print("同一主键返回同一对象:", a is b, "-> 会话内一份数据, 免重复 SQL 且保证一致")
    conn.execute("UPDATE users SET name='hacked' WHERE id=1")
    conn.commit()
    print("外部直改后 Session 视角仍是旧值:", get(1)["name"], "<- 这就是缓存污染")
    row = conn.execute("SELECT id, name FROM users WHERE id=1").fetchone()
    identity_map[1] = {"id": row[0], "name": row[1]}       # 等价 expire + refresh
    print("expire 后重读:", get(1)["name"])
    print("结论: identity map 的生命周期等于 Session; 长命 Session 期间任何绕过 ORM 的写入都表现为脏读")

if HAS_SQLA:
    class Base(DeclarativeBase):
        pass

    class User(Base):
        __tablename__ = "users"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]

    def demo_sqla():
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        with Session(engine) as s:
            s.add(User(id=1, name="alice"))
            s.commit()
            a = s.get(User, 1)
            b = s.get(User, 1)
            print("同一主键返回同一对象:", a is b)
            raw = engine.raw_connection()
            raw.execute("UPDATE users SET name='hacked' WHERE id=1")
            raw.commit()
            print("外部直改后 Session 视角:", s.get(User, 1).name, "<- identity map 命中, 未发 SQL")
            s.expire_all()
            print("expire_all 之后:", s.get(User, 1).name)
            raw.close()

if __name__ == "__main__":
    if HAS_SQLA:
        demo_sqla()
    else:
        print("sqlalchemy 未安装, 用 sqlite3 等价演示 identity map 机制")
        demo_pure()
