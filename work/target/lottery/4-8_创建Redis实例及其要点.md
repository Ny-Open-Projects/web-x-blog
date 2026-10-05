# Go 企业级抽奖项目: 创建 Redis 实例及其要点

## 纲要

- Redis 连接配置：通过 `conf.RdsConfig` 描述单个 Redis 节点的地址、端口、账号与运行状态。
- 单例模式（Singleton）：全局只持有一个 Redis 连接池，避免重复建连。
- 连接池（Connection Pool）：使用 `redigo` 的 `redis.Pool`，配置最大空闲、最大活跃、空闲超时等参数。
- 命令封装：封装最底层的 `Do` 方法，统一执行任意 Redis 命令，并在内部做连接借还、耗时统计与异常打印。
- 耗时统计：每次命令记录起止时间戳（纳秒），换算为微秒打印，便于线上排查慢查询。

## Redis 连接配置

项目把 Redis 的连接信息集中放在 `conf` 包中，支持配置多个缓存节点，并默认取第一个可用的节点：

```go
package conf

type RdsConfig struct {
	Host      string
	Port      int
	User      string
	Pwd       string
	IsRunning bool // 是否正常运行
}

// 系统中用到的所有 redis 缓存资源
var RdsCacheList = []RdsConfig{
	{
		Host:      "127.0.0.1",
		Port:      6379,
		User:      "",
		Pwd:       "",
		IsRunning: true,
	},
}

var RdsCache RdsConfig = RdsCacheList[0]
```

> 说明：XORM 对数据源有内置支持，但 Redis 相对“原生”，因此连接池与命令执行需要我们自己封装。

## 单例模式与连接池设计

Redis 客户端一般使用连接池来管理 TCP 连接。连接池有两个基本动作：从池里 `Get` 一个连接，用完之后 `Close` 归还。`redigo` 在 `Close` 时并不会关闭底层 TCP 连接，而是把连接状态复位后放回池中复用。

为了保证整个进程只初始化一次连接池，我们用 `sync.Once` 实现单例：

```go
package datasource

import (
	"sync"

	"imooc.com/lottery/conf"
	"github.com/gomodule/redigo/redis"
)

var (
	cacheInstance *redis.Pool
	cacheOnce     sync.Once
)

// InstanceCache 返回全局唯一的 Redis 连接池（单例）
func InstanceCache() *redis.Pool {
	cacheOnce.Do(func() {
		cacheInstance = newCache()
	})
	return cacheInstance
}
```

`newCache` 负责建立连接池，核心是 `Dial` 函数：通过 TCP 连接 Redis 的 `IP:Port`，连接失败直接返回错误中断；连接成功则将连接交回池中。生产环境可根据实际情况微调 `MaxIdle`、`MaxActive`、`IdleTimeout` 等参数：

```go
// newCache 创建 Redis 连接池
func newCache() *redis.Pool {
	return &redis.Pool{
		MaxIdle:     10,                // 最大空闲连接数
		MaxActive:   10000,             // 最大活跃连接数
		IdleTimeout: 180 * time.Second, // 空闲连接的超时时间
		Dial: func() (redis.Conn, error) {
			c, err := redis.Dial("tcp",
				fmt.Sprintf("%s:%d", conf.RdsCache.Host, conf.RdsCache.Port))
			if err != nil {
				return nil, err
			}
			return c, nil
		},
	}
}
```

> 上述 `InstanceCache` / `newCache` 为实现思路示意（根据讲稿逻辑补充）。`cacheInstance` 为小写私有变量，外部无法直接访问，必须通过公开的 `InstanceCache()` 获取，这也是单例封装的意义。

## Do 方法封装与执行耗时统计

连接池之上，我们封装一个最底层、最通用的 `Do` 方法。它接受命令名和任意多个参数，因为返回值类型未知（可能是字符串、整数、数组等），所以统一用 `interface{}` 承载，出错时返回 `error`。

关键点：

