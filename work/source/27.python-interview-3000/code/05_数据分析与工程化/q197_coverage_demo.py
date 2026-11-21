def grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "B"
    return "C"

def test_high_score():
    # 只有这一条测试时:line coverage 可能到 60% 以上
    # 但 branch coverage 会指出 elif 为假、以及最后的 return C 从未覆盖
    assert grade(95) == "A"

def test_all_branches():
    # 补齐分支后,branch coverage 才是 100%
    assert grade(75) == "B"
    assert grade(30) == "C"
