# day14-14-用户还款-第四阶段-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-14-用户还款-第四阶段-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 6分16秒（音频 376s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前的话我们把用户还款业务当中第三阶段的功能全部开放完毕而且呢我们也把业务出发入口里边的代码呢也补充上了但接下来呢这一阶段我们暂时先不进行功能测试因为我们前面分析过说这个第三阶段跟第四阶段这一块的业务是不是紧密相连呢对吧而且他们之间是不是还是存在一个分布式事物的问题
[00:29] 所以我们接下来呢就是继续开发第四阶段功能等第四阶段开发完之后我们一起做一个功能测试咱们接下来看看这个第四阶段第四阶段是2.3到什么呀2.9但是在走这个2.3之前呢我们是不是应该要先接收消息吗是不是咱在第三阶段是不是实现了这个发送消息那么在第四阶段我们首先要接收消息接收完消息之后呢我们再走2.3就是通过飞
[01:00] 开启干什么呀就开始发请求到从来代理服务然后一直往后走那咱接下来这样我们把这个第四阶段的给它拆成两块啊一块呢就是接收消息这一块啊一块呢就是2.3到2.9这个常规的一个什么呀业务处理分成这两块之后呢咱先搞定2.3到2.9这个常规的业务处理这块搞完之后呢咱接收一下消息是不是就可以触发这个常规这个业务的一个什么呀执行了啊
[01:30] 这个整体的思路大家先搞清楚那么2.3到2.9这个常规业务的处理对于我们来说应该不是多大的一个难事了咱们前面多次提到过啊呃我们的微服务发请求到存款代理存款代理呢呃他做的这些事情是不是就是那个什么老套路的对不对咱们非常非常熟悉了啊所以这块代码呢咱们接下来就是快速的把它给实现一下然后呢我们再去搞定这个什么接收消息这一块
[01:58] 那2.3到2.9的话大家看看我们首先是不是也是要定义接口嘛对不对因为你看还款服务是不是通过非发起请求到哪到存款代理服务这边存款代理服务这边肯定对应的是一个Controller是不是那咱接下来把Controller这块的接口先给它定义出来那咱看看讲义你看他这说了嘛请求存款银行存款系统进行确认还款反合结果给还款服务对吧这是这个接口的作用嘛
[02:29] 就这个接口期嘛接口期他是不是最终要跟银行从来没有打交道要要处理这个还款嘛然后呢要返回这个这个结果呃这是Controller这一块的一个一个什么一个接口所以说我们需要去apm接口当中啊新增这么一个conform什么呀conform repayment方法咱找到这个apm这是哪个
[03:01] 买卖deposit是吧存款代理服这边的API这个接口啊然后呢我们再下边再加一块东西就是加个注释吧这叫什么呀还款确认吧确认对吧然后呢咱接下来把这个方法给它定义一下这个反应值吗跟上面都一样啊因为control上这边咱统一了嘛返回头都是这么来进一封装的就是rest response
[03:32] 这个发明咱跟讲义保持一致吧就是这个谁呀叫conformalrepayment对吧然后呢这个方法呢有几个参数一个参数这个参数是不是咱第三阶段最终是不是封装了那个那个那个什么呀叫就第三阶段我们最终封装的是那个谁呀叫repayment request呢你还有一项吗这个代码咱是不是刚写过对不对然后呢我们把这个参数给他加上repay
[04:08] 对将来的话还款服务呢就是通过飞啊往这儿发请求发请求同时呢是不是把这个数据给他对传过来就行了咱把账呢也给他补充一下这个参数的话就是表示什么呀对还款信息还款信息好这是接口里边呢咱们这个发进好定好之后咱们之前一样顺手呢把扛出来里边的这个方法给他生成
[04:44] 先来一个空时线啊那这儿是不是都已经报错了咱给他生成到最下面对不对生成哎我们看看在这对不对那咱接下来参考讲一把这些哎这个方法上面最基本的一些注解呢给他补充完善一下就行了我们看一下是不是这一块在这然后呢这个request body不能忘我咱大家看一下吧这个接口实验功能就是最后一步来确认还款了对不对然后呢这个
[05:35] 请求地址大家看一下是这个地址L开头的咱应该很熟悉了什么意思啊那就这个地方只能被微服务访问不能报了给前端对不对那你看咱这个不就是谁去访问的呀不就是这个还款服务吗是不是是还款服务啊他通过飞嘛往这发请求的啊这是具体的请求地址然后传过来的数据呢这个阶层格式的对不对这呢我们用这个什么呀
[06:04] 加上这个request body这个注意这个千万不要忘了啊这是目前吧咱先把这个什么呀对这个接口期吧这一块的这个代码先搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解还款业务的接口定义与实现，包括在控制器中新增确认还款方法、定义接口参数、实现业务逻辑并统一返回响应。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款业务流程图，包含“还款服务”、“存管代理服务”、“存管系统”三个角色，流程步骤包括：1.1查看到期的还款计划、1.2生成还款明细、1.3还款处理、1.4通过规则生成签名及摘要、1.5保存交易记录、1.6处理还款-还款（直连接口）、1.7冻结还款金额、1.8资金冻结成功、1.9更新交易记录、1.10还款处理成功、1.11还款成功。
画面2：展示PPT内容，标题为“6.1 定义接口（接口⑦）”，内容包括：1. 接口描述（1）请求求系统进行确认还款、（2）返回结果给还款服务；2. 接口定义（在DepositoryAgentApi接口中新增confirmRepayment方法）。
画面3：展示IDE中RepaymentServiceImpl.java文件内容，包含生成还款明细、处理还款逻辑、打印日志、调用repaymentProducer.confirmRepayment方法。
画面4：展示IDE中项目结构，选中wanningzp-api模块。
画面5：展示多个窗口，包括PPT、IDE、数据库管理工具等，说明在DepositoryAgentController类中实现confirmRepayment方法。
画面6：展示PPT内容，标题为“6.1 定义接口（接口⑦）”，内容包括：1. 接口描述（1）请求求系统进行确认还款、（2）返回结果给还款服务；2. 接口定义（在DepositoryAgentApi接口中新增confirmRepayment方法）。
画面7：展示IDE中DepositoryAgentApi.java文件内容，包含confirmLoan方法和confirmRepayment方法。
画面8：展示IDE中DepositoryAgentController.java文件内容，包含@ApiOperation注解和createConsumer方法。
画面9：展示IDE中DepositoryAgentController.java文件内容，包含@ApiOperation注解和confirmRepayment方法。
画面10：展示PPT内容，标题为“6.1 定义接口（接口⑦）”，内容包括：1. 接口描述（1）请求求系统进行确认还款、（2）返回结果给还款服务；2. 接口定义（在DepositoryAgentApi接口中新增confirmRepayment方法）。
画面11：展示IDE中DepositoryAgentController.java文件内容，包含confirmRepayment方法和getRestResponse方法。
画面12：展示IDE中DepositoryAgentController.java文件内容，包含confirmRepayment方法和getRestResponse方法。
画面13：展示还款业务流程图，包含“还款服务”、“存管代理服务”、“存管系统”三个角色，流程步骤包括：1.1查看到期的还款计划、1.2生成还款明细、1.3还款处理、1.4通过规则生成签名及摘要、1.5保存交易记录、1.6处理还款-还款（直连接口）、1.7冻结还款金额、1.8资金冻结成功、1.9更新交易记录、1.10还款处理成功、1.11还款成功。
画面14：展示还款业务流程图，包含“还款服务”、“存管代理服务”、“存管系统”三个角色，流程步骤包括：1.1查看到期的还款计划、1.2生成还款明细、1.3还款处理、1.4通过规则生成签名及摘要、1.5保存交易记录、1.6处理还款-还款（直连接口）、1.7冻结还款金额、1.8资金冻结成功、1.9更新交易记录、1.10还款处理成功、1.11还款成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
在DepositoryAgentApi接口中新增confirmRepayment方法：
```java
/**
 * 还款确认
 * @param repaymentRequest 还款信息
 * @return
 */
RestResponse<String> confirmRepayment(RepamentRequest repaymentRequest);
```
在DepositoryAgentController类中实现该方法：
```java
@Override
@RequestMapping(value = "/confirm-repayment")
public RestResponse<String> confirmRepayment(RepamentRequest repaymentRequest) {
    return null;
}
```
画面3：
```java
//生成还款明细
repaymentPlanList.forEach(repaymentPlan -> {
    RepaymentDetail repaymentDetail = repaymentService.getRepaymentDetail(repaymentPlan, repaymentDetail.getRepaymentRequest());
    //处理还款
    Boolean proRepaymentResult = proRepayment(repaymentPlan, repaymentDetail.getRepaymentRequest());
    if (proRepaymentResult) {
        System.out.println("还款处理成功");
        RepaymentRequest repaymentRequest = repaymentService.generateRepaymentRequest(repaymentPlan, repaymentRequest);
        repaymentProducer.confirmRepayment(repaymentPlan, repaymentRequest);
    }
});
```
画面7：
```java
/**
 * 还款确认
 * @param loanRequest
 * @return
 */
RestResponse<String> confirm(LoanRequest loanRequest);
```
画面8：
```java
@ApiOperation(value = "存管代理服务", tags = {"depository-agent"})
@RestController
public class DepositoryAgentController implements DepositoryAgentApi {

    @Autowired
    private DepositoryRecordService depositoryRecordService;

    @ApiOperation(value = "生成开户请求数据", value = "开户信息", required = true, dataType = "ConsumerRequest", paramType = "body")
    @PostMapping("/consumers")
    public RestResponse<String> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
        return RestResponse.success(depositoryRecordService.createConsumer(consumerRequest));
    }
}
```
画面9：
```java
@ApiOperation(value = "修改标的的状态", value = "修改标的的状态DTO", required = true, dataType = "ModifyProjectStatusDTO", paramType = "body")
@PostMapping("/modify-project-status")
public RestResponse<String> modifyProjectStatus(@RequestBody ModifyProjectStatusDTO modifyProjectStatusDTO) {
    DepositoryResponseDTO depositoryResponseDTO = depositoryRecordService.modifyProjectStatus(modifyProjectStatusDTO);
    return getRestResponse(depositoryResponseDTO);
}
```
画面11：
```java
@Override
public RestResponse<String> confirmRepayment(RepamentRequest repaymentRequest) {
    //统一处理响应信息
    @SuppressWarnings("unused")
    RestResponse<String> restResponse = new RestResponse<>();
    restResponse.setMsg(depositoryResponse.getRespData().getRespMsg());
    return restResponse;
}
```
画面12：
```java
@Override
@ApiOperation(value = "确认还款")
@ApiOperation(value = "还款信息", required = true, dataType = "RepamentRequest", paramType = "body")
@PostMapping("/confirm-repayment")
public RestResponse<String> confirmRepayment(RepamentRequest repaymentRequest) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：流程图结构：还款服务 → 存管代理服务 → 存管系统，步骤包括：1.1查看到期的还款计划、1.2生成还款明细、1.3还款处理、1.4通过规则生成签名及摘要、1.5保存交易记录、1.6处理还款-还款（直连接口）、1.7冻结还款金额、1.8资金冻结成功、1.9更新交易记录、1.10还款处理成功、1.11还款成功。
画面2：PPT标题为“6.1 定义接口（接口⑦）”，内容包括：1. 接口描述（1）请求求系统进行确认还款、（2）返回结果给还款服务；2. 接口定义（在DepositoryAgentApi接口中新增confirmRepayment方法）。
画面5：PPT标题为“6.1 定义接口（接口⑦）”，内容包括：1. 接口描述（1）请求求系统进行确认还款、（2）返回结果给还款服务；2. 接口定义（在DepositoryAgentApi接口中新增confirmRepayment方法）。
画面13：流程图结构：还款服务 → 存管代理服务 → 存管系统，步骤包括：1.1查看到期的还款计划、1.2生成还款明细、1.3还款处理、1.4通过规则生成签名及摘要、1.5保存交易记录、1.6处理还款-还款（直连接口）、1.7冻结还款金额、1.8资金冻结成功、1.9更新交易记录、1.10还款处理成功、1.11还款成功。
画面14：流程图结构：还款服务 → 存管代理服务 → 存管系统，步骤包括：1.1查看到期的还款计划、1.2生成还款明细、1.3还款处理、1.4通过规则生成签名及摘要、1.5保存交易记录、1.6处理还款-还款（直连接口）、1.7冻结还款金额、1.8资金冻结成功、1.9更新交易记录、1.10还款

