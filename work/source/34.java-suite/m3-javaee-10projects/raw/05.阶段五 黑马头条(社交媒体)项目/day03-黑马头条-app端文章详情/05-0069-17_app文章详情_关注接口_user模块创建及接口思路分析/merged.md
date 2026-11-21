# 17_app文章详情_关注接口_user模块创建及接口思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\17_app文章详情_关注接口_user模块创建及接口思路分析【海量资源尽在 666java.com】.mp4
- 时长 16分15秒（音频 975s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位下面呢咱们就来去完成当前的第三个接口是关注接口咱们先来理解一下当前的关注接口啊首先的关注接口是实现当前登录用户关注其他用户那关注其他用户是啥意思呢就是说啊咱们之前其实在讲这个需求的时候咱们再来打开当前的需求这边呢是有一个关注对吧关注的话应该是属于某一篇文章那文章是不是属于某一个作者呀
[00:31] 也就是说我当前用户我是否需要当关注当前的文章的作者就这么一个操作你关注的时候今天咱们早上说过关注的时候就是啥意思就是说这个关注这点字会高亮不关注他就不会高亮就这么一个操作应该是就这么一个动作咱们回过头来再来去说一下这个接口首先这个接口它属于啥呢它属于当前APP用户中心
[01:00] 这个这个算是微服啊所以说呢首先呢咱们需要去先去创建当前的一个工程啊这个工程的话呢咱们创建起来其实非常简单咱们就直接先创建一下啊这个呢步骤呢咱们之前也经常创建啊我就快点去说一下啊那首先咱们在这啊去创建一个模块拷贝一下然后在这去拗一个模块出来下一步好直接把它拷过来然后好
[01:30] 换一下啊不对好点飞逆时这时候的这个模块就算创建出来啦他创建出来之后呢还不太行是吧你需要干嘛呢你需是不是需要去搭建环境啊咱们就直接从之前的这些啊配置文件跑过来好哪啊考到他的根本然后还有两个啊还有就是当前的配置配置的话咱们要考过来啊这两个搞到当前的resource下面这个好像还没有变色是吧你看这个颜色是不是好像没有
[02:01] 变回来是吧变回来也没有问题你怎么办你需要在这去刷新一下你会发现当前的user它是忽略掉的你可以把它给取消忽略点一下取消忽略之后你再去刷新一下应该就可以了稍等好稍等它应该会变过来变过来了现在变过来之后这里边的东西你需要去改一改改哪就是改当前的arbitration.publish里边这个并不是behaviour
[02:32] 并不是他了是谁啊当前的咱们是一个user模块啊userm模块啊像这个呢是他的一个断口号是吧一个是应用名称这个都在哪定义呢在当前的comment啊咱们可以再打开看一眼打开啊这有一个配置啊application properties啊下面呢是有一些东西啊比如说port.user就是9605然后下面还有一个就是他的应用名称往下走往下走啊
[03:01] 他的域名称就是当前的user看到了吧ok啊没问题那这功能他搭建完之后呢咱们下面还有些东西咱们需要去做了来看一下啊就说你需要把当年的破模件给拷过来破模件的话其实你也去参考当前的article就可以了啊嗯好打开呃打开比开盘article都一样啊其实哪个都行主要是把这个依赖给粘过来就可以啊control c一下啊control c然后找到user模块user呢
[03:33] user 模块打开POM文件然后是直接粘贴过来这样就完事了啊呃完事之后呢咱们下面呢就有一个这种我再往下看还有一个配置啊这个配置啊配置的话还有一些引导类咱们需要去设置一下像这些咱们不需要把它给删掉啊稍微改一改目前的话呢其实就需要这一个买搜索就可以了啊这两个咱们还在上不要OK那就写下呗写下啊在这你的家伙里边然后是创建一个包
[04:03] 创建一个包啊这个包呢叫com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.
[04:38] 当然上面还少一个注解啊哪个注解啊是当前的Spring BootRBlication好吧行那这个引导类创建完之后呢咱们下面去创建它的包它的包是哪个呢首先是有一个config然后还有啥还有一个Service还有什么还有controllercontroller你不要忘了什么东西Controller.v
[05:11] 是吧他们是一版本好点ok好了那这时候不明创建完了下面咱们要去把当前的Tomcat不是Tomcat是mycircle给加载进来这个咱们写一个初始化的类配置类就可以了mycircleconfig这里边咱们首先它是一个什么configuration然后下面什么components看是吧然后这里边可以去锁名个包说叫com.hema common什么
[05:41] mycircle核心这样的话我们看的我说的mycircle都已经加进来了加进来之后下面咱们就去定义接口定义接口之前咱们还要再分析一下这个接口到底去包含了哪些你看咱们再来读一下这句话就是此接口用于当前用户当前用户关注其他用户的记录关注其他用户的记录它应该包含两部分一个是
[06:08] 一个是关注的操作一个是取消关注的操作这两个操作一个是新增一个是啥一个是当前的什么东西一个是当前的这种取消的就删除行那这个咱们看一下当前这个GTO它需要从前台传递过来什么样才是Ctrl C一下是Shift Shift去找到当前这个类这个类里边其实你看这GTO里边
[06:38] 有两个啊一个一个类东西有这么一个几个参数吧第一个是当前的文章作者ID第二个是用户登录的ID啊第三个是文章ID第四个是你到底是取消还是关注啊这两个操作行那这是一块内容其实这里边还有一个隐含的一个需求又是啥呢一旦关注之后啊我需要干嘛呢我需要记录当前的关注的行为
[07:04] 关注的行为这个咱们我在这去画了个图其实里边一共是包含了两部分那两部分第一个部分就是当前的什么关注的行为关注的行为然后第二个就是当前的一个这种关注和取消的操作关注和取消的操作行咱们先去看一下当前关注的这种行为这行为的话刚才说了就这三个参数第一个是设备ID
[07:33] 第二个是当前的文章ID第三个是当前的Float ID这Float ID其实就是当前关注的用户的ID关注的用户的ID所以说这个你一定要理解一下这个就是当前比如说这样说吧就是当前作者他APP的账号ID当前作者当前文章作者的APP账号的ID这个就是Float ID
[08:00] 现在这个那么思路上呢他是涉及到两张表啊第一个是行为实体第二个是APP观众行为那这个其实跟咱们之前做那种保存行为这个思路其实差不多的啊怎么办呢来你们说来我写写来第一步要干嘛呢第一步永远不变是吧先干嘛呢先编程先使用先怎么办根据当前设备ID是吧Qui设备ID呢或者啥呢
[08:33] 或者是当前登录的user id去查询什么查询行为实体对吧查询行为实体这是第一步操作这是咱们保存当前的这种行为的话咱们永远都是第一步然后第二个呢第二个要干嘛呢就是有一个关注的行为其实需要去保存保存关注行为
[09:04] 那这行为的话其实咱们主要保存的就是像Pflow的开发这个咱们主要是看一个表咱们看这个表看里边有什么数据当前是哪个就是他这里边首先是有一个entryID这个ID能拿到吗能是吧咱们已经查出来了当前的行为实体第二个是articleID能拿到吗有因为咱们在这是不是也传过来当前的一个文章ID然后第三个来看一看
[09:33] 第三个是flow的ID这个是不是也有关注的用户ID是不是也传过来了好一个时间没了OK没了这个关注或者说保存当前关注的行为还是比较简单的OK那行这是第一个这是第一个接口咱们不是说第一个操作咱们需要去做的那咱们说第二块咱们去换个颜色换成这样的颜色
[09:59] 再说第二块第二块的话就是当用户去关注或取消关注的时候用户关注和取消关注的时候他有一些什么样的操作咱们再来说一下首先还是再分析一下首先他从前台传递过来的就那么多东西那么多首先第一个是当前的作者的ID可以拿到当前的用户ID可拿到也有可能拿不到但是拿不到怎么办呢拿不到咱们一会再说文章ID肯定能拿到
[10:29] 然后这个operation就是到底是操作的取决和关注这个肯定能够获取到好吧这里边它是涉及到了四张表这四张表咱们说一下首先是关注信息表然后还有的是粉丝表那为什么有粉丝呢咱们比如在分析还有一个是当前的用户APP用户还有一个是作者信息表作者信息表那这个思路是啥呢大家想想什么思路呢咱们可以在这写一下
[10:59] 大家听好,怎么办呢首先呢咱们要通过通过什么DTO中的user ID去查询什么查询吗获取吧去获取关注人的ID关注人的ID这个关注人的ID呀其实就是谁呀就是当前的你需要关注的某一个账号信息某一个账号信息
[11:35] 当然这里边传过来一个user id啊我们只是去查看到底到底没有传过来刚才说了他有可能没有传过来啊如果有可能是没有传过来的啊如果说啊如果没有user id怎么办呢可以通过啥呢可以通过当前的什么作者id去查询啊去查询这部咱们之前做过啊去查询那用完之后呢就是可以可以获取到
[12:11] 就是作者的APP账号信息其实咱们同一起个名字叫Float ID这就是要关注人的ID这是第一步拿到ID之后咱们就可以进行保存了保存之前咱们首先要去判断一下判断啥呢判断用户到底是啥呢判断用户是否
[12:43] 是啥呢关注或者取消或者取消关注和取消它的操作是不一样的关注的话咱们主要是保存数据取消的话咱们是删除数据那就说回来关注保存什么取消又要删除什么好来看一下首先第三步是关注如果说就是关注关注的话首先咱们先去先去哪先去当前的APGoeser Flow
[13:16] 然后去表中啊表啊表好检查是否已经关注这个啊因为关注完之后呢咱们统一不会去存到当前的表中如果说查到数据的说明已经关注了那这时候咱们就没有必要再进行保存了如果说没有啊如果说没有没有关注没有关注然后再进行保存保存的数据就包含两部分一个是当前的AP
[13:55] user flow第二个是当前的vp user fun那这个fun的话是啥意思啊这flow大家应该能理解啊就是这里边咱们可以去记录当前登录人和关注的用户的信息对吧你可以打开这表啊这个表的话就是当前的user flow是他吧你看这个用户ID和一个不是他
[14:22] 就是他当前的用户ID和个flow的ID其实这个flow的ID就是关注人的ID其实这个粉丝ID写错了就是关注人的ID就是关注人的ID他俩是有关系就可以然后同时咱们需要再去创建一个就是user1就是粉丝那粉丝的话正好相反正好相反哪块相反呢你看这个是用户ID那这个是粉丝ID那我想问一下
[14:51] 当前登录人是不是要关注关注某一个作者那你说作者是用户ID还是粉丝ID很显然嘛很显然就啥呢作者就是用户ID那粉丝就是谁啊粉丝ID谁啊粉丝ID就是当前登录人ID当前登录人ID没错吧OK啊那这个逻辑大家一定要能够去绕过来玩啊行那这个啊咱们说好了啊就是要去保存这两个数据就可以了
[15:19] 同时呢这一块还要再去加一个东西啊就是这个有一个星啊这个样啊要去保存保存用户关注的行为其实这个呢其实就是干嘛呢就是要用上面一个Service这个Service呢其实就是刚才咱们上面定的Service啊行那这是第三步啊还有第四步是吧就是取消关注取消关注的话就是删除数据啊就是删除数据
[15:58] 那创作数据的话其实也是在蓝表啊也是这个用户跟当前关注人的数据删除了就可以了行这个啊就是咱们的整体的一个思路然后下面咱们就用代码的方式就来去实现

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
创建并配置一个名为 heima-leadnews-user 的 Maven 模块，用于实现用户关注功能，包括工程创建、依赖引入、配置文件复制和主启动类编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了文档目录结构，当前位于“3.3 关注接口”下的“3.3.1 工程创建”部分。
- 文档内容说明：在根项目下创建 Maven 模块，项目名称为 heima-leadnews-user，group id 为 com.heima。
- 文档内容说明：在 heima-leadnews-user/pom.xml 中增加父项目信息。
- 文档内容说明：复制 heima-leadnews-article 下的 dev、test、prod 三个环境配置文件到 heima-leadnews-user 下。
- 文档内容说明：复制 heima-leadnews-article/resources 下的 application.properties、log4j2.xml 文件到 heima-leadnews-user/src/main/resources 下。
- 文档内容说明：复制 heima-leadnews-article/pom.xml 中的依赖 build 内容到 heima-leadnews-user/pom.xml 中。

