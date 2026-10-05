// Package crosscluster 跨集群搜索（CCS）与跨集群复制（CCR）。
//
// 覆盖知识点：
//   - KP-XC-01 CCS 跨集群搜索（ccs_minimize_roundtrips 优化跨集群往返）
//   - KP-XC-02 CCR 跨集群复制（注意：需要 Platinum 授权）
//   - KP-XC-03 在 _cluster/settings 注册 remote cluster seeds
//
// 重要版本/授权提示（审计纠正点）：
//   - CCS 在 7.x 免费可用；CCR 需要 Platinum 授权，社区版不可用。
//   - 8.x 默认开启安全层，跨集群通信需配置 API Key / TLS，不能用裸 http。
package crosscluster

import (
	"context"
	"fmt"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/es/client"
)

// CC 跨集群封装。
type CC struct {
	c *client.Client
}

// New 构造 CC。
func New(c *client.Client) *CC { return &CC{c: c} }

// RegisterRemote 注册远程集群（用于 CCS / CCR）。对应 KP-XC-03。
func (x *CC) RegisterRemote(ctx context.Context, name, seed string) error {
	body := fmt.Sprintf(`{ "persistent": { "cluster.remote.%s.seeds": ["%s"] } }`, name, seed)
	_, err := x.c.Perform(ctx, "PUT", "/_cluster/settings", body)
	return err
}

// CrossClusterSearch 跨集群搜索：索引名用 <remote>:<index> 语法。
// ccs_minimize_roundtrips=true 让协调节点尽量合并请求、减少跨集群往返。对应 KP-XC-01。
func (x *CC) CrossClusterSearch(ctx context.Context, remote, index string, query elastic.Query) (int64, error) {
	target := fmt.Sprintf("%s:%s", remote, index)
	res, err := x.c.Client.Search().Index(target).Query(query).Size(10).Do(ctx)
	if err != nil {
		return 0, err
	}
	if res.Hits == nil || res.Hits.TotalHits == nil {
		return 0, nil
	}
	return res.Hits.TotalHits.Value, nil
}

// FollowIndex 建立 CCR 跟随（目标集群执行）。注意：需要 Platinum 授权。对应 KP-XC-02。
func (x *CC) FollowIndex(ctx context.Context, remote, leader, follower string) error {
	body := fmt.Sprintf(`{ "remote_cluster": "%s", "leader_index": "%s" }`, remote, leader)
	_, err := x.c.Perform(ctx, "PUT", "/"+follower+"/_ccr/follow", body)
	return err
}
