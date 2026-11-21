"""setUp/tearDown 时序:addCleanup 兜底 setUp 中途失败。"""
import io
import unittest


class ResourceTest(unittest.TestCase):
    def setUp(self):
        print("  setUp")
        self.log = ["open"]
        self.addCleanup(self._close)      # 逆序执行,先于 tearDown 收尾注册的资源

    def _close(self):
        print("  addCleanup: close")
        self.log.append("closed")

    def tearDown(self):
        print("  tearDown, log =", self.log)

    def test_first(self):
        print("  test_first")

    def test_second(self):
        print("  test_second")
        self.assertEqual(1, 2)            # 失败也不影响清理


if __name__ == "__main__":
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=0)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(ResourceTest))
    print("测试数:", result.testsRun, "失败数:", len(result.failures))
    print("清理函数全部执行,失败用例也完成了资源兜底")
