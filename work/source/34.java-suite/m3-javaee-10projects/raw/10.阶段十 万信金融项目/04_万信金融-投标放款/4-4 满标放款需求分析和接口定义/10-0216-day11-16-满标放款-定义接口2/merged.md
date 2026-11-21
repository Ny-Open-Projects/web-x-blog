# day11-16-满标放款-定义接口2

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-4 满标放款需求分析和接口定义
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-4 满标放款需求分析和接口定义\day11-16-满标放款-定义接口2_【海量资源尽在 666java.com】.mp4
- 时长 4分59秒（音频 299s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接口一咱们定义好之后呢按照顺序咱接下来定义接口二接口二大家看图说话啊接口二呢就是说交易中心要通过非发起远程请求到哪到存款代理服务这边对不对看图啊然后呢存款代理服务这边要实现的功能就是这老套路对不对大家应该都很熟悉了生成签名啊保存交易记录数据状态是未同步然后发请求到银行那边对吧银行就要做
[00:27] 这个处理处理完之后呢从代理服务这边根据这个什么样结果来更新交易记录主要是更新这个什么样数据状态为什么呀一同步然后这个表示什么方法成功了是不是说这是接口二吧我们要实现的功能啊在图里边展示的非常清晰我就不在过头说了那接下来参考讲义把这个二定义一下那这次呢我们要定义的这个接口或者这个方法就应该放到哪个微服里边是针对哪个微服为来
[00:56] 是不是针对主要是针对谁啊存贯代理服务的对不对那所以说呢我们应该去API工程里边找一下这个depository找到这个接口啊然后我们需要在这里边再新增一个方法好我们看一下讲义conform论对吧我们把这一块呢给它粘过去拿过来放到这好大家大家看一眼吧
[01:35] 这里边的话有一个参数啊learn request这个呢咱根据以往的经验我们基本上能分析出来这个learn request其实就是封装谁啊交易中心通过封印发过来的这个数据啊这些数据呢会封装成什么呀learn request啊这个类呢咱一会粘过来那这个处理完之后最终返回的类型就是stream吧你看这放缓成功嘛一个字母串就可以表示这个结果那咱接下来呢把这个learn request这个类呢我们找一找
[02:04] 粘过来就行了我们找一下啊在这里边乐日快走我们看他应该站到什么地方API那我们就ctrl c然后呢应该是在这里边吧粘过来这边应该会自动倒包对不对好然后我们看看啊这边呢他其实里边啊我们看都写了什么东西有一个属性放款明细的对不对你看
[02:36] 咱们这个图里边上一步他这是不是形成了放款明细吗所以说这个放款明细的信息呢他应该是封装到learn detail request里边然后最终呢由于放款明细是这个数据是多个嘛所以他用例子进行的封装啊新台的佣金啊啊标底的编码啊请求留语号啊操作对象ID吧这些我们用到的时候再说大家熟悉一下然后这里边是不是还缺一个类叫learn detail request接下来我们也把它给拷过来我们找一下啊在这对吧
[03:05] 好我们看一看应该考到什么地方还是A片好我们Ctrl C还是这给它粘过来然后这边应该会自动倒包那我刚才说了这个Long Detail Request主要是封装那个放款明细的对不对咱大概的熟悉一下这里边主要是一个放款金额还有一个预处理业务流水号这些东西都是咱用到的时候再详细给大家介绍这是目前咱把第二个接口里边所涉及的这个方法给定好然后
[03:39] 接下来咱也是顺手呢把这个Controller给它生成一下Controller里边的方法那咱这个应该是谁啊存管代理服务我们找找Controller应该是这个对吧我们看它现在报错了我们把这个方法呢给它生成出来OK那接下来也是参考讲义把这个相关的一些注解吧给它补一下就行了还是stagger和spring mvc的注解
[04:14] 然后还有就是这个request的body我们看一下吧这个请求路径啊请求路径呢大家看一下L大头的L大头的咱之前提过是不是应该是微服之间去访问的对吧那你看咱这个图你看咱这个第二个接口是不是就是由谁去远程请求的呀有谁发起这个远程请求交易中心嘛对吧交易中心也是一个微服嘛是不是从这L开头那没有问题然后就是你要注意这个注解啊他这个交易中心发过来的数据
[04:49] 在这进行封装的时候这要加什么request body这个注写这是第几个接口咱就定义好了对第二个接口就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个贷款审批流程中，交易中心如何调用存管系统进行放款确认，并展示相关的 Java 代码实现和数据模型定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个流程图，描述了“交易中心”向“存管系统”发起“放款确认”请求的流程，包含多个步骤和条件判断。
画面2：在 IntelliJ IDEA 中展示 `TransactionController.java` 文件，定义了 `@ApiOperation("审核标的满标放款")` 注解的 `loansApprovalStatus` 方法，用于处理放款审批。
画面3：在 Word 文档中展示“3) 生成放款单据”和“4) 请求存管系统进行确认放款”的文字说明，并列出在 `DepositoryAgentApi` 接口中定义的 `confirmLoan` 方法。
画面4：在 IntelliJ IDEA 中展示 `DepositoryAgentApi.java` 文件，定义了 `confirmLoan` 方法的接口签名。
画面5：在 IntelliJ IDEA 中展示 `DepositoryAgentApi.java` 文件，高亮显示 `confirmLoan` 方法的参数 `LoanRequest`。
画面6：在 Windows 资源管理器中，右键点击 `LoanRequest.java` 文件，弹出菜单显示“用 Notepad++ 打开”等选项。
画面7：在 IntelliJ IDEA 中展示 `LoanRequest.java` 文件，定义了 `LoanRequest` 类，包含 `details`、`commission`、`projectNo`、`requestNo` 和 `id` 等字段。
画面8：在 IntelliJ IDEA 中展示 `LoanRequest.java` 文件，高亮显示 `private List<LoanDetailRequest> details;` 字段。
画面9：在 Windows 资源管理器中，显示 `LoanDetailRequest.java` 文件。
画面10：在 IntelliJ IDEA 中展示 `LoanDetailRequest.java` 文件，定义了 `LoanDetailRequest` 类，包含 `amount` 和 `requestNo` 字段。
画面11：在 IntelliJ IDEA 中展示 `TransactionApi.java` 文件，定义了 `loansApprovalStatus` 方法的参数和返回值。
画面12：在 IntelliJ IDEA 中展示 `DepositoryAgentController.java` 文件，定义了 `userAutoPreTransaction` 和 `confirmLoan` 方法。
画面13：在 IntelliJ IDEA 中展示 `DepositoryAgentController.java` 文件，高亮显示 `getRestResponse` 方法的定义。
画面14：与画面1相同，再次展示流程图，描述“交易中心”向“存管系统”发起“放款确认”请求的流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@ApiOperation("审核标的满标放款")
@ApiImplicitParams({
    @ApiImplicitParam(name = "id", value = "标的.id", required = true,
            dataType = "long", paramType = "path"),
    @ApiImplicitParam(name = "approveStatus", value = "标的的状态", required = true,
            dataType = "string", paramType = "path"),
    @ApiImplicitParam(name = "commission", value = "平台佣金", required = true,
            dataType = "string", paramType = "query"),
    @ApiImplicitParam(name = "requestNo", value = "请求流水号", required = true,
            dataType = "string", paramType = "query")
})
@RequestMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") String approveStatus, String commission, String requestNo) {
    return null;
}
```

画面3：
```java
/**
 * 审核标的满标放款
 * @param loanRequest
 * @return
 */
