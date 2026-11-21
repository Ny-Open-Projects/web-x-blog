# 22.Nacos-服务发现-Dubbo服务发现-service1微服务

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\22.Nacos-服务发现-Dubbo服务发现-service1微服务【海量资源尽在 666java.com】.mp4
- 时长 9分44秒（音频 585s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现service1微服务根据double服务架构的图我们来看一下刚才我们实现了service2实现了application调用service2然后接下来我们实现service1那service1它也是要对外暴露double协议那么application将来是不是可以调用service1而service1是不是可以调用service2对吧
[00:23] 好那现在呢需求我们清楚了之后呢我们来开发service1为服务它要做的事是不是就是要对外暴露double接口并且还要调用service2啊好那我们来看一下因为它要暴露double接口是吧所以呢它呢采用的工程结构和service2是一致的也是里面有两个子工程一个API一个server好了那现在呢我们来看一下创建一下它的工程叫service1同样的方法啊这里边
[00:54] 我们打开它的这个工程的结构啊然后呢找到这个model那找到model之后呢我们看到上面是不是有一个加号然后点击新建对吧然后下面我们选择复工程还是Nexus Discovery然后呢我们选择这个工程好这个工程搞定了之后呢接下来我们还是根据刚才我们说的我们是不是要建两个子工程一个是API一个是server好新建
[01:23] 然后我们选择复工程是不是就是service1别选错了好然后呢API对吧好这里边它的位置要注意我们选择service1是吧好然后呢接下来我们还要做的事是不是要建它的这个接口实现的工程接口实现的工程是不是就是service1-server好那现在呢同样的道理我们新建model然后呢下一步选择复工程service1
[01:55] 好然后呢接下来选择他的目录service1ok那这个时候就是不是就建好了那建好了之后各位我们来看一下吧service2当初我们的做法怎么做呀我们是不是在这个API当中加接口然后server里面加实现呀同样的道理来我们写一个实现啊写一个接口和一个实现
[02:22] 首先呢我们来看一下这个接口因为比较简单啊所以其实基本上我们就可以打开我们的这个讲义呢然后把这个接口的路径呢能考到我们把它考进去节省时间啊来我们把它复制进去所以这个接口其实这个接口的开发跟我们普通的interface没有啥区别对吧所以这里边呢我们写一个interfaceinterface然后呢接下来在这个interface里头看这个过程不写了啊直接考过去来它是不是就是
[02:53] 叫double service1这个方法呀那在这个接口实现类当中呢同样的道理我们也是跟刚才一样那么写但是啊我们这里边这里边我们就按照正规的流程走了我们可以先不用写这个实现我们先在这个碰当中把1来加进去我们刚才学了嘛你是要调用你是要基于service1的接口所以你要把service1的接口引进来将来你还要调用service2所以啊你要把service2的
[03:23] 这个接口也引进来对不对所以我们就可以把这个依赖呢把它一次性把它加进去另外你要暴露double服务对吧所以呢你是不是还要把double的这个依赖也加进去那double的依赖呢你从原来的这个工程当中拷贝一下包括什么包括它的这个要注册向服务注册中心注册服务它有一个necros的客户端对吧所以你一次性的就把它全加进去这是不是就OK了吧
[03:53] OK了之后呢我们接下来我们是不是就再去写这个实现啊好那这个实现呢其实跟刚才差不多啊我们选择它的一个什么暴露镜暴露镜然后呢在这儿好然后选择它的一个暴露镜之后呢我们现在准备去新建它的一个实现实现统一都是以这个结尾是impl命名对吧好实现Service什么啊1对不对哎刚才说了
[04:26] 我们说要想最终暴露成一个什么double的一个网络接口我们是不是需要用double的这个Service这个注解啊这没问题吧然后呢这里边呢我们让他这个接口实现方法呢返回一个对吧可以吧他返回什么呀注意我们不要一味的去拷贝啊我们要看看什么看我们这个架构service1是不是要调用service2是不是啊所以你要调用service2各位就需要干嘛
[04:55] 就需要用一个注解就是reference这个注解reference这是不是也是double框架给我们提供的注解它呢干嘛对接口生成带来对象对吧这个接口是哪个我们要调用谁那就写谁就是service2那就写service2对吧这时候我们说它是不是要调用service2的接口这一步是不是就是我们说的什么对远程调用service2远程调用service2是不是得到一个结果呀
[05:24] 得到一个结果的话我们说它是不是就可以把这个结果输出啊那其实输出的就比较简单了对这个你可以跟讲义保持一致啊就是double service1就表示double service1被调用了然后呢后边加一个那个service2的一个调用的一个结果OK了吧然后呢到这里呢我们再增加一个什么配置文件增加一个配置文件bootstrap好这个bootstrap这个配置文件呢
[05:56] 跟原来我们配置service2这个配置文件是不是类似是不是大同小异对不对其实你可以直接拷贝它对吧把端口号改了把服务名改了其他基本上都不用改当然还有这个扫描包的路径是不是也要改对吧所以其实这个配置文件我们就可以直接拿过来跟刚才service2差不多那么这里边有几个点就我刚才点的端口服务名还有这个扫描的路径
[06:25] 都是要注意其他都一样当然还有这个double协议的端口这两个端口都是要对赖暴露服务的端口上面是redfoot的端口下面是什么double协议的端口这两个端口我告诉你都是唯一的都不要和其他的服务重复其实你可以看一下service2的端口原来我们设计是20891而现在你这个端口是不是叫20881这几个细节大家要注意OK那下面我们是不是就要写它这个sbermboost的一个启动类就完事了那这个就比较简单了你只要拿过来
[06:55] 拷贝一下啊好改个名叫1这是不是就完工了那到这为止各位我们的Surface 1就做完了吧Surface 1做完之后我们是不是就可以直接启动好那我们看到啊如果启动完Surface 1啊现在我们就需要怎么做啊我们是不是就需要从这个Networks这个服务注册中心当中啊去看一下看有没有你看是不是有了你看Surface 1和Surface 2是不是都成功了当然我们刚才说了这个
[07:26] 从这个service1service2一样它呢都会由这个double框架呢注册到一些其他的服务那这个是有一些原信息获取的服务我们不用管它我们只要关注我们自己定义的这个服务名就可以好那么到这儿呢service2就service1和service2是不是都可以了那接下来我们要实现什么application调用service1根据我们的架构图是不是application不光调用我们的service2也要调用service1所以找到application
[07:56] 然后呢找到他的什么control其实调用方法就比较简单了你要调用谁你是不是要引入谁对吧你现在要调用service1那你就引入service1没错吧那引进来之后呢只要你用一个什么对runfrance注解然后呢我们就可以对这个接口生成代理对象所以这里面的方法其实跟刚才我们调用service2差不多好这就是service1 API
[08:26] 对不对那这样的话我们想调用很简单我们再来一个这就是3行不行这是3这个3这里边它要调用是不是就是service1了调用service1你说要用service1 API这个接口来调用对不对它要调用是不是就拿到一个结果那现在呢我们就可以把consumer把它重启一下这时候我们就可以来看一下调用的结果
[08:51] 那这个调用的结果就比较常了你看看啊首先调用service1service1调用service2是不是啊这一串流程对不对那好我们来看那在这里面我们是不是要访问Service节啊3对不对你看对吧首先调用service1service1再调用service2这个结果是不是都输出到空中单那好到这呢我们是不是就完成了整个的这个double服务架构的开发
[09:20] 所以在整个架务开发当中我们要清楚的知道每个服务它暴露什么样的协议的接口我们的应用层的微服务它都是统一对外暴露RESTful接口供客户端调用我们的微服务层的接口它都是统一对外暴露double协议接口好到这我们的double服务发现的章节就讲完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Dubbo 和 Nacos 构建微服务架构，包括创建服务接口、服务提供者、服务消费者、配置 Nacos 服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前章节为“2.4.1 Dubbo服务架构”，并显示测试成功页面，请求地址为 http://127.0.0.1:56020/service2，显示“consumer dubbo invoke dubboService2 表明service2调用成功”。
画面2：在 IntelliJ IDEA 中，通过“Project Structure”对话框为项目添加新模块，当前选中“service1-server”。
画面3：在 IntelliJ IDEA 中，通过“Project Structure”对话框选择“New Module”并准备创建新模块。
画面4：展示 PPT 页面，标题为“1.1 微服务架构”，内容说明微服务架构将系统拆分为多个独立服务，并展示一个电商系统的架构图（App/Web -> Web App 1, Web App 2, Web App 3）。
画面5：展示 PPT 页面，标题为“2.4.5.2 定义service1-server”，显示 service1-server 的 Maven 项目结构和接口定义。
画面6：在 IntelliJ IDEA 中，展示 service1-server 的 pom.xml 文件，其中包含对 service1-api 和 service2-api 的依赖。
画面7：在 IntelliJ IDEA 中，展示 service1-server 的 pom.xml 文件，其中包含对 spring-cloud-starter-dubbo 和 spring-cloud-starter-alibaba-Nacos-discovery 的依赖。
画面8：在 IntelliJ IDEA 中，展示 service1-server 的 ServiceImpl.java 文件，其中实现 ServiceApi 接口并返回 null。
画面9：在 IntelliJ IDEA 中，展示 service1-server 的目录结构，其中包含 bootstrap.yml 文件。
画面10：在 IntelliJ IDEA 中，展示 service1-server 的 bootstrap.yml 文件，其中配置了 dubbo 的 registry 为 Nacos，地址为 Nacos://127.0.0.1:8848。
画面11：在 IntelliJ IDEA 中，展示 service1-server 的 ServiceBootstrap.java 文件，其中使用 SpringApplication.run 启动服务。
画面12：在 IntelliJ IDEA 中，展示 service1-consumer 的目录结构，其中包含 ServiceBootstrap.java 文件。
画面13：在 IntelliJ IDEA 中，展示 service1-consumer 的 RestConsumerController.java 文件，其中调用 service2Api.dubboService2()。
画面14：展示 PPT 页面，标题为“2.4.1 Dubbo服务架构”，显示 Dubbo 协议的系统架构图，包括客户端、API 网关、Application-1、Nacos Server、Service-1、Service-2 等组件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
测试：
请求：http://127.0.0.1:56020/service2
显示：consumer dubbo invoke dubboService2 表明service2调用成功。

