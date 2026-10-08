# 166 抽象工厂：一次产出一族相关对象

> 分类：设计模式/创建型 | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**抽象工厂** / **产品族** / **风格一致性** / **Go 接口分层**
> 原文锚点：第 23~56 段「以家具为例：FurnitureFactory 接口含 CreateChair/CreateSofa，Modern/Classic 两工厂各产同风格椅+沙发，新增风格不改旧码」

## 一句话总述
抽象工厂定义"创建相关对象族的工厂接口"，一次调用产出一组相互依赖、风格一致的对象（如现代风椅子+沙发）；新增产品族只加新工厂，不动旧代码，契合开闭原则。

## 面试官视角
- 意图：确认候选人理解"产品族一致性"是抽象工厂与工厂方法的本质区别（红旗：把它当多个独立工厂方法的堆砌）。
- P5 能写出 Factory 接口 + 两工厂；P6 能说清"族一致性"（Modern 工厂绝不出 Classic 椅子）；P7 能指出单维度变化上抽象工厂=过度设计。
- 红旗：以为抽象工厂只是"很多工厂方法"；给单一产品维度硬上抽象工厂。
- 惊艳点：Go 里用接口嵌套（Chair/Sofa 都嵌入 Furniture）表达"族"，比 Java 的抽象类继承更轻。

## 主问答
**Q（面试官原话）：** 抽象工厂解决什么问题？Go 里怎么写家具这套？
**A：**
1. **结论**：抽象工厂保证"一次创建出来的对象属于同一族、风格一致"；核心是一个工厂接口，每个方法产族内一种产品，ConcreteFactory 实现整族。
2. **机制**：`FurnitureFactory` 接口含 `CreateChair()/CreateSofa()`；`ModernFactory` 返回 `ModernChair+ModernSofa`，`ClassicFactory` 返回 `ClassicChair+ClassicSofa`，客户端只依赖接口、不 new 具体类 `[源码]`。
3. **边界**：仅当"多产品需成套一致"时才用（如跨平台 UI、多风格家具）；单维度变化用工厂方法即可，套抽象工厂是过度设计 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 解决啥 | 概念 | 产品族一致性 | 判 P5 |
| L2 | Go 怎么写 | 会用 | 工厂接口+两实现 | 判 P5+ |
| L3 | 与工厂方法 | 区别 | 族 vs 单产品 | 判 P6 |
| L4 | 新增风格 | 开闭 | 只加工厂不改旧 | 判 P6+ |
| L5 | 何时过度 | 实战 | 单维度别上它 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 无版本依赖 | 无 | 抽象工厂与语言版本无关；Go 用接口+结构体实现，无需继承 `[经验]` |

## 关键代码
```go
// 示意，未验证：抽象工厂（家具族）
type Furniture interface{ Style() string }
type Chair interface{ Furniture; HasLegs() bool }
type Sofa interface{ Furniture; HasCushions() bool }

type FurnitureFactory interface {
    CreateChair() Chair
    CreateSofa() Sofa
}

type ModernFactory struct{}

func (ModernFactory) CreateChair() Chair { return ModernChair{} }
func (ModernFactory) CreateSofa() Sofa  { return ModernSofa{} }

type ClassicFactory struct{}

func (ClassicFactory) CreateChair() Chair { return ClassicChair{} }
func (ClassicFactory) CreateSofa() Sofa   { return ClassicSofa{} }
```

## 总结与追问预判
- 抽象工厂=一工厂产一族、保证风格一致；新增族只加工厂。
- 预判：单产品变化 → 见 166-factory-comparison（工厂方法）；三者选型 → 见 166-three-factories。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对抽象工厂接口分层（Furniture/Chair/Sofa + FurnitureFactory）与"新增风格不改旧码"的开闭性；仅做了 ASR 解码将多组 Go 标识符与设计模式术语音译为崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
