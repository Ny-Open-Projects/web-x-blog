# 23.对接SaaS-准备工作-部署SaaS系统

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\23.对接SaaS-准备工作-部署SaaS系统【海量资源尽在 666java.com】.mp4
- 时长 14分9秒（音频 849s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面我们来部署SaaS系统根据刚才对接SaaS的步骤分析第一步我们要把SaaS系统给它部署成功好,首先我们先看数据库我们这里边要导入SaaS系统的数据库脚本好,那么打开我们的资料文件夹那么这里边我们有一个它的代码目录
[00:21] 好注意看啊这里边有一个叫散具配下滑线SAS的circle然后呢我们把它拷到我们的桌面然后这时候打开数据库啊这时候呢我们开始来执行这个脚本好所以在桌面当中我们选择刚才我们的这个脚本执行那这样的话这个SAS系统所需要的数据库呢我们就来创建成功了
[00:48] 因为这个系统呢是一个通用的系统这里边呢我们就不再去详细的解释里边的东西除非后边我们教学需要我们呢再会打开里边的这个什么内容给大家看大家看啊这里边导进去的有两个数据库一个是散具配下滑线UAA这个数据库两个表另外一个就是散具配下滑线UZER这里边这一些表那么这里边的一些表呢后边在对接的时候呢也会打开给大家看因为也可以验证我们是否对接成功好
[01:17] 这个数据库呢我们就搞定接下来呢我们要部署我们SaaS系统的三个服务那么这三个服务分别是这个GatewayUAA和User那么这三个服务具体的功能作用呢后边呢我们在具体对接的时候呢会给大家讲用到哪个呢我讲哪个首先呢现在呢就是我们按照文档呢把它部署到我们的IDEA这个项目当中好来看一下啊
[01:47] 那找到它的代码那这是给大家提供的资料里面有个代码文件夹我们找到这几个工程我们把它拷贝到我们的IDL的这个工程目录中看到了是吧然后呢拷进去之后呢按照我们说的这个流程啊我们打开我们的IDL看好打开IDL啊哪个呢好多啊是吧那么打开IDL之后呢这里边呢我们来看在这儿呢我们
[02:16] 它会有这三个工程呢就显示出来了看好是不是这个是getaway这是ua和user对吧然后呢这时候呢我们需要打开它的这个这个项目的一个结构然后呢我们需要怎么做呀之前为大家已经导过这个交易服务大家还有印象吗首先呢你需要去把它一个一个的把它导进来啊导的时候呢我们需要去找到找到我们现在的这个工程
[02:44] 比如说先到Gateway然后下一步对吧好这个是地址没有错啊地址没有错然后下一步选这个是干嘛这个是他的一个什么嗯没有找到这个导入好然后我们再来看一下啊我们再刷新一下再看一下然后我们再打开
[03:18] 刚才我们是不是把它考到我们的这个工程目录了但是你要注意我考进去之后你看这它的这个颜色呢它只是一个目录你看它并没有识别出是一个工程对吧所以这里边呢我们是需要去执行这个导入的过程的导入的过程呢这里边呢我们先导入KTV吧刚才我们导的时候是不是报错了import下一个再来然后再继续
[04:03] 这个是默认选中刚才那个是没有默认选中是吧好继续好然后再走好这样的话这三个工程大家看到现在应该是颜色要变了对吧好那么现在呢我们就把它给导进来了并且这个POP文件大家看到是不是也识别出来了那接下来呢我们要就是按照我们讲义上的要求啊我们把它参数呢给它就配置一下啊首先这里边呢我们要配置一个配置文件一个叫GWT
[04:35] 这个是将来我们进行认证的时候所需要的一个东西后边我会讲这个知识点啊咱们先打开我们的这个什么NetCourse好然后呢这里边我们新新增一个就是这个gwdl yml那么这个配置文件大家看到它只有一项配置啊一个是我们要把它的这个包就是这个group啊把它设置成common啊然后呢还有这个是它的一个参数是它的一个什么密钥
[05:05] 好回头我会说这个来你把它设到这各位这是不是就完事了对吧好那么这个弄完了之后呢嗯接下来呢你就可以把它发布然后接下来还有我们对照讲义开始做吧因为这个过程应该还没有涉及到技术东西啊这是gateway Service这是我觉得大家猜能猜得到吧这个配置文件是不是就是给我们的gateway来配置具体的配置文件对吧
[05:34] 所以这里边呢还是回到这个列表新增但是这个过程你可千万注意不要操作错你严格按照我的讲义上面来操作因为如果你操作错的话那么这个配置文件就读不到读不到的话这个SaaS系统呢它就起不上来好那这个呢大家看到它这个是一个叫Gateway-Service它的是配置内容我们是需要去拷贝一下的对吧好那一会呢我给大家拷贝一下
[06:05] 好那我们打开资料文件夹这里边呢我们看到有一个文件对吧我们打开然后呢你把它复制到我们的Gateway Service的那个配置文件中好那么我们复制进去呢之后呢这里边我们就可以直接点击发布好然后接下来我们继续再配置的是修改我们这个闪聚Gateway Service
[06:35] 这个这一步修改什么你大概知道吗你看是不是就是改我们的Namespace那你找到我们的Namespace的ID号然后呢我们现在要修改的话我们就一次性的把这个所有的都给它改了吧因为这里边呢我们考的这个导入的工程里边它的这个Namespace的ID号应该都不对就是和你的这个机器上的ID号都不一样看就这个
[07:06] 对吧好然后呢这个是Gateway还有我们刚才还导了一个UAA对吧UAA的这个呢你也参考刚才的方法呢你去把它给改一下好然后呢继续你把这个user呢也改一下行吧好这样的话我们把这三个这个工程的Necros的Namespace呢就改好了然后接下来呢我们看需要这里边
[07:38] 我们在Nexus里边再添一个UAA的这个配置因为刚才添的是Gateway嘛现在我们要添UAA另外一个服务好然后呢我们看到这个配置呢大家看它是什么呢它是UAA这个工程它所需要的一些配置这里边我们直接把它复制到我们的Nexus里边注意这里边有一个东西要改啊我相信你们看到啊就是这个数据库
[08:10] 因为刚才第一步我们是不是导数据库了你把这个数据库的这个账号和密码呢改正确就OK了好然后呢接下来啊我们就可以改统一账号的东西我们要给统一账号服务就是啊我们SaaS系统总共三个服务嘛一个Gateway一个UA一个User统一账号所以这里边呢我们在这儿也新增一个配置文件这些工作虽然繁琐啊但是呢你需要仔细
[08:39] 细心一点你要是配错了因为这个服务呢它就启动不起来了所以呢你把它考过去之后呢还要注意看到数据库连接的地方呢你要把它给改成正确的账号和密码好那这个过程是不是就OK了吧然后呢点击发布然后继续那内部space修改刚才统一都改过了对不对好那到这儿这个部署SaaS系统是不是就做完了
[09:07] 做完了之后呢你就说老师那怎么检测一下我能这个是否部署成功了呀好其实这三个服务呀我们是把原代码直接都导进来了所以说呢其实你要去看一下它成功不成功很简单那你只要因为它也是个Spring Boot的程序嘛你要把它给启动起来就OK了后边我们在对接SaaS呀包括统一认证等等我们都需要来启动它们对所以说各位
[09:37] 你要把它们给它启动起来那启动起来之后呢后边其实我们就在调对接SaaS的时候呢这三个服务呢我们就可以从这儿直接找到它的启动记录直接启动就不用来找它的这个启动类了对不对好那么我们这里边呢把它都启动起来之后呢注意不能让它干嘛哎报错刚开始这个启动这个服务呢
[10:05] 它可能会是有些报错为什么因为它要从这个Necros去找接口大家看到这里边UAA user还有一个东西我们刚才是不是启动了一个还有一个Gateway对不对你看这报了一个啥错这一看就是我们说的连接数据库是不是有问题对不对这是user那UAA呢UAA它也在报错报啥错
[10:37] 也是连接数据库我们看一下我刚才没有改对吗发布好看这啊我们看啊再再捋一下刚才我们配置的这几个啊一个是gatewaygateway这里头呢它是没有什么没有数据库连接的吧然后呢还有一个是ua你找到下面这个这是也ok了吧因为我们刚才是不是已经导
[11:06] 到数据库了对吧包括数据库的账号密码我也改对了啊然后呢还有一个是user这个这是三个配置文件嘛你看这个也对了没错吧好那我们现在呢再来看啊报错吗我们现在再找到啊再找到别着急看一下啊首先呢我们还是找到ua和gateway user我们先启动gateway把它起来一个一个起
[11:41] 看一下嗯他说的是现在他报这个东西是没有办法找到的也就是刚才我们配置的那个GWT的那个配置文件对不对嗯那这个好像有点问题了你再打开打开你看他这个ID对吗这应该是没有问题的吧看一下好然后再看他这个ID号F打头的到4这儿啊你不能配错了这好像是正确的吧这没问题的
[12:26] 然后再往后看你看这个文件不是也加载了吗也加载了这个是common group我们再看一下那个gwtcommon group也没问题我们再来这是啥原因啊执行我们看一下到底是什么原因啊好那么下面我们把necros呢给它重启一下然后呢接下来我们再重启这个gateway
[13:06] 其实我们这个时候呢我们就发现它这个配置呢就可以读取到了所以大家遇到这种从Necros上面读取配置读取不到的情况下呢除了你检查这个Namespace这里头是否正确然后呢把Necros呢也可以重启一下好那么我们再来重启一个是Gateway还有什么呀User还有一个UAA这几个服务呢都
[13:37] 必须能够启动成功好那么启动成功呢就算我们的SaaS系统呢部署成功了OK那么下边呢我们来看其实基本上我们看到是没有报错基本上就启动成功了对吧好那么到这儿呢我们这个部署SaaS系统整个的工作呢咱们就完成了后边呢我们就开始和SaaS系统呢进行一个对接好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Nacos 配置中心管理微服务的配置，并演示了 Spring Cloud Gateway 服务的启动与配置加载过程。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示项目目录结构，包含多个子模块如 shanjupay-transaction、shanjupay-merchant-application 等。
画面 2: 在 IDEA 中查看 PayChannelServiceApi.java 代码，其中包含从缓存中获取支付渠道参数的逻辑。
画面 3: 在 IDEA 中右键项目，弹出菜单，鼠标悬停在“Reimport”选项上。
画面 4: 在 IDEA 中打开 pom.xml 文件，显示了项目依赖和模块结构，同时弹出“Invalid VCS root mapping”提示。
画面 5: 在 Nacos 配置管理页面，显示了多个配置文件列表，包括 spring-boot-http.yaml、merchant-application.yaml 等。
画面 6: 在 Nacos 配置管理页面，鼠标光标位于“Data ID”输入框内，准备输入或修改配置。
画面 7: 在 Nacos 配置管理页面，选择“user-Service.yaml”配置文件，显示其内容为 username: root 和 password: yourpassword。
画面 8: 展示 PPT 页面，标题为“1.4 对接SaaS代码实现”，内容包含 Nacos 配置的详细说明。
画面 9: 在 IDEA 中打开 GatewayBootstrap.java 文件，显示了 Spring Boot 应用的启动类代码。
画面 10: 在 IDEA 中查看调试日志，显示了 Dubbo 服务注册和连接的详细信息。
画面 11: 在 IDEA 中查看调试日志，显示了数据库连接失败的异常信息。
画面 12: 在 IDEA 中打开 bootstrap.yaml 文件，显示了 Nacos 配置的详细内容，包括 server-addr、namespace、cluster-name 等。
画面 13: 在 IDEA 中查看调试日志，显示了服务启动成功的信息，包括 Nacos 注册、Dubbo 服务等。
画面 14: 在 IDEA 中查看调试日志，显示了服务启动完成的信息，包括 Dubbo 服务、QueueProvider 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2 代码：
```java
if (exists) {
    //从redis获取支付渠道参数列表（json串）
    String PayChannelParaDTO.String = cache.get(rediKey);
    //将json转成List<PayChannelParaDTO>
    List<PayChannelParaDTO> payChannelParaDTOs = JSON.parseArray(PayChannelParaDTO, String);
    return payChannelParaDTOs;
}
```

画面 4 pom.xml 结构：
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>com.shanjupay</groupId>
    <artifactId>shanjupay-user-Service</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>shanjupay-user-Service</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-config</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-consul-discovery</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Nacos-config</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-RocketMQ</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-RocketMQ</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-RocketMQ</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-RocketMQ</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-Sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-RocketMQ</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </

