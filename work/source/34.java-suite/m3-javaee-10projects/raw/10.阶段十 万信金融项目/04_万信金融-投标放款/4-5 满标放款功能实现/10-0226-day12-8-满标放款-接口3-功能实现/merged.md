# day12-8-满标放款-接口3-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-8-满标放款-接口3-功能实现_【海量资源尽在 666java.com】.mp4
- 时长 8分5秒（音频 485s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我刚才呢我们把接口二这块功能呢给实现了那接下来咱看接口三啊这个接口三呢其实你看看图你会发现嗯他要实现的功能跟接口二呢是非常非常的什么呀相似的呃第一个相似点大家看是不是也是交易中心发请求给谁啊对给存款代理服务对吧这是第一个相似点第二个相似点大家看一看
[00:25] 交易中心这边做的事情啊或者说要完成的功能跟接口二是不是也几乎是非常非常相似的也是生成签名保存交易记录对吧只不过啊接口二这边主要是实现什么放款功能的而接口三主要是改一改这个什么呀对标题的状态啊给它改成什么还款中仅此而已然后既然还是更新交入交易记录状态为一同步然后再回对不对
[00:50] 所以说呢这个借口三呢这个代码写下来跟刚才我们的借口二是非常非常相似的那咱接下来也是快速的把借口三这块的功能我们实现一下那这一块的话我们看看啊这个数据库的操作呢主要是涉及到这个修改的修改什么标题状态对吧那么这一块呢这个呃数据网站这个代码咱老早都编写过了所以说这儿也是直接从业务层开始咱找一找这个谁呀找一找还是这个从来代理服务对不对
[01:20] 找到这个右层的接口我们在这需要再增加一个方法我们从讲义里边找一找这个方法就是这我们拿过来用修改标题状态我说要改成什么改成什么干什么你看这个什么图画还款中对不对然后咱看看这个方法发名字叫modify project status见名之意修改标题的状态对吧
[01:55] 然后呢这里边我们重点关注的就是这个参数咱点击去看一看modify project的stater DTO这里边都有啥流水号对不对标底号啊标底的最新的一个状态对吧然后标底的ID下着这个闷发只是一个测试类咱不用管它这是它这里边这个封装好的东西这些数据从哪来啊是不是从交易中心发过来看图是不是
[02:21] 那这个代码呢咱是在接口一里边都已经写好了啊咱找一找回顾一下接口一的这个代码这应该是第三个阶段对不对看这修改状态你看他是不是提前溜了一个modifyproject的staterdto然后把他这边要的数据是不是封上进去了然后在这看好了在这是通过非硬代理啊调用这个方法是不是开始发这个请求然后把这个dc对象是不是就发到哪边来啊
[02:47] 对就发到我们这个存款代理服务这边在这就可以进行什么呀接收了这是右层里边的接口或者接口里边的这个方法我们定好然后呢我们就去实现内当中去实现这个方法这边应该要报错了啊咱们把这个方法快速先生成一下在这对吧那这里边我们要编写的代码跟刚才我们说的接口二那块代码基本上是怎么说呢一模一样对不对我们也是要先溜一个什么呀
[03:18] 对depository交易记录对象depository什么request那这里面是不是还是封装几个数据大概是不是应该是4个数据然后第一个数据就是流水号是不是我们从参数里边来取就行了modify.getrequestnumber还有什么东西还要请求类型是不是请求类型我们还是从depository哪个request type
[03:51] 扣的是吧底儿我们这次应该是取哪个指南应该取这个我们这次进行的请求会要进行的业务是不是就修改标的状态是不是点给的扣的获取自主券值然后第三个参数呢就是什么呀对象的类型我们修改的不是标的吗对不对p o g p o g c t对吧project然后呢这个id就是从参数里边取呗
[04:23] 对费点地球对吧点get什么爱的套路都一模一样然后这是什么样交易记录这个对象我们就溜出来溜出来之后直接保存吗也不是我们又要想到干什么呀密等性的一个实现对不对那当然代码一样还是调用这个方法把这个交易记录呢扔进去内部呢分三种情况来分别进行处理处理完之后呢是不是会返回给我这么类型的一个什么对象我们接收一下日子发的地球
[04:56] 然后接下来就是干什么呀接下来就是做判断呗看这个请求要不要继续往下走了判断了你看跟前面那基本上就一模一样啊如果他不等于闹那就是结束了啊证明这个请求前面已经处理完了直接就是return response什么的那如果他是闹证明这个请求是不是还要往下走对吧往下干啥那往下不还是签名啊然后发送请求吗是不是那咱现在还跟上面一样还是要干什么呀
[05:26] 先根据这个number查询出来最新的交易记录然后准备签名然后进行发送这个单位我就不再编写了写来写去从外代理服这边基本上都是一样的我们可以在这把这个注释稍微加加这是什么呀密等性实现对吧当然这样呢就不是什么呀lon request 的吧对不对这应该怎么改这应该是咱这个参数嘛叫modify对吧
[05:59] 这儿呢也是要这个对象看看吧这是根据request number查询出来最新的这个什么样交易记录然后呢把这个参照转成json格式的然后进行base64编码对吧接下来呢就准备开始往银行那边干什么呀对发数据了发请求了啊还是调send http get
[06:21] 那这时候呢这个值肯定就要改了因为咱处理的业务是不一样的嘛咱本次是修改标的状态呢是不是然后咱找一找这个值应该是取这个值啊modify下线project然后其他代码呢咱就不用改了都是一样的这是哪个地方的代码呀对接口三这块代码就编写完了啊又从那就编写完了啊那编完之后呢咱接下来也是把Controller那一块的代码给他
[06:53] 完善一下就行了看除了这个Controller那个方法是哪个呀应该是对就是这个方法是不是那咱们这怎么写啊一样的吧掉一下什么呀右层的方法就完事了啊那就是depositoryrequiredservice.modify什么呀project什么呀对staters然后把这个谁啊参数给他扔进去
[07:21] 人与之后呢他返回的是不是哪种类型的数据啊来我给你考过来吧他这个还是比较长的我先接收一下七个名字就叫迪泡特日胖子地球吧然后呢啊可不能直接把它进行返回还是跟刚才一样我们要调什么呀get rest response来取下数据搞一个封装然后把它扔进去就行这样呢直接就可以返回这个结果搞定是不是
[07:57] 那截止到目前吧咱就把接口三啊整个这一块功能呢全部开发完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个银行存管系统中，项目状态修改的接口实现，包括控制器层、服务层和底层调用银行存管系统的代码逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示控制器层的两个接口方法，分别是“用户预交易”和“确认放款”，并标注了请求参数和返回值。
画面2：展示服务层的“confirmLoan”方法，用于处理放款请求，参数为LoanRequest，返回值为RepositoryResponseDTO。
画面3：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面4：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面5：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面6：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面7：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面8：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面9：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面10：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面11：展示服务层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面12：展示控制器层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面13：展示控制器层的“modifyProjectStatus”方法，用于修改项目状态，参数为ModifyProjectStatusDTO，返回值为RepositoryResponseDTO。
画面14：展示一个流程图，描述了项目状态修改的完整流程，包括多个步骤和交互。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@ApiOperation(value = "用户预交易", value = "用户预交易请求信息")
@ApiImplicitParam(name = "userAutoPreTransactionRequest", value = "平台向存管系统发起的信息", required = true, dataType = "UserAutoPreTransactionRequest", paramType = "body")
@PostMapping("/user-auto-pre-transaction")
public RestResponse<String> userAutoPreTransaction(@RequestBody UserAutoPreTransactionRequest userAutoPreTransactionRequest) {
    DepositoryResponseDTO DepositoryBaseResponse depositoryResponse = depositoryRecordService.userAutoPreTransaction(userAutoPreTransactionRequest);
    return getRestResponse(depositoryResponse);
}

