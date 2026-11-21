---
title: [Q2617] 描述符查找顺序的完整矩阵:data、non-data 与实例字典
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2617 · 描述符查找顺序的完整矩阵:data、non-data 与实例字典

> 难度:★★★★☆ | 标签:描述符, 属性查找, 数据描述符

**问**:实例属性、数据描述符、非数据描述符同时存在时,`obj.x` 到底找到谁?

**答**:查找优先级由描述符是否定义 `__set__` 决定,形成清晰矩阵:**数据描述符**(定义了 `__get__` 和 `__set__`)永远压过实例字典——`property`、带 `__set__` 的自定义描述符、成员描述符都属于这类,这就是 property 永远拦截不了赋值失败原因的根源;**非数据描述符**(只有 `__get__`)则相反,会被实例字典里的同名属性覆盖——函数、`functools.cached_property` 是这类,所以往实例上写同名属性就能「顶掉」方法。类层面则沿 MRO 查找。这四层顺序是:类型 MRO 上的数据描述符 > 实例 `__dict__` > 类型 MRO 上的非数据描述符 > 类属性。读懂这张表,property、cached_property、方法绑定的行为差异全都能推出来。

```python
# file: code/01_语言核心与底层/q2617_descriptor_matrix.py
"""描述符查找矩阵:数据描述符压制实例字典,非数据描述符被压制。"""


class DataDesc:
    """数据描述符:定义了 __set__,永远优先于实例字典。"""

    def __get__(self, obj, owner=None):
        return "来自数据描述符"

    def __set__(self, obj, value):
        raise AttributeError("数据描述符拒绝写入")


class NonDataDesc:
    """非数据描述符:只有 __get__,会被实例字典同名属性覆盖。"""

    def __get__(self, obj, owner=None):
        return "来自非数据描述符"


class Host:
    dd = DataDesc()
    nd = NonDataDesc()


if __name__ == "__main__":
    h = Host()
    print("dd 实例访问:", h.dd)                  # 数据描述符
    print("nd 实例访问:", h.nd)                  # 非数据描述符

    h.__dict__["nd"] = "实例字典的值"
    print("nd 写入实例字典后:", h.nd)            # 被实例字典覆盖
    print("nd 类访问:", Host.nd)                 # 类访问仍走描述符

    try:
        h.dd = "试试写"
    except AttributeError as exc:
        print("dd 赋值被拦:", exc)

    print("dd 在实例 __dict__ 里塞值也无效:")
    h.__dict__["dd"] = "塞不进去的值"
    print("dd 仍是:", h.dd)
```

**追问**:1) 为什么 `cached_property` 是非数据描述符而不是数据描述符?——它只在首次访问时往实例 `__dict__` 写缓存,之后靠实例字典命中返回,定义为非数据描述符才能让缓存写入生效。2) 完整查找矩阵?——类 MRO 的数据描述符 > 实例 __dict__ > 类的非数据描述符/类属性 > __getattr__(Q451/452);slots 类没有实例 __dict__,cached_property 失效;self 写回让描述符「自我消亡」。3) 设计启示?——「可被实例字典覆盖」是非数据描述符的特征(方法可被实例属性遮蔽——同名实例属性盖方法);cached_property 并发行为分版本(3.8-3.11 类级写锁,3.12 起 gh-90459 移除,见 Q452)。4) 生产陷阱?——同名实例属性盖掉方法(隐蔽行为变化);slots + cached_property 组合崩;并发 miss 重复计算。
