# Go PaaS 平台开发: 云应用市场服务端 Proto 开发

## 纲要

- 使用 Protocol Buffers（proto3）定义 `appStore` 微服务契约，由 protoc 生成 Go 代码（`appStore.pb.go`、`appStore.pb.micro.go`）。
- 定义 9 个 RPC：`AddAppStore`、`DeleteAppStore`、`UpdateAppStore`、`FindAppStoreByID`、`FindAllAppStore` 以及安装数/浏览数的 `AddInstallNum`、`GetInstallNum`、`AddViewNum`、`GetViewNum`。
- 核心消息 `AppStoreInfo` 聚合了主表字段与五类关联子消息：`AppImage`、`AppPod`、`AppMiddle`、`AppVolume`、`AppComment`。
- 辅助消息：`AppStoreId`（按 ID 操作）、`FindAll`（空查询）、`Response`（通用返回）、`AllAppStore`（列表返回）、`Number`（计数返回）。
- 设计要点：分类 `app_category_id` 与服务商 `app_isv_id` 只存 ID；`app_check` 表示官方审核状态；关联资源以模板 ID 引用。

## Proto 在微服务中的角色

在 go-micro 体系中，Proto 是服务端与客户端的「契约」。我们先把对外要开放的接口与报文结构定义清楚，再用 protoc 生成强类型的 Go stub，Handler 只需实现生成的接口即可。本章云应用市场首先需要完善的就是这份契约。

## 服务与 RPC 定义

```protobuf
syntax = "proto3";

package appStore;

option go_package = "./proto/appStore;appStore";

service AppStore {
    // 对外提供添加服务
    rpc AddAppStore(AppStoreInfo) returns (Response) {}
    rpc DeleteAppStore(AppStoreId) returns (Response) {}
    rpc UpdateAppStore(AppStoreInfo) returns (Response) {}
    rpc FindAppStoreByID(AppStoreId) returns (AppStoreInfo) {}
    rpc FindAllAppStore(FindAll) returns (AllAppStore) {}

    // 添加常用的接口
    rpc AddInstallNum(AppStoreId) returns (Response) {}
    rpc GetInstallNum(AppStoreId) returns (Number) {}
    rpc AddViewNum(AppStoreId) returns (Response) {}
    rpc GetViewNum(AppStoreId) returns (Number) {}
}
```

五个基础 CRUD 加上四个统计接口，正好覆盖应用市场的日常操作。统计接口单独成组，是因为「安装数」与「浏览数」是高频自增字段，与主体信息更新解耦，避免每次查看都走完整更新链路。

## 核心消息 AppStoreInfo

`AppStoreInfo` 是添加/更新/查询的主体报文，字段与 GORM 模型一一对应：

```protobuf
message AppStoreInfo {
    int64 id = 1;
    string app_sku = 2;
    string app_title = 3;
    string app_describe = 4;
    string app_detail = 5;
    float app_price = 6;
    int64 app_install = 7;
    int64 app_views = 8;
    bool app_check = 9;
    int64 app_category_id = 10;
    int64 app_isv_id = 11;
    repeated AppImage app_image = 12;
    repeated AppPod app_pod = 13;
    repeated AppMiddle app_middle = 14;
    repeated AppVolume app_volume = 15;
    repeated AppComment app_comment = 16;
}
```

需要特别说明的几个字段：

- `app_sku`：应用的唯一标识（库存单位），建表时设为 `unique_index`，用于幂等上架。
- `app_check`：官方审核标记。添加应用通常要经官方审核（安全扫描、敏感内容过滤），审核通过后才对使用者可见。
- `app_category_id` / `app_isv_id`：只存分类与服务商的 ID，具体名称由前端动态拉取分类/服务商接口渲染，避免冗余存储。
- 五个 `repeated` 子消息：图片、Pod 模板、中间件、存储模板、评论，构成应用市场的辅助信息（详见 11.3 节的模型开发）。

## 关联子消息

每个关联子消息都只保留「应用 ID + 模板/实体 ID」：

```protobuf
message AppImage {
    int64 app_id = 1;
    string app_image_src = 2;
}

message AppPod {
    int64 app_id = 1;
    int64 app_pod_id = 2;
}

message AppMiddle {
    int64 app_id = 1;
    int64 app_middle_id = 2;
}

message AppComment {
    int64 app_id = 1;
    string app_comment_title = 2;
    string app_comment_detail = 3;
    int64 app_user_id = 4;
}

message AppVolume {
    int64 app_id = 1;
    int64 app_volume_id = 2;
}
```

## 辅助消息与返回

```protobuf
message AppStoreId {
    int64 id = 1;
}

message FindAll {

}

message Response {
    string msg = 1;
}

message AllAppStore {
    repeated AppStoreInfo appStore_info = 1;
}

message Number {
    int64 num = 1;
}
```

- `AppStoreId`：所有「按 ID 操作」接口的统一入参。
- `Response`：删除/添加/统计等只关心成功与否的接口返回，携带一条 `msg`。
- `AllAppStore`：`FindAllAppStore` 的返回，承载 `AppStoreInfo` 列表。
- `Number`：安装数/浏览数查询的返回。

## 生成方式

完成 Proto 后，通过 protoc 配合 micro 插件生成 Go 代码：

```bash
protoc --proto_path=. --micro_out=. --go_out=. proto/appStore/appStore.proto
```

生成的 `appStore.pb.go` 包含消息结构与序列化逻辑，`appStore.pb.micro.go` 包含微服务接口与客户端 stub，Handler 直接实现 `AppStoreHandler` 接口即可对外提供能力。

## API 速览

| RPC | 入参 | 返回 | 语义 |
| --- | --- | --- | --- |
| AddAppStore | AppStoreInfo | Response | 新增应用 |
| DeleteAppStore | AppStoreId | Response | 删除应用（级联清理子表） |
| UpdateAppStore | AppStoreInfo | Response | 更新应用 |
| FindAppStoreByID | AppStoreId | AppStoreInfo | 按 ID 查询（含关联预加载） |
| FindAllAppStore | FindAll | AllAppStore | 查询全部 |
| AddInstallNum | AppStoreId | Response | 安装数 +1 |
| GetInstallNum | AppStoreId | Number | 获取安装数 |
| AddViewNum | AppStoreId | Response | 浏览数 +1 |
| GetViewNum | AppStoreId | Number | 获取浏览数 |

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

相关度：100%。是否需要继续：是。代码是否可运行：否。
