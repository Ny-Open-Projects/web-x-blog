"""相关系数矩阵与共线性检查:Pearson 矩阵定位高相关对,VIF 手算确认"""

try:
    import pandas as pd
except ImportError:
    pd = None

# 列:面积, 房间数, 距地铁距离, 房价
COLS = [
    [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
    [800, 600, 500, 450, 400, 350, 300, 250, 200, 150],
    [200, 260, 300, 350, 390, 450, 500, 560, 620, 700],
]
NAMES = ["area", "rooms", "metro_dist", "price"]


def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    sx = sum((a - mx) ** 2 for a in xs) ** 0.5
    sy = sum((b - my) ** 2 for b in ys) ** 0.5
    return cov / (sx * sy)


def solve(A, b):
    """高斯消元解线性方程组(带列主元)"""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        for r in range(n):
            if r != col and M[col][col]:
                f = M[r][col] / M[col][col]
                for c in range(col, n + 1):
                    M[r][c] -= f * M[col][c]
    return [M[i][n] / M[i][i] for i in range(n)]


def vif(cols, idx):
    """VIF_i = 1/(1-R2):把第 idx 列当因变量,对其余列做最小二乘求 R2"""
    ys = cols[idx]
    others = [c for j, c in enumerate(cols) if j != idx]
    n = len(ys)
    X = [[1.0] + [c[i] for c in others] for i in range(n)]
    p = len(others) + 1
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(p)] for a in range(p)]
    Xty = [sum(X[i][a] * ys[i] for i in range(n)) for a in range(p)]
    beta = solve(XtX, Xty)
    yhat = [sum(beta[a] * X[i][a] for a in range(p)) for i in range(n)]
    my = sum(ys) / n
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    ss_tot = sum((v - my) ** 2 for v in ys)
    r2 = 1 - ss_res / ss_tot
    return 1 / (1 - r2) if r2 < 1 else float("inf")


if pd is None:
    print("标准库降级:Pearson 相关矩阵")
    print("        " + " ".join(f"{n:>10}" for n in NAMES))
    for i, a in enumerate(NAMES):
        row = [f"{pearson(COLS[i], COLS[j]):>10.3f}" for j in range(len(NAMES))]
        print(f"{a:>8} " + " ".join(row))
else:
    df = pd.DataFrame({n: c for n, c in zip(NAMES, COLS)})
    print(df.corr().round(3))
print("\nVIF(VIF>10 视为严重共线性):")
for i, name in enumerate(NAMES):
    print(f"  {name:<11} VIF = {vif(COLS, i):.1f}")
print("要点:相关矩阵看两两关系,共线性要看'能被其他列解释多少',rooms 与 area 高相关导致两者 VIF 都爆表,建模前要去一留一")
