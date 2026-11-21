# day12-4-满标放款-接口1-功能实现4

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-4-满标放款-接口1-功能实现4_【海量资源尽在 666java.com】.mp4
- 时长 10分33秒（音频 633s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把第二阶段也就是接口二放款这个功能呢搞定了这里边的话主要就是交易中心网什么呀存款代理服务这边发请求啊把这个放个明细的传回去然后呢存款代理服务这边是要做后续的一堆什么呀处理那接下来呢按照顺序开始编写第三阶段在嘛就是接口三的这个功能啊就是三这个功能是不是主要是修改标底的状态就是修改成什么呀还款
[00:31] 中对不对那这个地方大家看他是不是也是交易中心要往哪发这个请求啊往存款代理服务这边发请求发去之后呢这边也是要干什么呀生成签名啊保证交易记录啊啊还要去发请求到银行那边哎修改这个状态都是修改成什么呀还款中然后呢最后呢这个返回什么修改成功那么交易中心呢根据这个结果也要修改什么呀标的的状态也要改成什么呀
[01:00] 还款中啊这是咱接下来要实现的接口三这功能那这个功能整个这个代码是不是应该是放到这位置是应该放到这对不对你阶段二成功了我才走什么呀阶段三嘛对不对说他应该放到这个什么呀衣服里面那我们说到这个刚才看图啊这个接口三是不是也是直接就是干什么呀发请求对不对交易中心网存款代理服务发请求那也是通过飞运发了那怎么发呢咱
[01:30] 是不是前面在这个飞行接口里边是不是新增了这么一个方法了我们一会呢一调用这个方法其实就是往这发请求了啊这是那个接口三那个那个请求那我们接下来就调用这个方法那就是depository urgent API urgent然后调用哪个方法调用这个方法modify什么呀project status然后大家看一看他要一个参数这个参数什么类型呢
[01:59] 对这个参数叫modifyprojectstatusdto那既然他要这么一个对象大家想一想我是不是应该在前面先把这个对象给他干什么呀对new出来newmodify那其实说白了我们接下来要做的事就是哎把这个对象new出来之后看看他里边都要啥他要啥呢我们就把这个值搞到手
[02:29] 我们就把这个值给搞到手然后封装到这个对象里边把这个对象往这一扔不就行了吗那他里边要的这个数据证明就是是谁想要的那就是从外代理服这边想要的那他可能在实现这个什么141516这功能时候需要这些数据对不对那他都要哪些东西呢咱点进去看一看就行什么呀请求留意号标底号标底的状态这个实体ID对吧就就几个就四个这个也比较简单啊咱挨个给他复职就行了呗
[03:00] 那我这呢再加点这个注释啊这个呢就是怎么着创建什么呀我们叫叫什么呀叫请求参数的对象吧这不就是发请求吗啊把他需要的数据呢封装这个对象里面啊就是请求封装请求参数对象啊然后呢我们就调用他的什么呀setter方法开始往里边存数据首先存这个标底的id吧就set id啊就是project哎不是他project
[03:34] 还要啥啊还要啥我们看呗然后就是这个就是状态吧这个状态的话我们是不是要修改成那个什么呀叫叫缓缓中对吧缓缓中这个状态不能随便乱写我们找一找应该有一个叫project code.project code.一个枚举啊我们应该是要哪个呢要这个缓缓中然后调他的get code的话得到我们想要的值
[04:07] 还需要封上啥还需要封装这个什么呀request能报是不是那么这个request能报的话我们不打算重新生成一个值为啥不打算重新升值呢你看虽然这儿也是一次请求但是这个请求包括这个请求是不是都属于一这个地方接口一这个一个大的请求里面对不对那我们再接口二这个地方是不是已经生成过一个一个什么呀请求的号啊那这样呢我们就直接用
[04:37] 前面这个生成的这个请求留意号就行了不再重新生成了那上来那个情流水号我们是不是封装到这个什么浪人是快色了一边你看看在哪来浪人 request他是不是也是在这对不对这儿溜了一个对象然后呢在这对不对封上进去了所以说呢我的这儿呢就可以直接通过浪人 request 的点给他什么呀
[05:07] request number因为这是一个业务嘛一个大的一个什么买家放款的一个业务所以说我就不再存益生成了啊呃这为啥报错呀报错是因为我们这应该调set方法对不对还缺个啥呀还有吗我们这是几个来一个两个三个还有吗还有谁呀还有这个什么标底号就是project number对不对那我们在这再来一个
[05:42] 第二setprojectnumber然后呢这还是从什么呀project对象里边来取就行这不该封装的都封装到位了吧然后呢就可以把这个对象哎往这一放那将来呢我们在执行这个方法的时候是不是就是走到哪一块走的就是这个什么呀13就这啊然后呢就把这个什么呀就把这里边的数据然后就干什么呀
[06:13] 发给谁对发给这个村里服务然后他拿这个数据该干嘛干嘛是不是那他这边处理完之后接下来我们接着中心还要干啥交易中心这边是不是还要修改什么呀对修改标的的状态也改成什么呀还款重那你看这样是不是就是发起这个非典型请求的他处理完之后我们这边是不是还要接收这个结果这个结果还是rest response饭行还是什么呀谁大家都比较熟了
[06:44] 那咱起个名字叫叫啥嘞叫我们用这个名字吧好吧我们跟前面这个要要要有所区别就要这个名字然后我们首先是要判断这个有没有处理成功吗是不是跟借口二那个套路是一样的一否然后这里边怎么写啊就是modifyproject status第二什么呀get谁呀给他reads out对不对
[07:21] 然后他和谁比啊还是那个五个零啊对不对那就是呃那就是怎么写叫deposit return code对吧点哎这有拿到手了五个零然后点给他谁啊对给他扣的那衣服就表示什么呀对比较成功了那else就表示什么呀失败那咱还是先编写失败的这种情况的这个代码失败了
[07:50] 那能怎么着呢咱就这一个套路就是抛异常啊然后这个提示信息的话我们挑一个吧挑一个叫transcationaircode我们还是用这个腰散啊凡是从矮带里那边出问题的都用这个那衣服就要成功成功的时候我们说要做什么事成功要做什么事我们是不是还得看什么看图对不对成功了要干啥呀成功的时候
[08:24] 是不是修改标标底的这个状态改成什么呀还款中那标底的状态不就是你投到那个标这里边有个状态吗这里边有个状态就是哪个状态啊应该是这个状态project status啊我们看看之前给的值project status这不是满标吗对吧我们现在需要把这个满标给它换成什么呀换成还款中
[08:52] 那这个不就是一个普通的一个修改吗很简单我们就是第二project对象的set方法set这个谁呀prosetproject status我们要给他一个还款中的一个值这个值怎么给呢就是project code吧点我们看看就是这个repay对吧还款中点get code要的就是这个值
[09:20] 然后只能修改完之后呢我们是不是应该调用这个谁啊update by d吧这个方法来完成数据库的修改是不是这就搞定了啊我这加点注释吧这是干什么呀像什么呀对存款代理服务发起请求然后呢这呢就是什么呀如果处理成功就
[10:03] 修改标的状态为什么呀对还款猪那好大家看一下截止到目前咱应该就把第几阶段的代码编写完了对第三阶段就是接口三这块代码编写完了主要就是往什么往存款代理服务那边发个请求然后修改一下这个什么呀对状态主要是改成什么还款猪

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在贷款审批服务中，通过修改项目状态（如从“已放款”改为“还款中”）并调用外部代理服务来完成状态变更，并展示相关代码实现和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个流程图，描述了从“前端APP”到“业务系统”的贷款审批流程，其中包含“项目管理”、“还款服务”、“清算系统”等模块，以及状态变更（如“已放款”→“还款中”）和异常处理（如“失败”→“已拒绝”）。
画面2：展示IDE中`ProjectServiceImpl.java`文件，代码中定义了`confirmLoan`、`userAutoProTransaction`、`modifyProjectStatus`等方法，以及`depositoryAgentAgent`类的`else`分支抛出`BusinessException`异常。
画面3：展示IDE中`ModifyProjectStatusDTO.java`文件，定义了`requestNo`、`projectNo`、`projectStatus`、`id`等字段，并展示`main`方法中创建`ModifyProjectStatusDTO`对象。
画面4：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并设置`projectStatus`为`REPAYING`。
画面5：展示IDE中`ProjectServiceImpl.java`文件，代码中设置`modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode())`。
画面6：展示IDE中`ProjectServiceImpl.java`文件，代码中设置`modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo())`。
画面7：展示IDE中`ProjectServiceImpl.java`文件，代码中设置`modifyProjectStatusDTO.setProjectNo(project.getProjectNo())`。
画面8：展示数据库管理工具，显示`pjq_transaction_1`数据库中的`loan`表数据，包含`PROJECT_ID`、`PROJECT_NO`、`AMOUNT`、`STATUS`、`CREATE_DATE`等字段。
画面9：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法。
画面10：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并判断返回值是否等于`RETURN_CODE_00000`。
画面11：展示IDE中`ProjectServiceImpl.java`文件，代码中抛出`BusinessException(TransactionErrorCode.E_150113)`异常。
画面12：展示数据库管理工具，显示`pjq_transaction_1`数据库中的`project_1`表数据，包含`PROJECT_ID`、`PROJECT_NO`、`AMOUNT`、`STATUS`、`CREATE_DATE`等字段。
画面13：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并设置`project.setStatus(ProjectCode.REPAYING.getCode())`。
画面14：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并设置`project.setStatus(ProjectCode.REPAYING.getCode())`，并添加注释“如果处理成功，就修改的状态方法函数中”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
confirmLoan(LoanRequest loanRequest)
userAutoProTransaction(UserAutoProTransactionRequest userAutoProTransactionRequest)
modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO)
```
```java
depositoryAgentAgent
```
```java
else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```
画面3：
```java
private String requestNo;
private String projectNo;
private String projectStatus;
private Long id;
```
```java
public static void main(String[] args) throws UnsupportedEncodingException {
    // 使用省略号续写 一修改状态为还款中
    // 构造请求参数
    ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
    modifyProjectStatusDTO.setId(project.getId());
```
画面4：
```java
Project project = projectPathById(14);
// 校验信息
queryWrapper.lambda().eq(Project::getProjectId, 14);
List<Tender> tenderList = tenderMapper.selectList(queryWrapper);
// 生成放款请求
LoanRequest loanRequest = generateLoanRequest(project, tenderList);
// 第二阶段，放款
RestResponse<String> restResponse = depositoryAgentApiAgent.confirmLoan(loanRequest);
if (restResponse.getResult().equals(RepositoryReturnCode.RETURN_CODE_00000)) {
    // 修改状态
    ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
    modifyProjectStatusDTO.setId(project.getId());
    modifyProjectStatusDTO.setProjectCode(ProjectCode.REPAYING.getCode());
    modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
    depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatusDTO);
} else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```
画面5：
```java
modifyProjectStatusDTO.setProjectCode(ProjectCode.REPAYING.getCode());
```
画面6：
```java
modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
```
画面7：
```java
modifyProjectStatusDTO.setProjectNo(project.getProjectNo());
```
画面9：
```java
depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatus);
```
画面10：
```java
RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatus);
if (modifyProjectStatus.getResult().equals(DepositReturnCode.RETURN_CODE_00000.getCode())) {
```
画面11：
```java
throw new BusinessException(TransactionErrorCode.E_150113);
```
画面13：
```java
project.setStatus(ProjectCode.REPAYING.getCode());
```
画面14：
```java
project.setStatus(ProjectCode.REPAYING.getCode());
```
画面8：
```sql
SELECT PROJECT_ID, PROJECT_NO, AMOUNT, STATUS, CREATE_DATE FROM loan;
```
画面12：
```sql
SELECT PROJECT_ID, PROJECT_NO, AMOUNT, STATUS, CREATE_DATE FROM project_1;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：流程图，从“前端APP”指向“业务系统”，“业务系统”指向“项目管理”、“还款服务”、“清算系统”，“项目管理”指向“还款服务”，“还款服务”指向“清算系统”，“清算系统”指向“业务系统”，“业务系统”指向“前端APP”，并包含状态变更和异常处理。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

