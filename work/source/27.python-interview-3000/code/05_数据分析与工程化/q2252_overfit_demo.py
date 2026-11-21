"""过拟合直观演示: 多项式次数与验证误差的 U 形曲线"""

import random

random.seed(42)


def make_data(n, noise=0.8):
    xs, ys = [], []
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = 3 * x + 1 + random.gauss(0, noise)
        xs.append(x)
        ys.append(y)
    return xs, ys


def solve(A, b):
    """高斯消元求线性方程组, 部分主元"""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        p = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[p][col]) < 1e-12:
            return None
        M[col], M[p] = M[p], M[col]
        for r in range(col + 1, n):
            f = M[r][col] / M[col][col]
            for c in range(col, n + 1):
                M[r][c] -= f * M[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = M[r][n] - sum(M[r][c] * x[c] for c in range(r + 1, n))
        x[r] = s / M[r][r]
    return x


def polyfit(xs, ys, deg):
    A = [[sum(x ** (i + j) for x in xs) for j in range(deg + 1)] for i in range(deg + 1)]
    b = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(deg + 1)]
    return solve(A, b)


def sse(xs, ys, coef):
    return sum((y - sum(c * x ** i for i, c in enumerate(coef))) ** 2 for x, y in zip(xs, ys))


if __name__ == "__main__":
    train = make_data(12)
    valid = make_data(200, noise=0.8)
    results = []
    for deg in range(1, 8):
        coef = polyfit(train[0], train[1], deg)
        tr = sse(train[0], train[1], coef) / len(train[0])
        va = sse(valid[0], valid[1], coef) / len(valid[0])
        results.append((deg, tr, va))
    best = min(results, key=lambda r: r[2])
    print(f"{'次数':>4}{'训练误差':>10}{'验证误差':>10}")
    for deg, tr, va in results:
        mark = "  <- 验证最低" if deg == best[0] else ""
        print(f"{deg:>4}{tr:>10.3f}{va:>10.3f}{mark}")
    print("真函数是一次线性, 验证误差却在低次数处最低: 训练误差一路降而验证误差回升就是过拟合")