@ApiOperation(value = "审核标的的预标放款")
@ApiImplicitParam(name = "loanRequest", value = "标的的预标放款信息", required = true, dataType = "LoanRequest", paramType = "body")
@PostMapping("/confirm-loan")
public RestResponse<String> confirmLoan(@RequestBody LoanRequest loanRequest) {
    DepositoryResponseDTO DepositoryBaseResponse depositoryResponse = depositoryRecordService.confirmLoan(loanRequest);
    return getRestResponse(depositoryResponse);
}
```

画面2：
```java
// 申请放款数据
@Param loanRequest
@return
DepositoryResponseDTO DepositoryBaseResponse confirmLoan(LoanRequest loanRequest)

// 修改标的的状态
@Param modifyProjectStatusDTO
@return
DepositoryResponseDTO DepositoryBaseResponse modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO)
```

画面3：
```java
private long id;

public static void main(String[] args) throws UnsupportedEncodingException {
    // 用银行存管服务来修改状态
    ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
    // 业务实体id
    modifyProjectStatusDTO.setId(130782714400204546L);
    // 业务状态
    modifyProjectStatusDTO.setProjectStatus("REPAYING");
    // 请求流水号
    modifyProjectStatusDTO.setRequestNo("PRO_FEBBE6902F1D4C839EB6A6B351D37230");
    String reqData = EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(modifyProjectStatusDTO));
    final String sign = RSAUtil.sign(JSON.toJSONString(modifyProjectStatusDTO), "M1BVAIBADABRgqk");
    String str = "serviceName" + URLEncoder.encode("MODIFY_PROJECT", "utf-8");
}
```

画面4：
```java
// 第一阶段：生成放款请求
LoadRequest loadRequest = TenderMapper.selectList(project, tenderList, commission);
// 第二阶段：修改状态
ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
modifyProjectStatusDTO.setId(project.getId());
modifyProjectStatusDTO.setProjectStatus("REPAYING");
modifyProjectStatusDTO.setRequestNo(loadRequest.getRequestNo());
// 向存管代理发送放款请求
RestResponse<String> modifyProjectStatus = depositoryAgentAgent.modifyProjectStatus(modifyProjectStatus);
if (modifyProjectStatus.getResult().equals(DepositoryReturnCode.RETURN_CODE_0000)) {
    // 修改状态成功
}
```

画面5：
```java
// 申请放款数据
@Param loanRequest
@return
DepositoryResponseDTO DepositoryBaseResponse confirmLoan(LoanRequest loanRequest)

