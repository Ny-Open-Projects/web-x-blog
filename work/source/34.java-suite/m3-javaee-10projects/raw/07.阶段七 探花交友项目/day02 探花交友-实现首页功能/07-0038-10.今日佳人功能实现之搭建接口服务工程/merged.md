# 10.今日佳人功能实现之搭建接口服务工程

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\10.今日佳人功能实现之搭建接口服务工程_【海量资源尽在 666java.com】.mp4
- 时长 8分5秒（音频 480s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来搭建我们的接口服务的工程那么在前面呢我们这个图中呢我们其实知道啊那么我们刚刚呢是不是已经完成的是我们double这个服务的一个编写然后呢我们现在是不是还没有做这一块对吧然后呢给这个前端系统去提供一个接口这样的一个服务所以说呢接下来呢我们将去创建这个工程然后呢在这个工程中呢去做接口服务的一个完成
[00:28] 那么要注意的是呢那么在后续我们的开发过程中啊那么我们都会针对于前端这个系统去访问我们的接口服务呢都定义到这个里面来啊统一去做一个管理那么下面我们来创建一下这个工程那么这个工程的名字呢我们就叫这个碳化这个server啊然后呢我们就直接来做一个创建吧
[00:52] 然后呢我们来看一下在我们这个下面呢我们再来创建一个module然后呢下一步啊这个artifact id又叫什么呢my-tank-server然后呢这个呢就ok点击下一步到这然后呢点击这个finish完成
[01:12] 那么到这里呢这个工程呢就创建好了接下来呢我们需要导入一些这个依赖那么这样我们把这个依赖呢先导入过来然后呢我们再去一一呢去看一下它的一些导入的依赖有哪些依赖啊有没有我们一些陌生的需要给大家讲一下的一些依赖啊那么如果是比较熟悉的依赖呢我们就不讲了啊然后呢我们来看一下啊这个位置呢所导入的是interface啊这个应该改成什么呢麦炭花
[01:40] 这样的话就对了对吧1.0这样的一个版本那么在这个位置呢我们去导入依赖的时候呢要把这个MongoDB这个的要排除掉那么为什么要把它排除掉呢原因是我们在我们这个工程中是不是就是我们这个这个serve这个工程中其实我们并不需要并不需要它那么我们把它排除掉然后呢下面的这个呢是都是一些标准的一些这种依赖了就不重复了这个呢是我们
[02:09] SpringDate对Redis的一个支持这样的一个依赖那么下面是Double的一些Spring Boot的支持等等这个就不说了然后一些工具包的一些依赖Commons浪包然后还有MyBetis以及MyBetis的插件然后还有MyBetis Plus
[02:34] 然后它的一个spin boot的一个支持然后下面这个是mycircle的一个驱动那么为什么我们要导入一些mybatties相关的一些依赖呢原因是在我们这个工程中它会访问我们的数据库所以说我们会导入这样的一个依赖好那么这个依赖我们就已经搞定了那么如果说后面我们觉得这个在开发的过程中如果
[03:00] 有一些没有导的依赖我们再去增加就可以了好那么下面我们来看一下我们的一个application properties这样的一个配置文件那么这个呢是spin boot的一个标准的一个配置文件那么我们在这个里面去编写一下这个配置文件然后呢我们把这个配置项呢就拷贝过来那我们来看一下这个里面的一些内容啊那么首先呢可以看到啊上面的
[03:26] 这个是我们的服务的应用然后以及这个服务的端口是18081那么要注意跟我们之前的SSO要区分开来那么SSO它是18080对吧我们这个要设置为18081两个不能一样如果要是相同的话那么就服务跑不起来了
[03:47] ok 那么下面的这个呢是我们的这个数据库的连接的这个信息啊这个呢也是ok的没有问题然后呢下面的这个是我们的一些买杯的意思的一些这个配置啊那么他呢有需要一些这个包啊那么这个包呢一会我们来创建吧那么这个指定他的表的前缀啊然后呢一些id的一些这个自增长的一些这种策略啊等等然后呢下面的这个呢是我们double的一些这个
[04:12] 服务的地址其实主要配置的是我们的注册中心的地址然后就可以去找到我们的一些所在我们的double中所去发布的一些我们这个服务然后去做一些远程的一些RPC的调用
[04:28] 然后下面的这两个是干嘛的呢这样我们先把这两个就我们先不讲它吧这个我们先注释掉吧到我们后面用的时候我们再来给大家来说一下这两个的一些个参数OK好那么这个全局的一个配置我们就先讲到这里那么下面我们来看一下我们的这个server的一个application就是我们这个spin boot它的一个启动类
[04:58] 我们先来创建一个包创建一个包那么我们先来创建在这创建一个我们的packager创建一个包然后我们把这个就拷贝过来这是一个非常标准的一个启动类然后在这我们设置了一些扫描包当然我们也可以把它就直接可以创建出来对吧把这个包就创建出来
[05:25] 那么可以看到这个包呢就OK了对吧好嘞好那么接着继续往下面看那么下面呢我们来写一些我们基础性的一些这种代码比如说呢我们把这个resttemplate这个去先写出来那么我们为什么要去使用这个resttemplate呢大家可以去回想一下就是那么在我们之前啊所写的这个SSO中呢是不是提供了一个
[05:51] 我们的一个rest这样的一个接口的服务就是根据我们的一个这个token呢来查询这个用户的一个信息那么我们是不是在我们这个server中呢也是需要通过这个token去做一个查询的需要调用啊也就是说这个系统需要调用它的一个什么呢rest4这样的一个这个接口那么去查询这个数据所以说呢我们需要有一个什么resttemplate这样的一个配置啊所以我们把这个配置呢先写出来
[06:19] 然后我们需要创建一个config的包那么这个包下面我们会配置一系列的节配置当然了我们首先配置的第一个就是我们rest template一个config那我们可以大致的来浏览一下它就是首先我们写一个类叫做rest template configure把它定义为是一个configuration然后下面有两个bin那么一个就是我们的
[06:47] 定一个restrest template做这样的一个定义然后在这个位置我们去设置什么设置我们的一个message converter就是消息处理器然后消息转化器应该叫做设置为它的编码是UTF-8因为它默认的是使用ISO8859-1那么我们那个是不支持中文的所以要把它设置为UTF-8
[07:13] 然后呢下面的这个呢我们去设置我们的一个这个facture就是我们的一个这个工程啊然后呢主要设置的有两个这个参数啊一个就是我们的读取的一个超时时间和我们去连接的一个超时时间啊这两个我们要要设置的参数啊如果不设置的话就会出现一种这个卡顿啊一直去等待这个服务响应啊会出现这样的一个bug啊这样的一个情况那么其实啊到这里呢我们这个基础性的一些这个
[07:42] 工程呢就搭建完成了那我们就后续呢就可以在这个基础之上呢去完成我们的一些这个功能了OK好那么关于我们这个服务啊就是我们这个探花这个server这个服务的这个工程呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 Dubbo 的推荐系统服务端开发流程，包括项目结构、依赖配置、服务注册与配置文件设置，以及核心业务逻辑实现。

