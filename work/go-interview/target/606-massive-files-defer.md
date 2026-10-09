# 606 打开 10 万个文件：从循环 defer 到并发限流的四步演进

> 分类：Go / 工程实践 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**文件句柄上限**/**ulimit**/**封装函数即关**/**WaitGroup 并发**/**goroutine 池**
> 原文锚点：第 1~31 段「操作系统对同时打开的文件句柄数量是有限制的，大多数 Linux 默认是 1024，可以通过 ulimit -n 查看…先打开十万个文件再依次关闭，很可能导致资源被耗尽…封装到单独的函数里，每处理完一个文件就关闭…还可以用异步并发的方式…存在协程堆积的情况，需要协程池控制同时存活数量」

## 一句话总述
海量资源的关闭管理是一个**四步演进链**：① 循环里 defer（全部攒到函数返回，句柄耗尽）→ ② **封装成函数**让每文件用完即关 → ③ **WaitGroup + goroutine 并发**提速 → ④ 发现无界并发会堆积协程耗内存，**用 goroutine 池控制并发上限**——本质是「defer 的函数级语义」叠加「操作系统句柄配额」叠加「无界并发的内存风险」三重约束。

## 面试官视角
- 考察意图：看你是否能把一个真实工程问题**推演到底**——大多数人停在「封装函数」这一步，能主动说出并发堆积与池化限流的才算完整。
- 分档：P5 知道循环 defer 会耗尽句柄；P6 会封装函数 + 报得出 ulimit -n / 1024；P7 能给出 WaitGroup 并发版并指出无界并发的内存风险与池化方案。
- 红旗答案：以为 defer 出循环就执行；并发版无脑 go 出去不设上限。
- 惊艳点：「句柄上限不只是 1024——soft/hard 两级，Go 程序能通过 `syscall.Getrlimit` 读取，容器里还受 cgroup 与宿主 ulimit 双重约束」 [经验]。

## 主问答
**Q（面试官原话）：** 要打开 10 万个文件处理，用 defer 关闭有什么问题？怎么改？
**A：**
1. **第一步：看清 defer 的函数级语义**——循环体里 `defer f.Close()` 不会每轮执行，而是把 10 万个关闭调用**压栈到函数返回前**，期间 10 万个句柄同时打开。macOS 实测句柄上限 1048575，而**大多数 Linux 默认 soft limit 只有 1024**（`ulimit -n` 查看）——第 1025 个文件就 `too many open files` 报错 [源码]。
2. **第二步：封装函数，用完即关**。把「打开-处理-关闭」包成一个子函数，defer 写在子函数里——每次调用返回时立刻关闭，**同一时刻只有 1 个句柄**。这是 defer 的正确姿势：**defer 的粒度 = 资源的生命周期** [源码]。
3. **第三步：WaitGroup 并发提速**。文件 IO 慢，串行 10 万次总耗时惊人；改为每个文件 `wg.Add(1)` + `go func` 处理，`wg.Done()` 标记完成，主协程 `wg.Wait()` 等全部结束。注意 `wg.Add(1)` 要在 **go 之前**调用，否则存在 Wait 提前返回的竞态 [源码]。
4. **第四步：给并发加闸门**。无界并发的隐患：文件处理慢时**协程堆积**（10 万个 goroutine 的栈内存与调度压力），或文件大时**同时载入内存**耗尽内存。解法是 **goroutine 池/信号量**——用带缓冲 channel（`make(chan struct{}, N)`）或 worker pool 把同时存活的协程数限制在可控范围 [源码]。
5. **循环 defer 坑的机制层**：defer 对象（`_defer` 结构）在函数生命周期内持续累积，除了句柄风险还有内存与 deferproc 开销——机制细节见 `607-defer-mem-leak`、`604-defer-runtime.deep` [边界]，本卡聚焦资源管理演进不重述。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 循环里 defer 关文件有什么问题？ | 语义 | 函数返回才统一关闭，句柄堆积 | P5 停 |
| L2 | Linux 默认句柄上限多少？ | 常识 | ulimit -n，soft 默认 1024 | P5 停 |
| L3 | 怎么保证每个文件用完即关？ | 解法 | 封装子函数，defer 粒度=资源生命周期 | P6 停 |
| L4 | 并发版为什么要有界？ | 深一层 | 协程堆积耗内存/大文件撑爆内存，需池化 | P6 停 |
| L5 | 容器里句柄上限还看 ulimit 吗？ | 环境意识 | cgroup 与宿主 ulimit 双重约束，Getrlimit 实测 | P7 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| macOS/BSD | soft limit 常见 256 或很大（实测 1048575） | 别背死 1024，跑 ulimit -n 确认 [实测] |
| 主流 Linux | soft 1024 / hard 常见 1048576 | 1024 是 soft，root 可调 hard |
| systemd 服务 | Unit 配 LimitNOFILE 覆盖 shell ulimit | 服务句柄耗尽先查 Unit 配置 |
| 容器 | cgroup fd 配额 + 宿主 ulimit 双层 | 容器内 Getrlimit 看到的才是真值 |
| Go 1.19+ | `debug.SetMemoryLimit` 管内存软限，句柄仍靠 OS | 池化限流是应用层自己的责任 |

## 关键代码
```go
// 四步演进的终态: 有界并发 + 每文件用完即关
func processFiles(paths []string, concurrency int) {
	sem := make(chan struct{}, concurrency) // 池闸门: 同时最多 concurrency 个
	var wg sync.WaitGroup
	for _, p := range paths {
		wg.Add(1) // 必须 go 之前 Add
		go func(p string) {
			defer wg.Done()
			sem <- struct{}{} // 拿令牌
			defer func() { <-sem }()
			f, err := os.Open(p) // 子作用域内 defer: 用完即关
			if err != nil {
				return
			}
			defer f.Close()
			process(f)
		}(p)
	}
	wg.Wait()
}
// [实测] ulimit -n: macOS=1048575; Linux 默认 soft=1024 —— 第 1025 个文件即 too many open files
```

## 总结与追问预判
一句话记忆：**「defer 粒度 = 资源生命周期；并发必须上闸门；句柄上限先 ulimit 再谈优化」**。defer 的运行时机制与求值时机见 `604-defer-runtime.deep`、`607-defer-eval-moment`，循环变量捕获见 `607-defer-loop-var` [边界]。常追问「池大小设多少」——答按 IO 类型：纯磁盘 IO 接近盘并发（NVMe 可几十），网络存储看远端吞吐，压测定档位；再追问「wg.Add 放错位置会怎样」——go 之前没 Add 时 Wait 可能提前通过，新协程成了孤儿 [经验]。

## ⚠️ 原文纠错
1. 术语归一：[经验] 源为语音转写，「deffer/differ」应为 defer，「weightgroup/waitergroup/deweitergroup」应为 WaitGroup，「携程」应为「协程（goroutine）」，统一为规范术语。
2. 数字核校：Linux 默认 1024 正确，但为 **soft limit**；macOS 实测 1048575，平台差异本卡已补进版本表 [实测]。
3. 补充：源未提 wg.Add 必须在 go 之前的竞态细节与容器 cgroup 约束，均为高频追问点，本卡已补。
