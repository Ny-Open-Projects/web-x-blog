# day10-10-投标预览-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-10-投标预览-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 11分26秒（音频 686s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才咱们做了需求分析对吧接下来我们也说了首先要开发哪个功能第一阶段功能叫投标预览投标预览的话这个功能比较简单大家主要就是看这张图就行我们刚才明确了一下就是要查几块信息三块信息第一块就是标底的信息对吧比较利息你借多少时间借多少钱等等等等这是第一块第二块信息就是这块就是这个
[00:30] 出借记录就是目前的这个标啊已经有多少人这个投过了啊就这个借给他钱了就相当于是出借记录投标记录这是第二块的这个信息第三块信息呢就是这一块就是借款人的一些信息啊基本信息他的姓名姓名年龄啊姓啊等等一些信息所以说呢第一阶段啊就是投标预览我们就是查这三块信息然后反位前段让他展示一下就行这是第一阶段投标预览这个我们最终要达到的效果然后实现啥功能我们先明确一下
[01:00] 因此我们一共要先定义几个接口三个接口那你再看看看看刚才这个时序图你看第一个接口是不是获取标的信息的第二个接口是获取出借记录图标记录的第三个接口就是获取对借款人信息全都是查询这一块全都是查询我们分别定义三个接口搞三次查询就OK了那咱一个一个来咱先看看第一个接口
[01:30] 第一个接口呢是我们要在交易中心这边定义一个查询什么信息啊对标的信息的这个接口啊根据标的的什么呀ID啊查询标的相关的一些信息那咱是不是应该去哪定义这个接口啊定义这个方法对我们应该找到translation API这个接口啊在这个接口里边呢我们新增一个查询的方法就是根据ID
[01:57] 来查询标的相关的信息那咱先看一看讲义吧讲义里边呢咱看这个方案名字啊叫queryprojectsids哎大家看一下它这个名字里边都带着s根据咱以往的经验对有同学说不用根据经验了对我往后一看我发现它有可能传进来的是什么呀是多个id然后你再看这儿这个反而指里边这是一个什么呀
[02:25] 集合然后结合这个注释我们发现咱讲义里边定义的这个方法是可以根据什么呀多个ID是不是来查询多个标底的信息没错吧这个大家应该都能看出来啊那这里边有的朋友就会有一个疑问咱这有必要这么做吗就是一次查多个标底的信息呢那看咱这个功能我觉得是必要性不大啊因为咱这一次就是查几个标底对一个标底的信息
[02:56] 但是我们考虑到这个扩展性对不对将来我们不排除在别的地方是不是他有可能会遇到什么呀一次要查什么呀对多个标底的信息所以说考虑到可扩展性的话我们这准备就是让他将来可以干什么呀传过来多个ID然后呢查出来多个标底的信息我给他封装到一个什么呀list集合里面
[03:23] 因为你能查多个标的自然就能查什么呀对一个标的嘛所以这一块的话是需要大家注意一下的那咱接下来呢就找到这个transication API这个接口在这个接口里边呢把这个方法呢给它编写出来接口是不是都在API这个工程里呢咱找一找transication API没错吧好我们应该是在这个地方对不对把这个方法呢给它定义出来方法名的话我们要跟讲义保持一致
[03:57] 然后这个方案刚才说的有一个参数但是这个参数呢是可以传进来什么呀对多个这个什么呀ID的然后有一个返回值返回值呢最终封装的还是什么呀对rest response但是你要注意啊这里边的范形是一个对list集合那list集合里边存的就是什么呀对标底信息标底信息是用project的DTO来进行什么呀
[04:26] 对进行封装的这是咱把这个方法又定义出来然后这个注释咱也加一加吧咱就拿讲义当中的这个注释拿过来那这是第一个接口啊咱就定义好了那第一个接口定义好之后咱跟以前的套路一样吧顺手把那个扛车来一个空时线先放了应该去这儿对不对交易中心吧能找到这个扛车他现在应该要报错了呗
[05:02] 是不是咱把它生成一下就扔到这就这个方法是不是那当然这里边一些这个注解咱该补充给他补充一下吧这也都对不对SWAG的还有这个什么呀MVC的基本给他补一下这些我就不再过头说了这个大家都很熟了然后呢这个地方不要忘因为我们这个前端传过来数据我们是不是通过这个路径直接传过来就是resful的风格所以说呢你需要在这
[05:34] 千万别忘了加这个啊帕特瓦卜这个注解这个很容易忘记这咱就放到这这是第几个接口啊对第一个接口来紧接着第二个接口第二个接口我们说了是不是还获取那个出界记录或者叫投标记录的对不对也是一个查询那么这个也是定义在交易中心的啊穿着看下一篇我们又定义一个方法叫queryquery什么呀这个querytender啊tenders对吧这个tender就是投标的意思啊by
[06:05] project ID这个发明的建名之一就是根据这个标的的ID或者说查询某个标的的什么样投标记录所以说这个参数就是传过来就是一个什么样对标的来历我要查的是某个标的的这个什么样投标记录那么投标记录这个信息呢我们封装成这个对象啊叫tender overviewoverview就是预览的信息意思吗DTO对象是不是
[06:33] 由于一个标的投标记录有可能是多个所以说我们这返回的是一个什么集合进行了封装这是第二个接口我们定义的方法也比较简单我把这也给它粘过去是不是还是在transcation API里面又在这了在这个地方我们接着给它再加一个方法这是第二个接口是用来查什么对查投标记录
[07:13] 那这儿报错是不是咱没有这个类吗这个类的话我们可以从这个客架里边去找一找把它拷过来就行了咱们找到这个资料文件夹哎这里边就有这么一个类啊我们要看一看它应该是考到什么地方dq啊我们看看它是放到什么ap对吧ap这个地方好那咱就control c然后呢在ap是不是这个地方吧粘过来这就ok了对不对那这就不报错
[07:46] 然后呢还是顺带着把Controller里边的这个方法也给他生成一下这还报错吗不报错是反应慢好我们把这个方法也顺手给他来一个空时线扔到这那还是要把一些基本的注解给他加上那大家看一下这里边是不是这个前端发过来的这个参数是不是也是通过什么呀路径直接传过来所以说还是这要加这么一个注解不要忘了
[08:27] 这是第二个接口查询这个某个标底的投标记录的那接下来就是最后一个接口最后一个接口就是我们要获取刚才那个图里边的什么借款人的这个信息我要借给你钱我得知道你的一些基本信息对不对说这是第三个接口那么这个接口定义的时候这个方法就要定义到什么用户中心那边就是consumer API那定义一个方法这个方法名叫啥叫get board
[08:55] 这个包包呢其实就是什么呀出借人的意思借款人借款人的意思不是出借人借款人给他包包见名之义然后呢这个传进来的就是谁呀对借款人的那个那个用户的ID我们根据ID呢其实就是查一下这个借款人的这个信息然后封装成这个包包什么呀DTO对象就OK了也很简单那我们就把这个方法呢给他定义到这个什么consumer API当中
[09:25] 好我们找一找consumer API在下面再加一个方法这是获取借款人的用户信息的啊那这个Bover DTO不存在我们也是去资料文件家里边找一找就行了咱还是去资料文件家找一找就是他吧对不对然后咱看看应该考到什么地方API consumer那里对不对那咱就是control c然后找到这吧
[10:00] 看好了别考错地方了啊伸过来这就不报错了对吧关于这个DTO对象咱现在先不管他等后边咱具体用到的时候再说啊因为大家现在都有经验了这个DTO无非就是封装一些这个数据的一些信息的那咱接下来就应该是顺手把那个Controller里边的这个这个方法来个空时线吧就应该去哪去consumer了是吧去consumer在这consumer里边的Controller我报错了
[10:37] 我们把这个方法呢给他这个生成一下来一个空时线在这啊然后我们把基本的一些注解啥的给他加一下就这一块然后这里边还是要注意这个问题你看这几个查询这三个接口啊这三个接口三个查询全是通过这个路径来传直的啊所以说都要用到pass verb这个注解这个大家一定要注意了这是目前吧咱们把什么呀投标预览这个阶段里边涉及到了几个接口啊
[11:18] 对三个接口全部定一号定一号之后呢咱接下来就该实现功能

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲P2P平台“投标”功能的接口设计与实现，包括交易中心和用户中心相关接口的定义与代码编写。

