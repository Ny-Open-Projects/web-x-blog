# 画面线理解：06-微服务调用组件Feign：案例测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\06-微服务调用组件Feign：案例测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:21, 02:25, 03:47, 04:13, 06:04, 08:35, 09:46, 11:22, 12:18, 13:16, 14:29, 15:37, 16:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:50:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 微服务架构中，通过 Feign 客户端配置拦截器来统一处理请求头（如 JWT Token），并展示相关代码实现与测试调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IDEA 中，右键点击 `DepartmentController.java`，弹出菜单，准备进行操作（如关闭、移动、重命名等）。
画面 2: 展示 `UserController.java` 中定义的两个 Feign 调用接口：`testFeign` 和 `assignRoles`。
画面 3: 在 IDEA 中，`UserController.java` 的 `assignRoles` 方法被选中，提示输入 `Ctrl+Shift+Enter` 以选择并插入代码。
画面 4: 在 Postman 中，向 `localhost:9002/sys/profile` 发送 POST 请求，请求头包含 JWT Token，响应体显示操作成功。
画面 5: 在 SQLyog 中，打开 `hrm_system` 数据库，准备执行 SQL 操作。
画面 6: 展示一张微服务架构图，包含 Eureka 服务注册中心、企业微服务、系统微服务、员工微服务，以及浏览器通过 `/test` 接口访问系统微服务。
画面 7: 在 IDEA 中，右键点击项目 `hrm_common`，弹出“New”菜单，准备创建新文件或模块。
画面 8: 展示 `hrm_common` 项目的 `pom.xml` 文件内容，其中定义了 Spring Boot、Spring Cloud、JWT、Jackson 等依赖。
画面 9: 展示 `FeignConfiguration.java` 文件，其中定义了 `requestInterceptor()` 方法，用于配置 Feign 拦截器。
画面 10: 在 `FeignConfiguration.java` 中，为 `RequestInterceptor` 类添加 `@Configuration` 注解，并开始编写拦截器逻辑。
画面 11: 在 `FeignConfiguration.java` 中，为 `RequestInterceptor` 类添加 `@Configuration` 注解，并开始编写拦截器逻辑。
画面 12: 在 `FeignConfiguration.java` 中，编写拦截器代码，从 `ServletRequestAttributes` 中获取请求头，并遍历所有请求头。
画面 13: 展示 `DepartmentController.java` 中的 `findAll`、`findById` 和 `update` 方法，用于处理部门相关的 HTTP 请求。
画面 14: 在 Postman 中，向 `localhost:9002/sys/rest/1063676045212913664` 发送 GET 请求，请求头包含 JWT Token，响应体显示操作成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@Autowired
private UserService userService;

@Autowired
private PermissionService permissionService;

@Autowired
private JwtUtils jwtUtils;

/**
 * 测试Feign组件
 */
@RequestMapping(value = "/test/{id}", method = RequestMethod.GET)
public Result testFeign(@PathVariable(value = "id") String id) {
}

/**
 * 分配角色
 */
@RequestMapping(value = "/user/assignRoles", method = RequestMethod.PUT)
public Result assignRoles(@RequestBody Map<String, Object> map) {
    String userId = (String) map.get("id");
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
    // 该请求的用户id
