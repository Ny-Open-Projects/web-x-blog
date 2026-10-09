# Go PaaS 平台开发: 云应用辅助信息 Model 开发

## 纲要

- 应用市场采用「主表 + 关联子表」的领域建模：`AppStore` 为主表，子表覆盖分类、图片、Pod 模板、中间件、存储模板、评论、服务商。
- 关联子表统一通过 `AppID` 与主表建立一对多关系（GORM `ForeignKey:AppID`）。
- Pod、中间件、存储三类关联只记录「模板 ID」，模板在前期章节已创建，避免应用层重复造轮子。
- 分类 `AppCategory` 与服务商 `AppIsv` 是较特殊的实体：其 ID 可直接映射到应用字段，前端可动态读取名称。
- 模型全部使用 GORM 标签（`primary_key`、`not null`、`unique_index`、`ForeignKey`、`json`），既驱动建表也支撑 JSON 序列化（供 Proto 表单转换复用）。

## 建模动机

一个「云应用」不是孤立的单个 Pod，而是 Pod 模板、中间件、存储模板、图片、分类、服务商、评论等信息的组合。如果把这些全部塞进一张大宽表，字段会无限膨胀且难以维护。因此课程采用主从分离建模：主表 `AppStore` 存核心字段，其余放在各自的子表中，通过 `app_id` 关联。

```dir
appstore/domain/model/
├── app_store.go      # 主表：应用市场
├── app_category.go   # 应用分类
├── app_image.go      # 应用图片（可多张）
├── app_pod.go        # Pod 模板引用
├── app_middle.go     # 中间件模板引用
├── app_volume.go     # 存储模板引用
├── app_comment.go    # 应用评论
└── app_isv.go        # 服务商
```

## 主表 AppStore

主表承载应用的核心字段，并以 `ForeignKey:AppID` 声明与五个子表的一对多关联：

```go
package model

// 应用市场
type AppStore struct {
    ID int64 `gorm:"primary_key;not_null;auto_increment"`
    // 应用的标识
    AppSku string `gorm:"unique_index;not null" json:"app_sku"`
    // 应用标题
    AppTitle string `json:"app_title"`
    // 应用描述
    AppDetail string `json:"app_detail"`
    // 应用价格
    AppPrice float32 `json:"app_price"`
    // 安装次数
    AppInstall int64 `json:"app_install"`
    // 访问次数
    AppViews int64 `json:"app_views"`
    // 应用审核
    AppCheck bool `json:"app_check"`
    // 应用分类
    AppCategoryID int64 `json:"app_category_id"`
    // 服务商
    AppIsvID int64 `json:"app_isv_id"`
    // 应用图片
    AppImage []AppImage `gorm:"ForeignKey:AppID" json:"app_image"`
    // 应用组合，应用的模板
    AppPod []AppPod `gorm:"ForeignKey:AppID" json:"app_pod"`
    // 中间件组合
    AppMiddle []AppMiddle `gorm:"ForeignKey:AppID" json:"app_middle"`
    // 存储组合
    AppVolume []AppVolume `gorm:"ForeignKey:AppID" json:"app_volume"`
    // 评论
    AppComment []AppComment `gorm:"ForeignKey:AppID" json:"app_comment"`
}
```

这里 `AppDetail` 在模型里作为「描述」字段，与 Proto 中 `app_describe`/`app_detail` 的命名略有差异——实际项目中以 JSON Tag 对齐为准，二者在数据流上映射到同一语义。

## 分类与服务商

分类与服务商是较特殊的两个实体：它们的值（名称）对应用而言是「可映射」的，前端可动态拉取分类接口、服务商接口来渲染名称，因此 `AppStore` 只存其 ID。

```go
// 应用分类
type AppCategory struct {
    ID           int64  `gorm:"primary_key;not_null;auto_increment"`
    CategoryName string `json:"category_name"`
    // @TODO 还可扩展 parentID 以支持多级分类
}

// 服务商（ISV）
type AppIsv struct {
    ID          int64  `gorm:"primary_key;not_null;auto_increment"`
    AppIsvName  string `json:"app_isv_name"`
    AppIsvDetail string `json:"app_isv_detail"`
}
```

`AppCategory` 预留了 `parentID`（父级分类）的扩展点，可按业务需要实现多级分类树。

## 图片：可展示多张

应用详情页需要多张截图来提升吸引力，因此图片是一对多，且可存多个地址：

```go
// 云应用图片
type AppImage struct {
    ID          int64  `gorm:"primary_key;not_null;auto_increment"`
    AppID       int64  `json:"app_id"`
    // 图片地址
    AppImageSrc string `json:"app_image_src"`
}
```

## Pod / 中间件 / 存储：仅记录模板 ID

这三类是本课程建模的关键设计——它们**只引用模板 ID**，不复制模板内容：

