# 105. classmethod vs staticmethod：一个拿 cls，一个什么都不拿

> 分类：编程范式/Python 类 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**classmethod** / **staticmethod** / **cls** / **代码组织**
> 原文锚点：第 54~60 段「classmethod 第一个参数是类本身，staticmethod 跟普通函数几乎一样」

## 一句话总述
两者都能用 `类名.方法()` 调用；**`@classmethod`** 首参是**类本身 `cls`**（可读写类变量、可作工厂），**`@staticmethod`** **不接收 `self`/`cls`**，只是把一个普通函数**放进类的命名空间**做代码组织。

## 面试官视角
- **考察意图**：考"什么时候必须用它"，尤其是**替代构造器**这个真实场景。
- **P5** 能说出一个拿 cls 一个不拿 / **P6** 举出 `classmethod` 做**工厂方法**（`from_xxx`）的例子 / **P7** 能指出 `classmethod` **绑定到类**、子类调用时传入的是**子类**，而 `staticmethod` 无此行为 `[源码]`。
- **红旗**：① 认为 `staticmethod` 也能访问类变量（它拿不到 `cls`，只能硬编码类名）；② 把两者都叫"类方法"混为一谈；③ 说不出任何使用场景。
- **惊艳点**：`classmethod` 的最大价值是**替代构造器 + 支持继承**——子类调用时 `cls` 是子类，`Child.from_str()` 直接返回 Child 实例；`staticmethod` 做不到。验证：父子类各调一次 `type(obj)` 即可看出差异 `[实测]`。

## 主问答
**Q：classmethod 和 staticmethod 有什么区别？分别什么时候用？**
**A：**
1. **classmethod**：首参 `cls` 指向**类本身**，可引用/修改**类变量**；典型用途是**工厂方法**（如 `Person.from_birth_year`），且**子类调用时 `cls` 是子类**。
2. **staticmethod**：不接收 `self`/`cls`，跟普通函数几乎一样，只是**放在类里做代码组织**、给它一个命名空间；如原文中的 `get_full_name` 没引用类的任何东西。
3. **调用**：两者都能通过 `类名.方法()` 或 `实例.方法()` 调用；实例调用时 `classmethod` 传入的是该实例所属的类。
**加分层**：判据很简单——**函数体里需不需要类（类变量/构造实例）**；需要就用 `classmethod`，完全不需要就 `staticmethod`，否则直接写成模块级函数更清爽。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 两者区别 | 概念 | 有无 cls | 换题 → 不及格 |
| L2 | staticmethod 能访问类变量吗 | 机制 | 不能，需硬编码类名 | 判 P5 |
| L3 | classmethod 用来干嘛 | 应用 | 工厂方法 | 判 P6 |
| L4 | 子类调用时 cls 是谁 | 深入 | 子类 | 判 P6+ |
| L5 | 何时两者都不用 | 选型 | 用模块级函数 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 2.2+ | 两个装饰器引入 | 现代代码均可用 |
| Python 3.9+ | 可叠加 @property | 组合用法较新，慎用 |
| 描述符协议 | 两者都是描述符 | 可解释绑定行为 |

## 关键代码
```python
class Person:
    country = "China"
    def __init__(self, name): self.name = name

    @classmethod
    def from_str(cls, s):            # cls 可用于构造
        return cls(s.split(",")[0])

    @staticmethod
    def full_name(a, b):             # 不碰类，纯组织用
        return f"{a}{b}"

class Student(Person): pass
print(type(Person.from_str("老王,18")))    # <class 'Person'>
print(type(Student.from_str("小李,20")))   # <class 'Student'> —— cls 是子类
```

## ⚠️ 原文纠错
原文"classmethod 第一个参数是类本身，它可以引用类变量；staticmethod 使用起来跟普通函数几乎一样，只是放在类里组织一下"，描述准确，予以保留。原文把 `staticmethod` 的动机归纳为"出于代码组织的需要"、把 `classmethod` 归纳为"使用类变量的需要"，卡面补充了**工厂方法与子类 `cls` 绑定**这一更关键的场景，已用 `[源码]`/`[实测]` 标注。转写中的音译词已还原为标准术语。

## 总结与追问预判
- 需要类 → **`@classmethod`**（工厂 + 继承友好）；不需要 → **`@staticmethod`**（纯组织）。
- 下一题：**元类与 type**（106）、**类变量 vs 实例变量**（103）。
