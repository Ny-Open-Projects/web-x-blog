# Go PaaS 平台开发: 接入 K8s 客户端、初始化数据表并注册服务（下）

## 纲要

- 校验上节创建的 K8s 客户端（Clientset）可用。
- 作为客户端调用其他服务时，引入熔断插件做容错。
- 数据库表只需要在首次启动时通过 `AutoMigrate` 自动创建一次，无需 SQL 文件导入导出。
- 把 K8s 客户端传入 Repository/Service，用于真正操作集群资源。
- 初始化 Handler 并注册到微服务，启动服务对外提供能力。
- 回顾集群外与集群内两种 config 创建方式。

## 校验 K8s 客户端

上节通过 `clientcmd.BuildConfigFromFlags` 得到了 `rest.Config`，并用 `kubernetes.NewForConfig` 生成了 `Clientset`。拿到 clientset 后，先做一次简单调用验证它可用，例如列出命名空间或节点：

```go
// 用 clientset 做一次真实调用，验证连通性
func Ping(clientset *kubernetes.Clientset) error {
    _, err := clientset.CoreV1().Namespaces().List(context.TODO(), metav1.ListOptions{})
    if err != nil {
        return fmt.Errorf("k8s 客户端不可用: %v", err)
    }
    return nil
}
```

验证通过后，再进入后续逻辑，避免在无效客户端上继续操作。

## 调用其他服务时引入熔断

当本服务要去调用别的微服务时，就用到上一节准备好的熔断插件。熔断作为客户端 Wrapper 注入，每个服务的降级逻辑写在各自插件里：

```go
// 作为客户端去调用其他服务，挂上熔断 Wrapper
micro.WrapClient(hystrix2.NewClientHystrixWrapper()),
```

熔断插件的核心是在 `hystrix.Do` 中区分"正常执行"与"走熔断降级"两条路径，业务相关的返回值在这里处理，从而限制对下游的并发冲击（例如限额 1000，超过则走熔断或返回兜底信息）。

## 初始化数据表

平台模型（如 Pod、AppPod 等）定义好字段后，无需手写 SQL 导入导出，首次启动时用 GORM 的 `AutoMigrate` 自动建表即可：

```go
// 仅在首次执行，后续重复执行可注释掉
func InitTable(db *gorm.DB) {
    db.AutoMigrate(
        &model.Pod{},
        &model.PodEnv{},
        &model.PodPort{},
        &model.AppPod{},
    )
}
```

要点：

- 建表只初始化一次；第二次启动若不需要重建，把 `AutoMigrate` 注释掉，避免重复开销。
- 字段结构以模型为准，GORM 会自动创建对应列。

## 把 K8s 客户端接入数据访问层

K8s 客户端真正操作集群的逻辑放在 Repository/Service 层。因为数据访问层需要它来创建、删除、更新集群内的资源，所以初始化时要将 clientset 传进去：

```go
// Repository 持有 K8s 客户端，用于操作集群
type PodRepository struct {
    db        *gorm.DB
    clientset *kubernetes.Clientset
}

func NewPodRepository(db *gorm.DB, clientset *kubernetes.Clientset) *PodRepository {
    return &PodRepository{db: db, clientset: clientset}
}
```

service 层在此基础上封装"创建到 K8s / 从 K8s 删除 / 更新"等业务方法，供 Handler 调用。

## 注册 Handler 并启动服务

Handler 在 `main.go` 中初始化并注册到微服务，然后启动对外提供服务：

```go
// 初始化 K8s 客户端
clientset, err := k8s.NewClientOutOfCluster()
if err != nil {
    common.Fatal(err)
}

// 初始化数据表（仅首次）
InitTable(db)

// 创建数据服务
podDataService := service.NewPodDataService(repository.NewPodRepository(db, clientset))

// 注册 Handler 到微服务
pod.RegisterPodHandler(service.Server(), &handler.PodHandler{PodDataService: podDataService})

// 启动服务
if err := service.Run(); err != nil {
    common.Fatal(err)
}
```

启动后，服务会注册到 Consul。打开 Consul 控制台即可看到该服务，说明它已正常对外暴露。

## 集群外与集群内 config 创建方式回顾

两种方式的核心差异在 `rest.Config` 来源：

| 场景 | 创建方式 | 说明 |
| --- | --- | --- |
| 集群外 | `clientcmd.BuildConfigFromFlags("", kubeConfig)` | 读取本地 `~/.kube/config` |
| 集群内 | `rest.InClusterConfig()` | 读取 Pod 挂载的 ServiceAccount |

另外，数据库初始化用的 `AutoMigrate` 同样只执行一次即可，不需要用 SQL 文件导入导出。

## 衔接

本篇把 K8s 客户端接入了服务，并完成数据表初始化与服务注册。下一篇开始编写 Pod 的 Handler 业务逻辑（增删改查），实现对外服务的五个方法。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/k8s-install/check_host.sh`
- `code/课件/common/config.go`
- `code/课件/middleware/domain/model/middle_config.go`
- `code/课件/k8s-install/install_master.sh`
- `code/课件/go-paas-html/pages-404.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：94%。是否需要继续：是。代码是否可运行：是。
