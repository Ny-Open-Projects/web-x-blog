# Go PaaS 平台开发: API 完善与 Pod 前端页面开发（上）

## 纲要

- 完善 API 默认接口 `Call`：实现"查询全部 Pod"，前端列表默认访问该地址。
- 完善 `DeletePodById`：从 URL 参数取 `pod_id`，调用后端删除服务。
- `UpdatePod` 与 `AddPod` 业务逻辑留待下一篇补全。
- 前端采用 HTML + jQuery 前后端分离方式，列表页 `pod-index.html` 用 AJAX 拉取数据。
- 详情页 `pod-detail.html` 按 `pod_id` 查询并回填表单。
- 前端访问地址统一指向网关（如 `http://127.0.0.1:8080/podApi/`）。

## 完善查询全部（默认接口 Call）

前端进入应用列表时，默认访问 `/podApi/`（即默认 `Call` 方法），由它返回全部 Pod。这里调用后端 `FindAllPod`：

```go
// 默认的方法 podApi.Call 通过 API 向外暴露为 /podApi/call，接收 http 请求
// 即：/podApi/call 或 /podApi/ 请求会调用 go.micro.api.podApi 服务的 podApi.Call 方法
func (e *PodApi) Call(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.Call 的请求")
    allPod, err := e.PodService.FindAllPod(ctx, &pod.FindAll{})
    if err != nil {
        common.Error(err)
        return err
    }
    rsp.StatusCode = 200
    b, _ := json.Marshal(allPod)
    rsp.Body = string(b)
    return nil
}
```

`allPod` 经 JSON 序列化后写入 `rsp.Body`，前端即可遍历 `pod_info` 渲染表格。

## 完善删除接口

删除从 URL 的 `pod_id` 参数取值，校验缺失后调用后端删除：

```go
func (e *PodApi) DeletePodById(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.DeletePodById 的请求")
    if _, ok := req.Get["pod_id"]; !ok {
        return errors.New("参数异常")
    }
    podIdString := req.Get["pod_id"].Values[0]
    podId, err := strconv.ParseInt(podIdString, 10, 64)
    if err != nil {
        common.Error(err)
        return err
    }
    response, err := e.PodService.DeletePod(ctx, &pod.PodId{Id: podId})
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

返回值的乱码问题可在前端或响应头统一处理（如设置 `Content-Type: application/json; charset=utf-8`）。

## 前端列表页

`pod-index.html` 用 jQuery 的 `$.ajax` 向网关发 GET 请求，把返回数据动态拼进表格：

```javascript
$.ajax({
    type: "get",
    url: "http://127.0.0.1:8080/podApi/",
    success: function (data) {
        $("#table-data").html("");
        $.each(data['pod_info'], function (i, item) {
            $("#table-data").append(
                '<tr class="gradeA">' +
                '<td>' + item.id + '</td>' +
                '<td>' + item.pod_name + '</td>' +
                '<td>' + item.pod_namespace + '</td>' +
                '<td class="center">' + item.pod_cpu_max + '</td>' +
                '<td class="center">' + item.pod_memory_max + '</td>' +
                '<td class="center">' + item.pod_replicas + '</td>' +
                '<td class="center">' +
                '<a href="pod-detail.html?pod_id=' + item.id + '">详情</a> ' +
                '<a href="http://localhost:8080/podApi/deletePodById?pod_id=' + item.id + '" style="color:red;">删除</a>' +
                '</td>' +
                '</tr>'
            );
        })
    },
    error: function (result) { console.log(result); }
});
```

注意：前端页面中的地址写死为开发环境网关地址（`127.0.0.1:8080`）。若部署到远程，需把删除链接等地址改成实际网关地址，否则会变成空调用。

## 前端详情页

`pod-detail.html` 通过 `getUrlParam('pod_id')` 取 URL 参数，再向 `/podApi/findPodById` 查询并回填只读表单：

```javascript
$.ajax({
    type: "get",
    url: "http://127.0.0.1:8080/podApi/findPodById?pod_id=" + getUrlParam('pod_id'),
    success: function (data) {
        if (data.id != null) {
            $('#pod_id').val(data.id);
            $("#pod_name").val(data.pod_name);
            $('#pod_namespace').val(data.pod_namespace);
            $('#pod_pull_policy').val(data.pod_pull_policy);
            $('#pod_replicas').val(data.pod_replicas);
            $('#pod_restart').val(data.pod_restart);
            $('#pod_team_id').val(data.pod_team_id);
            $('#pod_type').val(data.pod_type);
            $('#pod_image').val(data.pod_image);
        }
    },
    error: function (result) { console.log(result); }
});
```

## 前后端分离

平台前端采用 HTML + jQuery 模板，与后端完全分离：

- 后端只暴露标准 API（JSON）。
- 前端模板负责页面与交互，地址在开发环境指向网关。
- 这种分离让前端可独立迭代，也便于后续用工程工具生成脚手架。

## 衔接

本篇打通了"列表/详情查询"的前端闭环。下一篇补全 `AddPod` 的表单处理（端口、环境变量等特殊类型）与 `form` 插件转换，并演示从页面创建应用到 K8s 落库的完整流程。

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

相关度：94%。是否需要继续：是。代码是否可运行：是。
