# day12-6-满标放款-接口1-功能实现6

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-6-满标放款-接口1-功能实现6_【海量资源尽在 666java.com】.mp4
- 时长 1分54秒（音频 115s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好咱刚才呢分成四个阶段把业务层的代码呢就全部搞定了这块搞完之后呢咱接下来是不是该把Controller里边代码补充完善一下对不对咱找一下这个Controller这块代码就比较简单了这儿是不是调用业务层的方法就OK了啊那就是project Service点哪个方法对叫learns of prosdators对不对这里边呢给他扔进去三个参数二百第一个就是id
[00:31] 第二个就是什么状态approval status第三个参数就是什么平台的佣金是不是那调完了之后他返回的是不是我们一个什么字符串我们就可以先接收一下result这个字符串我们需要封装到什么rest response然后再进行返回rest response调用他的什么特色的方法
[01:01] 然后呢把这个result放进去就ok 了啊这是咱们这个什么呀Controller 这个代码比较简单咱补充玩看一下那Controller 代码搞定完之后咱接下来是不是按以前的这个套是不是该进行功能测试了是不是那这咱能进行测试吗我问一下大家能进行测试吗不能啊那接口一咱这个代码虽然基本上不见完了但是没法测试啊为啥呢因为你看这里边接口二接口三接口四这里边功能是不是还没没开发呢对不对
[01:32] 咱接口一里边呢只是把调用或者访问他们的代码给写了一下啊但是呢借口二借口三借口四的功能还没开发所以说呢暂时呢咱先不进行测试啊等着后续都开发完了咱们一块进行测试就行了这是截止到目前吧咱相当于是把接口一啊整个这块功能给开发完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个项目审批状态变更的业务流程，包括控制器层的接口定义、服务层的业务逻辑实现，以及对应的时序图。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `ProjectServiceImpl.java` 中 `loansApproveStatus` 方法的实现，包含三阶段逻辑：生成放款明细、确认放款、修改项目状态。代码中包含 `QueryWrapper` 查询条件、`repositoryAgentAgent.confirmLoan` 调用、`modifyProjectStatusDTO` 状态修改。
画面2：继续展示 `ProjectServiceImpl.java` 中 `loansApproveStatus` 方法，聚焦于“修改状态”部分，代码中包含 `ModifyProjectStatusDTO` 的构造和 `setProjectStatus` 设置状态。
画面3：展示 `ProjectServiceImpl.java` 中 `loansApproveStatus` 方法的完整代码，包含“生成放款明细”、“确认放款”、“修改状态”三个阶段的完整逻辑。
画面4：展示 `TransactionController.java` 中 `@PostMapping` 注解的接口定义，包含 `@ApiImplicitParams` 注解定义的三个参数：`id`、`approveStatus`、`commission`。
画面5：展示 `TransactionController.java` 中 `loansApprovalStatus` 方法的实现，调用 `projectService.loansApprovalStatus(id)`。
画面6：展示 `TransactionController.java` 中 `loansApprovalStatus` 方法，参数 `approveStatus` 从 `@PathVariable` 改为 `@RequestParam`。
画面7：展示 `TransactionController.java` 中 `loansApprovalStatus` 方法，参数 `commission` 从 `@RequestParam` 改为 `@PathVariable`。
画面8：展示 `TransactionController.java` 中 `loansApprovalStatus` 方法，最终调用 `projectService.loansApprovalStatus(id, approveStatus, commission)`。
画面9：展示 `TransactionController.java` 中 `loansApprovalStatus` 方法，返回 `RestResponse.success(result)`。
画面10：展示 `TransactionController.java` 中 `loansApprovalStatus` 方法，返回 `RestResponse.success(id)`。
画面11：展示一个时序图，描述“项目审批状态变更”流程，涉及“调用方”、“交易中心”、“存管系统”、“清算系统”四个角色。
画面12：展示时序图，描述“项目审批状态变更”流程，涉及“调用方”、“交易中心”、“存管系统”、“清算系统”四个角色。
画面13：展示时序图，描述“项目审批状态变更”流程，涉及“调用方”、“交易中心”、“存管系统”、“清算系统”四个角色。
画面14：展示时序图，描述“项目审批状态变更”流程，涉及“调用方”、“交易中心”、“存管系统”、“清算系统”四个角色。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public String loansApproveStatus(Long id, String approveStatus, String commission) {
    //第一阶段：1. 生成放款明细
    //2. 标的信息
    Project project = projectMapper.selectById(id);
    //3. 报价信息
    QueryWrapper<Tender> queryWrapper = new QueryWrapper<>();
    queryWrapper.lambda().eq(Project::getId, id);
    List<Tender> tenderList = tenderMapper.selectList(queryWrapper);
    //生成放款明细
    LoanRequest loanRequest = generateLoanRequest(project, tenderList, commission);
    //第二阶段：2. 确认放款
    RestResponse<String> restResponse = depositoryAgentAgent.confirmLoan(loanRequest);
    if(restResponse.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
        //第三阶段：3. 修改状态
        ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
        modifyProjectStatusDTO.setProjectId(project.getId());
        modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode());
        modifyProjectStatusDTO.setProjectNo(project.getProjectNo());
        //存管代理返回异常请求
        RestResponse<String> restResponse1 = depositoryAgentAgent.modifyProjectStatus(modifyProjectStatusDTO);
        if(restResponse1.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
            //更新放款状态
            project.setProjectStatus(ProjectCode.REPAYING.getCode());
            updateById(project);
            return "success";
        }
    }
    return "fail";
}
```

画面2：
```java
//存管代理返回异常请求
RestResponse<String> restResponse1 = depositoryAgentAgent.modifyProjectStatus(modifyProjectStatusDTO);
if(restResponse1.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
    //更新放款状态
    project.setProjectStatus(ProjectCode.REPAYING.getCode());
    updateById(project);
    return "success";
}
```

画面3：
```java
@Override
public String loansApproveStatus(Long id, String approveStatus, String commission) {
    //第一阶段：1. 生成放款明细
    //2. 标的信息
    Project project = projectMapper.selectById(id);
    //3. 报价信息
    QueryWrapper<Tender> queryWrapper = new QueryWrapper<>();
    queryWrapper.lambda().eq(Project::getId, id);
    List<Tender> tenderList = tenderMapper.selectList(queryWrapper);
    //生成放款明细
    LoanRequest loanRequest = generateLoanRequest(project, tenderList, commission);
    //第二阶段：2. 确认放款
    RestResponse<String> restResponse = depositoryAgentAgent.confirmLoan(loanRequest);
    if(restResponse.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
        //第三阶段：3. 修改状态
        ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
        modifyProjectStatusDTO.setProjectId(project.getId());
        modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode());
        modifyProjectStatusDTO.setProjectNo(project.getProjectNo());
        //存管代理返回异常请求
        RestResponse<String> restResponse1 = depositoryAgentAgent.modifyProjectStatus(modifyProjectStatusDTO);
        if(restResponse1.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
            //更新放款状态
            project.setProjectStatus(ProjectCode.REPAYING.getCode());
            updateById(project);
            return "success";
        }
    }
    return "fail";
}
```

画面4：
```java
@ApiOperation("审核标的放款")
@ApiImplicitParams({
    @ApiImplicitParam(name = "id", value = "标的.id", required = true, dataType = "long", paramType = "path"),
    @ApiImplicitParam(name = "approveStatus", value = "标的的状态", required = true, dataType = "string", paramType = "path"),
    @ApiImplicitParam(name = "commission", value = "平台佣金", required = true, dataType = "string", paramType = "query")
})
@PostMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @PathVariable("approveStatus") String approveStatus) {
    projectService.loansApprovalStatus(id);
}
```

画面5：
```java
@PostMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @PathVariable("approveStatus") String approveStatus) {
    projectService.loansApprovalStatus(id);
}
```

画面6：
```java
@PostMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @RequestParam("approveStatus") String approveStatus) {
    projectService.loansApprovalStatus(id, approveStatus);
}
```

画面7：
```java
@PostMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @RequestParam("approveStatus") String approveStatus, @RequestParam("commission") String commission) {
    projectService.loansApprovalStatus(id, approveStatus, commission);
}
```

画面8：
```java
@PostMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @RequestParam("approveStatus") String approveStatus, @RequestParam("commission") String commission) {
    projectService.loansApprovalStatus(id, approveStatus, commission);
}
```

画面9：
```java
public RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission) {
    String result = projectService.loansApprovalStatus(id, approveStatus, commission);
    return RestResponse.success(result);
}
```

画面10：
```java
public RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission) {
    String result = projectService.loansApprovalStatus(id, approveStatus, commission);
    return RestResponse.success(id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面11-14：展示一个时序图，描述“项目审批状态变更”流程，涉及“调用方”、“交易中心”、“存

