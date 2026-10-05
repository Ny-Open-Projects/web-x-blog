# Go 企业级抽奖项目: 定义数据库和 Redis 配置

## 纲要

- 在 `conf` 包中分别定义数据库配置与 Redis 配置两个结构体
- 数据库配置 `DbConfig`：驱动、Host、Port、User、Pwd、Database、状态
- Redis 配置 `RdsConfig`：Host、Port、User、Pwd、运行状态
- 配置用**切片**保存，支持一主多从或多节点；同时提供可直接使用的单例（`DbMaster`、`RdsCache`）
- 本地默认配置：MySQL `127.0.0.1:3306`、Redis `127.0.0.1:6379`

## 数据库配置

先建一个数据库配置文件，定义连接所需的结构体。数据源类型这里用 `mysql`，所以驱动字段记为 `mysql`：

```go
type DbConfig struct {
	DriverName string // 驱动类型，如 mysql
	Host       string // IP
	Port       int    // 端口
	User       string // 登录用户名
	Pwd        string // 密码
	Database   string // 使用的数据库名
	IsRunning  bool   // 是否正常运行（预留）
}
```

配置不一定只有一个（主从、多库），所以用切片承载：

```go
// 系统中用到的所有数据库资源
var DbMasterList = []DbConfig{
	{
		DriverName: "mysql",
		Host:       "127.0.0.1",
		Port:       3306,
		User:       "root",
		Pwd:        "password",
		Database:   "lottery",
		IsRunning:  true,
	},
}

// 直接可用的单例主库配置
var DbMaster = DbMasterList[0]
```

后续创建数据库实例时，直接取 `conf.DbMaster` 即可，无需每次从头拼连接串。

## Redis 配置

Redis 配置与数据库配置高度相似。下面是项目 `conf/redis.go` 中的真实定义：

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

Redis 同样支持用户名/密码鉴权（部分部署会要求），因此结构里保留了 `User`、`Pwd`。本地默认端口是 `6379`，密码为空。`RdsCache` 取切片第一个，作为全局直接可用的缓存配置单例。

## 配置组织方式小结

| 配置项 | 数据库 | Redis |
| --- | --- | --- |
| 结构体 | `DbConfig` | `RdsConfig` |
| 连接要素 | DriverName/Host/Port/User/Pwd/Database | Host/Port/User/Pwd |
| 集合 | `DbMasterList []DbConfig` | `RdsCacheList []RdsConfig` |
| 单例 | `DbMaster` | `RdsCache` |
| 本地默认值 | `127.0.0.1:3306 / lottery` | `127.0.0.1:6379` |

用“切片 + 单例”的组织方式，既能横向扩展多个节点，又为调用方提供了最省事的 `conf.DbMaster` / `conf.RdsCache` 直取入口。

## API 速览

- `conf.DbConfig` / `conf.RdsConfig`：配置结构体
- `conf.DbMaster DbConfig`：直接可用的主库配置单例
- `conf.RdsCache RdsConfig`：直接可用的 Redis 配置单例
- `conf.DbMasterList` / `conf.RdsCacheList`：配置集合，支持多节点

## Demo 示例

下面给出一个可运行的最小配置示例（仅演示配置定义与读取，无需外部依赖）：

```go
package main

import "fmt"

type DbConfig struct {
	DriverName string
	Host       string
	Port       int
	User       string
	Pwd        string
	Database   string
}

type RdsConfig struct {
	Host string
	Port int
	User string
	Pwd  string
}

var DbMaster = DbConfig{"mysql", "127.0.0.1", 3306, "root", "password", "lottery"}
var RdsCache = RdsConfig{"127.0.0.1", 6379, "", ""}

func main() {
	fmt.Printf("db: %s@tcp(%s:%d)/%s\n",
		DbMaster.User, DbMaster.Host, DbMaster.Port, DbMaster.Database)
	fmt.Printf("redis: %s:%d\n", RdsCache.Host, RdsCache.Port)
}
```

运行说明：直接 `go run main.go`，输出数据库与 Redis 的连接信息。

代码说明：该示例对应 `conf` 包的配置定义形态，真实项目中 `DbMaster`/`RdsCache` 来自切片首元素，且字段更多（含 `IsRunning`）。

技术点总结：数据库与 Redis 配置各自用结构体描述，统一放在 `conf` 包；用切片支持多节点，再用包级单例（`DbMaster`/`RdsCache`）提供最便捷的取值入口；字段命名遵循 Go 导出规范，便于 `datasource` 在创建实例时直接读取。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/conf/redis.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
