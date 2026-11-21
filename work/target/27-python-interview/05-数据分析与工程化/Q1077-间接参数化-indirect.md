---
title: [Q1077] 间接参数化 indirect
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1077 · 间接参数化 indirect

> 难度:★★★★ | 标签:pytest, parametrize

**问**:`@pytest.mark.parametrize("db", ["prod", "staging"], indirect=True)` 的 indirect 到底做了什么?

**答**:普通参数化把值直接传给测试函数;`indirect=True` 把值先传给同名 fixture 的 `request.param`,由 fixture 决定怎么用这个参数构造资源,测试函数拿到的还是 fixture 返回值。意义在于"参数化的是资源的构造方式,而不是资源本身":同一个测试函数,不同环境、不同后端的初始化差异全部封装在 fixture 里。适合环境矩阵、数据库后端矩阵这类"参数改变 setup"的场景,保持测试体零分支。

```python
# file: code/05_数据分析与工程化/q1077_indirect_parametrize.py

FIXTURES = {}

def fixture(name):
    def deco(fn):
        FIXTURES[name] = fn
        return fn
    return deco

@fixture("db")
def db_fixture(request):
    # indirect=True 时,参数化值通过 request.param 进入 fixture
    env = request.param
    return {"engine": "sqlite", "env": env}

def parametrize(argname, values, indirect=False):
    cases = []
    for v in values:
        if indirect:
            fake_request = type("R", (), {"param": v})()
            cases.append((argname, FIXTURES[argname](fake_request)))
        else:
            cases.append((argname, v))
    return cases

if __name__ == "__main__":
    # pytest 中:@pytest.mark.parametrize("db", ["prod", "staging"], indirect=True)
    for name, value in parametrize("db", ["prod", "staging"], indirect=True):
        print(name, value)
```

**追问**:
- 追问 1:partial indirect 怎么写?—— `indirect=["db"]` 只对列表内参数走 fixture,其余仍直接传入,适合混合参数。
- 追问 2:fixture 里怎么拿到 parametrize 的 id?—— `request.node.callspec.id`,可用于日志与按 id 跳过。