- 从池中取出连接 `conn := InstanceCache().Get()`，结束时必须 `defer conn.Close()` 归还。
- 调用 `conn.Do(commandName, args...)` 执行命令。
- 记录命令执行前后时间戳，换算为微秒，打印命令名、参数、返回值与耗时，用于调试与异常排查。

```go
import (
	"fmt"
	"time"

	"imooc.com/lottery/conf"
	"github.com/gomodule/redigo/redis"
)

// Do 执行任意 Redis 命令，并打印执行耗时，便于调试
func Do(commandName string, args ...interface{}) (interface{}, error) {
	conn := InstanceCache().Get()
	defer conn.Close()

	t1 := time.Now().UnixNano()
	reply, err := conn.Do(commandName, args...)
	t2 := time.Now().UnixNano()

	// 换算为微秒
	usec := (t2 - t1) / 1000
	if err != nil {
		// 异常处理：打印命令与错误信息，避免静默失败
		fmt.Printf("redis Do error: command=%s, usec=%d, err=%v\n",
			commandName, usec, err)
		return nil, err
	}
	fmt.Printf("redis Do: command=%s, usec=%d, reply=%v\n",
		commandName, usec, reply)
	return reply, nil
}
```

## 设计要点小结

- 单例 + 连接池：全局只建一次连接池，连接复用，降低 TCP 握手成本。
- 连接归还：务必 `defer Close()`，否则连接泄漏会拖垮 Redis。
- 通用 Do：用 `interface{}` + 变参屏蔽命令差异，再叠加耗时统计，使后续业务层调用简单且可观测。
- 配置外置：`conf.RdsConfig` 集中管理节点信息，业务代码几乎无需修改即可适配不同环境。

## API 速览

| 方法 / 类型 | 说明 | 关键参数 | 返回值 |
| --- | --- | --- | --- |
| `redis.Pool` | redigo 连接池类型 | `MaxIdle` / `MaxActive` / `IdleTimeout` / `Dial` | `*redis.Pool` |
| `redis.Dial(network, addr)` | 建立一条 TCP 连接 | `"tcp"` / `"host:port"` | `redis.Conn, error` |
| `conn.Do(cmd, args...)` | 执行单条命令 | 命令名 + 变参 | `interface{}, error` |
| `conn.Close()` | 归还连接到池中 | 无 | `error` |
| `InstanceCache()` | 单例获取连接池 | 无 | `*redis.Pool` |

示例：

```go
// 写入与读取一个字符串
_, _ = Do("SET", "lottery:demo", "hello")
reply, _ := redis.String(Do("GET", "lottery:demo"))
fmt.Println(reply) // hello
```

## Demo 示例

运行说明：示例依赖 `github.com/gomodule/redigo/redis`，本地需启动一个 `127.0.0.1:6379` 的 Redis 实例。

```go
package main

import (
	"fmt"
	"time"

	"github.com/gomodule/redigo/redis"
)

func newCache() *redis.Pool {
	return &redis.Pool{
		MaxIdle:     10,
		MaxActive:   100,
		IdleTimeout: 180 * time.Second,
		Dial: func() (redis.Conn, error) {
			return redis.Dial("tcp", "127.0.0.1:6379")
		},
	}
}

func Do(conn redis.Conn, cmd string, args ...interface{}) (interface{}, error) {
	t1 := time.Now().UnixNano()
	reply, err := conn.Do(cmd, args...)
	t2 := time.Now().UnixNano()
	fmt.Printf("cmd=%s usec=%d err=%v\n", cmd, (t2-t1)/1000, err)
	return reply, err
}

func main() {
	pool := newCache()
	conn := pool.Get()
	defer conn.Close()

	Do(conn, "SET", "k", "v")
	v, _ := redis.String(Do(conn, "GET", "k"))
	fmt.Println("GET k =", v)
}
```

代码说明：把连接池、`Do` 耗时统计浓缩成一个最小可运行示例，验证单例连接池与命令封装思路。

技术点总结：单例保证唯一连接池；连接池提升并发下的连接复用率；`Do` 统一封装让业务层无需关心连接借还与耗时埋点；耗时微秒级打印是排查线上慢命令的第一道观测手段。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/conf/redis.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
