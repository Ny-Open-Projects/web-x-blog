# Go PaaS 平台开发: Main 入口与基础中间件初始化（上）

## 纲要

- main.go 先声明变量：服务端口、熔断器监控端口、注册中心地址、配置中心地址
- 引入注册中心（go-micro registry）与配置中心（config），地址统一管理
- 从配置中心读取 MySQL 配置，拼装 DSN 并用 `sql.Open` 建立连接
- 用 GORM `Open` 包装出 `*gorm.DB`，记得 `defer db.Close()`
- App 应用侧模型（AppPod / AppCategory / AppMiddle / AppVolume / AppIsv / AppImage）构成应用商店骨架

## main.go 的职责

main.go 是程序入口，本小节先把"基础中间件"搭起来：注册中心、配置中心、MySQL 连接。这些是所有微服务共用的底座。变量在每个环境上取值不同（本机开发端口可能冲突，需手动错开），但 K8s 内部以 Service 暴露，端口可统一。

## 变量声明

```go
package main

import "fmt"

// 服务端口（控制配置使用），int64 类型便于与注册中心参数对齐
var (
	serverPort   int64 = 8080
	monitorPort  int64 = 9090 // 熔断器 hystrix 监控端口，每台应用需不同
)
```

> 如果本服务不作为客户端去访问别的服务，端口与熔断器可以不写；作为服务端时加上熔断器，作为客户端时再加上监控端口。同一主机部署多个服务务必错开监控端口。

## 注册中心与配置中心

```go
import (
	"github.com/micro/go-micro/v3/registry"
	"github.com/micro/go-micro/v3/config"
	_common "git.imooc.com/coding-535/common" // 课程通用包
)

func main() {
	// 1. 注册中心（地址来自前面声明的变量）
	reg := registry.NewRegistry(
		registry.Address("127.0.0.1:2379"), // 如 etcd/consul 地址
	)
	// 名称可定为 "registry" 之类，便于识别

	// 2. 配置中心：复用注册中心存经常变动的配置（key-value 形式）
	cfg, err := config.NewConfig(
		config.WithRegistry(reg),
	)
	if err != nil {
		// 出错先记录到日志文件，不直接 panic 退出
		_common.LogError(err)
	}
}
```

配置中心从注册中心中读取 MySQL 等易变配置，避免硬编码。

## MySQL 连接

```go
import (
	"database/sql"
	"fmt"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

func initMysql(cfg config.Config) (*gorm.DB, error) {
	// 从配置中心取出 mysql 配置结构体（已在 common 中定义）
	type mysqlConf struct {
		User     string `json:"user"`
		Pwd      string `json:"pwd"`
		Host     string `json:"host"`
		Port     string `json:"port"`
		DbName   string `json:"db_name"`
	}
	var mc mysqlConf
	if err := cfg.Get("mysql").Scan(&mc); err != nil {
		return nil, err
	}

	// 拼装 DSN（格式固定）
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?charset=utf8&parseTime=true",
		mc.User, mc.Pwd, mc.Host, mc.Port, mc.DbName)

	// 建立标准库连接（调试阶段可用 fmt.Println 打印，生产环境移除）
	sqlDB, err := sql.Open("mysql", dsn)
	if err != nil {
		return nil, err
	}

	// 用 GORM 包装
	db, err := gorm.Open("mysql", sqlDB)
	if err != nil {
		return nil, err
	}
	// 用完后务必关闭，长期占用会影响 MySQL 使用
	// defer db.Close()
	return db, nil
}
```

> 调试阶段可用 `fmt.Println` 把 DSN 打到终端直接观察；生产环境应移除明文打印，改为 `common` 包的错误记录。连接使用完记得 `defer db.Close()`，否则连接泄漏会影响 MySQL。

## 应用商店侧模型

5-13 关联的模型文件构成"应用商店"骨架（来自 `appstore/domain/model`）：

```go
// 应用分类
type AppCategory struct {
	ID           int64  `gorm:"primary_key;not_null;auto_increment"`
	CategoryName string `json:"category_name"`
}

// 应用与 Pod 的关联
type AppPod struct {
	ID       int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID    int64 `json:"app_id"`
	AppPodID int64 `json:"app_pod_id"`
}

// 应用与中间件的关联
type AppMiddle struct {
	ID          int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID       int64 `json:"app_id"`
	AppMiddleID int64 `json:"app_middle_id"`
}

// 应用存储模板
type AppVolume struct {
	ID         int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID      int64 `json:"app_id"`
	AppVolumeID int64 `json:"app_volume_id"`
}

// 服务商
type AppIsv struct {
	ID           int64  `gorm:"primary_key;not_null;auto_increment"`
	AppIsvName   string `json:"app_isv_name"`
	AppIsvDetail string `json:"app_isv_detail"`
}

// 云应用图片
type AppImage struct {
	ID          int64  `gorm:"primary_key;not_null;auto_increment"`
	AppID       int64  `json:"app_id"`
	AppImageSrc string `json:"app_image_src"`
}
```

这些模型通过 `AppID` 把分类、Pod、中间件、存储、服务商、图片关联起来，是"产品化应用"的数据底座。

## API 速览

| 步骤 | 动作 | 关键 API |
| --- | --- | --- |
| 注册中心 | `registry.NewRegistry(registry.Address(...))` | go-micro v3 |
| 配置中心 | `config.NewConfig(config.WithRegistry(reg))` | go-micro v3 |
| MySQL | `sql.Open("mysql", dsn)` → `gorm.Open` | database/sql + gorm |

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/base/domain/model/base.go`
- `code/课件/appstore/domain/model/app_category.go`
- `code/课件/appstore/domain/model/app_pod.go`
- `code/课件/appstore/domain/model/app_middle.go`
- `code/课件/appstore/domain/model/app_volume.go`
- `code/课件/appstore/domain/model/app_isv.go`
- `code/课件/pod/domain/model/pod_env.go`
- `code/课件/appstore/domain/model/app_image.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
