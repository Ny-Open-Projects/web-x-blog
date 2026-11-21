# 画面线理解：day08-20-查询标的信息-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-20-查询标的信息-功能实现1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:55, 02:23, 03:18, 04:24, 05:37, 07:02, 09:10, 10:06, 11:24, 11:53, 12:15, 13:11, 13:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:57:38

1) 这一组画面整体在讲什么（一句话）：
在项目服务层实现分页查询功能，包括在接口中定义查询方法、在实现类中编写具体逻辑、以及使用 QueryWrapper 进行条件组装。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，标题为“3.4.2 功能实现”，说明在ProjectService接口中新增一个查询方法，方法签名包含projectQueryDTO、order、pageNo、pageSize、sortBy参数，返回值为PageVO<ProjectDTO>。
画面2：PPT内容与画面1相同，但光标位置略有不同。
画面3：展示IDE中ProjectServiceImpl类的代码，显示@Service注解和类继承结构，包含@Autowired注入的ConsumerApiAgent和ConfigService。
画面4：展示ProjectServiceImpl类中queryProjectsByQueryDTO方法的实现部分，光标位于方法定义处。
画面5：展示ProjectQueryDTO类的代码，包含@Data注解和多个@ApiModelProperty注释，定义了类型、名称、起止期限等字段。
画面6：展示Project实体类的代码，包含@Data注解、@EqualsAndHashCode注解、@Accessors(chain = true)注解，以及主键和发标人用户标识字段。
画面7：展示PPT目录结构，当前位于“3.4 有标的信息”章节下的“3.4.2 功能实现”。
画面8：展示PPT内容，标题为“3.4.2 功能实现”，展示QueryWrapper的条件组装代码，包括类型、年化利率、起止期限、状态等条件。
画面9：展示Project实体类的代码，光标位于@Data注解后。
画面10：展示IDE中多个窗口，包括PPT、代码编辑器和数据库管理工具，光标位于代码编辑器中。
画面11：展示ProjectServiceImpl类中QueryWrapper条件组装代码，光标位于“标的类型”条件判断处。
画面12：展示ProjectServiceImpl类中QueryWrapper条件组装代码，光标位于“标的类型”条件判断处。
画面13：展示ProjectServiceImpl类中创建Page对象的代码，光标位于Page<Project> page = new Page<>(pageNo, pageSize);语句处。
画面14：展示ProjectServiceImpl类中创建Page对象的代码，光标位于Page<Project> page = new Page<>(pageNo, pageSize);语句处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 根据分页条件检索标的的信息
 *
 * @param projectQueryDTO
 * @param order
 * @param pageNo
 * @param pageSize
 * @param sortBy
 * @return
 */
PageVO<ProjectDTO> queryProjectsByQueryDTO(ProjectQueryDTO projectQueryDTO,
String order, Integer pageNo, Integer pageSize, String sortBy);
```

画面3：
```java
@Service
public class ProjectServiceImpl extends ServiceImpl<ProjectMapper, Project> implements ProjectService {
    @Autowired
    private ConsumerApiAgent consumerApiAgent;
    @Autowired
    private ConfigService configService;
```

画面4：
```java
@Override
public PageVO<ProjectDTO> queryProjectsByQueryDTO(ProjectQueryDTO projectQueryDTO,
String order, Integer pageNo, Integer pageSize, String sortBy) {
```

画面5：
```java
@Data
@Model(value = "ProjectQueryDTO", description = "标的的信息查询对象")
public class ProjectQueryDTO {

    @ApiModelProperty("标的的类型")
    private String type;

    @ApiModelProperty("名称")
    private String name;

    @ApiModelProperty("起止标的的期限(单位:天)")
    private Integer startPeriod;

    @ApiModelProperty("起止标的的期限(单位:天)")
    private Integer endPeriod;
```

画面6：
```java
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
public class Project implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 主键
     */
    @TableId("ID")
    private Long id;

    /**
     * 发标人用户标识
     */
    @TableField("CONSUMER_ID")
    private Long consumerId;
```

画面8：
```java
// 起止年化利率 -- 区间
if (null != projectQueryDTO.getStartAnnualRate()) {
    queryWrapper.lambda().ge(Project::getAnnualRate, projectQueryDTO.getStartAnnualRate());
}
if (null != projectQueryDTO.getEndAnnualRate()) {
    queryWrapper.lambda().le(Project::getAnnualRate, projectQueryDTO.getEndAnnualRate());
}
// 起止期限 -- 区间
if (null != projectQueryDTO.getStartPeriod()) {
    queryWrapper.lambda().ge(Project::getPeriod, projectQueryDTO.getStartPeriod());
}
if (null != projectQueryDTO.getEndPeriod()) {
    queryWrapper.lambda().le(Project::getPeriod, projectQueryDTO.getEndPeriod());
}
// 标的的状态
if (StringUtils.isNotBlank(projectQueryDTO.getProjectStatus())) {
    queryWrapper.lambda().eq(Project::getProjectStatus, projectQueryDTO.getProjectStatus());
}
```

画面13：
```java
// 分页
Page<Project> page = new Page<>(pageNo, pageSize);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“3.4.2 功能实现”，内容为“1. 数据访问层在前面保存标的的信息时已经搞定，这里不用再管了。2. 在ProjectService接口中新增一个查询方法：...”。
画面7：标题为“3.4 有标的信息”，子标题为“3.4.2 功能实现”。
画面8：标题为“3.4.2 功能实现”，内容为“// 起止年化利率 -- 区间...// 标的的状态...”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
