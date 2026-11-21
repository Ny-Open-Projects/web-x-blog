# 画面线理解：day01-20-Swagger生成文档

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-20-Swagger生成文档_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:38, 02:13, 02:38, 03:05, 03:39, 03:54, 04:15, 04:55, 05:42, 06:15, 06:46, 07:30, 08:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:12:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Swagger2 生成并测试 RESTful API 文档。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- IDE 界面显示 `ConsumerController.java` 文件，其中定义了两个 API 接口：`@GetMapping("/hello")` 和 `@PostMapping("/hi")`。
- `@ApiImplicitParam` 注解为 POST 接口的 `name` 参数添加了描述和必填约束。
- 项目结构中可见 `SwaggerConfiguration.java` 文件。

画面 2:
- 控制台日志显示服务已启动，端口为 53050，Eureka 服务注册成功。

画面 3:
- 控制台日志显示服务初始化完成，Spring Dispatcher 初始化成功。

画面 4:
- IDE 界面显示 `SwaggerConfiguration.java` 文件，其中 `private ApiInfo buildApiInfo()` 方法用于构建 API 文档信息。
- `ApiInfoBuilder` 设置了文档标题、描述、联系人和版本号。

画面 5:
- 浏览器显示 Swagger UI 页面，标题为“万信金融P2P平台-用户服务API文档”，包含 GET `/hello` 和 POST `/hi` 两个接口。

画面 6:
- IDE 界面显示多个窗口，包括 Swagger UI 页面和项目结构，表明正在演示 Swagger 文档的访问。

画面 7:
- 浏览器显示 Swagger UI 页面，展示 GET `/hello` 接口的详细信息，包括响应状态码 200。

画面 8:
- 浏览器显示 Swagger UI 页面，展示 POST `/hi` 接口的详细信息，包括参数 `name` 和响应示例。

画面 9:
- IDE 界面显示 `ConsumerController.java` 文件，高亮显示 `@ApiImplicitParam` 注解，用于定义 POST 接口的参数。

画面 10:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的“Execute”按钮被点击，准备发送请求。

画面 11:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的“Execute”按钮正在执行，页面显示“LOADING”状态。

画面 12:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的响应结果，包括 Curl 命令和请求 URL。

画面 13:
- IDE 界面显示 `SwaggerConfiguration.java` 文件，其中 `@ConditionalOnProperty` 注解用于控制 Swagger 是否启用。

画面 14:
- 浏览器显示 Swagger UI 页面，POST `/hi` 接口的参数输入框中已填写“小明”，准备执行请求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import org.springframework.web.bind.annotation.RestController;

@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
public class ConsumerController {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() {
        return "hello";
    }

    @ApiOperation("测试hi")
    @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
    @PostMapping(value = "/hi")
    public String hi(String name) {
        return "hi," + name;
    }
}
```

画面 4:
```java
private ApiInfo buildApiInfo() {
    Contact contact = new Contact(name: "黑马程序员", url: "", email: "");
    return new ApiInfoBuilder()
        .title("万信金融P2P平台-用户服务API文档")
        .description("包含用户服务api")
        .contact(contact)
        .version("1.0.0")
        .build();
}
```

画面 13:
```java
@Configuration
@ConditionalOnProperty(prefix = "swagger", value = "enable", havingValue = "true")
@EnableSwagger2 // 开启swagger注解
public class SwaggerConfiguration {
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
            .apiInfo(buildApiInfo())
            .select()
            .apis(ScanHandlerSelectors.basePackage("cn.itcast.wanxing2p"))
            .paths(PathSelectors.any())
            .build();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
