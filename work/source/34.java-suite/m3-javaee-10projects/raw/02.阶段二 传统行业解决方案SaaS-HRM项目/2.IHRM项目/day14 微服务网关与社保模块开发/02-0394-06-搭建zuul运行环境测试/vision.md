# 画面线理解：06-搭建zuul运行环境测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\06-搭建zuul运行环境测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:38, 01:01, 01:06, 01:47, 01:54, 02:02, 02:27, 02:41, 03:12, 04:01, 05:52, 06:09, 06:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:13:04

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务架构，包含 Eureka 服务注册中心、公司服务（CompanyApplication）和网关服务（GateApplication）的配置与调用流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：展示 IntelliJ IDEA 中的项目结构，当前选中模块为 `ihrm_company`。
- 代码内容：`EurekaServer.java` 文件内容：
  ```java
  package com.ihrm.eureka;
  import ...
  /**
   * eureka服务的启动类
   */
  @SpringBootApplication
  @EnableEurekaServer //开启eureka服务端
  public class EurekaServer {
      public static void main(String[] args) {
          SpringApplication.run(EurekaServer.class, args);
      }
  }
  ```

画面 2：
- 项目结构：选中模块 `ihrm_company`，界面为空白，显示 IntelliJ IDEA 的默认提示信息。

画面 3：
- 项目结构：选中模块 `ihrm_company`，并展开 `src` 目录。
- 代码内容：`EurekaServer.java` 文件内容与画面 1 相同。
- 控制台日志：显示 `Cannot determine local hostname` 错误。

画面 4：
- 项目结构：选中模块 `ihrm_company`，并展开 `src/main/java/com/ihrm/company`。
- 代码内容：`CompanyApplication.java` 文件内容：
  ```java
  //1.配置springboot的包扫描
  //2.配置jpa扫描
  //3.注册到eureka
  @EnableEurekaClient
  @SpringBootApplication
  @EntityScan(value="com.ihrm.domain.company")
  public class CompanyApplication {
      //启动类
      public static void main(String[] args) {
          SpringApplication.run(CompanyApplication.class, args);
      }
      @Bean
      public JwtUtils jwtUtils() {
          return new JwtUtils();
      }
      @Bean
      public IdWorker idWorker() {
          return new IdWorker();
      }
  }
  ```
- 控制台日志：显示 `Tomcat started on port(s): 8088 (http)` 和 `Started EurekaServer in 15.852 seconds`。

画面 5：
- 项目结构：选中模块 `ihrm_company`。
- 代码内容：`CompanyApplication.java` 文件内容与画面 4 相同。
- 控制台日志：显示 `Tomcat started on port(s): 8088 (http)` 和 `Started EurekaServer in 15.852 seconds`。
- 右键菜单：显示“Split Vertically”、“Move Right”等选项。

画面 6：
- 项目结构：选中模块 `ihrm_company`。
- 代码内容：`CompanyController.java` 文件内容：
  ```java
  @RestController
  @RequestMapping(value="/company")
  public class CompanyController {
      private CompanyService companyService;
      //新增企业
      @PostMapping(value="", method = RequestMethod.POST)
      public Result save(@RequestBody Company company) {
          companyService.add(company);
          return new Result(ResultCode.SUCCESS);
      }
  }
  ```
- 控制台日志：显示 Hibernate 初始化日志。

画面 7：
- 项目结构：选中模块 `ihrm_company`。
- 代码内容：`CompanyController.java` 文件内容：
  ```java
  //删除企业
  @DeleteMapping("/id")
  public Result delete(@PathVariable(value="id") String id) {
      companyService.deleteById(id);
      return new Result(ResultCode.SUCCESS);
  }
  //根据id查询企业
  @GetMapping("/id")
  public Result findById(@PathVariable(value="id") String id) throws CommonException {
      company = companyService.findById(id);
      return new Result(ResultCode.SUCCESS, company);
  }
  ```
- 控制台日志：显示 `DiscoveryClient` 相关日志。

画面 8：
- 项目结构：选中模块 `ihrm_company`。
- 代码内容：`CompanyController.java` 文件内容：
  ```java
  @RestController
  @RequestMapping(value="/company")
  public class CompanyController {
      @Autowired
      private CompanyService companyService;
      //新增企业
      @PostMapping(value="", method = RequestMethod.POST)
      public Result save(@RequestBody Company company) {
          companyService.add(company);
          return new Result(ResultCode.SUCCESS);
      }
  }
  ```
- 控制台日志：显示 `DiscoveryClient` 相关日志。

画面 9：
- 工具界面：Postman 界面，请求地址为 `127.0.0.1:9001/company`。
- 请求体：JSON 格式，包含企业信息。

画面 10：
- 工具界面：Postman 界面，请求地址为 `127.0.0.1:9001/company`。
- 响应体：JSON 格式，包含错误信息 `{"status": 404, "error": "Not Found", "message": "No message available"}`。

画面 11：
- 项目结构：选中模块 `ihrm_gate`。
- 代码内容：`application.yml` 文件内容：
  ```yaml
  zuul:
    routes:
      ihrm-company:
        path: /company/** #需要被转发的路径
        url: http://127.0.0.1:9001 #映射到对应的实际微服务的url路径
  ```

画面 12：
- 项目结构：选中模块 `ihrm_gate`。
- 代码内容：`ZuulProperties.class` 文件内容：
  ```java
  public void setStripPrefix(boolean stripPrefix) {
      this.stripPrefix = stripPrefix;
  }
  public Boolean getStripPrefix() {
      return this.stripPrefix;
  }
  public Map<String, ZuulProperties.ZuulRoute> getRoutes() {
      return this.routes;
  }
  public void setRoutes(Map<String, ZuulProperties.ZuulRoute> routes) {
      this.routes = routes;
  }
  public boolean isAddProxyHeaders() {
      return this.addProxyHeaders;
  }
  public void setAddProxyHeaders(boolean addProxyHeaders) {
      this.addProxyHeaders = addProxyHeaders;
  }
  public void setAddHostHeader(boolean addHostHeader) {
      this.addHostHeader = addHostHeader;
  }
  public Set<String> getIgnoredServices() {
      return this.ignoredServices;
  }
  public Set<String> getIgnoredPatterns() {
      return this.ignoredPatterns;
  }
  ```

画面 13：
- 项目结构：选中模块 `ihrm_gate`。
- 控制台日志：显示 `GateApplication` 启动日志，包括 `Tomcat started on port(s): 9000 (http)`。

画面 14：
- 项目结构：选中模块 `ihrm_gate`。
- 代码内容：`application.yml` 文件内容：
  ```yaml
  #服务配置
  server:
    port: 9000
  #spring配置
  spring:
    application:
      name: ihrm-gate #指定服务名
  #zuul配置
  zuul:
    routes:
      ihrm-company:
        path: /company/** #需要被转发的路径
        url: http://127.0.0.1:9001 #映射到对应的实际微服务的url路径
        stripPrefix: false #不剥离请求的前缀
  ```
