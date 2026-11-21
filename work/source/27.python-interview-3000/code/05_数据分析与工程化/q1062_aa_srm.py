
def srm_chi2(observed, expected):
    total_o, total_e = sum(observed), sum(expected)
    exp_scaled = [e * total_o / total_e for e in expected]
    return sum((o - e) ** 2 / e for o, e in zip(observed, exp_scaled))

chi = srm_chi2([4800, 5200], [1, 1])
print(f"SRM 卡方 = {chi:.2f},阈值 3.84 -> {'SRM 异常,停实验排查' if chi > 3.84 else '正常'}")
print("AA 测试:两个对照组对同一指标做两比例检验,p 应 >= 0.05")
print("AA 显著或 SRM 报警都指向平台问题,而不是业务效应")
