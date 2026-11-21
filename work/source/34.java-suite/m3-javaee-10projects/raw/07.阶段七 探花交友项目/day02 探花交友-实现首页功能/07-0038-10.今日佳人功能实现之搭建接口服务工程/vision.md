# 画面线理解：10.今日佳人功能实现之搭建接口服务工程

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\10.今日佳人功能实现之搭建接口服务工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:58, 01:25, 01:45, 02:14, 02:57, 03:19, 04:30, 04:46, 05:07, 05:22, 06:23, 07:05, 07:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:24:08

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
    <groupId>org.apache.zookeeper</groupId>
    <artifactId>zookeeper</artifactId>
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
dubbo.registry.address=zookeeper://192.168.31.81:2181
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
dubbo.registry.address=zookeeper://192.168.31.81:2181
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
//设置mapper接口的扫描包
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