画面4：
1.1 微服务架构
为适应企业的业务发展，提高软件研发的生产力，降低软件研发的成本，软件架构也升级和优化，将一个独立的系统拆分成若干小的服务，每个服务运行在不同的进程中，服务与服务之间采用RESTful、RPC等协议传输数据，每个服务所拥有的功能具有独立性强的特点，这样的设计就实现了单个服务的高内聚，服务与服务之间的低耦合效果，这些小服务就是微服务，基于这种设计方法的系统架构即微服务架构。
下图是基于服务架构的电商系统：
App/Web
  ↓
Web App 1
  ↓
Web App 2
  ↓
Web App 3

画面5：
<parent>
    <artifactId>nasco dubbo Service</artifactId>
    <groupId>com.ithema.Nacos</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>
<modelVersion>4.0.0</modelVersion>
<artifactId>service1-api</artifactId>

3、定义接口
package com.ithema.microservice.service1.api;
public interface ServiceApi {
    public String dubboService();
}

画面6：
<modelVersion>4.0.0</modelVersion>
<artifactId>service1-server</artifactId>
<dependencies>
    <dependency>
        <groupId>com.ithema.Nacos</groupId>
        <artifactId>service1-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.ithema.Nacos</groupId>
        <artifactId>service2-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>

画面7：
<dependencies>
    <dependency>
        <groupId>com.ithema.Nacos</groupId>
        <artifactId>service1-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.ithema.Nacos</groupId>
        <artifactId>service2-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-dubbo</artifactId>
    </dependency>
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
    </dependency>
