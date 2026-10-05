// Package ilm 索引生命周期管理封装（对应《索引生命周期管理原理及实践》）。
//
// 覆盖知识点：
//   - KP-ILM-01 ILM 策略四阶段 hot/warm/cold/delete
//   - KP-ILM-02 rollover 滚动 + 写别名（避免单索引无限膨胀）
//   - KP-ILM-03 绑定策略 / 调压缩算法（index.codec=best_compression，需先 close）
package ilm

import (
	"context"
	"fmt"

	"es-demo/internal/es/client"
)

// ILM 封装。
type ILM struct {
	c *client.Client
}

// New 构造 ILM。
func New(c *client.Client) *ILM { return &ILM{c: c} }

// PutPolicy 创建/更新 ILM 策略（hot→warm→cold→delete）。对应 KP-ILM-01。
func (i *ILM) PutPolicy(ctx context.Context, name, body string) error {
	_, err := i.c.Perform(ctx, "PUT", "/_ilm/policy/"+name, body)
	return err
}

// GetPolicy 读取 ILM 策略。
func (i *ILM) GetPolicy(ctx context.Context, name string) (string, error) {
	return i.c.Perform(ctx, "GET", "/_ilm/policy/"+name, "")
}

// DeletePolicy 删除 ILM 策略。
func (i *ILM) DeletePolicy(ctx context.Context, name string) error {
	_, err := i.c.Perform(ctx, "DELETE", "/_ilm/policy/"+name, "")
	return err
}

// Rollover 触发 rollover（索引须用「写别名」写入）。对应 KP-ILM-02。
func (i *ILM) Rollover(ctx context.Context, alias string) (string, error) {
	return i.c.Perform(ctx, "POST", "/"+alias+"/_rollover", "")
}

// BindPolicy 把 ILM 策略绑到索引（或索引模板）。对应 KP-ILM-03。
func (i *ILM) BindPolicy(ctx context.Context, index, policy string) error {
	body := fmt.Sprintf(`{ "index.lifecycle.name": "%s" }`, policy)
	_, err := i.c.Perform(ctx, "PUT", "/"+index+"/_settings", body)
	return err
}

// SetCodec 调整压缩算法（best_compression 更高压缩比）。注意：必须先 close 索引。
func (i *ILM) SetCodec(ctx context.Context, index, codec string) error {
	if _, err := i.c.Perform(ctx, "POST", "/"+index+"/_close", ""); err != nil {
		return err
	}
	body := fmt.Sprintf(`{ "index.codec": "%s" }`, codec)
	if _, err := i.c.Perform(ctx, "PUT", "/"+index+"/_settings", body); err != nil {
		return err
	}
	_, err := i.c.Perform(ctx, "POST", "/"+index+"/_open", "")
	return err
}
