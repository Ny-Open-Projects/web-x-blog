---
title: [Q1834] __set_name__ 当调试钩子:实例复用的早期报警
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1834 · __set_name__ 当调试钩子:实例复用的早期报警

> 难度:★★★☆☆ | 标签:__set_name__, 调试, 元编程

**问**:Q453 讲了 __set_name__ 给描述符传名,不写描述符时它能当什么调试钩子?

**答**:__set_name__(self, owner, name) 在类体创建时对每个该类实例调用一次,传回「我被挂到了哪个类的哪个名字上」——这本身就是登记与报警的钩子。极简 Field 用 slot 属性记录首次归属:同一 Field 实例第二次被挂名(复用)立即抛错——「多个属性共用一个声明对象」是声明式 DSL 里的真实 bug,共享状态会让两个属性互相污染;3.9 会把 __set_name__ 里的异常包成 RuntimeError、原 TypeError 挂在 __context__,demo 把两层都打出来。配合用途:自动派生数据库列名(类属性名即列名)、构建 owner 级注册表校验命名规范,全部不需要 metaclass,错误左移到 import 期被 CI 拦截。

```python
# file: code/01_语言核心与底层/q1834_set_name_alarm.py
"""__set_name__ 当调试钩子:实例复用的早期报警。"""


class Field:
    def __set_name__(self, owner, name):
        prev = getattr(self, "slot", None)
        if prev is not None:
            raise TypeError("Field 实例被复用: " + prev + " 与 " + name)
        self.slot = name
        self.owner = owner.__name__

    def describe(self):
        return self.owner + "." + self.slot


class Article:
    id = Field()
    title = Field()


def reuse_alarm():
    shared = Article.id                    # 反面用法:把已归属的实例再挂到新类
    try:
        type("Comment", (), {"body": shared})
    except RuntimeError as e:
        # 3.9 会把 __set_name__ 里的 TypeError 包成 RuntimeError,原异常在 __context__
        return str(e)[:42] + " | 原因: " + str(e.__context__.__class__.__name__)
    return "没拦住"


if __name__ == "__main__":
    print("id 归属:", Article.id.describe(), "| title 归属:", Article.title.describe())
    print("复用报警:", reuse_alarm())
```

**追问**:1) 为什么错误要左移到类创建时?——类体错误在 import 期暴露、CI 拦截;留到实例化才发现,排查要绕一大圈。2) __set_name__ 当调试钩子的模式?——描述符在 __set_name__ 里校验命名规范、字段冲突、实例复用(模块级单例描述符挂两个名字 Q453);抛错即 import 失败,错误左移。3) 与其他声明期钩子的分工?——__init_subclass__ 管类级约束、__set_name__ 管字段级、__class_getitem__ 管参数化;三者都在「定义期」拦截。4) 生产陷阱?——钩子抛错让整个模块 import 失败(报错信息要带类名与字段名);误报阻止合法用法;与 lint 规则重复,团队要定优先级。
