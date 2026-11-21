
def reverse_twice(xs):
    return list(reversed(list(reversed(xs))))

try:
    from hypothesis import given, strategies as st
    HAS_HYP = True
except ImportError:
    HAS_HYP = False

if HAS_HYP:
    @given(st.lists(st.integers()))
    def test_reverse_twice(xs):
        assert reverse_twice(xs) == xs

    test_reverse_twice()
    print("hypothesis 随机生成 + 自动缩小,验证通过")
else:
    import random
    random.seed(0)
    for _ in range(300):
        xs = [random.randint(-100, 100) for _ in range(random.randint(0, 20))]
        assert reverse_twice(xs) == xs
    print("未安装 hypothesis,降级为随机 300 组性质验证,思想相同")
