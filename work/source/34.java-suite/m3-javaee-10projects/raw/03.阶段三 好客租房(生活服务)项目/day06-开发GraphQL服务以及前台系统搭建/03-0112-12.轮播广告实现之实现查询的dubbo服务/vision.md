# 画面线理解：12.轮播广告实现之实现查询的dubbo服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\12.轮播广告实现之实现查询的dubbo服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:53, 03:05, 04:37, 05:52, 07:09, 08:43, 10:10, 11:56, 13:23, 15:17, 16:25, 17:42, 19:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:14:00

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 Dubbo 的广告管理服务的开发过程，包括项目结构、实体类、接口、服务实现、MyBatis 配置及 Dubbo 服务注册。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 IntelliJ IDEA 中的项目结构，当前选中模块为 `itcast-haoke-manage-dubbo-server`。
- 显示 `pom.xml` 文件内容，包含父模块信息和依赖配置：
  ```xml
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <parent>
      <artifactId>itcast-haoke-manage</artifactId>
      <groupId>cn.itcast.haoke.manage</groupId>
      <version>1.0-SNAPSHOT</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>itcast-haoke-manage-dubbo-server</artifactId>
  <packaging>pom</packaging>
  <modules>
      <module>itcast-haoke-manage-dubbo-server-house-resources</module>
      <module>itcast-haoke-manage-dubbo-server-generator</module>
      <module>itcast-haoke-manage-dubbo-server-common</module>
  </modules>
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter</artifactId>
      </dependency>
  </dependencies>
  ```

画面 2：
- 选中 `itcast-haoke-manage-dubbo-server-ad-interface` 模块。
- 显示该模块的 `pom.xml` 文件内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <parent>
          <artifactId>itcast-haoke-manage-dubbo-server-ad</artifactId>
          <groupId>cn.itcast.haoke.manage</groupId>
          <version>1.0-SNAPSHOT</version>
      </parent>
      <modelVersion>4.0.0</modelVersion>
      <artifactId>itcast-haoke-manage-dubbo-server-ad-interface</artifactId>
  </project>
  ```

画面 3：
- 显示 PDF 文档《讲义.pdf》的第 24 页，内容为 `Ad` 实体类的 Java 代码。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.pojo;
  import com.baomidou.mybatisplus.annotation.IdType;
  import com.baomidou.mybatisplus.annotation.TableId;
  import com.baomidou.mybatisplus.annotation.TableName;
  import lombok.Data;
  import lombok.experimental.Accessors;
  @Data
  @Accessors(chain = true)
  @TableName("tb_ad")
  public class Ad extends BasePojo {
      @TableId(value = "id", type = IdType.AUTO)
      private long id;
      //广告类型
      private Integer type;
      //描述
      private String title;
      //图片URL地址
      private String url;
  }
  ```

画面 4：
- 显示 `Ad.java` 文件内容，与画面 3 代码一致，但注释更完整。

画面 5：
- 显示 `PageInfo` 类的 Java 代码，位于 `itcast-haoke-manage-dubbo-server-house-resources` 模块。
- 代码内容：
  ```java
  import java.util.Collections;
  import java.util.List;
  @Data
  @AllArgsConstructor
  public class PageInfo<T> implements java.io.Serializable {
      private static final long serialVersionUID = -2105385778778117877L;
      //总条数
      private Integer total;
      //当前页
      private Integer pageNum;
      //一页显示的大小
      private Integer pageSize;
  }
  ```

画面 6：
- 显示 `ApiAdService.java` 文件内容，定义了分页查询广告数据的接口。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.api;
  import cn.itcast.haoke.dubbo.server.pojo.Ad;
  import cn.itcast.haoke.dubbo.server.vo.PageInfo;
  public interface ApiAdService {
      /**
       * 分页查询广告数据
       */
      PageInfo<Ad> queryAdList(Integer type, Integer page, Integer pageSize);
  }
  ```

画面 7：
- 显示 `AdServiceImpl.java` 文件，正在编写实现类。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.service.impl;
  public class AdServiceImpl extends BaseServiceImpl<Ad> {
  ```

画面 8：
- 显示 `AdServiceImpl.java` 文件，正在编写 `queryAdList` 方法。
- 代码内容：
  ```java
  import cn.itcast.haoke.dubbo.server.service.BaseServiceImpl;
  import cn.itcast.haoke.dubbo.server.vo.PageInfo;
  import javax.management.Query;
  public class AdServiceImpl extends BaseServiceImpl<Ad> implements AdService {
      @Override
      public PageInfo<Ad> queryAdList(Ad ad, Integer page, Integer pageSize) {
          Query query = new Query();
          return super.queryPageList(query, page, pageSize);
      }
  }
  ```

画面 9：
- 显示 `AdServiceImpl.java` 文件，正在使用 `QueryWrapper`。
- 代码内容：
  ```java
  import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
  QueryWrapper<Ad> queryWrapper = new QueryWrapper<>();
  return super.queryPageList(queryWrapper, page, pageSize);
  ```

画面 10：
- 显示 PDF 文档《讲义.pdf》的第 25 页，内容为“3.3.8、创建AdMapper接口”。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.mapper;
  import cn.itcast.haoke.dubbo.server.pojo.Ad;
  import com.baomidou.mybatisplus.core.mapper.BaseMapper;
  public interface AdMapper extends BaseMapper<Ad> {
  }
  ```

画面 11：
- 显示 `MybatisConfig.java` 文件，正在创建 `PaginationInterceptor`。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.config;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.context.annotation.Bean;
  @Configuration
  public class MybatisConfig {
      @Bean
      public PaginationInterceptor paginationInterceptor() {
          return new PaginationInterceptor();
      }
  }
  ```

画面 12：
- 显示 `application.properties` 文件内容，配置 Dubbo 服务。
- 代码内容：
  ```properties
  # Spring boot application
  spring.application.name = itcast-haoke-manage-dubbo-server-ad
  # 数据库
  spring.datasource.driver-class-name=com.mysql.jdbc.Driver
  spring.datasource.url=jdbc:mysql://172.16.55.185:3306/haoke?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&maxReconnects=10
  spring.datasource.username=root
  spring.datasource.password=root
  # 服务的扫描包
  dubbo.scan.basePackages = cn.itcast.haoke.dubbo.server.api
  # 应用名称
  dubbo.application.name = dubbo-provider-ad
  # 协议及端口
  dubbo.protocol.name = dubbo
  dubbo.protocol.port = 21880
  # zk注册中心
  dubbo.registry.address = zookeeper://172.16.55.185:2181
  dubbo.registry.client = zkclient
  ```

画面 13：
- 显示 `AdDubboProvider.java` 文件内容，启动 Dubbo 服务。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  @SpringBootApplication
  public class AdDubboProvider {
      public static void main(String[] args) {
          new SpringApplicationBuilder(AdDubboProvider.class)
                  .web(WebApplicationType.NONE) // Web 服务类型
                  .run(args);
      }
  }
  ```

画面 14：
- 显示 PDF 文档《讲义.pdf》的第 4 页，内容为“3.3. 实现查询接口（dubbo服务）”。
- 代码内容：
  ```markdown
  3.3.1、分析
  - 首页的轮播广告，属于网站广告，不能只是开发一个功能而是要开发全站广告功能
  - 实现独立的dubbo服务，便于后期的扩展和维护
  3.3.2、创建common工程
  创建itcast-haoke-manage-dubbo-server-common工程，将BasePojo、BaseServiceImpl移动至
