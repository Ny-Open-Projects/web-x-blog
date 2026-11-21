# 画面线理解：day12-16-满标放款-前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-16-满标放款-前后端集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 02:24, 05:05, 05:56, 06:59, 08:07, 08:53, 09:21, 10:00, 11:15, 11:48, 12:32, 13:17, 14:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:57:24

1) 这一组画面整体在讲一个贷款项目从发起、审核、放款到还款的全流程业务逻辑与对应的代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个贷款业务流程图，包含“调用方APP”、“交易中心”、“存管代理”、“还款服务”、“存管系统”等模块，描述了从用户发起贷款到最终还款的流程。
画面2：展示贷款管理后台的“贷款列表”，列出了“张伟先生5次借款”、“张伟先生4次借款”等记录，状态为“募集中”，年化利率10%。
画面3：展示贷款业务流程图，聚焦在“交易中心”和“存管代理”之间的交互。
画面4：展示IDE中“ProjectService.java”文件，列出“测试功能”包括：1. 查看存管服务是否保存交易记录；2. 查看交易中心是否修改项目状态；3. 查看还款服务是否生成并保存还款计划；4. 查看还款服务是否收到后端测试。
画面5：展示贷款详情页面，显示“张伟先生”贷款信息，金额12000元，期限12个月，借款人信息包括姓名、年龄、性别、手机号、身份证号。
画面6：展示贷款业务流程图，聚焦在“交易中心”和“存管代理”之间的交互。
画面7：展示IDE中“ProjectService.java”文件，代码部分为：RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatus); if (modifyProjectStatus.getRemit().equals(DepositoryReturnCode.RETURN_CODE_0000.getcode())) { project.setStatus(ProjectCode.REPAYING.getCode()); updateProject(); }
画面8：展示IDE中“ProjectService.java”文件，代码部分为：ProjectWithTenderDTO project = new ProjectWithTenderDTO(); project.setProjectId(projectId); project.setTenderList(tenderList); project.setCommissionInvestorAnnualRate(configService.getCommissionInvestorAnnualRate()); project.setCommissionBorrowerAnnualRate(configService.getBorrowerAnnualRate());
画面9：展示IDE中“ProjectService.java”文件，代码部分为：LoadRequest loadRequest = generateLoanRequest(project, tenderList, commission); RestResponse<String> restResponse = depositoryAgentApiAgent.confirmLoan(loadRequest); if (restResponse.getRemit().equals(DepositoryReturnCode.RETURN_CODE_0000.getcode())) { updateTenderStatusAlreadyLoan(tenderList); }
画面10：展示IDE中“ProjectService.java”文件，代码部分为：ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO(); modifyProjectStatusDTO.setProjectId(project.getId()); modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode()); modifyProjectStatusDTO.setRequestId(loadRequest.getRequestId());
画面11：展示IDE中“ProjectService.java”文件，代码部分为：ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO(); modifyProjectStatusDTO.setProjectId(project.getId()); modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode()); modifyProjectStatusDTO.setRequestId(loadRequest.getRequestId());
画面12：展示IDE中“ProjectService.java”文件，代码部分为：ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO(); modifyProjectStatusDTO.setProjectId(project.getId()); modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode()); modifyProjectStatusDTO.setRequestId(loadRequest.getRequestId());
画面13：展示数据库管理工具，显示“p2p_transaction_0.sql”文件，表结构包括“AMOUNT”、“TENDER_STATUS”、“CREATE_DATE”、“REQUEST_ID”、“STATUS”、“PROJECT_NAME”、“PROJECT_PERIODS”、“PROJECT_ANNUAL_RATE”等字段。
画面14：展示贷款业务流程图，聚焦在“交易中心”和“存管代理”之间的交互。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面4：
```java
测试功能：
1. 查看存管服务是否保存交易记录，状态是否从“未同步”改为“已同步”
2. 查看交易中心是否修改项目状态为“已放款”
3. 查看还款服务是否生成并保存还款计划，且还款计划收到后端测试
```

画面7：
```java
RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatus); 
if (modifyProjectStatus.getRemit().equals(DepositoryReturnCode.RETURN_CODE_0000.getcode())) { 
    project.setStatus(ProjectCode.REPAYING.getCode()); 
    updateProject(); 
}
```

画面8：
```java
ProjectWithTenderDTO project = new ProjectWithTenderDTO(); 
project.setProjectId(projectId); 
project.setTenderList(tenderList); 
project.setCommissionInvestorAnnualRate(configService.getCommissionInvestorAnnualRate()); 
project.setCommissionBorrowerAnnualRate(configService.getBorrowerAnnualRate());
```

画面9：
```java
LoadRequest loadRequest = generateLoanRequest(project, tenderList, commission); 
RestResponse<String> restResponse = depositoryAgentApiAgent.confirmLoan(loadRequest); 
if (restResponse.getRemit().equals(DepositoryReturnCode.RETURN_CODE_0000.getcode())) { 
    updateTenderStatusAlreadyLoan(tenderList); 
}
```

画面10：
```java
ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO(); 
modifyProjectStatusDTO.setProjectId(project.getId()); 
modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode()); 
modifyProjectStatusDTO.setRequestId(loadRequest.getRequestId());
```

画面12：
```java
ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO(); 
modifyProjectStatusDTO.setProjectId(project.getId()); 
modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode()); 
modifyProjectStatusDTO.setRequestId(loadRequest.getRequestId());
```

画面13：
```sql
AMOUNT
TENDER_STATUS
CREATE_DATE
REQUEST_ID
STATUS
PROJECT_NAME
PROJECT_PERIODS
PROJECT_ANNUAL_RATE
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、3、6、14：展示一个贷款业务流程图，包含“调用方APP”、“交易中心”、“存管代理”、“还款服务”、“存管系统”等模块，描述了从用户发起贷款到最终还款的流程。
画面2：展示贷款管理后台的“贷款列表”，列出了“张伟先生5次借款”、“张伟先生4次借款”等记录，状态为“募集中”，年化利率10%。
画面5：展示贷款详情页面，显示“张伟先生”贷款信息，金额12000元，期限12个月，借款人信息包括姓名、年龄、性别、手机号、身份证号。
画面13：展示数据库管理工具，显示“p2p_transaction_0.sql”文件，表结构包括“AMOUNT”、“TENDER_STATUS”、“CREATE_DATE”、“REQUEST_ID”、“STATUS”、“PROJECT_NAME”、“PROJECT_PERIODS”、“PROJECT_ANNUAL_RATE”等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