画面2：
- 展示了 IntelliJ IDEA 中的项目结构，根项目为 heima-leadnews，包含多个子模块，如 heima-leadnews-spis、heima-leadnews-article、heima-leadnews-behavior 等。

画面3：
- 展示了 heima-leadnews-user 模块下的 maven_dev.properties 文件内容。
- 文件内容：
  log_level=DEBUG
  log_pattern=%d(DEFAULT) %M%n %l %t %N %M%n%msg%n

画面4：
- 展示了 heima-leadnews-common 模块下的 application.properties 文件内容。
- 文件内容：
  # 全局字符集设置
  spring.http.encoding.force=true
  spring.http.encoding.charset=UTF-8
  server.Tomcat.uri-encoding=UTF-8
  # 全局端口定义
  port.gateway=8081
  port.Eureka=8761
  port.boot.admin=8766
  port.login=9001
  port.article=9003
  port.behavior=9004
  port.user=9005
  port.media=9006
  port.admin=9007
  port.crawler=9008
  port.WebSocket=9009
  port.images=9010
  port.quartz=9011
  port.migration=9012

画面5：
- 展示了 heima-leadnews-behavior 模块下的 pom.xml 文件内容，正在编辑 dependencies 部分。
- 文件内容：
  <dependencies>
    <!-- 引入依赖模块 -->
    <dependency>
      <groupId>com.heima</groupId>
      <artifactId>heima-leadnews-model</artifactId>
      <version>4.0.0</version>
    </dependency>
    <dependency>
      <groupId>com.heima</groupId>
      <artifactId>heima-leadnews-common</artifactId>
      <version>4.0.0</version>
    </dependency>
    <dependency>
      <groupId>com.heima</groupId>
      <artifactId>heima-leadnews-spis</artifactId>
      <version>4.0.0</version>
    </dependency>
  </dependencies>

