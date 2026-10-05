// Package search 查询封装。
//
// 覆盖知识点：
//   - KP-SEARCH-01 term vs match、bool 组合查询
//   - KP-SEARCH-02 nested 查询（object 数组扁平化坑的填坑）
//   - KP-SEARCH-03 range / exists / ids 查询
//   - KP-SEARCH-04 function_score 相关性干预
//   - KP-SEARCH-05 排序（含 script 排序、geo 距离排序）
//   - KP-SEARCH-06 search_after 深翻页（替代 from/size 深翻）
//   - KP-SEARCH-07 scroll 滚动查询（用完必须 Clear）
//   - KP-SEARCH-08 msearch 并发搜索（提升搜索性能之并发搜索）
//   - KP-SEARCH-09 track_total_hits / highlight / _source 字段过滤
//   - 铁律：查单索引 + 带 routing + 少取字段
package search

import (
	"context"
	"encoding/json"
	"fmt"
	"io"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/es/client"
)

// Searcher 查询封装。
type Searcher struct {
	c *client.Client
}

// New 构造 Searcher。
func New(c *client.Client) *Searcher { return &Searcher{c: c} }

// SearchResult 归一化后的查询结果。
type SearchResult struct {
	Total   int64
	Sources [][]byte // 每个 hit 的 _source 原文
	TookMS  int
}

// Simple 通用查询：bool(must/should/filter) + 排序 + 分页 + track_total_hits。
// 对应 KP-SEARCH-01 / KP-SEARCH-05 / KP-SEARCH-09。
func (s *Searcher) Simple(ctx context.Context, index, routing string, must, should, filter []elastic.Query,
	from, size int, sorts ...elastic.Sorter) (*SearchResult, error) {

	boolQ := elastic.NewBoolQuery()
	if len(must) > 0 {
		boolQ = boolQ.Must(must...)
	}
	if len(should) > 0 {
		boolQ = boolQ.Should(should...)
	}
	if len(filter) > 0 {
		boolQ = boolQ.Filter(filter...)
	}

	svc := s.c.Client.Search().Index(index).Query(boolQ).
		From(from).Size(size).TrackTotalHits(true).Preference("_local")
	if routing != "" {
		svc = svc.Routing(routing)
	}
	for _, so := range sorts {
		svc = svc.SortBy(so)
	}

	res, err := svc.Do(ctx)
	if err != nil {
		return nil, err
	}
	return toResult(res), nil
}

// Nested 查询 nested 字段（path 指向 nested 字段）。
// 对应 KP-MAP-05 / KP-SEARCH-02：只有 nested query 才能保留数组元素内部字段关系。
func (s *Searcher) Nested(ctx context.Context, index, path string, inner elastic.Query) (*SearchResult, error) {
	q := elastic.NewNestedQuery(path, inner)
	res, err := s.c.Client.Search().Index(index).Query(q).Size(20).TrackTotalHits(true).Do(ctx)
	if err != nil {
		return nil, err
	}
	return toResult(res), nil
}

// HasChild 由子文档条件反查父文档（join 类型）。对应 KP-MAP-06。
func (s *Searcher) HasChild(ctx context.Context, index, childType string, inner elastic.Query) (*SearchResult, error) {
	q := elastic.NewHasChildQuery(childType, inner)
	res, err := s.c.Client.Search().Index(index).Query(q).Size(20).Do(ctx)
	if err != nil {
		return nil, err
	}
	return toResult(res), nil
}

// FunctionScore 用 function_score 干预相关性（如按销量/热度加权）。
// 对应 KP-SEARCH-04。
func (s *Searcher) FunctionScore(ctx context.Context, index string, base elastic.Query, field string) (*SearchResult, error) {
	q := elastic.NewFunctionScoreQuery().
		Query(base).
		AddScoreFunc(elastic.NewFieldValueFactorFunction().Field(field).Factor(0.1).Modifier("log1p"))
	res, err := s.c.Client.Search().Index(index).Query(q).Size(20).Do(ctx)
	if err != nil {
		return nil, err
	}
	return toResult(res), nil
}