2) 按时间顺序列出每张画面的要点：
画面1：展示PPT第1.2节“投标”，介绍借款人发标后投资人可查看并投标，引出用户投标流程。
画面2：展示PPT中的“第一阶段：投标预览(图中1.1-1.6)”流程图，图中包含“前端APP”、“交易中心”、“用户中心”、“后台管理”等模块，以及“借款人发标”、“投资人查看”、“投资人投标”、“交易成功”等流程节点。
画面3：展示IntelliJ IDEA中TransactionApi.java文件，其中包含方法声明：
RestResponse<String> projectApprovalStatus(Long id, String approveStatus);
RestResponse<PageVO<ProjectDTO>> queryProjects(ProjectQueryDTO projectQueryDTO, Integer pageNo, Integer pageSize);
画面4：展示TransactionApi.java文件，高亮显示方法：
RestResponse<List<ProjectDTO>> queryProjectsIds(String ids);
画面5：展示TransactionController.java文件，其中包含方法：
@Override
@ApiOperation(value = "借款人发标", tags = "transaction")
@PostMapping("/my/projects")
public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
    return RestResponse.success(dto);
}
画面6：展示PPT第2.2.1.2节“交易中心查询投标记录(接口③)”，内容包括接口描述和定义，提到在TransactionApi接口中新增queryTendersByProjectId方法。
画面7：展示TransactionApi.java文件，高亮显示方法：
RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(Long id);
画面8：展示TransactionApi.java文件，高亮显示方法：
RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(Long id);
画面9：展示PPT第2.2.1.3节“用户中心获取借款人信息接口(接口③)”，内容包括接口定义。
画面10：展示TransactionController.java文件，高亮显示方法：
@Override
@ApiOperation("根据标的id查询投标记录")
@GetMapping("/tenders/projects/{id}")
public RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(@PathVariable Long id) {
    return null;
}
画面11：展示Windows资源管理器，路径为“wanship2p > day10 > 资料 > 类”，显示文件“BorrowerDTO.java”和“TenderOverviewDTO.java”。
画面12：展示IntelliJ IDEA中ConsumerAPI.java文件，其中包含方法：
RestResponse<BorrowerDTO> getBorrower(Long id);
画面13：展示ConsumerController.java文件，其中包含方法：
@Override
@ApiOperation("获取借款人用户信息")
@GetMapping("/my/consumers")
public RestResponse<ConsumerDTO> getMyConsumer() {
    return RestResponse.success(consumerDTO);
}
@Override
@ApiOperation("获取借款人用户信息")
@GetMapping("/my/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(Long id) {
    return null;
}
@Override
@ApiOperation("过关卡保护资源，进行认证拦截测试")
@GetMapping(value = "/my/consumers/test", params = "jsonToken")
public RestResponse<String> testResource(String jsonToken) {
    return RestResponse.success(EncryptUtil.decode(jsonToken));
}
画面14：展示PPT第2.2节“投标预览”，内容包括“第二阶段：用户投标预览(2.1-2.13)”的流程描述，以及“2.2 投标预览”的标题。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
RestResponse<String> projectApprovalStatus(Long id, String approveStatus);
RestResponse<PageVO<ProjectDTO>> queryProjects(ProjectQueryDTO projectQueryDTO, Integer pageNo, Integer pageSize);
画面4：
RestResponse<List<ProjectDTO>> queryProjectsIds(String ids);
画面5：
@Override
@ApiOperation(value = "借款人发标", tags = "transaction")
@PostMapping("/my/projects")
public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
    return RestResponse.success(dto);
}
画面6：
在TransactionApi接口中新增queryTendersByProjectId方法：
/**
 * 根据标的id查询投标记录
 * @param id
 * @return
 */
