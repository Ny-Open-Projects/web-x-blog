"""Q2862 容量的压力分级:水位评级 滞回与预案联动。

容量治理不能等到打挂才反应:按利用率划等级,每级绑定一组预案动作
(砍批处理 收窄模型 收紧准入);升级即时,降级要留滞回区,防止水位
在阈值附近来回抖动导致预案反复横跳。
"""

LEVELS = [
    (60, "L0", []),
    (80, "L1", ["batch_shed"]),
    (95, "L2", ["batch_shed", "small_model_only"]),
    (10 ** 9, "L3", ["batch_shed", "small_model_only", "queue_reject"]),
]


def level_by_util(u):
    for th, name, actions in LEVELS:
        if u < th:
            return name
    return "L3"


def evaluate(u, current_idx):
    """返回新等级索引:升级即时,降级需低于上一档阈值再减 5。"""
    target = 0
    for i, (th, _, _) in enumerate(LEVELS):
        if u < th:
            target = i
            break
    if target > current_idx:
        return target
    if target < current_idx:
        down_threshold = LEVELS[current_idx - 1][0] - 5
        if u < down_threshold:
            return target
        return current_idx
    return current_idx


def main():
    seq = [70, 85, 97, 91, 70, 50]
    idx, trail = 0, []
    for u in seq:
        idx = evaluate(u, idx)
        trail.append(LEVELS[idx][1])
    assert trail == ["L1", "L2", "L3", "L3", "L1", "L0"], trail
    # 91 时按水位本应回 L2,滞回挡住了抖动;70 才真正降级
    assert evaluate(91, 2) == 2, evaluate(91, 2)
    assert evaluate(70, 2) == 1, evaluate(70, 2)
    # 等级与预案一一对应
    assert LEVELS[2][2] == ["batch_shed", "small_model_only"]
    print("利用率序列:", seq)
    print("等级轨迹:", trail, "(91 处滞回生效,未回落)")
    print("L2 预案:", LEVELS[2][2])


if __name__ == "__main__":
    main()
