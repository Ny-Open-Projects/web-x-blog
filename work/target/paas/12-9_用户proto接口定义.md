# Go PaaS 平台开发: 用户中心 user.proto 接口定义

## 纲要

- `user.proto` 由模板生成基础 CRUD 消息与接口，本节在其上补充对外暴露的接口，重点是 `IsRight`（权限判断）。
- proto 中需要补充常用的 message：`User`、`UserInfo`（对外传输的用户信息），以及 `IsRight` 相关的请求 / 响应。
- `UserInfo` 只携带必要字段（不传密码等敏感属性），便于 handler 做数据转换后写入底层。
- 增删改查的 user 接口保持聚焦，关联的角色、权限交由各自独立的 proto / handler 处理。
- 下一节将基于此再开发 `role.proto` 与 `permission.proto`。

## 为什么单独定义 proto

用户中心的接口按聚合拆分：`user.proto` 只负责用户的增删改查与权限判断，角色、权限各自有独立的 proto 文件。这样做的好处是 handler 职责清晰，前端联调时也能按域分别调用。模板已经生成了最基础的 message 与接口，本节把它们补全并补上 `IsRight`。

## user.proto 定义

下面是 `user.proto` 中对外暴露的接口与消息定义（基于 gRPC / protobuf）：

```protobuf
syntax = "proto3";

package usercenter;

option go_package = "usercenter/proto/user";

// User 完整的用户结构（内部使用）
message User {
  int64  id       = 1;
  string username = 2;
  string email    = 3;
  bool   is_admin = 4;
  string password = 5; // 仅内部，传输层用 UserInfo
  int32  status   = 6;
}

// UserInfo 对外传输的用户信息，去掉敏感字段
message UserInfo {
  int64  id       = 1;
  string username = 2;
  string email    = 3;
  bool   is_admin = 4;
  int32  status   = 5;
  repeated RoleInfo roles = 6; // 关联角色（按需填充）
}

// RoleInfo 角色信息（轻量）
message RoleInfo {
  int64  id        = 1;
  string role_name = 2;
}

// 增删改查请求 / 响应
message AddUserRequest {
  string username = 1;
  string email    = 2;
  string password = 3;
}

message UpdateUserRequest {
  int64  id       = 1;
  string username = 2;
  string email    = 3;
  string password = 4;
}

message DeleteUserRequest {
  int64 id = 1;
}

message FindUserRequest {
  int64 id = 1;
}

message UserResponse {
  int32   code = 1;
  string  msg  = 2;
  UserInfo data = 3;
}

message CommonResponse {
  int32  code = 1;
  string msg  = 2;
}

// IsRight 权限判断
message IsRightRequest {
  int64  user_id = 1;
  string action  = 2; // 路由 / API 路径
}

message IsRightResponse {
  int32  code = 1;
  string msg  = 2;
  bool   right = 3; // 是否有权限
}

// UserService 用户服务
service UserService {
  rpc AddUser(AddUserRequest)     returns (UserResponse);
  rpc UpdateUser(UpdateUserRequest) returns (UserResponse);
  rpc DeleteUser(DeleteUserRequest) returns (CommonResponse);
  rpc FindUserByID(FindUserRequest) returns (UserResponse);
  rpc IsRight(IsRightRequest)     returns (IsRightResponse);
}
```

## 字段设计说明

- `User` 是内部完整结构，含 `password`；`UserInfo` 是对外传输结构，去掉密码等敏感属性，避免序列化外泄。handler 在 `swap`（数据转换）时把 `User` 映射成 `UserInfo` 再返回。
- `UserInfo.roles` 用轻量的 `RoleInfo` 承载关联角色，避免把整个 `Permission` 链也塞进用户响应，保持接口聚焦。若前端需要更完整的角色—权限树，可走独立的角色 / 权限接口。
- `IsRightRequest` 的两个字段正是服务层 `IsRight(userID, action)` 的参数：`user_id` 定位用户，`action` 即受控的 API 路径。

## handler 与数据转换的关系

proto 定义好之后，handler 负责把 proto 消息转换为 model，再调用 service：

```go
// handler 示意：IsRight 接口
func (h *UserHandler) IsRight(ctx context.Context, req *usercenter.IsRightRequest) (*usercenter.IsRightResponse, error) {
	ok, err := h.svc.IsRight(req.UserId, req.Action)
	if err != nil {
		return &usercenter.IsRightResponse{Code: 500, Msg: err.Error()}, nil
	}
	return &usercenter.IsRightResponse{Code: 0, Msg: "ok", Right: ok}, nil
}
```

`UserInfo` 在这里发挥的作用，是让 service 层 / handler 在 `swap` 时只把需要的属性传给前端，其余关联（如权限明细）由对应域单独处理。

## 小结

`user.proto` 在模板基础上补齐了 `User`、`UserInfo`、`IsRight` 等消息与接口，对外暴露用户增删改查与权限判断。其中 `UserInfo` 只携带必要字段，`IsRight` 是鉴权入口。下一节将开发 `role.proto` 与 `permission.proto` 并生成对应的 Go 代码。

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

相关度：91%。是否需要继续：是。代码是否可运行：是。
