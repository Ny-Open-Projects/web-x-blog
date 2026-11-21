# 画面线理解：day01-14-玩转Apollo

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-14-玩转Apollo_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 02:35, 03:46, 05:57, 06:41, 07:20, 08:35, 09:06, 10:52, 11:32, 12:31, 13:56, 14:26, 15:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:08:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Apollo 配置中心创建自定义命名空间（namespace）并配置 Eureka 服务地址，以实现服务的动态配置管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PDF 文档，章节为“3.5 玩转Apollo”，子章节“3.5.1 基础设置”，内容提到 Apollo 默认有两个样例部门，可通过系统参数修改。
画面 2: 在 Apollo Portal 的“应用配置”页面，输入 key 为 "organizations"，value 为 JSON 数组，包含三个样例部门信息，准备保存。
画面 3: 浏览器地址栏显示 "localhost:8070"，页面为空白，表示访问了 Apollo 的基础服务端口。
画面 4: 在 IntelliJ IDEA 中打开项目 "wanning2p-consumer-service" 的 application.properties 文件，其中包含 Eureka 和 Ribbon 的配置，如 eureka.client.serviceUrl.defaultZone 和 ribbon.ReadTimeout 等。
画面 5: 浏览器地址栏显示 "localhost:8070"，页面为空白，表示访问了 Apollo 的基础服务端口。
画面 6: 浏览器地址栏显示 "localhost:8070"，页面为空白，表示访问了 Apollo 的基础服务端口。
画面 7: 在 Apollo Portal 的“application”命名空间下，点击“DEV”环境下的“beijing”集群，准备进入该集群的配置页面。
画面 8: 在 Apollo Portal 的“新建 Namespace”页面，选择“DEV”环境下的“default”和“beijing”集群，准备创建新的命名空间。
画面 9: 在 Apollo Portal 的“application”命名空间下，切换到“TEST3.eureka”命名空间，页面显示该命名空间下的配置项。
画面 10: 在 Apollo Portal 的“TEST3.eureka”命名空间下，显示配置项 "eureka.client.serviceUrl.defaultZone" 的值为 "http://localhost:53000/eureka/"。
画面 11: 在 Apollo Portal 的“新建 Namespace”页面，选择“public”或“private”权限，准备创建新的命名空间。
画面 12: 浏览器地址栏显示 "localhost:8070"，页面为空白，表示访问了 Apollo 的基础服务端口。
画面 13: 浏览器地址栏显示 "localhost:8070"，页面为空白，表示访问了 Apollo 的基础服务端口。
画面 14: 在 Apollo Portal 的“TEST3.eureka”命名空间下，显示配置项 "eureka.client.serviceUrl.defaultZone" 的值为 "http://localhost:53000/eureka/asdasdas"，并显示最后修改人为 "zhanhong"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 中的 application.properties 内容：
```
spring.http.encoding.charset=UTF-8
spring.http.encoding.force=true
spring.http.encoding.enabled=true

# springCloud eureka配置
eureka.client.serviceUrl.defaultZone=http://localhost:53000/eureka/
#注册地址，不使用ip地址，使用应用名
eureka.instance.preferIpAddress=true
eureka.instance.instance-id=${spring.cloud.client.ip-address}:${spring.application.name}

# springCloud ribbon配置
#默认超时时间，当Eureka中可以找到服务，但是服务连不上时会重试
ribbon.MaxAutoRetries=2
#请求连接超时时间
ribbon.ConnectTimeout=300
#请求读取超时时间
ribbon.ReadTimeout=20000
#请求失败后的重试次数
ribbon.MaxAutoRetriesNextServer=2
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
