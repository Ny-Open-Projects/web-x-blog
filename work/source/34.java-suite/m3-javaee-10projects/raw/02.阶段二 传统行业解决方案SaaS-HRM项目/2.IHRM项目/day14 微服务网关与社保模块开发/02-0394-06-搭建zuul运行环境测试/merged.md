# 06-搭建zuul运行环境测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\06-搭建zuul运行环境测试_【海量资源尽在 ubkz.com】.mp4
- 时长 6分59秒（音频 420s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:04] 现在呢我们已经把做网关搭建成功了那我们接下来呢就可以做一个小小的测试好了回到这张图呢我简单的说一下那我准备呢请求就是请求到company咱们查询一下企业列表那接下来呢会发送到我的API网关那所以我请求的路径呢其实很简单请求的其实就是API网关这个路径
[00:29] 那经过我们API网关的路由转发规则的配置是不是自动的会去找到我们的企业微服务啊所以接下来呢回到我这边的idea我先把这个基本的环境给它跑起来那找到我们的ERICA先启动ERICA因为我们的所有的项目呢都已经把它部署都已经交给了这个注册中心了所以这个ERICA要启动起来那ERICA启动成功了之后这边有我们的company
[01:02] 找到company找到company当中的这个启动类但是我先说一下是这样的就是为了方便我们测试啊咱们这边呢需要在v服务的shareware配置部分呢做一个小小的修改因为我们这边呢所有的配置是不是都有这种全新校验的shareware配置啊
[01:23] 所以我把这一句话给他注视起来这样一来呢不管你是不是真的登录了其实都不会做全新交易了主要是方便我们这边做测试好了我保存一下接着再去启动我们的企业微服OK那这边的企业微服呢先让他启动着我们来找一下在企业微服我们请求的的全部企业列表请求全部企业列表就是company开头OK
[01:59] 那接着查询所有企业查询所有企业列表OK是不是get请求咱们的company就可以了好了回到我们这边postman我们可以做一个测试那我们请求的就是localhost或者就是127.0.0.1我们先来看一下不经过网关能不能得到数据9001好了我们请求cmy注意啊各位9001
[02:27] 代表的是我们这个企业微服务的请求路径来9001我现在只是访问企业微服务好了get方式请求没问题看一下有没有数据走你发现数据已经获取到了没错吧那这回呢我不想一个一个微服务去访问了那我们访问访问哪个咱们去访问一下我们的网关9090注意回到我们的ID一起来看一下网关getway
[02:59] 配置我们请求的是9090那接下来我们请求的company来看一下是不是能够拿到相同的数据来send走各位发现这边呢其实是出现了一个小的错误其实这个错误主要是404错误没有找到相同的路径那么可以这样啊就注意来看啊我们请求company接着我再加一个c y m p a n ycompany我再来请求send哎各位会发现
[03:25] 现在是不是通过我们的ZOO网关也能够拿到和刚才企业微服务效果一模一样的数据没错吧好了这个呢是跟各位来看了一下能够通过ZOO拿到数据但是为什么我们在company之后再要加一个company呢那我们之前访问企业微服务是不是9001咱们启动访问就可以啊那我们也想做到9090企业网关
[03:54] 也能够访问到企业里面跟他的路径保持一致那怎么做呢OK是这样的回到我们的ID简单的说一下在做网关的配置特别是配置路由的时候他会自动的这边简单的写一下就这个ZUU自动的自动的会删除我们的请求的前缀那我们如果请求的路径呢是这个含义Localhost
[04:25] 9090company那它其实自动的把这个前缀就删除掉了那如果我们请求了一个company之后又请求一个company那根据这个比对规则比对规则它是不是把这个请求删掉接着给我拼接成了一个完整的抱歉应该这样算我们pn1我们请求的路径其实是这样那么请求的时候呢根据它自动会删除路径
[04:53] 他其实把这company删掉之后接着给我访问到这个路径下边所以我们最终请求的路径就变成了9090那因为他之前把这比对的前缀已经删掉了那接下来呢我们是不是刚才请求的是company-compy-compy那接下来呢他会根据这个比对A一致那接着把这个前缀删掉是不是就只剩下一个company接着再拼接到路径后面去请求
[05:21] 那这个是他的一个请求规则那如果我们想要做到啊就是说不让你把这个前缀删掉那怎么办呢也可以那这边呢可以做一个小的配置这个配置scripts t r i p好了perfix好了false这个代表的含义就是不删除删除请求前缀ok好了我们加上了这个啊这句话之后呢
[05:52] 我们一起再来试一下注意重新启动一下我们的网关来了这个启动稍微有一点点慢各位耐心等待一下OK现在我们的网关已经启动成功了回到我们的给你们一起来试还是刚才9001咱们直接访问企业服务走数据没问题这回请求9090好了company来走
[06:34] 这回效果是不是跟刚才一模一样那这样一来呢我们其实就可以通过统一的一个入口我们的租网关根据我们的路由配置是不是转发到不同的微服务所以我们接下来呢要做的事情呢其实很简单了你有多个微服务在这边是不是配置它的路由规则就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务架构，包含 Eureka 服务注册中心、公司服务（CompanyApplication）和网关服务（GateApplication）的配置与调用流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：展示 IntelliJ IDEA 中的项目结构，当前选中模块为 `ihrm_company`。
- 代码内容：`EurekaServer.java` 文件内容：
  ```java
  package com.ihrm.Eureka;
  import ...
  /**
   * Eureka服务的启动类
   */
  @SpringBootApplication
  @EnableEurekaServer //开启Eureka服务端
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
  //1.配置Spring Boot的包扫描
  //2.配置jpa扫描
  //3.注册到Eureka
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

