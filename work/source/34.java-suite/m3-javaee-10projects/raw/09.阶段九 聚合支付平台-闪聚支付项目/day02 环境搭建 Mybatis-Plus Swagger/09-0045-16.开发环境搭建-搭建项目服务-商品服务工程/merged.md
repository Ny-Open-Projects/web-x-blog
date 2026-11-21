# 16.开发环境搭建-搭建项目服务-商品服务工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\16.开发环境搭建-搭建项目服务-商品服务工程【海量资源尽在 666java.com】.mp4
- 时长 10分54秒（音频 655s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来搭建闪区支付商户服务工程那么根据刚才我们的解释商户服务工程对外暴露double服务对吧给商户平台应用去调用商户服务工程呢包括两个子工程一个是API一个是API的实现工程好那下面我们分别来进行搭建首先我们是需要创建一个商户服务工程这个它的一个什么它的副工程好来
[00:30] 打开跟刚才我们创建商户平台应用工程的方法一样找到它的这个添加model的位置然后呢下一步那这个副工程仍然还是选择散局配然后呢这里面这是商户服务对吧商户服务然后往下这个工程是不是就完成好那这个工程完成了之后接下来还要做什么呀你要创建两个工程吧一个是商户的一个什么
[01:00] API一个是API的实现注意啊你从讲义上要找什么找坐标啊找坐标不要自己瞎写要找坐标你要这个坐标写错了后边的这个代码可能就依赖有问题了跟我们讲义就是根据我们项目所规定的这个坐标啊去定义你的这个每个工程好那现在呢继续吧添加这个副工程要选哪个各位是不是要选择三户
[01:31] 服务这个副工程了好然后接下来这个目录各位是不是也要选择商户服务完成同样我们说API嘛还有一个什么API的实现所以这里边呢我们再来看一下啊新建新建然后呢接下这副工程是不是还是商户服务啊然后呢这里我们选择目录选哪个商户服务好再走
[02:12] 各位这个工程我们是不是就创建好了对吧好那这个工程我们创建好了之后好像有问题不太对了你看是不是这个这一点是不是有问题了你看见吗那么有问题的咋弄有问题的这么弄看我教你还进到刚才这个位置对你把有问题的首先从这个models这个列表当中给它干掉
[02:48] 对这有问题了是吧那有问题了行我们把它干掉那它有问题了那你怎么弄啊整个删掉是吧好注意你这时候呢你最好进到它的磁盘对应的这个目录里头来瞧瞧哎里边是不是创建了一个API了吗还是还差一个还差一个来刚才应该是哪里我们选择的是有问题所以大家不要对出现了问题不知道
[03:19] 在哪里走怎么做啊来我们还是进到这个界面然后呢还是要新添一个 mode 是吧然后接下来这个要选择哪个肯定是选择他吧哎我记得刚才好像就是这么做的吧然后这里选择他吧这吧这样行吧哎走完成这是不是就可以了大家可以看到啊现在看我们的这个工程结构这是我们的这个最
[03:52] 对这个根的这个根工程了那里面是不是就是什么呀我们最初的这个导入的基础工程的一个什么POM对吧然后这是我们的通用工程那里面是不是有一些什么工具类呀或者说这个DOMIN对象啊这些类型啊等等这个是啥这是不是我们刚才创建的商户服务工程下面商户应用其实刚才我们创建的是不是就是这俩工程啊好那么再回来
[04:20] 商户服务工程一个是API一个是API的这个什么接口实现类那刚才我们把API工程创建好了之后我们是不是需要把API工程的这个什么泡沫依赖给它完善了基本上所有工程它都会去依赖什么这个common所以这里边呢你看API我就让它依赖这个common了那
[04:50] Service呢我们打开Service它就稍微有些复杂你要注意Service是不是接口实现类在这里头将来是不是会暴露Double协议的接口啊所以这里边你看好啊它首先要把自己注册到配置中心然后呢还有服务发现中心还有Double的依赖还有我们这个Spring MVC的包对吧等等啊这些包括它要连数据库这里边是不是也要把GDPC的包包括Meptis Plus的包包括这个连接池的包
[05:20] 驱动的包日制的包括刚才我们在导入技术工程的有一些运维的包括单元测试的包是不是都要把它弄进去后面有一些工具类回头我用到会给大家说好到这我们把怎么样这个依赖给它完善了好那这个依赖呢我们写好了之后接下来各位我们说它这个POM文件是不是就算完工了
[05:55] 那你来你回忆啊现在我们建一个新的功能POM文件完成了之后那接下来干啥好像光依赖还不行吧是不是还得有什么日志文件呀还有一些什么这个它的bootstrap这个配置文件呀等等对不对跟刚才我们搭建这个应用工程差不多啊那各位那日志文件其实我们说可以共用的你从应用这里头你看你把你把这俩都拷过去都拷到这拷到这回头我们把比如说这个日志呢这个内容就不用改了
[06:25] 这个bootstrap我们把它改一下就行了bootstrap这一块呢这个是刚才我们的应用的这个工程差不多这个服务工程和应用工程这个文件的端口必须不能一样对不对包括这个怎么样它的服务名不能一样其他的基本上你没发现吧都一样也就是这个bootstrap这个文件其实上基本上也是一样的只不过有几个点大家要注意一个是端口号一个是它的服务名
[06:56] 好了这是不是就Service这个工程也搞定了那我Service工程搞定了之后它的组配置文件是不是也得写一下吧组配置文件组配置文件这里边大家知道这个组配置文件是不是就是微服务的名称和什么扩展名拼装而成所以来打开那块4在哪里在DV切到DV来在这添它的它的这个什么它的这个group是啥
[07:29] 我们统一是不是都是散剧group对好然后呢不要慌不要忙然后呢这里边我们不要把这个东西写错了你别看一堆配置你说感觉是没有啥技术含量但是你要是配错了他你可能就不太好排错来继续啊这次就他的工程路径了啊来走发布这是商户服务的这是商户应用的对吧配置文件搞定
[08:03] 然后当然它也需要一个启动类这个启动类好像好多呀是吧所以这我们得把它这个首先把包给它创建起来其实这个三户应用和三户服务的这个包路径基础的包路径都一样都是COM闪聚配然后呢Marchint然后下边我们把它的这个启动类创建一下把这个关掉好
[08:31] 创建启动类其实这个启动类就写了好多了所以我们就直接拷贝了把它拿回去各位这我是不是就写好了那写好了之后有人说老师那怎么测呀嗯启动它启动它了之后呢如果它加载配置文件出错那就控制台会报错如果成功它就会把自己注册到Nexus里头所以你看好像出现一点什么
[09:01] 问题对吧出现啥问题你看他报了一个什么东西还是连数据库的对不对那你现在我们现在还没有连数据库吧我们现在连数据库了吗还没有吧对一会儿呢我们但是上面是不是没有报错呀一会儿我们写代码的时候我们要连接数据库然后呢要查询数据库的信息等一会儿我们把这个驱动包括数据库连接池的配置呢也配好好那到这儿其实他就已经应该把自己已经注册上去了
[09:31] 这还是有一些问题的还是有一些问题的也就是说什么呀对它的命名空间命名空间那命名空间的话这里边呢你我们是不是统一都在这个DV下面我们再改一下然后呢再重启好所以说你在搭工程的时候一定要把工程啊然后呢按照一定的步骤流程把它搭起来
[10:09] 后边在这里边去填代码就行了好像这个还是也还不行那就说明我们现在你看它是不是缺了一个叫DataSource的URL但是现在目前来说将来我们把DataSource的URL补充上去之后它可以连上我们的数据库然后整个的启动我估计就可以完成也就是说现在大家可以看到还没有向我们的注册中心去注册它的服务不要着急目前来说
[10:37] 基本上是正常启动成功了然后呢稍后我们在这里边去填充我们要的这些代码然后顺便呢把刚才我们连接数据库的URL呢把它补充起来好那么到这儿我们的搭建商户服务工程就完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中创建并配置商户服务工程（shanjupay-merchant-api），并为该工程添加依赖和配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在项目结构中，右键点击 shanjupay-merchant 工程，选择“New” -> “Module”，创建名为 shanjupay-merchant-api 的模块。
画面 2: 在“Project Structure”中，选择“Modules”，确认新模块 shanjupay-merchant-api 的路径和名称。
画面 3: 在“New Module”对话框中，设置模块名称为 shanjupay-merchant-api，模块路径为 F:\teach\shanjupay\model2\code\shanjupay\merchant，点击“Finish”完成创建。
画面 4: 在 shanjupay-merchant 工程目录下，右键点击 shanjupay-merchant-api，选择“Add framework support...”，添加 Spring Boot 支持。
画面 5: 在 shanjupay-merchant-api 的 pom.xml 文件中，显示了父工程的配置，包括 artifactId、groupId、version 等。
画面 6: 在 shanjupay-merchant-api 的 pom.xml 文件中，显示了 <dependencies> 标签，其中包含 <version>1.0-SNAPSHOT</version>。
画面 7: 在 shanjupay-merchant-api 的 pom.xml 文件中，显示了 <dependency> 标签，其中包含 <artifactId>mysql-connector-java</artifactId>。
画面 8: 在 shanjupay-merchant-Service 的 pom.xml 文件中，显示了 <dependency> 标签，其中包含 <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>。
画面 9: 在 shanjupay-merchant-Service 的 bootstrap.yml 文件中，显示了 dubbo 配置，包括 scan、base-packages、protocol、name、port、registry、application、qos 等。
画面 10: 在 shanjupay-merchant-Service 的 bootstrap.yml 文件中，显示了 spring 配置，包括 application、main、allow-bean-definition-overriding、cloud、Nacos、discovery、config 等。
画面 11: 在 shanjupay-merchant-Service 的 bootstrap.yml 文件中，显示了 spring 配置，包括 application、main、allow-bean-definition-overriding、cloud、Nacos、discovery、config 等。
画面 12: 在 shanjupay-merchant-Service 的 MerchantApplicationBootstrap.java 文件中，显示了 Spring Boot 启动失败的错误信息，提示未配置数据源。
画面 13: 在 shanjupay-merchant-Service 的 bootstrap.yml 文件中，显示了 spring 配置，包括 application、main、allow-bean-definition-overriding、cloud、Nacos、discovery、config 等。
画面 14: 在 shanjupay-merchant-Service 的 pom.xml 文件中，显示了 <repositories> 标签，其中包含 <id>aliyun maven</id>。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1: 无代码或配置。
画面 2: 无代码或配置。
画面 3: 无代码或配置。
画面 4: 无代码或配置。
画面 5: 
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>shanjupay-merchant</artifactId>
        <groupId>com.shanjupay</groupId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>
    <artifactId>shanjupay-merchant-api</artifactId>
