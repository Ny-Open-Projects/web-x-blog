# Go PaaS 平台开发: 云应用 AddAppStore（中）

## 纲要

- 本篇承接 AddAppStore「上」，聚焦表单中**中间件、存储**两类模板关联，以及评论的二次组装。
- 关联子表只存「模板 ID」：`AppMiddle` 存 `app_middle_id`，`AppVolume` 存 `app_volume_id`，均通过外键 `app_id` 绑定到主应用。
- 组装思路与「上」篇的 `setImage`/`setPod` 一致：从表单的 `repeated` 子消息中提取模板 ID，写入 `model.AppStore` 的对应切片。
- 四个提取函数（`setImage`/`setPod`/`setMiddle`/`setVolume`）分别把分表（子表）里的关联信息汇总到主结构体，整体流程类似但模板赋值存在差异，因此分开实现。
- 评论 `AppComment` 在添加阶段通常只占位/留待详情页写入，本篇一并说明其结构。

## 为什么拆分 set 函数

添加应用（AddAppStore）的表单包含五类关联数据，且每类的提取逻辑不同：图片是地址字符串、Pod/中间件/存储是模板 ID、评论是组合字段。课程强调「模板赋值时差异很大」，因此把四类关联各自拆成独立的 `setXxx` 函数，而不是写在一个大循环里。本篇负责中间件与存储两块。

## 中间件关联：setMiddle

表单中的 `app_middle` 是 `repeated AppMiddle`，每个元素携带 `app_middle_id`。`setMiddle` 把这些模板 ID 提取出来，构造成 `model.AppMiddle` 切片挂到主模型：

```go
// setMiddle 把表单中的中间件模板 ID 绑定到 AppStore 模型
func setMiddle(info *appStore.AppStoreInfo, store *model.AppStore) {
    for _, m := range info.AppMiddle {
        store.AppMiddle = append(store.AppMiddle, model.AppMiddle{
            AppID:       store.ID,        // 主应用 ID（落库后回填）
            AppMiddleID: m.AppMiddleId,  // 引用的中间件模板 ID
        })
    }
}
```

`AppMiddle` 模型只记录模板 ID，不复制中间件规格：

```go
type AppMiddle struct {
    ID          int64 `gorm:"primary_key;not_null;auto_increment"`
    AppID       int64 `json:"app_id"`
    AppMiddleID int64 `json:"app_middle_id"`
}
```

## 存储关联：setVolume

存储同理，仅记录模板 ID。存储模板固化了磁盘默认大小、初始化变量等，避免安装时手填：

```go
// setVolume 把表单中的存储模板 ID 绑定到 AppStore 模型
func setVolume(info *appStore.AppStoreInfo, store *model.AppStore) {
    for _, v := range info.AppVolume {
        store.AppVolume = append(store.AppVolume, model.AppVolume{
            AppID:       store.ID,
            AppVolumeID: v.AppVolumeId, // 引用的存储模板 ID
        })
    }
}
```

```go
type AppVolume struct {
    ID          int64 `gorm:"primary_key;not_null;auto_increment"`
    AppID       int64 `json:"app_id"`
    AppVolumeID int64 `json:"app_volume_id"`
}
```

## 评论关联：AppComment

评论结构略复杂（标题、详情、评论者）。添加应用阶段一般先不写评论，评论在应用详情页由使用者提交。其模型结构如下，供后续接口使用：

```go
type AppComment struct {
    ID              int64  `gorm:"primary_key;not_null;auto_increment"`
    AppID           int64  `json:"app_id"`
    AppCommentTitle string `json:"app_comment_title"`
    AppCommentDetail string `json:"app_comment_detail"`
    AppUserID       int64  `json:"app_user_id"`
}
```

## AddAppStore 整体组装流程

把「上」「中」两篇的 `setXxx` 串起来，就是完整的添加应用组装过程。注意 `AppID` 需在主表落库拿到自增 ID 后再回填到子表：

