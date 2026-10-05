# Go PaaS 平台开发: API 完善与 Pod 前端页面开发（下）

## 纲要

- 补全 `AddPod`：先单独处理端口（多值、默认 TCP），再用 `form` 插件把表单字段映射到结构体。
- `form` 插件 `FromToPodStruct` 按 json 标签把前端 name 映射到结构体字段并做类型转换，端口/环境变量单独处理。
- 类型转换 `TypeConversion` 支持 string/int/int32/int64/float/time 等。
- 前端 `pod-create.html` 表单 `action` 指向网关 `/podApi/AddPod`，各 `input` 的 `name` 与 `PodInfo` 的 json 标签一一对应。
- 演示：从页面创建应用（副本 2、端口 8081、nginx 镜像），验证数据库与 K8s 双写成功，并能删除。

## AddPod 完整实现

端口是数组类型且含协议，不能走通用映射，因此先单独解析，再交给 `form` 插件处理其余普通字段：

```go
func (e *PodApi) AddPod(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.AddPod 的请求")
    addPodInfo := &pod.PodInfo{}

    // 1. 单独处理 port（多值）
    dataSlice, ok := req.Post["pod_port"]
    if ok {
        podSlice := []*pod.PodPort{}
        for _, v := range dataSlice.Values {
            i, err := strconv.ParseInt(v, 10, 32)
            if err != nil {
                common.Error(err)
            }
            port := &pod.PodPort{
                ContainerPort: int32(i),
                Protocol:      "TCP",
            }
            podSlice = append(podSlice, port)
        }
        addPodInfo.PodPort = podSlice
    }

    // 2. form 通用字段转换到结构体
    from.FromToPodStruct(req.Post, addPodInfo)

    // 3. 调用后端添加
    response, err := e.PodService.AddPod(ctx, addPodInfo)
    if err != nil {
        common.Error(err)
        return err
    }
    rsp.StatusCode = 200
    b, _ := json.Marshal(response)
    rsp.Body = string(b)
    return nil
}
```

环境变量（`pod_env`）与端口同理，可在 API 层单独遍历 `req.Post` 后构造切片，再交给后端；通用字段交给插件即可。

## form 插件

`from.FromToPodStruct` 利用反射，按结构体 json 标签（去掉 `,omitempty`）匹配表单 key，并做类型转换：

```go
// 根据结构体中 json 标签映射数据到结构体中并且转换类型
func FromToPodStruct(data map[string]*podApi.Pair, obj interface{}) {
    objValue := reflect.ValueOf(obj).Elem()
    for i := 0; i < objValue.NumField(); i++ {
        dataTag := strings.Replace(objValue.Type().Field(i).Tag.Get("json"), ",omitempty", "", -1)
        dataSlice, ok := data[dataTag]
        if !ok {
            continue
        }
        valueSlice := dataSlice.Values
        if len(valueSlice) <= 0 {
            continue
        }
        // 端口、环境变量的单独处理
        if dataTag == "pod_port" || dataTag == "pod_env" {
            continue
        }
        value := valueSlice[0]
        name := objValue.Type().Field(i).Name
        structFieldType := objValue.Field(i).Type()
        val := reflect.ValueOf(value)
        var err error
        if structFieldType != val.Type() {
            val, err = TypeConversion(value, structFieldType.Name()) // 类型转换
            if err != nil {
                common.Error(err)
            }
        }
        objValue.FieldByName(name).Set(val)
    }
}
```

类型转换函数覆盖常见类型：

```go
func TypeConversion(value string, ntype string) (reflect.Value, error) {
    switch ntype {
    case "string":
        return reflect.ValueOf(value), nil
    case "int":
        i, err := strconv.Atoi(value)
        return reflect.ValueOf(i), err
    case "int32":
        i, err := strconv.ParseInt(value, 10, 32)
        return reflect.ValueOf(int32(i)), err
    case "int64":
        i, err := strconv.ParseInt(value, 10, 64)
        return reflect.ValueOf(i), err
    case "float32":
        i, err := strconv.ParseFloat(value, 64)
        return reflect.ValueOf(float32(i)), err
    case "float64":
        i, err := strconv.ParseFloat(value, 64)
        return reflect.ValueOf(i), err
    case "time.Time", "Time":
        t, err := time.ParseInLocation("2006-01-02 15:04:05", value, time.Local)
        return reflect.ValueOf(t), err
    default:
        return reflect.ValueOf(value), errors.New("未知的类型：" + ntype)
    }
}
```

API 层做前端数据过滤与结构体装配的好处：后端 Service 直接拿到整理好的结构体，业务逻辑稳定；前端字段变化只在 API 层调整。

## 前端创建页

`pod-create.html` 的表单 `action` 指向网关地址，`input` 的 `name` 与 `PodInfo` 的 json 标签对应，从而实现自动映射：

```html
<form action="http://localhost:8080/podApi/AddPod" class="form-horizontal" method="post">
    <input type="text" required name="pod_name">
    <input type="text" required name="pod_namespace" value="default">
    <input type="text" required name="pod_pull_policy" value="Always">
    <input type="text" required name="pod_replicas">
    <input type="text" required name="pod_port">
    <input type="text" required name="pod_restart" value="Always">
    <input type="text" required name="pod_team_id">
    <input type="text" required name="pod_type" value="Rolling">
    <input type="text" required name="pod_image">
    <button type="submit" class="btn btn-primary">创建应用</button>
</form>
```

要点：

- `name` 必须与后端结构体 json 标签一致（下划线小写），否则 `FromToPodStruct` 匹配不到。
- 地址写死为开发环境网关（`localhost:8080`）。部署到远程时务必改为真实网关地址。
- 端口支持多个 input（同名 `pod_port`），后端会聚合成 `PodPort` 切片。

## 端到端演示

填写表单创建应用：

- 应用名称：`holle-world`（K8s 不允许大写，用小写）。
- 命名空间：`default`。
- 拉取策略：`Always`。
- 副本个数：`2`。
- 端口：`8081`。
- 团队 ID：随意（预留字段）。
- 更新策略：`Rolling`。
- 镜像：`nginx`（K8s 自动从官网拉取最新）。

点击创建后：

1. 后端收到 `AddPod` 请求，先创建到 K8s，再落库。
2. 数据库应用表中出现该记录。
3. `kubectl get pods` 可见两个副本（`holle-world` 相关）均为 `Running`，说明副本数设置生效。
4. 列表页刷新可见该应用；详情页展示完整信息；点击删除可同时清理 K8s 资源与数据库记录。

这说明"前端表单 → 网关 → API → Service → K8s / 数据库"的完整链路已打通。CPU、内存等字段可在表单中扩展，未设置时列表显示为空。

## 衔接

本篇完成 API 完善与前端开发，本章核心开发任务基本收尾。下一篇做整体总结与开发路径回顾，并给出三个开放性思考题。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/podapi/filebeat.yml`
- `code/课件/podapi/go.mod`
- `code/课件/podapi/proto/podApi/podApi.proto`
- `code/课件/podapi/plugin/hystrix/hystrix.go`
- `code/课件/podapi/plugin/form/from.go`
- `code/课件/podapi/main.go`
- `code/课件/podapi/README.md`
- `code/课件/podapi/handler/podApiHandler.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：95%。是否需要继续：是。代码是否可运行：是。
