# Go PaaS 平台开发: Service 服务端 model 模型开发

## 纲要

- 开发前置**三步走**：① 用 cap-tool 生成代码目录 → ② 生成 proto 文件 → ③ 启动 cap-api-gateway。
- 目录生成走 **docker** 方式：挂载当前目录、传入授权码，服务名 `new-service` **必须连写且大写**。
- 生成后依次执行：`make proto`（生成 pb.go）→ `go mod`（拉依赖）→ 编译启动 → 在**注册中心**确认服务存在。
- **Service 模型**：服务名（唯一、非空）、命名空间（非空）、绑定 Pod 名（非空）、服务类型（四种）、团队 ID、端口集合。
- **SvcPort 结构体**：`ServicePort` / `TargetPort` / `NodePort` / 协议（协议必填）；ExternalName 类型额外需要外部名子段。

## 一、开发前置流程（三步走）

1. **生成代码目录**：使用 cap-tool（docker 方式）按模板创建工程目录。
2. **生成 proto 文件**：在生成目录基础上用 `make proto` 生成协议代码。
3. **启动网关**：把 `cap-api-gateway` 启动起来。

### 目录生成命令

```bash
docker run --rm \
  -v $(pwd):/work -w /work \
  -e IQ_CODE=<你的授权码> \
  <cap-tools-image> \
  new-service \
  service/
```

- `--rm`：用完即删容器；`-v` 把主机当前目录与容器内工作目录对应。
- `IQ_CODE`：购买课程后在课程详情页右侧获取的授权码，替换成自己的即可。
- `new-service`：**必须连起来写、首字母大写**，不能分开。
- 最后的参数是生成目录地址，会按 `/` 逐级创建目录并把代码生成进去。
- 出现成功提示即表示目录创建完成。

### 生成后的操作

```bash
make proto     # 生成 pb.go（proto 对应的 Go 文件）
go mod tidy    # 拉取依赖
go build       # 编译，检测能否启动成功
```

启动成功后，可在**注册中心**查看服务是否存在。

> 说明：生成的代码里会有一些"未生成 pb.go / 依赖未拉取"导致的编辑器报红，属正常现象，不影响后续生成。

## 二、Service 模型字段设计

| 字段 | 约束 | 说明 |
|------|------|------|
| 服务名称 | **唯一、非空** | 服务名唯一标识 |
| 命名空间 | **非空** | 所属 namespace |
| 绑定 Pod 名 | **非空** | 不写就不知道绑定到哪个 Pod |
| 服务类型 | 四选一 | `ClusterIP` / `NodePort` / `LoadBalancer` / `ExternalName` |
| ExternalName | 仅 ExternalName 类型需要 | 其他类型可为空 |
| 团队 ID | 字符串 | 虽叫 ID，但可能是名字，故用字符串；用于团队隔离 |
| 端口 | 可多个 | 课程演示一个端口 |

```go
package model

// Service 服务管理主模型
type Service struct {
	ID           int64     `gorm:"primary_key;auto_increment" json:"id"`
	ServiceName  string    `gorm:"unique;not null" json:"service_name"`  // 服务名称，唯一且不为空
	Namespace    string    `gorm:"not null" json:"namespace"`            // 命名空间，不为空
	PodName      string    `gorm:"not null" json:"pod_name"`             // 绑定的 Pod 名称，不为空
	ServiceType  string    `json:"service_type"`                         // ClusterIP/NodePort/LoadBalancer/ExternalName
	ExternalName string    `json:"external_name"`                        // 仅 ExternalName 类型需要，其余可空
	TeamID       string    `json:"team_id"`                              // 团队隔离用（可能是名字，故用 string）
	SvcPort      []SvcPort `gorm:"foreignkey:ServiceID" json:"svc_port"` // 端口集合
}
```

## 三、SvcPort 端口结构体

用来绑定服务的端口信息，与 Service 是一对多关系：

| 字段 | 说明 |
|------|------|
| `ServicePort` | Service 对外暴露的端口 |
| `TargetPort` | 容器（Pod）中实际映射的目标端口 |
| `NodePort` | **仅 NodePort 模式**需要设置；课程用 ClusterIP，故仅预留字段 |
| `PortProtocol` | 端口协议（如 TCP/UDP），**必填** |

```go
// SvcPort 服务端口
type SvcPort struct {
	ID           int64  `gorm:"primary_key;auto_increment" json:"id"`
	ServiceID    int64  `json:"service_id"`
	ServicePort  int32  `json:"service_port"`            // Service 暴露端口
	TargetPort   int32  `json:"target_port"`             // 容器目标端口（containerPort）
	NodePort     int32  `json:"node_port"`               // 节点端口，NodePort 模式下设置
	PortProtocol string `gorm:"not null" json:"port_protocol"` // 端口协议，必填
}
```

## 四、数据表创建

在 `main.go` 中，首次执行时会打开并创建对应的数据表（GORM AutoMigrate），无需手写建表 SQL：

```go
// 首次运行自动建表
if err := db.AutoMigrate(&model.Service{}, &model.SvcPort{}); err != nil {
	// 处理错误
}
```

## 小结

- 先走**三步走**把工程骨架和 proto 准备好，再写业务 model。
- Service 模型的关键是**服务名唯一 + 命名空间 + 绑定 Pod 名**三个非空约束。
- 端口拆成独立的 `SvcPort` 结构体，支持一服务多端口，并预留 `NodePort` 字段。
- 下一节开发 Service 的 proto 文件并生成代码。
