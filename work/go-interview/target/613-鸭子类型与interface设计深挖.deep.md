# 613 鸭子类型与 interface 设计 深挖

> 覆盖源 6-13 全文：鸭子类型语义 + Go 是否 OO + 函数式vs OO 本质 + interface 隐式实现示例。主卡已给机制总览，本附录做 interface 设计技巧与隐式实现陷阱。

## 思路与架构

```text
鸭子类型落地
├─ 设计: 小接口(1~3 方法) 易满足 → 如 io.Reader/Writer
├─ 陷阱: 值/指针接收者方法集差异、nil 接口 vs nil 具体类型
└─ 选型: 鸭子类型(行为) vs 显式继承(Java) — Go 走前者
```

## 方案取舍
- **小接口优先**：方法越少越易"被鸭子式满足"，标准库 io.Reader/io.Writer 即典范；大接口反而束缚实现方 [经验]。
- **值 vs 指针接收者**：指针接收者方法不在值类型方法集中，赋接口时易漏实现；统一用指针接收者更稳 [经验]。
- **nil 接口陷阱**：接口变量 nil ≠ 底层具体类型 nil；具体类型 nil 赋给接口后接口非 nil，易在判空/panic 上踩坑。

## 答题技巧
- 被问"Go 接口和 Java 区别"先答隐式实现（方法集匹配、无声明），再补编译器转换与 nil 陷阱 [经验]。
- 主动边界到 `615-interface-two-impls`(隐式实现机制)、`615-go-oop`(组合优于继承)，构成接口全栈 [边界]。

## 细节与核心 API

```go
// Go 是结构化类型（鸭子类型）：只要方法集匹配即实现接口，无需声明 implements
type Reader interface { Read(p []byte) (int, error) }
type MyReader struct{}
func (MyReader) Read(p []byte) (int, error) { return 0, nil }
var _ Reader = MyReader{} // 编译期断言：MyReader 实现 Reader
// 小接口（1~3 方法）是 Go 风格：io.Reader/io.Writer/io.Closer 组合出大能力
// 空接口 interface{} 可装任何值，但失去编译期约束（Go 1.18+ 优先用泛型约束）
// 指针接收者方法不提升给值类型：*T 实现接口不代表 T 实现（反之亦然）
```
