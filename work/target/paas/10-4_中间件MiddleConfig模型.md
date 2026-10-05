# Go PaaS 平台开发: 中间件默认配置模型 MiddleConfig 设计

## 纲要

- 许多中间件（如 MySQL、Redis）在初始化时会自动生成账号密码或预置数据库，这些信息需要持久化。
- `MiddleConfig` 以一对一方式关联 `Middleware`，与端口、环境变量、存储等「一对多」子表不同。
- 模型保存 root 账户/密码、普通账户/密码、预置数据库名等可选字段。
- 不同中间件类型所需的配置不同：MySQL 需要初始化账号与数据库，而 Consul、Redis 通常不需要。

## 配置模型

```go
package model

// 中间件配置的结构体
type MiddleConfig struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	// 关联的中间件 ID
	MiddleID int64 `json:"middle_id"`
	// 可能存在的 root 用户
	MiddleConfigRootUser string `json:"middle_config_root_user"`
	// 可能存在的 root 密码
	MiddleConfigRootPwd string `json:"middle_config_root_pwd"`
	// 可能存在的普通用户
	MiddleConfigUser string `json:"middle_config_user"`
	// 普通用户的密码
	MiddleConfigPwd string `json:"middle_config_pwd"`
	// 预置数据库名称
	MiddleConfigDataBase string `json:"middle_config_data_base"`
	// 其它设置
}
```

### 字段说明

- `MiddleID`：外键，与主模型一对一关联。
- `MiddleConfigRootUser` / `MiddleConfigRootPwd`：root 账户与密码，仅当中间件支持初始化 root 时才填写。
- `MiddleConfigUser` / `MiddleConfigPwd`：普通业务账户及密码。
- `MiddleConfigDataBase`：创建实例时一并初始化的数据库名。

## 与主模型的关联

```go
// 中间件主模型中的配置字段（一对一）
MiddleConfig MiddleConfig `gorm:"ForeignKey:MiddleID" json:"middle_config"`
```

## 类型差异处理

配置是否必填取决于中间件类型，这一点在对外 API 层体现得最为明显：前端为 MySQL 展示 root 账号、普通账号、预置数据库等表单；而 Consul、Redis 的创建表单则不展示这些字段。后端在解析请求时，也会依据 `MiddleTypeName` 判断是否需要填充 `MiddleConfig`：

```go
// middlewareapi handler 中的类型分支
switch middleTypeInfo.MiddleTypeName {
case "MYSQL":
	middleConfig := e.setMiddleConfig(req)
	addMiddleInfo.MiddleConfig = &middleConfig
}
```

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/docker-compose/chapter3/prometheus.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：否（模型定义，需配合 GORM 初始化与 API 层使用）。
