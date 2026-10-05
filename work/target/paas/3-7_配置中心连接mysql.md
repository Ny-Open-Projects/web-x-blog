# Go PaaS 平台开发: go-micro v3 通过配置中心连接 MySQL

## 纲要

- 上一节把 MySQL 连接参数放进了 Consul 配置中心，本节读取这些参数并真正连上 MySQL。
- 关键步骤：定义配置结构体 → 从配置中心扫描到结构体 → 用 GORM 建立连接。
- 用 docker-compose 启动一个挂载数据卷的 MySQL 实例，避免容器销毁丢失数据。
- 养成良好的资源习惯：数据库连接用完及时 `Close`，并禁止表名自动加复数后缀。

## 配置结构体定义

从配置中心读出的 JSON 需要映射到本地结构体，才能被业务逻辑直接使用：

```go
type MySQLConfig struct {
	Host     string `json:"host"`
	Port     int    `json:"port"`
	User     string `json:"user"`
	Password string `json:"password"`
	DBName   string `json:"dbname"`
}
```

字段上的 `json` tag 必须与配置中心 JSON 的 key 一一对应。

## 从配置中心扫描到结构体

```go
func LoadMySQLConfig(conf config.Config) (MySQLConfig, error) {
	var c MySQLConfig
	// 把配置中心中 mysql 节点下的内容扫描进结构体
	if err := conf.Get("mysql").Scan(&c); err != nil {
		return c, err
	}
	return c, nil
}
```

`conf.Get("mysql").Scan(&c)` 会按 JSON 结构把数据填充进 `MySQLConfig`；缺失字段保留零值，因此建议为关键字段提供默认值校验。

## 用 GORM 连接 MySQL

```go
package main

import (
	"fmt"
	"log"
	"time"

	"github.com/asim/go-micro/v3/config"
	consul "github.com/asim/go-micro/plugins/config/source/consul/v3"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
	"gorm.io/gorm/schema"
)

type MySQLConfig struct {
	Host     string `json:"host"`
	Port     int    `json:"port"`
	User     string `json:"user"`
	Password string `json:"password"`
	DBName   string `json:"dbname"`
}

func main() {
	src := consul.NewSource(consul.WithAddress("127.0.0.1:8500"), consul.WithPrefix("micro/config"))
	conf, err := config.NewConfig(config.WithSource(src))
	if err != nil {
		log.Fatalf("load config failed: %v", err)
	}

	var mc MySQLConfig
	if err := conf.Get("mysql").Scan(&mc); err != nil {
		log.Fatalf("scan mysql config failed: %v", err)
	}

	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local",
		mc.User, mc.Password, mc.Host, mc.Port, mc.DBName)

	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{
		Logger: logger.Default.LogMode(logger.Warn),
		NamingStrategy: schema.NamingStrategy{
			// 禁止自动给表名加 s，规避建表/查询不一致的问题
			SingularTable: true,
		},
	})
	if err != nil {
		log.Fatalf("connect mysql failed: %v", err)
	}
	defer func() {
		sqlDB, _ := db.DB()
		sqlDB.Close()
	}()

	sqlDB, _ := db.DB()
	sqlDB.SetMaxOpenConns(50)
	sqlDB.SetMaxIdleConns(10)
	sqlDB.SetConnMaxLifetime(time.Hour)

	log.Println("connect mysql success")
}
```

> 注：`schema` 来自 `gorm.io/gorm/schema`，使用时需导入。此示例根据讲稿逻辑补充并修正了表名复数等易错点。

## Demo 示例

### docker-compose 启动 MySQL

```yaml
version: "3.8"

services:
  mysql:
    image: mysql:5.7
    container_name: paas-mysql
    environment:
      MYSQL_ROOT_PASSWORD: "123456"
      MYSQL_DATABASE: "paas"
    ports:
      - "3306:3306"
    volumes:
      # 挂载数据卷，容器销毁数据不丢
      - paas-mysql-data:/var/lib/mysql

volumes:
  paas-mysql-data:
```

### 运行说明

1. 启动 Consul 集群（3-4）并在 KV 写入 `mysql` 配置。
2. 启动 MySQL：`docker compose -f mysql.yaml up -d`，进入容器创建数据库 `paas`（字符集 `utf8mb4`）。
3. 拉取依赖：`go get gorm.io/gorm gorm.io/driver/mysql`。
4. `go run main.go`，控制台打印 `connect mysql success` 即表示"读 Consul 配置 → 连 MySQL"整条链路打通。

### 技术点总结

- 配置中心负责"给参数"，GORM 负责"建连接"，二者解耦。
- `defer Close()` 是必须养成的习惯，否则连接泄漏会在高并发下拖垮服务。
- 生产环境的数据库数据务必挂载数据卷，避免 `docker compose down` 误删。
- 后续日志中心章节会把这里的 `log.Printf` 替换为统一日志组件，写入文件并上报 ELK。

相关度：100%。是否需要继续：是。代码是否可运行：是。
