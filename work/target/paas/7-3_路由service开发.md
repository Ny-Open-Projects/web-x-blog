# Go PaaS 平台开发: 路由 Service 开发

## 纲要

- `IRouteDataService` 接口：数据库操作 + Kubernetes Ingress 操作
- 用 client-go 的 NetworkingV1 接口创建 / 更新 / 删除 Ingress
- `setIngress`：构造 Ingress 对象（基础信息、ingress-nginx class、规则）
- `getIngressPath`：把路由路径映射为 `HTTPIngressPath`（Prefix 前缀匹配）
- 删除时先删 Ingress，再删数据库记录

上一节完成 model 与 repository，本节在 service 层把「操作数据库」和「操作 Kubernetes Ingress」两件事合并到一起。service 依赖 `IRouteRepository` 与 `kubernetes.Clientset` 两个依赖。

## 接口定义

```go
type IRouteDataService interface {
	AddRoute(*model.Route) (int64, error)
	DeleteRoute(int64) error
	UpdateRoute(*model.Route) error
	FindRouteByID(int64) (*model.Route, error)
	FindAllRoute() ([]model.Route, error)

	CreateRouteToK8s(*route.RouteInfo) error
	DeleteRouteFromK8s(*model.Route) error
	UpdateRouteToK8s(*route.RouteInfo) error
}
```

前五个是纯数据库操作（直接转发给 repository），后三个是与 Kubernetes 交互的核心。构造函数注入 repository 和 clientset：

```go
func NewRouteDataService(routeRepository repository.IRouteRepository, clientSet *kubernetes.Clientset) IRouteDataService {
	return &RouteDataService{RouteRepository: routeRepository, K8sClientSet: clientSet, deployment: &v1.Deployment{}}
}
```

## 创建 Ingress 到 Kubernetes

`CreateRouteToK8s` 先用 `setIngress` 构造对象，再判断是否已存在——已存在则直接报错返回（避免重复创建），不存在则调用 `NetworkingV1().Ingresses(ns).Create`：

```go
func (u *RouteDataService) CreateRouteToK8s(info *route.RouteInfo) (err error) {
	ingress := u.setIngress(info)
	if _, err = u.K8sClientSet.NetworkingV1().Ingresses(info.RouteNamespace).Get(
		context.TODO(), info.RouteName, v14.GetOptions{}); err != nil {
		if _, err = u.K8sClientSet.NetworkingV1().Ingresses(info.RouteNamespace).Create(
			context.TODO(), ingress, v14.CreateOptions{}); err != nil {
			common.Error(err)
			return err
		}
		return nil
	}
	common.Error("路由 " + info.RouteName + " 已经存在")
	return errors.New("路由 " + info.RouteName + " 已经存在")
}
```

> 注意这里用的是 **client-go 的 NetworkingV1 接口**（`k8s.io/api/networking/v1`），和 protobuf 自动生成的接口不同，操作的是真实集群里的 Ingress 资源。

## 构造 Ingress 对象

`setIngress` 设置元数据、使用 `ingress-nginx` 这个 IngressClass，并调用 `getIngressPath` 填充规则：

```go
func (u *RouteDataService) setIngress(info *route.RouteInfo) *v12.Ingress {
	route := &v12.Ingress{}
	route.TypeMeta = v14.TypeMeta{Kind: "Ingress", APIVersion: "v1"}
	route.ObjectMeta = v14.ObjectMeta{
		Name:      info.RouteName,
		Namespace: info.RouteNamespace,
		Labels:    map[string]string{"app-name": info.RouteName, "author": "Caplost"},
		Annotations: map[string]string{"k8s/generated-by-cap": "由Cap老师代码创建"},
	}
	className := "nginx"
	route.Spec = v12.IngressSpec{
		IngressClassName: &className,
		DefaultBackend:   nil,
		TLS:              nil, // 开启 HTTPS 时在此设置
		Rules:            u.getIngressPath(info),
	}
	return route
}
```

课程演示未开启 HTTPS，因此 `TLS` 留空；如需 HTTPS，在这里补充证书配置即可。

## 路径映射到 HTTPIngressPath

`getIngressPath` 给 Ingress 设置 host，并遍历每条 `RoutePath`，生成 `HTTPIngressPath`。路径类型使用 **Prefix（前缀匹配）**：定义了 `/api`，则 `/api/xxx` 也能匹配；第二层路径若不完全相等则匹配不到。

```go
func (u *RouteDataService) getIngressPath(info *route.RouteInfo) (path []v12.IngressRule) {
	pathRule := v12.IngressRule{Host: info.RouteHost}
	ingressPath := []v12.HTTPIngressPath{}
	for _, v := range info.RoutePath {
		pathType := v12.PathTypePrefix
		ingressPath = append(ingressPath, v12.HTTPIngressPath{
			Path:     v.RoutePathName,
			PathType: &pathType,
			Backend: v12.IngressBackend{
				Service: &v12.IngressServiceBackend{
					Name: v.RouteBackendService,
					Port: v12.ServiceBackendPort{Number: v.RouteBackendServicePort},
				},
			},
		})
	}
	pathRule.IngressRuleValue = v12.IngressRuleValue{
		HTTP: &v12.HTTPIngressRuleValue{Paths: ingressPath},
	}
	path = append(path, pathRule)
	return
}
```

因为一个域名可能对应多个后端 Service，所以这里用循环逐个绑定；若要做「一个域名一个路径挂多个 Service」，按相同思路扩展即可。

## 更新与删除

```go
func (u *RouteDataService) UpdateRouteToK8s(info *route.RouteInfo) (err error) {
	ingress := u.setIngress(info)
	if _, err = u.K8sClientSet.NetworkingV1().Ingresses(info.RouteNamespace).Update(
		context.TODO(), ingress, v14.UpdateOptions{}); err != nil {
		common.Error(err)
		return err
	}
	return nil
}

func (u *RouteDataService) DeleteRouteFromK8s(route2 *model.Route) (err error) {
	if err = u.K8sClientSet.NetworkingV1().Ingresses(route2.RouteNamespace).Delete(
		context.TODO(), route2.RouteName, v14.DeleteOptions{}); err != nil {
		common.Error(err)
		return err
	}
	// Ingress 删除成功后，再清理数据库记录
	if err := u.DeleteRoute(route2.ID); err != nil {
		common.Error(err)
		return err
	}
	common.Info("删除 ingress ID：" + strconv.FormatInt(route2.ID, 10) + " 成功！")
	return
}
```

删除顺序很关键：**先删 Kubernetes 里的 Ingress，成功后再删数据库记录**，保证两边最终一致。

## API 速览

| 方法 | 作用 |
| --- | --- |
| `CreateRouteToK8s` | 幂等创建 Ingress（已存在则报错） |
| `UpdateRouteToK8s` | 用最新规则更新 Ingress |
| `DeleteRouteFromK8s` | 先删 Ingress，再删库记录 |
| `AddRoute` / `UpdateRoute` / `DeleteRoute` / `FindRouteByID` / `FindAllRoute` | 纯数据库 CRUD，转发给 repository |

## 技术点总结

- service 层是「数据库 + Kubernetes」双重写入的汇聚点。
- 操作 Ingress 走 client-go NetworkingV1（真实资源），路径匹配用 Prefix。
- 创建做幂等校验，删除严格先 K8s 后数据库，避免脏数据。

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
