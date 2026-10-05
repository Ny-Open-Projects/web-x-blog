# Go PaaS 平台开发: Pod Handler 对外服务逻辑实现（下）

## 纲要

- 更新 Pod：先更新 K8s 中的资源，再同步数据库记录。
- 按 ID 查询：优先使用数据库维度（业务字段更全），再转换为响应体返回。
- 查询全部：遍历数据集合并逐条转换为 proto，整理成统一格式返回。
- 数据库维度高于 K8s 维度：计费、团队等业务字段只在数据库存储。
- 五个方法全部实现后，通过运行服务 + 查库 + 查 K8s 完成端到端验证。

## 更新 Pod

更新遵循"先更新集群，再同步数据库"的顺序：

```go
// 更新指定的 pod
func (e *PodHandler) UpdatePod(ctx context.Context, req *pod.PodInfo, rsp *pod.Response) error {
    // 先更新 k8s 中的 pod 信息
    err := e.PodDataService.UpdateToK8s(req)
    if err != nil {
        common.Error(err)
        return err
    }
    // 查询数据库中的 pod
    podModel, err := e.PodDataService.FindPodByID(req.Id)
    if err != nil {
        common.Error(err)
        return err
    }
    // 把请求体映射回模型
    err = common.SwapTo(req, podModel)
    if err != nil {
        common.Error(err)
        return err
    }
    // 更新数据库
    e.PodDataService.UpdatePod(podModel)
    return nil
}
```

`UpdateToK8s` 按要求把副本数、镜像、端口等变更下发到集群；数据库侧则保持业务字段（如团队、计费）与应用最新状态一致。

## 按 ID 查询

查询接口先从数据库取出模型，再转换为响应体：

```go
// 查询单个信息
func (e *PodHandler) FindPodByID(ctx context.Context, req *pod.PodId, rsp *pod.PodInfo) error {
    podModel, err := e.PodDataService.FindPodByID(req.Id)
    if err != nil {
        common.Error(err)
        return err
    }
    // 模型 -> 响应体
    err = common.SwapTo(podModel, rsp)
    if err != nil {
        common.Error(err)
        return err
    }
    return nil
}
```

为什么以数据库为准？因为 K8s 里的 Pod 数据主要是运行状态维度，而平台按业务需要额外存储了计费、团队等字段，这些维度更偏向业务侧，数据库才是完整视图。

## 查询全部

查询所有 Pod 时，先把集合取出，逐条转换并 append 到响应：

```go
// 查询所有 pod
func (e *PodHandler) FindAllPod(ctx context.Context, req *pod.FindAll, rsp *pod.AllPod) error {
    allPod, err := e.PodDataService.FindAllPod()
    if err != nil {
        common.Error(err)
        return err
    }
    // 整理格式
    for _, v := range allPod {
        podInfo := &pod.PodInfo{}
        err := common.SwapTo(v, podInfo)
        if err != nil {
            common.Error(err)
            return err
        }
        rsp.PodInfo = append(rsp.PodInfo, podInfo)
    }
    return nil
}
```

## 五个方法汇总

| 方法 | 入参 | 主要动作 |
| --- | --- | --- |
| AddPod | `PodInfo` | 转换模型 → 创建到 K8s → 落库 |
| DeletePod | `PodId` | 查模型 → 删 K8s 资源 → 删库 |
| UpdatePod | `PodInfo` | 更新 K8s → 同步库 |
| FindPodByID | `PodId` | 按 ID 查库 → 转响应 |
| FindAllPod | `FindAll` | 查全部 → 逐条转换返回 |

五个方法全部实现后，Handler 无编译报错，说明对外服务契约已满足。

## 端到端验证

1. 启动服务：数据库无表时 `AutoMigrate` 自动建表；日志统一写入 `micro.log`。
2. 查库：确认数据表与字段自动创建成功。
3. 查 K8s：`kubectl get pods` 确认资源状态正常。
4. 通过后续 API 层与前端页面发起调用，验证整条链路（前端 → 网关 → API → Service → K8s / 数据库）打通。

## 衔接

Pod 后端服务五个方法已开发完成，标志着后端服务收尾。下一篇把它们打包进 Docker 镜像，并讲解容器网络隔离带来的地址配置注意事项。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/go-paas-html/pages-404.html`
- `code/课件/pod/handler/podHandler.go`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/go-paas-html/pages-login.html`
- `code/课件/go-paas-html/pages-login2.html`
- `code/课件/go-paas-html/pages-sign-up.html`
- `code/课件/go-paas-html/layouts-nosidebars.html`
- `code/课件/go-paas-front/volume-create.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：95%。是否需要继续：是。代码是否可运行：是。
