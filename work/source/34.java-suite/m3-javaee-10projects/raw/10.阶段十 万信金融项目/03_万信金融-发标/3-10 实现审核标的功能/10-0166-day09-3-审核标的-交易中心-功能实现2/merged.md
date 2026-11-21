# day09-3-审核标的-交易中心-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-10 实现审核标的功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-10 实现审核标的功能\day09-3-审核标的-交易中心-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 12分43秒（音频 764s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那咱接着实现功能那首先咱实验第一步第一步就是根据ID查询这个标题信息转成D丢这个对于大家来说非常简单了那根据ID做查询用哪个方法叫get什么呀get什么呀对就叫get by ID大家看到这个方法然后把ID扔进去就这么简单这就完成查询了但是它返回的是一个什么类型的对象被projectproject但我说我们将来传输数据的时候不是传的project的而是要转成什么呀
[00:34] 对转上dto对象啊所以说我们现在要完成一个转换这个咱以前有没有写过这方法有吧你看这儿贴调用就行了咱以前已经有过这个方法那在这就直接调用呗然后把谁扔进去啊把project然后出来的就是什么呀project的dtoproject的dto那将来呢我就需要把这个对象是不是进行传出就行了啊这报错是啥意思
[01:11] 哎呀他这个他这是反的是吧他是把DQ转成安排那不行啊那不行咱现在是反着的一个要求那咱从简安里边把这个发口就行你自己改造一下也行应该是在哪呢应该是在这个地方这那你就放到这个方向的下边呗我们现在是要把project转成什么呀DQ而咱以前这个是DQ转成project是不是就咱这样需要
[01:52] 需要再加一个方法好这就完了咱现在应该调的是这个方法在上面这要换一换好这就完成转换了将来我就可以把DTO对象放到这干什么传入过去在传入之前我们说了是不是这要生成一个流水号这个流水号大家之前有印象吗我们是怎么生成的说通过一个工具类叫code什么Utilcode numberUtil它有一个方法叫get什么number
[02:27] 那么这里边还需要通过一个枚举就是大家看到有个扣的prefix code因为不同交易它前面潜跃是什么不一样的咱看咱这个交易应该用的是哪个咱应该是扣的prefix code点应该是request就用它生成流水号的我们可以点进去看一下请求流水号潜跃对吧
[03:01] 这个是当时那个什么呀标的号和这个哎我们应该是用哪个呢我咱这是发请求的发请求应该是用这个咱们是托飞发请求吗应该是用这个啊没有错就用这个然后呢这个流水上上升成之后你要存到这个dto对象带着一块过去吗因为银行那边他有用第二set什么呀叫set我们找一找有一个方法
[03:31] 叫set request numberrequest number对就他然后把生成的流水号给他放进去这一步也就搞定了接下来我们就通过飞把 DTO对象是不是给他发过去就行了通过飞行代理的话我们是不是需要先注意一下在最上面就在这我们复制一下我们刚才定义的代理证明对吧depository我们要改一下DPO
[04:11] 然后我们找一下就是他了注入进来之后我们在这就可以调用他的方法在这个地方对吧点他就这一个方法create project然后把project的dto给他传过去大家注意了这一步这一步在我们实际图里边其实走的就是哪就是2.2标的信息同步其实说白了就是交易中心把dto对象通过分
[04:48] 远程访问存款代理服务然后给他发过去发过去之后呢从我的代理服务那边是不是开始走2.3一直到什么呀2.8对不对这块代码咱一会单独要在存款代理服务那边去实现现在你先不用管那我们这边处理完之后他是不是应该要返回有一些值是不是反映一下值我们这边要做什么呀接收他返回的是什么值呢你查一下这个方案不就知道了他返回的是一个rest response然后呢范形是什么类型啊
[05:18] 对sprint类型我们就用这种类型做一个接收就行了接受一下处理的结果rest response然后整个远程访问代码这一块咱是不是写了写完之后接下来我们说了是要判断结果对不对判断结果到底是一个什么值从而决定我是要修改状态还是要干什么对抛一场这个怎么判断这一块的话我们定义的也有一些枚举类
[05:51] 我们也需要参考讲义查一查我们应该是用哪个我们找一找就这个地方这个代码我就拿过来了它其实就是一个判断只不过这里边涉及到要用枚举咱看看这个代码就行了你看这个rest response不就是存在戴利福那边处理完返回的结果封装这里边给他入道他其实要拿到字符上的结果结果会是什么值我们要跟谁做判断
[06:27] 我们这有美酒我们可以点进去看一下这个东西是直接拿用五个零就表示什么呀成功啊这个咱之前在开会还是哪个地方是不是用过那一旦是这个值的话就表示是不是那边处理成功了处理成功之后我这边就要做什么事对我就要修改状态这个你也要看那个实际图看这标的信息同步成功之后你看这边就要干什么呀要数据状态要改成什么呀你发布是不是
[06:58] 如果也有可能会出现什么失败的情况我们就要干什么跑一场我先把失败的情况代码写一下我们跟以前一样抛一个我们自己new的什么business bu封装的自己封装这里边的话我们也封装好了一个异常的类型叫transcationaircode在这就是它点
[07:29] 我们这个应该是属于选择哪个有合适的吗我们应该是我们应该选择这个15013就从来代理服务那边反正是处理失败了我们看一看有没有更合适的把这个值的话你觉得没有合适的话你可以自己定义去美举类里边自己加就行你也可以改这里边值比如说我们选的是13你可以改成从来代理服务什么
[07:59] 审核标的处理失败或者怎么着咱这个名字你可以自己定义啊自己改这我这就挑一个这个150113反正那边失败之后呢我就跑一个一程那如果成功的话这边我是不是要修改那个什么呀那个状态把它改成什么呀已发布是不是修改咱以前做过怎么实现我们就用这个W那个叫什么WRAPP一样子就用它吧
[08:29] 他们有一个方法我们找一找叫lambda update是不是用这个更简单不用创建对象update然后然后的话我们要调用他的方法什么方法修改修改你想想我要告诉他我修改哪些字段修改成什么值然后我要根据什么条件进行修改这里边都有相关的一些方法比如说赛的方法赛法就是来设置你要修改哪个字段以及把它改成什么值的我现在修改的是哪个字段对staters
[09:03] project哪个呢就是这个啊叫同步不同步的那个状态get status就是它所以这是我们要确定改哪个字段改成什么值呢改成什么值的话我们要怎么着改成什么值的话其实这个值不就是我们就从这儿获取了就是它就是前端传回来那个那个1嘛就是它我们就拿它去用就行
[09:35] 一的话一比二成功一的话但是这是字符串它这个是什么类型它这个是integer所以说我们这还要做一个转换怎么转换就integer.parseInt然后把参数给它正面了对这个就是我们要修改的什么对要修改的值然后设置完之后还没完我们还需要接着去调用方法就设置条件我是要修改哪个标底的状态是不是
[10:07] 所以我们有一个判断这个判断是不是就根据 ad进行判断那就是project我们要得到他的什么id值不就是他传过来的谁ad就参数就这个我们这需要加我们这需要加一个分号对不对我们看一下这里边报了一些错误我们看这是什么意思
[10:43] 这个地方不知道大家有没有印象我们在使用Varps的时候这个地方需要设置范形就是这个project需要设置一下这个范形然后这个就没有错了这是我们修改了一下什么对修改了一个状态这个修改完之后你还没完你要看一下咱这个方法右层这个方法本身是不是有一个返回值咱到现在是不是还没有返回一些什么数据是不是没有我们如果一切都处理正常
[11:15] 一切都处理成功的话我们最终呢在这要返回一个return叫success吧succes反而一个这个不要那失败就跑一场咱也不用管什么反而反正他跑一场成功的话我们需要返回一个success那么整个代码呢咱就编辑完毕了整体咱过一下第一步呢就是根据传过来的这个标的ID把标的的所有信息全部查出来然后顺手把它转化成DTO对象因为将来在传输的时候都是传输的DTO对象
[11:45] 那由于我们这是交易嘛他肯定涉及到流水号所以说我们在这呢又根据一些工具类啊生成流水号也存到DTO对象里边将来会随着DTO对象一块传过去那这些处理完之后呢第三步呢我们就是通过非印代理发起这个请求对吧把DTO对象就传过去了那边就要做一系列的一些处理比如说要要访问那个谁啊要访问银行的那边系统对不对呃他那边处理完之后会返回我们这个结果然后我们这边就根据结果
[12:13] 如果失败就抛异常如果成功我就修改那个状态办案未同步改成什么呀已同步就是那个一码我们传过来审核通过这边是前端传回来是一码最终呢我们返回一个我们这个方案本身要返回一个success这个是哪边代码对这是我们这个什么呀审核标的这一块交易中心这边的这个代码我们写完一会呢我们要编写存款代理服务就是2.3到2.8这块代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个项目审批服务中，如何通过 Feign 调用远程服务、使用代码前缀工具类生成唯一标识、并根据返回结果更新项目状态的完整流程。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的代码，其中调用 queryWrapper 的 getOne 方法获取项目实体，并调用 convertProjectEntityToDTOList 方法转换为 DTO 列表。代码中注释说明“根据审批好的信息开转换为DTO对象”。

