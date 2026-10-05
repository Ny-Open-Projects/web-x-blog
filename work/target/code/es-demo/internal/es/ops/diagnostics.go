package ops

// diagnostics.go —— 把运维判断固化成可执行的「诊断器」。
// 这些逻辑是纯函数，不依赖真实集群，已配套单元测试（diagnostics_test.go）。
// 对应《ES集群运维常用API与故障处置手册》的 Demo 示例。

import (
	"fmt"
	"sort"
	"strings"
)

// ---------------------------------------------------------------- 磁盘水位线

// Watermark 一条磁盘水位线。ES 允许百分比或具体剩余空间，但同一组不能混用。
type Watermark struct {
	Name      string
	IsPercent bool
	Percent   float64
	FreeGB    float64
}

// WatermarkSet 低/高/洪水三档。
type WatermarkSet struct {
	Low, High, Flood Watermark
}

// Defaults ES 出厂默认：85% / 90% / 95%。
func Defaults() WatermarkSet {
	return WatermarkSet{
		Low:   Watermark{Name: "low", IsPercent: true, Percent: 85},
		High:  Watermark{Name: "high", IsPercent: true, Percent: 90},
		Flood: Watermark{Name: "flood_stage", IsPercent: true, Percent: 95},
	}
}

// Validate 校验水位线是否混用百分比与具体空间（ES 明确禁止）。
func (w WatermarkSet) Validate() error {
	all := []Watermark{w.Low, w.High, w.Flood}
	pct, abs := 0, 0
	for _, x := range all {
		if x.IsPercent {
			pct++
		} else {
			abs++
		}
	}
	if pct > 0 && abs > 0 {
		return fmt.Errorf("水位线混用了百分比(%d档)与具体空间(%d档)，ES 不允许", pct, abs)
	}
	if pct == 3 && w.Low.Percent > w.High.Percent {
		return fmt.Errorf("低水位线高于高水位线，配置非法")
	}
	return nil
}

func (w Watermark) hit(usedPercent, freeGB float64) bool {
	if w.IsPercent {
		return usedPercent >= w.Percent
	}
	return freeGB <= w.FreeGB
}

// Stage 磁盘所处阶段。
type Stage struct {
	Name   string
	Effect string
}

// Evaluate 根据磁盘使用情况判定阶段。从洪水线往低水位线判（命中最高风险档）。
func (w WatermarkSet) Evaluate(totalGB, usedGB float64) Stage {
	usedPercent := usedGB / totalGB * 100
	freeGB := totalGB - usedGB
	switch {
	case w.Flood.hit(usedPercent, freeGB):
		return Stage{"洪水线", "索引被置为只读，无法写入；腾出空间后需手动解除只读"}
	case w.High.hit(usedPercent, freeGB):
		return Stage{"高水位线", "ES 尝试把分片重新分配到低于该水位线的节点"}
	case w.Low.hit(usedPercent, freeGB):
		return Stage{"低水位线", "新主分片不受影响，但副本不再分配到该节点"}
	default:
		return Stage{"正常", "分片可正常分配"}
	}
}

// ---------------------------------------------------------------- 未分配分片诊断

// Op 一条推荐处置动作，带可直接执行的命令。
type Op struct {
	Action  string
	Command string
}

// Explain 对应 _cluster/allocation/explain 的关键字段。
type Explain struct {
	Index   string
	Shard   int
	Primary bool
	Reason  string // decide.explanation 里的关键原因
}

var playbook = []struct {
	keys    []string
	actions []Op
}{
	{
		[]string{"node_left", "node left", "offline"},
		[]Op{
			{"重启离线节点（生产最常见）", "ssh <node> && sudo systemctl restart elasticsearch"},
			{"确认节点已重新加入集群", "GET /_cat/nodes"},
		},
	},
	{
		[]string{"same_shard", "shard rule", "cannot allocate"},
		[]Op{
			{"主副不能同节点：扩容节点或调整分片数", "GET /_cat/nodes?v"},
			{"若因单节点分片数达上限，临时提额", `PUT /_cluster/settings {"persistent":{"cluster.max_shards_per_node":2000}}`},
		},
	},
	{
		[]string{"disk", "watermark", "flood"},
		[]Op{
			{"临时抬高磁盘水位线", `PUT /_cluster/settings {"persistent":{"cluster.routing.allocation.disk.watermark.high":"95%"}}`},
			{"扩容磁盘或清理历史索引", "DELETE /log-2026.01*"},
			{"若已触发洪水线，手动解除只读", `PUT /idx/_settings {"index.blocks.read_only_allow_delete":null}`},
		},
	},
	{
		[]string{"retry", "failed allocation", "too many attempts"},
		[]Op{{"手动重试分配", "POST /_cluster/reroute?retry_failed=true"}},
	},
	{
		[]string{"corrupt", "broken", "inconsistent", "stale"},
		[]Op{
			{"副本数归零再设回（重建副本）", `PUT /idx/_settings {"index.number_of_replicas":0}`},
			{"副本恢复后设回原值", `PUT /idx/_settings {"index.number_of_replicas":1}`},
		},
	},
}