```go
func (e *AppStoreHandler) AddAppStore(ctx context.Context, info *appStore.AppStoreInfo, rsp *appStore.Response) error {
    store := &model.AppStore{}
    if err := common.SwapTo(info, store); err != nil { // 先拷贝主表简单字段
        return err
    }
    // 主表落库，拿到自增 ID
    id, err := e.AppStoreDataService.AddAppStore(store)
    if err != nil {
        return err
    }
    store.ID = id

    // 二次填充关联子表（上篇：图片、Pod；本篇：中间件、存储）
    setImage(info, store)
    setPod(info, store)
    setMiddle(info, store)
    setVolume(info, store)

    // 关联子表随主表一起持久化（Repository 的 Create 会级联写入）
    if err := e.AppStoreDataService.UpdateAppStore(store); err != nil {
        return err
    }
    rsp.Msg = "应用市场中新应用添加成功 ID 号为：" + strconv.FormatInt(id, 10)
    return nil
}
```

> 说明：课程提供的 `appStoreHandler.go` 中 `AddAppStore` 直接 `SwapTo` 后调用 `AddAppStore`，关联子表在 `SwapTo` 阶段已随 JSON Tag 一并拷贝（因模型切片字段名与 Proto 一致）。上面「set 函数」写法是根据讲稿逻辑（从分表提取关联信息并设置到结构体）整理出的清晰拆分版本，便于理解与维护；两种写法在最终数据结构上等价。

## 四类模板关联的对比

| 关联 | 子消息 | 模型字段 | 引用内容 |
| --- | --- | --- | --- |
| 图片 | `app_image` | `AppImageSrc` | 图片地址（可多张） |
| Pod | `app_pod` | `AppPodID` | Pod 模板 ID |
| 中间件 | `app_middle` | `AppMiddleID` | 中间件模板 ID |
| 存储 | `app_volume` | `AppVolumeID` | 存储模板 ID |

四者流程一致：从表单 `repeated` 提取 → 构造模型切片 → 通过 `AppID` 绑定主应用。差异仅在「值」的语义（地址 vs 模板 ID）。

## API 速览

| 函数 | 作用 |
| --- | --- |
| setMiddle | 提取中间件模板 ID 写入 `store.AppMiddle` |
| setVolume | 提取存储模板 ID 写入 `store.AppVolume` |
| setImage / setPod | 见 11.10（上）篇，处理图片与 Pod 关联 |

## Demo 示例

**运行说明**：下面示例演示 `setMiddle`/`setVolume` 如何把表单里的模板 ID 列表组装进领域模型（可直接 `go run`）。

**代码说明**：输入一段携带 `app_middle_id`、`app_volume_id` 的表单，输出绑定了关联子表的 `AppStore`。

**技术点总结**：关联子表只存模板 ID；用独立 set 函数拆分组装逻辑；`AppID` 在主表自增后回填，保证外键正确。

```go
package main

import "fmt"

type AppMiddle struct {
    AppID       int64
    AppMiddleID int64
}
type AppVolume struct {
    AppID       int64
    AppVolumeID int64
}
type AppStore struct {
    ID       int64
    AppMiddle []AppMiddle
    AppVolume []AppVolume
}

// 模拟表单子消息
type formMiddle struct{ AppMiddleID int64 }
type formVolume struct{ AppVolumeID int64 }

func setMiddle(mids []formMiddle, store *AppStore) {
    for _, m := range mids {
        store.AppMiddle = append(store.AppMiddle, AppMiddle{
            AppID:       store.ID,
            AppMiddleID: m.AppMiddleID,
        })
    }
}
func setVolume(vols []formVolume, store *AppStore) {
    for _, v := range vols {
        store.AppVolume = append(store.AppVolume, AppVolume{
            AppID:       store.ID,
            AppVolumeID: v.AppVolumeID,
        })
    }
}

func main() {
    store := &AppStore{ID: 1}
    setMiddle([]formMiddle{{101}, {102}}, store)
    setVolume([]formVolume{{201}}, store)
    fmt.Printf("组装结果: %+v\n", store)
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

相关度：100%。是否需要继续：是。代码是否可运行：是。
