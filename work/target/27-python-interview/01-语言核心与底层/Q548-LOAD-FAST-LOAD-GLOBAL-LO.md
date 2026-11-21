---
title: [Q548] LOAD_FAST/LOAD_GLOBAL/LOAD_DEREF:名字查找的字节码
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q548 · LOAD_FAST/LOAD_GLOBAL/LOAD_DEREF:名字查找的字节码

> 难度:★★★★ | 标签:字节码, 作用域

**问**:同样是读变量,为什么字节码有三种 LOAD?3.11 的自适应指令又做了什么?

**答**:编译期已确定每个名字的类别:局部变量 LOAD_FAST(按槽位索引,数组寻址最快);闭包变量 LOAD_DEREF(经 cell 对象间接寻址);全局/内置 LOAD_GLOBAL(查两层数字典,最慢)。这正是「局部快、全局慢、内置更慢」性能准则的字节码根源——把全局函数存成局部别名(local_len = len)的经典优化就是减少 LOAD_GLOBAL。3.11 起自适应解释器会把热点的 LOAD_GLOBAL 特化为带缓存版本(缓存版本索引),大幅降低字典查找成本,但语义分类不变。LOAD_NAME 只出现在模块与类体(动态命名空间)。

```python
# file: code/01_语言核心与底层/q548_name_opcodes.py
import dis

GLOBAL = "global value"

def outer():
    enclosed = "enclosed value"

    def inner(local_param):
        local_var = local_param + 1
        return (local_var, enclosed, GLOBAL, len)

    return inner

if __name__ == "__main__":
    for ins in dis.get_instructions(outer()):
        if ins.opname.startswith("LOAD") or ins.opname in {"STORE_FAST", "RETURN_VALUE"}:
            print(f"{ins.offset:4d} {ins.opname:16s} {ins.argrepr}")

    print("call result:", outer()(1))
```

**追问**:1) 为什么 LOAD_FAST 最快?——局部变量在帧对象的固定数组里,按编译期索引直接取,没有哈希与查找;LOAD_GLOBAL 即使带缓存也要处理 globals 与 builtins 两级回退。2) 三种查找的失败模式?——LOAD_FAST 未绑定抛 UnboundLocalError(槽在值不在);LOAD_GLOBAL 走 globals→builtins 两级,缺失 NameError;LOAD_DEREF 对应闭包 cell,未绑定有专门错误。3) 3.11+ 的优化?——自适应解释器给 LOAD_GLOBAL/LOAD_ATTR 加 inline cache;LOAD_FAST_LOAD_FAST 组合指令连续取两个局部,指令数与分派成本双降。4) 生产陷阱?——循环内反复取模块级名字,应先绑定到局部变量;shadowing builtins(list=str)让全局查找命中错误对象;热函数把全局常量搬进默认参数或局部。
