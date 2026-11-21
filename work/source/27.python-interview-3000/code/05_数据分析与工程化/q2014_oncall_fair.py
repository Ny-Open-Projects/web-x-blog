"""值班表公平性:按累计加权负载挑人,节假日加倍计入"""

from datetime import date, timedelta

MEMBERS = ["Alice", "Bob", "Carol", "Dave"]
START = date(2026, 11, 2)      # 周一开始
WEEKS = 8
HOLIDAYS = {date(2026, 11, 26)}        # 含一个节假日
WEEKEND_W, HOLIDAY_W, NORMAL_W = 1.5, 2.0, 1.0


def week_load(day):
    total = 0.0
    for i in range(7):
        d = day + timedelta(days=i)
        if d in HOLIDAYS:
            total += HOLIDAY_W
        elif d.weekday() >= 5:
            total += WEEKEND_W
        else:
            total += NORMAL_W
    return total


def schedule(members, start, weeks):
    load = {m: 0.0 for m in members}
    shifts = []
    for w in range(weeks):
        week_start = start + timedelta(days=7 * w)
        person = min(members, key=lambda m: (load[m], members.index(m)))
        load[person] += week_load(week_start)
        shifts.append((f"第{w + 1}周({week_start})", person))
    return shifts, load


if __name__ == "__main__":
    shifts, load = schedule(MEMBERS, START, WEEKS)
    for week, person in shifts:
        print(f"{week}: {person}")
    print("累计加权负载:", load)
    spread = max(load.values()) - min(load.values())
    verdict = "公平" if spread <= 3 else "需要调班"
    print(f"负载极差 {spread:.1f} -> {verdict}")
    print("要点:节假日与周末权重更高,轮转看累计负载而不是按名单循环;调班必须记回负载账本,否则公平性账目失效")
