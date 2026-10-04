---
disableNunjucks: true
title: "Go 项目开发: Go 中正确使用 Redis 与压缩缓存"
date: 2026-10-02 09:20:00
categories: [es, Go, Redis]
tags: [Redis, go-redis, GZIP, 连接池, 压缩缓存]
---

# Go 项目开发: Go 中正确使用 Redis 与压缩缓存

Redis 用对了是性能利器，用错了是内存黑洞。这一节讲两件事：**怎么封装一个能同时支持单机与集群的 Redis 客户端**，以及**怎么用 GZIP 压缩给 Redis 省内存**。

## 纲要

- 客户端封装：单机版与集群版分开初始化
- 连接参数的合理默认值
- 集群版初始化的一个阻塞坑
- 统一的 Set/Get 与慢操作日志
- 压缩缓存：JSON + GZIP
- 压缩的额外收益：HTTP GZIP 直通

## 客户端封装

基于 `github.com/redis/go-redis/v9` 封装，核心结构是把**单机客户端与集群客户端**放进同一个结构体：

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"time"

	"github.com/redis/go-redis/v9"
)

// RedisClient 同时持有单机与集群客户端，用 nil 区分当前模式
type RedisClient struct {
	standalone *redis.Client        // 单机版
	cluster    *redis.ClusterClient // 集群版
	slowLog    time.Duration        // 超过该耗时的操作打印告警
}

// InitRedis 初始化单机版客户端
func InitRedis(ctx context.Context, clientName, addr string) (*RedisClient, error) {
	if clientName == "" {
		return nil, errors.New("client name is required")
	}
	if addr == "" {
		return nil, errors.New("redis addr is required")
	}

	c := redis.NewClient(&redis.Options{
		Addr:            addr,
		DialTimeout:     2 * time.Second,  // 连接超时
		ReadTimeout:     3 * time.Second,  // 读超时
		PoolTimeout:     4 * time.Second,  // 连接池超时 = 读超时 + 1s
		ConnMaxIdleTime: 10 * time.Second, // 空闲超时（v9 由 IdleTimeout 改名）：连接池可复用，别太快失效
	})

	if err := c.Ping(ctx).Err(); err != nil {
		return nil, fmt.Errorf("ping redis: %w", err)
	}
	log.Printf("redis [%s] connected", clientName)
	return &RedisClient{standalone: c, slowLog: 200 * time.Millisecond}, nil
}

// InitClusterRedis 初始化集群版客户端，直接透传原生 Options
func InitClusterRedis(ctx context.Context, clientName string, opts *redis.ClusterOptions) (*RedisClient, error) {
	if clientName == "" {
		return nil, errors.New("client name is required")
	}
	c := redis.NewClusterClient(opts)

	// 注意：NewClusterClient 会尝试连接并发送 CLUSTER INFO，
	// 如果传入的所有地址都连不上，这里会阻塞很长时间
	if err := c.Ping(ctx).Err(); err != nil {
		return nil, fmt.Errorf("ping cluster: %w", err)
	}
	return &RedisClient{cluster: c, slowLog: 200 * time.Millisecond}, nil
}

// Set 统一的 Set：单机与集群走同一段逻辑，按 nil 区分
func (r *RedisClient) Set(ctx context.Context, key, value string, ttl time.Duration) error {
	if len(key) == 0 {
		return errors.New("empty key")
	}
	start := time.Now()
	var err error
	if r.standalone != nil {
		err = r.standalone.Set(ctx, key, value, ttl).Err()
	} else {
		err = r.cluster.Set(ctx, key, value, ttl).Err()
	}
	if cost := time.Since(start); cost > r.slowLog {
		log.Printf("slow op: set key=%s ttl=%s cost=%s", key, ttl, cost)
	}
	return err
}

// Get 统一的 Get
func (r *RedisClient) Get(ctx context.Context, key string) (string, error) {
	if r.standalone != nil {
		return r.standalone.Get(ctx, key).Result()
	}
	return r.cluster.Get(ctx, key).Result()
}

