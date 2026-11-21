# 画面线理解：day14-16-用户还款-第四阶段-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-16-用户还款-第四阶段-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 00:46, 01:31, 03:25, 03:46, 04:20, 04:46, 05:18, 05:53, 06:48, 07:07, 07:30, 08:00, 08:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:25:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在还款服务中通过 Feign 客户端调用存管代理服务确认还款，并处理相应的业务逻辑和异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `DepositoryAgentController` 中的 `confirmRepayment` 方法，用于接收还款请求并调用 `depositoryRecordService`。
画面2：展示 `DepositoryAgentApiAgent` 接口，定义了 `/user-auto-pre-transaction` 和 `/confirm-repayment` 两个 Feign 接口。
画面3：再次展示 `DepositoryAgentApiAgent` 接口，强调 `/confirm-repayment` 接口用于确认还款。
画面4：PPT 页面，说明在 `RepaymentService` 接口中新增 `invokeConfirmRepayment` 方法，用于接收消息后调用。
画面5：展示 `DepositoryAgentApiAgent` 接口，再次强调 `/confirm-repayment` 接口。
画面6：PPT 页面，说明在 `DepositoryAgentApiAgent` 接口中新增 `confirmRepayment` 方法，用于向存管代理服务发请求。
画面7：展示 `RepaymentServiceImpl` 中的 `executeRepayment` 方法，包含计算还款金额、生成还款计划等逻辑。
画面8：展示 `RepaymentServiceImpl` 中的 `invokeConfirmRepayment` 方法，调用 `depositoryAgentApiAgent.confirmRepayment`。
画面9：再次展示 `DepositoryAgentController` 中的 `confirmRepayment` 方法。
画面10：展示 `RepaymentServiceImpl` 中的 `invokeConfirmRepayment` 方法，准备调用 `depositoryAgentApiAgent.confirmRepayment`。
画面11：展示 `RepaymentServiceImpl` 中的 `invokeConfirmRepayment` 方法，调用 `depositoryAgentApiAgent.confirmRepayment`。
画面12：展示 `RepaymentServiceImpl` 中的 `invokeConfirmRepayment` 方法，准备抛出异常。
画面13：展示 `RepaymentServiceImpl` 中的 `invokeConfirmRepayment` 方法，抛出 `BusinessException` 异常。
画面14：流程图，展示用户还款成功后的处理流程，包括发送确认还款信息、确认还款处理、生成交易明细、更新交易记录等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
@ApiOperation(value = "确认还款")
@ApiImplicitParam(name = "repaymentRequest", value = "还款信息",
required = true, dataType = "RepaymentRequest", paramType = "body")
@PostMapping("/confirm-repayment")
public RestResponse<String> confirmRepayment(@RequestBody RepaymentRequest repaymentRequest) {
    return getRestResponse(depositoryRecordService.confirmRepayment(repaymentRequest));
}
```

画面2：
```java
package cn.itcast.wanxing2p.repayment.agent;

import cn.itcast.wanxing2p.api.depository.model.UserAutoPreTransactionRequest;
import cn.itcast.wanxing2p.common.domain.RestResponse;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@FeignClient(value = "depository-agent-service")
public interface DepositoryAgentApiAgent {

    @PostMapping("/depository-agent/user-auto-pre-transaction")
    RestResponse<String> userAutoPreTransaction(@RequestBody UserAutoPreTransactionRequest userAutoPreTransactionRequest);

    @PostMapping("/depository-agent/confirm-repayment")
    RestResponse<String> confirmRepayment(@RequestBody RepaymentRequest repaymentRequest);
}
```

画面4：
```java
/**
 * 远程调用确认还款接口
 * @param repaymentPlan
 * @param repaymentRequest
 */
void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);
```

画面6：
```java
/**
 * 远程调用确认还款接口
 * @param repaymentPlan
 * @param repaymentRequest
 */
void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);

// 3. 定义Feign代理
// 在DepositoryAgentApiAgent接口中新增confirmRepayment方法，用于向存管代理服务发请求
@PostMapping("/depository-agent/confirm-repayment")
RestResponse<String> confirmRepayment(@RequestBody RepaymentRequest repaymentRequest);

// 4. 在RepaymentServiceImpl中实现invokeConfirmRepayment方法：
@Override
public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    RestResponse<String> repaymentResponse = 
        depositoryAgentApiAgent.confirmRepayment(repaymentRequest);
}
```

画面7：
```java
// 1.2 获取项目信息
List<CenderDTO> tenders = projectDTO.getTenders();

// 1.3 计算应还的总天数
Double ceil = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = ceil.intValue();

// 1.4 还款方式，只支持等额本息
String repaymentWay = projectDTO.getRepaymentWay();

// 1.5 生成还款计划
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO, projectDTO.getTenders());
    List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
    // 1.6 生成还款明细
    for (CenderDTO tender : projectDTO.getTenders()) {
        EqualInterestRepayment receipt = RepaymentUtil.fixedRepayment(tenderDTO, tender.getTenderAmount(), tender.getTenderPeriod());
    }
}
```

画面8：
```java
@Override
public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    depositoryAgentApiAgent.confirmRepayment(repaymentRequest);
}
```

画面10：
```java
// 检查存管代理服务处理请求失败
if (repaymentResponse == null) {
    throw new BusinessException("存管代理服务处理请求失败");
}
```

画面11：
```java
@Override
public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    RestResponse<String> repaymentResponse = depositoryAgentApiAgent.confirmRepayment(repaymentRequest);
    if (repaymentResponse.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000.getCode())) {
        // 处理成功
    }
}
```

画面12：
```java
// 检查存管代理服务处理请求失败
if (repaymentResponse == null) {
    throw new BusinessException("存管代理服务处理请求失败");
}
```

画面13：
```java
@Override
public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    RestResponse<String> repaymentResponse = depositoryAgentApiAgent.confirmRepayment(repaymentRequest);
    if (!repaymentResponse.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000.getCode())) {
        throw new BusinessException("交易失败");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：1. 接口描述
内容：
1) 请求存管代理服务进行确认还款
2) 根据返回结果处理后续流程
2. 接口定义
在RepaymentService接口中，新增invokeConfirmRepayment方法，接到消息后需要调用该方法：

画面6：
标题：3. 定义Feign代理
内容：
在DepositoryAgentApiAgent接口中新增confirmRepayment方法，用于向存管代理服务发请求
@PostMapping("/depository-agent/confirm-repayment")
RestResponse<String> confirmRepayment(@RequestBody RepaymentRequest repaymentRequest);

4. 在RepaymentServiceImpl中实现invokeConfirmRepayment方法：
@Override
public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    RestResponse<String> repaymentResponse = 
        depositoryAgentApiAgent.confirmRepayment(repaymentRequest);
}

画面14：
流程图标题：用户还款成功流程图
流程：
1.10 还款成功
1.1 发送确认还款信息
1.2 确认还款处理
1.3 更新还款明细，状态为“已还款”
1.4 更新还款计划，状态为“已还款”
1.5 更新交易记录，状态为“已还款”
2.1 通过交易明细生成签名及票据
2.2 通过交易明细生成交易记录
2.3 更新交易记录，状态为“未同步”
2.4 还款成功（直接抵扣）
2.5 更新交易记录，状态为“已还款”
2.6 更新还款明细，状态为“已还款”
2.7 更新交易记录，状态为“已还款”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
