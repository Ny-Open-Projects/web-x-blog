# Go PaaS 平台开发: 中间件微服务 Proto 接口定义

## 纲要

- 使用 Protobuf（proto3）定义中间件微服务的对外 RPC 接口
- `service Middleware` 同时暴露「中间件实例」与「类型/版本」两组独立接口
- 消息体 `MiddlewareInfo` 与 `Middleware` 模型字段一一对应
- 通过 `protoc-gen-micro` 生成 `.pb.go` 与 `.pb.micro.go`

## 为什么先写 Proto

在开发 service 层之前，先把对外接口（Proto）梳理清楚。本章的中间件服务基于 go-micro 框架，对外以 gRPC/RPC 形式提供能力。Proto 是前后端、服务间契约的「单一真相源」，service 层实现这些 RPC 方法即可。

中间件服务对外实际包含两类生命周期：

1. **中间件实例**的增删改查（用户真正创建出来的那个 MySQL 等）；
2. **类型与版本**的增删改查（目录数据，见 10.6），作为后台能力对外暴露。

因此 `service Middleware` 中前五个是基础实例接口，后五个是类型/版本接口。

## Proto 完整定义

```protobuf
syntax = "proto3";

package middleware;

option go_package = "./proto/middleware;middleware";

service Middleware {
	// 对外提供添加服务
	rpc AddMiddleware(MiddlewareInfo) returns (Response) {}
	rpc DeleteMiddleware(MiddlewareId) returns (Response) {}
	rpc UpdateMiddleware(MiddlewareInfo) returns (Response) {}
	rpc FindMiddlewareByID(MiddlewareId) returns (MiddlewareInfo) {}
	rpc FindAllMiddleware(FindAll) returns (AllMiddleware) {}
	// 根据中间件的类型查找所有中间件
	rpc FindAllMiddlewareByTypeID(FindAllByTypeId) returns (AllMiddleware){}
	// 获取中间件类型
	rpc FindMiddleTypeByID(MiddleTypeId) returns (MiddleTypeInfo){}
	rpc AddMiddleType(MiddleTypeInfo) returns (Response){}
	rpc DeleteMiddleTypeByID(MiddleTypeId) returns (Response){}
	rpc UpdateMiddleType(MiddleTypeInfo) returns(Response){}
	rpc FindAllMiddleType(FindAll) returns (AllMiddleType){}
}

message MiddlewareInfo {
	int64 id = 1;
	string middle_name = 2;
	string middle_namespace =3;
	int64 middle_type_id = 4;
	int64 middle_version_id =5;
	repeated MiddlePort middle_port=6;
	MiddleConfig middle_config=7;
	repeated MiddleEnv middle_env=8;
	float middle_cpu=9;
	float middle_memory=10;
	repeated MiddleStorage middle_storage =11;
	int32 middle_replicas = 12;
	// 添加需要的镜像版本
	string middle_docker_image_version=13;
}

message MiddlePort {
	int64 middle_id=1;
	int32 middle_port=2;
	string middle_protocol=3;
}

message MiddleConfig{
	int64 middle_id =1;
	string middle_config_root_user =2;
	string middle_config_root_pwd =3;
	string middle_config_user =4;
	string middle_config_pwd =5;
	string middle_config_data_base =6;
}

message MiddleEnv {
	int64 middle_id=1;
	string env_key=2;
	string env_value=3;
}

message MiddleStorage{
	int64 middle_id =1;
	string middle_storage_name=2;
	float middle_storage_size=3;
	string middle_storage_path=4;
	string middle_storage_class=5;
	string middle_storage_access_mode=6;
}

message FindAllByTypeId {
    int64 type_id =1;
}

message MiddleTypeId {
	int64 id=1;
}

message MiddlewareId {
	int64 id = 1;
}

message FindAll {

}

message Response {
	string msg =1 ;
}

message AllMiddleware {
	repeated MiddlewareInfo middleware_info = 1;
}

message MiddleTypeInfo {
	int64 id =1;
	string middle_type_name=2;
	string middle_type_image_src=3;
	repeated MiddleVersion middle_version=4;
}

message MiddleVersion{
	int64 middle_type_id =1;
	string middle_docker_image=2;
	string middle_vs=3;
}

message AllMiddleType{
	repeated MiddleTypeInfo middle_type_info =1;
}
```

## 关键设计点

- **`MiddlewareInfo` 与模型一一对应**：除模型已有字段外，多出一个 `middle_docker_image_version`（field 13），即 `镜像地址:版本号` 拼好的完整镜像引用（由 10.6 的 `FindImageVersionByID` 生成），供 Kubernetes 拉取镜像直接使用。
- **`repeated` 表示列表**：端口、环境变量、存储都是 `repeated`，对应 Go 里的切片。
- **请求/响应分离**：单条查询用 `MiddlewareId` / `MiddleTypeId` 这样的轻量请求消息；批量用 `AllMiddleware` / `AllMiddleType` 包裹 `repeated` 列表；统一返回 `Response{ msg }` 表达操作结果。
- **类型与版本内嵌**：`MiddleTypeInfo` 内嵌 `repeated MiddleVersion`，与前文 `Preload("MiddleVersion")` 的查询逻辑呼应。

## 代码生成

使用 `protoc-gen-micro`（go-micro 的代码生成插件）生成 Go 代码。它会产出两个文件：

- `middleware.pb.go`：纯 Protobuf 消息的 Go 结构与方法；
- `middleware.pb.micro.go`：go-micro 的 service/handler 脚手架。

不同操作系统只需把生成命令中的输出目录换成对应路径即可。生成后即可在 service 层引用 `middleware.MiddlewareInfo`、`middleware.MiddlewareService` 等类型。

## API 速览

| RPC | 请求 | 响应 | 说明 |
| --- | --- | --- | --- |
| `AddMiddleware` | `MiddlewareInfo` | `Response` | 创建实例 |
| `DeleteMiddleware` | `MiddlewareId` | `Response` | 删除实例 |
| `UpdateMiddleware` | `MiddlewareInfo` | `Response` | 更新实例 |
| `FindMiddlewareByID` | `MiddlewareId` | `MiddlewareInfo` | 按 ID 查 |
| `FindAllMiddleware` | `FindAll` | `AllMiddleware` | 全量查 |
| `FindAllMiddlewareByTypeID` | `FindAllByTypeId` | `AllMiddleware` | 按类型查 |
| `FindMiddleTypeByID` | `MiddleTypeId` | `MiddleTypeInfo` | 查类型（含版本） |
| `AddMiddleType` | `MiddleTypeInfo` | `Response` | 新增类型 |
| `DeleteMiddleTypeByID` | `MiddleTypeId` | `Response` | 删除类型 |
| `UpdateMiddleType` | `MiddleTypeInfo` | `Response` | 更新类型 |
| `FindAllMiddleType` | `FindAll` | `AllMiddleType` | 全量类型 |

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

相关度：100%。是否需要继续：否。代码是否可运行：是。
