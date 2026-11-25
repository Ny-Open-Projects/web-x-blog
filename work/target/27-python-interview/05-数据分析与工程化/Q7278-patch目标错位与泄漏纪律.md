---
title: "[Q7278] Mock 悄悄漏到了下一个测试：patch 目标错位与恢复纪律"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7278 · Mock 悄悄漏到了下一个测试：patch 打错目标与恢复纪律

难度：P6 ｜ 标签：mock、patch 目标、where-to-patch、状态泄漏、上下文管理器

基线：Python 3.12；复现 patch 的"打错目标"（在定义处 patch 而非使用处）与"手动 start 忘 stop"两种经典事故，实现 patch 泄漏的探测断言与 ExitStack 嵌套纪律，全标准库实跑。

**问**：patch 了 `module.requests`，真实请求还是发出去了；或者用了 `mock.patch.object(...).start()` 后，后续所有测试的同一个函数全变假——patch 该打在哪个名字上？手动 start/stop 与装饰器/上下文管理器怎么选？怎么在测试里探测"patch 泄漏"？

**答**：
- **结论**：patch 的对象是**名字查找的绑定**，不是函数本身：`patch("a.requests")` 改的是模块 a 命名空间里的 `requests` 属性。经典错位：模块 a 里 `from util import fetch`，patch 打在 `util.fetch` 上，但 a 运行时查的是**自己命名空间的 `fetch`**（import 时已绑定）——真函数照样跑。正确姿势是 **patch 使用处**：`patch("a.fetch")`。判断口诀：**import 进来的名字 patch 使用方，`module.func` 形式调用的名字 patch 定义方**。泄漏事故的另一半是**手动 start/stop**：`patcher.start()` 忘了 `stop()`，替换物就留在模块命名空间里，污染后续所有测试——症状是"某个测试单独跑绿、跟在其他测试后面跑红"，与顺序耦合（Q7276）同病不同根。纪律：装饰器/上下文管理器优先（退出即恢复，结构保证），手动 start 只在 fixture 里用且 **yield 前注册 teardown**；嵌套三个以上 patch 用 ExitStack（Q448/Q2135）统一管理，避免装饰器参数顺序地狱（Q7239）。泄漏探测：测试入口断言关键名字的原始性——`func.__module__`/`isinstance(mock.Mock)` 检查，或在 fixture teardown 里断言 `patcher.stop()` 后目标已还原。
- **取舍**：① 装饰器 vs 上下文管理器 vs 手动：装饰器最省事但参数顺序反直觉（自下而上注入，Q7239），patch 多了函数签名爆炸；上下文管理器语义清晰但缩进加深；ExitStack 折中——patch ≥3 个的默认选择；② patch 粒度：patch 整个 `requests` 模块 vs patch `session.get`——粒度越粗泄漏面越大，能 patch 到具体方法不 patch 整模块；③ autoscale：`autospec=True` 让 mock 继承真实签名，打错目标/调用签名错当场暴露（Q7215 autospec 同族）——默认开启是防错位的最强单招；④ 泄漏探测的成本：每个测试入口全量探测有开销，折中是"关键模块注册表 + conftest 里的统一 teardown 断言"，只探测易泄漏的集成点。
- **实战**：① 团队规范：测试里禁止裸 `patcher.start()`——要么装饰器要么 fixture+yield；code review 检查项；② `mock.patch.object(obj, "attr")` 的 target 参数写"字符串点路径"时，路径解析在 import 时发生——动态导入的模块 patch 要延迟到运行时（`importlib` 后 patch），避免打在旧引用上；③ 泄漏急救：测试报告红但单跑绿时，先跑"二分顺序重放"（前一半套件 + 该测试）确认污染源，再 grep `patcher.start` 定位；④ 与 fixture 化 monkeypatch 的关系：pytest 的 monkeypatch fixture 自带恢复（Q194/Q1080），团队无特殊理由优先 monkeypatch 而非手搓 patcher。

