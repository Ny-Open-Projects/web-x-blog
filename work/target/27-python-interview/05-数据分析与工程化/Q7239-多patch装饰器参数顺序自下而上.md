---
title: "[Q7239] 三个 @patch 叠在一起：参数顺序是自下而上，写反了照样跑"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7239 · 三个 @patch 叠在一起：参数顺序是自下而上，写反了照样跑

难度：P6 ｜ 标签：pytest、unittest.mock、patch、装饰器

基线：Python 3.12 标准库；用最小 patch 装饰器实现复现参数注入顺序。

**问**：一个测试同时 patch 了 HTTP 客户端、缓存、数据库三层，装饰器自上而下写 `@patch("app.http")`、`@patch("app.cache")`、`@patch("app.db")`，函数签名按同样顺序写成 `(mock_http, mock_cache, mock_db)`。测试全绿，直到某次线上 bug 需要断言「缓存没被写」，才发现断言一直打在数据库 mock 上。为什么写反了不报错？正确的顺序到底是什么？

**答**：
- **结论**：`@patch` 是装饰器，**最靠近函数的那个最先应用、最先注入**，于是参数顺序是**自下而上**（从里到外）。上面三个装饰器的注入顺序是 `app.db` → `app.cache` → `app.http`，函数签名必须写成 `(mock_db, mock_cache, mock_http)`。写反了不会报错，因为三个参数都是 `MagicMock`，类型相同、位置参数照样绑定，只是语义全错——断言打在了另一个 mock 上，而 `MagicMock` 对任何属性访问和调用都返回新 mock，不会抛异常。
- **取舍**：① 新代码优先用 `with patch(...) as a, patch(...) as b:`，顺序是**从左到右**，可读性远好于堆叠装饰器；② 用 `pytest-mock` 的 `mocker.patch`，不需要注入参数，通过 `mocker.patch("app.db")` 拿返回值，顺序问题消失；③ 必须用装饰器时，给 mock 参数起**带模块名的名字**（`mock_db`、`mock_http`），并在测试开头加一行注释写明注入顺序。
- **实战**：① 断言前先 `assert mock_db.call_count == 0` 之类的"负向断言"，能立刻暴露打错对象；② 用 `autospec=True` 让 mock 校验签名，签名不符会报错（对"参数顺序写反"仍然无效，但能挡住参数名错误）；③ Code Review 时把"装饰器顺序 vs 参数顺序"当成固定检查项；④ 更根本的做法是**依赖注入**：把 db/cache/http 作为构造参数传入，测试直接传 fake，不用 patch 路径（路径一变测试就碎）。

```python
"""复现 @patch 的注入顺序：自下而上；写反了不报错但断言打错对象。"""
import functools


class Mock:
    def __init__(self, target: str) -> None:
        self.target = target
        self.calls: list[tuple] = []

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        return f"<{self.target} result>"

    def __repr__(self) -> str:
        return f"Mock({self.target})"


class _Patch:
    """既能当装饰器、也能当上下文管理器，模拟 unittest.mock.patch。"""

    def __init__(self, target: str) -> None:
        self.target = target
        self.mock: Mock | None = None

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(Mock(self.target), *args, **kwargs)
        return wrapper

    def __enter__(self) -> Mock:
        self.mock = Mock(self.target)
        return self.mock

    def __exit__(self, *exc) -> bool:
        return False


def patch(target: str) -> _Patch:
    return _Patch(target)


@patch("app.http")
@patch("app.cache")
@patch("app.db")
def test_correct(mock_db, mock_cache, mock_http):
    print("正确签名 ->", mock_db, mock_cache, mock_http)
    return mock_db, mock_cache, mock_http


@patch("app.http")
@patch("app.cache")
@patch("app.db")
def test_swapped(mock_http, mock_cache, mock_db):
    print("写反签名 ->", mock_http, mock_cache, mock_db)
    print("  名为 mock_http 的参数实际指向:", mock_http.target)
    return mock_http, mock_cache, mock_db


if __name__ == "__main__":
    db, cache, http = test_correct()
    print("  db 是 db:", db.target == "app.db")
    print("  http 是 http:", http.target == "app.http")

    wrong_http, _, _ = test_swapped()
    print("  对它做 assert_called_once -> 实际检查的是:", wrong_http.target, "\n")

    # with 写法：顺序从左到右，肉眼可核对
    with patch("app.db") as m_db, patch("app.cache") as m_cache:
        print("with 写法 ->", m_db, m_cache, "| 顺序即书写顺序")
    print("结论：装饰器参数自下而上；能不用堆叠就不用，用 mocker.patch 更省心")
```

**追问一**：为什么 `MagicMock` 不会因为"参数名对不上"而报错？

→ 解析：装饰器注入的是**位置参数**，不是关键字参数，函数签名里的形参名只是本地名字，绑定位置即可，名字叫什么它根本不关心。`MagicMock` 又对任意属性访问返回子 mock、对任意调用都成功，所以"把 cache 的 mock 当 db 用"不会有任何异常，只有断言逻辑悄悄失效。`autospec=True` 能校验**被 patch 对象的签名**（调用参数个数/名字不对会抛 TypeError），但它不知道你函数形参的命名意图，仍然救不了顺序写反。

**追问二**：函数里又用 `@pytest.mark.parametrize` 时，patch 注入的参数和参数化参数谁在前？

→ 解析：`patch` 注入的参数**总是追加在最前面**（因为它是最外层包装先加参数），`parametrize` 的参数按名字绑定、位置无所谓（pytest 用关键字传参）。所以常见写法是 `def test_x(mock_db, mock_cache, case_id, expected)`：mock 在前、parametrize 在后；但如果你把 parametrize 的参数写成位置依赖的形式（比如通过 fixture 的 `request.param`），顺序又会互相干扰。最稳的约定：**mock 参数永远放最左，业务参数一律关键字或 fixture 注入**。