画面7：
RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(Long id);
画面8：
RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(Long id);
画面9：
@Override
@ApiOperation("根据标的id查询投标记录")
@GetMapping("/tenders/projects/{id}")
public RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(@PathVariable Long id) {
    return null;
}
画面12：
RestResponse<BorrowerDTO> getBorrower(Long id);
画面13：
@Override
@ApiOperation("获取借款人用户信息")
@GetMapping("/my/consumers")
public RestResponse<ConsumerDTO> getMyConsumer() {
    return RestResponse.success(consumerDTO);
}
@Override
@ApiOperation("获取借款人用户信息")
@GetMapping("/my/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(Long id) {
    return null;
}
@Override
@ApiOperation("过关卡保护资源，进行认证拦截测试")
@GetMapping(value = "/my/consumers/test", params = "jsonToken")
public RestResponse<String> testResource(String jsonToken) {
    return RestResponse.success(EncryptUtil.decode(jsonToken));
}

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：架构图标题为“第一阶段：投标预览(图中1.1-1.6)”，图中包含“前端APP”指向“交易中心”和“用户中心”，“交易中心”指向“后台管理”，“用户中心”指向“后台管理”，“后台管理”指向“前端APP”。
画面6：PPT标题为“2.2.1.2 交易中心查询投标记录(接口③)”，内容包括“1. 接口描述”和“2. 接口定义”。
画面9：PPT标题为“2.2.1.3 用户中心获取借款人信息接口(接口③)”。
画面14：PPT标题为“2.2 投标预览”，内容包括“第二阶段：用户投标预览(2.1-2.13)”的流程描述。

5) 无。

