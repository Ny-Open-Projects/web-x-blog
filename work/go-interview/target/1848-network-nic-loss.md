# 1848 网卡与中间网络丢包（链路层）

> 分类：网络/TCP | 难度：L3 | 题型：八股题 | 频率：低 | 关键词：**网卡队列**/**txqueuelen**/**中间网络**/**ping**/**MTR**

> 原文锚点：第 13~22 段（流量控制丢包/网卡队列 txqueuelen/drop/调整）+ 第 43~53 段（中间网络丢包/ping/MTR -u -r/loss/百度.com）+ 第 54~56 段（TCP 只保证传输层）

## 一句话总述
网卡侧与中间网络侧丢包是**服务端外侧/链路层**问题：网卡队列（`txqueuelen`）溢出或网卡硬件/驱动缺陷会丢包；跨机房的长链路上任意路由器/交换机/光缆节点都可能丢，用 `ping` / `mtr -u -r` 逐跳定位 `%loss`。

## 面试官视角
这题考「链路层与网络层排查」的动手能力。考点：① 网卡队列溢出怎么看（`ifconfig` 的 `drop`/`txqueuelen`）；② 中间网络用什么工具逐跳查（`mtr` 比 `ping` 信息更全）；③ 收口回到「TCP 只保传输层」。能熟练用 `mtr` 看每跳丢包率，是 SRE/网络向候选加分项。

## 主问答
**Q（面试官原话）：** 网卡和中间网络导致的丢包怎么排查？

**A：**
1. **网卡队列（流量控制）丢包**：网卡处理能力有限，突发流量在发送队列排队，队满即丢。用 `ifconfig <网卡>` 看 `txqueuelen`（队列长度）与 `drop` 计数，`drop > 0` 即队列溢出证据；可调大：`ifconfig <网卡> txqueuelen 2000`（默认值常是 1000）。
2. **网卡/驱动硬件丢包**：网线质量差、水晶头接触不良、网卡性能不足或驱动 bug，属物理层/驱动层丢包，需换线、换网卡或升级驱动，靠 `ethtool -S <网卡>` 看特定错误计数（如 `rx_errors`/`dropped`）。
3. **中间网络逐跳丢包**：A、B 间链路经过多层路由器/交换机/光缆，任一节点都可能丢。先 `ping 目标` 看端到端丢包与延迟；再用 `mtr -u -r 目标`（`-u` 用 UDP 探测可绕过部分防火墙，`-r` 以报告形式输出）看**每一跳的 `%loss`**——定位到底是哪个中间节点在丢。
4. **收口边界**：无论哪一层丢，都要记住 **TCP 只保证「A 传输层 → B 传输层」的字节流可靠有序，不保证对端应用层真正消费**；应用层可靠性（确认/重传/幂等）必须自己实现。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 网卡队列怎么看？ | txqueuelen/drop | ifconfig 看 drop 计数与队列长 | 无命令算 L1 未过 |
| L2 | 队列满了调什么？ | txqueuelen 调整 | ifconfig <if> txqueuelen 2000 | 不知算 L2 未过 |
| L3 | 硬件丢包怎么查？ | ethtool 错误计数 | ethtool -S 看 rx_errors/dropped | 只会换线算 L3 未过 |
| L4 | 中间网络怎么定位？ | mtr 逐跳 | mtr -u -r 目标看每跳 %loss | 只会 ping 算 L4 未过 |
| L5 | TCP 保到哪层？ | 传输层vs应用层 | 只到对端传输层，应用层自保 | 混淆算 L5 未过 |

## 版本与兼容性
- `mtr` 的 `-u`（UDP 探测）可绕过部分基于 ICMP 的限速/防火墙，`-r` 一次性报告模式适合脚本采集；不同发行版 `mtr` 版本参数略有差异，但 `-u/-r` 通用。
- `txqueuelen` 默认 1000，高吞吐场景（如 10G+ 网卡）可调大到 2000~10000；需配合 `ethtool -G` 的 ring buffer 一起看。
- 这些诊断**与编程语言无关**，是 Linux 网络栈事实。

## 关键代码

```go
// 用 mtr 逐跳定位中间网络丢包（Go 调用外部命令解析报告）
func probePath(host string) (string, error) {
	out, err := exec.Command("mtr", "-u", "-r", "-c", "10", host).CombinedOutput()
	if err != nil {
		return "", err
	}
	// 解析输出中的 %loss 列，定位首个高丢包跳
	return string(out), nil
}

// 应用层自保示例：写超时 + 失败重传，不依赖 TCP 保证对端应用收到
func sendWithRetry(c net.Conn, payload []byte, maxRetry int) error {
	for i := 0; i < maxRetry; i++ {
		_ = c.SetWriteDeadline(time.Now().Add(2 * time.Second))
		if _, err := c.Write(payload); err != nil {
			time.Sleep(time.Duration(i+1) * 100 * time.Millisecond) // 退避
			continue
		}
		// 还需对端应用层 ACK 才算送达（TCP 只保证到对端传输层）
		return nil
	}
	return errors.New("send failed after retries")
}
```

## 总结与追问预判
收口：**外侧丢包 = 网卡队列/硬件（看 `ifconfig drop`/`ethtool -S`）+ 中间网络（看 `mtr -u -r` 每跳 `%loss`）**，最后统一回到「TCP 不保应用层」。预判追问：① 内侧队列/缓冲丢包 → 1848.md`；② 应用层自保手段（消息确认/重传/幂等）。回答时把 `mtr` 的「逐跳 `%loss`」作为亮点抛出来，比只说 `ping` 更专业。

## ⚠️ 原文纠错
源视频转写将 txqueuelen / MTR / /proc/net/snmp / 链路 等音译为崩坏词（如「TSqueenlenges」「MTR 杠u 杠r」「leightstate 指代 snmp」「光缆这些」保留但节点表述崩坏），本卡已还原为规范术语（txqueuelen / MTR / /proc/net/snmp / 路由器交换机光缆链路）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** `ping` 只能看端到端丢包，`mtr` 才能看**逐跳**丢包率——定位「到底是哪个中间节点丢」必须用 `mtr -u -r`。面试中说出「先看 ping 端到端，再用 mtr 逐跳定位」的排查顺序，比只背命令更显工程素养。
