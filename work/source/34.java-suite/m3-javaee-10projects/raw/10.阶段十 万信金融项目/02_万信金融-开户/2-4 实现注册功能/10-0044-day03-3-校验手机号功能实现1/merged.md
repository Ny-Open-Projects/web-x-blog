# day03-3-校验手机号功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-3-校验手机号功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 7分18秒（音频 438s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们在SMS Service当中呢已经把校验验证码的这个功能给实现了这功能实现完之后呢接下来咱要实现哪个功能呢看这儿啊接下来我们就要实现校验手机号的功能这个功能其实指的就是查一下这个手机号是否已经存在了那说白了就是涉及到数据库操作
[00:29] 具体来讲应该是数据库查询嘛对不对查查表里边这个手机号它是否已经存在了那如果已经存在的话那我们将来是不是就要直接登录了对不对如果不存在的话我们是不是得先注册然后再去进行什么呀登录所以说呢我们接下来要实现这个功能当我们实现这个功能的话大家也看到很明显要操作数据库操作数据库呢我们前面也讲过了我们是不是要用MP对吧就是MyBethes
[00:59] 而我们现在呢这个Account这个vf呢里边并不具备MP的环境所以说我们要先进行MP相关的配置先把这个环境先给它搞定然后再编码去实现校验手机号的这个功能这个环境呢咱大家看一下讲义吧你看首先是不是要先引入MP相关的依赖吧对不对你看它是有一些依赖的你看这个是
[01:29] MP跟Spring Boot的整合包对吧这是关联的一些包还有什么呀这是不是阿里巴巴的那个数据库连线池这是不是MySQL的驱动对吧相关的我们都需要有那咱就直接把它给粘过来稍等好我们粘贴一下粘到POM文件当中注意看是Account里边POM文件里边这里边这几个加包应该是没有的这环境我们大概过一遍吧应该是没有
[02:07] 反正你粘贴的时候你最好是从上往下过一遍粘过来中间这个就删掉了保存它这是有反应的对不对这个不用管它了
[02:26] 这是POM文件我们需要加的一些依赖还有什么还有一些配置是不是MP的一些配置这个配置大家要注意这个配置现在是不是都在Apollo上这我要给大家强调一下这个配置虽然咱现在是用Apollo在管理但是从理解的层面来讲它是没有变化的那些配置该怎么着还是怎么着只是位置发生变化了这个你一定要注意那咱就要去Apollo上看看有没有哪些配置咱需要调整的讲义里边其实都告诉你
[02:55] 咱去安保的里边找一找account咱从上往下过一遍看看跟数据库有关的对不对往下看找跟数据库有关的这个跟数据库有关吧数据库廉持咱看看有没有需要改的这儿是不是咱改过了以前是不是反正你要检查你的你要是没有改的话你这儿要改一改这儿要换成P2P下完线account你看你改了没有没改你就改一下还要包裹这个密码这个你自己要检查
[03:28] 其他的这个咱就不需要动了啊往下走走这个是不是MP的对不对这个我们要重点看一看的MP里边呃我先跟大家说一说MP里边像中间这些配置你不用管啊其实我们前面没怎么给大家提中间这几个配置那你要有兴趣的话可以查查文档呃这儿呢给大家说一说这几个配置其实不加也是可以的我们当时其实又讲了三个配置嘛一个是这个配置
[03:55] 就是扫描那个那个什么呀实体内那个包的可以起别名嘛对不对还有就是这个是那个全局缓存的那个开关啊我们开发期间呢把这个缓存关掉还有这个就是扫描什么呀那个Mapper映射配置文件那个路径了对不对那你看我们这几个配置有没有需要改的呀很明显这个地方是不是就需要改对吧你看他原来这写的是什么Consumer对不对那我们Occounter里边这个实体内是不是应该放到
[04:26] 应该放到哪应该是放到Account Entity是不是所以我们这要改一改啊怎么改呢把它原来的这个公共配置给它覆盖掉点这你看点击一下啊然后呢把这改成ACCUNT就可以了点击提交嗯然后呢你看这需要修改吗这个路径我们对照一下吧你看它是什么CNITCards的万行P2PCNITCards的万行P2P对吧
[04:57] 行行啊这是account那没事能匹配mappermapper有Mapper吧没错哎他下边是不是还多了一个文件夹叫xml对不对咱这没有吧那你看你要么是改这把这一层给他干什么呀去掉要么就是你这再加一层什么呀目录就是xml目录那咱这样咱改这个值吧咱改这个值覆盖一下把这一层给他去掉
[05:28] 对改成这个样子就可以了提交其他应该就不需要动了不需要动的话一定要注意要干什么要发布不发布不生效要发布一下好这就可以了MP的相关的配置然后还有哪个地方需要配的吗应该还有吧启动类了是不是你看这讲一上有你看这要改一改其实这少写一个对不对
[05:55] 是不是还有那个那个XML刚才那个路径我们也改了改你要注意的然后呢启动类上要加这个Mapper接口的一个扫描Mapper接口这个扫描大家也不要忘了这个地方我们找一找启动类就是这个启动类这加过了是不是啊这加过了好咱看看这个这个对不对啊这个路径不对啊对不对你看这个路径不对啊
[06:25] 你看咱应该是怎么写的呀cn.itcast.对这应该是万信p2p.account.map这回对了吧再检查检查cn.itcast.万信p2p没错吧.account然后.mapp到这了对不对我们将来接口是都要往这放的
[06:57] 往这放所以这个地方你一定要注意这儿也得写对了要检查检查细心一下那应该就没了吧是不是跟MP相关的这个配置一些是在Apollo上一些是在这个咱们本地该修改的该加的都已经加过了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中引入 MyBatis-Plus 依赖、配置 Apollo 配置中心的 MyBatis-Plus 相关属性，并在启动类中使用 @MapperScan 注解扫描 Mapper 接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前章节为“3.5.3 功能实现”，内容涉及“开户（注册、登录、开户）”、“会员 成为DP平台的会员/用户”、“时序图”、“注册：1. 发送并获得短信验证码 2. 保存手机号和短信验证码 3. 保存用户信息”。
画面 2: 展示 PPT 内容“2）引入MP相关的依赖”，并列出 Maven 依赖：
<dependency>
    <groupId>com.baozidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-typehandlers-jsr318</artifactId>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
