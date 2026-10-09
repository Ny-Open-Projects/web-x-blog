# 1610 Go 实现装饰器模式：四角色结构体版

> 分类：设计模式 / 结构型 | 难度：L2 | 题型：实现题 | 频率：高 | 关键词：**装饰器模式**/**组件接口**/**抽象装饰器**/**层层包裹**/**接口嵌入**

> 原文锚点：第 2~13 段「Component 接口 → 具体组件 → 抽象/具体装饰器 → 客户端层层装饰」

## 一句话总述
装饰器模式四角色在 Go 的落地：**组件接口**（Operation 契约）→ **具体组件**（原始实现）→ **抽象装饰器**（内嵌 `wrapped Component` 字段，Operation 默认委托）→ **具体装饰器 A/B**（嵌入抽象装饰器、重写 Operation 前后加行为）——客户端 `B(A(base))` 层层包裹，输出像洋葱一样叠加，**原组件代码零修改**。

## 面试官视角
162 号卡讲过装饰器的函数式形态（HTTP 中间件），这题考的是**经典四角色结构体版**——考官用它验证你是否懂模式的完整骨架而非只会闭包糖。三个采分点：① 抽象装饰器的**委托默认实现**为什么存在（让具体装饰器只重写关心的方法）；② 层层包裹的**调用顺序**（最外层先执行）；③ 能纠正「Go 继承」的表述——嵌入是组合，委托显式发生。

## 主问答
**Q（面试官原话）：** 如何使用 Go 实现装饰器模式？

1. **组件接口**：`Component interface { Operation() string }`——装饰前后的对象共用同一契约，这是「透明扩展」的根基。
2. **具体组件**：`ConcreteComponent` 实现基础功能——**永远不需要修改它**。
3. **抽象装饰器**：`BaseDecorator{ wrapped Component }` 持有被装饰对象，Operation 默认委托 `wrapped.Operation()`——具体装饰器嵌入它后，**只重写要扩展的方法**，其余自动继承委托行为。
4. **具体装饰器**：DecoratorA/DecoratorB 嵌入 BaseDecorator，各自在委托前后插入行为（[实测] A 前置加 `A(...)`、B 后置加 `B(...)`）。
5. **层层包裹**：[实测] 输出链——原始 `基础功能` → A 装饰后 `A(基础功能)` → `B(A(base))` 调用得 `B(A(基础功能))`；**调用顺序 = 最外层装饰器先执行、沿洋葱向内**。B 与 base 满足同一接口（[实测] 接口断言成立），客户端对装饰透明。
6. **与函数式形态的关系**：结构体版是教科书骨架（多方法契约/带状态扩展时用）；单方法接口的 Go 里 `func(Component) Component` 闭包版更轻（HTTP 中间件即此，见 `162-decorator.md`）——两形态对比见深卡。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 装饰器解决什么问题？ | 说不清不改原对象动态加职责 |
| L2 | 四个角色怎么落地？ | 串不起 接口/组件/抽象装饰器/具体装饰器 |
| L3 | 抽象装饰器存在的意义？ | 说不清委托默认实现、免重复代码 |
| L4 | B(A(base)) 的执行顺序？ | 说不清最外层先执行、洋葱模型 |
| L5 | 和代理/中间件的区别？ | 混淆三者控制权与意图差异 |

## 版本与兼容性
| 主题 | 说明 |
|------|------|
| 接口嵌入 | 具体装饰器嵌入抽象装饰器结构体，方法集自动提升 |
| 方法重写 | Go 无 override——外层方法**遮蔽**嵌入层同名方法 |
| 契约不变 | 装饰前后类型都满足 Component，客户端无感 |
| 层数 | 任意叠加；顺序敏感（洋葱模型） |

## 关键代码
```go
type Component interface{ Operation() string }

type BaseDecorator struct{ wrapped Component }

func (b BaseDecorator) Operation() string { return b.wrapped.Operation() } // 默认委托

type DecoratorA struct{ BaseDecorator }

func (d DecoratorA) Operation() string { return "A(" + d.wrapped.Operation() + ")" }

type DecoratorB struct{ BaseDecorator }

func (d DecoratorB) Operation() string { return "B(" + d.wrapped.Operation() + ")" }

// 客户端: B(A(base)) 层层包裹, 任意叠加
var c Component = DecoratorB{BaseDecorator{wrapped: DecoratorA{BaseDecorator{wrapped: ConcreteComponent{}}}}}
```

[实测] 输出：`B(A(基础功能))`；接口断言成立（装饰后仍是 Component）。

## 总结与追问预判
核心：**四角色骨架 + 抽象装饰器委托默认 + 具体装饰器遮蔽重写 + 洋葱式层层包裹；原组件零修改**。追问常拐向「和函数式中间件怎么选」「与代理模式的区别」（代理控制访问、装饰增强功能）——函数式与结构体式对比及代理边界见 `1610-decorator-two-forms.deep.md`，函数式形态主线见 `162-decorator.md`，策略/建造者等模式族见 `169-strategy-context-tradeoffs.deep.md`/`168-builder-pattern-roles.md`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文「类继承了组件接口」「利用继承的特性」表述失准——Go 无继承；抽象装饰器与具体装饰器之间是**结构体嵌入（组合）**，方法是**遮蔽**而非重写（多态分派不经嵌入发生）；「component/concentratecomponent/concarrotdoctor」等音转已规范为 Component/ConcreteComponent/ConcreteDecorator。
2. 事实核校： [经验] 原文说装饰器「允许向现有对象添加新功能同时不改变其结构」正确，但需补半句：前提是**客户端面向接口编程**——若客户端依赖具体类型，装饰器无法透明替换。
