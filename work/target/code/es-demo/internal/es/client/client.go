// Package client 封装 olivere/elastic/v7 客户端。
//
// 设计要点（对应课程《Go操作ES的技巧和注意事项》）：
//   - 一个进程可连多个集群：用 ClientSet 区分「读协调节点」与「写 ingest 节点」。
//   - 显式关闭 sniff：生产有专门协调节点时，不要让它把流量散到数据节点。
//   - 配多个地址：单点下线时 SDK 能自动切到其它节点。
//   - HTTPClient 可注入：单元测试用 httptest 拦截请求，无需真实集群。
package client

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/olivere/elastic/v7"
)

// Client 对 *elastic.Client 的轻封装，额外保存连接地址等元信息。
type Client struct {
	*elastic.Client
	urls []string
}

// Option 客户端选项（函数选项模式）。
type Option func(*config)

type config struct {
	urls        []string
	user        string
	password    string
	sniff       bool
	healthcheck bool
	hcInterval  time.Duration
	httpClient  *http.Client
}

// WithURLs 设置 ES 节点地址（建议 >=2 个）。
func WithURLs(urls ...string) Option { return func(c *config) { c.urls = urls } }

// WithBasicAuth 设置基础认证。
func WithBasicAuth(user, password string) Option {
	return func(c *config) { c.user, c.password = user, password }
}

// WithSniff 显式开/关 sniff（生产建议 false）。
func WithSniff(b bool) Option { return func(c *config) { c.sniff = b } }

// WithHealthcheck 开/关健康检查；interval 可选，省略则用默认 15s。
func WithHealthcheck(b bool, interval ...time.Duration) Option {
	return func(c *config) {
		c.healthcheck = b
		if len(interval) > 0 && interval[0] > 0 {
			c.hcInterval = interval[0]
		}
	}
}

// WithHTTPClient 注入自定义 *http.Client（测试用）。
func WithHTTPClient(h *http.Client) Option { return func(c *config) { c.httpClient = h } }

// New 新建一个 ES 客户端。
func New(opts ...Option) (*Client, error) {
	cfg := &config{sniff: false, healthcheck: true, hcInterval: 15 * time.Second}
	for _, o := range opts {
		o(cfg)
	}
	if len(cfg.urls) == 0 {
		cfg.urls = []string{"http://localhost:9200"}
	}

	esOpts := []elastic.ClientOptionFunc{
		elastic.SetURL(cfg.urls...),
		elastic.SetSniff(cfg.sniff),
		elastic.SetHealthcheck(cfg.healthcheck),
		elastic.SetHealthcheckInterval(cfg.hcInterval),
	}
	if cfg.user != "" || cfg.password != "" {
		esOpts = append(esOpts, elastic.SetBasicAuth(cfg.user, cfg.password))
	}
	if cfg.httpClient != nil {
		esOpts = append(esOpts, elastic.SetHttpClient(cfg.httpClient))
	}

	ec, err := elastic.NewClient(esOpts...)
	if err != nil {
		return nil, fmt.Errorf("elastic.NewClient: %w", err)
	}
	return &Client{Client: ec, urls: cfg.urls}, nil
}

// URLs 返回连接地址列表。
func (c *Client) URLs() []string { return c.urls }

// Ping 探测集群可达性，返回版本号。
func (c *Client) Ping(ctx context.Context) (string, error) {
	res, _, err := c.Client.Ping(c.urls[0]).Do(ctx)
	if err != nil {
		return "", err
	}
	return res.Version.Number, nil
}

// Health 返回集群健康状态（green/yellow/red）。
func (c *Client) Health(ctx context.Context) (string, error) {
	h, err := c.Client.ClusterHealth().Do(ctx)
	if err != nil {
		return "", err
	}
	return h.Status, nil
}

// Perform 直接调用任意 ES REST 端点（用于没有 typed 方法的运维/ILM/跨集群 API）。
// body 为空则不带请求体；返回原始响应 JSON 字符串。
func (c *Client) Perform(ctx context.Context, method, path, body string) (string, error) {
	var b interface{}
	if body != "" {
		b = json.RawMessage(body)
	}
	res, err := c.Client.PerformRequest(ctx, elastic.PerformRequestOptions{
		Method: method,
		Path:   path,
		Body:   b,
	})
	if err != nil {
		return "", err
	}
	return string(res.Body), nil
}

// ClientSet 读写分离的双客户端：读走协调节点，写走 ingest 节点。
type ClientSet struct {
	Read  *Client
	Write *Client
}

// NewClientSet 初始化读写两个客户端。
func NewClientSet(readURLs, writeURLs []string, user, password string) (*ClientSet, error) {
	rc, err := New(WithURLs(readURLs...), WithBasicAuth(user, password))
	if err != nil {
		return nil, fmt.Errorf("read client: %w", err)
	}
	wc, err := New(WithURLs(writeURLs...), WithBasicAuth(user, password))
	if err != nil {
		return nil, fmt.Errorf("write client: %w", err)
	}
	return &ClientSet{Read: rc, Write: wc}, nil
}
