# 画面线理解：day14-11-用户还款-第三阶段-本地事务2

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-11-用户还款-第三阶段-本地事务2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:51, 02:34, 04:05, 04:51, 06:35, 08:00, 09:00, 09:23, 10:04, 10:46, 11:12, 12:06, 12:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:20:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在还款服务中，通过代码逻辑更新还款计划状态并持久化对应的还款明细。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `RepaymentServiceImpl.java` 中 `confirmRepayment` 方法的代码，重点是更新 `receivable_plan` 表的状态为“已还款”。
画面2：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面3：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面4：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面5：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面6：在 `confirmRepayment` 方法中，创建 `ReceivableDetail` 对象并设置其属性，然后调用 `receivableDetailMapper.insert(...)` 插入数据。
画面7：展示 `ReceivableDetailMapper.java` 文件，该文件是 MyBatis 的 Mapper 接口，继承自 `BaseMapper<ReceivableDetail>`。
画面8：展示 `RepaymentServiceImpl.java` 文件中 `startRepayment` 方法的代码，用于生成还款计划。
画面9：展示 `RepaymentServiceImpl.java` 文件中 `confirmRepayment` 方法的代码，重点是创建 `ReceivableDetail` 对象并插入数据库。
画面10：在 `confirmRepayment` 方法中，通过 `receivablePlan.setAmount(...)` 设置还款计划金额。
画面11：在 `confirmRepayment` 方法中，通过 `receivablePlan.setConsumerId(...)` 设置还款计划的消费者ID。
画面12：在 `confirmRepayment` 方法中，通过 `receivablePlan.setProjectId(...)` 设置还款计划的项目ID。
画面13：在 `confirmRepayment` 方法中，通过 `receivablePlan.setShouldRepaymentDate(...)` 设置还款计划的应还款日期。
画面14：展示一个流程图，描述了还款处理的完整流程，包括接收请求、更新交易记录、生成还款计划、插入还款明细等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//2.1 更新receivable_plan表为：已收
receivablePlanMapper.update(entity: null, Wrappers.<RepaymentDetail>lambdaUpdate().set(RepaymentDetail::getStatus, StatusCode.STATUS_IN.getCode()));
```

画面2：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面3：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面4：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面5：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面6：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面7：
```java
package cn.ictast.wanxingzp.repayment.mapper;

import cn.ictast.wanxingzp.repayment.entity.ReceivableDetail;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

/**
 * @author
 */
public interface ReceivableDetailMapper extends BaseMapper<ReceivableDetail> {

}
```

画面8：
```java
private ReceivablePlanMapper receivablePlanMapper;
private RepaymentDetailMapper repaymentDetailMapper;
private DepositoryAgentApiAgent depositoryAgentApiAgent;

@Transactional(rollbackFor = BusinessException.class)
public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
    //2.1 生成借款人还款计划
    //2.2 获取还款计划的信息
    ProjectDTO projectDTO = projectWithTendersDTO.getProject();
    //2.3 获取投标信息
    List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
```

画面9：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面10：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面11：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面12：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面13：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面14：
无代码或配置，为流程图。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
流程图标题：用户还款计划处理流程图。
流程图结构：
- 起始节点：用户发起还款请求。
- 步骤1.6：发送处理请求，调用接口。
- 步骤1.7：压线还款金额。
- 步骤1.8：原交易成功。
- 步骤2.1：发送确认还款事务消息。
- 步骤2.2：默认还款处理。
- 步骤2.3：处理确认还款请求。
- 步骤2.4：更新交易记录，状态为“已同步”。
- 步骤2.5：根据还款计划生成签名及摘要。
- 步骤2.6：更新还款交易信息为“已还款”。
- 步骤3.1：更新交易记录，状态为“已同步”。
- 步骤3.2：更新还款计划，状态为“已还款”。
- 步骤3.3：更新还款明细，状态为“已还款”。
- 步骤3.4：更新还款计划，状态为“已还款”。
- 步骤3.5：更新还款明细，状态为“已还款”。
- 步骤3.6：更新还款计划，状态为“已还款”。
-
