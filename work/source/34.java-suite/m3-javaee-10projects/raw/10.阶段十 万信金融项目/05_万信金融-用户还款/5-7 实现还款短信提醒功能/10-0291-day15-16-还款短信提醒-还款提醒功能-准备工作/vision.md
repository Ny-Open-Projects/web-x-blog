# 画面线理解：day15-16-还款短信提醒-还款提醒功能-准备工作

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-16-还款短信提醒-还款提醒功能-准备工作_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:11, 02:07, 02:38, 03:21, 03:43, 04:11, 04:33, 05:23, 05:59, 06:48, 07:53, 08:36, 09:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:40:03

1) 这一组画面整体在讲如何在还款服务中通过 Feign 客户端调用用户服务，获取借款人信息并发送还款提醒。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了还款服务的项目结构，包含 controller、entity、mapper 等包，以及多个配置类和 Mapper 文件。
画面 2: 在数据库管理工具中查看了 `p2p_borrower` 表的结构，包含字段如 FULLNAME、USER_NO、MOBILE 等。
画面 3: 在数据库管理工具中查看了 `repayment_plan` 表的结构，包含字段如 ID、PROJECT_ID、USER_NO 等。
画面 4: 在数据库管理工具中查看了 `consumer` 表的结构，包含字段如 ID、FULLNAME、USER_NO 等。
画面 5: 在 IDEA 中查看了 PPT 内容，其中包含在 ConsumerAPI 中新增方法、在 ConsumerController 中实现方法、创建 Feign 代理、在 RepaymentService 中实现 sendRepaymentNotify 方法。
画面 6: 在 IDEA 中查看了 ConsumerAPI 接口定义，包含获取当前登录用户、获取借款人用户信息、获取当前登录用户余额信息等方法。
画面 7: 在 IDEA 中查看了 ConsumerAPI 接口定义，高亮显示了获取借款人用户信息的方法。
画面 8: 在 IDEA 中查看了 ConsumerController.java 文件，其中包含获取当前登录用户、获取借款人用户信息、获取用户可用余额等方法。
画面 9: 在 IDEA 中查看了 ConsumerAPI 接口定义，高亮显示了获取借款人用户信息的方法。
画面 10: 在 IDEA 中查看了 PPT 内容，其中包含在 ConsumerAPI 中新增方法、在 ConsumerController 中实现方法、创建 Feign 代理、在 RepaymentService 中实现 sendRepaymentNotify 方法。
画面 11: 在 IDEA 中查看了 ConsumerController.java 文件，高亮显示了获取借款人用户信息的方法。
画面 12: 在 IDEA 中查看了项目结构，高亮显示了还款服务的包路径。
画面 13: 在 IDEA 中查看了 ConsumerAgent.java 文件，其中定义了 ConsumerAPI 接口。
画面 14: 在 IDEA 中查看了 PPT 内容，其中包含在 ConsumerAPI 中新增方法、在 ConsumerController 中实现方法、创建 Feign 代理、在 RepaymentService 中实现 sendRepaymentNotify 方法。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 5:
```java
/**
 * 获取借款人用户信息-供服务访问
 * @param id 用户标识
 * @return
 */
RestResponse<BorrowerDTO> getBorrowerMobile(Long id);

@Override
@ApiOperation("获取借款人用户信息-供服务访问")
@ApiImplicitParam(name = "id", value = "用户标识", required = true, dataType = "Long", paramType = "path")
@GetMapping("/l/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(Long id) {
    return RestResponse.success(consumerService.getBorrower(id));
}

// 在还款服务中创建Feign代理
@FeignClient(value = "consumer-service")
public interface ConsumerApiAgent {
    @GetMapping(value = "/consumer/l/borrowers/{id}")
    RestResponse<BorrowerDTO> getBorrowerMobile(@PathVariable "id") Long id;
}
```

画面 6:
```java
RestResponse<ConsumerDTO> getCurUser(String mobile);
// 获取当前登录用户
@return
RestResponse<ConsumerDTO> getCurUser();

// 获取借款人用户信息
@Param id
@return
RestResponse<BorrowerDTO> getBorrower(Long id);

// 获取当前登录用户余额信息
@Param userNo 用户编码
@return
RestResponse<BalanceDetailsDTO> getBalance(String userNo);
```

画面 8:
```java
public RestResponse<ConsumerDTO> getMyUser() {
    ConsumerDTO consumerDTO = consumerService.getBorrower(SecurityUtil.getUser());
    return RestResponse.success(consumerDTO);
}

@Override
@ApiOperation("获取借款人用户信息-供服务访问")
@ApiImplicitParam(name = "id", value = "用户标识", required = true, dataType = "Long", paramType = "path")
@GetMapping("/my/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(@PathVariable Long id) {
    return RestResponse.success(consumerService.getBorrower(id));
}

@Override
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/l/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
    return RestResponse.success(consumerService.getBalance(userNo));
}
```

画面 13:
```java
package cn.itcast.wanxingzp.repayment.agent;

import cn.itcast.wanxingzp.repayment.api.ConsumerAPI;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(value = "consumer-service")
public interface ConsumerApiAgent {
    @GetMapping(value = "/consumer/l/borrowers/{id}")
    RestResponse<BorrowerDTO> getBorrowerMobile(@PathVariable Long id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构、表格数据：
画面 5:
标题：8.3.1 还款服务还款提醒接口
内容：
1. 在 ConsumerAPI 中新增一个方法，用来根据用户 id 获取用户信息
2. 在 ConsumerController 类中实现该方法
3. 在还款服务中创建 Feign 代理
4. 在 RepaymentService 中实现 sendRepaymentNotify 方法

画面 10:
标题：8.3.1 还款服务还款提醒接口
内容：
1. 在 ConsumerAPI 中新增一个方法，用来根据用户 id 获取用户信息
2. 在 ConsumerController 类中实现该方法
3. 在还款服务中创建 Feign 代理
4. 在 RepaymentService 中实现 sendRepaymentNotify 方法

画面 14:
标题：8.3.1 还款服务还款提醒接口
内容：
1. 在 ConsumerAPI 中新增一个方法，用来根据用户 id 获取用户信息
2. 在 ConsumerController 类中实现该方法
3. 在还款服务中创建 Feign 代理
4. 在 RepaymentService 中实现 sendRepaymentNotify 方法