</dependencies>

画面8：
package com.ithema.microservice.service1.Service;
import com.ithema.microservice.service1.api.ServiceApi;
@Service
public class ServiceImpl implements ServiceApi {
    public String dubboService() {
        return null;
    }
}

画面9：
resources
  api
    ServiceApi.java
  service1-server
    pom.xml
    service1-server.iml
  src
    main
      java
        com.ithema
          microservice
            service1
              Service
                ServiceApiImpl.java

画面10：
main:
allow-bean-definition-overriding: true # Spring Boot 2.1 需要开启
cloud:
  Nacos:
    server-addr: 127.0.0.1:8848
dubbo:
  scan:
    base-packages: com.ithema.microservice.service1.Service
  protocol:
    name: dubbo
    port: 2000
  registry:
    address: Nacos://127.0.0.1:8848
    application:
      name: dubbo
      qos-enable: false # Dubbo远程服务也开启
    consumer:
      # 其他配置

画面11：
package com.ithema.microservice.service1;
import ...
@SpringBootApplication
public class ServiceBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(ServiceBootstrap.class, args);
    }
}

画面12：
resources
  bootstrap.yml

画面13：
@GetMapping(value = "/service2")
public String service2(){
    String providerResult = serviceApi.dubboService2();
    return "consumer dubbo invoke " + providerResult;
}

画面14：
2.4.1 Dubbo服务架构
下图是做服务采用Dubbo协议的系统架构图：
客户端
  ↓ HTTP
API网关
  ↓ RESTful
Application-1
  ↓ dubbo
Service-1
  ↓ dubbo
Service-2
组件说明：

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：1.1 微服务架构
内容：
- 说明微服务架构将系统拆分为多个独立服务。
- 展示电商系统的架构图：
  - App/Web 指向 Web App 1、Web App 2、Web App 3。
  - Web App 1、Web App 2、Web App 3 之间通过 REST API 互相连接。

画面14：
标题：2.4.1 Dubbo服务架构
内容：
- 展示 Dubbo 协议的系统架构图：
  - 客户端通过 HTTP 指向 API 网关。
  - API 网关通过 RESTful 指向 Application-1。
  - Application-1 通过 dubbo 指向 Service-1。
  - Service-1 通过 dubbo 指向 Service-2。
  - Service-1 和 Service-2 都指向 Nacos Server（服务发现中心）。
- 组件说明：无具体说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

