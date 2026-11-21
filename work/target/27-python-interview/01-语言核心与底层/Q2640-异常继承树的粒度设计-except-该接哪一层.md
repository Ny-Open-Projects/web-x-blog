---
title: [Q2640] 异常继承树的粒度设计:except 该接哪一层
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2640 · 异常继承树的粒度设计:except 该接哪一层

> 难度:★★★★☆ | 标签:异常设计, 继承, API 演化

**问**:自定义异常该建多深的继承树?调用方的 except 会不会因为加类而失效?

**答**:异常继承树是 API 契约的一部分:树太浅,调用方只能 `except AppError` 全收,无法区分处理;太深,每个调用点都要穷举分支。经验结构是三层:根基类(带 code、可序列化上下文)、按**处理方式**而非按模块分类的中层(NotFound、Conflict、Transient)、叶子具体异常。关键演化性质:except 按 isinstance 匹配,**在中间插入新父类不会破坏既有 handler**——只要新异常挂在调用方已捕获的祖先之下,老代码照常工作;反之把异常改挂到另一个分支才是破坏性变更。所以设计时先想「调用方会以哪几种方式反应」,再让继承树与反应方式对齐。

```python
# file: code/01_语言核心与底层/q2640_exception_tree.py
"""异常树粒度:三层结构、演化安全性与 handler 匹配。"""


class AppError(Exception):
    """根:所有业务异常的祖先,携带机器可读 code。"""
    code = "APP_ERROR"


class NotFound(AppError):
    code = "NOT_FOUND"


class UserNotFound(NotFound):
    code = "USER_NOT_FOUND"


class Transient(AppError):
    """中层的另一种维度:可重试。"""
    code = "TRANSIENT"


class RateLimited(Transient):
    code = "RATE_LIMITED"


def handle_user_missing(err):
    return f"按 NotFound 处理: {err.code}"


if __name__ == "__main__":
    err = UserNotFound("user 42")
    print(isinstance(err, NotFound), isinstance(err, AppError))
    print(handle_user_missing(err))

    # 演化:后来插入的中间类不破坏老 handler
    try:
        raise UserNotFound("still fine")
    except AppError as exc:                       # 老代码只认识 AppError
        print("老 handler 仍然接住:", exc.code)

    # 重试维度独立于存在维度,同一个异常可双重归类吗
    print("RateLimited 是 Transient:", issubclass(RateLimited, Transient))
    print("RateLimited 不是 NotFound:", not issubclass(RateLimited, NotFound))
```

**追问**:1) 一个异常能同时属于两个处理分支吗?——可以,多继承异常类(如 `class X(NotFound, Transient)`)让它被两类 handler 接住,但会模糊「该按哪种方式反应」,慎用。2) 粒度设计的原则?——异常继承树反映「处理方式的差异」而不是「错误语义的细分」;能同方式处理的合并、要不同反应的分层;底层异常保留语义信息,边界翻译(Q1558)。3) 与 except* 的配合?——ExceptionGroup 拆包时按类型分支,粒度决定拆分路径;嵌套组(Q469)要防「类型藏在子组」。4) 生产陷阱?——为每个错误码建类(爆炸)或一个 GodException(无差别);多继承异常让 except 顺序敏感;粒度与错误码映射(Q1817)脱节。
