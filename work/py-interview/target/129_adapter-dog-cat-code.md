# 129. 适配器实战：用 setattr 把狗叫猫叫统一成 make_noise

> 分类：编程范式/设计模式 | 难度：L3 | 题型：代码题 | 频率：中 | 关键词：**setattr** / **接口统一** / **make_noise** / **适配器**
> 原文锚点：第 29~37 段「Dog 有 bark、Cat 有 meow，适配器用 ditupupdate 把二者统一成 make_noise」

## 一句话总述
原文的经典例子：有 `Dog.bark()` 和 `Cat.meow()` 两个**不同名**方法，用**适配器**把它们统一成 `make_noise()`，调用方无需关心对象到底是狗还是猫——这正是适配器"接口转接"的核心价值。

## 面试官视角
- **考察意图**：考你能否**动手实现**一个适配器，并理解为什么用 `setattr` 动态挂方法比写死 `if isinstance` 更优雅。
- **P5** 能写出 Dog/Cat 两个类 + 适配器 / **P6** 能说出用 `setattr` **动态注入**统一方法名，避免 `if/else` 分支 / **P7** 能指出这种"运行时改属性"的隐患（掩盖错误、破坏封装），并给出更稳的**显式方法转发**写法 `[经验]`。
- **红旗**：① 用 `if isinstance(x, Dog)` 硬分支而非统一接口；② 把 `setattr` 写成字面字符串拼错；③ 适配器里重写业务逻辑（越权）。
- **惊艳点**：`setattr(obj, 'make_noise', obj.bark)` 把**绑定方法**挂到新名字上，调用 `make_noise()` 即触发原 `bark`。验证：同一循环遍历狗和猫都调 `make_noise()` 不报错 `[实测]`。

## 主问答
**Q：写个适配器，让狗和猫都能用 make_noise() 叫？**
**A：**
1. **结论**：定义 `Dog.bark` 与 `Cat.meow`，再写一个适配器，把二者**重映射到统一方法名** `make_noise`。
2. **机制**：适配器用 `setattr` 把 `make_noise` **动态指向**被适配对象的原有方法（狗→bark，猫→meow），调用方只认 `make_noise`。
3. **边界**：这种动态挂方法**不利于静态检查**；更稳的做法是适配器里写显式 `def make_noise(self): return self._a.bark()`，可读性更好。
**加分层**：生产里更推荐**组合 + 显式转发**，而非 `setattr` 运行时改属性，避免隐藏 bug。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 这例子干嘛用 | 概念 | 接口统一 | 换题 → 不及格 |
| L2 | setattr 作用 | 机制 | 动态挂方法 | 判 P5 |
| L3 | 不用 setattr 怎么写 | 替代 | 显式转发 | 判 P6 |
| L4 | setattr 隐患 | 风险 | 破坏封装/难查 | 判 P6+ |
| L5 | 真实接入旧接口 | 深入 | 旧 SDK 适配 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 全版本 | setattr 内置稳定 | 用 setattr 动态注入 |
| Py3.7+ | dataclass 可简化 | 也可用属性转发 |
| 静态类型 | mypy 难推断 setattr | 显式转发更友好 |

## 关键代码
```python
class Dog:
    def bark(self): return "汪"
class Cat:
    def meow(self): return "喵"

class Adapter:
    def __init__(self, obj, method):
        setattr(self, "make_noise", getattr(obj, method))  # 动态统一接口

animals = [Adapter(Dog(), "bark"), Adapter(Cat(), "meow")]
print([a.make_noise() for a in animals])     # ['汪', '喵'] —— 统一调用
```

## ⚠️ 原文纠错
原文示例逻辑清晰（狗 bark、猫 meow，适配器统一为 `make_noise`），予以保留。机翻"ditupupdate方式"经语义重建为 **`setattr`**（动态设置属性），"macnoise/magnology"为 **`make_noise`**，"设备器类"为**适配器类**。原文示例用 `setattr(self, 'macnoise', dog.bark)` 动态挂方法，卡面给出可运行代码并补出"显式转发更安全"的工程建议。无事实错误，仅术语需还原。

## 总结与追问预判
- 适配器让**异名方法统一**；`setattr` 是动态实现手段，但**显式转发更稳**。
- 下一题：**外观模式**（130）、**适配器本质**（128）。
