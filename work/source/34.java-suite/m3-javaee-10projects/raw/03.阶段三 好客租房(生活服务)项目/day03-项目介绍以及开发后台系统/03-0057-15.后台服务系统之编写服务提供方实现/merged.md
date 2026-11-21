# 15.后台服务系统之编写服务提供方实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\15.后台服务系统之编写服务提供方实现【海量资源尽在 ubkz.com】.mp4
- 时长 19分10秒（音频 1150s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来编写服务的提供方就我们前面所提到provider那么前面呢我们已经把注册中心是不是已经搞定了那么接下来呢我们来看一下这个服务的提供啊
[00:14] 那么我们首先来创建一个工程来做一个这个测试啊呃工程名呢叫做itcast这个double然后呢呃上面的group id呢就cn.itcast然后呢double好来我们来创建一下工程那么我们打开idea工具然后呢在idea工具中呢我们去点击这个create new一个projector然后呢我们呃等待他一下loading这个template这个其实我们是不需要的不需要这个模板的
[00:44] 然后呢我们选择这个project sdk就选择我们自己所安装的这个ddk啊然后呢下一步那么gobid cn.itcast.n doublebbo然后呢itcast double然后呢我们把这个呢call一下然后呢下一步然后呢拷贝finish完成好这工程呢我们就已经创建好了来看一下这一个标准的一个memory工程
[01:16] 好然后呢我们在这个位置呢点击右键啊去new一个module创建一个子工程在这个位置呢我们注意要选择我们的这个JDK啊自己这个JDK然后呢我们来拷贝一下来一个什么呢叫Service是不是提供这个服务对吧提供服务的然后呢我们下一步拷贝然后呢finish完成那我们这个工程是不是就已经创建好了
[01:41] 那么操作好之后接下来我们来给他导入一些依赖导入相关的一些依赖那么我们首先在 idcast double的工程也就是我们这个副工程副工程的pub是在这在这个里面我们导入一些依赖咱们把这个拿过来那么咱们一点一点来call首先我们给这个工程添加一个parent就是我们sprint boot的一个parent那么所使用的版本是2.1.0的release版本
[02:10] 我们添加Pandas之后后面我们是不是导入一些Spin boot相关的依赖就比较方便一些了好那么我们接下来继续往下面导那么咱们把这个靠过来靠这个吧把dependencies然后全部都靠过来就是一些依赖由于我们在复工程中是不是已经添加了像什么Spin boot的一个测试test这样的一个测试框架然后下面是不是
[02:39] 导入了一个double的一个这样的一个框架是不是有个阿里巴巴下面的一个boot然后下面有一个double sprint boot start然后再往下面走导入的这个是double的一个依赖
[02:55] 那么在这其实要解释一下其实你下面这个可以不用添加注意可以不用添加如果你不添加的话那么在这个里面它也有一些相关的一些这个依赖去导入但是它所使用的这个double的版本不是这个2.6.4因为目前这个2.6.4是最新版
[03:12] 所以我们就单独去导入了一个double框架那么版本的指定它是2.6.4其实我们可以把它拿掉来看一下效果把它拿掉我们到这个里面来找一下看一下那么其实在这个里面找到刷一下还没出来dependence我们来看一下这个里面它所引入的一个double的框架看到了没有是不是2.6.2这个
[03:37] 版本的框架那么没有如果你不不单独引用的话那么就使用他的传依赖的做一个传递那么我们可以在下面这个位置添加一个double的一个依赖就是变成2.6.4那么他就会变成一个2.6.4但是我们会发现当我们就添加之后他好像并没有自动刷新对吧那说明我们这个配置稍微有点问题我们来调一下在这个settings下面找到一个build然后我们看一下这块有没有问题找到这个位置有个maron
[04:05] 下面呢有一个有一个这个叫import你看它import这个maniple这个自动这个打一个勾啊自动导入然后呢我们再看一下下面这个inglow里面那么这个这块没有问题是ok的好那么这样的话应该就好了咱们来测试一下把它拿掉然后呢我们再来再添加一下
[04:29] 那么我们来看现在是不是就自动是不是就加进来了那么现在所使用的这个double的框架的版本就是2.6.4这个版本ok好那么我们这个依赖就已经导入进来了那么接下来我们再添加一个这个plugin这个是Spring Boot的一个memory这样的一个插件咱们把它添加一下然后我们接着继续往下面看
[04:54] 我们找到我们这个子工程叫做Service的工程在这个工程里面我们去导入一些依赖导入什么依赖把这个扣过来把这个扣过来好那么往这里扣来看一下导入了什么依赖那么导入的是一个spin boot的依赖注意这个是一个非web项目那么如果我们报错刚才是多了一个w多了个w那么这样的话就好了
[05:25] 然后我们可以看到导入这个依赖它是一个非web项目那么由于我们是编写的服务的提供方那么是它是没有必要去做一个web服务的所以说我们导入的是一个非web项目然后下面注意在这个位置我们导入了一个Rootkeeper的一个client的这个它的客户端的一个
[05:45] 这个包啊然后呢下面呢我们导入一个ZKZClient这个包注意这两个必须得有没有的话我们这个服务的提供者呢他是没有办法去连接到我们的RooKeeper的这个注册中心的啊好那么这个呢我们也搞定了那么接下来呢我们就需要去编写一些我们的一些服务的服务的这个提供的一些这个具体代码那么首先呢我们先来创建一个我们的这个对象啊那么我们在这个下面我们先在这
[06:14] 在这个下面呢我们先来创建一个我们这个podio这个包然后呢我们把这个U的这个类我们拷过来这个呢就是一个非常普通的一个U的这个类那么在这个里面呢我们定义了一些什么像U的对象的一些属性像什么ID啊UNAME啊PASSWORD啊AGE啊等等一些相关的一些属性那么我们可以看到
[06:37] 这个类呢他实现了一个序列化的接口然后呢并且呢他也给他设置了一个这个序列化的一个ID然后呢我们在这需要强调的一点是这个double呢去要求我们传输对象的必须要去实现这个序列化的接口那么这个大家要注意一下那么我们写这个类的时候呢就给他加一个序列化的一个接口就OK了好那么接下来呢我们就要去写一些这个服务那么首先呢我们创建一个包
[07:06] 这个包叫做Service这个包那么我们在这创建一个这个Service的包然后在这个Service这个包下面我们创建一个接口注意是一个接口这个接口就叫userservice那么在这个userservice下面我们定义了一个方法叫做queryall这个方法那么这个仅仅是一个接口注意它仅仅是个接口它并没有实现类那么接下来我们需要做的事情就要去编写它的一个实现类
[07:34] 那么我们在这儿来创建一个包是不叫IMPL那么我们一般写实现类什么都会写到这个包下面去所以我们下面的把这个实现类我们拷过来那么这个实现类实现了这个接口然后实现了一个快速二那么在这我们要强调的一点是由于他要求返回的是一个集合list的一个user这样的一个集合那么我们现在就不做一个具体的数据库的一个查询那我们就做一个模拟的实现
[08:05] 然后再上去构造一个长度为10的这样的一个集合给他做一个return那么我们如果能够拿到这个数据那么是不是就说明这个接口是跑通了对吧那么我们后期再去结合整合数据库这个应该不是什么太大的一个问题
[08:21] OK然后呢我们来看一下这个接口的一个这个接口实现类的一个编写那么首先呢他是实现了我们这个接口对吧实现了接口然后呢我注意的是我们在这个接口在这个实现类上面添加一个Service注解要注意的是这个Service注解并不是Spring的那个Service注解而是什么呢而是这个double所提供的一个这个Service这个注解看到了吗哎呀OK是不是有个这个double这个包下面的这个注解
[08:50] 那我们给他添加了一个注解叫Service并且我们给他添加了一个Watson那么在这呢我也给大家简单的解释一下这个Watson什么意思呢他指的是我们这个版本啊指的我们是个版本那么为什么要有版本这个概念呢我们来看一下我们画一个图给大家来讲解一下就是说我们这个假设啊假设这个是我们的这个服务啊服务的提供方那么在我们的服务提供方里面呢我们会有一个
[09:18] 会有一个服务比如说就叫User ServiceUser ServiceUser Service服务那么我现在是不是会有一个客户端有个客户端他就会去调用我User Service服务OK我相信大家都能够理解没有任何问题对不对那么大家可以想象一下那么我User Service以后是不是可能会做更新
[09:46] 对不对那么是不是可能会做更新那么如果要做更新的话那么假设假设我直接在这个上面去做更新的话对吧做个更新的话那么他的代码逻辑就是原来调用的代码逻辑我们写一下这个叫消费者或者叫客户端叫消费者消费者或者消费方消费方那么他调用我们这个服务假设我这个服务是不是做升级那么有可能他的代码逻辑是不是也要跟着我们去做一些修改
[10:16] 这个大家能不能能不能够理解啊那么有可能是不是去做一个修改当然我说的是有可能啊有可能那么这个时候呢我们来看假设我们现在有好多的这个服务的这个消费方了有好多啊有好多哎有好多那么这个时候呢他们原来是不是都是去调用我这个服务对吧都调用这个服务都没有任何问题都可以去调用对不对那么现在呢我们这个服务需要做升级了那么
[10:44] 我假设我们现在这次的升级啊变化比较大要求消费方的都必须去做一些修改才能够使用我这个服务那么这个时候那么是不是我们如果说我们要做强制的在这个上面做申请是不是所有的人都需要去动啊对不对那么我们我们有一个做法呢就是说哎我可以给我这个服务干嘛呢我再来提供一个服务注意再来提供服务呢我给他制定他的版本指定他的一个版本
[11:13] 版本比如说变成2.0这个版本那么原来肯定这个版本是不是就1.0版本那就是1.0那么OK那么这个时候我的这个服务的消费方其实他本身是不是就会有一个选择了就是说你可以选择原来的1.0版本去使用也可以选择我们的2.0这个版本是做一个使用那么如果我再来一个消费者
[11:36] 再来一个消费者那么他是不是就可以选择我其实没有必要使用1.0了我是不是可以直接使用2.0对吧直接使用2.0这样是不是就OK了对吧那么等到我消费方他以后做版本更新的时候是不是我再去指向到2.0使用就OK了现在没有必要做一个跟着我是不是做一个升级大家能够理解这个意思吗
[12:01] 就是他是要升级但是呢不一定现在马上要做升级他可以在未来是不是做一个升级这样的话呢就可以做到一个服务的一个多样化的这样的一个支持哎OK这样的话我相信大家能够理解这个意思啊那么我会依然呢回到这个代码我们来看一下在这个代码中呢是不是我们给指定了一个版本那么后面我是不是可以给他指定一个多的一些这个版本的一些这个实现哎OK好那么我们接着继续往下面看那么我们现在呢已经是有了一个具体的实现类那么我们是不是需要接下来
[12:30] 要做的事情呢就是要给他去编写一个配置文件那么这个配置文件呢熟悉这个Spring Boot的同学呢并不陌生对吧就是Spring Boot的一个叫做application.publish文件那么我们来看一下这个文件中我们配置了有哪些内容把它贴过来
[12:48] 那么在这个里面我们可以看到前面这两个配置就是我们Spring Boot的项目的一些配置我们的应用的名称包括我们服务的端口然后往下面走下面的这个就变成了什么变成了我们自己Double的服务这样的一些配置那么首先我们给它指定的是一个版本1.0.0这个版本要注意这个版本是不是就刚刚我们在这个里面有用到在这在这个里面是不是有用到了它有的用到了它你看
[13:17] 一样的就他好那么我们来继续往下面看那么我们设置了一个扫描包就是说我们需要去扫描我们 double 的一些服务那么他所在的包在哪里是不是扫描的是 Service包他会扫描到我们接口以及实现内由于我们在实现内是不是加了 Service 注解所以他就会扫描到这个这个就是我的一个 double 的一个服务ok
[13:41] 好然后呢我们继续往下面看是不是设置了一个我们这个double的ablation name要注意的是这个是double的应用名称和上面这个一定要区分开来好那么我们继续往下面看在这个位置呢我们设置它的一个协议要注意协议
[13:58] 那么这个协议是指什么意思呢我们来看一下我们的这个讲义啊那么回到前面我们的这个注册中心那么再讲这个注册回到架构啊在这个架构里面我们可以看到那么我的消费者是不是通过我的注册中心是不是拿到我的一个这个服务我就去调用了对不对那么要注意的是我这个消费者
[14:20] 跟我的这个服务的提供方可能不在同一台机器是不是他们在两台机器那么一定会通过一个网络是不是进行通信对不对那么就通过网络进行通信那么也就意味着他们必然要通过一个协议进行通信那么这个协议所使用的是一个什么协议呢我们在这使用的是一个double他自己所自创的这样的一个或者说自定义的这样的一个协议double这个协议
[14:46] 那么我们继续往下面看然后呢这个呢是指定这个协议的端口呢是20880啊这个端口
[14:54] 然后呢继续往下面看到我们在这个位置指定它是一个ZK的一个注册中心的一个地址是不是我们这个172 1655 185 2181这个端口那么这个是不是就是我们在前面所部署的这个ZK的这样的一个注册中心哎OK好那么现在我们是来看一下啊现在我们是不是已经有了一个服务对吧有了一个配置大家想一想现在还缺什么吗是不是我们缺一个启动类去启动它呀哎OK好那我们来找一下我们这个启动类怎么去编写来看一下
[15:24] 那么在这边写这个启动类咱们把它靠过来那么我们这个呢把它放到哪里呢就放到这个double这个下面就放到这在这个下面呢我们去有一个叫做double的一个provider那就是我们这个启动类那provider呢是不是就是我们前面所说的服务的提供者然后呢我们在它上面呢就添加了一个sprint boot application这样的一个注解
[15:49] 这样的一个注解那么这个是不是就spin boot一个应用通过它是不是就可以启动一个spin boot项目然后我们写一个man方法做一个启动那么我们在这是不是启动启动我们的spin boot并且指定我们是一个非web项目非web项目然后我们指定的一个启动类就是它然后若去启动就可以了这样的话一旦启动的话那么它就会去读取配置文件
[16:16] 然后读取配置文件的就会去启动我们这个double启动这个double好嘞那我们来先来看一下这个效果点击这个RAW启动等待它的一个启动好开始启动了开始启动了看一下启动完成了吗还没有他呢正在去要去连接到我们的ROOTCAPER然后的做一个注册做个注册你看看到了吗在这个位置是不是有一个
[16:57] 叫RooKeeper这样的一个包他说明他也正在使用RooKeeper这个包进行通信好那么我们是不是可以进到这个里面来刷新一下刷一下我先点停止重来一下这个我输入我的RooKeeper的服务的地址172.16.55.185点击这个OK等待他的一个连接我们来看一下他有没有把这个服务
[17:27] 注册到我们的Rulekeeper上面去稍微等待一下我们来看一下他有没有做一个注册看一下我们的这个控制台控制台中到这呢已经就启动完成了启动完成了启动了启动了通过了30秒钟的一个时间做一个启动
[17:46] 好那么我们来看一下在这个Rule Keeper中它已经有了一个double的这一个节点那么在这个下面是不是也做了一个注册看到了吗是不是通过我们这个包这个是我们的一个服务是不是User Service这个服务然后它的一些配置包括的Provider它的一些提供方那么提供者的一些信息我们其实可以看到是不是有这么多信息
[18:09] 这个是我的一些端口号对吧端口号然后呢这个是我来币地址后面是我的这个具体的一个实现类实现类可以看到是不是有很多这个信息哎呀OK答案了在最后其实我们可以看到大家能看到吗是不是有个Warson是不是有个1.0.0是不是我们所指定那个版本号哎呀OK好那么到这呢其实我们就可以看到我们是不是已经成功的
[18:32] 将我们的一个这个服务的提供者是不是已经就注册到了注册中心那么回到这个架构上面来看那么是我们就完成了第一步通过这个容器这个容器呢是不是就是我们Spring布的这个容器做一个这个启动那么启动之后呢我们的服务的一个提供者他就将我们的一个服务注册到了注册中心注册中心就是什么呢JK这个注册中心然后呢接下来我们要做的事情是不是我们编写一个服务的一个消费方
[19:02] 去消费这个服务然后去做一个调用OK好那么我们关于这个服务的一个提供方的编写我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
创建并配置一个基于 Spring Boot 和 Dubbo 的服务提供方项目，包括工程初始化、依赖管理、POJO 类定义、服务接口与实现类编写以及配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示创建新工程的对话框，Group ID 为 cn.itcast.dubbo，Artifact ID 为 itcast-dubbo，Version 为 1.0-SNAPSHOT。
画面 2: 在 IntelliJ IDEA 中，右键点击项目，选择“Add Framework Support...”，并选择 Spring。
画面 3: 编辑父项目的 pom.xml，添加 Spring Boot 的 parent 依赖。
画面 4: 编辑父项目的 pom.xml，添加 Spring Boot Test 依赖。
画面 5: 编辑父项目的 pom.xml，添加 Dubbo Spring Boot 依赖。
画面 6: 编辑子模块的 pom.xml，添加 ZooKeeper、gRPC、Dubbo 依赖。
画面 7: 编辑 User.java 文件，定义 User 类的属性和方法。
画面 8: 编辑 UserServiceImpl.java 文件，实现 UserSerivce 接口的 queryAll 方法。
画面 9: 显示一个空白的流程图或架构图。
画面 10: 编辑 application.properties 文件，配置 Spring Boot 和 Dubbo 相关属性。
画面 11: 在 application.properties 文件中，将 dubbo.protocol.port 设置为 20880。
画面 12: 编辑 DubboProvider.java 文件，使用 @SpringBootApplication 注解并配置主方法。
画面 13: 运行 DubboProvider.java，控制台输出 Dubbo 客户端连接信息。
画面 14: 显示 User.java 文件，定义 User 类的属性和方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
Group Id: cn.itcast.dubbo
Artifact Id: itcast-dubbo
Version: 1.0-SNAPSHOT

