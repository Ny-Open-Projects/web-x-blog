# 06-流程定义操作：前端页面展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\06-流程定义操作：前端页面展示_【海量资源尽在 ubkz.com】.mp4
- 时长 10分27秒（音频 628s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们现在呢把这些代码呢已经写好了接来呢可以连上我们的页面来看一下它这个展示效果那各位在我们启动的时候呢这边有一个小小的问题需要各位注意一下那我们在之前定义的时候呢上边已经定义好了我请求的附录镜其实就是Process那刚才我写代码的时候没有看到啊那在这边我们把这个Process多余的给它删掉OK
[00:30] 好了那删掉了之后呢我们开始启动起来我们当前的这个微服务找到我们的启动类来执行好了那这个启动呢相对来说呢会有一点点慢各位和我一起耐心等待一下好了各位来看现在呢已经启动成功了并且没有任何的异常那接下来清空一下控制台回到我们的页面哎回到页面那接下来登录进去
[01:03] 那登录过去之后呢这边呢会多出来两个按钮一个是员工一面一个是审批对应的页面那这些呢需要各位注意的是那如果想要有类似的这些数据我们需要在权限这边呢做一个小小的设置这个是需要各位一定一定要注意的在权限这边
[01:25] 好了我们添加了两个对应的菜单一个就是员工资助的这么一个页面一个是审批对应的这么一个页面各位应该能够看到没错吧好了那我们现在关注的是这个审批栏那进来之后呢这边呢会爆出异常的我们不需要管它我们来看在右上角是不是这边有一个叫做设置的一个按钮那这个设置按钮一点击其实就跟我们刚才分析的这个界面是一模一样那就目前而言呢
[01:52] 那点击之后呢会进入到这么一个设置界面那这个界面你有多少流程展示出来那我们的系统当中内置了三个请假加班和离职那我们回到页面一起来看一下那现在有请假加班以及离职那这些呢全部都是一些至灰色不可至灰色的这么几个按钮为啥那我们知道那我们之前做不管是做流程上传
[02:20] 还是做列表查询还是我们挂起激活全部是在我们的测试代码当中完成的没有连上任何的我们的前端页面没错吧那并且呢数据库当中我们这边的流程定义那各位会发现现在呢全部都写的是传输博客我们的租户ID没错吧那我们现在登录的用户呢租户ID是1显然它根本就没有流程所以默认是这么一个灰色的状态那如果你想点击会告诉你
[02:50] 你这个流程还没有上传所以对于我们来说怎么做呢很简单我们可以在这边点击按钮找到我们的流程文件传上去为我们当前的这个传职博客企业传一个请假流程那这个请假流程在之前的资料当中呢已经给各位准备好了同时我们自己也画过这个请假流程把请假流程拖拽过来现在已经导入成功那导入成功再去看一下设置
[03:18] 这边有一个小小的异常没错了好了那接下来呢我们可以一起打开F12来验证一下刷新一把呢这边呢会执行其实咱们这边呢已经执行了definition已经发送了请求已经发送成功了但是呢这边会告诉我一个响应代表的是抱歉啊这个系统出错了没错了那为什么会有这个问题呢那这边呢是
[03:49] activity呢它的一个小小的问题那我们来看一下就是在我们这个请求发送过来我们查询的是列表definition那发送过来之后我们得到的是一个例子集合那对于这个例子集合得到的是process definition那点击过去你会发现是一个接口
[04:10] 我们可以找到对应的时间类就叫做NPL那这个NPL里面呢是我们最终得到的数据那其中会有这么一些粒子集合等等等等那这些粒子集合在进行Jason转化的时候是这样的我们请求过来最终是不是思维查询那查询通过Controller咱们是把它要转化成Jason那转化成Jason的时候由于activity
[04:36] 它内置的一些加载逻辑会导致对于这些list没有加载数据它最终会抛出空着针一场导致我们整个的查询会出现错误那我们可以打开这边的空台一起来看一下这边会告诉你就是HDP message什么什么not available其实就是你得到这个process definition的时候会有一个小小的转换jest这么一个问题各位来看
[05:05] 就是有这么一个什么identity什么links就在这个identity links这个不好找这个不找了其实就是内置的一个这么一个对象会有一个问题那对于这个内置对象的问题那怎么办也能解决也能解决我们只需要在sprint boot进行内置转化的时候咱们把这玩意给它过滤掉其实就可以了就是说对于
[05:36] 类似的这个链接这个属性我们不进行执行转换JSON转化就这么一个处理逻辑那这个处理逻辑呢在今天资料当中也给各位准备好了在第17天这边有一个处理JSON转换异常的这么一个文件好了把里面这段代码呢Ctrl C拷过来那copy到我们的启动类当中就行了找到我们的启动类再来过来那这边呢我简单的解释一下就是为了解决为了解决
[06:09] ACTIVITI对象转化JSON的问题好了我们这边通过自定义JSON转化器的形式来完成那这个说是叫自定义JSON转化器其实说的简单一点其实我们就是通过使用FASTJSON来替换默认的JSON转化我们的JSON数据
[06:43] 好了并且呢在在我们这个转化器中过滤了刚才出现错误的这个identity links属性就这么一个小小的套路好了那我们把这个补丁呢给它加上了之后啊接着回到我们这边重新启动一下我们再来看一下这个问题呢是否已经解决了
[07:14] 那这边呢需要各位一定一定要注意啊其实这个activity呢在对json处理的时候呢就会有这些类似的问题那出现这些类似的问题呢要处理起来也很简单其实就是说了对于它内置属性什么identity links咱们不过来处理因为我们在页面上或者我们在咱们前端的业务流程根本用不上类似的这些属性好了那我们来看一下启动呢还在启动啊
[07:45] 再启动不管了回到我们的页面部分咱们这回再来刷新来试一下重新加载好了那各位还会发现我们刚才呢已经上传了一个请假流程并且这回没有报错是不是这回你会发现这个请假流程是不是默认已经给它变成绿色是不是就是激活了那同时我们看一下我们的数据库表哎流程定义里面在流程定义当中多了一个请假流程只不过这一回
[08:17] 租户ID是不是变成1了好了那同时当前的这个状态是不是也是1也就是可用的一个状态没错了那如果想要把这个玩意儿变成不可用那怎么办很简单回到我们的页面那我一点击它会发送一个请求到我们刚才写好的Controller里面通过咱们的代码挂起的这个方法来进行是不是挂起操作
[08:50] 那如果你再点一下是不是就变成激活操作了我们一起来试一下回到页面好了现在是一个正常状态走好了各位来看发送了一个请求那接着回到我们的数据库来验证一下变成二了没问题那接下来呢再回到页面我们再走又发送了一下那回到数据库再来看是不是变成一了那这样一来咱们就已经完成了
[09:19] 对一个企业你可以上传类似的一个流程并且对流程进行控制好了那接着有朋友就说了那我们设置这个流程的挂起或者设置这个流程的激活它究竟有什么作用那这边三言两语和各位做一个小小的解释那对于这个流程的定义或者流程定义的这个激活或者挂起是为了解决啊
[09:50] 是为了解决类似这样的问题就是说你企业当中有可能这个流程目前不想让它用也就是说目前呢你不想让员工请假那怎么办我只需要把这个流程设置为挂起那接着员工就不能请假了因为activity在进行流程处理的时候会判断流程是否处于挂起状态如果流程处于挂起状态而你又发送了请假那这个时候它会默认投注一成
[10:18] 所以呢这个挂起主要是为了控制流程是否可以执行的这么一个状态OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  - （1）配置 Controller
    ```java
    @RequestMapping(value = "/process/suspend/{processKey}", method = RequestMethod.GET)
    public Result setProcessAbility(@PathVariable String processKey) {
        processService.suspendProcess(processKey);
        return new Result(ResultCode.SUCCESS);
    }
    ```

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

