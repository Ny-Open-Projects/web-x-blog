# 画面线理解：day09-4-审核标的-存管代理-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-10 实现审核标的功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-10 实现审核标的功能\day09-4-审核标的-存管代理-功能实现1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:48, 02:01, 02:51, 03:24, 03:56, 06:03, 07:39, 08:25, 10:06, 11:26, 12:43, 13:31, 14:39, 15:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:03:04

1) 这一组画面整体在讲什么（一句话）：
演示一个银行存款项目中，如何在Java服务端实现“新建标”业务的请求处理、数据转换、签名加密及与银行系统交互的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDEA项目结构，当前选中的是 `wanningzp-depository-agent-service` 模块下的 `mapper` 包，准备进行开发。
画面2：展示文件资源管理器，位于 `wanningzp > day09 > 资料` 目录，包含 `ElasticSearch`、`画`、`用户发债.png` 等文件。
画面3：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryResponseDTO.java` 文件，其中定义了 `@ApiModelProperty("签名数据") private String signature;` 字段。
画面4：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryBaseResponse.java` 文件，其中定义了 `@ApiModelProperty("返回码") private String respCode;`、`@ApiModelProperty("错误信息") private String respMsg;`、`@ApiModelProperty("交易状态") private Integer status;`、`@ApiModelProperty("请求流水号") private String requestNo;` 等字段。
画面5：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `@Autowired private ConfigService configService;` 和 `public GatewayRequest createConsumer(ConsumerRequest consumerRequest) { ... }` 方法。
画面6：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `public DepositoryResponseDTO DepositoryBaseResponse createProject(ProjectDTO projectDTO) { ... }` 方法。
画面7：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `public DepositoryResponseDTO DepositoryBaseResponse createProject(ProjectDTO projectDTO) { ... }` 方法，当前光标在 `saveDepositoryRecord` 方法调用处。
画面8：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRequestTypeCode.java` 文件，其中定义了 `public enum DepositoryRequestTypeCode { CREATE("CREATE", "新增标的"), ... }` 枚举。
画面9：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `private DepositoryRecord saveDepositoryRecord(String requestNo, String requestType, String objectType, Long objectId) { ... }` 方法。
画面10：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());` 方法调用。
画面11：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());` 方法调用。
画面12：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());` 方法调用。
画面13：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());` 方法调用。
画面14：在 `wanningzp-depository-agent-service` 项目中，查看 `DepositoryRecordServiceImpl.java` 文件，其中定义了 `private ProjectRequestDataDTO convertProjectDTOToProjectRequestDataDTO(ProjectDTO projectDTO, String requestNo) { if (projectDTO == null) { return null; } }` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@Data
public class DepositoryResponseDTO implements Serializable {
    /**
     * 业务数据报文，JSON格式
     */
    @ApiModelProperty("业务数据报文，JSON格式")
    private String respData;

    /**
     * 签名
     */
    @ApiModelProperty("签名数据")
    private String signature;
}
```

画面4：
```java
@Encoders(chain = true)
public class DepositoryBaseResponse implements Serializable {
    @ApiModelProperty("返回码")
    private String respCode;
    @ApiModelProperty("错误信息")
    private String respMsg;
    @ApiModelProperty("交易状态")
    private Integer status;
    @ApiModelProperty("请求流水号")
    private String requestNo;
}
```

画面5：
```java
@Service
public class DepositoryRecordServiceImpl extends ServiceImpl<DepositoryRecordMapper, DepositoryRecord> implements DepositoryRecordService {

    @Autowired
    private ConfigService configService;

    public GatewayRequest createConsumer(ConsumerRequest consumerRequest) {
        // 保存交易记录
        saveDepositoryRecord(consumerRequest);
        // 签名数据加密
        String reqData = JSON.toJSONString(consumerRequest);
        String sign = RSAUtil.sign(reqData, configService.getPrivateKey(), "utf-8");
        GatewayRequest gatewayRequest = new GatewayRequest();
        gatewayRequest.setServiceName("PERSONAL_REGISTER");
    }
```

画面6：
```java
public DepositoryResponseDTO DepositoryBaseResponse createProject(ProjectDTO projectDTO) {
    // 保存交易记录
    DepositoryRecord depositoryRecord = saveDepositoryRecord(projectDTO.getRequestNo(), DepositoryRequestTypeCode.CREATE.getCode(), "Project", projectDTO.getId());
    // 签名数据
    ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());
    // 在银行存管系统发送数据（你的信息）
    String jsonStr = JSON.toJSONString(projectRequestDataDTO);
    String base64Str = EncryptUtil.encodeUTF8StringBase64(jsonStr);
    String url = configService.getDepositoryUrl() + "/service";
    // 向银行存管系统发送HTTP请求
    return sendHttpGet("CREATE_PROJECT", url, base64Str, depositoryRecord);
    // 保存交易记录
}
```

画面7：
```java
@Override
public DepositoryResponseDTO DepositoryBaseResponse createProject(ProjectDTO projectDTO) {
    // 保存交易记录
    DepositoryRecord depositoryRecord = saveDepositoryRecord(projectDTO.getRequestNo(), DepositoryRequestTypeCode.CREATE.getCode(), "Project", projectDTO.getId());
    // 签名数据
    ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());
    // 在银行存管系统发送数据（你的信息）
    String jsonStr = JSON.toJSONString(projectRequestDataDTO);
    String base64Str = EncryptUtil.encodeUTF8StringBase64(jsonStr);
    String url = configService.getDepositoryUrl() + "/service";
    // 向银行存管系统发送HTTP请求
    return sendHttpGet("CREATE_PROJECT", url, base64Str, depositoryRecord);
    // 保存交易记录
}
```

画面8：
```java
public enum DepositoryRequestTypeCode {
    /**
     * 新增标的
     */
    CREATE("CREATE", "新增标的"),
    /**
     * 用户投标
     */
    TRADING("TRADING", "用户投标"),
    /**
     * 审核成功放款
     */
    FULL_LOAD("FULL_LOAD", "审核成功放款"),
    /**
     * 修改标的的状态
     */
    MODIFY_STATUS("MODIFY_STATUS", "修改标的的状态"),
}
```

画面9：
```java
private DepositoryRecord saveDepositoryRecord(String requestNo, String requestType, String objectType, Long objectId) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(requestNo);
    depositoryRecord.setRequestType(requestType);
    depositoryRecord.setObjectType(objectType);
    depositoryRecord.setObjectId(objectId);
    depositoryRecord.setCreateDate(LocalDateTime.now());
    depositoryRecord.setRequestStatus(StatusCode.STATUS_OUT.getCode());
    save(depositoryRecord);
    return depositoryRecord;
}
```

画面10：
```java
ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());
```

画面11：
```java
ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());
```

画面12：
```java
ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());
```

画面13：
```java
ProjectRequestDataDTO projectRequestDataDTO = convertProjectDTOToProjectRequestDataDTO(projectDTO, depositoryRecord.getRequestNo());
```

画面14：
```java
private ProjectRequestDataDTO convertProjectDTOToProjectRequestDataDTO(ProjectDTO projectDTO, String requestNo)
