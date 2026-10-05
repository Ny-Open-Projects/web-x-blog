// Package agg 聚合查询封装。
//
// 覆盖知识点（对应面试题「集群运维 / 搜索实战」）：
//   - KP-AGG-01 桶聚合 terms / date_histogram、指标聚合 avg/sum/max
//   - KP-AGG-02 shard_size 提升 terms 聚合精度（避免分片级 topN 截断误差）
//   - KP-AGG-03 pipeline 聚合（如 derivative / bucket_script 做环比）
package agg

import (
	"context"
	"fmt"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/es/client"
)

// Aggregator 聚合封装。
type Aggregator struct {
	c *client.Client
}

// New 构造 Aggregator。
func New(c *client.Client) *Aggregator { return &Aggregator{c: c} }

// TermsAgg 按字段做 terms 桶聚合，shardSize 提升精度。
// 对应 KP-AGG-02：terms 默认每个分片取 size 个，shard_size 控制分片级取样量。
func (a *Aggregator) TermsAgg(ctx context.Context, index string, field string, size, shardSize int) (map[string]int64, error) {
	agg := elastic.NewTermsAggregation().Field(field).Size(size)
	if shardSize > 0 {
		agg = agg.ShardSize(shardSize)
	}
	res, err := a.c.Client.Search().Index(index).Size(0).
		Aggregation("by_"+field, agg).Do(ctx)
	if err != nil {
		return nil, err
	}
	return parseTerms(res, "by_"+field), nil
}

// DateHistogram 按时间桶聚合（如按天统计日志量）。对应 KP-AGG-01。
func (a *Aggregator) DateHistogram(ctx context.Context, index, field, interval string) (map[string]int64, error) {
	agg := elastic.NewDateHistogramAggregation().Field(field).CalendarInterval(interval)
	res, err := a.c.Client.Search().Index(index).Size(0).
		Aggregation("over_time", agg).Do(ctx)
	if err != nil {
		return nil, err
	}
	return parseDateHist(res, "over_time"), nil
}

// AvgWithPipeline 对 avg 指标做 derivative（环比）pipeline 聚合。
// 对应 KP-AGG-03。
func (a *Aggregator) AvgWithPipeline(ctx context.Context, index, dateField, valueField, interval string) error {
	dateAgg := elastic.NewDateHistogramAggregation().Field(dateField).CalendarInterval(interval)
	dateAgg = dateAgg.SubAggregation("avg_val", elastic.NewAvgAggregation().Field(valueField))
	dateAgg = dateAgg.SubAggregation("delta", elastic.NewDerivativeAggregation().
		BucketsPath("avg_val"))
	_, err := a.c.Client.Search().Index(index).Size(0).
		Aggregation("over_time", dateAgg).Do(ctx)
	return err
}

func parseTerms(res *elastic.SearchResult, name string) map[string]int64 {
	out := map[string]int64{}
	if res.Aggregations == nil {
		return out
	}
	if t, ok := res.Aggregations.Terms(name); ok {
		for _, b := range t.Buckets {
			out[fmt.Sprintf("%v", b.Key)] = b.DocCount
		}
	}
	return out
}

func parseDateHist(res *elastic.SearchResult, name string) map[string]int64 {
	out := map[string]int64{}
	if res.Aggregations == nil {
		return out
	}
	if d, ok := res.Aggregations.DateHistogram(name); ok {
		for _, b := range d.Buckets {
			// KeyAsString 是指针，需判空后解引用。
			if b.KeyAsString != nil {
				out[*b.KeyAsString] = b.DocCount
			}
		}
	}
	return out
}
