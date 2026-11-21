"""用纯逻辑模拟 gh-ost 三阶段: 建影子表 分批拷贝 回放增量 原子切换"""
import itertools

def migrate(rows, changelog, batch=2):
    # 1) 影子表: 结构即目标结构, 这里直接用列表模拟
    shadow = {}
    source = dict(rows)
    for i in range(0, len(source), batch):
        for k in itertools.islice(source.keys(), i, i + batch):
            shadow[k] = source[k] + "_migrated"          # 模拟结构转换
        # 2) 拷贝间隙回放 binlog 增量
        for op, k, v in changelog[:]:
            if k not in shadow:
                shadow[k] = v + "_migrated"
                changelog.remove(op and (op, k, v))
        print(f"已拷贝 {min(i + batch, len(source))} 行, 影子表 {len(shadow)} 行")
    # 3) 原子切换: 真实 gh-ost 是 RENAME TABLE 原表与影子表互换
    return shadow

if __name__ == "__main__":
    rows = [(k, f"row{k}") for k in range(1, 7)]
    changelog = [("insert", 7, "row7")]
    result = migrate(rows, changelog)
    print("切换后新表:", result)