画面2：
要点：展示 ProjectServiceImpl 类中 convertProjectEntityToDTOList 方法的实现，将 Project 实体列表转换为 ProjectDTO 列表。代码中注释说明“如果项目为null则返回null”。

画面3：
要点：展示 ProjectServiceImpl 类中 convertProjectDTOToEntity 方法的实现，将 ProjectDTO 转换为 Project 实体。代码中注释说明“如果DTO为null则返回null”。

画面4：
要点：展示 ProjectServiceImpl 类中调用 CodeUtil.getNo 方法，用于生成唯一标识。代码中注释说明“通过feign远程调用代理服务，把标的的信息传输过去”和“根据结果修改状态”。

画面5：
要点：展示 ProjectServiceImpl 类中设置项目DTO的请求码，使用 CodeUtil.getNo 方法。代码中注释说明“通过feign远程调用代理服务，把标的的信息传输过去”和“根据结果修改状态”。

画面6：
要点：展示 ProjectServiceImpl 类中 createProject 方法的实现，调用 consumerApiAgent 的 getCurrentConsumer 方法获取当前消费者信息。代码中注释说明“根据结果修改状态”。

画面7：
要点：展示 DepositoryAgentApiAgent 接口，定义了 createProject 方法，使用 @FeignClient 和 @PostMapping 注解。代码中注释说明“通过feign远程调用代理服务，把标的的信息传输过去”。

