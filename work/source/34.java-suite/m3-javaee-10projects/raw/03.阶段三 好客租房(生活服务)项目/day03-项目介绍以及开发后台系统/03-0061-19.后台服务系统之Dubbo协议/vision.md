# 画面线理解：19.后台服务系统之Dubbo协议

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\19.后台服务系统之Dubbo协议【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:31, 05:24, 05:36, 05:43, 05:49, 05:56, 06:03, 06:11, 06:15, 06:28, 06:44, 06:51, 07:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:37:52

1) 这一组画面整体在讲什么（一句话）：
演示 Dubbo 服务提供者配置、服务注册与发现、以及不同协议（如 dubbo://、http://、rest://）的文档查阅过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中查看并编辑 Dubbo 服务提供者的 application.properties 配置文件，其中包含服务端口、版本、扫描包、协议、注册中心等配置。
画面 2: 在 Dubbo OPS 管理平台查看服务提供者列表，显示了 IP、端口和操作按钮。
画面 3: 在 Typora 编辑器中查看文档，内容为“3.2.8. dubbo:// 协议”，包含协议架构图和特性说明。
画面 4: 在 Dubbo 官方文档网站查看“负载均衡策略”页面，包含 RoundRobin、LeastActive、ConsistentHash 三种策略的描述。
画面 5: 在 Dubbo 官方文档网站的左侧导航栏中，鼠标悬停在“hessian//”协议链接上。
画面 6: 在 Dubbo 官方文档网站查看“协议参考手册”页面。
画面 7: 在 Dubbo 官方文档网站查看“rmi://”协议的文档页面。
画面 8: 在 Dubbo 官方文档网站查看“http://”协议的文档页面，包含配置示例。
画面 9: 在 Dubbo 官方文档网站查看“rest://”协议的文档页面。
画面 10: 在 Typora 编辑器中查看“3.2.8. dubbo:// 协议”文档，与画面 3 内容相同。
画面 11: 在图像编辑软件 PicPick 中，对“协议参考手册”导航菜单进行截图。
画面 12: 在 PicPick 中，对“协议参考手册”导航菜单进行截图，其中“dubbo://”项被选中。
画面 13: 在 Typora 编辑器中查看“3.2.8. dubbo:// 协议”文档，与画面 3 内容相同。
画面 14: 在 Typora 编辑器中查看“3.2.8. dubbo:// 协议”文档，与画面 3 内容相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
server.port = 9090
dubbo.service.version = 1.0.0
dubbo.scan.basePackages = cn.itcast.dubbo.service
dubbo.application.name = dubbo-provider-demo
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
dubbo.registry.address = zookeeper://172.16.55.185:2181
dubbo.registry.client = zkclient
```

画面 4:
```
<dubbo:service interface="..." loadbalance="roundrobin" />
```

画面 8:
```
<dubbo:protocol name="http" port="8080" />
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: 架构图标题为“dubbo:// 协议”，结构为：
Client → Header → Body → Server
其中，Client 通过 Header 和 Body 与 Server 通信，中间经过 Codec 和 Serialization。
Transporter 连接 Client 和 Server。
Implement 指向 Server。
Server 指向 Dispatcher。
Dispatcher 指向 Implement。
Threadpool 指向 Implement。

画面 4: 表格数据包含三种负载均衡策略的描述：
- RoundRobin LoadBalance: 描述为“轮询，按公约后的权重设置轮询比例”。
- LeastActive LoadBalance: 描述为“最少活跃调用数，相同活跃数的随机，活跃数调用得到后计数器会越大”。
- ConsistentHash LoadBalance: 描述为“一致性 Hash，相同参数的请求发到同一提供者”。

画面 5: 无表格数据。

画面 6: 无表格数据。

画面 7: 无表格数据。

画面 8: 无表格数据。

画面 9: 无表格数据。

画面 10: 无表格数据。

画面 11: 无表格数据。

画面 12: 无表格数据。

画面 13: 无表格数据。

画面 14: 无表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
