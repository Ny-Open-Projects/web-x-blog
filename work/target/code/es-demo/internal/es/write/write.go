// Package write 文档写入与批量写入。
//
// 覆盖知识点（对应《Go操作ES的技巧和注意事项》）：
//   - KP-WRITE-01 refresh 三值 false(默认)/true/wait_for
//   - KP-WRITE-02 BulkProcessor 三个阈值（worker数/文档数/字节数）任一触发即提交
//   - KP-WRITE-03 external 版本号乐观锁（传入版本须 > 现有版本）
//   - KP-WRITE-04 upsert：Doc(partial) + Upsert(full) 组合
//   - KP-WRITE-05 update / delete / updateByQuery / deleteByQuery（必须 ProceedOnVersionConflict）
//   - KP-WRITE-08 routing：带 routing 写入/更新才能命中正确分片
//   - KP-WRITE-06 ingest pipeline（大文本/邮件场景做预处理）
package write

import (
	"context"
	"fmt"
	"time"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/es/client"
)

// Refresh 取值：对应 refresh 三值。
const (
	RefreshFalse   = "false" // 默认，写完约 1s 后可见，吞吐最高
	RefreshTrue    = "true"  // 立即刷新主副分片，实时性高但吞吐骤降
	RefreshWaitFor = "wait_for" // 等下一次 refresh 后返回，折中
)

// Writer 文档写入封装，内置一个全局 BulkProcessor。
type Writer struct {
	c    *client.Client
	bulk *elastic.BulkProcessor
}

// NewWriter 创建写入器并启动后台 bulk 处理器。
func NewWriter(ctx context.Context, c *client.Client, opts ...WriterOption) (*Writer, error) {
	cfg := &writerConfig{workers: 3, bulkActions: 500, bulkSize: 5 << 20, flush: time.Second}
	for _, o := range opts {
		o(cfg)
	}
	proc, err := elastic.NewBulkProcessorService(c.Client).
		Name("es-demo-bulk").
		Workers(cfg.workers).
		BulkActions(cfg.bulkActions).
		BulkSize(cfg.bulkSize).
		FlushInterval(cfg.flush).
		After(func(_ int64, _ []elastic.BulkableRequest, resp *elastic.BulkResponse, err error) {
			if err != nil {
				// 生产：可重试的进重试队列，其余落存储补偿
				fmt.Printf("[bulk] submit error: %v\n", err)
				return
			}
			if resp != nil && resp.Errors {
				fmt.Printf("[bulk] %d items failed\n", len(resp.Items))
			}
		}).Do(ctx)
	if err != nil {
		return nil, fmt.Errorf("bulk processor: %w", err)
	}
	return &Writer{c: c, bulk: proc}, nil
}

// WriterOption 可选项。
type WriterOption func(*writerConfig)

type writerConfig struct {
	workers     int
	bulkActions int
	bulkSize    int
	flush       time.Duration
}

// WithBulkWorkers 设置 bulk worker 数。
func WithBulkWorkers(n int) WriterOption { return func(c *writerConfig) { c.workers = n } }

// WithBulkActions 设置每批文档数阈值。
func WithBulkActions(n int) WriterOption { return func(c *writerConfig) { c.bulkActions = n } }

// WithBulkSize 设置每批字节数阈值。
func WithBulkSize(b int) WriterOption { return func(c *writerConfig) { c.bulkSize = b } }

// Index 单条写入；refresh 显式传值，避免误用 true 拖垮吞吐。
func (w *Writer) Index(ctx context.Context, index, id, routing string, doc interface{}, refresh string) error {
	svc := w.c.Client.Index().Index(index)
	if id != "" {
		svc = svc.Id(id)
	}
	if routing != "" {
		svc = svc.Routing(routing)
	}
	if _, err := svc.BodyJson(doc).Refresh(refresh).Do(ctx); err != nil {
		return fmt.Errorf("index doc: %w", err)
	}
	return nil
}

// IndexWithVersion 使用 external 版本做乐观锁：传入版本须 > ES 现有版本才成功。
func (w *Writer) IndexWithVersion(ctx context.Context, index, id string, doc interface{}, version int64) error {
	if _, err := w.c.Client.Index().Index(index).Id(id).BodyJson(doc).
		Version(version).VersionType("external").Do(ctx); err != nil {
		return fmt.Errorf("index with version: %w", err)
	}
	return nil
}

