# Go PaaS 平台开发: Service 服务开发（K8s 增删改查）

## 纲要

- 服务层 `SvcDataService` 接口：数据库 CRUD + K8s 操作两类方法
- 依赖注入：`ISvcRepository`（数据访问）与 `K8sClientSet`（K8s 客户端）
- `CreateSvcToK8s`：先查后建，避免重复创建，构建 `v1.Service`
- `setService`：把 `SvcInfo` 映射为 K8s 对象（ObjectMeta / Spec / ClusterIP）
- `UpdateSvcToK8s` / `DeleteFromK8s`：先查后改、先删 K8s 再删库
- 平台把"K8s 实际资源"与"数据库记录"两个动作封装在一次调用里

## 服务层结构

`SvcDataService` 同时承载两个职责：对数据库的持久化（委托给 `repository`）与对 Kubernetes 的实际操作（通过 `client-go` 的 `K8sClientSet`）。构造函数把两者注入：

```go
type ISvcDataService interface {
	AddSvc(*model.Svc) (int64, error)
	DeleteSvc(int64) error
	UpdateSvc(*model.Svc) error
	FindSvcByID(int64) (*model.Svc, error)
	FindAllSvc() ([]model.Svc, error)
	CreateSvcToK8s(*svc.SvcInfo) error
	UpdateSvcToK8s(*svc.SvcInfo) error
	DeleteFromK8s(*model.Svc) error
}

func NewSvcDataService(svcRepository repository.ISvcRepository, clientSet *kubernetes.Clientset) ISvcDataService {
	return &SvcDataService{SvcRepository: svcRepository, K8sClientSet: clientSet}
}

type SvcDataService struct {
	SvcRepository repository.ISvcRepository
	K8sClientSet  *kubernetes.Clientset
}
```

> 平台约定：纯数据库操作（增删改查）由 `repository` 实现，业务层直接委托；只有涉及 K8s 资源生命周期的方法才写在服务层。

## 创建服务到 K8s

`CreateSvcToK8s` 的核心逻辑："先按命名空间 + 名称查找，找不到才创建"。这样天然实现了幂等，重复点击创建不会报错。

```go
func (u *SvcDataService) CreateSvcToK8s(svcInfo *svc.SvcInfo) (err error) {
	service := u.setService(svcInfo)
	// 查找是否已存在指定服务
	if _, err = u.K8sClientSet.CoreV1().Services(svcInfo.SvcNamespace).Get(
		context.TODO(), svcInfo.SvcName, v12.GetOptions{}); err != nil {
		// 查找不到，就创建
		if _, err = u.K8sClientSet.CoreV1().Services(svcInfo.SvcNamespace).Create(
			context.TODO(), service, v12.CreateOptions{}); err != nil {
			common.Error(err)
			return err
		}
		return nil
	}
	common.Error("Service " + svcInfo.SvcName + "已经存在")
	return errors.New("Service " + svcInfo.SvcName + "已经存在")
}
```

## 把 SvcInfo 映射为 K8s Service

`setService` 是平台的关键转换函数：用 `SvcInfo` 拼出 `v1.Service` 的元信息与服务规格。课程固定采用 `ClusterIP` 模式，`Selector` 与 `Labels` 都写 `app-name=SvcPodName`，与第 6.1 节讲的"标签选择"完全一致。

```go
func (u *SvcDataService) setService(svcInfo *svc.SvcInfo) *v1.Service {
	service := &v1.Service{}
	service.ObjectMeta = v12.ObjectMeta{
		Name:      svcInfo.SvcName,
		Namespace: svcInfo.SvcNamespace,
		Labels: map[string]string{
			"app-name": svcInfo.SvcPodName,
			"author":   "Caplost",
		},
		Annotations: map[string]string{
			"k8s/generated-by-cap": "由Cap老师代码创建",
		},
	}
	service.Spec = v1.ServiceSpec{
		Ports: u.getSvcPort(svcInfo),
		Selector: map[string]string{
			"app-name": svcInfo.SvcPodName,
		},
		Type: "ClusterIP",
	}
	return service
}
```

