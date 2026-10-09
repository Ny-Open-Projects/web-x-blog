# 1313 ES 部署 OS 配置（二）：交换分区与透明大页

> 分类：搜索 / Elasticsearch | 难度：L3 | 题型：运维题 | 频率：中 | 关键词：**swapoff**/**vm.swappiness**/**透明大页**/**THP**/**性能**
> 原文锚点：第 16~39 段「禁用交换 + 交换偏好 + 禁用透明大页」

## 一句话总述
为性能 ES 应禁用交换分区（`swapoff -a` 临时、注释 /etc/fstab 永久）；若不忍禁用可设 `vm.swappiness` 偏低（如 1）减少换出；并禁用**透明大页（THP）**（向 /sys/kernel/mm/transparent_hugepage/{enabled,defrag} 写 `never`），因其导致内存分配抖动与延迟毛刺。

## 面试官视角
- 考察意图：是否知道交换与 THP 对 JVM/ES 延迟的危害，以及临时与永久两种改法。
- 分档：P5 知要关 swap；P6 知 swapoff + fstab、swappiness 取值；P7 知 THP 写 never、swappiness 内核版本差异（3.5+/RHEL 2.6.32-303+ 设 1 即最少交换）。
- 红旗答案：以为 swappiness=0 就是禁用交换（实为「仅内存不足才用」）；或不知 THP 要写 never。
- 惊艳点：点出「swappiness=1 在现代内核是『最少量交换』而非完全禁用；=0 才是内存不足才用」。

## 主问答
**Q（面试官原话）：** 为什么要禁用交换分区和透明大页？怎么操作？
**A：**
1. **禁用交换（swapoff）**：交换会让 ES 堆外内存/页缓存被换出，引发 GC 停顿与查询延迟飙升；临时 `swapoff -a` 立即关，永久注释 /etc/fstab 的 swap 行（否则重启恢复）。ES 节点建议完全禁用。
2. **交换偏好（vm.swappiness）**：若不能禁用，设 `vm.swappiness=1`（0~100，越低越偏物理内存）；现代内核（3.5+/RHEL 2.6.32-303+）设 1 即最少量交换而不禁用，设 0 才是「仅内存不足才用」。`sysctl -w vm.swappiness=1` 临时、写 sysctl.conf 永久。
3. **禁用透明大页（THP）**：THP 在后台做大页合并，会造成内存分配延迟抖动与毛刺，不利低延迟；向 /sys/kernel/mm/transparent_hugepage/enabled 与 .../defrag 写 `never`（或写进 rc.local 开机执行）彻底关闭。
4. **验证**：`free -h` 看 swap 是否为 0；`cat /sys/kernel/mm/transparent_hugepage/enabled` 应为 never。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 为什么要关 swap？ | 基础 | 避免换出致延迟 | P5 |
| L2 | 临时/永久怎么关？ | 操作 | swapoff -a / fstab | P6 |
| L3 | swappiness=0 含义？ | 细节 | 仅不足才用 | P6 |
| L4 | 为什么禁 THP？ | 深度 | 分配抖动毛刺 | P7 |
| L5 | THP 写啥值？ | 操作 | enabled/defrag 写 never | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Linux 内核 3.5+ / RHEL 2.6.32-303+ | swappiness=1 行为变化 | 现代内核设 1=最少交换；老内核才近似禁用 |

## 关键代码
```go
// 程序侧读 swappiness / THP 状态（部署自检）
import (
	"os"
	"strconv"

	"golang.org/x/sys/unix"
)
func checkSwapTHP() {
	s, _ := unix.Sysctl("vm.swappiness") // 应接近 0/1
	sw, _ := strconv.Atoi(s)
	// 读 /sys/kernel/mm/transparent_hugepage/enabled 内容应为 never
	b, _ := os.ReadFile("/sys/kernel/mm/transparent_hugepage/enabled")
	_ = sw
	_ = string(b)
}
```

## 总结与预判
交换与 THP 是延迟类调优。网络参数/JVM 堆等剩余配置下一张。

## ⚠️ 原文纠错
1. 事实核校： [经验] swapoff 关交换(临时+注释 fstab 永久)、swappiness 偏低(ES 设1)、THP 写 never 禁用——均正确；补正：swappiness=0 是「仅内存不足才用」而非完全禁用，现代内核设 1 即最少交换。
2. 崩坏词归一：源码将若干 ES/Linux 专有名词音译为崩坏词，本卡统一为规范术语。
