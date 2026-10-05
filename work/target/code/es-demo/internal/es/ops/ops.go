// Package ops 集群运维 API 封装（对应《ES集群运维常用API与故障处置手册》）。
//
// 覆盖知识点：
//   - KP-OPS-01 集群健康 / cat APIs（_cat/shards、_cat/thread_pool）
//   - KP-OPS-02 allocation explain 定位未分配分片
//   - KP-OPS-03 磁盘三档水位线 85%/90%/95%，百分比与具体空间不能混用
//   - KP-OPS-04 forcemerge?only_expunge_deletes 清理已删除文档
//   - KP-OPS-06 snapshot/restore 跨集群迁移
//   - KP-OPS-07 reindex（conflicts:proceed + op_type:create 幂等重跑）
//   - KP-OPS-08 热点线程 / pending 任务排查 CPU
//   - KP-OPS-10 只读开关 / 禁止通配符删除
//
// 说明：运维端点没有 typed 方法，统一走 client.Perform（原始 JSON），
// 这样代码和课程里的 REST 文档一一对应，初学者最容易对照。
package ops

import (
	"context"
	"fmt"

	"es-demo/internal/es/client"
)

// Ops 运维封装。
type Ops struct {
	c *client.Client
}

// New 构造 Ops。
func New(c *client.Client) *Ops { return &Ops{c: c} }

// Health 集群健康状态。
func (o *Ops) Health(ctx context.Context) (string, error) {
	h, err := o.c.Client.ClusterHealth().Do(ctx)
	if err != nil {
		return "", err
	}
	return h.Status, nil
}

// CatShards 列出分片（含未分配原因）。对应 KP-OPS-01。
func (o *Ops) CatShards(ctx context.Context) ([]string, error) {
	rows, err := o.c.Client.CatShards().Do(ctx)
	if err != nil {
		return nil, err
	}
	var out []string
	for _, r := range rows {
		out = append(out, fmt.Sprintf("%s/%d/%s state=%s reason=%q node=%s",
			r.Index, r.Shard, r.Prirep, r.State, r.UnassignedReason, r.Node))
	}
	return out, nil
}

// AllocationExplain 未分配分片的原因。对应 KP-OPS-02。
func (o *Ops) AllocationExplain(ctx context.Context, index string, shard int, primary bool) (string, error) {
	body := ""
	if index != "" {
		body = fmt.Sprintf(`{"index":"%s","shard":%d,"primary":%t}`, index, shard, primary)
	}
	return o.c.Perform(ctx, "GET", "/_cluster/allocation/explain", body)
}

// SetDiskWatermarks 设置磁盘三档水位线。low/high/flood 要么全百分比要么全具体空间，
// 不能混用——这是课程反复强调的坑。对应 KP-OPS-03。
func (o *Ops) SetDiskWatermarks(ctx context.Context, low, high, flood string) error {
	body := fmt.Sprintf(`{
      "persistent": {
        "cluster.routing.allocation.disk.watermark.low": "%s",
        "cluster.routing.allocation.disk.watermark.high": "%s",
        "cluster.routing.allocation.disk.watermark.flood_stage": "%s"
      }}`, low, high, flood)
	_, err := o.c.Perform(ctx, "PUT", "/_cluster/settings", body)
	return err
}

// ForcemergeExpunge 仅清理已删除文档（比合并到指定段数安全、压力小）。对应 KP-OPS-04。
func (o *Ops) ForcemergeExpunge(ctx context.Context, index string) error {
	_, err := o.c.Client.Forcemerge(index).OnlyExpungeDeletes(true).Do(ctx)
	return err
}

// Reindex 幂等重建索引：conflicts=proceed 遇冲突继续，op_type=create 只拷目标不存在的。
// 对应 KP-OPS-07 / KP-WRITE-07。
func (o *Ops) Reindex(ctx context.Context, source, dest string) error {
	body := fmt.Sprintf(`{
      "conflicts": "proceed",
      "source": { "index": "%s" },
      "dest":   { "index": "%s", "op_type": "create" }
    }`, source, dest)
	_, err := o.c.Perform(ctx, "POST", "/_reindex", body)
	return err
}

// ReindexRemote 跨集群重建索引（需先配 cluster.remote.*.seeds）。对应 KP-XC-03。
func (o *Ops) ReindexRemote(ctx context.Context, remote, source, dest string) error {
	body := fmt.Sprintf(`{
      "source": { "remote": { "host": "%s" }, "index": "%s" },
      "dest":   { "index": "%s" }
    }`, remote, source, dest)
	_, err := o.c.Perform(ctx, "POST", "/_reindex", body)
	return err
}

// SetReadOnly 对索引设置/解除只读（洪水线触发后必须手动解除）。
func (o *Ops) SetReadOnly(ctx context.Context, index string, readOnly bool) error {
	v := "true"
	if !readOnly {
		v = "null"
	}
	body := fmt.Sprintf(`{ "index.blocks.read_only_allow_delete": %s }`, v)
	_, err := o.c.Perform(ctx, "PUT", "/"+index+"/_settings", body)
	return err
}

// DestructiveRequiresName 禁止通配符删除（生产必开）。对应 KP-OPS-10。
func (o *Ops) DestructiveRequiresName(ctx context.Context, enable bool) error {
	body := fmt.Sprintf(`{ "persistent": { "action.destructive_requires_name": %t } }`, enable)
	_, err := o.c.Perform(ctx, "PUT", "/_cluster/settings", body)
	return err
}

// PutClusterSetting 通用：设置集群级 persistent 开关（如 allocation.enable）。
func (o *Ops) PutClusterSetting(ctx context.Context, key, value string) error {
	body := fmt.Sprintf(`{ "persistent": { "%s": %s } }`, key, value)
	_, err := o.c.Perform(ctx, "PUT", "/_cluster/settings", body)
	return err
}

// Snapshot 注册仓库并打快照（跨集群迁移/备份）。对应 KP-OPS-06。
func (o *Ops) Snapshot(ctx context.Context, repo, repoBody, snap, snapBody string) error {
	if _, err := o.c.Perform(ctx, "PUT", "/_snapshot/"+repo, repoBody); err != nil {
		return err
	}
	_, err := o.c.Perform(ctx, "PUT", "/_snapshot/"+repo+"/"+snap, snapBody)
	return err
}

// ThreadPools 线程池统计（看 active/queue/rejected；rejected>0 表示有请求被拒）。
// 走 _cat/thread_pool?format=json，返回原始 JSON。对应 KP-OPS-08。
func (o *Ops) ThreadPools(ctx context.Context) (string, error) {
	return o.c.Perform(ctx, "GET", "/_cat/thread_pool?format=json", "")
}

// HotThreads 热点线程（哪个线程在烧 CPU）。对应 KP-OPS-08。
func (o *Ops) HotThreads(ctx context.Context) (string, error) {
	return o.c.Perform(ctx, "GET", "/_nodes/hot_threads", "")
}

// PendingTasks 集群级待处理任务。对应 KP-OPS-08。
func (o *Ops) PendingTasks(ctx context.Context) (string, error) {
	return o.c.Perform(ctx, "GET", "/_cluster/pending_tasks", "")
}