// Diagnose 根据 explain 结果给出处置建议（关键字 → 剧本）。
func Diagnose(e Explain) []Op {
	lower := strings.ToLower(e.Reason)
	for _, p := range playbook {
		for _, k := range p.keys {
			if strings.Contains(lower, k) {
				return p.actions
			}
		}
	}
	return []Op{{"原因未命中已知剧本，人工介入", "GET /_cluster/allocation/explain"}}
}

// LossyOps 会产生数据丢失的兜底操作——只在磁盘确认损坏且短期无法恢复时使用。
func LossyOps(e Explain) []Op {
	kind := "allocate_empty_primary"
	if e.Primary {
		kind = "allocate_stale_primary"
	}
	return []Op{
		{"兜底：剔除原分片元数据（会丢数据）",
			fmt.Sprintf("POST /_cluster/reroute {\"commands\":[{\"%s\":{\"index\":\"%s\",\"shard\":%d,\"node\":\"node-1\",\"accept_data_loss\":true}}]}",
				kind, e.Index, e.Shard)},
		{"集群恢复后从上游数据库重建索引", "POST /_reindex {\"conflicts\":\"proceed\",\"dest\":{\"op_type\":\"create\"}}"},
	}
}

// ---------------------------------------------------------------- 滚动重启

// validateEnable 校验 allocation.enable 取值。none 与 null 语义相反，重启流程禁止 none。
func validateEnable(v string) (string, error) {
	switch v {
	case "all", "null":
		return "恢复全部分片分配（null = 清除设置回到默认）", nil
	case "primaries":
		return "只允许主分片迁移，不主动恢复丢失的副本 —— 重启前设这个", nil
	case "new_primaries":
		return "只允许新索引的主分片分配", nil
	case "none":
		return "", fmt.Errorf("none 表示不允许任何分片分配，滚动重启流程中禁止使用该值")
	default:
		return "", fmt.Errorf("未知取值 %q", v)
	}
}

// RestartStep 滚动重启的一步。
type RestartStep struct {
	Name, Command, Note string
}

// RestartPlan 单节点滚动重启标准流程（六步）。
func RestartPlan(node string) []RestartStep {
	return []RestartStep{
		{"禁用副本分配", `PUT /_cluster/settings {"persistent":{"cluster.routing.allocation.enable":"primaries"}}`,
			"否则节点离线 1 分钟后 ES 自动恢复副本，带来大量 IO 与网络消耗"},
		{"停止写入并 flush", "POST /_flush", "清空 translog，可极大加快分片恢复速度"},
		{"重启节点", fmt.Sprintf("ssh %s && sudo systemctl restart elasticsearch", node), "一次只重启一个节点"},
		{"确认节点已加入", "GET /_cat/nodes", "节点数没回来到齐之前，不要进行下一步"},
		{"恢复副本分配", `PUT /_cluster/settings {"persistent":{"cluster.routing.allocation.enable":null}}`,
			"用 all 或 null，绝不能是 none"},
		{"等待回到 green", "GET /_cat/health", "green 之后再重启下一个节点"},
	}
}

// ---------------------------------------------------------------- 线程池健康度

// ThreadPool 对应 _cat/thread_pool 的一行。
type ThreadPool struct {
	Node, Name          string
	Size, Active, Queue int
	Rejected            int64
}

// Health 线程池风险评估。
type Health struct {
	Level string
	Hint  string
}

// Health 计算线程池风险等级。
func (t ThreadPool) Health() Health {
	switch {
	case t.Rejected > 0:
		return Health{"危险", fmt.Sprintf("已有 %d 次请求被拒绝；写请求被拒会直接丢数据，业务层必须识别 429 并重试", t.Rejected)}
	case t.Size > 0 && t.Queue > t.Size*2:
		return Health{"告警", fmt.Sprintf("队列 %d 已远超线程池大小 %d，节点即将拒绝请求", t.Queue, t.Size)}
	case t.Size > 0 && t.Active*10 >= t.Size*9:
		return Health{"注意", fmt.Sprintf("活跃线程 %d/%d，接近打满，建议扩容或限流", t.Active, t.Size)}
	default:
		return Health{"正常", "水位健康"}
	}
}

// RankThreads 按危险度排序（最该处理的排最前）。
func RankThreads(pools []ThreadPool) []ThreadPool {
	order := map[string]int{"危险": 0, "告警": 1, "注意": 2, "正常": 3}
	out := append([]ThreadPool{}, pools...)
	sort.SliceStable(out, func(i, j int) bool {
		hi, hj := out[i].Health(), out[j].Health()
		if hi.Level != hj.Level {
			return order[hi.Level] < order[hj.Level]
		}
		return out[i].Rejected > out[j].Rejected
	})
	return out
}

// ValidateEnable 暴露给外部调用（避免未使用告警）。
func ValidateEnable(v string) (string, error) { return validateEnable(v) }
