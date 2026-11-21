# 16-Spring Cloud 体系技术综合应用说明

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\16-Spring Cloud 体系技术综合应用说明_【海量资源尽在 ubkz.com】.mp4
- 时长 2分49秒（音频 170s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] Spring Cloud体系技术综合应用说明在这一小节中我们的主要目标是了解Spring Cloud中的Eureka GatewayConfigBusFame等技术的综合应用现在打开讲义通过一幅图来了解这些技术的综合应用那在这幅图中我们把这两天学习的Spring Cloud的技术组件都综合的应用了起来首先我们会开发相应的微服务如用户服务订单服务
[00:32] 又对这些服务能可以做集群部署那这些服务都会注册到Urica注册中心服务之间如果有需要调用的话那么可以通过我们的Faim来进行调用比如用户服务要调用订单服务的时候就可以通过Faim进行一个调用好然后我们的各个微服务呢需要使用到配置文件那这些配置文件呢可以通过配置中心也就是我们的Spring Cloud Config从
[01:01] git 仓库中获取对应的配准键去使用那如果呢这些配准键有更新的话那如果有一个用户去更新一个配置在git 仓库中去对应修改这些配准键改了以后呢再去刷新用 post 请求方式去刷新配置中心的一个地址buzz gun refresh刷新后会发一个消息到rebi mq发了以后也就是用我们的 spring cloud buzz然后呢这个
[01:30] MQ中有对应的消息以后我们的这些微服会去从MQ的队列中监听到消息再去更新它对应的配置项也就是可以及时去更新到修改的配置项好那如果一般的请求一般的请求的话比如有PC端移动端那这些请求会先到我们所有微服的统一入口也就是我们的网关Gateway在Gateway中我们可以做一些全线鉴定
[02:00] 异常日志记录等这些那再去将我们的请求呢路由到不同的微服务在路由的时候如果有集群那么会用我们的ribbon进行一个负载均衡它会根据我们的服务名到我们的Urica中获取服务地址列表再基于负载均衡算法从中选择到一个地址去调用当服务出现异常的时候呢也可以通过我们的highstreet进行一个服务降级好这就是我们的
[02:30] Spring Cloud体系技术中的一个综合应用就是这一些我们现在回到笔记中把这一幅图给记录起来那如果要综合应用的话可以这么应用好这就是我们Spring Cloud体系综合应用的一个说明

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Cloud 体系中各核心组件（Eureka、Gateway、Config、Bus、Feign）的协同工作流程与代码实现。

2) 按时间顺序列出每张画面的要点：
画面1: 显示了 Spring Cloud 项目中 `application.yml` 配置文件的片段，用于配置 RabbitMQ 连接信息。
画面2: 展示了 Spring Cloud 微服务架构图，包含 PC端/移动端、网关 Gateway、用户服务、订单服务、配置中心 Spring Cloud Config、Git 仓库、注册中心 Eureka Server 和 Spring Cloud Bus/MQ。
画面3: 与画面2相同，鼠标在“订单服务”模块上。
画面4: 与画面2相同，鼠标在“Feign”调用线上。
画面5: 与画面2相同，鼠标在“Git 仓库”模块上。
画面6: 与画面2相同，鼠标在“注册中心 Eureka Server”模块上。
画面7: 与画面2相同，鼠标在“网关 Gateway”模块上。
画面8: 与画面2相同，鼠标在“注册中心 Eureka Server”模块上。
画面9: 与画面2相同，鼠标在“配置中心 Spring Cloud Config”模块上。
画面10: 显示了编辑器界面，内容为 Spring Cloud 项目中 `UserController` 的代码片段。
画面11: 与画面10相同，光标在编辑器中。
画面12: 与画面10相同，光标在编辑器中，显示了图片插入的上下文菜单。
画面13: 与画面10相同，光标在编辑器中，显示了图片插入的上下文菜单。
画面14: 与画面10相同，光标在编辑器中，显示了图片插入的上下文菜单。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1:
```yaml
# 配置RabbitMQ信息：如果是跟与默认值一致则不需要配置
RabbitMQ:
  host: localhost
  port: 5672
  username: guest
  password: guest
```

画面10:
```java
@RestController
@RequestMapping("/user")
@RefreshScope // 动态刷新
public class UserController {
    @Autowired
    private UserService userService;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2:
标题: 无明确标题，但内容为“Spring Cloud 体系技术综合应用说明”。
架构图结构:
- PC端 和 移动端 → 请求 → 网关 Gateway
- 网关 Gateway → 路由 → 用户服务 (两个实例)
- 网关 Gateway → 路由 → 订单服务 (两个实例)
- 用户服务 → Feign → 订单服务
- 订单服务 → 获取 → 配置中心 Spring Cloud Config
- 配置中心 Spring Cloud Config → 获取 → Git 仓库
- Git 仓库 → post刷新 → 人形图标 (表示用户)
- 配置中心 Spring Cloud Config → 发送消息 → Spring Cloud Bus : MQ
- 用户服务、订单服务、网关 Gateway、配置中心 Spring Cloud Config → 注册 → 注册中心 Eureka Server

5) 无其他内容。