</project>

画面 6: 
<dependencies>
    <dependency>
        <groupId>com.shanjupay</groupId>
        <artifactId>shanjupay-commons</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>

画面 7: 
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>

画面 8: 
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
</dependency>

画面 9: 
dubbo:
  scan:
    # dubbo 服务扫描基准包
    base-packages: com.shanjupay
  protocol:
    # dubbo 协议
    name: dubbo
    port: 20890
  registry:
    address: Nacos://127.0.0.1:8848
  application:
    port: 22240 # dubbo qos端口配置 命令行注入
  qos:
    check: false
    timeout: 90000
    retries: -1

画面 10: 
spring:
  application:
    name: merchant-Service
  main:
    allow-bean-definition-overriding: true # Spring Boot 2.1 需要设定
  cloud:
    Nacos:
      discovery:
        server-addr: ${Nacos.server.addr}
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8
        cluster-name: DEFAULT
      config:
        server-addr: ${Nacos.server.addr} # 配置中心地址
        file-extension: yaml # 命令行注入
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8 # 命令行注入
        group: SHANJUPAY_GROUP # 聚合支付业务组
        ext-config:
          refresh: true
          data-id: spring-boot-http.yaml # Spring Boot http配置
          group: COMMON_GROUP # 通用配置组

画面 11: 
spring:
  application:
    name: merchant-Service
  main:
    allow-bean-definition-overriding: true # Spring Boot 2.1 需要设定
  cloud:
    Nacos:
      discovery:
        server-addr: ${Nacos.server.addr}
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8
        cluster-name: DEFAULT
      config:
        server-addr: ${Nacos.server.addr} # 配置中心地址
        file-extension: yaml # 命令行注入
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8 # 命令行注入
        group: SHANJUPAY_GROUP # 聚合支付业务组
        ext-config:
          refresh: true
          data-id: spring-boot-http.yaml # Spring Boot http配置
          group: COMMON_GROUP # 通用配置组

画面 12: 
Error starting ApplicationContext. To display the conditions report re-run your application with 'debug' enabled.
[...]
APPLICATION FAILED TO START
Description:
Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.

画面 13: 
spring:
  application:
    name: merchant-Service
  main:
    allow-bean-definition-overriding: true # Spring Boot 2.1 需要设定
  cloud:
    Nacos:
      discovery:
        server-addr: ${Nacos.server.addr}
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8
        cluster-name: DEFAULT
      config:
        server-addr: ${Nacos.server.addr} # 配置中心地址
        file-extension: yaml # 命令行注入
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8 # 命令行注入
        group: SHANJUPAY_GROUP # 聚合支付业务组
        ext-config:
          refresh: true
          data-id: spring-boot-http.yaml # Spring Boot http配置
          group: COMMON_GROUP # 通用配置组

画面 14: 
<repositories>
    <repository>
        <id>aliyun maven</id>
        <name>aliyun maven</name>
    </repository>
</repositories>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.6.2 搭建商户服务工程”，内容为“在基础工程的基础上创建商户服务工程，商户服务工程包括接口和接口实现两个子工程。”
画面

