# 17.开发环境搭建-工程测试-生成代码及Mybatis-plus配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\17.开发环境搭建-工程测试-生成代码及Mybatis-plus配置【海量资源尽在 666java.com】.mp4
- 时长 15分20秒（音频 920s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们进行工程的测试那么在刚才我们搭建了商户平台应用和商户服务工程下面呢我们通过一个简单的案例根据ID来查询商户信息这个案例呢我们测试一下整个工程的这个代码开发的流程通过呢本次工程的测试呢希望大家呢能掌握咱们整个这个项目工程项目架构的一个开发的基本流程那什么基本流程呢就是
[00:27] 怎么开发我们的微服务怎么连接数据库怎么去写我们的Service接口以及开发我们应用平台的这个接口然后去调用微服务最终把整个流程的测试通就根据ID查询商户这样一个需求好那么我们回顾当初我们去进行研究double服务架构的这个方法我们知道API里面是写接口的
[00:56] Service里面是不是要写接口实现然后呢在这个application当中我们是不是要写就是暴露RESTful接口的Controller然后在application这个Controller里面是不是要远程调用double full的接口就是这个这个结构啊大家呢一定要注意就是我们必须按照我们的这个流程先写接口再写接口实现然后呢再写application应用
[01:26] 当中的这个Controller去调用我们的微服务这样一个流程好那么我们先写接口先写接口实现那这里边就涉及到有一些这个通用的代码我们是需要先去自动生成的对吧所以这里边呢我们需要去打开我们的自动生成的工程然后呢我们来进行自动代码的这个生成对吧好那么这个生成的
[01:55] 自动生成代码这一块呢我们当初是应该在我们的资料文件夹下边这个基础工程这一块应该给大家提供了是不是当初其实我们应该已经导入成功了对不对那这里面呢其实我们就直接打开我们的generator就可以了打开generator这里面呢我们来看我们是现在要做一件事啊这是原来生成的我们把它删掉一会我们再新生成一份代码
[02:24] 第一件事要做什么呢是不是要连接你的数据库对不对你现在数据库我们要准备生成什么现在我们主要做的是商户这一块的这个功能所以我们要连接这个数据库叫闪聚配Marchint Service就这个数据库所以这里边呢我们在这改一下看懂吗然后呢这个是账号密码都不说了然后呢这个是包这个包就是你将来生成代码所基于哪个包
[02:55] 来放是吧好那接下来我们再看那我们说那你刚才数据库改过了那这个包名是不是也不用改了那现在我们就可以直接运行了吧那么我们如果运行的话各位还记得不记得它是需要要求我们去输入一个模块名还有印象吧所以这里面我们要输入一个模块名这个模块名注意这个模块名我建议和
[03:25] 我们的这个注意这个包名看见吗你打开是不是有一叫Machines是吧跟它保持一致来我们在这数一下好注意这时候呢它就连接上我们的数据库连接你看这是五张表吧然后呢它就生成了什么五个Entity五个Map对吧来我们来瞧一下你看包是这样吧这个是Entity
[04:00] 是五个吧然后Mapper大家看见吧所以其实我们目前来说我们就把这个Mapper和Entity就生成好了包括Service也有但当其实我们只用Entity和Mapper所以这里面呢我们生成完代码了之后啊我们就可以把这两个东西干嘛呀其实可以把它给拷到我们的工程下边了这两个不要了都删掉
[04:30] 那时候要的呢要的留下来直接考com然后呢到我们的工程上考到哪啊你告诉我考到哪你现在是要做的事是不是就是在我们的Service这个API的实现类当中我们要把它考进去是不是就进来了好这就是我们生成的这个类将来我们就直接用它就可以了好自动生成代码这一块我们是不是就完工了
[05:03] 好那么自动送送代码完成了之后呢接下来我们是不是还需要去做一件事就是要配置我们MapBasePlus的一些连接数据库的参数啊那么来看一下首先呢我们是需要去创建一个配置文件这配置文件呢也是个公用的配置文件叫Common Group是不是在这个组里头呢那它呢主要是配置一个叫Droid的连接池来
[05:32] 我们呢来看一下啊在哪里啊在这点击添加好这个坠的呢也是一个连接池啊跟我们之前学习的这个C3P0啊或者说DBCP啊等等这些连接池是差不多的来我们把它拿过来好这个到这选择YAML这是不是就搞定了
[06:07] 但是其实这里边要注意注意有几点就是说大家看这里边的这个东西你看看这是不是有一个URL你看见吗这是不是就是连接数据库的参数那我问大家一个问题现在我按照讲义上的内容我把它拷贝到咱们的这个Necros里边你看把它配置它是相当于写死了对吧但是其实我们的账号数据库账号密码不是这样的对吧包括我们的数据库也不是这个
[06:35] 其实这只是一个通用的配置后边如果谁想改就是可以在各个微服务里边去覆盖咱们是不是之前说过对微服务自己的主配置文件可以覆盖它的配置对不对好这是个通用配置那这些配置其实你不用改了就可以去使用通用的了好那么这整个的就是比如说这个是它的一个什么包括它的这个链接数
[06:58] 然后空闲链接数啊初始化链接数啊最大链接数啊等等这些配置呢我们就不在课堂上一一讲了其实大家可以去网上搜一下这个Dread的一个相关详细的参数的一个说明啊大家呢就自行去查阅文档啊然后呢这里我们就把这个Dread的配置文件就搞定了那刚才说了嘛你的这个数据库连接需要个性化对不对所以我们需要独立再配置一个什么它的组配置类那里边呢我们要把它填进去覆盖
[07:28] 注意的这个配置文件当中的这个连接参数好我们先把它发布啊发布完了之后呢我们现在要这地方好像还有问题呢看一下吗MarchandService你看它扫了一个扩展名你看一下嘛这个问题其实是挺严重的一个问题啊然后呢因为它你扫一个扩展名它肯定是没有办法去找到这个配置文件了对不对所以这里边呢各位啊看好
[07:58] 我先把这个配置给它粘出来好然后呢这个配置呢我们需要改一下就这个因为它没有扩展名嘛你先把它三了再建一下对吧啊然后呢这个是不是就是闪聚配哎然后呢来把刚才的配置呢拿过来啊顺便呢把我们将要往里边填的这些配置也拿过去啊各位这上面是原来的它的这个啊
[08:36] 这个工程的一个目录啊对吧然后下面呢这个是他的一个数据库的连接那数据库连接这边我们就把它配正确根据你自己配啊你不要看着我是配了一个root mycycle因为我的密码是mycycle所以呢你的密码是多少包括你的账号是多少你都配正确好那发布这是不是就可以了好然后呢继续还有一个组配置文件因为你刚才啊你是不是配了一个叫Droid的连接池的这个组配置文件
[09:10] 这个配置文件呢你需要在哪里啊在扩展在主配置文件这个bootstrap里边就扩展这个配置文件来看一下来找到它的配置配置好多啊那一会儿我给大家捋一下我配完了之后你就知道了好看好啊好这有问题了你看见吗对不对这是我们先看一下啊这个应该改成什么了我们之前学过吗0对不对这就是1是吧
[09:50] 其实可以这么玩就原来我们讲Necros的时候是怎么配的其实我们这么弄这样也行对不对这样也行这时候我们就扩展了一个Drived的配置文件注意看Poodstrap这个配置文件是我们项目启动所要用的对吧然后一用的话它就自动会加载这个服务名加上扩展名的这个配置文件这个配置文件在Necros里面是不是已经有了对吧那这个配置文件优先级最高优先级最高
[10:22] 然后呢它在扩展了一个是http通用配置一个是什么阿坠的数据库连接池的这个通用配置继续往后再看啊myvtes plus本身我们也要扩展一个通用配置然后呢继续这个就common了common group然后呢在这个里头要扩展哪些配置呢其实就是myvtes本身当初我们学习myvtes的时候我们是不是说了它自己要设一些配置比如说缓存的呀驼峰命名映射的方式呀
[10:56] 对吧还有它的一些全局的配置包括它的这个什么别名扫描包包括Mapper地址的配置其实还跟刚才一样就是你这里边你配的是一个通用的配置回头呢谁想覆盖呢你可以覆盖某些项目的配置对不对你比如说你想这个别名的扫描包对不对明显呢它这个地址呢将来是需要覆盖的对吧但你要不覆盖的话它就用这个地址了走这个通用的配置是搞定了吗通用的配置
[11:27] 搞定了之后你就需要在我们的bootstrap里边去扩展扩展的方法跟刚才我讲的一样你就笔糊了画瓢了这时候你看来一个你看是不是又把刚才这个扩展的这个通用配置放上去了好那么继续那刚才呢我们说嘛你这是通用的配置你要想覆盖那你就需要在你本身的微服务上面去覆盖那本身的微服务咋覆盖啊那你就在这里边去
[11:57] 覆盖它的一个属性就行了你看我覆盖了啥一个是扫描这个什么那个entity这些别名的这个包的路径一个还有啥它的Mapper文件的这个路径当前其实我们还没有定义Mapper文件因为我们当前只是自动生成了Mapper接口将来如果我们要自定义Mapper各位你要根据这个路径来了这是不是就是com
[12:26] 散具配下边这有个星也就是这里边你可以写目录随便目录然后后面有个map你要记得这个路径啊发布这个配置文件到这为止各位我们是不是就完成了还有当初我们讲买Batis Plus的时候我们是不是说了要进行分页需要配它的一个分页插件对不对所以这里边看好配一下在哪配啊这是
[12:59] 不要打错工厂啊在我们的这个商户服务这儿是吧在这儿来一个可不可以就前期我们搭项目的时候你会发现东西好多是吧啊又是配这啊又是干那其实要注意啊一会儿呢我给大家简单总结一下你就知道了其实没几项东西其实像这个mybatesplus的分页插件的配置这跟我们当初讲mybates啊这个知识的时候课程的时候你是不是就学过这个东西啊所以这没有
[13:31] 太难啊嗯好这个是启用一个性能分析的插件这个插件呢将来我们用到再说啊主要是这个这个是分页的插件好还有一个就是扫描我们说Mapper接口的这个位置啊扫描Mapper接口的位置嗯OK那么各位到这儿各位我们是不是就完成了这个买白TestPlus的各项配置我们现在捋一下啊首先目前来说我们要做的事是不是就是跟要写一个案例根据ID查询商户啊
[14:01] 那么我们知道嘛万事开头难很多的这个代码都是没有的我们就需要用generator我们提供的一个代码生成的工程我们生成我们要的一些代码生成哪些代码呢其实我们就生成了两类一类是entity一类是Mapper这是我们说对应表的那个模型对吧然后还有一个叫Mapper接口那你学过MapBitx你知道这个就是我们必须要定义的一个接口将来根据这个接口
[14:30] 来对数据库进行增长改查好然后呢又接下来我们又配置了什么呀它的MyBitX Plus的各项东西MyBitX Plus呢要连接数据库嘛所以我们配置一个数据库的连接配置文件然后呢还配置了这个它的什么MyBitX Plus自己的配置文件然后以及它的分野插件OK那么到现在
[14:58] 我们是不是就完成了生成代码以及买BetisPlus的这些配置其实到这为止我们这个基础的工程就是我们刚才在搭建完创建完这个工程基础之上我们把这些该做的配置就是买BetisPlus相关的配置就算完成了那以后其实我们就直接可以写Service接口调用Mapper来操作我们的数据库了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 代码生成器自动生成商户服务的实体、Mapper 等文件，并配置 Nacos 作为配置中心管理 Spring Boot 项目配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程大纲，当前章节为“1.7 工程测试”，子章节“1.7.1 生成代码”，并显示了修改数据源配置的代码片段。
画面 2：展示文件资源管理器，路径为“.../output/dao02/资料/工程测试/generator”，目录下有“src”、“target”和“generator.ini”文件。
画面 3：在课程大纲中，显示了“3) 运行生成类，输入模块名：merchant”的提示，并在代码编辑器中高亮了“merchant”。
画面 4：在 IntelliJ IDEA 中，显示了 MyBatis-Plus 代码生成器的 Java 类 `MyBatisPlusGenerator.java`，其中包含 `initMap()` 方法和 `outputFile()` 方法的代码。
画面 5：在 IntelliJ IDEA 中，显示了 `App.java` 文件，其中定义了 `@TableField` 注解的 `appId` 和 `appname` 字段。
画面 6：在 IntelliJ IDEA 中，显示了 `StaffMapper.java` 文件，其中定义了 `StaffMapper` 接口，继承自 `BaseMapper<Staff>`。
画面 7：在课程大纲中，显示了“1.7.2.1 配置连接池Druid”的子章节，并高亮了 Druid 数据源配置的代码片段。
画面 8：在 Nacos 配置管理页面，显示了“删除配置成功”的提示，配置 ID 为 `merchant-Service`，分组为 `SHANJUPAY_GROUP`。
画面 9：在 IntelliJ IDEA 中，显示了 `bootstrap.yml` 文件，其中配置了 Dubbo 的 `scan`、`protocol`、`name`、`port` 和 `registry` 等属性。
画面 10：在 Nacos 配置管理页面，显示了“新建配置”的表单，Data ID 为 `spring-boot-mybatis-plus.yaml`，Group 为 `COMMON_GROUP`。
画面 11：在 IntelliJ IDEA 中，显示了 `bootstrap.yml` 文件，其中配置了多个 `data-id` 和 `group`，用于加载不同的配置文件。
画面 12：在 Nacos 配置管理页面，显示了配置列表，包括 `spring-boot-http.yaml`、`merchant-application.yaml`、`spring-boot-starter-druid.yaml`、`merchant-Service.yaml` 和 `spring-boot-mybatis-plus.yaml`。
画面 13：在 IntelliJ IDEA 中，显示了 MyBatis-Plus 代码生成器的 Java 类 `MyBatisPlusGenerator.java`，其中包含 `outputFile()` 方法的代码。
画面 14：在 IntelliJ IDEA 中，显示了 `AppMapper.java` 文件，其中定义了 `AppMapper` 接口，继承自 `BaseMapper<App>`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
// 商户服务
dataSourceConfig
    .setUrl("jdbc:mysql://127.0.0.1:3306/shanjupay_merchant_service?"
            + "serverTimezone=Asia/Shanghai");
