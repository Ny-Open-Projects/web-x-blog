# 13_通用说明_多环境配置说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\13_通用说明_多环境配置说明【海量资源尽在 666java.com】.mp4
- 时长 3分33秒（音频 213s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位下面呢咱们来说一下咱们整个项目中的一个多环境的切换那这个呢是在跟实际开发是接轨的在真正的开发的时候呢肯定的是有多个环境的需要切换比如说咱们在开发的时候有一个开发环境还测试的时候呢有一个测试环境正式上线的时候呢会有一个生产环境
[00:23] 那这样的话呢咱们的不同的环境呢它配置的东西是不太一样的所以说呢你会发现啊在咱们每一个项目下面啊基本上都有这三个文件而后期呢咱们再去创建一些微服务的时候呢同样的需要把这三个文件呢给拷贝过来然后咱们需要再再再去重新的去配置当然刚才说了每一个环境的配置方式是不太一样的啊
[00:50] 那行那咱们简单说一说啊首先呢这有个DB那DB呢这个呢是一个开发环境开发环境然后下面呢还有一个就是这块呢是一个这种正式环境也就是咱们刚才说的生产环境这里边配着一些内容OK那在咱们整个的开发阶段啊其实咱们用的最多的就是当前的一个测试环境好再说一遍啊就在当前的项目
[01:18] 跟目录下边去创建三个proprieties分别对应的是开发环境生产环境和测试环境好那这里边那它是怎么加载的呢大家学过MavenMaven里边有一个Maven profile其实呢就是在咱们当前复工程下面有一个home文件是吧里边呢咱们可以往下找找一些插件插件找一找好这个插件呢其实就在这儿这有一个Maven profile
[01:53] 那下找啊这啊这mayman profile啊profile私里边你可以配着三个profile看到了吗看到三个profile啊他的文件路径其实呢都已经指定好了分别是在根目录下边如果说你要是有一个包的话比如说我在根目录下边有一个config要是有这么一个config包的话你就这么写如果没有的话我们就这么写就可以了就说明是在目前的根目录下面他默认加在哪个呢
[02:22] 大家可以看一下这有一个什么呢Active by Defund以后默认加载的应该是当前的一个测试环境也就是咱们的目前用的最多的一个开发的环境当然在在咱们后期如果想要进行打包的时候呢咱们可以执行一些不同的命令来去找到不同的环境那这打包的命令呢其实就在这比如说package然后是
[02:48] -P这个P是大写你可以指定test provide和db这样的话就能去切换到不同的环境下面进行打包当然如果说你要不指定参数的话刚才说了默认就是指定的当前的一个测试环境也就是说它会去加载这里边的属性来去找到对应的一些东西当然你看这里边最简单的一个比如说你测试环境或者你开发环境就是一个联系的本地的主机库
[03:17] 如果说你是生产环境的话那肯定的就不是当前的logo house应该是你的某一个mycircle的服务器的地址ip对吧那行啊那这一块呢内容呢咱们这个多环境切换呢咱们这块呢就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Maven 项目中通过 profiles 配置实现多环境（开发、测试、生产）切换，重点是配置文件的管理与 pom.xml 中的 profile 定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档中关于“6.5.1 多环境切换”的说明，指出需在项目根目录下创建三个配置文件：maven_dev.properties、maven_prod.properties、maven_test.properties，并提到默认环境为 test，可通过 package -P 参数指定。
画面 2: 在 IntelliJ IDEA 中，项目结构视图显示了三个配置文件（maven_dev.properties、maven_prod.properties、maven_test.properties）位于 heima-leadnews-common 模块下。
画面 3: 编辑器中显示了 maven_prod.properties 文件内容，包含日志配置、数据库连接（URL、用户名、密码、驱动、包扫描范围）和 Eureka 服务地址。
画面 4: 编辑器中显示了 maven_test.properties 文件内容，数据库 URL 为 localhost:3306/heima_leadnews，其他配置与 prod 相同。
画面 5: 选中并高亮了 maven_test.properties 文件。
画面 6: 编辑器中显示了 pom.xml 文件的依赖部分，包含 mybatis、mybatis-spring、pagehelper-spring-boot-starter、jsoup 等依赖。
画面 7: 编辑器中显示了 pom.xml 文件的插件配置部分，包含 resources 和 testResources 插件配置，其中 filtering 设置为 true。
画面 8: 编辑器中显示了 pom.xml 文件的插件配置部分，已配置好 resources 和 testResources 插件。
画面 9: 编辑器中显示了 pom.xml 文件的 profiles 配置部分，已定义了 id 为 dev 的 profile。
画面 10: 编辑器中显示了 pom.xml 文件的 profiles 配置部分，已定义了 id 为 test 的 profile。
画面 11: 编辑器中显示了 pom.xml 文件的 profiles 配置部分，已定义了 id 为 prod 的 profile。
画面 12: 编辑器中显示了 maven_test.properties 文件内容，其中数据库 URL 为 localhost:3306/heima_leadnews，其他配置与 prod 相同。
画面 13: 编辑器中显示了 maven_test.properties 文件内容，其中数据库 URL 为 localhost:3306/heima_leadnews，其他配置与 prod 相同。
画面 14: 展示了课程文档中关于“6.5.1 多环境切换”的说明，指出需在项目根目录下创建三个配置文件：maven_dev.properties、maven_prod.properties、maven_test.properties，并提到默认环境为 test，可通过 package -P 参数指定。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```text
• InitJacksonConfig 提供自动化配置默认 ObjectMapper，让整个框架自动处理日期和id混淆
6.5 通用环境说明
6.5.1 多环境切换
在每一个微服务的工程中的根目录下创建三个文件，方便各个环境的切换
(1) maven_dev.properties
定义开发环境的配置
(2) maven_prod.properties
定义生产环境的配置
(3) maven_test.properties
定义测试环境的配置，开发阶段使用这个测试环境
默认加载的环境为test，在打包的过程中也可以指定参数打包 package -P test/prod/dev
具体配置，请查看工程下的maven插件的profiles配置
<profiles>
  <profile>
    <id>dev</id>
    <build>
      <filters>
        <filter>maven_dev.properties</filter>
      </filters>
    </build>
  </profile>
```

