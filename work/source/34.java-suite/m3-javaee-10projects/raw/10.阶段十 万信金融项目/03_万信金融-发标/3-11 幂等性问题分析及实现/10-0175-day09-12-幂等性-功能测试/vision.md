# 画面线理解：day09-12-幂等性-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-11 幂等性问题分析及实现
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-11 幂等性问题分析及实现\day09-12-幂等性-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:14, 02:42, 03:16, 04:25, 05:20, 05:51, 06:54, 07:49, 08:43, 09:11, 09:59, 10:43, 12:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:09:48

1) 这一组画面整体在讲什么（一句话）：
在分布式系统中，通过为请求添加唯一标识（REQUEST_NO）并利用 Redis 的原子性操作，实现幂等性控制，避免重复提交。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 讲解功能测试中需要修改数据库表结构，为每个请求添加唯一标识字段 REQUEST_NO。
画面 2: 展示了分布式系统中交易中心服务与多个存管代理服务集群的交互流程图，说明请求如何分发。
画面 3: 展示了 Java 代码中，若交易记录不存在则保存并返回 null 的逻辑。
画面 4: 展示了 Java 代码中，利用 Redis 的原子性操作（如 incrBy）来实现请求幂等性控制。
画面 5: 展示了在数据库中执行 SQL 语句，为多个表（如 pzp_transaction_0, pzp_transaction_1）添加 REQUEST_NO 字段。
画面 6: 讲解在 Project 类中新增对应的属性。
画面 7: 展示了向银行存管系统发送请求的代码，构造了请求体并调用 sendHttpPost 方法。
画面 8: 展示了代码中，若请求状态为 STATUS_OUT，则通过 Redis 原子操作获取并更新请求计数。
画面 9: 展示了代码中，若请求计数等于 1，则设置请求有效期并返回 null。
画面 10: 展示了代码中，若请求计数大于 1，则抛出业务异常。
画面 11: 展示了代码中，若请求计数等于 1，则设置请求有效期并返回 null。
画面 12: 展示了代码中，若请求计数大于 1，则抛出业务异常。
画面 13: 展示了代码中，若请求计数大于 1，则抛出业务异常。
画面 14: 展示了代码中，交易记录已存在且状态为“已同步”时，返回响应数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
ALTER TABLE pzp_transaction_0.project_0
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;
ALTER TABLE pzp_transaction_0.project_1
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;
ALTER TABLE pzp_transaction_1.project_0
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;
ALTER TABLE pzp_transaction_1.project_1
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;

画面 5:
ALTER TABLE pzp_transaction_0.project_0
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;
ALTER TABLE pzp_transaction_0.project_1
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;
ALTER TABLE pzp_transaction_1.project_0
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;
ALTER TABLE pzp_transaction_1.project_1
ADD COLUMN REQUEST_NO varchar(50) NULL COMMENT '发标请求流水号' AFTER
IS_ASSIGNMENT;

画面 3:
//1. 交易记录不存在，保存交易记录
if(null == depositorRecordDTO) {
saveDepositorRecord(depositorRecord);
return null;
}
//2. 重复点击，重复请求，利用redis的原子性，争夺执行权
if (StatusCode.STATUS_OUT.getCode() ==
depositorRecordDTO.getRequestStatus()) {
//如果requestNo不存在则返回，如果已经存在，则会返回（requestNo已存在个数+1）
Long count = cache.incrBy(requestNo, delta: 1L);
if (count == 1) {
cache.expire(requestNo, expire: 5); //设置requestNo有效期5秒
return null;
}

画面 4:
//1. 交易记录不存在，保存交易记录
if(null == depositorRecordDTO) {
saveDepositorRecord(depositorRecord);
return null;
}
//2. 重复点击，重复请求，利用redis的原子性，争夺执行权
if (StatusCode.STATUS_OUT.getCode() ==
depositorRecordDTO.getRequestStatus()) {
//如果requestNo不存在则返回，如果已经存在，则会返回（requestNo已存在个数+1）
Long count = cache.incrBy(requestNo, delta: 1L);
if (count == 1) {
cache.expire(requestNo, expire: 10); //设置requestNo有效期10秒
return null;
}

画面 7:
String sendHttpPostService = "http://localhost:8080/service";
return sendHttpPost(serviceName, "CREATE_PROJECT", url, reqData, depositorRecord);

画面 8:
Execute SQL: SELECT ID,REQUEST_NO,REQUEST_TYPE,OBJECT_TYPE,OBJECT_ID,CREATE_DATE,IS_SYN,REQUEST_STATUS,CONFIRM_DATE,RESPONSE_DATA FROM depositor_record WHERE project_name = 'xxx' AND server_port = '8080'

画面 9:
//3. 交易记录已存在，并且状态是“已同步”
return JSON.parseObject(depositorRecordDTO.getResponseData(),
new TypeReference<DepositorResponseDTO.Depositor.BaseResponse>() {});

画面 10:
//3. 交易记录已存在，并且状态是“已同步”
return JSON.parseObject(depositorRecordDTO.getResponseData(),
new TypeReference<DepositorResponseDTO.Depositor.BaseResponse>() {});

画面 11:
//3. 交易记录已存在，并且状态是“已同步”
return JSON.parseObject(depositorRecordDTO.getResponseData(),
new TypeReference<DepositorResponseDTO.Depositor.BaseResponse>() {});

画面 12:
//3. 交易记录已存在，并且状态是“已同步”
return JSON.parseObject(depositorRecordDTO.getResponseData(),
new TypeReference<DepositorResponseDTO.Depositor.BaseResponse>() {});

画面 13:
//3. 交易记录已存在，并且状态是“已同步”
return JSON.parseObject(depositorRecordDTO.getResponseData(),
new TypeReference<DepositorResponseDTO.Depositor.BaseResponse>() {});

画面 14:
//3. 交易记录已存在，并且状态是“已同步”
return JSON.parseObject(depositorRecordDTO.getResponseData(),
new TypeReference<DepositorResponseDTO.Depositor.BaseResponse>() {});

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
架构图结构：
- DB ... 位于顶部，向下连接到三个“存管代理服务”（A、B、C）。
- 三个“存管代理服务”（A、B、C）位于一个矩形框内，框内标注“集群”。
- “交易中心服务”位于底部，向上连接到三个“存管代理服务”（A、B、C）。
- “交易中心服务”向三个“存管代理服务”（A、B、C）分别发送“第1次请求”、“第2次请求”、“第3次请求”。
- 三个“存管代理服务”（A、B、C）分别向上连接到“DB ...”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
