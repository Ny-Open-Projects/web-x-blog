"""导出文件的行列上限保护: 超限拒导, 贴近上限预警"""

XLSX_MAX_ROWS = 1048576
XLSX_MAX_COLS = 16384
WARN_RATIO = 0.9


class ExportTooLarge(Exception):
    """导出规模超过格式硬上限"""


def guard_export(n_rows, n_cols):
    if n_cols > XLSX_MAX_COLS:
        raise ExportTooLarge(f"列数 {n_cols} 超过 xlsx 上限 {XLSX_MAX_COLS}, 请裁列或改 CSV/Parquet")
    if n_rows > XLSX_MAX_ROWS:
        raise ExportTooLarge(
            f"行数 {n_rows} 超过 xlsx 上限 {XLSX_MAX_ROWS}, 可选: 1 改 CSV/Parquet 2 按日期分片 3 服务端聚合后导出")
    ratio = n_rows / XLSX_MAX_ROWS
    if ratio >= WARN_RATIO:
        return "warn", ratio
    return "ok", ratio


if __name__ == "__main__":
    try:
        guard_export(2_000_000, 20)
    except ExportTooLarge as e:
        print("超限拦截:", e)
    else:
        raise AssertionError("超上限必须拒绝导出")
    status, ratio = guard_export(1_000_000, 30)
    print(f"百万行导出: {status}, 已用上限 {ratio:.1%}, 预警线 {WARN_RATIO:.0%}")
    assert status == "warn"
    status, ratio = guard_export(500_000, 30)
    print(f"50 万行导出: {status}, 余量充足")
    assert status == "ok"
    print("要点: 上限保护要在生成文件之前做, 拒绝信息必须给出替代方案, 别让用户拿到半截文件")
