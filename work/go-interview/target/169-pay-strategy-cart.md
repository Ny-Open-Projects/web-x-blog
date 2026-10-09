# 169 策略模式实战：购物车多支付方式

> 分类：设计模式 / 行为型 | 难度：L2 | 题型：实现题 | 频率：高 | 关键词：**策略模式**/**支付策略接口**/**上下文持有策略**/**运行期切换**/**nil 防御**

> 原文锚点：第 2~14 段「PayStrategy 接口 → 三种支付实现 → 购物车上下文 → 结账」

## 一句话总述
用策略模式模拟多支付方式四步走：① 定义**支付策略接口**（PayStrategy，一个 Pay 方法）；② 信用卡/支付宝/微信各自实现该接口；③ **上下文（购物车）只持有接口类型字段**并暴露 SetPayStrategy 运行期换策略；④ 结账方法调用策略的 Pay——新增支付方式不改购物车代码，只加一个实现体。

## 面试官视角
策略模式是「手写设计模式」题的第一名。考官看三层：① 接口与实现体的分离是否干净（面向接口而非具体类型）；② **上下文怎么持有与切换策略**（字段 + setter，还是参数注入）；③ **边界处理**——策略未设置就结账怎么办。多数人只答到第一层；主动报 nil 防御与「为何不用 switch」的，直接进入设计讨论而非背诵考核。

## 主问答
**Q（面试官原话）：** 使用策略模式模拟实现多种支付方式？

1. **定义策略接口**：`PayStrategy interface { Pay(amount string) }`——所有支付方式的统一契约，购物车只认识它。
2. **三个具体策略**：CreditCard（卡号+CVV）、AliPay（账号+密码）、WeChatPay（OpenID）各自实现 Pay——打印各自的特征信息（金额+卡号/账号/OpenID）。**每种支付方式的知识全部封装在自己的实现体里**。
3. **上下文持有策略**：购物车结构体内嵌 `strategy PayStrategy` 字段 + `SetPayStrategy(s)`——**运行期随时换策略**，购物车代码零改动。
4. **结账与 nil 防御**：Checkout 前判断 `strategy == nil`——未设置就提示「支付策略未设置」，否则空指针 panic。这是源文案例里最容易被忽略、生产里最常见的雷。
5. **使用流程**：构造信用卡策略 → `cart.SetPayStrategy(cc)` → `cart.Checkout()`；换支付宝只需再 Set 一次——**「同一上下文，行为随策略切换」**即是策略模式的全部价值。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 策略模式解决什么问题？ | 说不清算法族可互换、消 if-else |
| L2 | 四个角色怎么落地？ | 接口/三实现/上下文/调用串不起来 |
| L3 | 怎么在运行期切换？ | 说不清上下文字段 + Set 方法 |
| L4 | 策略未设置怎么办？ | 说不清 nil 判断与防御 |
| L5 | 和直接 switch 支付方式比好在哪？ | 说不清新增方式不改老代码的开闭收益 |

## 版本与兼容性
| 主题 | 说明 |
|------|------|
| 接口实现 | Go 隐式实现：策略体无需声明 implements，解耦更彻底 |
| 策略注入 | setter 注入（可换）/ 构造注入（不可换）/ 函数类型注入（轻量） |
| 并发注意 | 上下文字段被并发 Set 时需加锁或保证串行 |
| nil 防御 | 结账前判 strategy == nil，防 panic |

## 关键代码
```go
type PayStrategy interface {
	Pay(amount int) string
}

type CreditCard struct{ CardNo string }

func (c CreditCard) Pay(amount int) string {
	return fmt.Sprintf("信用卡支付 %d 分, 卡号 %s", amount, c.CardNo)
}

type WeChatPay struct{ OpenID string }

func (w WeChatPay) Pay(amount int) string {
	return fmt.Sprintf("微信支付 %d 分, openID %s", amount, w.OpenID)
}

// Cart 上下文: 只认识 PayStrategy 接口, 运行期可换
type Cart struct {
	strategy PayStrategy
	total    int
}

func (c *Cart) SetPayStrategy(s PayStrategy) { c.strategy = s }

func (c *Cart) Checkout() string {
	if c.strategy == nil { // nil 防御: 策略未设置
		return "支付策略未设置"
	}
	return c.strategy.Pay(c.total)
}
```

## 总结与追问预判
核心：**接口契约 + 多实现体 + 上下文持策略字段 + Set 运行期切换；nil 策略必须防御**。追问常拐向「和工厂/状态模式的区别」「策略怎么注册与选择」——模式概念的立论与「策略主动选、状态被动变」见 `163-strategy.md`，工厂 what vs 建造者 how 见 `168-builder-pattern-roles.md`，设计模式全景见 `163-design-patterns.deep.md`，上下文持有与注入方式的取舍深挖见 `169-strategy-context-tradeoffs.deep.md`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文「配方法」= Pay 方法的音转、「crv」=CVV、「calculatetitle」=calculateTotal、「编载类/信付卡」等音转已按规范重写。
2. 事实核校： [经验] 原文说购物车「汇总结账之前需要判断支付策略是否为 new」——判断正确但未说明后果；不判断将空指针 panic（接口 nil 时调方法），本卡补齐该防御的工程动机。
