# day10-15-投标预览-接口2-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-15-投标预览-接口2-功能实现_【海量资源尽在 666java.com】.mp4
- 时长 12分21秒（音频 741s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面呢咱们把第一阶段接口1这一块的功能全部搞定了而且也测试通过那咱紧接着就开始实现接口2这块功能那这块功能呢就一个啊就是用来获取以投标记录的那对应的前端界面是这儿大家看一眼啊就是这个地方这个地方啊当我们点击这个按钮的时候呢它会新打开一个界面
[00:36] 在这个界面里边呢会展示该标的啊就这个标的都有哪些人进行了投标会把这个数据给呃展示一下所以说这呢主要就是一个什么呀查询主要就是一个查询那查到哪个表呢那查的自然就是这个tender表就这个投标信息表就这个表那根据什么去查呢我们查的是不是某个标底的投标记录吗那肯定是根据标底的这个标识就是project的小小线id
[01:06] 把这个标题的这个投标记录给他查询出来所以说这个功能比较简单只是一个查询带条件的一个查询而已那么这个DAO层的代码我们就不用编写了因为我们前面在实现接口1这个功能的时候我们是不是已经把这个tender map这块代码已经编写过了所以咱接下来直接从业务层开始就行了那业务层这块我们是不是也是在接口里边新定义一个方法然后在实现了一段时间实验这个方案就行了
[01:37] 那咱找到这个project Service这个接口在这里边呢我们新增一个方法就是接口2这个方法我们把这个东西粘过来咱一起瞅一眼大家看一下啊这个叫query tenders对吧就是查询投标记录根据什么来查呀对标底的ID我们查的就是某个标底的什么呀投标记录那么每一条投标记录将来会封装成tender overviewDTO这么一个对象
[02:12] 但由于呢一个标题的投标记录有可能是多个所以说我们最后呢是用list做了一个封装这是这个方法我们就在接口里边定义号然后呢我们去实现内容实现这个查询功能那我们先把这个方法先给它生成一下好大家看一下它生成到这个地方了啊那这里边我们跟大家说是不是就是去哪个边啊pinder表里边对不对pinder表里边根据这个谁呀project id
[02:49] 做一次查询就行了那咱先大概瞅一眼讲义啊大家看一下就是一个普通的查询我们调TenderMapper啊它的有一个方法叫Stacklist然后呢我们还是用什么呀Warp对吧进行条件的封装我们只有一个条件就是对标底的ID查完之后呢我们就得到一个集合然后呢便利集合干什么呀大家看到了我们这个查询查出来的这个
[03:19] 这个范形是不是tender而我们最终要的是tender overview detune然后发现咱遇到这个套路是跟之前都是一模一样了对不对然后做这个什么呀转换然后这里边还有一个细节就是人家投资人的手机号是人家隐私嘛对不对我们需要把它隐藏掉其他的基本上跟咱们平时的查询没有啥区别那咱接下来把这个代码呢我们快速的写一下首先的话我们就是直接调slack list的方法来通过这个某个条件来进行查询就行
[03:49] 那我们在这呢就开始编写这一块代码调用啊do层的有个方法叫叫叫叫什么呀select list这里边是不是封装条件啊我们的条件呢就一个就是那个标的id那我们这怎么写呢这个过程大家应该比较熟悉了啊啊我们应该是调用的是哪个条件对
[04:16] 我们先是调用lambda对吧我们是lambda写法我们这儿是没有这个点这应该是lambda query是不是我们是查询然后条件是什么EQ然后我们根据哪个字段是不是根据tender里边的谁对project ID值就是传过来的谁ID这就是我们封装好的查询条件然后把这个条件
[04:47] 扔给slack list的方法他就帮我们进行了这一次查询然后呢我们直接就可以用一个list的集合来进行接收了好我们接受一下接收完之后其实我们这次查询就搞定了对不对搞定完之后呢我们刚才说了我们需要做一些处理什么处理呢就是说呢大家也看到了啊我们查出来的这个范形是tender但是我们最终要的是tender overview什么呀对dto对象所以我们既然要做一个转换那咱跟之前一样先
[05:24] 提前创建好一个范形式DTO的list先准备好这个空气盒将来呢往里边存东西就行这个起啥名字都行NeoARA list然后呢接下来我们开始做转换这个转换的代码咱之前是不是有的时候是单独摘出来放到一个方法里边那我们这的话就直接写到这吧这个大家可以根据自己的情况Tender list我们还是用最近的这种写法否一起
[05:57] 就喇嘛的这种写法会方便一些对就是这种写法那在这个大管号里边呢我们要完成这个转换怎么转换呢其实跟咱以前的代码基本上是一样只不过现在换成了喇嘛的这种写法而已我们先创建一个DTO对象对不对NEODTO对象然后呢我们是不是要把集合当中每个tender对象的属性的值是不是来付给这个谁啊DTO对象
[06:25] 那我们一个一个复活是不是太麻烦了我们以前的套路是什么呀用这个谁啊对YouTube的Corpi Properties方法没错吧然后呢第一个对象就是Tender第二对象就是这个什么呀DTO对象这基本上我们就完成了这个什么呀对完成了转换但是这里边还没完啊我们前面提到过我们说了这里边的包含有什么呀
[06:53] 包含有投资人就是投标人的手机号啊咱今天来去tender里边抽一眼tendertender里边呢咱找一找这里边呢我们看看应该是有一个什么呀我们找找啊呃呃有一个应该是应该是这个consumer username啊这个呢就是说是投标人的用户名但这个用户名呢我们将来投标的时候呢其实是把投资人的手机号
[07:26] 存到这儿我们现在刚才在进行查询的时候肯定查出来这个手机号但是这个手机号呢我们对外展示的时候这个手机号相当于人家隐私嘛对不对你直接就把这个手机号直接就爆料到我们的平台上给别人看这个不合适这个不合适我们要保护这个人家个人的隐私所以说呢这个手机号我们查出来之后在这个前端展示的时候我们要给它加一层这个什么呀保护措施就是把里边的
[07:55] 比如说手机号中间那几位给它变成星号做一个个人隐私的一个保护所以说这个值我们需要单独做一个处理单独做一个处理怎么处理呢我们这儿呢写好了一个工具类大家瞅一瞅啊我给大家找一找专门针对这个手机号一个工具类叫Coreman YouTube这么一个工具类工具类当中呢你看我们写了这么一个方法叫Hidden Mobile就是隐藏手机号嘛对不对
[08:25] 这是你传过来的原始的手机号然后呢经过我们的处理会返回给你一个字符串但是这个字符串里边呢呃这个部分这个手机号当中的部分这个信息被隐藏掉了替换成星那这里边大家看这个代码其实我们就是调用字符串的replace all方法做了一个什么替换大家看这是正则两式我们的手机号不是11位吗这是前三个数字这是后四个数字这是中间的四个数字一共是多少位
[08:56] 是不是11位那后边这个写法指的是dollars1指的是这个第一个组dollars2指的是第二个组那中间是不是四个星啊那整体这行代码的意思就是把手机号当中中间的这个四个数字给它切换成什么样型号具体的效果我这有个例子大家看一下你看我是不是传过来一个手机号然后呢调用这个方法接下来大家看看它会产生什么效果一看到这个效果你就知道啥意思了现在明白咋回事吧
[09:25] 也就是把人家投资人的这个手机号这个中间这几位给他隐藏掉就行了所以说我们接下来呢要调这个工具类的这个方法对手机号这一块做一个处理那怎么处理呢那就是我们这么写就行了我们直接就是调用turned over view detail调用它的这个setter方法把它的值重新改一下改成那个中间是星星的对不对
[09:53] 那我们需要做处理啊需要调用这个cormacommoncormonyoutube的hidden什么mobile方法然后把这个原来的这个手机号给他干什么呀对给他传过去原来的手机号我们是不是通过getter方法不就得到了是不是因为前面在做这个copy properties的时候呢我们已经把这个手机号是不是呃付给这个什么dto对象
[10:24] 所以你再用getter方法把这个原始的手机号取出来然后扔给这个工具类让他做处理处理完之后呢我们再存进去这个时候我们存进去的这个手机号里边是不是在中间的四位就已经变成什么星星那我们就是多了这么一个处理而已处理完之后呢这个我们就需要把这个DTO对象是不是往集合里边来存了开始往集合里边来存就是什么呀Tender Overview DTO对吧
[10:55] 这样子的话我们就完成了转换最后呢我们要把谁给返回啊对这个例子的集合给他返回就行了哎这个事情我们就全部搞定啊所以这个查询箱来说比较简单那右层代码写完之后呢咱顺手把Controller的那个代码完善一下就行了Controller我们找一找Controller是在这对吧Controller的代码也比较简单是这个地方吧对不对
[11:27] 我们只需要调用一下业务层就OK了就projectservice.咱刚才的那个方法是不是叫querytendersby什么呀对byproject的ID然后呢把这个ID这个参数给他传过去就行了然后这时候你就得到那个投标记录就是那个集合了对吧但是这个集合呢我们不能直接就干什么呀返回以前呢我们是不是要封装成rest response
[11:56] 我们调用它的success方法直接就完成了封装把我们查出来的这个集合呢我们给它扔进去然后直接干什么呀对返回那么这个Controller代码我们就玩上那目前的话我们就把这个什么呀对第一阶段接口2这块功能全部搞定一会咱们进行功能测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

