# 画面线理解：19.开发环境搭建-Swagger接口工具-配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\19.开发环境搭建-Swagger接口工具-配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:41, 03:24, 04:36, 05:35, 06:47, 07:43, 09:08, 10:09, 11:32, 12:35, 13:37, 14:37, 15:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:47:02

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Swagger 以自动生成和展示 API 文档。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了项目结构，焦点在 `MerchantController.java` 中的 `@GetMapping("/merchants/{id}")` 方法，用于查询商户信息。
画面 2: 代码编辑器中高亮显示了 `@GetMapping("/merchants/{id}")` 方法，右侧显示了 Maven 依赖。
画面 3: 展示了 `pom.xml` 文件中添加的 Spring Boot 启动器依赖项。
画面 4: 代码编辑器中高亮显示了 `@GetMapping("/merchants/{id}")` 方法，右侧显示了 Maven 依赖。
画面 5: 展示了 `SwaggerConfiguration.java` 文件，其中配置了 Swagger 扫描的包路径。
画面 6: 展示了 `WebMvcConfig.java` 文件，其中配置了静态资源路径。
画面 7: 展示了浏览器中访问的 Swagger UI 页面，显示了 API 文档。
画面 8: 展示了 `SwaggerConfiguration.java` 文件，其中配置了 Swagger 扫描的包路径。
画面 9: 展示了 Swagger UI 页面，显示了 `GET /merchants/{id}` 接口的详细信息。
画面 10: 展示了 `MerchantController.java` 文件，其中定义了 `@GetMapping("/merchants/{id}")` 方法。
画面 11: 展示了 Swagger 文档中关于 `@ApiImplicitParam` 注解的说明。
画面 12: 展示了 `MerchantController.java` 文件，其中定义了 `@GetMapping("/hello")` 和 `@GetMapping("/hi")` 方法。
画面 13: 展示了 `pom.xml` 文件中添加的 Swagger 依赖项。
画面 14: 展示了 `SwaggerConfiguration.java` 文件，其中定义了 `buildApiInfo` 方法。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 1:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 2:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 3:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

画面 4:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 5:
```java
@Configuration
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.shanjugay.merchant.controller"))
                .paths(PathSelectors.any())
                .build();
    }
}
```

画面 6:
```java
@Component
public class WebMvcConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/**").addResourceLocations("classpath:/");
        registry.addResourceHandler("/swagger-ui.html").addResourceLocations("classpath:/META-INF/resources/");
        registry.addResourceHandler("/webjars/**").addResourceLocations("classpath:/META-INF/resources/webjars/");
    }
}
```

画面 7:
```html
GET /merchants/{id} queryMerchantById
```

画面 8:
```java
@Configuration
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.shanjugay.merchant.controller"))
                .paths(PathSelectors.any())
                .build();
    }
}
```

画面 9:
```html
GET /merchants/{id} queryMerchantById
```

画面 10:
```java
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
    return merchantDTO;
}
```

画面 11:
```text
@ApiImplicitParam属性：
属性      取值     作用
paramType  path    以地址的形式提交数据
```

画面 12:
```java
@GetMapping("/hello")
public String hello() {
    return "hello";
}

@GetMapping("/hi")
public String hi(String name) {
    return "hi " + name;
}
```

画面 13:
```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
</dependency>
```

画面 14:
```java
@Configuration
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.shanjugay.merchant.controller"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo buildApiInfo() {
        Contact contact = new Contact("开发者", "", "");
        return new ApiInfoBuilder()
                .title("商户平台API")
                .contact(contact)
                .version("1.0.0")
                .build();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 6:
标题: 1.7.2 配置 MyBatis-Plus
表格数据:
1.7.2.1 配置连接池 Druid
1.7.2.2 配置 MyBatis-Plus

画面 11:
标题: 2.1.3 Swagger常用注解
表格数据:
属性      取值     作用
paramType  path    以地址的形式提交数据

5) 不要评价画面美观，不要输出与课程无关的内容。