2) 按时间顺序列出每张画面的要点：
画面1: 展示系统架构图，前端（移动端）通过后台系统调用服务系统（dubbo完成服务调用），服务系统连接 MongoDB。
画面2: 在 IntelliJ IDEA 中创建新模块，选择父模块为 cn.itcast.tanhu，ArtifactId 为 my-tanhu-dubbo，版本为 1.0-SNAPSHOT。
画面3: 展示 pom.xml 文件中的依赖部分，包含 zkclient、commons-lang3、mybatis-plus、mysql-connector-java 等依赖。
画面4: 展示 pom.xml 文件中对 spring-boot-starter-data-mongodb 的排除配置。
画面5: 展示 pom.xml 文件中添加 dubbo-spring-boot-starter 和 dubbo 依赖，版本分别为 0.2.0 和 2.6.4。
画面6: 展示 pom.xml 文件中对 mysql-connector-java 依赖的配置。
画面7: 展示 application.properties 文件中配置 dubbo.registry.address 和 dubbo.registry.client。
画面8: 展示 application.properties 文件中配置 tanhua.sso.url 和 tanhua.sso.default.user。
画面9: 展示 application.properties 文件中配置 dubbo.registry.address 和 dubbo.registry.client。
画面10: 展示 application.properties 文件中配置 tanhua.sso.url 和 tanhua.sso.default.user。
画面11: 在 IntelliJ IDEA 中右键点击 src/main/java 目录，选择新建类。
画面12: 在 IntelliJ IDEA 中右键点击 com.tanhu.server 包，选择新建类 ServerApplication。
画面13: 展示 RestTemplateConfig.java 文件，配置 RestTemplate 和 ClientHttpRequestFactory。
画面14: 展示 RecommendUserApiImpl.java 文件，实现 queryPageInfo 方法，使用 Criteria 和 mongoTemplate 查询数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```
Add as module to cn.itcast.tanhu.my-tanhu 1.0-SNAPS
GroupId: cn.itcast.tanhu
ArtifactId: my-tanhu-dubbo
Version: 1.0-SNAPSHOT
```

