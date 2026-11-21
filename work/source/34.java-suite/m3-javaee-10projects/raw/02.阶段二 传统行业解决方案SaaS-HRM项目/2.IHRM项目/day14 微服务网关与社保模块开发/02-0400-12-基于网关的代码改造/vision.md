# 画面线理解：12-基于网关的代码改造

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\12-基于网关的代码改造_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:36, 01:56, 02:35, 03:25, 03:37, 03:54, 04:28, 04:40, 04:50, 05:13, 05:51, 07:02, 07:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:17:59

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务系统架构，包括网关、服务注册与发现、路由配置、权限控制及前端页面访问。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中的 GateApplication.java 文件，内容为 Spring Boot 启动类，包含 @SpringBootApplication、@EnableZuulProxy、@EnableDiscoveryClient 注解。
画面 2: 展示一个手绘的架构图，核心是“API网关”（zuul, spring cloud gateway），它连接“eureka注册中心”和三个微服务（“考勤服务”、“企业服务”、“员工服务”），并指向“网站前端”（vue）。图中还标注了“/sys/user”、“/company/list”等路由和“鉴权”、“error过滤器”等处理逻辑。
画面 3: 与画面 2 类似，但“员工服务”模块的名称被修改为“员工服务”。
画面 4: 显示 application.yml 配置文件，内容包括 Eureka 客户端配置、服务端口、Redis 配置、Zuul 路由规则（如 /company/** 路由到 ihm-company 服务）。
画面 5: 显示 application.yml 文件中关于 zuul 路由的配置，包括 ihm-company、ihm-system、ihm-employee 三个服务的路径、serviceId、stripPrefix 和 customSensitiveHeaders 等配置。
画面 6: 与画面 5 类似，显示了 ihm-employee 服务的路由配置。
画面 7: 显示 IntelliJ IDEA 中 EmployeeApplication.java 文件，内容为 Spring Boot 启动类，包含 @EntityScan、@EnableEurekaClient、@EnableFeignClients 注解。
画面 8: 显示 IntelliJ IDEA 中 SystemApplication.java 文件，同时弹出一个 IDE Fatal Errors 对话框，提示“Timed out request blocked”。
画面 9: 显示 SystemApplication.java 文件，下方的控制台输出了 Spring Boot 启动日志，包括路由映射信息。
画面 10: 与画面 9 类似，显示了 Spring Boot 启动日志，包括 Servlet、Filter、URLConfiguration 等初始化信息。
画面 11: 显示 SystemApplication.java 文件，下方的控制台显示“Compilation completed successfully with 1 warning in 5s 500ms (moments ago)”。
画面 12: 显示 Visual Studio Code 中的 index.js 文件，内容为前端配置，包括 proxyTable 设置代理到 '/api'，以及 devServer 设置。
画面 13: 显示 IntelliJ IDEA 中的 Result.java 文件，下方的控制台显示“Compilation completed successfully in 1s 941ms (a minute ago)”。
画面 14: 显示浏览器中访问的前端页面，左侧导航栏包含“首页”、“组织架构”、“员工”、“公司设置”、“社保”、“考勤”、“工资”、“员工反馈”等菜单项，当前选中“权限设置”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.ihrm.gate;
import ...
@SpringBootApplication(scanBasePackages="com.ihrm")
@EnableZuulProxy
@EnableDiscoveryClient
public class GateApplication {
    public static void main(String[] args) {
        SpringApplication.run(GateApplication.class);
    }
}
```

画面 4:
```yaml
#注册到eureka的服务元数据
eureka:
  client:
    service-url: http://127.0.0.1:8068/eureka
    defaultZone: http://127.0.0.1:8068/eureka
    instance:
      preferIpAddress: true
      instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm-gate #指定服务名
  redis:
    host: 127.0.0.1
    port: 6379
zuul:
  routes:
    ihm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际服务的url路径
      serviceId: ihm-company
      stripPrefix: false #不删除请求的前缀
      #zuul 自动会创建请求的url路径 http://127.0.0.1:9001/company
      #zuul 自动会删除请求的前缀 http://127.0.0.1:9001/company
```

画面 5:
```yaml
zuul:
  routes:
    ihm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际服务的url路径
      serviceId: ihm-company
      stripPrefix: false #不删除请求的前缀
      #zuul 自动会创建请求的url路径 http://127.0.0.1:9001/company
      #zuul 自动会删除请求的前缀 http://127.0.0.1:9001/company
      sensitiveHeaders: #指定路由的敏感头设置为白名单
        customSensitiveHeaders: true #对指定路由开启自定义敏感头
    ihm-system:
      path: /sys/** #配置请求URL的请求规则
      serviceId: ihm-system #指定Eureka注册中心中的服务id
      stripPrefix: false #将指定路由的敏感头设置为白
      customSensitiveHeaders: true #对指定路由开启自定义敏感头
    ihm-employee:
      path: /employees/** #配置请求URL的请求规则
      serviceId: ihm-employee #指定Eureka注册中心中的服务id
      stripPrefix: false #将指定路由的敏感头设置为白
      customSensitiveHeaders: true #对指定路由开启自定义敏感头
```

画面 12:
```javascript
assetsSubDirectory: 'static',
assetsPublicPath: '',
proxyTable: {
  '/api': {
    target: 'http://localhost:8080',
    changeOrigin: true,
    pathRewrite: {
      '^/api': ''
    }
  }
},
// Various Dev Server settings
host: 'localhost', // can be overwritten by process.env.HOST
port: 8080, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
autoOpenBrowser: false,
notifyErrors: true,
poll: false, // https://webpack.js.org/configuration/dev-server/#watchoptions
// Use ESLint Loader
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图结构：
- “网站前端”（vue）指向“API网关”。
- “API网关”指向“eureka注册中心”。
- “API网关”指向“考勤服务”、“企业服务”、“员工服务”。
- “eureka注册中心”指向“考勤服务”、“企业服务”、“员工服务”。
- “API网关”指向“/sys/user”、“/company/list”等路径。
- “API网关”指向“error过滤器”、“统计请求的时间”、“鉴权”等处理逻辑。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