func main() {
	ctx := context.Background()
	cli, err := InitRedis(ctx, "default", "127.0.0.1:6379")
	if err != nil {
		log.Fatalf("init: %v", err)
	}

	if err := cli.Set(ctx, "demo:key", "hello redis", time.Minute); err != nil {
		log.Fatalf("set: %v", err)
	}
	v, err := cli.Get(ctx, "demo:key")
	fmt.Println("get:", v, "err:", err)
}
```

依赖：

```bash
go get github.com/redis/go-redis/v9
```

## 连接参数的合理默认值

| 参数 | 默认值 | 理由 |
| --- | --- | --- |
| `DialTimeout` | 2s | 连接超时 |
| `ReadTimeout` | 3s | 读超时 |
| `PoolTimeout` | 读超时 + 1s（4s） | 等待池连接的时间应略长于单次读 |
| `IdleTimeout` | 10s（默认 5s） | 空闲连接池可复用，**不希望太快失效** |

参数校验不能省：`clientName` 与连接地址缺一不可，直接抛错比静默用零值跑起来好得多。

## 集群版初始化的一个阻塞坑

集群版客户端初始化时直接透传原生 `Options` —— 因为 Redis 集群的配置项多、定制需求也多，把选择权留给调用方。

但要格外留意：**`NewClusterClient` 会向集群发起连接并尝试发送 `CLUSTER INFO` 指令，如果传入的多个地址全部连不上，它会阻塞很长时间**。初始化阶段要控制好超时，别让服务启动卡死在这一步。

另外，集群版的连接地址是一个**数组**（多个节点地址），这与单机版不同，所以 SDK 里两者分开初始化、分开取用（`GetRedisClient` / `GetRedisClusterClient`）。

## 统一的 Set/Get 与慢操作日志

单机版与集群版在基本操作上是一致的，可以放进同一个逻辑，通过"哪个客户端非 nil"来区分当前模式（也可以显式加一个字段标识模式，实现更清晰）。

每次 `Set` 前校验 **key 长度不能为 0**（无意义的请求直接报错）；操作耗时超过 `slowLog` 阈值时，打印 key、value、TTL 与耗时 —— 这条慢操作日志在线上排查"Redis 变慢"时非常有用。

## 压缩缓存：JSON + GZIP

内存资源宝贵。为了节省 Redis 集群的内存，可以在**业务端先压缩再存入**：把响应给前端的数据结构 **JSON 序列化后 GZIP 压缩**，再写入 Redis。

```go
package main

import (
	"bytes"
	"compress/gzip"
	"encoding/json"
	"fmt"
	"io"
)

// GZipEncode GZIP 压缩
func GZipEncode(data []byte) ([]byte, error) {
	var buf bytes.Buffer
	w := gzip.NewWriter(&buf)
	if _, err := w.Write(data); err != nil {
		return nil, err
	}
	// Close 会 flush 并写入尾部校验，必须调用
	if err := w.Close(); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

// GZipDecode GZIP 解压
func GZipDecode(data []byte) ([]byte, error) {
	r, err := gzip.NewReader(bytes.NewReader(data))
	if err != nil {
		return nil, err
	}
	defer r.Close()
	return io.ReadAll(r)
}

type Profile struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
}

// CacheSet 序列化 + 压缩后返回可存入 Redis 的字节
func CacheSet(profile Profile) ([]byte, error) {
	raw, err := json.Marshal(profile)
	if err != nil {
		return nil, err
	}
	return GZipEncode(raw)
}

// CacheGet 解压 + 反序列化还原
func CacheGet(data []byte) (*Profile, error) {
	raw, err := GZipDecode(data)
	if err != nil {
		return nil, err
	}
	var p Profile
	if err := json.Unmarshal(raw, &p); err != nil {
		return nil, err
	}
	return &p, nil
}

func main() {
	p := Profile{ID: 1, Name: "imooc"}

	blob, err := CacheSet(p)
	if err != nil {
		panic(err)
	}
	fmt.Printf("压缩后大小: %d bytes\n", len(blob))

	got, err := CacheGet(blob)
	if err != nil {
		panic(err)
	}
	fmt.Printf("还原: %+v\n", got)
}
```

**运行说明**

```bash
mkdir redis-gzip && cd redis-gzip
go mod init redis-gzip
go run main.go   # 本示例只用标准库，无需 Redis 即可验证压缩往返
```

**代码说明**

- `gzip.Writer` 用完必须 `Close()`，否则尾部校验数据没写入，解压会失败。
- 需要更高压缩比时用 `gzip.NewWriterLevel` 传入压缩级别，默认级别在 CPU 与体积之间比较均衡。
- 从 Redis 取出的数据是 `string`，解压前要先转成 `[]byte`。

**技术点总结**

- 单机与集群客户端用 nil 区分，基本操作共用一套逻辑。
- 慢操作日志（key + 耗时）是线上排查 Redis 变慢的第一线索。
- JSON + GZIP 的压缩缓存，在"响应给前端的场景"下收益最大。

## 压缩的额外收益：HTTP GZIP 直通

压缩缓存最大的妙处在 HTTP 场景：**序列化 + 压缩后的数据缓存进 Redis；缓存命中时直接作为 HTTP 的 GZIP 数据流响应给前端** —— 服务端完全不需要解压再重新压缩，省掉了两头 CPU 消耗。

```mermaid
graph LR
    A[业务数据] -->|JSON 序列化| B[GZIP 压缩]
    B -->|存入| C[Redis]
    C -->|命中| D[直接作为 HTTP GZIP 流响应]
    D --> E[前端 解压渲染]
```

数据若不是给 HTTP 用的，取出后走解压 + 反序列化还原即可。

## Redis 封装结构一览

```dir
Redis 客户端封装/
├── 初始化
│   ├── 单机版           InitRedis
│   └── 集群版           InitClusterRedis（阻塞坑）
├── 统一操作
│   ├── Set              key 校验 + 慢日志
│   └── Get
└── 压缩缓存
    ├── JSON 序列化
    ├── GZIP 压缩        省内存
    └── HTTP 直通        直接作 GZIP 流响应
```

## 总结

Redis 封装的两个关键决策：**连接参数给合理默认值并校验入参**（尤其是集群版初始化的阻塞坑），**给响应类缓存加一层 GZIP**（省内存还省 CPU）。这两件事做好，Redis 既是性能利器，也不会变成内存黑洞。

