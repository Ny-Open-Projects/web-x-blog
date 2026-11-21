# 画面线理解：06-流程定义操作：前端页面展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\06-流程定义操作：前端页面展示_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:55, 01:35, 02:34, 03:27, 04:00, 04:28, 05:29, 05:59, 07:00, 07:44, 08:30, 09:03, 09:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:04:17

1) 这一组画面整体在讲什么（一句话）：
演示如何在基于 Spring Boot 和 Activiti 工作流引擎的系统中，通过控制器和业务服务层实现对流程定义的部署、查询、挂起与激活操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 IntelliJ IDEA 中的项目结构，当前选中 `target` 目录。
- 代码编辑器中展示 `ProcessController.java` 文件内容，包含部署流程的 `@RequestMapping` 注解方法和查询流程定义的 `@RequestMapping` 注解方法。
- 代码片段：
  ```java
  @RequestMapping(value = "/deploy", method = RequestMethod.POST)
  public Result deployProcess(@RequestParam("file") MultipartFile file) throws IOException {
      processService.deployProcess(file, companyId);
      return new Result(ResultCode.SUCCESS);
  }

  @RequestMapping(value = "/process/definition", method = RequestMethod.GET)
  public Result definitionList() throws IOException {
      List list = processService.getProcessDefinitionList(companyId);
      return new Result(ResultCode.SUCCESS, list);
  }
  ```

画面 2：
- 显示 IDEA 的运行日志，记录了 Spring Boot 应用启动过程，包括 Eureka、DiscoveryClient、Tomcat 等组件的初始化信息。
- 日志显示应用启动成功，端口为 9807。

画面 3：
- 显示 Web 界面，为一个名为“江苏传智播客教育科技股份有限公司”的系统后台。
- 页面左侧导航栏中“权限设置”菜单被选中，右侧列表显示了多个权限项，如“SaaS-Client”、“员工管理”等。

画面 4：
- 显示数据库管理工具（SQLyog）界面，连接到本地数据库。
- 数据库表 `act_re_procdef` 中显示了流程定义的记录，其中一条记录的 `KEY_` 为 `process_leave`。

画面 5：
- 显示浏览器开发者工具的 Network 面板，记录了对 `127.0.0.1` 的请求。
- 请求状态为 304（未修改），类型为 document 和 script。

画面 6：
- 显示 IDEA 中 `ProcessService.java` 文件内容，展示挂起流程的 `suspendProcess` 方法。
- 代码中包含对流程定义实体的查询和根据状态进行激活或挂起的逻辑。
- 代码片段：
  ```java
  public void suspendProcess(String processKey, String companyId) {
      ProcessDefinitionEntity definition = repositoryService.createProcessDefinitionQuery().processDefinitionKey(processKey)
              .processDefinitionTenantId(companyId).latestVersion().singleResult();
      if (definition.isSuspended()) {
          // 如果是挂起状态：设置为激活
          repositoryService.activateProcessDefinitionById(definition.getId());
      } else {
          // 如果不是挂起状态：设置为挂起
          repositoryService.suspendProcessDefinitionById(definition.getId());
      }
  }
  ```

画面 7：
- 显示 IDEA 中 `ProcessService.java` 文件内容，与画面 6 内容相同，但光标位置不同。
- 代码片段同上。

画面 8：
- 显示 IDEA 中 `ProcessDefinitionEntityImpl.class` 的反编译代码。
- 代码展示了 `ProcessDefinitionEntityImpl` 类的构造函数和 `getPersistentState` 方法。
- 代码片段：
  ```java
  protected String diagramResourceName;
  protected boolean isGraphicalNotationDefined;
  protected Map<String, Object> variables;
  protected boolean hasStartFormKey;
  protected int suspensionState;
  protected boolean isIdentityLinksInitialized;
  protected List<IdentityLinkEntity> definitionIdentityLinkEntities;
  protected IOSpecification iosSpecification;
  protected String engineVersion;

  public ProcessDefinitionEntityImpl() {
      this.suspensionState = SuspensionState.ACTIVE.getStateCode();
      this.definitionIdentityLinkEntities = new ArrayList();
  }

  public Object getPersistentState() {
      Map<String, Object> persistentState = new HashMap();
      persistentState.put("suspensionState", this.suspensionState);
      persistentState.put("category", this.category);
      return persistentState;
  }
  ```

