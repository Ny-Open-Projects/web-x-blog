# Go PaaS 平台开发: 角色 Handler 开发

## 纲要

- 角色 handler 实现 proto 生成的 `RoleServiceHandler` 接口
- 三个核心方法：AddPermission、UpdatePermission、DeletePermission（为角色管理权限）
- 提供 GetRolePermissions 辅助：根据角色 ID 与权限 ID 查出已存在的关联实例
- handler 复用前面抽出的参数获取与转换套路，逻辑高度统一
- 同样在 `main` 中注册 handler 与对应的 service

## 角色 Handler 的职责

角色 handler 关注"角色与权限之间的关系"，即"为某个角色挂上哪些权限"。它不直接操作 `permission` 主表的数据本身，而是操作 `role_permission` 关联表。proto 生成的接口大致如下：

```go
type RoleServiceHandler interface {
	AddPermission(ctx context.Context, req *AddPermissionRequest, rsp *AddPermissionResponse) error
	UpdatePermission(ctx context.Context, req *UpdatePermissionRequest, rsp *UpdatePermissionResponse) error
	DeletePermission(ctx context.Context, req *DeletePermissionRequest, rsp *DeletePermissionResponse) error
}
```

## 辅助查询：GetRolePermissions

在写入关联前，通常要先确认角色、权限在数据库中确实存在——否则按 ID 插入关联时会因查不到对应记录而失败。因此先抽一个查询辅助：

```go
package handler

import (
	"context"

	pb "code.xxx.io/gopaas/usercenter/proto/role"
	"code.xxx.io/gopaas/usercenter/service"
)

type RoleHandler struct {
	roleService service.RoleService
}

// GetRolePermissions 根据 role_id / permission_id 查询已存在的关联实例
func (h *RoleHandler) GetRolePermissions(ctx context.Context, req *pb.GetRolePermissionsRequest, rsp *pb.GetRolePermissionsResponse) error {
	list, err := h.roleService.FindRolePermissions(req.RoleId, req.PermissionId)
	if err != nil {
		return err
	}
	rsp.Items = list
	return nil
}
```

对应的 service 实现（基于 `role_permission` 表）：

```go
func (s *roleService) FindRolePermissions(roleId, permissionId int64) ([]*model.RolePermission, error) {
	var list []*model.RolePermission
	session := s.engine.Where("role_id = ?", roleId)
	if permissionId > 0 {
		session = session.And("permission_id = ?", permissionId)
	}
	err := session.Find(&list)
	return list, err
}
```

## 为角色添加权限

`AddPermission` 先确认角色与权限存在，再调用 service 写入关联：

```go
// AddPermission 为指定角色添加权限
func (h *RoleHandler) AddPermission(ctx context.Context, req *pb.AddPermissionRequest, rsp *pb.AddPermissionResponse) error {
	// 先确认角色、权限真实存在
	if _, err := h.roleService.FindRolePermissions(req.RoleId, req.PermissionId); err != nil {
		return err
	}
	if err := h.roleService.AddPermission(req.RoleId, req.PermissionId); err != nil {
		return err
	}
	rsp.Code = 0
	return nil
}
```

## 更新与删除

更新、删除与添加结构一致，都基于 `role_id + permission_id`，直接委托 service 完成：

```go
// UpdatePermission 更新角色的权限
func (h *RoleHandler) UpdatePermission(ctx context.Context, req *pb.UpdatePermissionRequest, rsp *pb.UpdatePermissionResponse) error {
	if err := h.roleService.UpdatePermission(req.RoleId, req.PermissionId); err != nil {
		return err
	}
	rsp.Code = 0
	return nil
}

// DeletePermission 删除角色的权限
func (h *RoleHandler) DeletePermission(ctx context.Context, req *pb.DeletePermissionRequest, rsp *pb.DeletePermissionResponse) error {
	if err := h.roleService.DeletePermission(req.RoleId, req.PermissionId); err != nil {
		return err
	}
	rsp.Code = 0
	return nil
}
```

由于这几类接口设计方式一致、参数结构相同，所以借助前面抽出的参数获取与类型转换模板，可以很快把三个接口补齐。

## 注册 Handler

```go
roleHandler := handler.NewRoleHandler(roleSvc)
_ = pb.RegisterRoleServiceHandler(service.Server(), roleHandler)
```

## API 速览

| RPC 方法 | 请求关键字段 | 响应 | 说明 |
| --- | --- | --- | --- |
| GetRolePermissions | `role_id`, `permission_id` | `items` | 查询角色-权限关联 |
| AddPermission | `role_id`, `permission_id` | `code` | 为角色添加权限 |
| UpdatePermission | `role_id`, `permission_id` | `code` | 更新角色权限 |
| DeletePermission | `role_id`, `permission_id` | `code` | 删除角色权限 |

## Demo 示例

```go
package main

import (
	"context"

	pb "code.xxx.io/gopaas/usercenter/proto/role"
	"code.xxx.io/gopaas/usercenter/handler"
	"code.xxx.io/gopaas/usercenter/service"
)

func main() {
	roleSvc := service.NewRoleService(engine)
	h := handler.NewRoleHandler(roleSvc)

	rsp := &pb.AddPermissionResponse{}
	// 为角色 1 添加权限 2
	if err := h.AddPermission(context.Background(),
		&pb.AddPermissionRequest{RoleId: 1, PermissionId: 2}, rsp); err != nil {
		panic(err)
	}
	println("code:", rsp.Code)
}
```

- 运行说明：在完整工程（已生成 proto、注入 `xorm.Engine`）下编译运行；演示前请在 `role`、`permission` 主表预置数据。
- 代码说明：handler 复用参数获取模板，核心逻辑下沉到 service，关联写入基于 `role_permission`。
- 技术点总结：角色 handler 只管理"角色-权限"关联，不碰权限自身数据；先查后写可避免脏关联插入失败。

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
