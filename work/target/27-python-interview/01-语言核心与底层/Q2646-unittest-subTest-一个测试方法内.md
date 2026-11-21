---
title: [Q2646] unittest.subTest:一个测试方法内的参数化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2646 · unittest.subTest:一个测试方法内的参数化

> 难度:★★★☆☆ | 标签:unittest, subTest, 测试设计

**问**:不用 pytest,unittest 怎么做到「一个用例里多个子场景,失败互不影响」?

**答**:`with self.subTest(**标记):` 把一段断言包成子用例:某个子用例失败会被记录并**继续执行后续子用例**,结束时一次性报告所有失败场景,而不是断言失败立刻终止整个方法。这就是 3.9 时代 unittest 的参数化姿势:配合循环覆盖多组输入,失败信息里带上子用例参数(如 `case=2`),定位比裸循环精确得多。注意边界:subTest 的失败计入同一个测试方法的结果(显示为该方法的失败,列出各子用例),setUp/tearDown 只执行一次,子用例之间共享实例状态——需要互相隔离的场景仍应拆成独立测试方法或用 `load_tests` 动态生成。

```python
# file: code/01_语言核心与底层/q2646_subtest.py
"""subTest:循环参数化,失败逐个记录互不阻断。"""
import io
import unittest


def slugify(text):
    """带一个已知瑕疵的实现,供特征对照。"""
    return text.strip().lower().replace(" ", "-")


class SlugifyTest(unittest.TestCase):
    CASES = [
        ("Hello World", "hello-world"),
        ("  Trim  ", "trim"),
        ("Multiple   Spaces", "multiple-spaces"),      # 当前实现会失败
    ]

    def test_cases(self):
        for text, expected in self.CASES:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)


if __name__ == "__main__":
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=0)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(SlugifyTest))
    print("失败数:", len(result.failures), "(失败场景已逐个列出,循环未中断)")
    for _, tb in result.failures:
        print(tb.splitlines()[0])
```

**追问**:1) subTest 失败后同方法内实例状态还可靠吗?——不可靠,所有子用例共享同一个 self,前一个失败可能污染后续断言,有状态用例必须拆方法。2) subTest 的定位?——同方法内参数化:失败逐一报告、其余继续跑;与 pytest.mark.parametrize 等价(报告粒度不同);无状态纯函数场景最合适。3) 与 setUp 的关系?——setUp 每「方法」一次不是每 subTest 一次;子用例需要独立初始化就在 subTest 内重建局部状态。4) 生产陷阱?——有状态用例共享 self(失败传染);subTest 内 try/except 吞失败(应让它自然上报);参数生成器耗尽问题(列表化)。
