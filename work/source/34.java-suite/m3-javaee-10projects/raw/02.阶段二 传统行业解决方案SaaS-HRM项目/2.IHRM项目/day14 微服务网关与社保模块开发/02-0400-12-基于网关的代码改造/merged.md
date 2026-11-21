# 12-基于网关的代码改造

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\12-基于网关的代码改造_【海量资源尽在 ubkz.com】.mp4
- 时长 7分38秒（音频 458s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了那到目前为止呢咱们其实已经把做网关所涉及到的大部分内容的全部都跟各位做做了一个介绍那接下来呢还有一个小小的问题需要和各位做一个简单的说明是这样的一张图随便来看那在咱们的做网关当中呢不管是在什么位置特别是做全新教验的时候咱们的网站前端是不是会想做网关这边请求
[00:30] 的投信息当中携带一个参数那这个参数呢我们叫做also renaissance哎各位应该还有印象吧OK我们这边有一个投信息投信息那这个投信息呢我们叫做also renaissancea o t h o r i z a t o nOK那接下来呢这些呢投信息呢其实是一些比较敏感的一些敏感投也就是说这玩意啊
[01:02] 你可以理解为是一些关键字是在投信息当中的一些关键字那这些关键字呢一旦请求到网关那网关就不会默认他不会把这些投信息继续发送到各个微服务了也就是说啊你这个投信息已经传到API网关网关能获益到但是在其系统微服务企业微服务员工微服务能获益到吗不能为什么是因为在shareware当中它有内部的这么一种机制
[01:32] 抱歉是在租网关当中它有这么一种内部的机制会自动的把这些敏感投信息给我清空掉也就是说这些敏感投网关获取到了之后就不会再往下传递了那么为了解决这个问题那应该怎么办呢很简单就是这么一段小小的配置好了我们一起来看一下回到我们的代码当中找到这个网关
[02:00] 那接着找到我们对应的配置那在配置当中底下我们可以加一段就是处理敏感投信息OK这个处理敏感投信息呢其实就是两句话好了我从今天资料当中的这个案例当中给各位直接就拿过来了很简单Ctrl CCtrl V放到这边放到这边就可以了好那到目前为止呢我们整
[02:37] 各的这个做网关相关的内容呢其实就跟各位都聊完了那在这边呢我们的案例当中呢现在呢只是处理了企业微服务没错吧那除了这个企业微服务那可能我们的系统当中还有比如说呢这边员工的微服务比如说呢这边还有我们的系统微服务那这些内容我们同样的也需要把它交给网关来进行处理那怎么办呢其实跟这边的企业微服务配置
[03:07] 是基本上差不多的好了我这边呢已经在今天资料当中给各位准备好了比如说有系统为服务比如说有咱们的员工为服务里面的配置跟我们的企业是一模一样的好了我们只需要把这一段话Ctrl C直接靠到我们这边的配置上就可以了注意啊靠过来之后要对齐好了咱们这样一来就已经把这些都准备好了那这样一来
[03:36] 这样一来我们的微服务部分呢咱们就已经搞定了那我们可以把这个相关的这几块微服务全部给它启动起来好了ERICA没问题Company没问题这边呢咱们再去启动我们的员工微服务来执行问方法走好了员工微服务呢这边让它慢慢重启接下来呢还有一个就是我们的系统微服务System那找到系统微服务好像这边启动的内容实在是有点
[04:13] 读啊ok 找到里面的启动类application来走没错不用管他好了没什么问题还有系统微服务好了同样也在启动启动有点慢各位耐心等待一下ok 这样一来我们这几个微服务呢全部就已经启动成功了UICAR代表是注册中心Database代表是网关那我们这边company
[05:07] 我们的员工还有我们的系统微服务都已经启动起来了那这些启动起来之后微服务所有相关的咱们就已经准备好了那别忘了我们的系统除了服务端之外是不是还有一个就是代表的是我们的没错代表的是我们的前端也就是页面那这个前端页面这些内容呢我已经给它打开了就在这边是我们的这个工程那我们这个工程呢之前呢咱们的配置方式需要跟各位简单的来提一下
[05:37] 之前我们配置全部都是在这个config里面有一个叫做index.js我们之前的配置是不是每一个都用一个target来进配置那这回有了我们的网关之后呢这些就全都不要了全都删掉只保留一个我们这回把所有的请求是不是都发送到localhost9090代表的是我们的网关路径啊
[06:02] 那这样一来我们就已经满足了你请求过来把数据发送到网关那网关再去把数据发送到对应的微服务当中完成我们的业务处理OK那这些我们都搞定了之后好了这边我已经改好了那接着重新启动一下我们的前端页面来走好了这个前端页面启动稍微有一点点的慢我这边先暂停一下
[06:37] 好了这边呢我已经启动成功了按住control鼠标左键那打开浪器我们可以一起访问一下来看一下好了首先呢这边呢我们请求的网站首页已经有了那接下来呢我点击登录咱们来看一下能不能够完成用户登录的相当的这个业务逻辑处理那注意我把这边的控台全部都打开一起来看一下登录呢肯定是我们的system application来走各位发现能够请求过来
[07:09] 好了那并且呢我左侧可以随便点点比如说呢我们的组织架构哎没问题员工哎没什么问题全线设置哎是不是都没问题啊OK好了那这样一来呢咱们就已经完成了哎对于住哎在我们系统当中的改造在我们系统当中主要承担网关以及做全线校验相应的这些内容OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务系统架构，包括网关、服务注册与发现、路由配置、权限控制及前端页面访问。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中的 GateApplication.java 文件，内容为 Spring Boot 启动类，包含 @SpringBootApplication、@EnableZuulProxy、@EnableDiscoveryClient 注解。
画面 2: 展示一个手绘的架构图，核心是“API网关”（zuul, spring cloud gateway），它连接“Eureka注册中心”和三个微服务（“考勤服务”、“企业服务”、“员工服务”），并指向“网站前端”（Vue）。图中还标注了“/sys/user”、“/company/list”等路由和“鉴权”、“error过滤器”等处理逻辑。
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
#注册到Eureka的服务元数据
Eureka:
  client:
    Service-url: http://127.0.0.1:8068/Eureka
    defaultZone: http://127.0.0.1:8068/Eureka
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
- “网站前端”（Vue）指向“API网关”。
- “API网关”指向“Eureka注册中心”。
- “API网关”指向“考勤服务”、“企业服务”、“员工服务”。
- “Eureka注册中心”指向“考勤服务”、“企业服务”、“员工服务”。
- “API网关”指向“/sys/user”、“/company/list”等路径。
- “API网关”指向“error过滤器”、“统计请求的时间”、“鉴权”等处理逻辑。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

