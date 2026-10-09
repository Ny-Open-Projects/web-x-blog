# 507 变长参数的局限与函数选项模式（Functional Options）

> 分类：Go 函数 | 难度：L3 | 题型：设计题 | 频率：中 | 关键词：**变长参数局限** / **顺序处理** / **函数选项模式** / **Functional Options** / **任意顺序**
> 原文锚点：第 25~32 段「变长参数须按序处理;如何任意顺序任意长度传参并识别参数→函数选项模式(后续章节详述)」

## 一句话总述
变长参数的硬伤是**必须按参数列表顺序逐一处理**，无法"任意顺序、任意长度"传参并识别"当前传的是哪个"。解决这类配置型需求的标准做法是**函数选项模式（Functional Options）**：把每个可选配置封装成 `func(*T)` 选项，调用时以任意顺序、任意数量传入，函数内部遍历应用，既灵活又类型安全。

## 面试官视角
- 意图：考察是否知道变长参数的局限，以及能否引出更优的配置 API 设计（Functional Options）。
- P5 知变长参数要按序；P6 知选项模式基本写法（Option=func(*T)）；P7 知选项模式 vs 变长参数的取舍、与构建者模式的关系。
- 红旗：把"任意顺序可选配置"硬塞进变长参数；或不知 Functional Options 这一惯用法。
- 惊艳点：点出"变长参数适合'同类型同角色多值'，选项模式适合'异构可选配置'"的边界 `[边界]` 见 507（变长参数规则）、162（工厂/构建者模式）。

## 主问答
**Q（面试官原话）：** 变长参数一定要按序传吗？怎么任意顺序传配置？
**A：**
1. **变长参数局限**：多个变长实参必须按位置顺序解析，难以表达"可选、可缺、可乱序"的配置语义。
2. **函数选项模式**：定义 `type Option func(*T)`，每个配置项是一个返回 Option 的函数；构造函数接收 `opts ...Option`，内部 `for _, o := range opts { o(s) }` 依次应用。
3. **任意顺序/任意长度**：调用方 `New(WithAddr(a), WithTimeout(d))` 顺序无关、可只传部分，类型安全且自文档化。
4. **取舍**：变长参数适合"同类型同角色的多值"（如 `append`、日志字段）；异构可选配置用 Functional Options 更清晰。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 变长局限 | 基础 | 须按序 | 判 P5 |
| L2 | 选项模式写法 | 设计 | Option=func(*T) | 判 P6 |
| L3 | 为何灵活 | 机制 | 遍历应用+顺序无关 | 判 P6+ |
| L4 | 与变长取舍 | 边界 | 同构多值 vs 异构配置 | 判 P7 |
| L5 | 与构建者 | 关联 | 选项模式即轻量构建者 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | 变长按序；Function Options 任意顺序可选配置 |

## 关键代码
```go
package main

import "time"

type Server struct {
	addr    string
	timeout time.Duration
}

// 函数选项模式：每个配置项封装成 func(*Server)
type Option func(*Server)

func WithAddr(a string) Option   { return func(s *Server) { s.addr = a } }
func WithTimeout(d time.Duration) Option { return func(s *Server) { s.timeout = d } }

// 任意顺序、任意长度传参
func NewServer(opts ...Option) *Server {
	s := &Server{addr: ":80"} // 默认值
	for _, o := range opts {
		o(s)
	}
	return s
}

func main() {
	_ = NewServer(WithAddr(":8080"), WithTimeout(time.Second)) // 顺序无关
}
```

## 总结与追问预判
- 变长参数须按序、适合同构多值；异构可选配置用 Functional Options（Option=func(*T)）更优。
- 预判：变长参数规则 → 见 507；切片展开与编译期 → 见 507；工厂/构建者 → 见 162-*。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：变长参数须按序处理、函数选项模式(Functional Options)解决任意顺序任意长度传参、Option=func(*T) 遍历应用——均正确，未做更正。