// Upsert 文档存在则更新部分字段，不存在则整体写入 full（用 external 版本）。
func (w *Writer) Upsert(ctx context.Context, index, id string, partial, full interface{}, version int64) error {
	if _, err := w.c.Client.Update().Index(index).Id(id).
		Version(version).VersionType("external").
		Doc(partial).Upsert(full).Do(ctx); err != nil {
		return fmt.Errorf("upsert: %w", err)
	}
	return nil
}

// AddAsync 单条丢进后台 bulk 处理器（攒批由处理器托管）。
// 注意：进程退出前必须 Flush/Close，否则 channel 里未提交的数据会丢失。
func (w *Writer) AddAsync(index, id string, doc interface{}) {
	w.bulk.Add(elastic.NewBulkIndexRequest().Index(index).Id(id).Doc(doc))
}

// BulkNow 一批文档实时提交，立刻拿到每条结果（高可用场景用这种）。
func (w *Writer) BulkNow(ctx context.Context, index string, docs []elastic.BulkableRequest) (bool, error) {
	resp, err := w.c.Client.Bulk().Index(index).Add(docs...).Do(ctx)
	if err != nil {
		return false, err
	}
	return !resp.Errors, nil
}

// Update 部分字段更新。文档设了 routing 也必须带 routing，否则更新走不到目标分片。
func (w *Writer) Update(ctx context.Context, index, id, routing string, partial map[string]interface{}) error {
	svc := w.c.Client.Update().Index(index).Id(id)
	if routing != "" {
		svc = svc.Routing(routing)
	}
	if _, err := svc.Doc(partial).Do(ctx); err != nil {
		return fmt.Errorf("update: %w", err)
	}
	return nil
}

// Delete 删除文档（带 routing）。
func (w *Writer) Delete(ctx context.Context, index, id, routing string) error {
	svc := w.c.Client.Delete().Index(index).Id(id)
	if routing != "" {
		svc = svc.Routing(routing)
	}
	_, err := svc.Do(ctx)
	return err
}

// UpdateByQuery 按条件批量更新（painless 脚本）。
func (w *Writer) UpdateByQuery(ctx context.Context, index string, query elastic.Query, script string) error {
	_, err := w.c.Client.UpdateByQuery(index).Query(query).
		Script(elastic.NewScript(script).Lang("painless")).
		ProceedOnVersionConflict(). // 防止中途版本冲突导致整体失败
		Do(ctx)
	return err
}

// DeleteByQuery 按条件批量删除；必须 ProceedOnVersionConflict。
func (w *Writer) DeleteByQuery(ctx context.Context, index string, query elastic.Query) error {
	_, err := w.c.Client.DeleteByQuery(index).Query(query).
		ProceedOnVersionConflict().Do(ctx)
	return err
}

// Get 按 ID 取文档；routing 必须带，否则按 _id 路由会取不到。
func (w *Writer) Get(ctx context.Context, index, id, routing string) (*elastic.GetResult, error) {
	svc := w.c.Client.Get().Index(index).Id(id)
	if routing != "" {
		svc = svc.Routing(routing)
	}
	return svc.Do(ctx)
}

// MGet 一次取多文档（每个 item 自带 index/routing）。
func (w *Writer) MGet(ctx context.Context, items []*elastic.MultiGetItem) ([]*elastic.GetResult, error) {
	res, err := w.c.Client.Mget().Add(items...).Do(ctx)
	if err != nil {
		return nil, err
	}
	return res.Docs, nil
}

// PutPipeline 创建 ingest pipeline（大文本场景做预处理，如字段拆分、低大小写）。
func (w *Writer) PutPipeline(ctx context.Context, id string, processors string) error {
	body := fmt.Sprintf(`{ "description": "%s", "processors": %s }`, id, processors)
	_, err := w.c.Client.IngestPutPipeline(id).BodyString(body).Do(ctx)
	return err
}

// Flush 把后台 bulk 强制刷出。
func (w *Writer) Flush() error { return w.bulk.Flush() }

// Close 关闭 bulk 处理器（内部会 flush 剩余请求）。
func (w *Writer) Close() error { return w.bulk.Close() }
