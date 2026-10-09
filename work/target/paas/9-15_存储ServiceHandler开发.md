# Go PaaS 平台开发: 存储 ServiceHandler 开发

## 纲要

- Handler 负责入参映射（info → model）与调用顺序编排，业务逻辑在 Service 层已完成
- 创建：先在 K8s 创建 PVC，成功后再同步写入平台数据库
- 删除：先从 K8s 删除 PVC，再删除数据库记录，两步都需处理错误
- 按 ID 查询 / 查询全部：直接从平台数据库读取并做数据转换
- Update 逻辑较复杂（涉及已创建资源的扩容等），课程中暂留作扩展
- 启动时需初始化数据表，并把监听 IP / 端口改为本机可用值避免冲突

## Handler 职责

Handler 层不直接写复杂业务，而是做两件事：

1. 把入参 `info` 映射到模型（通过结构体映射）
2. 编排调用顺序：先 K8s 后数据库，并处理错误返回，便于 API 层定位问题

## Demo 示例

### 代码说明

`handler/storage.go` —— 创建与删除的核心编排：

```go
package handler

import (
	"your-org/storage/service"
	"your-org/storage/model"
)

type StorageHandler struct {
	svc *service.StorageService
}

// Create 创建存储：先建 K8s PVC，成功后再写库
func (h *StorageHandler) Create(info *model.VolumeInput) error {
	m := info.ToModel() // 入参映射到模型

	// 1. 优先在 K8s 中创建 PVC
	if err := h.svc.CreateInK8s(m); err != nil {
		return err
	}
	// 2. K8s 创建成功后，再写入平台数据库
	if err := h.svc.SaveToDB(m); err != nil {
		return err
	}
	return nil
}

// Delete 删除存储：先删 K8s PVC，再删库记录
func (h *StorageHandler) Delete(id uint) error {
	// 1. 先从 K8s 删除
	if err := h.svc.DeleteFromK8s(id); err != nil {
		return err
	}
	// 2. 再删除数据库中的记录
	if err := h.svc.DeleteFromDB(id); err != nil {
		return err
	}
	return nil
}

// GetByID 按 ID 查询，直接查数据库
func (h *StorageHandler) GetByID(id uint) (*model.PVC, error) {
	return h.svc.FindByID(id)
}

// ListAll 查询全部已登记存储
func (h *StorageHandler) ListAll() ([]model.PVC, error) {
	list, err := h.svc.FindAll()
	if err != nil {
		return nil, err
	}
	// 数据转换：统一以对外 info 格式返回
	return toInfoList(list), nil
}
```

`service/storage.go` —— 业务层（K8s 与 DB 两层操作）：

```go
package service

import "your-org/storage/model"

type StorageService struct {
	k8s K8sClient
	db  DBClient
}

// CreateInK8s 在 K8s 创建 PVC（见「存储 Service 开发（上）」）
func (s *StorageService) CreateInK8s(m *model.PVC) error {
	return s.k8s.CreatePVC(m.Namespace, m.Name, m.StorageClass, m.AccessMode, m.Size)
}

// SaveToDB 写入平台数据库
func (s *StorageService) SaveToDB(m *model.PVC) error {
	return s.db.Insert(m)
}

// DeleteFromK8s 从 K8s 删除 PVC
func (s *StorageService) DeleteFromK8s(id uint) error {
	m, err := s.db.FindByID(id)
	if err != nil {
		return err
	}
	return s.k8s.DeletePVC(m.Namespace, m.Name)
}

// DeleteFromDB 删除数据库记录
func (s *StorageService) DeleteFromDB(id uint) error {
	return s.db.Delete(id)
}

// FindByID / FindAll 数据库查询
func (s *StorageService) FindByID(id uint) (*model.PVC, error) { return s.db.FindByID(id) }
func (s *StorageService) FindAll() ([]model.PVC, error)         { return s.db.FindAll() }
```

### 技术点总结

- 创建顺序强调"先 K8s 后 DB"：保证平台记录与实际资源一致，避免库里有记录但 K8s 创建失败导致的脏数据
- 删除顺序强调"先 K8s 后 DB"：同样保证实际资源被清理后再清记录
- `Update` 涉及已创建资源的扩容等复杂关注点，课程暂不实现，感兴趣可自行在 Service 层扩展
- 查询类接口直接从自有数据层返回，无需走 K8s，响应更快
- 启动时要先初始化数据表（`AutoMigrate`），并将监听 IP 写成本机 IP、端口避开冲突

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
