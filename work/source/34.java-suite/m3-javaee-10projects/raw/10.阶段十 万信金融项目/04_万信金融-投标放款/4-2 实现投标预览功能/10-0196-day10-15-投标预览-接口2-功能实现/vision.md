# 画面线理解：day10-15-投标预览-接口2-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-15-投标预览-接口2-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:58, 01:53, 02:38, 03:47, 04:20, 04:53, 05:56, 06:41, 08:19, 09:48, 10:15, 11:21, 12:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:26:23

1) 这一组画面整体在讲什么（一句话）：
实现交易中心查询投标记录接口，包括在 Service 层编写查询方法、处理数据转换和封装返回结果，并在 Controller 层提供 REST API 接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“2.2.3 交易中心查询投标记录接口(接口②)”，内容为“2.3.1 功能实现”，并列出“1. 在 ProjectService 接口中新增 queryTendersByProjectId 方法”和“2. 在 ProjectServiceImpl 中实现该方法”。
画面 2: 展示数据库管理工具，显示表“tender_0”的结构，包含字段 ID、CONSUMER_ID、CONSUMER_USERNAME、USER_ID、PROJECT_ID、PROJECT_NAME、TENDER_ID、TENDER_AMOUNT、TENDER_STATUS、TENDER_CREATE_TIME。
画面 3: 展示 IDE 中 ProjectService.java 文件，显示 queryProjects 方法的注释和 queryTendersByProjectId 方法的声明。
画面 4: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法的实现，其中包含获取项目剩余金额的私有方法 getProjectRemainingAmount。
画面 5: 展示 PPT 页面，标题为“3. 完善 TransactionController 类中的代码”，并显示多个窗口的缩略图，包括 IDE、数据库工具和网页界面。
画面 6: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法中调用 tenderMapper.selectList 的代码。
画面 7: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法中调用 tenderMapper.selectList 的代码，并显示了方法的参数类型。
画面 8: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法中使用 for 循环遍历 tenderList。
画面 9: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法中使用 BeanUtils.copyProperties 方法进行属性复制。
画面 10: 展示 IDE 中 CommonUtil.java 文件，显示隐藏手机号的静态方法 hiddenMobile。
画面 11: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法中调用 CommonUtil.hiddenMobile 方法设置 TenderOverviewDTO 的 consumerUsername。
画面 12: 展示 IDE 中 ProjectServiceImpl.java 文件，显示 queryTendersByProjectId 方法中调用 CommonUtil.hiddenMobile 方法设置 TenderOverviewDTO 的 consumerUsername。
画面 13: 展示 IDE 中 TransactionController.java 文件，显示 TransactionController 类的定义和 @RestController 注解。
画面 14: 展示 IDE 中 TransactionController.java 文件，显示 queryTendersByProjectId 方法的实现，调用 projectService.queryTendersByProjectId(id)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 根据标的id查询投标记录
 * @param id
 * @return
 */
List<TenderOverviewDTO> queryTendersByProjectId(Long id);
```
画面 3:
```java
/**
 * @param pageSize
 * @param sortBy
 * @return
 */
PageVO<ProjectDTO> queryProjects(ProjectQueryDTO projectQueryDTO, String order, Integer page, Integer pageSize);
```
画面 4:
```java
@Override
public List<TenderOverviewDTO> queryTendersByProjectId(Long id) {
    return null;
}

/**
 * 获取标的剩余可投标额度
 * @param project
 * @return
 */
private BigDecimal getProjectRemainingAmount(Project project) {
    // 很抱歉的...在投标表里已经没额度了
}
```
画面 6:
```java
tenderMapper.selectList(Wrappers.<Tender>lambdaQuery().eq(Tender::getProjectId, id));
```
画面 7:
```java
List<Tender> tenderList = tenderMapper.selectList(Wrappers.<Tender>lambdaQuery().eq(Tender::getProjectId, id));
```
画面 8:
```java
tenderList.forEach(tender -> {
```
画面 9:
```java
BeanUtils.copyProperties(tender, tenderOverviewDTO);
```
画面 10:
```java
public static String hiddenMobile(String mobile) {
    if (StringUtils.isBlank(mobile)) {
        return "";
    }
    return mobile.replaceAll("\\d{3}\\\\d{0}\\\\d{0}", "****");
}
```
画面 11:
```java
tenderOverviewDTO.setConsumerUsername(CommonUtil.hiddenMobile(tenderOverviewDTO.getConsumerUsername()));
```
画面 13:
```java
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private ProjectService projectService;

    @Override
    @ApiOperation(value = "借款人发标", tags = "transaction")
    @PostMapping("/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
```
画面 14:
```java
    @Override
    @GetMapping("/projects/{ids}")
    public RestResponse<List<ProjectDTO>> queryProjectsIds(@PathVariable String ids) {
        List<ProjectDTO> projectDTOList = projectService.queryProjectsIds(ids);
        return RestResponse.success(projectDTOList);
    }

    @Override
    @GetMapping("/tenders/projects/{id}")
    public RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(@PathVariable Long id) {
        return RestResponse.success(projectService.queryTendersByProjectId(id));
    }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.2.3 交易中心查询投标记录接口(接口②)”，子标题为“2.3.1 功能实现”，内容为“1. 在 ProjectService 接口中新增 queryTendersByProjectId 方法”和“2. 在 ProjectServiceImpl 中实现该方法”。
画面 5: PPT 标题为“3. 完善 TransactionController 类中的代码”。
画面 13: PPT 标题为“TransactionController”，内容为“@RestController”和“@Autowired private ProjectService projectService;”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
