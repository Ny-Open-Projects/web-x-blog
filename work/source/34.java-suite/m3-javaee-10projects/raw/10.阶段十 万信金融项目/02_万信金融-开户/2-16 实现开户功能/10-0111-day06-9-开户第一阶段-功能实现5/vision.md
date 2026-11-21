# 画面线理解：day06-9-开户第一阶段-功能实现5

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-9-开户第一阶段-功能实现5_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:12, 00:28, 00:43, 01:02, 01:17, 01:56, 03:28, 04:02, 04:22, 04:46, 04:59, 05:13, 06:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:18:40

1) 这一组画面整体在讲用户开户流程的前后端代码实现与系统架构交互。

2) 按时间顺序列出每张画面的要点：
画面1：展示ConsumerServiceImpl类中创建银行卡的代码逻辑，包括设置卡号、手机号、状态，并调用bankCardService保存。
画面2：展示ConsumerServiceImpl类中创建用户的逻辑，包括调用accountAgent注册账户并判断返回码。
画面3：展示ConsumerController类中用户注册的REST接口，使用@RequestBody接收参数并调用service层。
画面4：展示ConsumerController类中“生成开户请求数据”的接口，使用@RequestBody接收参数并调用service层。
画面5：展示开户流程的架构图，包含“浏览器/APP”、“用户中心”、“存管代理服务”、“存管系统”、“开卡银行”等模块及其交互流程。
画面6：展示ConsumerServiceImpl类中判断用户是否已开户的逻辑，通过bankCardService查询并抛出异常。
画面7：展示ConsumerServiceImpl类中判断银行卡状态是否为“未激活”的逻辑，通过bankCardService查询并抛出异常。
画面8：展示ConsumerController类中“生成开户请求数据”的接口，调用service层。
画面9：展示SecurityUtil类中获取当前用户登录信息的代码，通过request.getAttribute("jsonToken")获取并返回LoginUser对象。
画面10：展示在文件资源管理器中选中LoginUser.java文件并右键选择“使用 Windows Defender 防火墙”选项。
画面11：展示SecurityUtil类中获取当前用户登录信息的代码，通过request.getAttribute("jsonToken")获取并返回LoginUser对象。
画面12：展示ConsumerController类中“生成开户请求数据”的接口，调用SecurityUtil获取用户信息并调用service层。
画面13：展示ConsumerController类中“生成开户请求数据”的接口，调用SecurityUtil获取用户信息并调用service层。
画面14：展示开户流程的架构图，包含“浏览器/APP”、“用户中心”、“存管代理服务”、“存管系统”、“开卡银行”等模块及其交互流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//保存用户银行卡信息
BankCard bankCard = new BankCard();
bankCard.setConsumerId(consumerDTO.getConsumerId());
bankCard.setBankCode(consumerRequest.getBankCode());
bankCard.setCardNumber(consumerRequest.getCardNumber());
bankCard.setMobile(consumerRequest.getMobile());
bankCard.setStatus(StatusCode.STATUS_OUT.getcode());
if (bankCardDTO exist BankCard = bankCardService
        .getById(bankCard.getConsumerId());
bankCard.setT(existBankCard.getT());
bankCardService.saveOrUpdate(bankCard);
return depositaryAgent.createConsumer(consumerRequest);
```

画面2：
```java
AccountRegisterDTO accountRegisterDTO = new AccountRegisterDTO();
BeanUtils.copyProperties(accountRegisterDTO, consumerRequest);
RestResponse<AccountRegisterDTO> restResponse = accountAgent.register(accountRegisterDTO);
if (restResponse.getCode() != CommonErrorCode.SUCCESS.getCode()) {
    throw new BusinessException(CommonErrorCode.E_140106);
}
```

画面3：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true, dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {
    return RestResponse.success();
}
```

画面4：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    return null;
}
```

画面6：
```java
//判断当前用户是否已经开户
ConsumerDTO consumerDTO = getMobile(consumerRequest.getMobile());
if (consumerDTO.getIsBindCard() == 1) {
    throw new BusinessException(ConsumerErrorCode.E_140105);
}
```

画面7：
```java
//判断提交过来的银行卡是否已绑定
BankCardDTO bankCardDTO = bankCardService.getByCardNumber(consumerRequest.getCardNumber());
if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getcode()) {
    throw new BusinessException(ConsumerErrorCode.E_140151);
}
```

画面8：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    return consumerService.createConsumer(consumerRequest);
}
```

画面9：
```java
package cn.itcast.wanxingzp.consumer.common;

import ...

public class SecurityUtil {
    //获取当前登录用户
    public static LoginUser getUser() {
        ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder
                .getRequestAttributes();
        if (servletRequestAttributes == null) {
            HttpServletRequest request = servletRequestAttributes.getRequest();
            Object jwt = request.getAttribute("jsonToken");
            if (jwt instanceof LoginUser) {
                return (LoginUser) jwt;
            }
        }
    }
}
```

画面12：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    SecurityUtil.getLoginUser().getMobile();
    return consumerService.createConsumer(consumerRequest);
}
```

画面13：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    SecurityUtil.getLoginUser().getMobile();
    return consumerService.createConsumer(consumerRequest);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：
架构图标题：“开户业务流程图”
模块：
- 浏览器/APP
- 用户中心
- 存管代理服务
- 存管系统
- 开卡银行
交互流程：
- 浏览器/APP → 用户中心 → 存管代理服务 → 存管系统 → 开卡银行
- 存管系统 → 开卡银行 → 存管系统
- 开卡银行 → 存管系统 → 用户中心 → 浏览器/APP

画面14：
架构图标题：“开户业务流程图”
模块：
- 浏览器/APP
- 用户中心
- 存管代理服务
- 存管系统
- 开卡银行
交互流程：
- 浏览器/APP → 用户中心 → 存管代理服务 → 存管系统 → 开卡银行
- 存管系统 → 开卡银行 → 存管系统
- 开卡银行 → 存管系统 → 用户中心 → 浏览器/APP

5) 不要评价画面美观，不要输出与课程无关的内容。
