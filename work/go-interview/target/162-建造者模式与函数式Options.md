# 162 建造者模式与函数式 Options

> 分类：设计模式/创建型 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**Options 模式** / **可变参数** / **默认值**
> 原文锚点：第 32~53 段「建造者分离构建与表示，参数多且有默认值用建造者」

## 一句话总述
建造者把复杂对象的构建过程和表示分离；Go 里最地道的形式是函数式 Options——`NewServer(opts ...Option)` 用闭包逐步设默认值，避免十几个构造参数。

## 面试官视角
- 意图：能否用 Options 模式解决"参数爆炸"且保留默认值与可扩展性。
- P5 知用可变参数设配置 / P6 说清 Option 是 `func(*T)` 闭包、零值默认 / P7 知 Options 的代价（每次调用一次闭包分配、无法编译期校验必填项）。
- 红旗：构造函数堆十几个参数；以为 Options 能强制必填字段。
- 惊艳点：`Option` 本质是 `func(*Config)`，遍历执行即可合并，默认值在构造里先写好，未传即保留 —— 验证：grpc.DialOption 同构，go1.26.5 `[经验]`。

## 主问答
**Q（面试官原话）：** 一个 struct 有十几个配置项，怎么写构造函数？
**A：**
1. **结论**：用函数式 Options：`New(opts ...Option) *T`，Option 为 `func(*T)`，构造体先填默认值再依次应用选项。
2. **机制**：每个 `WithX(v)` 返回闭包修改目标，调用方只传关心的项；未传项保留默认值，新增项不破坏旧签名 `[源码]`。
3. **边界**：Options 是可选配置机制，无法在编译期强制必填；强必填项应作为普通位置参数，不要塞进 Option。
**加分层：** Options 每次调用产生闭包分配，超高频创建路径若在意分配可改用 plain config struct，别盲目套。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | Options 干嘛 | 概念 | 变参配置 | 换题 |
| L2 | 怎么实现 | 会用 | func(*T) 闭包 | 判 P5 |
| L3 | 必填怎么管 | 边界 | 位置参数 | 判 P6 |
| L4 | 代价 | 权衡 | 闭包分配 | 判 P6+ |
| L5 | 对比 config | 实战 | struct vs 闭包 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.0 起稳定 | 无 | 函数式 Options 不依赖任何版本特性，长期成立 `[经验]` |

## 关键代码
```go
// 示意，未验证：函数式 Options
type Config struct{ Addr string; Timeout int }
type Option func(*Config)

func WithTimeout(t int) Option { return func(c *Config) { c.Timeout = t } }

func New(addr string, opts ...Option) *Config {
	c := &Config{Addr: addr, Timeout: 30} // 默认值
	for _, o := range opts { o(c) }
	return c
}
```

## 总结与追问预判
- 建造者=构建与表示分离；Go 用 Options 解决参数爆炸，默认值+可选。
- 预判：全局唯一实例 → 见 162；创建接口收口 → 见 162。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
