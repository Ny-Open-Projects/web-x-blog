"""幂等合并写:胜者规则与顺序无关,同批次重复执行结果不变"""

MASTER = {}


def merge(master, rows):
    """行格式 (key, value, version);version 大者胜,version 相同比 value 大者胜"""
    for key, value, version in rows:
        cur = master.get(key)
        if cur is None or (version, value) > (cur[1], cur[0]):
            master[key] = (value, version)


if __name__ == "__main__":
    A = [("u1", 100, 1), ("u2", 50, 1)]
    B = [("u1", 90, 2), ("u3", 70, 1)]
    m1, m2 = {}, {}
    merge(m1, A)
    merge(m1, B)          # 先 A 后 B
    merge(m2, B)
    merge(m2, A)
    merge(m2, A)          # A 重复执行一次
    print("顺序1 最终:      ", m1)
    print("顺序2(含重复)最终:", m2)
    print("幂等成立:", m1 == m2)
    print("要点:合并写幂等的本质是把'谁赢'定义成与执行顺序无关的全序比较(version+value),再加批次号挡重复提交")