// SearchAfter 深翻页：传入上一页最后一条的排序值，避免 from/size 深翻的性能悬崖。
// 对应 KP-SEARCH-06。
func (s *Searcher) SearchAfter(ctx context.Context, index string, query elastic.Query, sort *elastic.FieldSort, after []interface{}) (*SearchResult, error) {
	svc := s.c.Client.Search().Index(index).Query(query).Size(10).SortBy(sort)
	if len(after) > 0 {
		svc = svc.SearchAfter(after...)
	}
	res, err := svc.Do(ctx)
	if err != nil {
		return nil, err
	}
	return toResult(res), nil
}

// Scroll 滚动查询：逐批回调。routing 必须带；跑完主动 Clear，别让滚动上下文占内存。
// 对应 KP-SEARCH-07。
func (s *Searcher) Scroll(ctx context.Context, index, routing string, query elastic.Query, size int,
	cb func(source []byte) error) error {
	scroll := s.c.Client.Scroll(index).Query(query).Size(size).KeepAlive("1m")
	if routing != "" {
		scroll = scroll.Routing(routing)
	}
	for {
		res, err := scroll.Do(ctx)
		if err != nil {
			if err == io.EOF {
				break
			}
			return err
		}
		if res.Hits == nil || len(res.Hits.Hits) == 0 {
			break
		}
		for _, hit := range res.Hits.Hits {
			if err := cb(hit.Source); err != nil {
				_ = scroll.Clear(ctx)
				return err
			}
		}
		if res.ScrollId == "" {
			break
		}
	}
	return scroll.Clear(ctx)
}

// MultiSearch 一次请求并行查多个索引/查询（并发搜索提升吞吐）。
// 对应 KP-SEARCH-08。
func (s *Searcher) MultiSearch(ctx context.Context, reqs ...*elastic.SearchRequest) (*elastic.MultiSearchResult, error) {
	return s.c.Client.MultiSearch().Add(reqs...).Do(ctx)
}

// WithHighlight 带高亮 + _source 字段过滤的查询（少取字段省带宽）。
// 对应 KP-SEARCH-09。
func (s *Searcher) WithHighlight(ctx context.Context, index string, query elastic.Query, hlField string, include []string) (*SearchResult, error) {
	src := elastic.NewSearchSource().Query(query).Size(20)
	if len(include) > 0 {
		fc := elastic.NewFetchSourceContext(true).Include(include...)
		src = src.FetchSourceContext(fc)
	}
	hl := elastic.NewHighlight().Field(hlField)
	res, err := s.c.Client.Search().Index(index).SearchSource(src).Highlight(hl).Do(ctx)
	if err != nil {
		return nil, err
	}
	return toResult(res), nil
}

// toResult 归一化 elastic.SearchResult。
func toResult(res *elastic.SearchResult) *SearchResult {
	out := &SearchResult{TookMS: int(res.TookInMillis)}
	if res.Hits != nil {
		if res.Hits.TotalHits != nil {
			out.Total = res.Hits.TotalHits.Value
		}
		for _, h := range res.Hits.Hits {
			out.Sources = append(out.Sources, h.Source)
		}
	}
	return out
}

// PrintResult 把查询结果漂亮地打印出来（demo 用）。
func PrintResult(label string, r *SearchResult) {
	fmt.Printf("[%s] total=%d took=%dms hits=%d\n", label, r.Total, r.TookMS, len(r.Sources))
	for i, src := range r.Sources {
		fmt.Printf("  #%d %s\n", i, string(src))
	}
}

// Pretty 把任意结构格式化成缩进 JSON（工具函数）。
func Pretty(v interface{}) string {
	b, _ := json.MarshalIndent(v, "", "  ")
	return string(b)
}
