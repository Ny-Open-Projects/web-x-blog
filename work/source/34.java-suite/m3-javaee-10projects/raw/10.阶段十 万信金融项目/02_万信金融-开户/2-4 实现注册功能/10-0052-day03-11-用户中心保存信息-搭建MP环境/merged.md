# day03-11-用户中心保存信息-搭建MP环境

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-11-用户中心保存信息-搭建MP环境_【海量资源尽在 666java.com】.mp4
- 时长 7分49秒（音频 464s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好接口呢现在已经定音好定音好之后呢咱接下来就该进行什么呀功能实现对吧但这块呢大家不要着急因为这里边是不是涉及到数据库操作那我们现在这个consumer这个wifu这边具备mybattlesplus的环境吗大家想一下这个事具备吗不具备啊咱现在这个consumer Service里边从来没有进行过什么呀数据库操作所以说这里边连mybattlesplus的环境都还没有
[00:30] 咱之前的这个数据操作都发生在什么地方对阿克汉的这边所以接下来你在实现功能的时候呢首先要在consumer当中把MP的环境先干什么呀对先给它搭起来再说那具体怎么搭呢如果你有印象你就可以自己搭如果没印象的话你可以参考这个章节因为咱当时是在这个章节讲的MP嘛就这个地方这不是入门吧对不对
[00:56] 这里边给大家详细的讲解了怎么搭环境我们首先一定是从什么呀POM键开始的对不对那咱参考这个啊在Consumer这个微幅里边把MP的环境给它先搭起来再说首先是不是POM键里边要引MP相关的依赖对吧那咱就从Aucana里边把这个代码粘过来就行了咱找一找应该是从这开始是吧从这当然了还有数据库的这个驱动啊这是一起的咱全部粘过来
[01:29] 然后呢我们就粘到什么地方我们过一边看这里边有没有加加过这些东西啊应该是没有了大概除以没有吧你看我们过了一遍没有是吧那我们就加到这个地方就行了这是依赖我们有了依赖有了之后接下来呢依赖有了之后接下来我们往下看哎需要修改Apollo上的环境了在Apollo当中我们是有两个地方需要进行修改
[02:04] 这两个你还有印象吗一个是扫描那个实体类的起边铭一个是那个map那个那个那个路径对不对那咱接下来就找到Apollo去哪配啊去consumer里边对不对consumer当然了你可以参考一下这个谁啊我打开两份吗这样子方便好现在已经打开了打开之后呢咱找一找这个相关的page就是mp相关的那自然是在这儿对不对
[02:48] MP相关的配置就是数据库吧相关的我们多打开看看当时咱应该是这个地方改是不是哎这是不是正好就不用改因为他那个恐卖那个默认配置里边这正好写的是consumer对不对那这就不用改刚刚好能用啊这需要改吗这咱看咱当时改的是什么啊咱尽量整个项目都保持一致呃不要这个各自为战看这里啊他应该改了
[03:19] 是不是他是把那一层给去掉了吗哎什么那一层去其实咱这个地方如果你都想去掉的话其实我觉得还不如改一下那个通用工厂啊口袜里边全部改啊那咱其他地方是不是都不用改了对不对这个下你自己改吧啊我就在这直接修改一下把它覆盖掉的了就把这一层保持一致就行了提交然后我们还要发布一下对不对要不然这个修改就不效了
[03:54] 这mp其实需要修改的也就这么点那接下来我们还要顺便检查跟数据库相关比如说导主一对不对这个数据库链接那这个地方我们也不用改了因为当时那个通用模板里边都是以consumer为例的嘛这个不用改还有哪没了吧应该找找啊rocky的mq我们暂时用不到mp那应该就是没了啊应该就是没了我们看看都录音那应该就是没了
[04:26] 那我们这基本上也没改啥东西就改了一个地方对不对就改了一个这个map这个扫描路径其他的基本上采用默认配置就可以了那还有一点需要注意的就是在启动内上需要加这么一个配置呃map接口的那个扫描我们找到consumer啊就是用户中心找到他的这个启动内这个对吧然后咱看这上面有这个注解吗没有吧那我们就把它给粘过来
[05:00] 粘过来之后呢这里边大家一定要注意一个细节这个地方可不能是什么呀Count要改成什么呀对要改成Consumer这就是我们平时敲代码的时候给大家说的你粘代码可以啊但是粘代码很容易是不是产生后遗症就粘完之后运行发现包错了为啥包错了就是大家遇到这种问题啊你粘过来代码之后一定要想一想这个代码是不是有些地方需要做什么呀对做修改啊所以说呢这就是一个细心的一个活吧
[05:30] 这是我们把这个注解们就加上了啊那这个准备工作做完之后还有什么别的准备工作要做吗那我们先来看看讲义对不对呃那我们这里边呢还有一个准备工作就是这边还有一个实体类是不是啊这是我们当时用的account实体类对不对那这次呢咱就不是account了应该是谁啊应该是consumer对不对consumer大家看这
[05:55] 我们也需要新建一个实体那大家知道呢这个实体的一般都跟某个表是有这个什么呀对这个对应关系啊或者说映射关系的那我们这个实体类consumer对应的表呢就是这个consumer这个表那么这个呢大家可以在这个数据库里边我们可以找一下来咱找一找啊给大家说说是哪个表就这个表就这个表这里边呢有很多这个什么呀
[06:24] 自断这个大家下去可以自己熟悉一下但是你看我们的实体内也行这个实体内你自己敲一遍也可以当然我们这也提供的有现成的你也可以直接拿着用大家看一下这里边的注解他还有印象吗这是不是浪不可的注解这个对的注解能起到什么作用他是不是可以帮我们自动生成给他三个方法对不对那然后下面这个at table内幕是不是用来设置这个类跟哪个表对应的包括下面这是不设置这个主件以及他的生成方式的
[06:53] 然后下面这个table field是不是设置哪个属性跟表里边的哪个字段进行什么呀对进行对应的这个大家下去可以自己看一下那这个类呢我也给大家提供好了在这个资料文件夹里边公共类里边大家看是他吧就是他然后你control c给他粘贴到哪个地方呢粘贴到这个entity这个包里边就行了我这里边都已经粘贴过了让他还看一下没错吧这是一个我们说这个我们要用到的一个什么呀
[07:24] 对实体类一定要注意它跟这个consumer这个表是映射关系这是目前吧我们就把相关的两个准备工作给搞定了一个是什么呀这个MP的环境一个是什么呀一个是这个实体类对吧那咱一会儿呢就可以实现功能

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务架构中，通过 Apollo 配置中心为消费者服务（consumer-Service）配置数据库连接信息，并展示相关代码和配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了在万向2p-api 工程中定义 ConsumerApi 接口，其中包含 register 方法。
- 代码：public interface ConsumerApi { /* 用户注册 */ @param consumerRegisterDTO @return } RestResponse register(ConsumerRegisterDTO consumerRegisterDTO);
- 同时展示了在 ConsumerController 中实现 register 方法的代码：
@ApiOperation("用户注册") @ApiImplicitParam(name = "consumerRegisterDTO", value = "用户注册", required = true, dataType = "AccountRegisterDTO", paramType = "body") @PostMapping(value = "/consumers") public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {

画面 2：
- 展示了在万向2p-account-Service 工程中定义 checkMobile 方法。
- 代码：
RestResponse<Integer> checkMobile(String mobile, String key, String code);
@ApiOperation("校验手机号和验证码") @ApiImplicitParams({@ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String"), @ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")}) @GetMapping("/mobiles/{mobile}/key/{key}/code/{code}") @Override public RestResponse<Integer> checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {

画面 3：
- 展示了万向2p-consumer-Service 的 pom.xml 文件内容，其中包含多个依赖项。
- 代码：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 4：
- 展示了万向2p-consumer-Service 的 pom.xml 文件内容，其中包含 Spring Cloud 的依赖。
- 代码：
<dependency> <groupId>org.springframework.cloud</groupId> <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-test</artifactId> <scope>test</scope> </dependency>

画面 5：
- 展示了万向2p-consumer-Service 的 pom.xml 文件内容，其中包含 MyBatis Plus 和 Druid 的依赖。
- 代码：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 6：
- 展示了 Apollo 配置中心的登录页面，地址为 localhost:8070/config.html#/?appId=consumer-Service。
- 页面为空白，等待加载。

画面 7：
- 展示了 Apollo 配置中心的界面，当前选中的是 account-Service 项目。
- 页面显示了多个配置项，如 micro_service.spring-boot-http、micro_service.spring-Eureka 等。

画面 8：
- 展示了 Apollo 配置中心中 consumer-Service 项目的配置页面。
- 页面显示了多个配置项，如 mybatis-plus.Mapper-locations、mybatis-plus.typeAliasesPackage 等。

画面 9：
- 展示了 Apollo 配置中心中 consumer-Service 项目的配置页面。
- 页面显示了 micro_service.mybatis-plus 配置项下的数据库连接信息。
- 代码：
spring.datasource.url jdbc:mysql://localhost:3306/pz_consumer?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=UTC
spring.datasource.driver-class-name com.mysql.cj.jdbc.Driver
spring.datasource.username root
spring.datasource.password 123456

画面 10：
- 展示了 Apollo 配置中心的界面，当前选中的是 consumer-Service 项目。
- 页面显示了多个配置项，如 micro_service.spring-boot-http、micro_service.spring-Eureka 等。

画面 11：
- 展示了万向2p-consumer-Service 项目的结构，其中包含了 ConsumerService 类。
- 代码：
package cn.itecast.wanxing2p.consumer; @SpringBootApplication @EnableDiscoveryClient @EnableFeignClients(basePackages = "cn.itecast.wanxing2p.consumer.agent") public class ConsumerService { public static void main(String[] args) { SpringApplication.run(ConsumerService.class, args); } }

画面 12：
- 展示了 SQLyog Professional 64 的界面，用于数据库操作。
- 页面为空白，等待输入。

画面 13：
- 展示了万向2p-api 工程中 Consumer 实体类的代码。
- 代码：
private String userNo; /* 用户编号，生成唯一，用户在容器系统标识 */ private String mobile; /* 平台预留手机号 */ private String userType; /* 用户类型，个人or企业，预留 */ private String role; /* 用户角色，借款人or投资人 */

画面 14：
- 展示了万向2p-consumer-Service 项目的 Consumer 实体类代码。
- 代码：
/* 用户编号，生成唯一，用户在容器系统标识 */ private String userNo; /* 平台预留手机号 */ private String mobile; /* 用户类型，个人or企业，预留 */ private String userType; /* 用户角色，借款人or投资人 */ private String role; /* @TableField("USER_NO") */ /* @TableField("MOBILE") */ /* @TableField("USER_TYPE") */ /* @TableField("ROLE") */

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
public interface ConsumerApi { /* 用户注册 */ @param consumerRegisterDTO @return } RestResponse register(ConsumerRegisterDTO consumerRegisterDTO);
@ApiOperation("用户注册") @ApiImplicitParam(name = "consumerRegisterDTO", value = "用户注册", required = true, dataType = "AccountRegisterDTO", paramType = "body") @PostMapping(value = "/consumers") public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {

画面 2：
RestResponse<Integer> checkMobile(String mobile, String key, String code);
@ApiOperation("校验手机号和验证码") @ApiImplicitParams({@ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String"), @ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")}) @GetMapping("/mobiles/{mobile}/key/{key}/code/{code}") @Override public RestResponse<Integer> checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {

画面 3：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 4：
<dependency> <groupId>org.springframework.cloud</groupId> <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-test</artifactId> <scope>test</scope> </dependency>

画面 5：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 6：
无代码或配置。

画面 7：
无代码或配置。

画面 8：
无代码或配置。

画面 9：
spring.datasource.url jdbc:mysql://localhost:3306/pz_consumer?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=UTC
spring.datasource.driver-class-name com.mysql.cj.jdbc.Driver
spring.datasource.username root
spring

