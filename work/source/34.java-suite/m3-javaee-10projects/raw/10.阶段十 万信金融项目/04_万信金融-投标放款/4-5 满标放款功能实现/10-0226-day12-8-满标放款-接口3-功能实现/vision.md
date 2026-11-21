# 画面线理解：day12-8-满标放款-接口3-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-8-满标放款-接口3-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:16, 01:37, 02:10, 02:28, 02:56, 03:19, 03:52, 04:36, 05:12, 05:41, 06:42, 06:58, 07:28, 07:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:50:40

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
String url = configService.getDepositoryUrl() + "/service";
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
String url = configService.getDepositoryUrl() + "/service";
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