画面6：
- 展示了文档目录结构，当前位于“3.3.2 初始项目”部分。
- 文档内容说明：创建 com.heima.user.config 包，并复制 heima-leadnews-article 项目下 com.heima.article.config 的 InitConfig、MysqlConfig、SecurityConfig 三个文件。
- 文档内容说明：创建启动类：com.heima.user.UserApplication。
- 文档内容说明：SpringBootApplication 注解类代码：
  @SpringBootApplication
  @EnableDiscoveryClient
  public class UserApplication {
    public static void main(String[] args) {
      SpringApplication.run(UserApplication.class, args);
    }
  }

画面7：
- 展示了 heima-leadnews-user 模块下的 pom.xml 文件内容，正在编辑 dependencies 部分。
- 文件内容：
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.dataformat</groupId>
      <artifactId>jackson-dataformat-xml</artifactId>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.dataformat</groupId>
      <artifactId>jackson-dataformat-yaml</artifactId>
    </dependency>
  </dependencies>

画面8：
- 展示了 UserApplication.java 文件内容。
- 文件内容：
  package com.heima.user;
  import org.springframework.boot.SpringApplication;
  public class UserApplication {
    public static void main(String[] args) {
      SpringApplication.run(UserApplication.class, args);
    }
  }

画面9：
- 展示了在 IntelliJ IDEA 中右键点击项目目录，弹出“New”菜单，准备创建新文件或目录。

