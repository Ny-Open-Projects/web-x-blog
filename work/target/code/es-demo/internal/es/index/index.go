// Package index 索引与 Mapping 操作。
//
// 覆盖知识点：
//   - KP-MAP-01 DynamicMapping 的四种策略 true/false/strict/runtime
//   - KP-MAP-02 字段类型选型（text/keyword/numeric/date/nested/object）
//   - KP-MAP-03 dynamic_templates（按名称/类型批量定型，防字段爆炸）
//   - KP-MAP-04 _source / enabled / doc_values / index:false
//   - KP-OPS-05 别名（滚动索引对外提供固定别名）
package index

import (
	"context"
	"fmt"

	"es-demo/internal/es/client"
)

// CreateIndex 若索引不存在则按 body 创建（body 即 settings+mappings 的 JSON）。
func CreateIndex(ctx context.Context, c *client.Client, index, body string) error {
	exists, err := c.Client.IndexExists(index).Do(ctx)
	if err != nil {
		return err
	}
	if exists {
		return nil
	}
	if _, err := c.Client.CreateIndex(index).BodyString(body).Do(ctx); err != nil {
		return fmt.Errorf("create index %s: %w", index, err)
	}
	return nil
}

// IndexExists 判断索引是否存在。
func IndexExists(ctx context.Context, c *client.Client, index string) (bool, error) {
	return c.Client.IndexExists(index).Do(ctx)
}

// CreateIndexStrict 预建索引并强制 strict：未定义字段直接拒绝写入（生产最安全）。
// 对应课程：DynamicMapping「特性也有毒性」—— 把不确定性挡在写入之前。
func CreateIndexStrict(ctx context.Context, c *client.Client, index string, props string) error {
	body := fmt.Sprintf(`{
      "settings": { "number_of_shards": 1, "number_of_replicas": 0 },
      "mappings": { "dynamic": "strict", "properties": %s }
    }`, props)
	return CreateIndex(ctx, c, index, body)
}

// CreateIndexDynamicFalse 演示 dynamic=false：新字段不进 mapping、保留在 _source、
// 能查到原始值但搜不到。
func CreateIndexDynamicFalse(ctx context.Context, c *client.Client, index string) error {
	body := `{
      "mappings": { "dynamic": "false", "properties": {} }
    }`
	return CreateIndex(ctx, c, index, body)
}

// PutDynamicTemplate 用动态模板按字段名规则定型，避免「字段爆炸」拖垮集群元数据。
// 例：把 *_kw 后缀字段统一映射成 keyword。
func PutDynamicTemplate(ctx context.Context, c *client.Client, index, name, pattern, esType string) error {
	body := fmt.Sprintf(`{
      "dynamic_templates": [
        { "%s": { "match_mapping_type": "string", "match": "%s",
                  "mapping": { "type": "%s" } } }
      ]
    }`, name, pattern, esType)
	_, err := c.Client.PutMapping().Index(index).BodyString(body).Do(ctx)
	return err
}

// GetMapping 读取索引 mapping（JSON 字符串返回，便于审计/调试）。
func GetMapping(ctx context.Context, c *client.Client, index string) (string, error) {
	res, err := c.Client.GetMapping().Index(index).Pretty(true).Do(ctx)
	if err != nil {
		return "", err
	}
	// Do 直接返回 map[索引名]mapping，按索引名取出。
	if m, ok := res[index]; ok {
		return fmt.Sprintf("%v", m), nil
	}
	return fmt.Sprintf("%v", res), nil
}

// AliasAdd 为索引挂上别名（滚动索引对外暴露固定别名）。
func AliasAdd(ctx context.Context, c *client.Client, index, alias string) error {
	_, err := c.Client.Alias().Add(index, alias).Do(ctx)
	return err
}

// AliasRemove 移除别名。
func AliasRemove(ctx context.Context, c *client.Client, index, alias string) error {
	_, err := c.Client.Alias().Remove(index, alias).Do(ctx)
	return err
}

// AliasSwap 原子切换别名指向（零停机切换读写索引）。
func AliasSwap(ctx context.Context, c *client.Client, alias, oldIndex, newIndex string) error {
	_, err := c.Client.Alias().
		Remove(oldIndex, alias).
		Add(newIndex, alias).
		Do(ctx)
	return err
}

// DeleteIndex 删除索引（生产务必配合 action.destructive_requires_name）。
func DeleteIndex(ctx context.Context, c *client.Client, index string) error {
	_, err := c.Client.DeleteIndex(index).Do(ctx)
	return err
}
