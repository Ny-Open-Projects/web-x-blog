---
title: [Q539] bool 是 int 的子类:历史与推论
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q539 · bool 是 int 的子类:历史与推论

> 难度:★★☆☆ | 标签:类型系统, bool

**问**:True + True 为什么等于 2?这个历史设计带来哪些推论与坑?

**答**:bool 继承自 int(True==1, False==0),这是 Python 2 时代为兼容旧布尔语义保留的设计。推论:bool 可以做算术与索引([\"a\",\"b\"][True] 即下标 1);sum(x > 2 for x in ...) 是合法计数惯用法;True 在 dict 里与 1 是同一个键(哈希相同),`{True: "yes", 1: "no"}` 只剩一个键。坑在于「本想存布尔却与整数撞键」「isinstance(True, int) 为 True 干扰类型判断」。现代写法:计数用 sum(谓词) 没问题,但作为 dict 键或 JSON 出参时,显式转 int(x) 消除歧义。另外 `True == 1` 为真而 `True is 1` 恒为假:`is` 比较身份,只能用于 None/True/False 这类单例,值相等一律用 `==`;对字面量用 `is` 会触发 SyntaxWarning。

```python
# file: code/01_语言核心与底层/q539_bool_is_int.py
if __name__ == "__main__":
    print("issubclass:", issubclass(bool, int), "| isinstance:", isinstance(True, int))
    print("True + True:", True + True, "| True * 3:", True * 3)
    print("as index:", ["a", "b", "c"][True])

    print("count via sum:", sum(x > 2 for x in range(5)))

    d = {True: "yes", 1: "no"}
    print("True and 1 are the same key:", d)
    print(True == 1, True is 1)           # True False:== 相等推不出身份相同

    print(type(False).__name__, False == 0)
```

**追问**:1) 为什么 Python 不把 bool 改成独立类型?——改动会破坏海量依赖「布尔即 0/1」的存量代码与 C 扩展 ABI,收益不抵迁移成本,这是语言演进的保守性典型样本。2) bool 是 int 子类带来哪些推论?——True+True == 2、isinstance(True, int) 为 True;dict 键 True 与 1 冲突(True == 1 且哈希相同,后者覆盖前者)。3) 底层单例语义?——bool 只有两个实例 True/False,3.12 起 immortal 引用计数永不减;bool() 只返回这两个对象,int 子类只重写了 __repr__/__str__。4) 生产陷阱?——用 1/0 当布尔参与算术输出混淆;dict/序列把 True 与 1 当同一键;sum(list_of_bools) 计数虽妙但可读性差,团队约定要统一;pytest 参数化里 bool 与 int 混淆用例。
