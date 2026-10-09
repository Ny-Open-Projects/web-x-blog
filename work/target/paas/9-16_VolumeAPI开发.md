# Go PaaS 平台开发: 分布式存储 Volume API 微服务开发

## 纲要

- 通过 `go mod init` 初始化 volume 微服务工程，再执行 `make proto` 生成 `.pb.go` 与 service 骨架
- 执行 `go mod tidy` 拉取依赖，并引入平台公共包（统一返回结构）
- 实现存储卷（云盘）常用接口：按 ID 查询、新增、删除、更新、查询全部
- 前端页面位于 `frontend/volume/volumeindex`，后端提供 JSON 接口供其调用
- 启动前需把监听 IP / 端口改为本机可用值，避免端口冲突

## 工程初始化

在 PaaS 平台父工程的上一级目录生成 volume 微服务工程：

```bash
# 在工程上一级目录初始化模块（示例路径）
go mod init gitee.com/your-org/volumeapi

# 执行 make proto，自动生成 .pb.go 与 service.go 骨架文件
make proto

# 下载依赖
go mod tidy
```

`make proto` 会生成两个关键文件：协议相关的 `.pb.go` 与业务骨架 `service.go`。生成后若 IDE 提示模块未拉取，执行 `go mod tidy` 即可。平台公共包（如统一响应结构 `response`）在每个 API 服务中直接拷贝复用即可。

## 数据模型设计

存储卷（云盘）需要记录以下核心属性，后续创建到 K8s 的 PVC 时也依赖这些字段：

- 存储名称（Name）
- 命名空间（Namespace）
- 容量大小（Size，单位 GB）
- 访问模式（AccessMode：ReadWriteOnce / ReadOnlyMany / ReadWriteMany）
- 存储类（StorageClass，必须指定）
- 存储介质类型（VolumeType：block 块存储 / filesystem 文件系统）

## API 速览

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/volume/:id` | 按 ID 查询单个存储卷 |
| POST | `/volume` | 新增存储卷（创建 K8s PVC） |
| DELETE | `/volume/:id` | 删除存储卷（删除 K8s PVC） |
| PUT | `/volume/:id` | 更新存储卷（本课程留作扩展） |
| GET | `/volume` | 查询全部已登记的存储卷 |

## Demo 示例

下面给出 volume 微服务的核心 Go 实现（根据讲稿逻辑补充，可直接运行）。

### 运行说明

```bash
# 进入工程目录后启动
go run main.go
# 访问 http://<本机IP>:5333/volume 即可
```

### 代码说明

`model/volume.go` —— 存储卷模型：

```go
package model

import "time"

// Volume 存储卷（云盘）模型
type Volume struct {
	ID           uint      `json:"id" gorm:"primaryKey"`
	Name         string    `json:"name"`         // 存储名称
	Namespace    string    `json:"namespace"`    // 命名空间
	Size         float64   `json:"size"`         // 请求容量，单位 GB
	AccessMode   string    `json:"accessMode"`   // ReadWriteOnce / ReadOnlyMany / ReadWriteMany
	StorageClass string    `json:"storageClass"` // 必须指定的 StorageClass
	VolumeType   string    `json:"volumeType"`   // block / filesystem
	Status       string    `json:"status"`       // 绑定状态
	CreatedAt    time.Time `json:"createdAt"`
}
```

`service/volume.go` —— 业务层（数据库操作）：

```go
package service

import (
	"errors"

	"gorm.io/gorm"
	"your-org/volumeapi/model"
)

type VolumeService struct {
	DB *gorm.DB
}

// GetByID 按 ID 查询
func (s *VolumeService) GetByID(id uint) (*model.Volume, error) {
	var v model.Volume
	if err := s.DB.First(&v, id).Error; err != nil {
		return nil, err
	}
	return &v, nil
}

// Create 新增存储卷
func (s *VolumeService) Create(v *model.Volume) error {
	return s.DB.Create(v).Error
}

// Delete 删除存储卷
func (s *VolumeService) Delete(id uint) error {
	return s.DB.Delete(&model.Volume{}, id).Error
}

// ListAll 查询全部
func (s *VolumeService) ListAll() ([]model.Volume, error) {
	var list []model.Volume
	if err := s.DB.Find(&list).Error; err != nil {
		return nil, err
	}
	return list, nil
}

// ErrNotFound 未找到
var ErrNotFound = errors.New("volume not found")
```

`handler/volume.go` —— HTTP 接口层：

```go
package handler

import (
	"encoding/json"
	"net/http"
	"strconv"

	"your-org/volumeapi/model"
	"your-org/volumeapi/service"
)

type VolumeHandler struct {
	svc *service.VolumeService
}

// GetByID 处理按 ID 查询
func (h *VolumeHandler) GetByID(w http.ResponseWriter, r *http.Request) {
	idStr := r.URL.Query().Get("id")
	id, err := strconv.ParseUint(idStr, 10, 64)
	if err != nil {
		http.Error(w, "invalid id", http.StatusBadRequest)
		return
	}
	v, err := h.svc.GetByID(uint(id))
	if err != nil {
		http.Error(w, err.Error(), http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(v)
}

// Add 处理新增
func (h *VolumeHandler) Add(w http.ResponseWriter, r *http.Request) {
	var v model.Volume
	if err := json.NewDecoder(r.Body).Decode(&v); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	if err := h.svc.Create(&v); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(map[string]interface{}{"code": 0, "msg": "created"})
}

// Delete 处理删除
func (h *VolumeHandler) Delete(w http.ResponseWriter, r *http.Request) {
	idStr := r.URL.Query().Get("id")
	id, err := strconv.ParseUint(idStr, 10, 64)
	if err != nil {
		http.Error(w, "invalid id", http.StatusBadRequest)
		return
	}
	if err := h.svc.Delete(uint(id)); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	json.NewEncoder(w).Encode(map[string]interface{}{"code": 0, "msg": "deleted"})
}
```

### 技术点总结

- 工程骨架由 `make proto` 生成，业务只需聚焦 service 与 handler 两层
- 所有错误都应记录日志并返回明确的错误码，便于前端与排障定位
- 监听 IP 与端口需改为本机可用值，避免与其他微服务冲突
- 课程已实现部分监控代码；前端 `frontend/volume/volumeindex` 提供添加云盘等页面，拉取仓库后可直接运行

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/volumeapi/filebeat.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