画面 2:
```text
heima-leadnews
├── heima-leadnews-api
├── heima-leadnews-common
├── heima-leadnews-model
├── heima-leadnews-utils
├── pom.xml
└── target
```

画面 3:
```text
# log日志配置
log.level=DEBUG
log.pattern="%d{DEFAULT} [%Thread] %-5level %msg%n"

# 本地环境配置
mysql.core.jdbc.url=jdbc:mysql://192.168.220.145:3306/itheima-news?autoReconnect=true&useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Shanghai
mysql.core.jdbc.username=root
mysql.core.jdbc.password=root
mysql.core.jdbc.driver=com.mysql.jdbc.Driver
mysql.core.root.Mapper=mappers
mysql.core.aliases.package=com.heima.model.poJos.**
mysql.core.tx.scan.package=execution(* com.heima.Service.**.*)
# admin 账户名
admin.username=admin
admin.password=admin
hostname.Eureka.server=localhost
Eureka.client.serviceUrl.defaultZone=http://localhost:8761/Eureka/
```

画面 4:
```text
# log日志配置
log.level=DEBUG
log.pattern="%d{DEFAULT} [%Thread] %-5level %msg%n"

# 本地环境配置
mysql.core.jdbc.url=jdbc:mysql://localhost:3306/heima_leadnews?autoReconnect=true&useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Shanghai
mysql.core.jdbc.username=root
mysql.core.jdbc.password=root
mysql.core.jdbc.driver=com.mysql.jdbc.Driver
mysql.core.root.Mapper=mappers
mysql.core.aliases.package=com.heima.model.poJos.**
mysql.core.tx.scan.package=execution(* com.heima.Service.**.*)
# admin 账户名
admin.username=admin
admin.password=admin
hostname.Eureka.server=localhost
Eureka.client.serviceUrl.defaultZone=http://localhost:8761/Eureka/
```

画面 6:
```xml
<dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>${mysql.version}</version>
</dependency>
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>${mybatis.version}</version>
</dependency>
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis-spring</artifactId>
  <version>${mybatis.spring.version}</version>
</dependency>
<dependency>
  <groupId>com.github.pagehelper</groupId>
  <artifactId>pagehelper-spring-boot-starter</artifactId>
  <version>${pagehelper.version}</version>
</dependency>
<dependency>
  <groupId>org.jsoup</groupId>
  <artifactId>jsoup</artifactId>
  <version>${jsoup.version}</version>
</dependency>
```

画面 7:
```xml
<plugin>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-maven-plugin</artifactId>
  <configuration>
    <source>${java.version}</source>
    <target>${java.version}</target>
  </configuration>
</plugin>
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-resources-plugin</artifactId>
  <version>3.2.0</version>
  <configuration>
    <encoding>UTF-8</encoding>
    <useDefaultDelimiters>true</useDefaultDelimiters>
    <resource>
      <directory>src/main/resources</directory>
      <includes>
        <include>**/*</include>
      </includes>
      <filtering>true</filtering>
    </resource>
    <testResource>
      <directory>src/test/resources</directory>
      <filtering>true</filtering>
    </testResource>
  </configuration>
</plugin>
```

画面 9:
```xml
<profiles>
  <profile>
    <id>dev</id>
    <build>
      <filters>
        <filter>maven_dev.properties</filter>
      </filters>
    </build>
  </profile>
```

画面 10:
```xml
<profiles>
  <profile>
    <id>test</id>
    <build>
      <filters>
        <filter>maven_test.properties</filter>
      </filters>
    </build>
  </profile>
```

画面 11:
```xml
<profiles>
  <profile>
    <id>prod</id>
    <build>
      <filters>
        <filter>maven_prod.properties</filter>
      </filters>
    </build>
  </profile>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.5 通用环境说明”，子标题为“6.5.1 多环境切换”，内容包括创建三个配置文件的说明和默认环境及打包参数的说明。
画面 14: PPT 标题为“6.5 通用环境说明”，子标题为“6.5.1 多环境切换”，内容包括创建三个配置文件的说明和默认环境及打包参数的说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

