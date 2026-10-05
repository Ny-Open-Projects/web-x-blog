# Go PaaS 平台开发: Proto 对外服务接口定义与代码生成

## 纲要

- 定义 `pod.proto`：package、service、message，描述对外暴露的 Pod 操作
- 五个 RPC：AddPod / DeletePodById / UpdatePod / FindPodById / Call（默认接口）
- 用 `docker run` 调用 protoc 镜像一键生成 `*.pb.go` 与 `*.micro.go`
- 各模块（svc / route / volume / pod / appStore）均遵循同一套 proto 结构

## 为什么先写 Proto

Service 层依赖 proto 中定义的类型与方法签名，因此在写 service 之前要先完成 proto 文件并生成 Go 代码。本平台采用 gRPC + go-micro，所有对外服务都通过 proto 描述契约。

## 定义 Pod 的 Proto 文件

`pod/domain/proto/pod/pod.proto` 定义了对外服务契约：

```proto
syntax = "proto3";

package pod;

option go_package = "./proto/pod;pod";

service Pod {
    rpc AddPod (PodInfo) returns (Response) {}
    rpc DeletePodById (PodId) returns (Response) {}
    rpc UpdatePod (PodInfo) returns (Response) {}
    rpc FindPodById (PodId) returns (PodInfo) {}
    // 默认接口
    rpc Call (Request) returns (Response) {}
}

message PodInfo {
    int64 id = 1;
    string pod_name = 2;
    string pod_namespace = 3;
    // CPU / 内存的最大值（最小值按固定比例推导）
    float pod_cpu_max = 4;
    float pod_memory_max = 5;
    // 端口列表
    repeated int32 pod_port = 6;
    // 环境变量，key -> value
    map<string, string> pod_env = 7;
    // 镜像拉取策略
    string pod_pull_policy = 8;
    // 重启策略
    string pod_restart = 9;
    // 发布策略
    string pod_type = 10;
    // 镜像名 + tag
    string pod_image = 11;
}

message PodId {
    int64 id = 1;
}

message Response {
    int64 id = 1;
    string msg = 2;
    int32 code = 3;
}
```

> 说明：字段编号与真实课件略有简化（`podApi.proto` 中 `Request/Response` 用于通用 Call 接口，本示例聚焦业务方法）。CPU/内存只存最大值，最小值可固定比例推导，端口以 `repeated` 传递。

## 通用 API 网关 Proto

对外 API 层（`podApi`）使用统一的 HTTP 风格消息，便于网关透传：

```proto
syntax = "proto3";

package podApi;

option go_package = "./proto/podApi;podApi";

service PodApi {
    rpc FindPodById (Request) returns (Response) {}
    rpc AddPod (Request) returns (Response) {}
    rpc DeletePodById (Request) returns (Response) {}
    rpc UpdatePod (Request) returns (Response) {}
    rpc Call (Request) returns (Response) {}
}

message Pair {
    string key = 1;
    repeated string values = 2;
}

message Request {
    string method = 1;
    string path = 2;
    map<string, Pair> header = 3;
    map<string, Pair> get = 4;
    map<string, Pair> post = 5;
    string body = 6;
    string url = 7;
}

message Response {
    int32 statusCode = 1;
    map<string, Pair> header = 2;
    string body = 3;
}
```

## 代码生成

写好 proto 后，借助课程提供的 protoc 镜像一键生成 Go 代码。镜像 `coding-535/podapi` 封装了 protoc 与 go-micro 插件：

```bash
# 本机执行需输入本机密码（macOS 授权 docker）
# --rm 用完即删；-v 挂载工作目录
docker run --rm \
  -v /your/absolute/workdir:/workdir \
  coding-535/podapi:latest \
  pod/proto/pod.proto
```

执行后会在 proto 目录下生成 `pod.pb.go`（消息序列化）与 `pod.micro.go`（gRPC 服务骨架），直接引用即可。

> 若在某系统上执行失败，优先排查：①路径是否写对（Windows 用正斜杠绝对路径）；②proto 文件本身是否有语法错误。可直接从课程代码仓库拉取后，复用 `Makefile` 中已写好的命令，仅替换本地绝对路径。

## API 速览

| RPC | 入参 | 出参 | 说明 |
| --- | --- | --- | --- |
| `AddPod` | `PodInfo` | `Response` | 创建 Pod |
| `DeletePodById` | `PodId` | `Response` | 删除 Pod |
| `UpdatePod` | `PodInfo` | `Response` | 更新 Pod |
| `FindPodById` | `PodId` | `PodInfo` | 查询 Pod |
| `Call` | `Request` | `Response` | 网关通用透传 |

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/svcapi/proto/svcApi/svcApi.proto`
- `code/课件/routeapi/proto/routeApi/routeApi.proto`
- `code/课件/volumeapi/proto/volumeApi/volumeApi.proto`
- `code/课件/podapi/proto/podApi/podApi.proto`
- `code/课件/volume/proto/volume/volume.proto`
- `code/课件/route/proto/route/route.proto`
- `code/课件/svc/proto/svc/svc.proto`
- `code/课件/appstoreapi/proto/appStoreApi/appStoreApi.proto`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
