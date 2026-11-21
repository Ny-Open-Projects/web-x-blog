"""环境漂移检查:对比生产与开发依赖清单,差异分级输出修复建议"""

PROD = {
    "pandas": "1.5.3", "numpy": "1.24.4", "requests": "2.31.0",
    "pydantic": "1.10.12",
}
DEV = {
    "pandas": "2.1.1", "numpy": "1.24.4", "requests": "2.31.0",
    "pydantic": "1.10.12", "pytest": "7.4.2", "ruff": "0.1.3",
}


def parse_ver(v):
    return tuple(int(x) for x in v.split("."))


def drift(prod, dev):
    rows = []
    for name in sorted(set(prod) | set(dev)):
        pv, dv = prod.get(name), dev.get(name)
        if pv is None:
            rows.append((name, "-", dv, "dev_only", "低:确认是否误装,或补进 prod 锁文件"))
        elif dv is None:
            rows.append((name, pv, "-", "prod_only", "高:dev 装不上会阻塞新人,补 dev"))
        elif parse_ver(dv) > parse_ver(pv):
            major_dev = dv.split(".")[0] != pv.split(".")[0]
            note = "高:主版本不一致,复现问题会失真" if major_dev else "中:小版本领先,收敛到同一锁文件"
            rows.append((name, pv, dv, "dev_newer", note))
        else:
            rows.append((name, pv, dv, "match", "一致"))
    return rows


if __name__ == "__main__":
    for name, pv, dv, kind, note in drift(PROD, DEV):
        print(f"{name:<10} prod={pv:<9} dev={dv:<9} [{kind}] {note}")
    print("要点:漂移根因是没共享锁文件;CI 里做依赖 diff 不一致直接红,主版本不一致的漂移会制造'本地好的线上坏'的幽灵问题")
