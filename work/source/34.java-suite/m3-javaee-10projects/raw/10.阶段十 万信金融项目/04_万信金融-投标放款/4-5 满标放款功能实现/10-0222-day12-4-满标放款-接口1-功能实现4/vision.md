# 画面线理解：day12-4-满标放款-接口1-功能实现4

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-4-满标放款-接口1-功能实现4_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:50, 02:50, 03:34, 04:02, 04:50, 05:20, 06:00, 06:37, 07:32, 08:07, 08:40, 09:16, 10:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:47:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在贷款审批服务中，通过修改项目状态（如从“已放款”改为“还款中”）并调用外部代理服务来完成状态变更，并展示相关代码实现和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个流程图，描述了从“前端APP”到“业务系统”的贷款审批流程，其中包含“项目管理”、“还款服务”、“清算系统”等模块，以及状态变更（如“已放款”→“还款中”）和异常处理（如“失败”→“已拒绝”）。
画面2：展示IDE中`ProjectServiceImpl.java`文件，代码中定义了`confirmLoan`、`userAutoProTransaction`、`modifyProjectStatus`等方法，以及`depositoryAgentAgent`类的`else`分支抛出`BusinessException`异常。
画面3：展示IDE中`ModifyProjectStatusDTO.java`文件，定义了`requestNo`、`projectNo`、`projectStatus`、`id`等字段，并展示`main`方法中创建`ModifyProjectStatusDTO`对象。
画面4：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并设置`projectStatus`为`REPAYING`。
画面5：展示IDE中`ProjectServiceImpl.java`文件，代码中设置`modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode())`。
画面6：展示IDE中`ProjectServiceImpl.java`文件，代码中设置`modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo())`。
画面7：展示IDE中`ProjectServiceImpl.java`文件，代码中设置`modifyProjectStatusDTO.setProjectNo(project.getProjectNo())`。
画面8：展示数据库管理工具，显示`pjq_transaction_1`数据库中的`loan`表数据，包含`PROJECT_ID`、`PROJECT_NO`、`AMOUNT`、`STATUS`、`CREATE_DATE`等字段。
画面9：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法。
画面10：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并判断返回值是否等于`RETURN_CODE_00000`。
画面11：展示IDE中`ProjectServiceImpl.java`文件，代码中抛出`BusinessException(TransactionErrorCode.E_150113)`异常。
画面12：展示数据库管理工具，显示`pjq_transaction_1`数据库中的`project_1`表数据，包含`PROJECT_ID`、`PROJECT_NO`、`AMOUNT`、`STATUS`、`CREATE_DATE`等字段。
画面13：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并设置`project.setStatus(ProjectCode.REPAYING.getCode())`。
画面14：展示IDE中`ProjectServiceImpl.java`文件，代码中调用`depositoryAgentApiAgent.modifyProjectStatus`方法，并设置`project.setStatus(ProjectCode.REPAYING.getCode())`，并添加注释“如果处理成功，就修改的状态方法函数中”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
confirmLoan(LoanRequest loanRequest)
userAutoProTransaction(UserAutoProTransactionRequest userAutoProTransactionRequest)
modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO)
```
```java
depositoryAgentAgent
```
```java
else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```
画面3：
```java
private String requestNo;
private String projectNo;
private String projectStatus;
private Long id;
```
```java
public static void main(String[] args) throws UnsupportedEncodingException {
    // 使用省略号续写 一修改状态为还款中
    // 构造请求参数
    ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
    modifyProjectStatusDTO.setId(project.getId());
```
画面4：
```java
Project project = projectPathById(14);
// 校验信息
queryWrapper.lambda().eq(Project::getProjectId, 14);
List<Tender> tenderList = tenderMapper.selectList(queryWrapper);
// 生成放款请求
LoanRequest loanRequest = generateLoanRequest(project, tenderList);
// 第二阶段，放款
RestResponse<String> restResponse = depositoryAgentApiAgent.confirmLoan(loanRequest);
if (restResponse.getResult().equals(RepositoryReturnCode.RETURN_CODE_00000)) {
    // 修改状态
    ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
    modifyProjectStatusDTO.setId(project.getId());
    modifyProjectStatusDTO.setProjectCode(ProjectCode.REPAYING.getCode());
    modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
    depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatusDTO);
} else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```
画面5：
```java
modifyProjectStatusDTO.setProjectCode(ProjectCode.REPAYING.getCode());
```
画面6：
```java
modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
```
画面7：
```java
modifyProjectStatusDTO.setProjectNo(project.getProjectNo());
```
画面9：
```java
depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatus);
```
画面10：
```java
RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProjectStatus);
if (modifyProjectStatus.getResult().equals(DepositReturnCode.RETURN_CODE_00000.getCode())) {
```
画面11：
```java
throw new BusinessException(TransactionErrorCode.E_150113);
```
画面13：
```java
project.setStatus(ProjectCode.REPAYING.getCode());
```
画面14：
```java
project.setStatus(ProjectCode.REPAYING.getCode());
```
画面8：
```sql
SELECT PROJECT_ID, PROJECT_NO, AMOUNT, STATUS, CREATE_DATE FROM loan;
```
画面12：
```sql
SELECT PROJECT_ID, PROJECT_NO, AMOUNT, STATUS, CREATE_DATE FROM project_1;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：流程图，从“前端APP”指向“业务系统”，“业务系统”指向“项目管理”、“还款服务”、“清算系统”，“项目管理”指向“还款服务”，“还款服务”指向“清算系统”，“清算系统”指向“业务系统”，“业务系统”指向“前端APP”，并包含状态变更和异常处理。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