```
画面 3：
```java
// 生成包配置
PackageConfig packageConfig = new PackageConfig();
packageConfig.setParent("com.shanjupay");
```
画面 4：
```java
@Override
public void initMap() {
    // to do nothing
}

// 如果模板引擎是 freemarker
String templatePath = "/templates/Mapper.xml.ftl";

// 自定义输出配置
List<FileOutConfig> focList = new ArrayList<>();
// 自定义配置会被优先输出
focList.add(new FileOutConfig(templatePath) {
    @Override
    public String outputFile(TableInfo tableInfo) {
        return "/Mapper" + tableInfo.getEntityName() + "Mapper.java";
    }
});
```
画面 5：
```java
public class App implements Serializable {
    private static final long serialVersionUID = 1L;
    @TableField(value = "ID", type = IdType.ID_WORKER)
    private Long id;
    @TableField("APP_ID")
    private String appId;
    // 商户名称
    @TableField("APP_NAME")
    private String appname;
}
```
画面 6：
```java
public interface StaffMapper extends BaseMapper<Staff> {
}
```
画面 7：
```yaml
type: com.alibaba.druid.pool.DruidDataSource
driver-class-name: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/oauth?useUnicode=true
username: root
password: yourpassword
druid:
  initial-size: 5
  min-idle: 5
  max-active: 20
  max-wait: 60000
  time-between-eviction-runs-millis: 60000
  min-evictable-idle-time-millis: 300000
  validation-query: SELECT 1 FROM DUAL
  test-while-idle: true
  test-on-borrow: true
  test-on-return: false
  pool-prepared-statements: true
  max-pool-prepared-statement-per-connection-size: 20
  filter:
    stat:
      slow-sql-millis: 1
      log-slow-sql: true
    filters: config,stat,wall,log4j2
    web-stat-filter:
      enabled: true
