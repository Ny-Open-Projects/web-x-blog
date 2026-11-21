# day10-11-投标预览-接口1-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-11-投标预览-接口1-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 16分31秒（音频 991s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把第一阶段就是投标预览这一块业务当中的三个接口呢全部定义好那接下来咱按照顺序先实现第一个接口的功能第一个接口呢就是获取标底的基本信息这个比较简单吧但是呢这儿呢我们需要稍待着再查一个东西什么东西呢大家看这儿看这个前端界面大家看一下
[00:32] 这块是不是就是标底的这个基本信息对吧那我们在查这个信息的时候呢我们准备把这个数据给他查出来那么将来你点击这个按钮的时候是不是会查到那个投标记录这个呢是第二个接口他要实现的功能啊但是我们把这个人数啊就是多少人出界这个人数呢放到咱第一个接口里边一块给他实现这是我们把第一个接口里边要实现的功能我们再明确一下那咱
[01:02] 按照顺序的话是不是应该是先DAO层然后再要层是不是那DAO层这块咱想一想查标题信息这个DAO层这个代码咱不用编写了吧因为以前都写过了以前咱查过这个标题信息嘛是不是所以说这块的这个DAO层代码咱不用管那咱主要是把查询这个什么呀对图标记录或者说图标人数
[01:25] 这个do层的代码我们需要编写因为这是涉及到图标这一块的啊这是这个do层的代码咱以前没有写过那咱就定义一个map解口呗我把这些都关掉map解口这应该定义到什么地方这个是不是应该定义到我们的交易中心吗是不是交易中心transication然后找到这个谁呀map解口你看这个跟标的有关呢这个do层的代码我们已经写过了之前
[02:01] 现在再增加一个投标的我们定义的是接口啊就叫tndr这个单词咱前面提过吧这个tender是不是就是投标的意思吗tender mapp让大家简单回顾一下我们现在使用的是mybattles plus是吧那在定义do层的时候需要怎么着需要继承谁啊对继承base map
[02:35] 那这里边还有一个范形就是这个图标的实体类啊tndr好我们把注释也加一下那这个接口其实就是将来用于什么呀对用于操作什么信息啊投标信息的Mapper接口那我们一会通过这个接口就可以实现哪个功能啊对就可以实现查询这个什么呀这个出界人数
[03:10] 先把它这个功能给搞定这是接受定好接受定好之后呢我们接下来是不是还要定义相配套的这个xmr文件就是应用车配有念我们通过咱以前的这个菜单那就创建好这个名字呢我们还是叫t e n d rm a p p r那这里边是不是只需要把那个map解口的路径给放到这就ok了啊c n点i d c u s点
[03:44] 然后继续点map是吧里边的刚才定义的tender map这搞定了啊dao层的代码就搞定第五层代码搞定之后呢咱接下来就开始编写右层的代码那咱找一找咱之前写的业务层的代码就是这个project Service大家应该还有印象咱要不曾是不是也是一般定义一个接口然后在实现类当中去
[04:15] 定义一个方法对吧然后在实现内容当中去实现这个方法那咱这呢就需要补充一个方法这个方法呢基本上跟咱control的那个接口里边定义的方案差不多啊咱进来一起看一看就这儿呃前面在定义接口的时候大家对这个方案应该有印象吧我们当然说的是什么呀是可以传进来多个这个ID啊把多个标题的信息一块查出来然后呢封装成一个集合还有印象吧
[04:42] 那我们现在只需要查一个标的那是不是这个方法同样也适用吗那咱就把这个方法定义到业务层的这个接口里面我们新增一个方法在project Service里面然后呢我们去这个实现类当中开始实现这个方法就准备呢开始把接口一里边功能给实现咱找到这个这个咱得先生成一下是不是这已经报错了
[05:18] 咱把他的这个方法给生成一下然后开始实现功能好大家看就是这儿那这里边咱都需要编写什么代码实现什么功能呢咱接下来先简单分析一下首先呢我们说我们要实现第一个功能就是查询标的信息没错吧还有一个功能就是查询什么呀出借人数你再看这个图
[05:54] 这块是不是标的信息吗这儿是不是这个出界的人数吗所以我们在这个方案里边呢主要是实现这两个功能的那咱接下来一个一个来吧第一个查询这个标的信息这个比较简单吧怎么查呀哎这里边大家要注意一点啊就是说呢呃咱们这个方案设计的时候是不是这个地方这个仓上是不是可以传进来多个什么id啊我们要考虑这种情况所以说这个地方我们要这个仓上要做处理
[06:24] 我们要进行分割嘛这个传参传过来的这个数据中间是用逗号分割的啊是一个字符串你看正类型的所以他多个id之间一定是用逗号分割所以我们这呢也要按逗号进行分割然后拿到每一个什么呀id然后呢再进行什么呀查询所以说呢我们这呢应该先对参数做一个处理怎么处理呢那就是id.split的方法按照什么来分割呀逗号
[06:54] 那分割出来的是一个什么东西啊是一个数组吧对不对大家看这个splay的方法是不是死生类型的一个数组然后咱为了这个接下来操作方面我准备把它转化成集合怎么转化成集合呢咱有个工具类叫A A A Y S等一下吧Arrays它有个方法叫AsList看到没有然后呢它就要的是一个什么数据咱就可以放进来那么
[07:26] 转换完之后呢你看他咱得到的是不是就是一个例子的集合里边范形是不是那现在这个集合里边存的是不是就是每一个什么呀对每一个ID那得到这个ID之后呢得到这个ID之后呢我们现在这个ID咱还用不了啊为啥用不了因为你看他现在这个ID是不是都是字数上来想那咱查到时候呢这个ID呢他可不是字数上来想他是数字来想啊整数
[07:53] 所以说我们接下来呢要做一个类型转换要把每个ID从字符刷转成这个整数那这个地方怎么转换呢我调用一下这个东西就栏目表示这么写大家看一下非一起这里边呢这么写STR然后栏目表示的语法大家有印象吧是不是这样子对吧然后里边呢我们接下来是一对大拇号在这个大拇号里边呢我们就要编写代码来实现类型的转换
[08:27] 我们要给他转换成长整形长整形怎么转换呢我们使用包装类那他有个方法叫帕斯拉然后呢把这个st啊干什么呀扔给他就行哎他转换返回的就是一个什么呀对返回的就是一个长整形的一个什么呀id那这个id呢我们要声明一个集合单独给他存一下啊这个集合咱起个名字就叫lis了吧
[09:01] 等于neo a i a list然后呢我们在这转换完之后给他存进去list.add这样子就可以了大家看一下我们首先写了一块代码这个代码呢主要是处理这个参数的因为这个参数里边呢它是一个字母串中间是用逗号进行分割的这个一堆这个什么呀标底的id所以说呢我们先用split的方法把它分割成字母串数组然后通过as list的方法转换成集合
[09:37] 然后通过蓝表式的写法把集合里边每个字符串类型的ID给它转化成对长整形然后存到了这个集合里边那现在这个集合里边存的就是数字型的啊一堆什么呀ID那咱既然拿了它就可以进行什么呀对查询了怎么查呢我们还是用query warp呗对还是这套东西query warp这里边的范形就是
[10:07] 我们查的不是标的吗就是project先把这个querywarp对象给它new出来再说等于newquerywarp我们这不是带条件的查询吗要根据ID嘛查询这个标的信息嘛所以我们要用querywarp对象先封装条件那么这个条件我们用什么类型的条件呢什么样的条件呢大家知道我们现在手头上是不是有一个集合集合里边是不是有一堆这个标的ID对吧那想在这种情况下我们应该怎么进行查询
[10:41] 因为他想到用什么查询用来用查询是不是应该用印查询印字查询是不是一啊那在这个块warp里边呢他也提供了一个方法就是印方法这个咱以前在讲mp的时候应该是给大家这个呃讲过这个东西的具体怎么用呢我们还是用这个lambda比R式的这种写法lambda你看他有一个什么呀一啊印字查询那这里边就要封装条件啊呃就是说我要
[11:10] 这个根据哪个字段进行查询呢根据ID嘛是吧P project get谁呀ID值是多少呢值是不是来自于那个集合嘛就是这个谁呀对list这个集合对list集合那最终呢它封装出来的这个条件其实就长这个样啊前面就是那个查询语句嘛我就不再写了那么后边条件就是where什么呀ID干什么呀in你明白什么意思吧
[11:44] 这里边就比较一啊多少二多少三多少四就这个样子这个ID不就是咱这一块内容吗那么后边小五号一二三四五这些值不就来自于这个什么呀集合吗人家印这个方法它就起这个作用了所以这是咱把条件封装好条件封装好之后接下来就要进行什么呀对就要进行查询了怎么查呢这个就要用到MP在业务层封装好的一个方法这也是咱以前用过的就是List的方法就是它
[12:12] 我们把这个query warp对象给它扔进去然后反而它是不是就一个list集合我们就可以接收一下声明一个listproject我们起个名字叫projects其实这一步就是在执行什么查询当然如果你将来这ID传过来的是三个ID这应该就会查出来三个标的如果你传过来是一个ID这查出来就是一个什么
[12:42] 标的信息大家能理解吧这就是在做查询啊那查完之后呢查完之后呢一般我们都要做一件事什么事因为你看我们返回的这个范形是什么范形啊DTO对吧我们这查出来的是什么呀Project所以说我们接下来一般要做什么事对所以说要做转换就是把Project转换成DTO对象那我接下来是不是得先提前创建好一个
[13:14] project DTO 范形的list 集合先准备好对不对那起个名字叫 DTOS 吧等于NeoRelease 先准备好啊转换完了这个对象是不是就存到这个集合里边那接下来这个转换的话我们就用4圈环吧可以吧就用4圈环啊我这加点注释吧呃这是查询标的信息是不是那这呢相当于就是该干什么的呀
[13:45] 对该进行转换转换为DTO对象那我们就来一个Full一起循环了那这里边的话呢就是怎么写Project后边要编列哪个集合呀是不是Project是不是然后就开始循环它循环的过程当中呢我们取出来每个对象然后呢调Convert的方法是不是就完成了转换Convert对象Convert的方法我们以前是有是这个吧
[14:25] 对大家看好别掉反了我们应该不是这个应该是这个是吧你别掉反了然后把这个谁project对象给他扔进去这不就完成转换了吗然后我们接受一下project的DTO是不是在这个学案当中我们就把每个project的对象就转换成了什么DTO对象然后接下来接下来大家注意了我们
[14:57] 还要封装一些别的一些信息我们还要封装啥信息呢咱可以进到project DTO这个对象里边咱瞅一瞅你看这里边的话你看这些信息是不是随着刚才这个标题的查询就有了对不对但是还有一些东西需要咱单独去查询的还有哪些呢来我你找找啊你看这他这里边是不是有个剩余额度对不对你看咱前端是要这个东西的你看这这是不是有个剩余的额度对不对
[15:28] 这个是直接是查不出来了需要我们进行处理还有是不是这个信息咱刚才提到过了对不对说这两个信息我们要进行查询或者说处理处理完之后呢我们还要封装到这个地球对象里面你看这有声音额度你看这是不是就那个人说吗对吧出街的人说我们现在还要搞定这两个事那我在这先把这个注释写上啊就是说呢我们还要做什么事一个事儿是不是就是这个查询出街人说这个咱刚才说过
[16:01] 还有一个事就是要获取什么呀对剩余额度这个剩余额度什么意思呢比如说人家要借三万块钱那已经有人借给他一万那就是还剩多少还剩两万就这个意思啊我们需要达到这个剩余额度还有这个出借人数然后一起封装到的这个什么呀DTO对象里面然后这个功能就搞定那这两个功能咱一会单独再实现

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个项目投资审批流程的系统架构图，并通过IDEA展示相关服务层代码实现，重点讲解如何通过LambdaQueryWrapper进行条件查询和数据转换。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示系统架构图，包含“浏览器/App”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”等模块，以及它们之间的交互流程（如1.1~1.6、2.1~2.7等步骤）。
画面2：IDEA项目结构，显示“wansin2p-transaction-Service”模块下的目录结构，包括src/main/java、resources等。
画面3：多窗口切换，显示“wansin2p_apollo”项目、前端页面、数据库工具等，但无具体代码或配置。
画面4：IDEA中显示“ProjectService.java”文件，展示方法签名和参数。
画面5：IDEA中显示“ProjectServiceImpl.java”文件，展示“projectsApprovalStatus”方法的实现，包含调用“restResponse”和“updateProject”。
画面6：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjects”方法的实现，包含“contentSearchAgent”调用。
画面7：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法的实现，开始处理字符串数组。
画面8：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法中使用“Arrays.asList”和“Long.parseLong”。
画面9：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法中创建“QueryWrapper”对象。
画面10：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法中使用“QueryWrapper.lambda”进行条件查询。
画面11：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法中使用“LambdaQueryWrapper”进行条件查询。
画面12：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法中使用“Bindings”进行数据绑定。
画面13：IDEA中显示“ProjectDTO.java”文件，展示类中定义的私有字段，如“requestNo”、“remainingAmount”、“risk”、“tenderCount”。
画面14：IDEA中显示“ProjectServiceImpl.java”文件，展示“queryProjectsIds”方法中使用“for”循环将“ProjectDTO”对象转换为“Project”对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
String projectsApprovalStatus(Long id, String approveStatus).
```
画面5：
```java
@Override
public String projectsApprovalStatus(Long id, String approveStatus) {
    // 根据当前审批信息并转换为DTO对象
    Project project = getById(id);
    ProjectDTO projectDTO = ConvertProjectEntityToDTO(project);
    // 生成流水号
    projectDTO.setOrderNo(CodeGenUtil.getW(CodePrefixEnum.CODE_REQUEST_PREFIX));
    // 通过远程调用查询事务服务，把招标信息传递过去
    RestResponse<String> restResponse = contentSearchAgent.createProject(projectDTO);
    if (DepositoryReturnCode.RETURN_CODE_00000.getCode() .equals(restResponse.getResult())) {
        updateProject(project);
        return "success";
    }
    return "fail";
}
```
画面6：
```java
@Override
public PageVO<ProjectDTO> queryProjects(ProjectQueryDTO projectQueryDTO, String order, Integer pageSi, String sortBy) {
    RestResponse<PageVO<ProjectDTO>> esResponse = contentSearchAgent.queryProjectIndex(projectQueryDTO);
    if (!esResponse.isSuccessful()) {
        throw new BusinessException(CommonErrorCode.UNKNOWN);
    }
    return esResponse.getResult();
}
```
画面7：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
}
```
画面8：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
}
```
画面9：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
}
```
画面10：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
    queryWrapper.lambda().inId(List.of(1, 2, 3, 4, 5));
}
```
画面11：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
    queryWrapper.lambda().inId(List.of(1, 2, 3, 4, 5));
}
```
画面12：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
    queryWrapper.lambda().inId(List.of(1, 2, 3, 4, 5));
}
```
画面13：
```java
private Integer idassignment
private String requestNo;
// 风险等级
private BigDecimal remainingAmount,
// 风险等级，目前默认B
private String risk = "B";
// 出借人数
private Integer tenderCount
```
画面14：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 查询用户信息
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        Long.parseLong(str);
    });
    queryWrapper.lambda().inId(List.of(1, 2, 3, 4, 5));
    List<Project> projects = new ArrayList<>();
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3. 获得剩余金额
        // 4. 查询出借人数
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，包含“浏览器/App”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”等模块，以及它们之间的交互流程（如1.1~1.6、2.1~2.7等步骤）。
画面3：无PPT标题或架构图。
画面6：无PPT标题或架构图。
画面10：无PPT标题或架构图。
画面11：无PPT标题或架构图。
画面12：无PPT标题或架构图。
画面14：无PPT标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

