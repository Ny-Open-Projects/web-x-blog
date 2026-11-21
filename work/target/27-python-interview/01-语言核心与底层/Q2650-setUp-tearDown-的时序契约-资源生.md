---
title: [Q2650] setUp/tearDown 的时序契约:资源生命周期与 addCleanup
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2650 · setUp/tearDown 的时序契约:资源生命周期与 addCleanup

> 难度:★★☆☆☆ | 标签:unittest, fixture, 资源管理

**问**:setUp 和 tearDown 在什么时机执行?tearDown 一定会跑吗?

**答**:unittest 对每个测试方法执行完整的「setUp -> test -> tearDown」周期:多个测试方法时 setUp/tearDown **各执行多次**,方法之间互不共享实例状态,这保证了测试独立性。tearDown 的契约是:只要 setUp 成功返回,即使测试断言失败,tearDown 也会执行——它承担资源兜底;但 setUp 本身抛错时 tearDown 不会跑,setUp 里已创建的资源要靠 `self.addCleanup(fn)` 注册的清理函数收尾(addCleanup 的清理在 tearDown 之后仍会全部执行,按注册逆序)。实践建议:易抛错的初始化放 setUp,但对应清理用 addCleanup 双保险;跨方法共享的昂贵资源不要放 setUp,用模块级或 `setUpClass`。

```python
# file: code/01_语言核心与底层/q2650_setup_teardown.py
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
```

**追问**:1) setUp 里创建了两个资源,第一个成功第二个失败怎么办?——tearDown 不会执行,但 setUp 中已通过 addCleanup 注册的清理仍会运行,所以「创建一个、立刻 addCleanup 一个」是安全模式。2) 时序契约?——setUp → 测试 → addCleanup(LIFO)→ tearDown;setUp 失败时只有已注册 cleanup 跑;cleanup 逆序执行(Q448 同理)。3) 与 pytest fixture 的对照?——fixture yield 后代码等价 cleanup;yield 前失败同样要部分清理(fixture 内 try/finally);addCleanup 比 tearDown 更细粒度。4) 生产陷阱?——tearDown 没跑资源泄漏(未 addCleanup);cleanup 顺序错(依赖先后);setUp 部分失败被吞成测试错误。
