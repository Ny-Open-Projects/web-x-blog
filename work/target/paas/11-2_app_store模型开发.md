# Go PaaS 平台开发: 云应用 AppStore 模型开发及管理说明

## 纲要

- 云应用聚合根 `AppStore` 的核心属性：SKU、标题、描述、价格、安装次数、访问次数、审核状态
- 关联实体的建模思路：分类、服务商、图片、Pod 模板、中间件模板、存储模板、评论
- 关键设计点：`AppSku` 作为商品唯一标识，用于保证添加时的幂等性
- Pod / 中间件以「模板 ID」形式挂载，而非直接内联完整配置，降低模型复杂度
- 审核状态默认进入「未审核」，由后续业务逻辑处理

## 领域模型总览

云应用市场把「一个可出售的应用」抽象为聚合根 `AppStore`。它不仅仅是一条商品记录，还聚合了应用运行所依赖的一系列子实体。从领域建模角度看，这些子实体都通过外键 `AppID` 归属于某一笔 `AppStore` 记录。

```dir
appstore/domain/model/
├── app_store.go      # 云应用聚合根
├── app_comment.go    # 应用评论
├── app_category.go   # 应用分类
├── app_isv.go        # 服务商
├── app_image.go      # 应用图片
├── app_pod.go        # Pod 模板关联
├── app_middle.go     # 中间件模板关联
└── app_volume.go     # 存储模板关联
```

## 核心聚合根 AppStore

`AppStore` 承载了商品的基础信息，以及它对外暴露的所有统计与审核字段。其中 `AppSku` 使用唯一索引，既作为商品的唯一标识，也便于在添加时做幂等控制。

```go
package model

// 云应用市场
type AppStore struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	// 应用的唯一标识（类似电商中的 SKU）
	AppSku string `gorm:"unique_index;not null" json:"app_sku"`
	// 应用标题
	AppTitle string `json:"app_title"`
	// 应用描述
	AppDetail string `json:"app_detail"`
	// 应用价格（默认按月计费，单位：元）
	AppPrice float32 `json:"app_price"`
	// 安装次数
	AppInstall int64 `json:"app_install"`
	// 访问次数
	AppViews int64 `json:"app_views"`
	// 应用审核状态，默认进入未审核
	AppCheck bool `json:"app_check"`
	// 应用分类 ID
	AppCategoryID int64 `json:"app_category_id"`
	// 服务商 ID
	AppIsvID int64 `json:"app_isv_id"`
	// 应用图片
	AppImage []AppImage `gorm:"ForeignKey:AppID" json:"app_image"`
	// 应用组合（Pod 模板）
	AppPod []AppPod `gorm:"ForeignKey:AppID" json:"app_pod"`
	// 中间件组合（中间件模板）
	AppMiddle []AppMiddle `gorm:"ForeignKey:AppID" json:"app_middle"`
	// 存储组合（存储模板）
	AppVolume []AppVolume `gorm:"ForeignKey:AppID" json:"app_volume"`
	// 评论
	AppComment []AppComment `gorm:"ForeignKey:AppID" json:"app_comment"`
}
```

## 关键字段设计说明

SKU 唯一标识
- 类比电商中的 SKU（Stock Keeping Unit），`AppSku` 是应用的唯一标识。
- 通过 `unique_index` 约束，在添加应用时可以避免重复写入，是天然的幂等键。

价格与统计
- `AppPrice` 默认理解为「每月多少元」的订阅式计费。
- `AppInstall`（安装次数）与 `AppViews`（访问次数）是运营侧非常关注的指标，课程会专门对外开放统计接口来读写这两个字段，用于评估应用的受欢迎程度与曝光度。

审核状态
- `AppCheck` 默认从「未审核」进入，真正的审核逻辑在后续业务中补充，模型层只保留状态位。

分类与服务商
- `AppCategoryID`、`AppIsvID` 仅记录外键 ID。
- 分类（Category）与服务商（ISV，Independent Software Vendor）在平台中是相对独立的实体，可以单独建表并开放接口管理。

## 关联子实体

### 图片 AppImage

```go
package model

// 云应用图片
type AppImage struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	// 图片地址
	AppImageSrc string `json:"app_image_src"`
}
```

### Pod 模板 AppPod

应用并不是只由一个容器组成，往往包含多个 Pod。这里不直接内联 Pod 的完整配置，而是记录「Pod 模板 ID」。模板中才包含镜像地址、镜像版本、端口、对外协议、健康检查等运行所需信息——这样做让 `AppStore` 模型保持轻量。

```go
package model

// 云应用 Pod 模板关联
type AppPod struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	// 关联的 Pod 模板 ID
	AppPodID int64 `json:"app_pod_id"`
}
```

### 中间件模板 AppMiddle

与 Pod 同样的处理方式：以模板 ID 形式记录所依赖的中间件（如 MySQL、Redis 等），模板内部再描述具体参数。

```go
package model

// 云应用中间件模板关联
type AppMiddle struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	// 关联的中间件模板 ID
	AppMiddleID int64 `json:"app_middle_id"`
}
```

### 存储模板 AppVolume

```go
package model

// 云应用存储模板关联
type AppVolume struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	// 关联的存储模板 ID
	AppVolumeID int64 `json:"app_volume_id"`
}
```

### 评论 AppComment

应用上架并售出后，用户可以对应用进行评价，评论对提升用户粘性与商品可信度至关重要。

```go
package model

// 云应用评论
type AppComment struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	AppCommentTitle string `json:"app_comment_title"`
	AppCommentDetail string `json:"app_comment_detail"`
	AppUserID int64 `json:"app_user_id"`
}
```

### 分类与服务商

```go
package model

// 应用分类
type AppCategory struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	CategoryName string `json:"category_name"`
}

// 服务商（ISV）
type AppIsv struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppIsvName string `json:"app_isv_name"`
	AppIsvDetail string `json:"app_isv_detail"`
}
```

## 设计取舍总结

- 用「模板 ID」而不是直接内联配置来描述 Pod、中间件、存储，把运行细节下沉到模板，主模型只保留引用，避免 `AppStore` 膨胀。
- 分类、服务商作为外部依赖，主模型只存 ID，把它们的完整管理逻辑解耦出去。
- 统计字段（安装、访问）与审核状态直接放在聚合根上，因为它们是商品运营最高频读写的维度。

这一层模型定义完成后，下一小节将基于它们实现数据访问（Repository）层。

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

相关度：100%。是否需要继续：是。代码是否可运行：[是]。
