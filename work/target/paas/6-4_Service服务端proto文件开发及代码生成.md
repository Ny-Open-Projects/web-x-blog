# Go PaaS 平台开发: Service 服务端 proto 文件开发及代码生成

## 纲要

- 上一节开发了 model，这一节**根据 model 把 proto 的参数完善**——开发 Service 时 proto 参数会被直接使用到。
- proto 中定義两类消息：**`ServiceInfo`**（服务主信息）与 **`SvcPort`**（端口信息），后者以 `repeated` 形式挂在前者下。
- `SvcPort` 包含：ID、ServiceID、`service_port`、`service_target_port`、`service_node_port`、端口协议。
- 查询口径：更新时可带上 Pod 信息；若不传扩展 ID，则通过 **`SvcId` 查找**。
- 执行 `make proto` 后会生成**两个文件**：`*.pb.go` 与 `*.micro.pb.go`。

## 一、proto 文件定义

```proto
syntax = "proto3";

package go.micro.service.service;

// Service 服务管理服务
service Service {
    // 新增服务
    rpc AddService(ServiceInfo) returns (Response) {}
    // 删除服务
    rpc DeleteService(ServiceId) returns (Response) {}
    // 更新服务
    rpc UpdateService(ServiceInfo) returns (Response) {}
    // 根据 ID 查询服务
    rpc FindServiceByID(ServiceId) returns (ServiceInfo) {}
    // 查询全部服务
    rpc FindAllService(FindAll) returns (ServiceAll) {}
}

// ServiceInfo 服务主信息（对应 model.Service）
message ServiceInfo {
    int64  id                    = 1;  // 主键，更新时可带上
    string service_name          = 2;  // 服务名称，唯一
    string service_namespace     = 3;  // 命名空间
    string service_pod_name      = 4;  // 绑定的 Pod 名称
    string service_type          = 5;  // ClusterIP/NodePort/LoadBalancer/ExternalName
    string service_external_name = 6;  // 仅 ExternalName 类型需要
    string service_team_id       = 7;  // 团队隔离
    repeated SvcPort svc_port    = 8;  // 端口集合
}

// SvcPort 服务端口（对应 model.SvcPort）
message SvcPort {
    int64  id                   = 1;  // 主键
    int64  service_id           = 2;  // 所属 Service
    int32  service_port         = 3;  // Service 暴露端口
    int32  service_target_port  = 4;  // 容器目标端口
    int32  service_node_port    = 5;  // 节点端口（NodePort 模式）
    string service_port_protocol = 6; // 端口协议，必填
}

message ServiceId {
    int64 service_id = 1;
}

message FindAll {}

message ServiceAll {
    repeated ServiceInfo service_info = 1;
}

message Response {
    string msg = 1;
}
```

> 说明：`ServiceInfo` 的字段与 model 一一对应；端口用 `repeated SvcPort` 表达"一个服务可配多个端口"。

## 二、生成代码

执行 Makefile 中的 proto 生成命令：

```bash
make proto
```

生成后会得到**两个文件**：

| 文件 | 说明 |
|------|------|
| `*.pb.go` | protobuf 消息与序列化代码 |
| `*.micro.pb.go` | go-micro 的服务/客户端桩代码 |

若本机 `make proto` 跑不通，可把 Makefile 里的 protoc 命令**直接复制到终端执行**：

```bash
# go-micro v3 生成命令（路径按本机实际情况调整）
protoc --proto_path=. --micro_out=. --go_out=:. proto/service.proto
```

> **注意**：命令里的地址（模块路径 / 输出路径）**必须改成本机能识别的地址**，否则生成的文件 import 路径会不对。

## 三、查找口径约定

- **更新**时可以把 Pod 信息一并带上；
- 若**不传扩展 ID（数据扩展 ID）**，则通过 **`SvcId`** 进行查找。

## 小结

- proto 是"对外契约"，字段要与 model 对齐，避免两边不一致。
- 生成物是 `*.pb.go` + `*.micro.pb.go` 两个文件，缺一不可。
- 生成命令的路径必须适配本机。
- 下一节开发 Service 服务端（`service` 层）逻辑。
