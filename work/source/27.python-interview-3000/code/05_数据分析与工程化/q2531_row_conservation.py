"""目标表行数守恒断言: 输入 = 落表 + 去重 + 隔离, 差一行都不行"""


class ConservationError(Exception):
    """行数守恒被破坏"""


def check_chunks(chunks):
    """chunks: 每块 (读入, 落表, 去重丢弃, 隔离区); 逐块与总账双重校验"""
    total_read = total_out = 0
    for i, (read, written, dup, reject) in enumerate(chunks):
        if read != written + dup + reject:
            raise ConservationError(
                f"第 {i} 块守恒失败: 读入 {read} != 落表 {written} + 去重 {dup} + 隔离 {reject}"
                f", 差额 {read - written - dup - reject}")
        total_read += read
        total_out += written + dup + reject
    return total_read, total_out


if __name__ == "__main__":
    good = [(1000, 950, 30, 20), (1000, 990, 5, 5), (1000, 995, 3, 2)]
    read, out = check_chunks(good)
    print(f"正常批次: 读入 {read}, 支出 {out}, 守恒通过")
    assert read == out == 3000
    broken = good[:]
    broken[1] = (1000, 900, 0, 1)          # 中途丢行, 去重与隔离都没接住
    try:
        check_chunks(broken)
    except ConservationError as e:
        print("守恒断言拦截:", e)
    else:
        raise AssertionError("坏批次必须被拦截")
    print("要点: 守恒式把'数据去哪了'变成强制回答, 静默丢行在落地当场爆炸而不是月底对账才发现")