```python
"""Q7278 patch 目标错位与泄漏: import绑定/使用处patch/泄漏探测断言。"""
import types


def fetch(url: str) -> str:
    """真实函数: 会发网络请求(演示用假实现)."""
    return f"REAL-RESPONSE-{url}"


# 模块 user_a: from util import fetch (import 时绑定到自己的命名空间)
user_a = types.ModuleType("user_a")
user_a.fetch = fetch                       # import 绑定: 复制了名字
user_a.__dict__["__real_fetch"] = fetch


def user_a_run(url: str) -> str:
    return user_a.fetch(url)               # 运行时查 user_a.fetch, 不是 util.fetch


def patch(module: types.ModuleType, name: str, repl) -> types.ModuleType:
    module.__dict__[name] = repl
    return module


def fake_fetch(url: str) -> str:
    return f"MOCK-{url}"


def is_leaked(module: types.ModuleType, name: str) -> bool:
    """泄漏探测: 目标名字仍指向 mock(未恢复)即泄漏."""
    impl = module.__dict__[name]
    return getattr(impl, "__name__", "").startswith("fake_") or \
        impl.__name__ == "fake_fetch"


if __name__ == "__main__":
    # 错位: patch 定义处 util.fetch, 但 user_a 已绑定自己的 fetch
    original = fetch
    patch(types.ModuleType("util"), "fetch", fake_fetch)   # 打到"另一个"命名空间
    r1 = user_a_run("http://x")
    print(f"patch 定义处(错位): user_a 调用 -> {r1}  <- 真函数还在跑")
    # 正确: patch 使用处
    patch(user_a, "fetch", fake_fetch)
    r2 = user_a_run("http://x")
    print(f"patch 使用处(正确): user_a 调用 -> {r2}")
    # 恢复 + 泄漏探测
    leaked_probe = is_leaked(user_a, "fetch")
    patch(user_a, "fetch", original)
    recovered = user_a_run("http://x")
    print(f"teardown 探测: 恢复前泄漏={leaked_probe}, 恢复后调用 -> {recovered}")
    ok = ("REAL" in r1 and "MOCK" in r2 and leaked_probe
          and "REAL" in recovered)
    print(f"校验: 错位复现 + 使用处patch生效 + 泄漏可探测 -> {'通过' if ok else '异常'}")
    print("结论：patch 的是名字绑定: import 进来的名字 patch 使用处;")
    print("      手动 start 必配 teardown; 泄漏症状='单跑绿连跑红'")
```

**追问一**：为什么 patch 一个被装饰器包装的函数或类方法时经常"打不上"或"行为怪异"？desc 元数据与绑定语义的坑在哪？

→ 解析：三类高频坑：① **装饰器包装**：`@functools.wraps` 的函数对象被替换的是装饰后的复合体，patch 打上去后 autospec 读到的签名是包装层的，`__wrapped__` 链上的真实参数可能对不上——mock 调用通过但真实逻辑没验到；解法是 patch 到**最内层可注入的接缝**（依赖注入把装饰逻辑留在使用方，Q1565 Seam 注入的同族思想），而不是 patch 装饰后的入口。② **类方法的绑定时机**：patch 类属性（`patch("cls.method")`）影响所有实例，但**已绑定方法**（`obj.method` 在 patch 前被引用保存）不受影响——lambda/闭包/函数引用缓存（Q2086 闭包捕获）里存着旧绑定，patch 永远追不上；教训：被测代码不要在模块级缓存方法引用。③ **只读命名空间**：内建模块、C 扩展的部分属性、`__slots__` 类的实例属性不可 patch——`patch("builtins.open")` 这类操作在某些实现下直接 AttributeError 或需要 `create=True` 绕过，而 create=True 又会把拼写错误静默变成"patch 了一个不存在的名字"（打上假名字，真名字继续跑，等于错位事故翻版）。总原则：**patch 的可靠前提是"名字查找在运行时经过被 patch 的命名空间"——任何绕开运行时查找的绑定（缓存、闭包捕获、C 层）都是 patch 的盲区，设计测试接缝时要把可替换性放进被测代码的结构里。**

**追问二**：多个 patch 嵌套时，装饰器参数顺序与退出顺序的规则是什么？ExitStack 为什么能根治"顺序地狱"？

→ 解析：装饰器形态：自下而上应用——`@patch(a) @patch(b) @patch(c) def t(ma, mb, mc)`，最先声明的 c 最先进入、最后退出（栈结构：离函数最近的装饰器先包裹），参数顺序恰好与声明顺序相反（Q7239 专卡），patch 到 5 个以上时人脑排序必错，错位注入的 mock 悄悄互换，测试"通过但验证错对象"。上下文管理器嵌套同理是 LIFO 退出。ExitStack 的根治逻辑：把 N 层嵌套**压平成栈注册**——`with ExitStack() as st: m1 = st.enter_context(patch(a)); m2 = st.enter_context(patch(b))`，进入顺序=书写顺序，退出由栈保证严格逆序，参数变量命名与业务对应而非与装饰器层级对应；patch 顺序在运行时显式可见，还能条件性注册（`if need_db: st.enter_context(...)`）——这是嵌套装饰器完全做不到的。配套纪律：ExitStack 内的 patch 与其他资源（临时目录、连接）统一入栈，teardown 一处收口，资源关闭顺序天然按依赖逆序（连接先关、目录后删）。一句话：**patch 嵌套超过两个，就从"装饰器语法问题"升级为"资源管理设计问题"，ExitStack 是唯一scale得住的答案。**
