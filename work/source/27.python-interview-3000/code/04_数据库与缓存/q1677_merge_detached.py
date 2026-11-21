"""detached 实例合并: merge 把游离对象的状态拷贝进当前 Session"""
import sqlite3

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
    HAS_SQLA = True
except ImportError:
    HAS_SQLA = False

def demo_pure():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.execute("INSERT INTO users VALUES(1, 'alice', 20)")
    conn.commit()

    detached = {"id": 1, "name": "alice-new", "age": 21}   # 游离对象: 不挂在任何会话上
    session_cache = {}

    def merge(cache, obj):
        pk = obj["id"]
        if pk in cache:                       # 持久实例已在会话里 -> 就地合并
            target = cache[pk]
        else:
            row = conn.execute("SELECT id, name, age FROM users WHERE id=?", (pk,)).fetchone()
            target = {"id": row[0], "name": row[1], "age": row[2]}
            cache[pk] = target                # SELECT 载入后进入持久态
        target.update(obj)                    # 逐属性拷贝游离状态
        return target

    merged = merge(session_cache, detached)
    print("merge 返回的是会话内对象, 不是传入对象:", merged is not detached)
    conn.execute("UPDATE users SET name=?, age=? WHERE id=?",
                 (merged["name"], merged["age"], merged["id"]))
    conn.commit()
    print("flush 落库:", conn.execute("SELECT name, age FROM users WHERE id=1").fetchone())
    print("要点: merge 永远不会把传入对象本身挂进会话;")
    print("      危险点: 持久实例上未提交的修改会被游离对象的值静默覆盖; 主键不存在时按新增处理")

if HAS_SQLA:
    class Base(DeclarativeBase):
        pass

    class User(Base):
        __tablename__ = "users"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]
        age: Mapped[int]

    def demo_sqla():
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        with Session(engine) as s:
            s.add(User(id=1, name="alice", age=20))
            s.commit()
        detached = User(id=1, name="alice-new", age=21)   # 游离实例
        with Session(engine) as s2:
            merged = s2.merge(detached)                   # 发 SELECT 后逐属性拷贝
            print("merge 返回的是会话内对象:", merged is not detached)
            s2.commit()
        with Session(engine) as s3:
            u = s3.get(User, 1)
            print("落库:", u.name, u.age)

if __name__ == "__main__":
    if HAS_SQLA:
        demo_sqla()
    else:
        print("sqlalchemy 未安装, 用 sqlite3 等价演示 merge 语义")
        demo_pure()
