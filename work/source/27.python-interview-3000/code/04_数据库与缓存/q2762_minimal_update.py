"""列级最小更新: 脏检查后只把变过的字段写回去"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
c = conn.cursor()
c.execute("""CREATE TABLE profile (
    id INTEGER PRIMARY KEY, name TEXT, city TEXT, age INTEGER, bio TEXT)""")
c.execute("INSERT INTO profile VALUES(1, '旧名', '北京', 30, '一段很长的个人简介')")

old = dict(zip(("name", "city", "age", "bio"),
               c.execute("SELECT name, city, age, bio FROM profile WHERE id=1").fetchone()))
new = {"name": "新名", "city": "北京", "age": 30, "bio": "一段很长的个人简介"}

changed = {k: v for k, v in new.items() if old.get(k) != v}
print("整行更新要写 %d 列; 脏检查后只需写 %d 列: %s"
      % (len(new), len(changed), sorted(changed)))
if changed:
    sets = ", ".join("%s=?" % k for k in changed)
    c.execute("UPDATE profile SET %s WHERE id=1" % sets, tuple(changed.values()))
print("更新结果:", c.execute("SELECT name, city, age, bio FROM profile WHERE id=1").fetchone())
print("没有差异时干脆不发 UPDATE, 乐观锁版本号也不会空转")
conn.close()
