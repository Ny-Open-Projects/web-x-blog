// Package cluster 节点角色、分片规划、分片分配感知、冷热分层。
//
// 覆盖知识点：
//   - KP-CLUSTER-01 节点角色 master/data/ingest/coordinating/ml
//   - KP-CLUSTER-02 分片/副本规划（10 台 32C128G 如何最大化吞吐）
//   - KP-CLUSTER-03 冷热分层（hot/warm/cold tier + ILM 驱动迁移）
//   - KP-CLUSTER-04 分片分配感知（rack_id / same_shard.host 避免同机多副本）
package cluster

import (
	"context"
	"fmt"

	"es-demo/internal/es/client"
)

// Cluster 封装。
type Cluster struct {
	c *client.Client
}

// New 构造 Cluster。
func New(c *client.Client) *Cluster { return &Cluster{c: c} }

// NodeRoles 列出节点及其角色（走 _cat/nodes?format=json，返回原始 JSON）。对应 KP-CLUSTER-01。
func (cl *Cluster) NodeRoles(ctx context.Context) (string, error) {
	return cl.c.Perform(ctx, "GET", "/_cat/nodes?format=json", "")
}

// ShardPlan 分片规划建议（纯计算，便于在面试中推导）。
// 对应 KP-CLUSTER-02：给定节点数/单节点分片上限/目标总分片，给每个索引建议分片数。
func ShardPlan(nodeCount, shardsPerNode, targetTotalShards int) int {
	maxByNode := nodeCount * shardsPerNode
	if targetTotalShards <= maxByNode {
		return targetTotalShards
	}
	// 超过单集群上限时，按节点数尽量均分（向上取整）
	s := (targetTotalShards + nodeCount - 1) / nodeCount
	if s > shardsPerNode {
		s = shardsPerNode
	}
	return s
}

// SetAllocationAwareness 设置分片分配感知（按 rack_id 打散）。对应 KP-CLUSTER-04。
func (cl *Cluster) SetAllocationAwareness(ctx context.Context, attr string) error {
	body := fmt.Sprintf(`{ "persistent": { "cluster.routing.allocation.awareness.attributes": "%s" } }`, attr)
	_, err := cl.c.Perform(ctx, "PUT", "/_cluster/settings", body)
	return err
}

// SetTierRouting 把索引限定到指定冷热角色节点（也可用 ILM 的 require.data_tier 驱动）。
// 对应 KP-CLUSTER-03。
func (cl *Cluster) SetTierRouting(ctx context.Context, index string, roles ...string) error {
	incl := ""
	for i, r := range roles {
		if i > 0 {
			incl += ","
		}
		incl += r
	}
	body := fmt.Sprintf(`{ "index.routing.allocation.include.data_role": "%s" }`, incl)
	_, err := cl.c.Perform(ctx, "PUT", "/"+index+"/_settings", body)
	return err
}

// SetTotalShardsPerNode 限制单个索引在每个节点上的分片数，防热点。对应 KP-CLUSTER-04。
func (cl *Cluster) SetTotalShardsPerNode(ctx context.Context, index string, n int) error {
	body := fmt.Sprintf(`{ "index.routing.allocation.total_shards_per_node": %d }`, n)
	_, err := cl.c.Perform(ctx, "PUT", "/"+index+"/_settings", body)
	return err
}
