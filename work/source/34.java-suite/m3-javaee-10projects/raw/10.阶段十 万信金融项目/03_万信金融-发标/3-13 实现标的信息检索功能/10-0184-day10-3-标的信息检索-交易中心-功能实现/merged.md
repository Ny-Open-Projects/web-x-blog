# day10-3-标的信息检索-交易中心-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-3-标的信息检索-交易中心-功能实现_【海量资源尽在 666java.com】.mp4
- 时长 3分43秒（音频 223s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好我们刚才呢把两边的接口全部定义好了一个是交易中心的一个是内容检索服务的啊两边接口全部定好接下来咱就该实现功能然后首先咱们实现交易中心这边功能交易中心这边主要干啥那主要干啥的话你看这个图就看出来了呗交易中心第一个是要接收扣端前端发过来的这个请求要封装这个参数对不对然后呢再把这个数据通过发起非应请求传给谁啊
[00:30] 传给内容检索服务这边所以交易中心这边其实主要就是一个非硬的一个远程调用那交易中心这块代码我们刚才说了这块代码我就不在现场编写了啊我给大家过一遍下去大家自己编写一下就行了那咱看看交易中心这边的功能实现首先我们刚才说了你是不是要通过非硬进行远程调用吗所以说你要先定义一个非硬代理大家看这个代码很熟悉吧这些代码咱之前经常写非硬client注入物件是吧然后呢
[01:01] 我们以前在写这个代码的时候提醒过大家注意什么地方对这个路径里边是不是要加上这几是不是咱以前入过坑这几要加上然后这些参数反应值我都不再说了这个大家都知道这是我们第一步交易中心这边要先定义一个分析代理第二步我们就是要搞业务层了这里边不涉及到数据法案层因为我们是要远程调用谁
[01:28] 内容检测服务让他那边从也是里边进行查询的啊这块不涉及到数据库所以我们直接搞业务层就行那业务层也是在接口里边新增一个方法叫curryprojects就不再说了这些参数反应值大家都知道然后呢就是在实现类里边实现这个方法来看一看吧这块代码看一下那我们刚才说了这个交易中心这边主要是要发起那个什么呀非语言声调用的啊所以说呢这呢要先把非语言代理对象先干什么先注进来
[01:57] 然后呢具体的这个功能代码咱一起看一看你看上来是不是就是通过这个代理开始发起远程调啊这儿呢代码一执行是不是就到哪了呀对就到内容检测服务那边那边就要进行对数据的一个查询了啊从ES索引库里面你看把这个他接收到的什么呀条件啊分页的数据啊排序的数据啊一股脑全给扔过去那边处理完之后返回的是不是这样一个类型的数据对吧
[02:27] 配置view里边是project DTO然后是封装成rest response过来那这个结果我们就拿手拿手之后呢我们是不是要干什么要判断一下有没有成功对吧有没有这个正常的接收到数据如果没有抛一个异常如果没有你就抛一个异常那如果没有出问题的话我们要干什么我们是不是要把这个数据给反映配置view是不是配view在哪配view在这个对象里边
[02:56] 那么怎么从这个对象里边把数据取出来呢我们需要调哪个方法对get result这个rest response嘛大家应该有印象但这个返回到这个数据其实是存到result里边我们调它的get fun就拿手拿手的东西就是这个配置标就查出来的分解数据啊直接作为反应值返回就行所以你看这块代码很简单主要就是一个非硬的一个远程调用那要求你搞完之后呢就是control了这块代码你完善一下就行了呗
[03:24] 把这个source注进来这儿调一下这个方法就OK了这块就不再说了这些代码咱之前编写过很多次了说说这个代码大家下去自己编写一下就行了咱一会儿重点是要编写的是哪一块代码对内容检索微服务那边的这个代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Feign 客户端调用内容搜索服务，实现交易中心对项目数据的分页查询功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程PPT的“4.1 需求分析”章节，包含一个系统交互流程图，图中“调用方(APP)”指向“交易中心”，“交易中心”指向“内容搜索服务”，“内容搜索服务”指向“ES集群”，并标注了数据流向和交互步骤。
画面2: 展示“4.6.2.1 交易中心的查询功能”下的“1. 定义Feign代理”部分，代码为：
@FeignClient(value = "content-search-Service")
public interface ContentSearchApiAgent {
    @PostMapping(value = "/content-search/l/projects/indexes/q")
    RestResponse<PageVO<ProjectDTO>> queryProjectIndex(
            @RequestBody ProjectQueryDTO projectQueryParamsDTO,
            @RequestParam Integer pageNo,
            @RequestParam Integer pageSize,
            @RequestParam(required = false) String sortBy,
            @RequestParam(required = false) String order);
}
画面3: 与画面2内容相同，仅光标位置不同。
画面4: 与画面2内容相同，仅光标位置不同。
画面5: 与画面2内容相同，仅光标位置不同。
画面6: 展示“3. 在ProjectServiceImpl类中实现该方法”，代码为：
@Autowired
private ContentSearchApiAgent contentSearchApiAgent;

