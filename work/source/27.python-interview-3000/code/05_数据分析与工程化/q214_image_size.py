def estimate_size(base_mb: float, layers_mb: list[float]) -> float:
    # 镜像大小 = 基础镜像 + 各层(已删文件不会减小历史层)
    return base_mb + sum(layers_mb)

def test_deleted_file_still_in_layer():
    # 经典坑:同一镜像里先装 300MB 再删,层仍占 300MB
    assert estimate_size(120, [300]) == 420
    # 合并 RUN 并同层清理后才是真瘦身
    assert estimate_size(120, [40]) == 160
