# day08-20-查询标的信息-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-20-查询标的信息-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 13分32秒（音频 812s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们把接口定义了一下接口定义好之后呢咱接下来就进行功能实现由于我们要进行查询嘛所以这里边就要涉及到数据访问层那数据访问层呢我们在前面保存标题新的的时候是不是已经搞过了那这你就不用管那我们直接从哪一层开始对从业务层开始就行那我们跟之前一样先在业务层的接口里边新增一个对查询方法
[00:27] 那这样呢给大家介绍一个经验啊这个经验呢我觉得大家在平时开发过程当中应该都已经知道这样呢我提一下啊就是你会发现啊我们要从接口里边定义的这个方法其实跟什么呀对跟Controller这块接口的里边的这个方法基本上是什么呀一样就哪一点不一样就这地方就反应值不一样Controller这个接口呢多了
[00:52] 这个一个封装了一层就是rest什么response因为他要给前端返回这个阶层数据他又多封装了一层如果把这一块去掉剩下的整个这块东西你会发现他跟右层接口里边几乎是什么一模一样发明无所谓你叫啥都无所谓参数和返回值可以说是什么一模一样那也就是说是control掉右层得到这个返回值之后在这个返回值的基础上又多封装了一层什么
[01:22] rest response而已所以这个呢大家应该是心里面要清楚那这个方法呢我就不再过多说了嘛我刚才说了跟kontrol里边那个接口人发是一样的这个是干啥的呀封装查询条件的order和sort by是干啥的呀排序的pay number pay size是搞分页的对不对project.do这个范形它是封装你查询出来的每一条数据的然后呢我们把这些数据
[01:50] 将来应该是一个集合嘛在统一封装成配置view对象这个前面都已经讲过了那这个代码呢我们就直接拿过来用我们找到业务层的接口是这个这是创建标的吗就保存吧来一个呃这个就是我们刚才说的这个业务层的这个什么呀接口接口定完之后呢咱接下来就该实现这个方法接口里边这个方法
[02:22] 这是实现类现在他应该报错了是不是好我们把这个方法给他生成一下给他卡了我这个卡了好在这个地方看一下是吧就是他那这里边我们要实现什么功能来我你说一下啊我们前面说了我们想实现一个相对完善的功能完善的一个方法那这里边就涉及到什么呀我是不是要带条件查询带条件啊还要干什么还要搞什么呀分业
[03:01] 还有什么呀刚才你看参数还有什么呀参数里边是不是还要order sort by是不是我还要搞什么呀对我还要搞排序查询对不对是综合的一个查询那你说呢我们一种写代码也是这么写的你得分成这三大块把这个条件先搞定然后再搞定分页然后再搞定什么呀排序最后的话我们就该干什么呀对前面这三样东西你全部都准备到位了我们接下来就该执行什么呀
[03:30] 对执行查询那查询完之后是不是就该封装什么呀结果了查出来的结果大概是这么一个流程吧呃整个写下来这个代码稍微有点复杂大家看一下讲义从这开始对不对啊往下走稍微有点多啊稍微有点麻烦那咱一点点来吧先说这个代条件吧这个代条件我们前面说过这个前端啊在进行查询的时候它可以按照什么呀
[04:04] 按照标的类型啊按照这个利率啊按照你借款的这个期限等等反正可以根据很多条件进行查询对吧那么前段在查询的时候这些条件的数据是不是都封装到什么地方了对这个project queryDTO里面我们再点进去看一下这里边你看一个标的类型名称期限利率对吧标的状态等等等等你可以根据很多条件进行查询总之吧
[04:32] 跟条件相关的数据是在这个对象里边存在的那我这呢先把这个条件先封装好咱们前面在讲MP的时候呃大家都比较熟悉这个带条件的啥去是不是要要先干什么呀先来一个条件构造器嘛用音箱嘛叫什么呀叫叫query warp是不是我们可以直接new也可以用那个不new的那种写法都可以咱这就来一个new的啊query什么呀qu
[05:01] 有啊一二位query是这个吧对带有一个范形这个范形是谁啊这个范形你一定要注意啊呃跟数据库操作有关的就是增加感啊有关了这个范形一定是写的是跟表对应的那个实体类那么大家是DQ对象吗不是是这个project就不是这个DQ啊不是这个DQ是projectp oproject是他啊
[05:30] 你看这里边这个实体来你点进去抽一眼你看这里边是配的就有那些注解吗跟表里边这个这个映射的那些注解就范行一定要写他然后呢我们就叫query warp等于6直接溜了啊他是直接溜出来这是这个条件构造器吗那我们将来接下来是不是要往这个构造器里边开始封装这个什么呀查询条件那我怎么知道前端他会按照哪些条件查不按哪些条件查
[06:02] 是不是我刚才说了查询条件很多啊但是靠谱在潜在操作的时候他不见得你有五个条件他就按五个条件都查他也可能按两个查询按三个查对不对那我怎么知道这个事呢那这里边你就要做一系列的这个什么呀非空什么呀判断这个哪个条件的值不为空那就按这个条件进行查那如果一判断这个条件的值是空那就证明不按这个条件进行什么呀查询
[06:30] 那大家看一下这个奖励这个代码比较简单我们看看奖励这个大家比较熟你看啊我们首先判断哪个条件标底的类型这个标底类型它有什么新标还有什么精英标它搞的一些这个什么呀营销吧你可以看看我以前有个截图吧你看这这就是什么精英标对不对精英标其实说白了就是这个借款人或者这个标底呢它这个可能质量比较高它起个名叫精英标
[07:01] 吸引大家投标的呗然后还有有个截图叫你看这有个什么呀新标是不是它分好几种这个类型其实就是P2P公司做的一些营销那你看这就先判断这个标题类型判断它的值为不为空怎么判断这个大家我们以前应该用吧String YouTube的安排器的一个工具类嘛字母串相关的一个工具类Is not blank这个单词简明之意就是不为空吧判断谁不为空啊就是标题的类型
[07:30] 这个值是不是从这个DTO对象里边取过来了我刚才说了前端这个所有的条件是不是都封装到这个DTO里边那你用down get法取值就行取出来这个值判断一下它违不违空如果不违空证明前端是不是传过来这个标的类型了那你就应该对这个标的类型进行条件的一个什么呀封装我将来就要按照这个条件进行什么呀查询这个代码大家应该很熟悉吧我们用的是Lambda是那种EQ就是相等判断嘛
[07:59] 判断什么呀判断标的类型它是否等于这个值吗是不是那下来这个这些道理一样吗下来这些道理都一样你可以判断这个什么利率对吧比如我是投资人打比方我是投资人我要投钱我就看这个标的谁给的利率高我就给谁投钱是不是简单来说你是可以这么按照这个策略来投资的说这里边呢我们也可以可以根据什么利率进行查询但是这个利率呢它毕竟是数字对吧那你应该是一个什么样区间
[08:29] 比如说这个利率我想挑这个8%到10%之间的这个标底给我搜出来对吧所以它是一个区间就是大于多少小于多少你看这是不是GELE是不是大于小于这个区间是不是那么前端将来会传过来一个什么呀歧视值嘛比如说这个值假设这个值就是8%这个值就是什么呀10%就这个意思它是一个区间那它首先也要判断它无作为空嘛但由于它不是自负创它是对象
[08:58] 所以你就不能用刚才这个什么呀啊Stream YouTube is not blank你就直接跟闹啊做判断就行如果不为空那你就用Core Warp进行这个条件封装就行包括这个借款期限这个借款期限不就是这个谁吗呃借款期限我想那个图在这也有就这个嘛你你借多少多长时间了多少个月了这是不是也是一个数字一个区间吧比如说我要搜索这个借款期期限是呃6到12个月了
[09:29] 对吧或者12到24个月对不对等等等等这也是一个区间那你你也是要判断他违不违控啊然后呢小爷谁大爷谁是吧这个道理都是一样的这个配合然后呢就是一个标底的一个状态这个标底的状态呢是分几种的啊我们看这个数据库里边有没有这个注释啊标底的状态标底的状态是这个啊他没有没有
[10:02] 给直那我们去实体内抽抽实体内就是这个project看里边有出声标底的状态也没说啊这个标底的状态的话大概给大家说一下其实咱前面在保存标底新一的时候提过一个状态叫目击中不是墨击啊目击不是母鸡啊目击中这个大家应该知道什么意思就是我刚发完标嘛就等着大家给我投钱了这个过程这个所处的状态就叫什么目击中
[10:34] 那将来还有什么状态满标满标咱们以前提过一次满标什么意思比如我要借五万块钱过了一星期吧这五万块钱这个大家给我给我投过是不是五万块钱我已经这个接到手这个时候这个状态就变成什么满标了就这个意思当然他还有别的纸这只是给他举两个例子所以说呢你看这儿也有一个状态的一个判断这个状态是字不算所以说他会归为空
[11:03] 就是通过stream youtube的is not blank进行判断boykong是把这个条件也干什么呀对也给他加进去就行所以这是一堆什么呀条件的这个封装或者构造啊这个代码虽然多但是其实我们看起来还是比较眼熟的那这个代码呢我就不再从头给他敲了我就把它直接拿过来用一下然后呢下边应该是从这开始一直到这个地方
[11:40] 这里边这些格式吧大概的调一下就行了这个去YouTube呢你这个包需要倒一下啊他说我刚才说的是阿帕奇的你倒一下倒的时候一定要注意说倒他是吧然后你看好了是谁啊阿帕奇的啊我们倒这个浪三的就行了啊就可以这是咱刚才那一堆条件的什么呀封装条件封装完之后我们接下来干什么呀封装这个分页数据吧你看我们的参数
[12:19] 这里边是不是有个配置number配置size配置number是第几页配置size是一页显示段行对吧根据咱以往这个学习的这个分页的经验这两个数据是不是也要进行封装对不对怎么封装呢我们要封装成一个对象大家往下看有一个对象就叫什么呀配置对象是不是应该构造分页对象了你把这个配置number配置size这两个数据呢给封装到这个对象里边就行了后边他在执行查询那时候就要用到这个对象配置对象这里边是不是也带着范型呢对不对
[12:49] 所以说这个分页这个构造很简单就一行代码然后呢这个配件呢我们需要导一下包导哪个包呢一定是MP的嘛是不是爆米豆嘛my bet is pass我们数据访问层用的是MP嘛所以你看这个分页的我们是不是也搞定了上面是不是什么呀条件我们也封装好那还差什么呀对还差排序排序搞完之后就是执行然后封装结果是不是那我们的这个
[13:24] 查询吧我们先停一下啊一会儿呢再接着写后边这个代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

