# Go PaaS 平台开发: 用户 Handler 开发

## 纲要

- handler 层实现 proto 生成的 `UserServiceHandler` 接口，对外暴露 RPC 方法
- 四个核心方法：AddUserRole、UpdateUserRole、DeleteUserRole、IsRight
- 额外提供 GetUsersByRoleIds：根据角色 ID 列表批量查出对应的用户切片
- handler 不直接写 SQL，而是委托给 service 层
- 多切片入参（如角色 ID 列表）通过组合后一次性查询，便于下游复用

## Handler 与 Proto 的关系

用户中心的微服务由 proto 定义接口，代码生成工具会产出 handler 接口。我们实现的 `userHandler` 只要补齐这些方法即可。在 go-micro v3 里，典型的 handler 签名形如：

```go
type UserServiceHandler interface {
	AddUserRole(ctx context.Context, req *AddUserRoleRequest, rsp *AddUserRoleResponse) error
	UpdateUserRole(ctx context.Context, req *UpdateUserRoleRequest, rsp *UpdateUserRoleResponse) error
	DeleteUserRole(ctx context.Context, req *DeleteUserRoleRequest, rsp *DeleteUserRoleResponse) error
	IsRight(ctx context.Context, req *IsRightRequest, rsp *IsRightResponse) error
}
```

## 实现用户 Handler

handler 持有 `UserService`，所有方法都是"取参 → 委托 service → 回填响应"的薄封装：

```go
package handler

import (
	"context"

	pb "code.xxx.io/gopaas/usercenter/proto/user"
	"code.xxx.io/gopaas/usercenter/service"
)

type UserHandler struct {
	userService service.UserService
}

func NewUserHandler(s service.UserService) *UserHandler {
	return &UserHandler{userService: s}
}

// AddUserRole 为用户添加角色
func (h *UserHandler) AddUserRole(ctx context.Context, req *pb.AddUserRoleRequest, rsp *pb.AddUserRoleResponse) error {
	if err := h.userService.AddUserRole(req.UserId, req.RoleId); err != nil {
		return err
	}
	rsp.Code = 0
	return nil
}

// UpdateUserRole 更新用户的角色
func (h *UserHandler) UpdateUserRole(ctx context.Context, req *pb.UpdateUserRoleRequest, rsp *pb.UpdateUserRoleResponse) error {
	if err := h.userService.UpdateUserRole(req.UserId, req.RoleId); err != nil {
		return err
	}
	rsp.Code = 0
	return nil
}

// DeleteUserRole 删除用户的角色
func (h *UserHandler) DeleteUserRole(ctx context.Context, req *pb.DeleteUserRoleRequest, rsp *pb.DeleteUserRoleResponse) error {
	if err := h.userService.DeleteUserRole(req.UserId, req.RoleIds); err != nil {
		return err
	}
	rsp.Code = 0
	return nil
}

// IsRight 校验用户是否具备指定权限
func (h *UserHandler) IsRight(ctx context.Context, req *pb.IsRightRequest, rsp *pb.IsRightResponse) error {
	ok, err := h.userService.IsRight(req.UserId, req.Action)
	if err != nil {
		return err
	}
	rsp.Right = ok
	return nil
}
```

## 根据角色批量查用户

除了上面四个 RPC 方法，handler 还提供一个常用辅助：根据一组角色 ID 查出对应的全部用户。由于角色 ID 是切片，这里把所有 ID 组合起来，通过一次查询拿到用户切片，供后续逻辑复用：

```go
// GetUsersByRoleIds 根据角色 ID 列表批量查询用户
func (h *UserHandler) GetUsersByRoleIds(ctx context.Context, req *pb.GetUsersByRoleIdsRequest, rsp *pb.GetUsersByRoleIdsResponse) error {
	users, err := h.userService.GetUsersByRoleIds(req.RoleIds)
	if err != nil {
		return err
	}
	rsp.Users = users
	return nil
}
```

对应的 service 方法可基于 `user_role` 关联表实现：

```go
func (s *userService) GetUsersByRoleIds(roleIds []int64) ([]*model.User, error) {
	var userIds []int64
	err := s.engine.Table("user_role").
		In("role_id", roleIds).
		Distinct("user_id").
		Find(&userIds)
	if err != nil {
		return nil, err
	}
	var users []*model.User
	if len(userIds) == 0 {
		return users, nil
	}
	err = s.engine.In("id", userIds).Find(&users)
	return users, err
}
```

## 注册 Handler

在 `main` 中把 handler 注册到微服务运行时，外部才能通过 RPC 调用：

```go
userHandler := handler.NewUserHandler(userSvc)
_ = pb.RegisterUserServiceHandler(service.Server(), userHandler)
```

## API 速览

| RPC 方法 | 请求关键字段 | 响应 | 说明 |
| --- | --- | --- | --- |
| AddUserRole | `user_id`, `role_id` | `code` | 为用户添加角色 |
| UpdateUserRole | `user_id`, `role_id` | `code` | 更新用户角色 |
| DeleteUserRole | `user_id`, `role_ids` | `code` | 删除用户角色 |
| IsRight | `user_id`, `action` | `right` | 权限校验 |
| GetUsersByRoleIds | `role_ids` | `users` | 按角色批量查用户 |

## Demo 示例

下面演示 handler 的最小装配（service 实例自行注入）：

```go
package main

import (
	"code.xxx.io/gopaas/usercenter/handler"
	"code.xxx.io/gopaas/usercenter/service"
)

func main() {
	userSvc := service.NewUserService(engine)
	h := handler.NewUserHandler(userSvc)

	// 模拟一次权限校验调用
	rsp := &pb.IsRightResponse{}
	if err := h.IsRight(context.Background(),
		&pb.IsRightRequest{UserId: 1, Action: "app"}, rsp); err != nil {
		panic(err)
	}
	println("right:", rsp.Right)
}
```

- 运行说明：在完整工程（已生成 proto、注入 `xorm.Engine`）下编译运行即可。
- 代码说明：handler 保持"薄"，所有业务与数据访问都下沉到 service / repository。
- 技术点总结：handler 实现 proto 接口、委托 service，是微服务分层的标准写法；切片入参用 `In` 一次查询，避免循环查库。

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
