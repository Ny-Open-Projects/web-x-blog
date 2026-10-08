# 1511 Prometheus 指标类型：Counter 与 Gauge

> 分类：监控 / Prometheus | 难度：L3 | 题型：概念题 | 频率：高 | 关键词：**Counter**/**Gauge**/**只增不减**/**当前状态**/**rate/irate**
> 原文锚点：第 6~36 段「四种指标类型 + Counter/Gauge」

## 一句话总述
Prometheus 四类指标里最基础的两个是 **Counter（计数器）**与 **Gauge（仪表）**：Counter 只增不减、表示累积量（如 HTTP 请求总数），用 `rate`/`irate` 算 QPS；Gauge 可增可减、表示当前瞬时状态（如内存/磁盘占用），用 `set`/`inc`/`dec` 直接改。

## 面试官视角
- 考察意图：是否分清「累积量」与「瞬时量」的本质差异，以及 Counter 为何不能减、Gauge 为何能减。
- 分档：P5 知 Counter 只增、Gauge 可变；P6 知 Counter 用 rate/irate 算速率、Gauge 直接看当前值；P7 知 irate 取瞬时、rate 取区间、重置要从 0 重计。
- 红旗答案：把 Gauge 当累积量算 QPS；或以为 Counter 能 decrease。
- 惊艳点：点出「Counter 重置（进程重启）后计数从 0 起，rate/irate 能自动处理断点」。

## 主问答
**Q（面试官原话）：** Counter 和 Gauge 有什么区别？分别怎么用？
**A：**
1. **Counter（只增不减）**：表示单调累积的度量值，如 HTTP 请求总数、系统处理总量；不能减少，进程重置时从 0 重新计数；查询用 `rate(counter[5m])` 或 `irate(counter[5m])` 算变化速率，从而得 QPS（irate 取最近两个样本更灵敏，rate 取区间平均更平滑）。
2. **Gauge（可增可减）**：反映系统当前瞬时状态，样本可增可减，如内存使用量、磁盘占用、温度；用 `set` 设值或 `inc`/`dec` 增减；查询直接 `gauge` 取值或做 `max`/`avg` 等聚合。
3. **选型口诀**：能下降的指标用 Gauge（状态类），只会上扬的用 Counter（累积类）；QPS 必须基于 Counter 而非 Gauge 算速率。
4. **标签过滤**：两类 metric 都带 labels（instance/job/method/uri/status 等），可 `http_requests_total{status="500"}` 按状态码过滤，本质是按标签维度做多维时序查询。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | Counter 能减吗？ | 基础 | 只增不减 | P5 |
| L2 | 怎么算 QPS？ | 用法 | rate/irate | P6 |
| L3 | irate vs rate？ | 细节 | 瞬时 vs 区间 | P6 |
| L4 | Gauge 怎么改？ | 用法 | set/inc/dec | P7 |
| L5 | 重置怎么办？ | 进阶 | rate 自动处理 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Prometheus 全版本 | 无 | Counter/Gauge 为最基础两类指标，跨版本一致 |

## 关键代码
```go
// client_golang 定义 Counter 与 Gauge（Go 侧视角）
var (
	httpTotal = prometheus.NewCounterVec(prometheus.CounterOpts{
		Name: "http_requests_total", // 只增不减
	}, []string{"method", "status"}),
	memUsed = prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "mem_used_bytes", // 可增可减
	}),
)
func handle() {
	httpTotal.WithLabelValues("GET", "200").Inc()
	memUsed.Set(getMem()) // Gauge 直接设当前值
}
```

## 总结与追问预判
Counter/Gauge 是标量的两类。分布类指标（Histogram/Summary）下一张——它们解决「平均值掩盖长尾」问题。

## ⚠️ 原文纠错
1. 事实核校： [经验] Counter 只增不减/rate-irate 算 QPS、Gauge 可增可减反映当前状态/set-inc-dec、labels 多维过滤——均正确。
2. 崩坏词归一：源码将若干 Prometheus/监控专有名词音译为崩坏词，本卡统一为规范术语。