@Override
public PageVO<ProjectDTO> queryProjects(ProjectQueryDTO projectQueryDTO,
        String order, Integer pageNo, Integer pageSize, String sortBy) {
    RestResponse<PageVO<ProjectDTO>> esResponse =
            contentSearchApiAgent.queryProjectIndex(projectQueryDTO,
                    pageNo, pageSize, sortBy,
                    order);
    if (esResponse.isSuccessful()) {
        throw new BusinessException(CommonErrorCode.UNKNOWN);
    }
    return esResponse.getResult();
}
画面7: 与画面6内容相同，仅光标位置不同。
画面8: 展示“4. 完善TransactionController中的代码”，代码为：
@PostMapping("/projects/indexes/q")
public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody
        ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize,
        String sortBy) {
    PageVO<ProjectDTO> projects = projectService.queryProjects(projectQueryDTO,
            order, pageNo, pageSize, sortBy);
    return RestResponse.success(projects);
}
画面9: 展示“4.6.2.2 检索服务标的查询功能”章节标题，下方有“1. 新建一个业务层接口ProjectIndexService:”的提示。
画面10: 与画面9内容相同，仅光标位置不同。
画面11: 与画面2内容相同，仅光标位置不同。
画面12: 与画面2内容相同，仅光标位置不同。
画面13: 与画面9内容相同，仅光标位置不同。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2:
@FeignClient(value = "content-search-Service")
public interface ContentSearchApiAgent {
    @PostMapping(value = "/content-search/l/projects/indexes/q")
    RestResponse<PageVO<ProjectDTO>> queryProjectIndex(
            @RequestBody ProjectQueryDTO projectQueryParamsDTO,
            @RequestParam Integer pageNo,
            @RequestParam Integer pageSize,
            @RequestParam(required = false) String sortBy,
            @RequestParam(required = false) String order);
}
画面6:
@Autowired
private ContentSearchApiAgent contentSearchApiAgent;

@Override
public PageVO<ProjectDTO> queryProjects(ProjectQueryDTO projectQueryDTO,
        String order, Integer pageNo, Integer pageSize, String sortBy) {
    RestResponse<PageVO<ProjectDTO>> esResponse =
            contentSearchApiAgent.queryProjectIndex(projectQueryDTO,
                    pageNo, pageSize, sortBy,
                    order);
    if (esResponse.isSuccessful()) {
        throw new BusinessException(CommonErrorCode.UNKNOWN);
    }
    return esResponse.getResult();
}
画面8:
@PostMapping("/projects/indexes/q")
public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody
        ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize,
        String sortBy) {
    PageVO<ProjectDTO> projects = projectService.queryProjects(projectQueryDTO,
            order, pageNo, pageSize, sortBy);
    return RestResponse.success(projects);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: PPT标题为“4.1 需求分析”，下方流程图结构为：
- “调用方(APP)” → “交易中心”
- “交易中心” → “内容搜索服务”
- “内容搜索服务” → “ES集群”
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用方(APP)” → “交易中心”（回指）
- “交易中心” → “内容搜索服务”（回指）
- “内容搜索服务” → “ES集群”（回指）
- “ES集群” → “内容搜索服务”（回指）
- “内容搜索服务” → “交易中心”（回指）
- “交易中心” → “调用方(APP)”（回指）
- “调用

