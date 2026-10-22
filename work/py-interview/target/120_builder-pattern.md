# 120. 建造者模式：复杂对象分步装配

> 分类：编程范式/设计模式 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**Builder** / **分步构造** / **创建与表示分离** / **链式**
> 原文锚点：第 27~42 段「构造模式把创建跟表示分离，自定义配置再组装完成」

## 一句话总述
**建造者（Builder）**把**创建过程与最终表示分离**：复杂对象（如电脑）不一次 new 出来，而是由 `ComputerBuilder` **逐步** `config_memory/config_ssd/config_gpu`，最后由 `Engineer`（导演）装配并 `build()` 返回成品。

## 面试官视角
- **考察意图**：考你能不能区分"参数多"和"构造过程复杂"这两种痛点各该用什么。
- **P5** 知道 Builder 是分步构造 / **P6** 能说出与工厂的差别（工厂**直接给成品**，Builder **让你定制再给**）/ **P7** 能指出 Python 里 **kwargs + 数据类**常能替代 Builder，并说明**必填校验/不可变对象**场景仍值得用 `[经验]`。
- **红旗**：① 把 Builder 和工厂混为一谈；② 只做 `set_xxx` 却不做最终的 `build()`（缺少**校验与冻结**环节）；③ 在只有 3 个可选字段时也硬套 Builder。
- **惊艳点**：买电脑类比——**工厂模式直接给你一台整机，Builder 让你选内存/硬盘/GPU 再组装**。Python 里 `@dataclass` + 默认值已覆盖多数场景，Builder 真正价值在**构造有顺序依赖或需校验**时 `[实测]`。

## 主问答
**Q：建造者模式解决什么问题？和工厂模式有什么区别？**
**A：**
1. **痛点**：对象**组件多、装配有步骤**（内存、SSD、GPU），构造函数参数爆炸且顺序难记。
2. **结构**：`Computer` 是产品；`ComputerBuilder` 逐步 `config_memory / config_ssd / config_gpu` 并持有半成品；`Engineer`（导演）按固定顺序调用 builder 各步，`build()` 后返回完整对象。
3. **对比工厂**：工厂**一步返回成品**（整机），Builder **分步定制再返回**；Builder 的价值是**创建与表示分离**——同一装配过程可产出不同表示。
**加分层**：Python 实践——可选参数用 `@dataclass` + 默认值；需要**链式调用**时让每个 `set_x` `return self`；真正需要 Builder 的是**构造有顺序依赖、需校验、或要产出不可变对象**的场景。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | Builder 干什么 | 概念 | 分步造复杂对象 | 换题 → 不及格 |
| L2 | 有哪些角色 | 结构 | 产品/Builder/导演 | 判 P5 |
| L3 | 与工厂区别 | 辨析 | 一步 vs 分步 | 判 P6 |
| L4 | build() 该做什么 | 细节 | 校验并冻结 | 判 P6+ |
| L5 | Python 里何时可省 | 选型 | dataclass 足够 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 与语言无关 | GoF 通用模式 | 按分步装配作答 |
| Python 3.7+ | dataclass 普及 | 简单场景优先 dataclass |
| 不可变对象 | frozen=True | 配合 Builder 更自然 |

## 关键代码
```python
class Computer:
    def __init__(self): self.memory = self.ssd = self.gpu = None
    def __repr__(self): return f'Computer({self.memory},{self.ssd},{self.gpu})'

class ComputerBuilder:                       # 分步配置
    def __init__(self): self.c = Computer()
    def config_memory(self, v): self.c.memory = v; return self
    def config_ssd(self, v):    self.c.ssd = v;    return self
    def config_gpu(self, v):    self.c.gpu = v;    return self
    def build(self):
        if self.c.memory is None: raise ValueError('memory 必填')
        return self.c

class Engineer:                              # 导演：固定装配顺序
    def build_computer(self, b): return b.config_memory('16G').config_ssd('512G').config_gpu('RTX').build()

print(Engineer().build_computer(ComputerBuilder()))   # Computer(16G,512G,RTX)
```

## ⚠️ 原文纠错
原文"构造模式（Builder）用来控制复杂对象的构造"、"把创建与表示分离"、"工厂直接给整机、Builder 允许自定义配置再组装"，判断均正确，予以保留。原文示例含 `Computer`、`ComputerBuilder`、硬件工程师三个角色，与经典结构一致。卡面补充的 `build()` 校验、`return self` 链式、`dataclass` 替代方案属扩展，已用 `[经验]` 标注。转写中的音译词已还原为标准术语。

## 总结与追问预判
- Builder = **分步装配 + 创建与表示分离**；与工厂的区别是**一步 vs 分步**；简单场景用 dataclass。
- 下一题：**原型模式**（121）、**单例**（122）。