画面10：
- 展示了在 heima-leadnews-model 模块下，正在编辑 UserRelationDto.java 文件。
- 文件内容：
  import ...
  @Data
  public class UserRelationDto {
    // 文章作者ID
    @IdEncrypt
    Integer authorId;
    // 用户ID
    @IdEncrypt
    Integer userId;
    // 文章
    @IdEncrypt
    Integer articleId;
    // 操作方式
    // 0 关注
    // 1 取消
    Short operation;
  }

画面11：
- 展示了在 Word 文档中，正在编辑 FollowBehaviorDto 类。
- 文件内容：
  public class FollowBehaviorDto {
    // 设备ID
    @IdEncrypt
    Integer equipmentId;
    // 文章ID
    @IdEncrypt
    Integer articleId;
    @IdEncrypt
    Integer followId;
  }

画面12：
- 展示了在 Word 文档中，对 FollowBehaviorDto 类添加了注释。
- 文件内容：
  public class FollowBehaviorDto {
    // 设备ID
    @IdEncrypt
    Integer equipmentId;
    // 文章ID
    @IdEncrypt
    Integer articleId;
    @IdEncrypt
    Integer followId;
  }
  1. 根据 equipmentId 或当前登录的 userId 去查询行为实体
  2. 保存关注的行为

画面13：
- 展示了在 Word 文档中，对 UserRelationDto 类添加了注释。
- 文件内容：
  UserRelationDto ap_user_follow APP用户关注信息表
  // 文章作者ID
  @IdEncrypt
  Integer authorId;
  // 用户ID
  @IdEncrypt
  Integer userId;
  // 文章
  @IdEncrypt
  Integer articleId;
  // 操作方式
  // 0 关注
  // 1 取消
  Short operation;

画面14：
- 展示了在 Word 文档中，对 UserRelationDto 类添加了注释。
- 文件内容：
  UserRelationDto ap_user_follow APP用户关注信息表
  // 文章作者ID
  @IdEncrypt
  Integer authorId;
  // 用户ID
  @IdEncrypt
  Integer userId;
  // 文章
  @IdEncrypt
  Integer articleId;
  // 操作方式
  // 0 关注
  // 1 取消
  Short operation;
  1. 通过 dto 中的 userId 去获取关注人的 id，如果没有 userId 可以通过当前的作者 id 去查询，作者的 app 账号信息 followId
  2. 判断用户是否是关注或者取消
  3. 关注
  先去 ap_user_follow 表，检查是否已经关注，再进行保存
  ap_user_follow
  ap_user_fan