画面 2:
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.dubbo</groupId>
    <artifactId>itcast-dubbo</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面 3:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 添加springBoot parent支持 -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.dubbo</groupId>
    <artifactId>itcast-dubbo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <modules>
        <module>itcast-dubbo-Service</module>
    </modules>
</project>

画面 4:
<dependencies>
    <!-- 添加Spring Boot测试 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>

画面 5:
<dependencies>
    <!-- 添加Spring Boot测试 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <!-- 添加dubbo的Spring Boot依赖 -->
    <dependency>
        <groupId>com.alibaba.boot</groupId>
        <artifactId>dubbo-spring-boot-starter</artifactId>
        <version>0.2.0</version>
    </dependency>
</dependencies>

画面 6:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <artifactId>itcast-dubbo</artifactId>
    <groupId>cn.itcast.dubbo</groupId>
    <version>1.0-SNAPSHOT</version>
    <artifactId>itcast-dubbo-Service</artifactId>
    <dependencies>
        <!-- 添加Spring Boot依赖，加web项目 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.ZooKeeper</groupId>
            <artifactId>ZooKeeper</artifactId>
            <version>3.4.13</version>
        </dependency>
        <dependency>
            <groupId>com.github.sgroschupf</groupId>
            <artifactId>zkclient</artifactId>
            <version>0.1.0</version>
        </dependency>
    </dependencies>