画面 9：
- 显示 IDEA 中 `AuditApplication.java` 文件内容，展示 Spring Boot 应用的主类。
- 代码包含 `@EnableEurekaClient`、`@EnableDiscoveryClient`、`@EnableFeignClients` 等注解。
- 代码片段：
  ```java
  @SpringBootApplication(scanBasePackages = "com.ihrm", exclude = {SecurityAutoConfiguration.class})
  @EntityScan(value = "com.ihrm.domain")
  @EnableEurekaClient
  @EnableDiscoveryClient
  @EnableFeignClients
  public class AuditApplication {
      public static void main(String[] args) {
          SpringApplication.run(AuditApplication.class, args);
      }
  }
  ```

画面 10：
- 显示 IDEA 中 `AuditApplication.java` 文件内容，展示自定义 `HttpMessageConverters` 的配置。
- 代码中定义了 `FastJsonHttpMessageConverter` 并配置了 `SimplePropertyPreFilter` 以排除 `identityLinks` 字段。
- 代码片段：
  ```java
  @Bean
  public HttpMessageConverters fastJsonHttpMessageConverters() {
      FastJsonHttpMessageConverter fjc = new FastJsonHttpMessageConverter();
      FastJsonConfig config = new FastJsonConfig();
      config.setSerializerFeatures(SerializerFeature.PrettyFormat);
      SimplePropertyPreFilter filter = new SimplePropertyPreFilter();
      filter.getExcludes().add("identityLinks");
      config.setSerializerFilters(filter);
      fjc.setFastJsonConfig(config);
      return new HttpMessageConverters(converter);
  }
  ```

画面 11：
- 显示 IDEA 的运行日志，记录了 Spring Boot 应用启动过程，包括 Eureka、DiscoveryClient、Tomcat 等组件的初始化信息。
- 日志显示应用启动成功，端口为 9807。

画面 12：
- 显示 IDEA 的运行日志，记录了 Spring Boot 应用启动过程，包括 DispatcherServlet、AbstractValidatingSessionManager 等组件的初始化信息。
- 日志显示应用启动成功。

画面 13：
- 显示 SQLyog 数据库管理工具界面，连接到本地数据库。
- 数据库表 `act_re_procdef` 中显示了流程定义的记录，其中一条记录的 `KEY_` 为 `process_leave`。

画面 14：
- 显示 PPT 页面，标题为“1.2 流程定义的挂起与激活”。
- 内容说明从 Activiti 5.11 开始支持流程挂起与激活功能。
- 代码片段：
  ```java
  @RequestMapping(value = "/process/suspend/{processKey}", method = RequestMethod.GET)
  public Result setProcessAbility(@PathVariable String processKey) {
      processService.suspendProcess(processKey);
      return new Result(ResultCode.SUCCESS);
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：1.2 流程定义的挂起与激活
- PPT 内容：
  - 从 activiti 5.11 起，activiti 已支持流程挂起与激活的功能。
  - 这也意味着如果某个流程暂时不用，则可以挂起功能暂停流程，这样就避免流程删除引起的各类麻烦了。
  - 当流程被挂起之后，是不能继续操作此流程的实例的，否则会抛出异常。
  - （1）配置 controller
    ```java
    @RequestMapping(value = "/process/suspend/{processKey}", method = RequestMethod.GET)
    public Result setProcessAbility(@PathVariable String processKey) {
        processService.suspendProcess(processKey);
        return new Result(ResultCode.SUCCESS);
    }
    ```

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