端口映射逻辑（`getSvcPort`）枚举 `SvcInfo.SvcPort`，逐个生成 `v1.ServicePort`：

```go
func (u *SvcDataService) getSvcPort(svcInfo *svc.SvcInfo) (servicePort []v1.ServicePort) {
	for _, v := range svcInfo.SvcPort {
		servicePort = append(servicePort, v1.ServicePort{
			Name:       "port-" + strconv.FormatInt(int64(v.SvcPort), 10),
			Protocol:   v1.Protocol(v.SvcPortProtocol),
			Port:       v.SvcPort,
			TargetPort: intstr.FromInt(int(v.SvcTargetPort)),
		})
	}
	return
}
```

## 更新与删除

更新同样"先查后改"：查不到说明服务未创建，直接报错；查到才 `Update`。

```go
func (u *SvcDataService) UpdateSvcToK8s(svcInfo *svc.SvcInfo) (err error) {
	service := u.setService(svcInfo)
	if _, err = u.K8sClientSet.CoreV1().Services(svcInfo.SvcNamespace).Get(
		context.TODO(), svcInfo.SvcName, v12.GetOptions{}); err != nil {
		return errors.New("Service" + svcInfo.SvcName + "不存在请先创建")
	}
	if _, err = u.K8sClientSet.CoreV1().Services(svcInfo.SvcNamespace).Update(
		context.TODO(), service, v12.UpdateOptions{}); err != nil {
		common.Error(err)
		return err
	}
	common.Info("Service " + svcInfo.SvcName + "更新成功")
	return nil
}
```

删除做了"两步收尾"：先删 K8s 中的 Service，再删数据库记录，保证两端一致。

```go
func (u *SvcDataService) DeleteFromK8s(svc *model.Svc) (err error) {
	if err = u.K8sClientSet.CoreV1().Services(svc.SvcNamespace).Delete(
		context.TODO(), svc.SvcName, v12.DeleteOptions{}); err != nil {
		common.Error(err)
		return err
	}
	if err := u.DeleteSvc(svc.ID); err != nil {
		common.Error(err)
		return err
	}
	common.Info("删除Service ID：" + strconv.FormatInt(svc.ID, 10) + "成功！")
	return
}
```

## 数据库侧方法

纯持久化方法直接委托 repository，业务层几乎零逻辑：

```go
func (u *SvcDataService) AddSvc(svc *model.Svc) (int64, error)      { return u.SvcRepository.CreateSvc(svc) }
func (u *SvcDataService) DeleteSvc(svcID int64) error               { return u.SvcRepository.DeleteSvcByID(svcID) }
func (u *SvcDataService) UpdateSvc(svc *model.Svc) error           { return u.SvcRepository.UpdateSvc(svc) }
func (u *SvcDataService) FindSvcByID(svcID int64) (*model.Svc, error) { return u.SvcRepository.FindSvcByID(svcID) }
func (u *SvcDataService) FindAllSvc() ([]model.Svc, error)         { return u.SvcRepository.FindAll() }
```

## API 速览

| 方法 | 入参 | 行为 |
| --- | --- | --- |
| `CreateSvcToK8s` | `*svc.SvcInfo` | 先查后建，幂等 |
| `UpdateSvcToK8s` | `*svc.SvcInfo` | 先查后改 |
| `DeleteFromK8s` | `*model.Svc` | 先删 K8s 再删库 |
| `AddSvc` / `UpdateSvc` / `DeleteSvc` / `FindSvcByID` / `FindAllSvc` | model / id | 委托 repository 做持久化 |

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/base/domain/service/base_data_service.go`
- `code/课件/appstore/domain/service/appStore_data_service.go`
- `code/课件/middleware/domain/service/middle_type_data_service.go`
- `code/课件/svc/domain/service/svc_data_service.go`
- `code/课件/route/domain/service/route_data_service.go`
- `code/课件/volume/domain/service/volume_data_service.go`
- `code/课件/pod/domain/service/pod_data_service.go`
- `code/课件/middleware/domain/service/middleware_data_service.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
