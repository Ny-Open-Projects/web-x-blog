# 05-搭建zuul运行环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\05-搭建zuul运行环境_【海量资源尽在 ubkz.com】.mp4
- 时长 10分27秒（音频 627s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了接下来我们就开始着手去创建工程完成Zoo网关的搭建好了回到我们的idea当中回到在idea当中我们先去创建一个我们的网关工程找到复工程在上面右键new一个model这个模块的名称其实叫什么都无所谓了我习惯的就是跟我们的命名规则一致HIM夏娃县我起一个名字就叫做Git网关
[00:31] OK点击next点击finish好了那现在呢我们已经把工程创建出来我们接下来需要引入箱的坐标那对于这个坐标依赖呢不需要各位重点去记忆在今天呢给各位准备的配套课程资料当中其中有一块就是网关箱的资料那在里面呢我们有一个pom.sml就是我准备好的箱的依赖好了
[01:02] 我把这个依赖打开让各位来看一下打开OK那我们要做的事情呢其实就是把这一段依赖呢相关的Ctrl C拿到我们的idea当中回到这边Ctrl VOK那对于这个依赖呢我简单的介绍一下其中呢第一个就是Erica Client好了接下来呢这边还有一个Netflix其实这玩意儿是我们最最核心的就是我们的租网关好那上边这个就是我们的Erica客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客客
[01:37] 好了这个目前来说呢我们还用不到啊因为我们一会儿呢配置动态路的时候哎通过这个语录卡让它动态查找我们到时候用到的时候再说我们现在其实只用一个住网关哎就可以了OK那这样一来呢我们的依赖已经倒进来了那接下来呢我们刚才说过除了创建工程我们还需要去配置一个启动类那配置这个启动类呢其实很简单了好了在合适的位置啊创建一个包
[02:09] cn.itcast.him比如说我就放到这个包下吧点起一个名字呢就叫做起一个名字叫做gate gate gateappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappappapp
[02:49] 就是第二步需要去创建一个启动类那创建这个启动类呢也很简单了来创建一个class把它放到com.ihm.我们起一个包名呢就叫git就叫git吧好了jate那我们这个工程呢这个这个类名git就叫git applicationappricatlongit application
[03:16] OK那对于启动类里面的这个方法呢其实很简单了就来一个闷方法psvm创建一个闷方法里面我们就可以通过SprintSprintApplication.runOK好了里面写好我们的类名.class那接下来呢上边呢可以给它进行相应的配置比如说呢我们首先呢就是声明是一个boot工程boot工程好了来个
[03:48] at sprint boot application好那接下来还有一个最最重要的注解这个注解呢就是开启做网关哎功能那这个注解呢at enable诶zooprocess那这样一来呢其实它就已经开启了我们做网关相应的这个功能可以这样说啊就是我们
[04:16] 这个类当中最最最重要的数据就是这个Enable to Pulse好了现在呢我们第二步呢也已经完成了那接下来呢还有第三步第三步呢就是准备一个对应的配置文件那这个配置文件呢可能比较内容比较多我从咱们之前写好的Ctrl C到这边Ctrl V Copy一份到这边Ctrl V Copy一份那接下来呢做一个简单的修改
[04:48] 这边的什么注册到ERICA服务的这个我们不要了好了留对应服务的端口好了这些呢目前来说没什么用OK那端口呢我们起一个名字就叫9090那接下来呢我们这个服务名称呢就叫做Git就叫做IHM Git好了那还有最后的第三个部分那第三个部分呢是我们做网关最最最最核心的配置了
[05:19] 来去配置我们的路由规则那这个路由规则呢咱们先玩一个最最简单的最简单的就是说我现在准备通过咱们这个请求的网关给他转发到我们的企业微服务当中那注意啊我们的需求是这样的网站前端发送请求到网关那接下来网关呢去发送到我们的具体的某一个微服务下边这是我们的
[05:50] 需求那这边呢就需要在我们的微服务工程里面的application.yml当中进行配置那配置的就叫做路由规则这个是路由转发规则那这个路由转发规则我们应该怎么配置呢很简单注冒号那路由配置呢叫做road哎roads那这个roads里面接下来呢要配置啥呢很简单就说啊
[06:19] 我们要配置的时候这边呢需要配置一下我们的就是路由ID咱们可以随便写好了当然了我这个路由ID呢虽然说过随便写了我还是配置的有一点点技术含量吧我起一个名字叫做IHRM好了我们说过要请求的是企业微服务那请求企业微服务我们这个企业微服务在这边打开
[06:47] 我抄一下他这个企业微服务的服务名称好了我把这个玩意理解为我们的IDOK好那这个ID呢咱们写过来之后那接下来你想要去发送到企业微服务那接下来呢这边有一个叫做URL的page就是说你这个企业微服务究竟他的路径在什么位置那我们都知道我们请求的路径就是httphttp
[07:17] 刚刚127.0.0.1我们叫做90090刚才看过了是9001没错9001那接下来呢你要根据什么样的规则去请求到企业为福啊因为你上边请求的这个路径特别多啊比如说有SYS开头的有Company开头的还有我们叫Eploy开头的那我们都知道是不是这个Company开头的这个路径
[07:46] 是不是应该划分为企业微服务啊所以这边呢我们需要进行一个配置就是配置它映射的路径地址好了passp a t h pass好了我们映射的路径地址i h r m c m p a n y c m p n y 杠星星好了那这个配置的就是我们的哎需要需要映射的路径
[08:23] 地址其实说的直白一点那如果你的请求路径哎回到这张图如果说前端请求路径是以company开头的那他会把类似的这个请求给我们转发到这个企业微服务当了转发到企业微服务其实转发的是这个地址下边所以这个地址代表的就是映射路径对应的实际微服务的UIL
[08:56] OK 好了那这样一来呢我们一个简单的做网关配置和环境搭建咱们就已经搞定了好了这个我们搞定了之后接下来呢可以把这个工程呢咱们启动起来看一看它究竟报不报错回到我们这边Git找到咱们的启动类好了在上面执行门房吧来走OK各位稍微耐心等待一下这个启动稍微有一点点慢哈OK
[09:35] 好了,希望各位注意一下,就是现在这边启动了报了一个错误那针对这个错误是什么原因造成的呢?
[09:42] 是这样的,就是由于我这边配置了Erica相应的依赖我先把这个依赖去掉,刚才我们大家工程的时候说过我们第一个工程其实这个Erica没有什么特别大的作用我们一会儿加上再说OK,好了,我现在把这Erica配置我们给它注掉了咱们再重新启动一下来看一下效果
[10:09] 这边还是稍微启动的有点慢因为这边打开的东西实在是太多了OK来看一下这回应该能够正常启动成功了OK现在已经启动了没什么问题

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
创建并配置一个基于 Spring Cloud 的 Zuul 网关服务（ihrm_gate），包括工程搭建、启动类编写和配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在课程 PPT 中展示“1.3.1 工程搭建”章节，内容为创建工程 ihrm_gate 并导入 zuul 依赖，显示了 Maven 依赖配置片段：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-zuul</artifactId>
</dependency>
```

画面2：在文件资源管理器中，显示了项目目录结构，包含 `ihrm_gate` 文件夹，内含 `application.yml` 和 `pom.xml` 文件。

画面3：在 IntelliJ IDEA 中打开 `pom.xml` 文件，显示了工程的依赖配置，包括 Spring Cloud Zuul、Spring Boot Actuator、MySQL Connector、以及自定义模块 ihrm_common 的依赖。

画面4：在 IntelliJ IDEA 中右键点击项目 `ihrm_gate`，弹出菜单，选中“Replace in Path...”选项，准备进行路径替换操作。

画面5：在 IntelliJ IDEA 中打开 `GateApplication.java`，显示了空的 `main` 方法，光标位于 `public static void main(String[] args) {` 行。

画面6：在 IntelliJ IDEA 中编辑 `GateApplication.java`，添加了 Spring Boot 启动注解 `@SpringBootApplication`。

画面7：在 IntelliJ IDEA 中编辑 `GateApplication.java`，添加了 Zuul 网关注解 `@EnableZuulProxy`。

画面8：在 IntelliJ IDEA 中打开 `application.yml` 文件，显示了服务配置和 Spring 配置的注释，光标位于第 10 行。

画面9：在 IntelliJ IDEA 中编辑 `application.yml`，在第 10 行添加了 `zuul:` 配置项。

画面10：在 IntelliJ IDEA 中编辑 `application.yml`，在 `zuul:` 下添加了 `routes:` 配置，定义了 `ihrm-company` 的路由规则。

画面11：在 IntelliJ IDEA 中编辑 `application.yml`，在 `ihrm-company` 的路由规则中，将 `url` 设置为 `http://127.0.0.1:9001`。

画面12：在 IntelliJ IDEA 中，光标位于 `GateApplication.java` 的 `main` 方法中，准备编写启动代码。

画面13：在 IntelliJ IDEA 中打开 `pom.xml` 文件，显示了父工程 `ihrm_parent` 的配置，以及 `ihrm_gate` 模块的依赖，包括 `spring-cloud-starter-netflix-Eureka-client`。

画面14：在 IntelliJ IDEA 的终端中，显示了 `GateApplication` 启动后的日志，包括 Zuul 初始化器启动、端点暴露等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-zuul</artifactId>
</dependency>
```

画面3：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-zuul</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
    <groupId>com.ihrm</groupId>
    <artifactId>ihrm_common</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

画面6：
```java
import org.springframework.boot.autoconfigure.SpringBootApplication;
```

画面7：
```java
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
```

画面8：
```yaml
#服务配置
server:
  port: 9000
#spring配置
spring:
  application:
    name: ihrm-gate #指定服务名
```

画面9：
```yaml
zuul:
```

画面10：
```yaml
zuul:
  routes:
    ihrm-company:
```

画面11：
```yaml
zuul:
  routes:
    ihrm-company:
      url: http://127.0.0.1:9001
```

画面13：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“1.3 快速入门”，子标题“1.3.1 工程搭建”。

画面8：PPT 展示了三个图表，分别是“无标题 - 建图”、“无标题 - 图表”、“无标题 - 表格”，但未显示具体内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