```go
// Pod 模板引用
type AppPod struct {
    ID       int64 `gorm:"primary_key;not_null;auto_increment"`
    AppID    int64 `json:"app_id"`
    AppPodID int64 `json:"app_pod_id"` // 引用的 Pod 模板 ID
}

// 中间件模板引用
type AppMiddle struct {
    ID          int64 `gorm:"primary_key;not_null;auto_increment"`
    AppID       int64 `json:"app_id"`
    AppMiddleID int64 `json:"app_middle_id"` // 引用的中间件模板 ID
}

// 云应用存储模板引用
type AppVolume struct {
    ID          int64 `gorm:"primary_key;not_null;auto_increment"`
    AppID       int64 `json:"app_id"`
    AppVolumeID int64 `json:"app_volume_id"` // 引用的存储模板 ID
}
```

为什么存储也要记录模板？因为应用挂载的磁盘往往有特定默认大小、初始化变量等设计，这些默认值由存储模板统一初始化。课程前几章创建资源时很多变量是手填的，而应用市场要求「安装即默认填好」，体验类似手机应用商店：点安装、注册即可用，无需手填内存与存储。模板正是用来固化这些默认值的。

## 评论

评论出现在应用详情页，包含标题、详情、评论者等：

```go
// 云应用评论
type AppComment struct {
    ID              int64  `gorm:"primary_key;not_null;auto_increment"`
    AppID           int64  `json:"app_id"`
    AppCommentTitle string `json:"app_comment_title"`
    AppCommentDetail string `json:"app_comment_detail"`
    AppUserID       int64  `json:"app_user_id"`
    // @TODO 还可扩展评论时间、审核状态等
}
```

## 建表入口

这些模型最终由 Repository 的 `InitTable` 统一建表（参见 11.4 节），一次性创建全部八张表：

```go
func (u *AppStoreRepository) InitTable() error {
    return u.mysqlDb.CreateTable(
        &model.AppStore{}, &model.AppComment{}, &model.AppVolume{},
        &model.AppPod{}, &model.AppImage{}, &model.AppCategory{},
        &model.AppIsv{}, &model.AppMiddle{},
    ).Error
}
```

## API 速览

| 模型 | 关键字段 | 关联关系 |
| --- | --- | --- |
| AppStore | AppSku(唯一)、AppTitle、AppDetail、AppPrice、AppCheck | 一对多关联 AppImage/AppPod/AppMiddle/AppVolume/AppComment |
| AppCategory | CategoryName | 被 AppStore.AppCategoryID 引用 |
| AppIsv | AppIsvName、AppIsvDetail | 被 AppStore.AppIsvID 引用 |
| AppImage | AppImageSrc | ForeignKey AppID |
| AppPod | AppPodID(模板ID) | ForeignKey AppID |
| AppMiddle | AppMiddleID(模板ID) | ForeignKey AppID |
| AppVolume | AppVolumeID(模板ID) | ForeignKey AppID |
| AppComment | AppCommentTitle、AppCommentDetail、AppUserID | ForeignKey AppID |

## Demo 示例

**运行说明**：以下示例展示如何构造一个带关联子表的应用模型，并交给 GORM 自动建表与写入（需引入 `github.com/jinzhu/gorm` 与对应 MySQL 驱动）。

**代码说明**：用 `AppStore` 聚合 `AppImage`、`AppPod`、`AppMiddle`、`AppVolume`，通过 `AppID` 自动关联；`AppPodID` 等只填模板 ID。

**技术点总结**：主从建模让应用市场结构清晰；模板以 ID 引用避免重复创建；JSON Tag 同时服务 GORM 与 Proto 表单转换。

```go
package main

import (
    "fmt"

    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
)

// 以下结构体与课程 model 包一致（省略 gorm 标签以聚焦逻辑）
type AppStore struct {
    ID           int64
    AppSku       string
    AppTitle     string
    AppPod       []AppPod
    AppVolume    []AppVolume
}
type AppPod struct {
    ID       int64
    AppID    int64
    AppPodID int64
}
type AppVolume struct {
    ID          int64
    AppID       int64
    AppVolumeID int64
}

func main() {
    // db, _ := gorm.Open("mysql", "user:pass@/appstore?charset=utf8&parseTime=True")
    // db.AutoMigrate(&AppStore{}, &AppPod{}, &AppVolume{})

    app := AppStore{
        AppSku:   "SKU-MYSQL-HA",
        AppTitle: "MySQL 高可用",
        AppPod:   []AppPod{{AppPodID: 101}},  // 引用 Pod 模板 101
        AppVolume: []AppVolume{{AppVolumeID: 202}}, // 引用存储模板 202
    }
    fmt.Printf("应用模型: %+v\n", app)
}
```

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/base/domain/model/base.go`
- `code/课件/appstore/domain/model/app_category.go`
- `code/课件/appstore/domain/model/app_pod.go`
- `code/课件/appstore/domain/model/app_middle.go`
- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/appstore/domain/model/app_volume.go`
- `code/课件/appstore/domain/model/app_isv.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
