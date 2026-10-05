// Package cache 多级缓存：用 Redis 缓存搜索结果，并对 value 做压缩，
// 减少网络与内存开销（对应《提升搜索性能之多级缓存策略》《Go中正确使用Redis与压缩缓存》）。
package cache

import (
	"bytes"
	"compress/gzip"
	"context"
	"fmt"
	"io"
	"time"

	"github.com/redis/go-redis/v9"
)

// SearchCache 搜索结果缓存（两级：本地 L1 由调用方持有，这里实现 Redis L2）。
type SearchCache struct {
	rdb *redis.Client
	ttl time.Duration
}

// New 连接 Redis。addr 形如 redis://localhost:6379。
func New(addr string, ttl time.Duration) (*SearchCache, error) {
	opt, err := redis.ParseURL(addr)
	if err != nil {
		return nil, fmt.Errorf("parse redis url: %w", err)
	}
	rdb := redis.NewClient(opt)
	return &SearchCache{rdb: rdb, ttl: ttl}, nil
}

// Set 压缩后写入 Redis（大搜索结果压缩能显著省内存/带宽）。
func (c *SearchCache) Set(ctx context.Context, key string, value []byte) error {
	compressed, err := gzipCompress(value)
	if err != nil {
		return err
	}
	return c.rdb.Set(ctx, key, compressed, c.ttl).Err()
}

// Get 读取并解压；命中返回 (data, true, nil)，未命中返回 (nil, false, nil)。
func (c *SearchCache) Get(ctx context.Context, key string) ([]byte, bool, error) {
	raw, err := c.rdb.Get(ctx, key).Bytes()
	if err == redis.Nil {
		return nil, false, nil
	}
	if err != nil {
		return nil, false, err
	}
	data, err := gzipDecompress(raw)
	if err != nil {
		return nil, false, err
	}
	return data, true, nil
}

// Close 关闭连接。
func (c *SearchCache) Close() error { return c.rdb.Close() }

func gzipCompress(b []byte) ([]byte, error) {
	var buf bytes.Buffer
	gw := gzip.NewWriter(&buf)
	if _, err := gw.Write(b); err != nil {
		return nil, err
	}
	if err := gw.Close(); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

func gzipDecompress(b []byte) ([]byte, error) {
	gr, err := gzip.NewReader(bytes.NewReader(b))
	if err != nil {
		return nil, err
	}
	defer gr.Close()
	return io.ReadAll(gr)
}