// 修改标的的状态
@Param modifyProjectStatusDTO
@return
DepositoryResponseDTO DepositoryBaseResponse modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO)
```

画面6：
```java
private DepositoryResponseDTO DepositoryBaseResponse sendHttpGet(
        String serviceName, String url, String reqData,
        DepositoryRecord depositoryRecord) {
    // 银行存管系统接收的 大参数：serviceName, platformNo, reqData, signature
    // signature会在@otb拦截器中处理
    String platformNo = configService.getPlatformCode();
    return sendHttpGet(serviceName, url, reqData, depositoryRecord);
}
```

画面7：
```java
String jsonStr = JSON.toJSONString(loanRequest);
String reqData = EncryptUtil.encodeUTF8StringBase64(jsonStr);
String url = configService.getDepositoryUrl() + "/Service";
return sendHttpGet(serviceName: "CONFIRM_LOAD", url: reqData, depositoryRecord);
```

画面8：
```java
private DepositoryResponseDTO DepositoryBaseResponse sendHttpGet(
        String serviceName, String url, String reqData,
        DepositoryRecord depositoryRecord) {
    // 银行存管系统接收的 大参数：serviceName, platformNo, reqData, signature
    // signature会在@otb拦截器中处理
    String platformNo = configService.getPlatformCode();
    return sendHttpGet(serviceName, url, reqData, depositoryRecord);
}
```

画面9：
```java
return responseDTO;
```

画面10：
```java
return responseDTO;
```

画面11：
```java
return responseDTO;
```

画面12：
```java
@ApiOperation(value = "修改标的的状态")
@ApiImplicitParam(name = "modifyProjectStatusDTO", value = "修改标的的状态DTO", required = true, dataType = "ModifyProjectStatusDTO", paramType = "body")
@PostMapping("/modify-project-status")
public RestResponse<String> modifyProjectStatus(@RequestBody ModifyProjectStatusDTO modifyProjectStatusDTO) {
    return null;
}
```

画面13：
```java
// 需要性实现
DepositoryResponseDTO DepositoryBaseResponse responseDTO = handleDepotent(depositoryRecord);
if (responseDTO != null) {
    return responseDTO;
}
// 准备签名
String jsonStr = JSON.toJSONString(modifyProjectStatusDTO);
String reqData = EncryptUtil.encodeUTF8StringBase64(jsonStr);
// 发送请求到银行存管系统
String url = configService.getDepositoryUrl() + "/Service";
return sendHttpGet(serviceName: "MODIFY_PROJECT", url: reqData, depositoryRecord);
```

画面14：
无代码或配置内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
流程图标题：流程图
流程图内容：
1. 管理员发起修改项目状态请求
2. 业务系统接收请求，生成放款请求
3. 业务系统调用银行存管系统
4. 银行存管系统处理请求，返回结果
5. 业务系统根据结果更新项目状态
6. 业务系统返回结果给管理员
7. 管理员收到结果，完成操作
8. 业务系统记录操作日志
9. 业务系统更新项目状态
10. 业务系统返回结果给管理员
11. 管理员收到结果，完成操作

