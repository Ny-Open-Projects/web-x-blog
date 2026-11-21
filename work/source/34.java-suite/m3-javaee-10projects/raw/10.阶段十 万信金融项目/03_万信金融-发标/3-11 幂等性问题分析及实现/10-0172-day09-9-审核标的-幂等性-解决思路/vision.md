# 画面线理解：day09-9-审核标的-幂等性-解决思路

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-11 幂等性问题分析及实现
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-11 幂等性问题分析及实现\day09-9-审核标的-幂等性-解决思路_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:16, 00:47, 01:11, 01:51, 02:59, 03:53, 04:58, 05:28, 05:51, 06:37, 06:57, 07:08, 09:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:07:17

1) 这一组画面整体在讲如何通过“幂等性”设计解决分布式系统中因网络问题或重复请求导致的业务数据不一致问题。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个架构图，包含“交易中心服务”向三个“存管代理服务”（A、B、C）发起请求，每个代理服务再连接到“DB”，并标注“第1次请求”、“第2次请求”、“第3次请求”。
画面2：展示一个弹窗，内容为“如果sql查询语句不带条件，可以吗？不行，如何解决重复量问题？”，并给出一个示例，说明如何通过logstash和MODIFY_DATE字段解决。
画面3：展示架构图，内容与画面1相同，但“交易中心服务”下方标注“前端”。
画面4：展示架构图，内容与画面1相同。
画面5：展示文档内容，说明“幂等性”的定义，并引出“3.6.2 功能实现”部分，描述当交易中心服务请求存管代理服务时，需先获取requestNo并记录，然后分三种情况处理。
画面6：展示一个时序图，描述“调数据/APP”、“交易中心”、“存管代理服务”、“标的待签服务”、“银行存管系统”之间的交互流程。
画面7：展示时序图，内容与画面6相同。
画面8：展示文档内容，说明“幂等性”的定义，并引出“3.6.2 功能实现”部分。
画面9：展示代码，显示“DepositoryRecordServiceImpl”类中的“saveDepositoryRecord”方法，用于保存交易记录。
画面10：展示代码，显示“DepositoryRecordServiceImpl”类中的“handleTdempotent”方法，用于处理幂等性。
画面11：展示代码，显示“DepositoryRecordServiceImpl”类中的“handleTdempotent”方法，光标位于方法定义处。
画面12：展示“DepositoryBaseResponse”类的代码，包含“respCode”、“respMsg”、“status”、“requestNo”等字段。
画面13：展示“DepositoryResponseDTO”类的代码，包含“respData”、“signature”等字段。
画面14：展示“DepositoryRecordServiceImpl”类中的“handleTdempotent”方法，光标位于方法定义处，注释说明“1. 交易记录不存在”、“2. 交易记录存在，并且状态为‘已同步’”、“3. 重复点击，重复请求，利用redis原子性，当务以行权”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面5：
在DepositoryRecordServiceImpl类中单定义一个方法实现幂等性：
/**
 * 实现幂等性
 * @param depositoryRecord
 * @return
 */
private depositoryResponseTO depositoryBaseResponse handleTdempotent(DepositoryRecord depositoryRecord) {
    //根据requestNo查询
    String requestNo = depositoryRecord.getRequestNo();
    DepositoryRecordDTO depositoryRecordDTO = getbyRequestNo(requestNo);
}

画面9：
private ProjectRequestDataDTO convertProjectDTOToObjectRequestDataDTO(ProjectDTO projectDTO, String requestNo) {
    if (projectDTO == null) {
        return null;
    }
    ProjectRequestDataDTO requestDataDTO = new ProjectRequestDataDTO();
    BeanUtils.copyProperties(projectDTO, requestDataDTO);
    requestDataDTO.setRequestNo(requestNo);
    return requestDataDTO;
}

画面10：
private void saveDepositoryRecord(ConsumerRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(ConsumerRequest.CONSUMER_CREATE.getCode());
    depositoryRecord.setObjectType(ConsumerRequest.CONSUMER.getCode());
    depositoryRecord.setObjectID(consumerRequest.getObjectId());
    depositoryRecord.setCreateTime(LocalDateTime.now());
    depositoryRecord.setRequestStatus(StatusCode.STATUS_OUT.getCode());
    save(depositoryRecord);
}

画面11：
private DepositoryResponseDTO DepositoryBaseResponse handleTdempotent(DepositoryRecord depositoryRecord) {
}

画面12：
public class DepositoryBaseResponse implements Serializable {
    @MyModelProperty("返回码")
    private String respCode;
    @MyModelProperty("描述信息")
    private String respMsg;
    @MyModelProperty("交易状态")
    private Integer status;
    @MyModelProperty("请求流水号")
    private String requestNo;
}

画面13：
@Data
public class DepositoryResponseDTO implements Serializable {
    /**
     * 业务数据报文，JSON格式
     */
    @MyModelProperty("业务数据报文，JSON格式")
    private RespData;
    /**
     * 签名
     */
    @MyModelProperty("签名数据")
    private String signature;
}

画面14：
private DepositoryResponseDTO DepositoryBaseResponse handleTdempotent(DepositoryRecord depositoryRecord) {
    //1. 交易记录不存在
    //2. 交易记录存在，并且状态为‘已同步’
    //3. 重复点击，重复请求，利用redis原子性，当务以行权
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：架构图，包含“DB”、“存管代理服务A”、“存管代理服务B”、“存管代理服务C”、“交易中心服务”，并标注“第1次请求”、“第2次请求”、“第3次请求”。
画面6：时序图，包含“调数据/APP”、“交易中心”、“存管代理服务”、“标的待签服务”、“银行存管系统”，并标注“1.1.借款人发标”、“1.3.发标成功,待审核”、“2.1.管理员审核通过”、“2.2.标的的信息同步”、“2.3.通过秘钥生成签名及数据”、“2.4.保存交易记录,状态为:未同步”、“2.5.标的的信息同步:直连接口”、“2.6.标的的信息保存”、“2.7.标的的信息同步成功”、“2.8.更新交易记录,状态为:已同步”、“2.9.标的的信息同步成功”、“2.10.建立标的索引”、“2.11.建立索引”、“2.12.索引建立成功”、“2.13.保存标的的信息,数据状态为:已发布”、“2.14.审核成功”。
画面5：文档标题“3.6.2 功能实现”，内容描述“当存管代理服务被交易中心请求时，首先获取该请求的requestNo并记录，然后分三种情况进行处理：1. 若交易记录不存在则新增记录，requestNo为唯一，新保存的数据的状态为“未同步”。2. 若交易记录存在并且数据状态为“未同步”，此阶段存在并发可能，利用redis原子性，争抢请求行权，若count大于1，说明已有线程在执行操作，直接返回“正在处理”。3. 若交易记录存在并且数据状态为“已同步”，直接返回处理结果。”
画面8：文档标题“3.6.2 功能实现”，内容与画面5相同。
画面14：代码注释“//1. 交易记录不存在”、“//2. 交易记录存在，并且状态为‘已同步’”、“//3. 重复点击，重复请求，利用redis原子性，当务以行权”。