</dependency>
画面 3: 展示 PPT 内容“3）修改Apollo上关于MP的配置：mybatis-plus.typeAliasesPackage”和“4）实体类”，并提示在启动类上添加 @MapperScan 注解。
画面 4: 在 IntelliJ IDEA 中打开项目 `wanning2p-account-Service` 的 `pom.xml` 文件，显示了项目的基本配置，包括父项目、版本和依赖。
画面 5: 在 IntelliJ IDEA 中，`pom.xml` 文件中高亮显示了 MyBatis-Plus 依赖，并弹出“Resolving Maven dependencies...”窗口，表示正在下载依赖。
画面 6: 打开 Apollo 配置中心的空白页面，URL 为 `localhost:8070/config.html#/appid=account-Service`。
画面 7: 在 Apollo 配置中心，显示了数据库相关的配置项，如 `spring.datasource.username` 的值为 `root`，`spring.datasource.password` 的值为 `123`。
画面 8: 在 Apollo 配置中心，显示了 MyBatis-Plus 的全局配置项，如 `mybatis-plus.global-config.db-column-underline` 的值为 `true`，`mybatis-plus.Mapper-locations` 的值为 `classpath:cn/itcast/wanning2p/Mapper/xml/*.xml`。
画面 9: 在 IntelliJ IDEA 中，`pom.xml` 文件中高亮显示了 `mybatis-plus-boot-starter` 依赖。
画面 10: 在 Apollo 配置中心，显示了 MyBatis-Plus 的配置项，鼠标悬停在 `mybatis-plus.Mapper-locations` 的值上。
画面 11: 在 IntelliJ IDEA 中，项目结构中高亮显示了 `Mapper` 包。
画面 12: 在 Apollo 配置中心，显示了 MyBatis-Plus 的配置项，页面顶部有“发布成功”的提示。
画面 13: 在 Apollo 配置中心，显示了数据库连接池相关的配置项，如 `spring.datasource.druid.web-stat-filter.enabled` 的值为 `true`，`spring.datasource.druid.web-stat-filter.session-max-count` 的值为 `1000`。
画面 14: 在 IntelliJ IDEA 中，打开 `Wanning2pAccountServiceApplication.java` 文件，显示了启动类代码，其中包含 `@MapperScan("cn.itcast.mp.Mapper")` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
<dependency>
    <groupId>com.baozidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-typehandlers-jsr318</artifactId>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
</dependency>

画面 4:
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>wanning2p</artifactId>
        <groupId>cn.itcast.wanning2p</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>wanning2p-account-Service</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>cn.itcast.wanning2p</groupId>
            <artifactId>wanning2p-api</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
        </dependency>
    </dependencies>

画面 8:
mybatis-plus.global-config.db-column-underline: true
mybatis-plus.Mapper-locations: classpath:cn/itcast/wanning2p/Mapper/xml/*.xml

画面 14:
package cn.itcast.wanning2p.account;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan;
import

