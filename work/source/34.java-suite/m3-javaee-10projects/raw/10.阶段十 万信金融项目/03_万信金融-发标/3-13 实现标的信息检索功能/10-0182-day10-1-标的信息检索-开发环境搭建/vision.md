# 画面线理解：day10-1-标的信息检索-开发环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-1-标的信息检索-开发环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 02:05, 02:45, 03:35, 04:04, 04:38, 05:42, 05:56, 06:50, 08:15, 08:57, 09:47, 10:22, 10:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:15:02

1) 这一组画面整体在讲如何通过 Logstash 解决 MySQL 数据库与 ES 引擎之间的数据同步问题，并展示相关代码配置实现。

2) 按时间顺序列出每张画面的要点：
画面1: 展示技术方案 PPT，内容为解决 MySQL 与 ES 数据同步问题，使用 Logstash 作为实时数据采集引擎，图示前端→交易中心微服务→MySQL 数据库→Logstash→ES 引擎的流程。
画面2: 显示项目 pom.xml 文件，添加了 spring-boot-starter-logstash、spring-boot-configuration-processor、apollo-client、elasticsearch 依赖。
画面3: 显示 application.yml 配置文件，配置了 Apollo 的 bootstrap 信息，包括 namespaces 和 logging.config。
画面4: 显示 ElasticsearchConfig.java 文件，定义了 @Configuration 和 @Value("${wanningzp.es.host}") 注解。
画面5: 显示 ProjectIndexDTO.java 文件，定义了项目索引实体类，包含 id、consumerId、userNo、projectNo、name 等字段。
画面6: 显示 ElasticsearchConfig.java 文件，展示 @Value("${wanningzp.es.host}") 注解和 RestHighLevelClient 的构造方法。
画面7: 展示 PPT 页面，内容为“改变中国IT教育，我们正在行动”，下方有“application”和“micro_service.spring-boot-http”等配置项。
画面8: 展示 PPT 页面，内容为“application”和“micro_service.spring-boot-http”等配置项，下方表格显示 swagger.enable=true 和 spring.mvc.throw-exception-if-no-handler-found=true。
画面9: 显示 Apollo 配置中心页面，配置了 wanningzp.es.host 为 127.0.0.1:9200，以及 wanningzp.es.index 为 wanningzp_project。
画面10: 显示 ElasticsearchConfig.java 文件，展示 @Value("${wanningzp.es.host}") 注解。
画面11: 显示 ElasticsearchConfig.java 文件，展示 @Value("${wanningzp.es.host}") 注解。
画面12: 显示项目结构，选中了 DiscoveryServer，准备运行。
画面13: 显示控制台日志，显示 Spring Boot 启动过程，包括 SERVER_PORT 设置、环境变量、配置加载失败等信息。
画面14: 显示控制台日志，显示 Spring Boot 启动过程，包括 SERVER_PORT 设置、环境变量、配置加载失败等信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-logstash</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>

<dependency>
    <groupId>com.ctrip.framework.apollo</groupId>
    <artifactId>apollo-client</artifactId>
</dependency>

<dependency>
    <groupId>org.elasticsearch</groupId>
    <artifactId>elasticsearch</artifactId>
    <version>7.2.0</version>
</dependency>
```

画面3:
```yaml
app:
  id: content-search-service
  apollo:
    bootstrap:
      enabled: true
      # eagerload:
      #   enabled: true
    namespaces: application,micro_service,spring-boot-http,micro_service,spring-eureka,micro_service,spring-cloud-feign
spring:
  application:
    name: content-search-service
  logging:
    config: classpath:log4j2-dev.xml
```

画面4:
```java
package cn.itcast.wanningzp.search.config;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ElasticsearchConfig {

    @Value("${wanningzp.es.host}")
    private String es_host;

    @Bean
    public RestHighLevelClient restHighLevelClient() {
        //创建RestHighLevelClient客户端
        String ip = es_host.split(":")[0];
        int port = Integer.parseInt(es_host.split(":")[1]);
        HttpHost httpHost = new HttpHost(ip, port);
        return new RestHighLevelClient(RestClient.builder(httpHost));
    }
}
```

画面5:
```java
public class ProjectIndexDTO {

    @ApiModelProperty(value = "标的索引信息")
    @TableId
    private Long id;

    @ApiModelProperty(value = "发标人标识")
    private Long consumerId;

    @ApiModelProperty(value = "发标人用户No")
    private String userNo;

    @ApiModelProperty(value = "标的编码")
    private String projectNo;

    @ApiModelProperty(value = "标的名称")
    private String name;
}
```

画面6:
```java
@Configuration
public class ElasticsearchConfig {

    @Value("${wanningzp.es.host}")
    private String es_host;

    @Bean
    public RestHighLevelClient restHighLevelClient() {
        //创建RestHighLevelClient客户端
        String ip = es_host.split(":")[0];
        int port = Integer.parseInt(es_host.split(":")[1]);
        HttpHost httpHost = new HttpHost(ip, port);
        return new RestHighLevelClient(RestClient.builder(httpHost));
    }
}
```

画面8:
```yaml
swagger.enable = true
spring.mvc.throw-exception-if-no-handler-found = true
```

画面9:
```yaml
Key | Value
wanningzp.es.host | 127.0.0.1:9200
wanningzp.es.index | wanningzp_project
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: 标题为“4.2 技术方案”，图示前端→交易中心微服务→MySQL 数据库→Logstash→ES 引擎。
画面7: 标题为“改变中国IT教育，我们正在行动”，下方有“application”和“micro_service.spring-boot-http”等配置项。
画面8: 标题为“application”和“micro_service.spring-boot-http”等配置项，下方表格显示 swagger.enable=true 和 spring.mvc.throw-exception-if-no-handler-found=true。
画面9: 标题为 Apollo 配置中心页面，配置了 wanningzp.es.host 为 127.0.0.1:9200，以及 wanningzp.es.index 为 wanningzp_project。

5) 无
