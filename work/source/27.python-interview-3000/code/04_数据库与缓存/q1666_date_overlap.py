"""日期区间重叠判断: 预订冲突检测的半开区间条件"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE booking(id INTEGER PRIMARY KEY, room TEXT, start_day TEXT, end_day TEXT);
INSERT INTO booking VALUES
 (1, 'A101', '2026-11-01', '2026-11-05'),
 (2, 'A101', '2026-11-08', '2026-11-10');
""")
# 约定: start_day 入住, end_day 退房, 退房当天可再订 => 半开区间 [start, end)

NEW_START, NEW_END = "2026-11-04", "2026-11-07"

# 错误写法: 只判断新预订的起点是否落在旧区间内, 包不住"新区间吞掉旧区间"
n = conn.execute(
    "SELECT COUNT(*) FROM booking WHERE room='A101' AND ? BETWEEN start_day AND end_day",
    (NEW_START,)).fetchone()[0]
print("错误条件命中:", n, "条; 若新区间起点在所有旧区间之外则会整体漏判")

# 正确条件: 旧起点 < 新终点 且 旧终点 > 新起点, 半开区间交叠
right = """SELECT id, start_day, end_day FROM booking
 WHERE room='A101' AND start_day < :e AND end_day > :s ORDER BY id"""
hits = conn.execute(right, {"s": NEW_START, "e": NEW_END}).fetchall()
print("正确条件命中:", hits)

# 边界验证: 旧 end_day 等于新 start_day 不冲突
touch = conn.execute(right, {"s": "2026-11-05", "e": "2026-11-08"}).fetchall()
print("11-05 入住(旧 end=5)不算冲突:", touch, "-> 半开区间端点相接不重叠")

def try_book(room, s, e):
    hit = conn.execute(
        "SELECT id FROM booking WHERE room=? AND start_day < ? AND end_day > ?",
        (room, e, s)).fetchone()
    if hit:
        return False, f"与现有预订 id={hit[0]} 冲突"
    cur = conn.execute(
        "INSERT INTO booking(room, start_day, end_day) VALUES(?,?,?)", (room, s, e))
    conn.commit()
    return True, f"预订成功 id={cur.lastrowid}"

print(try_book("A101", "2026-11-04", "2026-11-07"), "<- 与预订1重叠被拒")
print(try_book("A101", "2026-11-06", "2026-11-08"))
print("要点: 区间交叠判定 start < new_end AND end > new_start;")
print("      并发下单还要靠行锁串行化或 PG 的排他范围约束兜底, 只靠查后插必有竞态")
