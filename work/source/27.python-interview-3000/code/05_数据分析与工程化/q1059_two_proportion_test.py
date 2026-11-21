import math

def two_proportion_z(c1, n1, c2, n2):
    p1, p2 = c1 / n1, c2 / n2
    p = (c1 + c2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return z, p_value

z, p = two_proportion_z(120, 5000, 150, 5000)
print(f"p1={120/5000:.2%} p2={150/5000:.2%} 相对提升 {(150/5000)/(120/5000)-1:+.1%}")
print(f"z = {z:.3f}, p = {p:.4f}")
print("结论:", "显著,B 组更优" if p < 0.05 and 150 > 120 else "不显著,不能拒绝原假设")