画面8：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的实现，调用 DepositoryReturnCode 的 RETURN_CODE_0000 常量，判断返回结果是否为成功。代码中注释说明“根据结果修改状态”。

画面9：
要点：展示 ProjectServiceImpl 类中抛出 BusinessException 异常，用于处理业务异常。代码中注释说明“如果失败就抛异常”。

画面10：
要点：展示 ProjectServiceImpl 类中根据返回结果更新项目状态的代码，使用 Wrappers.lambdaUpdate 方法。代码中注释说明“如果失败就抛异常”。

画面11：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的实现，调用 Wrappers.lambdaUpdate 方法更新项目状态。代码中注释说明“如果失败就抛异常”。

画面12：
要点：展示 ProjectServiceImpl 类中 createProject 方法的实现，使用 QueryWrapper 进行条件查询。代码中注释说明“根据类型”、“禁止利率”、“借款期限”、“还款期限”等条件。

画面13：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的实现，调用 Wrappers.lambdaUpdate 方法更新项目状态。代码中注释说明“如果失败就抛异常”。

画面14：
要点：展示 P2P平台的架构图，包含“创贷宝”、“交易中心”、“存管代理服务”、“标的的检索服务”和“银行存管系统”五个模块。图中用箭头表示各模块之间的交互流程，如“1.1.借款人发标”、“2.1.管理外审标通过”、“2.3.通过校验生成签名及摘要”等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
@Override
public String projectsApprovalStatus(Long id, String approveStatus) {
    //根据审批好的信息开转换为DTO对象
    Project project = getById(id);
    ProjectDTO projectDTO = convertProjectEntityToDTO(project);
    projectDTO.setRequestNo(CodeUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
    //通过feign远程调用代理服务，把标的的信息传输过去
    RestResponse<String> restResponse = depositoryAgentApiAgent.createProject(projectDTO);
    //根据结果修改状态
    if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
        Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
        //如果失败就抛异常
        throw new BusinessException(TransactionErrorCode.E_150119);
    }
}
```

画面2：
```java
private List<ProjectDTO> convertProjectEntityListToDTOList(java.util.List<Project> projectList) {
    if (projectList == null) {
        return null;
    }
    List<ProjectDTO> projectDTOList = new ArrayList<>();
    for (Project project : projectList) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        projectDTOList.add(projectDTO);
    }
    return projectDTOList;
}
```

画面3：
```java
private ProjectDTO convertProjectEntityToDTO(Project project) {
    if (project == null) {
        return null;
    }
    ProjectDTO projectDTO = new ProjectDTO();
    BeanUtils.copyProperties(project, projectDTO);
    return projectDTO;
}
```

画面4：
```java
//通过feign远程调用代理服务，把标的的信息传输过去
//根据结果修改状态
//如果失败就抛异常
```

画面5：
```java
projectDTO.setRequestNo(CodeUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
//通过feign远程调用代理服务，把标的的信息传输过去
//根据结果修改状态
//如果失败就抛异常
```

画面6：
```java
public ProjectDTO createProject(ProjectDTO projectDTO) {
    RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getCurrentConsumer(SecurityUtil.get(User.class));
    //根据结果修改状态
    if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
        Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
        //如果失败就抛异常
        throw new BusinessException(TransactionErrorCode.E_150119);
    }
}
```

画面7：
```java
@FeignClient(value = "depository-agent-Service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/l/create-project")
    public RestResponse<String> createProject(ProjectDTO projectDTO);
}
```

画面8：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

画面9：
```java
throw new BusinessException(Transa...
```

画面10：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

画面11：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

画面12：
```java
QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
//根据类型
if (StringUtils.isNotBlank(projectDTO.getProType())) {
    queryWrapper.lambda().eq(Project::getProType, projectDTO.getProType());
}
//禁止利率（投资人）
if (null != projectDTO.getAnnualRate()) {
    queryWrapper.lambda().eq(Project::getAnnualRate, projectDTO.getAnnualRate());
}
//借款期限（投资人）
if (null != projectDTO.getPeriod()) {
    queryWrapper.lambda().eq(Project::getPeriod, projectDTO.getPeriod());
}
//还款期限（投资人）
if (null != projectDTO.getRepaymentPeriod()) {
    queryWrapper.lambda().eq(Project::getRepaymentPeriod, projectDTO.getRepaymentPeriod());
}
//标的类型
if (null != projectDTO.getProType()) {
    queryWrapper.lambda().eq(Project::getProType, projectDTO.getProType());
}
```

画面13：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14：
PPT标题：P2P平台
架构图结构：
- “创贷宝”指向“交易中心”（1.1.借款人发标）
- “交易中心”指向“存管代理服务”（1.2.保存标的的信息，状态为：募集中，数据状态为：未发布）
- “存管代理服务”指向“标的的检索服务”（2.3

