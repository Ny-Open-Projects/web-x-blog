# 2.6 公共组件工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.6 公共组件工程_【海量资源尽在 666java.com】.mp4
- 时长 10分42秒（音频 642s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面我们来看一看冷链设备监控平台整个项目的一个公共组件code common那么公共组件工程呢其实是一个普通的java工程啊也就是一个普通java的一个maven工程我们的很多实体类啊倒层的代码或者说一些工具类公共类放在这个工程里边那么实际的一个一些公共的一些组件的工程呢它的范围其实不太一样的
[00:27] 那么有很多种设计模式比如说我们针对于某一个微服务比如像我们单纯的一个用户服务那么用户服务里边可能包含了好多个小子服务那么有一些子服务里边可能公共使用一些公共的这个工程公共的一些类那么我们把它放在用户的公共的组件里边但是对于我们冷链设备监控平台里边来讲的话整个业务流转
[00:56] 相对来讲比较简单一些我们就建了一个单纯的一个公共组件工程叫codecomic那么我们来看一看这个工程里边的一些啊代码和类那首先我们打开的话我们发现它其实就是一个普通的啊Maven工程而这个工程里边呢有一些啊有一些包这个包的话我们打开看一眼那主要包括这么两类或三类的一些文件
[01:24] 第一个的话是我们针对于道层的文件和实体层的文件也就是说intact和道那么intact和道来讲的话我们为什么要把它放在相同的一个工程里边来呢大家可以想象一下我们有很多的这个子系统比如说我们有用户系统我们有基础服务系统我们还有那个native服务那么我们有一些定义的
[01:53] 业务对象的一个实体那在比如在我们用户里边会引用那么在我们的比如另外的系统管理服务里边可能也会引用那这个实体类我到底放在哪呢如果我放在用户实体里边里边来讲的话那相应的我的系统管理可能要引用用户实体的整个的一个工厂这其实不太合适的反之亦然那么如果在这种情况下我们可以把它放到一个公共的地方
[02:22] 而在这个公共地方的时候它的整个结构体是比较简单的那它为我们其他的服务呢提供这种引用我们比如说用户服务可以引用这个公共的组件那么另外一个呢另外一个系统服务呢也可以引用这个公共的组件所以呢我们就把我们的实体层和道层放在这里面了
[02:45] 相应来讲的话有很多的也有很多的是把道层呢不放在我们的实体层或者不放在我们的公共层里边这个道层呢直接就放到我们的Service也就是说我们的系统或者说我们的服务里边在那些工程里边每种方式其实都是可以的主要是为了让我们的整个代码体系结构更加的一个简洁
[03:08] 我们它取决于我们这个系统的复杂程度有些系统比较复杂那我可能把一些公共的组件或者公共的一些道呢放到对应的一些服务里边那么如果简单一点的话我们就直接把它放到一个统一的一个公共的公共的一个工程里边那另外一类的数据是我们的一些工具类这些工具类有这么几种第一种来讲的话我们有一个分页工具这个分页工具我们用的是Mavidis Plus
[03:38] 那么Mobility Plus里边我们需要定义我们的这个每一个分页也就是说我当前的页数是1然后每一页显示10条记录这样的一个列表的一个页我们用了一个公共的一个分页的一个工具那另外还有一个是非常非常重要的就是我们的返回值那么这个返回值是一个什么特点呢这个返回值是我们当前这个工程
[04:03] 比如说我的一个用户服务用户服务向我们的前端提供我们的前端调用我们的后台服务然后返回结果那么返回结果我们在前面我们提到了我们的一个给前端响应的时候要有响应的一个结果对吧那么响应结果的时候我需要定义这个响应的一个范围响应的到底编码是多少比如说是200的一个code还是多少
[04:32] 还是401还是500等等这样的一个其实是返回的返回的一个code那另外的话就是我们需要返回的返回体的整个的它的一个message也就是说消息那到底是返回成功了还是不成功了我们在这里边可以返回的那其他的话我们还可以添加我们的一个kvalue那么这个kvalue又是什么呢我们比如说我们返回
[05:01] 我们需要返回的去具有分页的形式那分页形式里边来讲的话比如像现在这里边我们有一个record count或者是total count也就是说我们有多少页啊当前页数是多少啊总共有多少个数量我们其实可以在我们的这个result里边我们添加啊添加一个主件这个主件就是比如说像这个total count然后呢把我们的这个值给它放放进去这个时候我们可以返回为前台就是一个json格式的对不对
[05:31] 所以说这个result来讲的话就是统一定义我们的向前端返回的一个数据的格式那么这个类serialize,util这个类是一个序列化和反序列化的一个工具那么为什么要序列化和反序列化那么我们知道我们的数据在网络中传输的时候是以自截流来传输的那么自截流大家可以理解为其实和我们的
[06:00] 具体的语言开发的东西是不一样的我们假设我们用加尔文化语言开发的是加尔的对象那么我们用C++语言开发的是C++的对象我们用其他的语言比如说用PGP语言开发的那又是PGP语言的一个对象那么每一个对象来讲的话它都是通过网络来传输的那么在传输的过程中它应该是传输的是相同的对吧都是自接流但是它需要
[06:28] 在我们的Java程序里面需要转化成我们的Java对象那么在PGP语言里边它要转化成PGP对象那么这个过程是怎么做的呢这就涉及到序列化和反序列化我把一个Java对象序列化成一个二进制的流那么二进制流就能在网络中传输了到达目的地之后呢我们同样的使用相同的方法把它反序列化反序列化出我的Java的一个对象PGP也是一样的所以序列化和反序列化
[06:57] 序列化的作用主要就是把我们某一种语言开发的对象转换成二进制的流然后呢二进制流再进行一个反向的逆向的一个操作转换成一个加外对象这就是序列化和反序列化的一个作用那还有一个类的话是我们也比较也挺有用的一个类这个类呢叫做我们的spacen content的一个工具类那么对于spacen来讲的话它有一个spacen的容器对吧
[07:22] 我们Spring容器如果我们定义我们的一个component也就是说我们定义一个组件的时候我们的这个容器里边这个组件是放在我们容器里边的那么此时我如果想要拿到这个容器的这个容器中的这个组件我可以通过什么方式比如说我们Spring Boot它封装了一下那么我们还可以通过我们的这个应用程序也就是Spring的它这个上下文来拿到根据这个组件的名字来拿到某一个组件
[07:52] 这个地方是理解的稍微抽象一点点大家就可以理解为我们的Spring的容器那么或者说我们的这个我们程序代码运行它是运行在Tomcat里面对不对或者运行在这种服务器的容器里面但是服务器容器我们Spring在创建的时候它又创建了一个自己的容器叫Spring的容器而Spring的容器里面我们有一些公共的一些组件或者叫公共的一些服务公共的一些工具
[08:20] 这些工具呢实际上在指定容器里边的我们通过这个工具类呢就能拿根据名字拿到在指定容器里边相应的我们的这个呃组件这个是这个工具类的一个作用那么这个validator的有特效是我们对于检测我们对象是符合属于什么样类型的啊比如说这个这个方法这个方法的话我们就检测当前的某一个对象
[08:46] 是到底是什么类型的啊是是我们的company类型呢还是属于我们warehouse类型的等等这样的这样的一个检测的类型那后边我们如果定义其他的一些怎么说呢我们如果定义其他的呃这种这个验证的一些类啊验证的一些工具啊我们都可以放到这里边来作为一个验证工具的一个作用大家注意这个里边的工具其实是一个static就是静态的一个
[09:13] 静态的一个类这个静态类的话我们当我们的GVM容器一启动的时候这个静态类就已经出手化到我们容器里边了那么其他的其他的一些工程工程方法的话其他一些方法就可以在我们GVM里边直接拿过来这些工具类来使用了那么YAM的一个有特效的话相同的道理它是我们要检测我们的YAM文件比如说我们在我们资源里边有一个
[09:41] 我举另外例子就是Urica这个服务注册中心我们有这个application的样本那么我还可以创建其他的样本文件对吧我创建样本文件的时候样本文件里边的配置我怎么得到呢那我只能通过那种方式来来得到我们的样本文件样本文件里边的一些数值那还有一个类的话就是我们的redis的一个客户端那么redis客户端的话实际上有好多种写法那么这里边只是提供了一种写法我们可以
[10:10] 通过我们的Redis客户端的这个工具来把我们的数据放到Redis里边或者是我们把我们的Redis里边数据拿过来这是我们Redis客户端的一个作用OK那现在的话这个地方就是我们给大家介绍我们整个的CodeCommandCodeCommand具有什么样的作用我们把实体类放在这里边我们把一些工具类放在这里边那么这个工程呢可能是为了其他的一些项目引用的时候来使用的
[10:39] 这是我们整个的 code comment

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个名为“cold-common”的公共组件工程，主要展示其 Maven 依赖配置、通用返回结果封装、数据序列化、参数校验和 Redis 连接池配置等核心功能实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `cold-common` 项目结构，编辑器中打开 `pom.xml`，显示依赖配置，其中包含 `jedis`、`lombok`、`joda-time`、`snakeyaml`、`druid-spring-boot-starter` 等依赖。
画面2：在 `pom.xml` 中展示 `properties` 配置，定义了 `spring.version`、`mybatis-plus.version`、`lombok.version`、`joda.time.version`、`fastjson.version`、`gson.version`、`druid.version`、`Swagger.version` 等版本号。
画面3：PPT 页面标题为“4 公共组件 (cold-common)”，内容说明该工程包含 Java 实体类、DAO 代码、工具类等，便于其他项目引用，并展示其目录结构图。
画面4：PPT 页面展示 HTTP 请求方法（GET、POST、PUT、DELETE、PATCH、HEAD、OPTIONS）的定义和示例，以及 3.3.6 过滤信息部分，说明 URL 参数格式。
画面5：PPT 页面展示 3.4.1 开发规范，强调接口返回格式应使用 JSON，避免 XML，并说明 3.4.2 基本格式，要求 GET/POST 请求参数必须包含 key 为 body 的参数，数据包装为 JSON 格式。
画面6：PPT 页面展示 3.4.3 响应实体信息，定义了响应数据结构，包含 code、message、entity、code 字段。
画面7：IDEA 编辑器中打开 `Result.java`，展示 `Result` 类的构造方法和静态方法 `error`、`error`、`ok`，用于封装统一的返回结果。
画面8：PPT 页面展示 3.4.5 响应分页格式，定义了分页响应数据结构，包含 code、message、recordCount、totalCount、pageNo、pageSize、data、totalPage 字段。
画面9：IDEA 编辑器中打开 `SerializeUtil.java`，展示 `serialize` 方法，用于对象序列化。
画面10：IDEA 编辑器中打开 `ValidationUtils.java`，展示 `validate` 方法，用于参数校验。
画面11：IDEA 编辑器中打开 `ValidationUtils.java`，展示 `validateEntity` 方法，用于实体类参数校验。
画面12：IDEA 编辑器中打开 `JedisUtil.java`，展示 `JedisUtil` 类的定义和注释，说明其用于操作 Redis。
画面13：IDEA 编辑器中打开 `JedisUtil.java`，展示 `JedisPoolConfig` 的配置，包括 `maxTotal`、`maxIdle`、`minIdle`、`maxWaitMillis`、`testOnBorrow`、`testOnReturn`、`testWhileIdle`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`testWhileIdle`、`testOnBorrow`、`testOnReturn`、`numTestsPerEvictionRun`、`timeBetweenEvictionRunsMillis`、`numTestsPerEv

