# 11-用户服务开发准备（服务启动类、配置类） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们用户服务的开发准备,刚才呢,我们是把配置文件都已经配置好了,那接下来呢,还有一个服务启动类的吧,服务启动类呢,我们直接来把这个包先来创建一下,还是看IT黑码品达,对吧,这个包结构是一致的,在咱们这个PD user下边,然后呢,我们先把这个package来创建一下,这个服务启动类呢,就叫什么呢,就叫做user application,对吧,user application,好,

在这来创建一下,user application,好,具体代码我就不再手敲了,对于我们启动类这种代码呢,咱们直接就复制过来,这些呢,大家也都见过了,supply boot application,然后呢,这个是作为我们这个discovery client,对吧,发现客户端,然后呢,这个是开启我们这个swagger,好,然后呢,直接启动就可以了,好,这是启动类,然后再往下呢,还有配置类的吧,

这个配置类呢,主要有这么两个,一个是咱们这个mybethplus,对吧,这个前面也用过了,主要使用到它的这个什么呢,分页插件,对吧,然后呢,还有一个呢,就是我们这个swagger的这个config,好,所以说呢,我们先把这个config包呢,来创建一下,然后把这两个配置类呢,咱们就直接复制过来,在这下边是不是来创建一个包,叫做config,然后在这个包下面呢,我们先来创建一个mybethplusconfig,好,代码呢,全都复制过来,

好,这个就搞定了,然后接下来呢,还有这个swagger的,对吧,因为我们需要使用到它这个swagger文档功能,所以说呢,需要把它复制过来,就叫做swaggerconfig吧,好,然后具体代码呢,也是啊,我们直接在这来复制一下,连这个也一块复制过来,那么整个这个代码呢,我们就不用再解释了,因为前面在pdbase里边了,咱们是不是都已经这个提到过了,

所以说呢,我们在这直接拿过来就可以了,主要创建的就是这个docty的对象,这样的话呢,就可以

可以

帮我们来扫描咱们指定的controller包下边所有的类了,对吧,所有的controller类,然后呢,给我们生成相应的这个api文档,好,这样的话呢,便于我们去进行这个接口的测试啊,好,那么到这儿的话呢,我们这个开发准备呢,全都已经完成了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”第3章“用户服务开发”的教学内容，主要聚焦于服务的启动配置和Swagger2 API文档的集成。讲师通过 IntelliJ IDEA 开发环境，演示了如何配置 Spring Boot 项目，包括主启动类 `UserApplication`、配置类 `MybatisPlusConfig` 用于配置 MyBatis-Plus 的分页插件，以及 `SwaggerConfig` 类用于集成 Swagger2 以自动生成和展示 API 文档。同时，视频也展示了项目结构、配置文件（如 `application.properties`）以及如何解决 Swagger2 与静态资源路径冲突的问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和 `caffeine.properties` 配置文件，介绍 `addressBook=2000, 2h` 的缓存配置。
*   **00:05 - 00:15**: 展示 `UserApplication` 启动类，讲解 `@SpringBootApplication` 注解的作用。
*   **00:15 - 00:25**: 进入“3.3 配置类”章节，展示 `MybatisPlusConfig` 配置类，用于注册 MyBatis-Plus 的分页拦截器。
*   **00:25 - 00:35**: 展示 `SwaggerConfig` 配置类，讲解如何通过 `@EnableSwagger2` 注解和 `Docket` 对象来配置 Swagger2。
*   **00:35 - 00:45**: 详细讲解 `createRestApi()` 方法中 `Docket` 的配置，包括 API 信息、扫描包路径等。
*   **00:45 - 00:55**: 展示 `ApiInfo` 的配置，设置 API 的标题和版本。
*   **00:55 - 01:05**: 讲解如何解决 Swagger2 与静态资源路径冲突的问题，通过重写 `addResourceHandlers` 方法来添加资源路径。
*   **01:05 - 01:15**: 转入“4. 地址簿管理”章节，展示地址簿的业务需求和产品原型。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **文档标题**: “TMS项目讲义_第1章 - Typora”
*   **章节结构**:
    *   第3章 用户服务开发 (pd-user)
        *   3.1 配置文件
        *   3.2 服务启动类
        *   3.3 配置类
        *   4. 地址簿管理
        *   5. 用户信息管理
*   **4.1 业务需求和产品原型**: 描述了地址簿的功能，用户可以在寄件时选择收件人和寄件人。

#### 代码关键内容

*   **`UserApplication.java` (主启动类)**:
    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    @EnableSwagger2
    public class UserApplication {
        public static void main(String[] args) {
            SpringApplication.run(UserApplication.class, args);
        }
    }
    ```

*   **`MybatisPlusConfig.java` (配置类)**:
    ```java
    @Configuration
    public class MybatisPlusConfig {
        @Bean
        public PaginationInterceptor paginationInterceptor() {
            return new PaginationInterceptor();
        }
    }
    ```

*   **`SwaggerConfig.java` (Swagger2 配置类)**:
    ```java
    @Configuration
    @EnableSwagger2
    public class SwaggerConfig extends WebMvcConfigurationSupport {
        private static final String splitter = ",";

        @Bean
        public Docket createRestApi() {
            return new Docket(DocumentationType.SWAGGER_2)
                    .apiInfo(apiInfo())
                    .select()
                    .apis(RequestHandlerSelectors.basePackage("com.itheima.pinda.controller"))
                    .paths(PathSelectors.any())
                    .build();
        }

        private ApiInfo apiInfo() {
            return new ApiInfoBuilder()
                    .title("品达物流订单模块-Swagger文档")
                    .version("1.0")
                    .build();
        }
    }
    ```

*   **解决静态资源冲突的代码**:
    ```java
    protected void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/**").addResourceLocations("classpath:/static/");
        registry.addResourceHandler("/swagger-ui.html").addResourceLocations("classpath:/META-INF/resources/");
        registry.addResourceHandler("/webjars/**").addResourceLocations("classpath:/META-INF/resources/webjars/");
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与配置文件展示 (00:00-00:05)**
    *   讲师在 IntelliJ IDEA 中展示了项目的目录结构，重点指向 `resources` 文件夹下的 `caffeine.properties` 文件。
    *   高亮显示了配置内容：`addressBook=2000, 2h`，并解释了其含义。

*   **场景二：服务启动类演示 (00:05-00:15)**
    *   讲师切换到 `UserApplication.java` 文件，讲解了 `@SpringBootApplication` 注解的综合功能。
    *   展示了 `main` 方法的结构，说明了 Spring Boot 项目的启动方式。

*   **场景三：MyBatis-Plus 配置演示 (00:15-00:25)**
    *   讲师在 Typora 文档中切换到“3.3 配置类”章节。
    *   展示了 `MybatisPlusConfig` 类，重点讲解了 `@Bean` 注解用于创建并注册 `PaginationInterceptor` 分页拦截器。

*   **场景四：Swagger2 配置与调试 (00:25-01:05)**
    *   讲师在 Typora 中展示 `SwaggerConfig` 类的代码。
    *   详细讲解了 `Docket` 对象的配置，包括设置 API 信息、扫描包路径。
    *   展示了 `ApiInfo` 的配置，设置了文档标题和版本。
    *   讲师在 IDEA 中演示了如何解决 Swagger2 与静态资源路径冲突的问题，通过重写 `addResourceHandlers` 方法来添加资源路径。

*   **场景五：业务需求与产品原型展示 (01:05-01:15)**
    *   讲师在 Typora 中切换到“4. 地址簿管理”章节。
    *   展示了“地址簿”的业务需求和产品原型图，说明了其在 TMS 系统中的作用。

---
