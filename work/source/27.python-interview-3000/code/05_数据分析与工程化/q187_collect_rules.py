class TestCart:
    # 类名必须以 Test 开头,且不能定义 __init__
    def test_total(self):
        assert 2 + 2 == 4

    def helper(self):
        # 没有 test_ 前缀,不会被当作测试收集
        return "helper"

def test_top_level():
    assert TestCart().helper() == "helper"