</project>

画面 7:
package cn.itcast.dubbo.pojo;
/**
 * 作用：dubbo要求传输的对象必须实现序列化接口
 */
public class User implements java.io.Serializable {
    private static final long serialVersionUID = -7341603993352159322L;
    private Long id;
    private String username;
    private String password;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

画面 8:
package cn.itcast.dubbo.Service.impl;
import java.util.ArrayList;
import java.util.List;
import cn.itcast.dubbo.pojo.User;
import cn.itcast.dubbo.Service.UserService;
import com.alibaba.dubbo.config.annotation.Service;
UserServiceVersion = "${dubbo.Service.version}"; //声明这是一个dubbo服务
public class UserServiceImpl implements UserService {
    //实现查询，这里随机从实现，不能具体的数据库查询
    public List<User> queryAll() {
        List<User> list = new ArrayList<User>();
        for (int i = 0; i < 10; i++) {
            User user = new User();
            user.setId(Long.valueOf(i + 1));
            user.setPassword("123456");
            user.setUsername("username" + i);
            list.add(user);
        }
        return list;
    }
}

画面 10:
# Spring boot application
spring.application.name = itcast-dubbo-Service
server.port = 9090
# Service version
dubbo.Service.version = 1.0.0
# 服务扫描包
dubbo.scan.basePackages = cn.itcast.dubbo.Service
# 应用名称
dubbo.application.name = dubbo-provider-demo
# 协议以及端口
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
# zk注册中心
dubbo.registry.address = ZooKeeper://172.16.55.185:2181
dubbo.registry.client = zkclient

画面 12:
package cn.itcast.dubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class DubboProvider {
    public static void main(String[] args) {
        new SpringApplicationBuilder(DubboProvider.class)
                .web(WebApplicationType.NONE) // 非 Web 应用
                .run(args);
    }
}

画面 14:
package cn.itcast.dubbo.pojo;
/**
 * 作用：dubbo要求传输的对象必须实现序列化接口
 */
public class User implements java.io.Serializable {
    private static final long serialVersionUID = -7341603993352159322L;
    private Long id;
    private String username;
    private String password;
    private Integer age;
    public Long