画面3:
```xml
<dependency>
    <artifactId>zkclient</artifactId>
    <version>0.1c</version>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
</dependency>
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus</artifactId>
    <version>${mybatis.mybatis-plus}</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

画面4:
```xml
<dependency>
    <groupId>cn.itcast.tanhu</groupId>
    <artifactId>my-tanhu-dubbo-interface</artifactId>
    <version>1.0-SNAPSHOT</version>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面5:
```xml
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>dubbo-spring-boot-starter</artifactId>
    <version>0.2.0</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dubbo</artifactId>
    <version>2.6.4</version>
</dependency>
<dependency>
    <groupId>org.apache.ZooKeeper</groupId>
    <artifactId>ZooKeeper</artifactId>
</dependency>
```

画面6:
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

画面7:
```properties
spring.application.name=itcast-tanhu-server
server.port=10081
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/tanhu?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true&useSSL=false
spring.datasource.username=root
spring.datasource.password=root

# 数据库相关
mybatis-plus.type-enums-package=com.tanhu.server.enums
mybatis-plus.global-config.db-config.table-prefix=tb_
# id策略为自增长
mybatis-plus.global-config.db-config.id-type-auto

dubbo.application.name=itcast-tanhu-server
dubbo.registry.address=ZooKeeper://192.168.31.81:2181
dubbo.registry.client=zkclient
```

画面8:
```properties
tanhu.sso.url=http://127.0.0.1:18080
#默认今日佳人推荐用户
tanhu.sso.default.user=2
```

画面9:
```properties
dubbo.application.name=itcast-tanhu-server
dubbo.registry.address=ZooKeeper://192.168.31.81:2181
dubbo.registry.client=zkclient
```

画面10:
```properties
tanhu.sso.url=http://127.0.0.1:18080
#默认今日佳人推荐用户
tanhu.sso.default.user=2
```

画面11:
```
//设置Mapper接口的扫描包
```

画面12:
```java
@SpringBootApplication
public class ServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ServerApplication.class, args);
    }
}
```

画面13:
```java
@Configuration
public class RestTemplateConfig {

    @Bean
    RestTemplate restTemplate(ClientHttpRequestFactory factory) {
        RestTemplate restTemplate = new RestTemplate(factory);
        // 支持中文编码
        restTemplate.getMessageConverters().set(1, new StringHttpMessageConverter(Charset.forName("UTF-8")));
        return restTemplate;
    }

    @Bean
    public ClientHttpRequestFactory simpleClientHttpRequestFactory() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setReadTimeout(5000); // 单位为ms
        factory.setConnectTimeout(5000); // 单位为ms
        return factory;
    }
}
```

画面14:
```java
@Override
public PageInfo<RecommendUser> queryPageInfo(Long userId, Integer pageNum, Integer pageSize) {
    Criteria criteria = Criteria.where("toUserId").is(userId);
    Pageable pageable = PageRequest.of(pageNum - 1, pageSize, Sort.by(Sort.Direction.DESC, "id"));
    Query query = Query.query(criteria);
    List<RecommendUser> recommendUsers = this.mongoTemplate.find(query, RecommendUser.class);
    // 说明：数据包条数，暂时不提供，如果需要的话再提供
    return new PageInfo<>(total, pageNum, pageSize, recommendUsers);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: 架构图，前端（移动端）指向后台系统，后台系统指向服务系统，服务系统指向 MongoDB。
画面7: PPT 标题为“2.4.2. application.properties”，内容为配置文件说明。
画面8: PPT 标题为“2.4.2. application.properties”，内容为配置文件说明。
画面9: PPT 标题为“2.4.2. application.properties”，内容为配置文件说明。
画面10: PPT 标题为“2.4.2. application.properties”，内容为配置文件说明。

5) 不要评价画面美观，不要输出与课程无关的内容。

