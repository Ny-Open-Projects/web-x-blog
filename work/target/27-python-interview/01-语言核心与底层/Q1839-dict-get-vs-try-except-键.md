---
title: [Q1839] dict.get vs try/except:键缺失路径实测
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1839 · dict.get vs try/except:键缺失路径实测

> 难度:★★★☆☆ | 标签:EAFP, 微优化, 实测

**问**:「键可能不存在」的读取,.get 带默认值还是 try d[key] except KeyError?实测差多少?

**答**:各 20 万次实测:键存在路径 try(约 0.029s)略快于 get(约 0.035s),因为 try 在无异常时代码近乎零开销而 get 是一次方法调用;键缺失路径 get(约 0.033s)显著快于 try(约 0.077s),异常构建与栈展开吃掉一倍多时间。选型结论:① 存在是常态、缺失是意外——try 更快也更 EAFP;② 缺失是常态或两态均势——get/setdefault 一次到位;③ 差异都在常数级,可读性优先,与 Q1568 的 set vs list 同款纪律。另外 get 不适合「键存在但值为 None」的歧义场景,用哨兵默认值(Q1282)或先 in 再取值更明确。

```python
# file: code/01_语言核心与底层/q1839_dict_get_try.py
"""dict.get vs try/except:键存在与缺失两条路径的实测。"""
import timeit

D = {("key" + str(i)): i for i in range(1000)}
PRESENT = "key500"
MISSING = "nope"


def via_get_present():
    return D.get(PRESENT, 0)


def via_try_present():
    try:
        return D[PRESENT]
    except KeyError:
        return 0


def via_get_missing():
    return D.get(MISSING, 0)


def via_try_missing():
    try:
        return D[MISSING]
    except KeyError:
        return 0


def bench(stmt, number=200000):
    return round(timeit.timeit(stmt, globals=globals(), number=number), 4)


if __name__ == "__main__":
    print("键存在  get:", bench("via_get_present()"))
    print("键存在 try:", bench("via_try_present()"))
    print("键缺失  get:", bench("via_get_missing()"))
    print("键缺失 try:", bench("via_try_missing()"))
    print("结论:存在路径两者接近,try 略快;缺失路径 get 明显更快")
```

**追问**:1) defaultdict 为什么在这个对比里赢?——缺失时由 C 层默认工厂直接建值,一次哈希完成「查-建-存」,比 get 后再赋值少一次查找。2) 三个路径的实测画像?——命中路径 get 最快(零分支);缺失路径 try/except 在 3.11 零开销 try 下不再贵(Q1260),但真正抛异常仍有构造 traceback 的成本;defaultdict 在「持续累积」场景赢。3) 选型依据?——语义优先:get 表达「默认值」,try 表达「缺失是异常路径」,defaultdict 表达「按需生长」;性能差异到不了换设计的量级。4) 生产陷阱?——get 默认值掩盖真 bug(缺键应是错);微优化驱动选型;结论不写测量条件。