```
画面 9：
```yaml
file-extension: yaml
namespace: f5ec3c1-4f05-40cd-964a-8444742ab4
group: SHANJUPAY_GROUP # Spring Boot 业务分组
ext-config:
  refresh: true
  data-id: spring-boot-http.yaml # Spring Boot http配置
  group: SHANJUPAY_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-starter-druid.yaml # Spring Boot starter druid配置
  group: COMMON_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-mybatis-plus.yaml # Spring Boot mybatis-plus配置
  group: COMMON_GROUP # 通用配置组
dubbo:
  scan: # dubbo 服务扫描包
    base-packages: com.shanjupay
  protocol:
    name: dubbo
    port: 20880
  registry:
    address: Nacos://127.0.0.1:8848
```
画面 11：
```yaml
file-extension: yaml
namespace: f5ec3c1-4f05-40cd-964a-8444742ab4
group: SHANJUPAY_GROUP # Spring Boot 业务分组
ext-config:
  refresh: true
  data-id: spring-boot-http.yaml # Spring Boot http配置
  group: SHANJUPAY_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-starter-druid.yaml # Spring Boot starter druid配置
  group: COMMON_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-mybatis-plus.yaml # Spring Boot mybatis-plus配置
  group: COMMON_GROUP # 通用配置组
dubbo:
  scan: # dubbo 服务扫描包
    base-packages: com.shanjupay
  protocol:
    name: dubbo
    port: 20880
  registry:
    address: Nacos://127.0.0.1:8848
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：PPT 标题为“1.7 工程测试”，子标题“1.7.1 生成代码”，内容为“通过一个案例‘根据id查询商户’的开发去熟悉项目架构的基本开发方法”。
画面 8：Nacos 配置管理页面，显示“删除配置成功”，配置 ID 为 `merchant-Service`，分组为 `SHANJUPAY_GROUP`。
画面 12：Nacos 配置管理页面，显示配置列表，包括 `spring-boot-http.yaml`、`merchant-application.yaml`、`spring-boot-starter-druid.yaml`、`merchant-Service.yaml` 和 `spring-boot-mybatis-plus.yaml`。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