RestResponse<String> confirmLoan(LoanRequest loanRequest);

@Override
@ApiOperation(value = "审核标的满标放款", value = "后的满标放款信息", required = true, dataType = "LoanRequest", paramType = "body")
@PostMapping("/confirm-loan")
public RestResponse<String> confirmLoan(@RequestBody LoanRequest loanRequest){
    return null;
}
```

画面4：
```java
/**
 * 审核标的满标放款
 * @param loanRequest
 * @return
 */
RestResponse<String> confirmLoan(LoanRequest loanRequest);
```

画面7：
```java
public class LoanRequest {
    /**
     * 放款明细
     */
    private List<LoanDetailRequest> details;
    /**
     * 平台佣金
     */
    private BigDecimal commission;
    /**
     * 标的编码
     */
    private String projectNo;
    /**
     * 请求流水号
     */
    private String requestNo;
    /**
     * 操作对象id
     */
    private Long id;
}
```

画面10：
```java
public class LoanDetailRequest {
    /**
     * 放款金额
     */
    private BigDecimal amount;
    /**
     * 预处理流水流水号
     */
    private String requestNo;
}
```

画面11：
```java
/**
 * 审核标的满标放款
 * @param id 标的id
 * @param approveStatus 审核状态
 * @param commission 平台佣金
 * @return
 */
RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission);
```

画面12：
```java
@Override
@ApiOperation(value = "预授权处理", value = "平台向存管系统发送预授权信息", required = true, dataType = "UserAutoPreTransactionRequest", paramType = "body")
@PostMapping("/user-auto-pre-transaction")
public RestResponse<String> userAutoPreTransaction(@RequestBody UserAutoPreTransactionRequest userAutoPreTransactionRequest) {
    return null;
}

@Override
public RestResponse<String> confirmLoan(LoanRequest loanRequest) {
    return null;
}
```

画面13：
```java
private RestResponse<String> getRestResponse(DepositoryResponseDTO DepositoryBaseResponse) {
    final RestResponse<String> restResponse = new RestResponse<>();
    restResponse.setSuccess(true);
    restResponse.setMsg("成功");
    restResponse.setResult(DepositoryBaseResponse);
    return restResponse;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1和画面14：
- 流程图标题：“放款流程”
- 流程图结构：
  - “交易中心” → “存管系统”
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“放款成功”或“失败”）
  - “交易中心” → “存管系统”（通过“放款确认”）
  - “存管系统” → “交易中心”（返回“

