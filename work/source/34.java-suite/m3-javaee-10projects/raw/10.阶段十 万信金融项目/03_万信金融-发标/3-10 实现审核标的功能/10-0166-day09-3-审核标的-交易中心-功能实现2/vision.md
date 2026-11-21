# 画面线理解：day09-3-审核标的-交易中心-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-10 实现审核标的功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-10 实现审核标的功能\day09-3-审核标的-交易中心-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:10, 01:39, 02:45, 03:34, 04:13, 05:12, 06:35, 07:27, 08:58, 09:50, 10:30, 11:17, 12:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:02:07

1) 这一组画面整体在讲一个项目审批服务中，如何通过 Feign 调用远程服务、使用代码前缀工具类生成唯一标识、并根据返回结果更新项目状态的完整流程。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的代码，其中调用 queryWrapper 的 getOne 方法获取项目实体，并调用 convertProjectEntityToDTOList 方法转换为 DTO 列表。代码中注释说明“根据审批好的信息开转换为DTO对象”。

画面2：
要点：展示 ProjectServiceImpl 类中 convertProjectEntityToDTOList 方法的实现，将 Project 实体列表转换为 ProjectDTO 列表。代码中注释说明“如果项目为null则返回null”。

画面3：
要点：展示 ProjectServiceImpl 类中 convertProjectDTOToEntity 方法的实现，将 ProjectDTO 转换为 Project 实体。代码中注释说明“如果DTO为null则返回null”。

画面4：
要点：展示 ProjectServiceImpl 类中调用 CodeUtil.getNo 方法，用于生成唯一标识。代码中注释说明“通过feign远程调用代理服务，把标的的信息传输过去”和“根据结果修改状态”。

画面5：
要点：展示 ProjectServiceImpl 类中设置项目DTO的请求码，使用 CodeUtil.getNo 方法。代码中注释说明“通过feign远程调用代理服务，把标的的信息传输过去”和“根据结果修改状态”。

画面6：
要点：展示 ProjectServiceImpl 类中 createProject 方法的实现，调用 consumerApiAgent 的 getCurrentConsumer 方法获取当前消费者信息。代码中注释说明“根据结果修改状态”。

画面7：
要点：展示 DepositoryAgentApiAgent 接口，定义了 createProject 方法，使用 @FeignClient 和 @PostMapping 注解。代码中注释说明“通过feign远程调用代理服务，把标的的信息传输过去”。

画面8：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的实现，调用 DepositoryReturnCode 的 RETURN_CODE_0000 常量，判断返回结果是否为成功。代码中注释说明“根据结果修改状态”。

画面9：
要点：展示 ProjectServiceImpl 类中抛出 BusinessException 异常，用于处理业务异常。代码中注释说明“如果失败就抛异常”。

画面10：
要点：展示 ProjectServiceImpl 类中根据返回结果更新项目状态的代码，使用 Wrappers.lambdaUpdate 方法。代码中注释说明“如果失败就抛异常”。

画面11：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的实现，调用 Wrappers.lambdaUpdate 方法更新项目状态。代码中注释说明“如果失败就抛异常”。

画面12：
要点：展示 ProjectServiceImpl 类中 createProject 方法的实现，使用 QueryWrapper 进行条件查询。代码中注释说明“根据类型”、“禁止利率”、“借款期限”、“还款期限”等条件。

画面13：
要点：展示 ProjectServiceImpl 类中 projectsApprovalStatus 方法的实现，调用 Wrappers.lambdaUpdate 方法更新项目状态。代码中注释说明“如果失败就抛异常”。

画面14：
要点：展示 P2P平台的架构图，包含“创贷宝”、“交易中心”、“存管代理服务”、“标的的检索服务”和“银行存管系统”五个模块。图中用箭头表示各模块之间的交互流程，如“1.1.借款人发标”、“2.1.管理外审标通过”、“2.3.通过校验生成签名及摘要”等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
@Override
public String projectsApprovalStatus(Long id, String approveStatus) {
    //根据审批好的信息开转换为DTO对象
    Project project = getById(id);
    ProjectDTO projectDTO = convertProjectEntityToDTO(project);
    projectDTO.setRequestNo(CodeUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
    //通过feign远程调用代理服务，把标的的信息传输过去
    RestResponse<String> restResponse = depositoryAgentApiAgent.createProject(projectDTO);
    //根据结果修改状态
    if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
        Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
        //如果失败就抛异常
        throw new BusinessException(TransactionErrorCode.E_150119);
    }
}
```

画面2：
```java
private List<ProjectDTO> convertProjectEntityListToDTOList(java.util.List<Project> projectList) {
    if (projectList == null) {
        return null;
    }
    List<ProjectDTO> projectDTOList = new ArrayList<>();
    for (Project project : projectList) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        projectDTOList.add(projectDTO);
    }
    return projectDTOList;
}
```

画面3：
```java
private ProjectDTO convertProjectEntityToDTO(Project project) {
    if (project == null) {
        return null;
    }
    ProjectDTO projectDTO = new ProjectDTO();
    BeanUtils.copyProperties(project, projectDTO);
    return projectDTO;
}
```

画面4：
```java
//通过feign远程调用代理服务，把标的的信息传输过去
//根据结果修改状态
//如果失败就抛异常
```

画面5：
```java
projectDTO.setRequestNo(CodeUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
//通过feign远程调用代理服务，把标的的信息传输过去
//根据结果修改状态
//如果失败就抛异常
```

画面6：
```java
public ProjectDTO createProject(ProjectDTO projectDTO) {
    RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getCurrentConsumer(SecurityUtil.get(User.class));
    //根据结果修改状态
    if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
        Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
        //如果失败就抛异常
        throw new BusinessException(TransactionErrorCode.E_150119);
    }
}
```

画面7：
```java
@FeignClient(value = "depository-agent-service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/l/create-project")
    public RestResponse<String> createProject(ProjectDTO projectDTO);
}
```

画面8：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

画面9：
```java
throw new BusinessException(Transa...
```

画面10：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

画面11：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

画面12：
```java
QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
//根据类型
if (StringUtils.isNotBlank(projectDTO.getProType())) {
    queryWrapper.lambda().eq(Project::getProType, projectDTO.getProType());
}
//禁止利率（投资人）
if (null != projectDTO.getAnnualRate()) {
    queryWrapper.lambda().eq(Project::getAnnualRate, projectDTO.getAnnualRate());
}
//借款期限（投资人）
if (null != projectDTO.getPeriod()) {
    queryWrapper.lambda().eq(Project::getPeriod, projectDTO.getPeriod());
}
//还款期限（投资人）
if (null != projectDTO.getRepaymentPeriod()) {
    queryWrapper.lambda().eq(Project::getRepaymentPeriod, projectDTO.getRepaymentPeriod());
}
//标的类型
if (null != projectDTO.getProType()) {
    queryWrapper.lambda().eq(Project::getProType, projectDTO.getProType());
}
```

画面13：
```java
//根据结果修改状态
if (DepositoryReturnCode.RETURN_CODE_0000.getetCode().equals(restResponse.getResultCode())) {
    Wrappers.lambdaUpdate().set(Project::getApprovalStatus, Integer.parseInt(approveStatus));
    //如果失败就抛异常
    throw new BusinessException(TransactionErrorCode.E_150119);
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14：
PPT标题：P2P平台
架构图结构：
- “创贷宝”指向“交易中心”（1.1.借款人发标）
- “交易中心”指向“存管代理服务”（1.2.保存标的的信息，状态为：募集中，数据状态为：未发布）
- “存管代理服务”指向“标的的检索服务”（2.3
