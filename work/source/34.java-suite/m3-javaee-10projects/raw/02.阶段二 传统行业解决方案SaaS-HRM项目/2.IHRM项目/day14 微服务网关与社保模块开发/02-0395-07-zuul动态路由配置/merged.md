# 07-zuul动态路由配置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\07-zuul动态路由配置_【海量资源尽在 ubkz.com】.mp4
- 时长 8分12秒（音频 493s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 在刚才呢我们一起简单的看过了ZOO这个网关那其实我们刚才的配置呢还是有一点点不太人性的地方比如说呢在我们这边配置路由的时候这边是一个UL路径已经给它写固定了已经写死了那其实这种方式呢还是不太方便那ZOO呢其实可以借助Erica这种服务发现的组件自动的
[00:29] 帮助我们找到对应的微服务境那接下来呢我们就可以一起来通过这种结合Erica服务发现组件共同完成我们这个做路由的这个配置好了这边呢我们把它称之为好了它的动态路由那要玩这个动态路由需要有这么几个需要各位注意的事项是这样的咱们这边呢有很多微服务
[01:00] 那每一个微服务系统微服务企业微服务员工微服务都需要把这些微服务注册到ERICA上好了我们都知道这边有一个叫做ERICAERICAEUREKA咱们的服务发现这么一个组件我们的注册中心也好或者服务怎么就叫注册中心吧注册中心中心那我们这边呢每一个微服务都需要给它
[01:36] 注册到注册中心上边好了每一个都需要注册过来那你注册过来之后呢这边就会有相应的对应的注册信息比如说呢咱们的解密服务COM就叫IHRM叫做COMPNY那它对应的请求路径127.0.0.1冒号9002随便写了好了当然了可能还有其他的
[02:09] 比如说我们叫做SYSTM那我们叫做900不无所谓了这个叫9001叫哪个其实无所谓那这样一来我们的所有信息就已经注册过来了那注册过来之后网关它也可以通过我们的注册中心得到相应的数据那这样一来你要发送到哪一个微服务其实只需要通过注册中心当中得到
[02:40] 你的服务名称以及对应的请求路径他能够得到得到之后其实就能够动态的选择他的URL地址OK那接着我们来看一下如何去做首先呢咱们要做这种动态的路由啊要做的第一件事就是所有的微服务都需要注册到注册中心哎这是第一个接着第二个第二个是这样的就是我们的网关微服务
[03:10] 网关微服务需要开启我们的注册发现服务发现服务发现功能这个时候就需要用到Erica了那接着第三件事第三件事呢就是修改我们微服务网关的配置网关的配置文件使用服务名称使用服务ID替换我们刚才说的URL能理解吧
[03:42] 一共就这么几个步骤好了我们一起来看一下首先第一个所有微服务都需要注册到注册中心打开我们今天的这个代码好这边呢我全部都关掉好了我们这边打开企业微服务看一下咱们的配置文件好了各位发现我这边的企业微服务其实已经注册到Urica上边了那除了企业微服务之外
[04:12] 我们这边还有我们的员工微服务同样打开配置文件简单的来看一下哎上边呢也已经把它哎注册到我们的语言卡当中当然了这边还有sitem同样的罗技啊也是这边有注册那这样一来呢咱们其实刚才说过的第一件事情就已经搞定了那接着哎咱们来看第二件事情第二件事情呢是这样的我截张图方便我们操作啊
[04:47] 抱歉几张图拷过来OK那我们的第一步呢已经搞定了接下来就是第二步那第二步呢就是我们要在网关为服务当中要开启服务发现的功能就是Erica那我们可以找到我们的Erica找到我们这个Gateway这个工程我们的网关工程在网关工程首先呢咱们需要引入相对坐标好了这个坐标拿过来好了坐标准备好了之后那接下来呢第二件事就是需要在我们的
[05:22] 启动类上可以给它来一个atEnableEnableDiscoveryClient这个其实就是开启我们的服务发现功能OK那咱们把配置配置好了之后还有第三个部分就是有箱的配置文件在配置文件当中咱们需要指定ERICA的咱们的服务地址
[05:58] 这个服务地址呢比较简单通过我们之前的工程copy一段即可Ctrl C拿到这边Ctrl VOK那咱们Erica相应的这个搞定了之后那接下来呢这边还有一个最后一项需要各位一定要注意的咱们之前配置路由的时候这边路由ID随便写hmcom没问题那pass咱们应职的路径也没问题注意这回URL我们不这样写了咱们不用URL了
[06:30] 用什么呢注意这边可以提供一个SEA VICESEA VICE Service ID那这个Service ID这回连的是什么连的是你请求的路径是company开头的你要把它转发到哪一个微服务上面那么的微服务呢就是company微服务我们的文件拿到这个就是它的服务名称OK那这样一来咱们的配置呢其实就已经配置完成了
[07:03] 咱们不需要指定 URL只需要给它指定上我们的服务名称你要调哪个服务它会自动的帮你从我们的注册中心当中拉取到服务的 URL比如说我们请求 Company它会从注册中心当中拉取对应的请求路径接着进行访问OK 我们可以一起重新启动一下再来试一下回到我们这边 GatewayApplication咱们把这个工程的重新启动一下
[07:38] 好了把这个图片呢我也给它关掉好了现在这边呢已经启动成功了回到我们这边Postman再来做一下测试还是127.0.1我们请就在网关路径来send走哎各位发现数据是不是也能够达到啊OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Cloud 项目中配置 Zuul 网关路由规则，并集成 Eureka 服务发现功能，实现微服务间的动态路由。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT页面，讲解Zuul路由规则，代码示例为在application.xml中配置路由规则。
画面2：在IDEA中展示Zuul网关的application.yml配置文件，包含server端口、spring配置、application名称及zuul路由规则。
画面3：展示一个架构图，说明Vue前端通过网关（Zuul, Spring Cloud Gateway）访问后端微服务，微服务注册到Eureka注册中心。
画面4：在IDEA中展示项目结构，选中了“ihrm_gate”模块，同时显示了application.yml文件。
画面5：在IDEA中展示“ihrm_company”服务的application.yml配置，包含Eureka客户端配置、服务端口、数据库连接等。
画面6：在IDEA中展示“ihrm_system”服务的application.yml配置，右键菜单显示了“Split Vertically”等选项。
画面7：在绘图工具中展示架构图，弹出窗口提示“1.所有的微服务都需要注册到注册中心”、“2.网关服务需要开启服务发现功能”、“3.微服务相关的配置文件，使用application.yml”。
画面8：在IDEA中展示项目结构，选中了“ihrm_system”模块。
画面9：在IDEA中展示“GateApplication.java”文件，包含@EnableZuulProxy和@EnableDiscoveryClient注解。
画面10：在IDEA中展示项目结构，选中了“ihrm_gate”模块。
画面11：在IDEA中展示“ihrm_company”服务的application.yml配置，正在编辑server端口。
画面12：在IDEA中展示“ihrm_gate”服务的application.yml配置，正在编辑路由规则，将serviceId改为“ihrm-company”。
画面13：在IDEA中展示“ihrm_gate”服务的运行日志，显示服务启动成功。
画面14：在IDEA中展示“ihrm_gate”服务的运行界面，准备运行服务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
zuul:
  routes:
    ihrm-company: # 这里是路由id，随意写
      path: /company/** # 这里是映射路径
      url: http://127.0.0.1:9001 # 映射到对应的实际url地址

画面2：
server:
  port: 9000
spring:
  application:
    name: ihrm-gate #指定服务名
zuul:
  routes:
    ihrm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际微服务的url路径
      stripPrefix: false #不删除请求的前缀

画面4：
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm-gate #指定服务名
zuul:
  routes:
    ihrm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际微服务的url路径
      stripPrefix: false #不删除请求的前缀

画面5：
#注册到Eureka的服务地址
Eureka:
  client:
    Service-url:
      defaultZone: http://127.0.0.1:8088/Eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm_company #指定服务名
#数据库配置
datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf-8
  username: root
  password: 111111
  hikari:
    maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
#JPA

画面6：
#注册到Eureka的服务地址
Eureka:
  client:
    Service-url:
      defaultZone: http://127.0.0.1:8088/Eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm_system #指定服务名
#数据库配置
datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf-8
  username: root
  password: 111111
  hikari:
    maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
#JPA

画面9：
package com.ihrm.gate;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
@SpringBootApplication
@EnableZuulProxy
@EnableDiscoveryClient
public class GateApplication {
    public static void main(String[] args) {
        SpringApplication.run(GateApplication.class, args);
    }
}

画面12：
#注册到Eureka的服务地址
Eureka:
  client:
    Service-url:
      defaultZone: http://127.0.0.1:8088/Eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm gate #指定服务名
zuul:
  routes:
    ihrm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际微服务的url路径
      stripPrefix: false #不删除请求的前缀

画面13：
2019-08-26 14:20:29.851 INFO 32836 --- [main] com.ihrm.gate.GateApplication: Refreshing Spring Boot context...
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c

