# day08-14-交易中心保存标的-Controller

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-14-交易中心保存标的-Controller_【海量资源尽在 666java.com】.mp4
- 时长 1分3秒（音频 63s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才咱们可以说是费了九牛二虎之力才把业务层的代码搞定搞定完之后咱最后要回到Controller要把这里边代码完善一下那Controller里边代码无非就是调用一下业务层就搞定了是不是咱找一找Controller然后我们先把Service是不是先注进来大家都比较熟悉了这个代码然后在发案里边调用一下就行了就这里这个代码比较简单
[00:40] 大家看一下这个DTO对象是不是就是前端这个发过来的数据封装成DTO了对吧然后扔给什么呀要藏啊要藏完成这个啊发标就是保存啊保存标底的这个信息然后呢最终呢我们把这个DTO对象呢又封装成封装到什么rest response里边返回前端就行这是control代码标签的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中完善 TransactionController 的代码，通过调用 ProjectService 来完成标的创建功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 createProject 方法中设置用户编码、用户 ID、标的名称、标的初始状态等逻辑。
画面 2: 展示了设置标的名称和状态的代码，光标位于设置状态的行。
画面 3: 展示了将 ProjectDTO 转换为 Project 实体，并设置年化利率、授信金额、判断是否为女性、设置借款人姓名等逻辑。
画面 4: 展示了 TransactionController 的类定义，包含 @Api 和 @RestController 注解。
画面 5: 展示了 TransactionController 类定义，光标位于 private 修饰符后。
画面 6: 展示了 TransactionController 的 createProject 方法，包含 @ApiImplicitParam 和 @PostMapping 注解。
画面 7: 展示了 IDEA 中的项目结构，包含 Controller、entity、Mapper、model、Service、transaction 等包。
画面 8: 展示了 TransactionController.java 文件，光标位于方法体内部。
画面 9: 展示了 TransactionController 的 createProject 方法，光标位于方法体内部。
画面 10: 展示了 TransactionController.java 文件，光标位于方法体内部。
画面 11: 展示了 TransactionController.java 文件，光标位于 @Autowired 注解后。
画面 12: 展示了 TransactionController 的 createProject 方法，光标位于方法体内部。
画面 13: 展示了多个服务端口的运行状态，包括 ApolloPortal、configService、adminService 等。
画面 14: 展示了 TransactionController 的 createProject 方法，光标位于 return 语句后。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Autowired
private ConsumerApiAgent consumerApiAgent;

@Override
public ProjectDTO createProject(ProjectDTO projectDTO) {
    Final RestResponse<ConsumerDTO> consumer =
            consumerApiAgent.getCurConsumer();

    // 设置用户编码
    projectDTO.setUserName(consumer.getResult().getUserName());
    // 设置用户id
    projectDTO.setConsumerId(consumer.getResult().getId());
    // 主标名称编码
    projectDTO.setProjectNo(CodeNullUtil.getNo(CodePrefixCode.CODE_PROJECT_PREFIX));
    // 标的初始状态修改
    projectDTO.setProjectStatus(ProjectCode.COLLECTING.getCode());
    // 标的可用状态修改，未同步
```

画面 2:
```java
projectDTO.setProjectNo(CodeNullUtil.getNo(CodePrefixCode.CODE_PROJECT_PREFIX));
// 标的初始状态修改
projectDTO.setProjectStatus(ProjectCode.COLLECTING.getCode());
```

画面 3:
```java
projectDTO.setType("NEW");
// 也转换entity
final Project project = convertProjectDTOToEntity(projectDTO);
// 设置利率(需要在Apollo中进行配置)
project.setBorrowerAnnualRate(configService.getBorrowerAnnualRate());
// 年化利率(借款人视角)
project.setAnnualRate(configService.getAnnualRate());
// 年化利率(平台租金+补贴)
project.setCommissionAnnualRate(configService.getCommissionAnnualRate());
// 借款人
project.setIsAssignment(0);
// 判断是否为女性
String sex = Integer.parseInt(16, 17) % 2 == 0 ? "女士" : "先生";
// 查询借款次数条件
QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
queryWrapper.lambda().eq(Project::getConsumerId, consumer.getResult().getId());
project.setUserName(
        consumer.getResult().getFullName() + sex
        + "第" + (count(queryWrapper) + 1) + "次借款");
```

画面 4:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {
```

画面 5:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {
```

画面 6:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Override
    @ApiOperation("借款人发标")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
```

画面 7:
```java
Project
├── Controller
│   └── TransactionController.java
├── entity
│   └── Project.java
├── Mapper
│   └── ProjectMapper.xml
├── model
│   └── ProjectDTO.java
├── Service
│   ├── ConfigService.java
│   ├── ProjectService.java
│   └── TransactionService.java
└── transaction
```

画面 8:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Override
    @ApiOperation("借款人发标")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
        return null;
    }
}
```

画面 9:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private ProjectService projectService;

    @Override
    @ApiOperation("借款人发标")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
```

画面 10:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private ProjectService projectService;

    @Override
    @ApiOperation("借款人发标")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
```

画面 11:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private ProjectService projectService;
```

画面 12:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private ProjectService projectService;

    @Override
    @ApiOperation("借款人发标")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
```

画面 13:
```text
ApolloPortal
configService
adminService
```

画面 14:
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private ProjectService projectService;

    @Override
    @ApiOperation("借款人发标")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
        ProjectDTO dto = projectService.createProject(projectDTO);
        return RestResponse.success(dto);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 4: PPT 标题为“7. 完善 TransactionController 的代码，调用 ProjectService 完成保存标的的功能”。
画面 13: 展示了多个服务端口的运行状态，包括 ApolloPortal、configService、adminService 等。

5) 不要评价画面美观，不要输出与课程无关的内容。

