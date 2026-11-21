# 画面线理解：24-总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\24-总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:20, 00:49, 00:55, 01:09, 01:15, 01:37, 02:00, 02:15, 02:33, 03:10, 03:30, 03:58, 04:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:18:07

1) 这一组画面整体在讲什么（一句话）：
演示 iHRM 人事管理系统中员工请假审批流程的前端操作与后端数据库及代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 点击左侧菜单“审批”进入审批主页面，显示工作日历和快捷入口。
画面 2: 点击“审批”菜单后，页面加载中，显示版权信息。
画面 3: 点击“申请请假”按钮，进入请假申请详情页，显示申请人信息和审批记录。
画面 4: 在审批列表页，切换到“待审批”标签，显示待处理的请假申请列表。
画面 5: 打开 SQLyog，查询 `act_ru_task` 表，查看流程实例和任务数据。
画面 6: 在请假申请详情页，查看具体请假信息，包括申请类型、时间、时长等。
画面 7: 点击“审批”菜单，页面跳转至审批主页面。
画面 8: 打开浏览器开发者工具，查看网络请求，显示 `app.js` 文件加载。
画面 9: 查看网络请求返回的 JSON 数据，包含审批操作的详细信息。
画面 10: 在 SQLyog 中，查询 `act_ru_task` 表，查看任务分配情况。
画面 11: 展示 PPT 页面，标题为“1.3 加班流程分析”，并附有流程图：开始 → 提交申请 → 部门审批 → 人事审批 → 结束。
画面 12: 在 SQLyog 中，查询 `act_re_procdef` 表，查看流程定义信息。
画面 13: 展示 PPT 页面，标题为“3.1 审批列表查询”，并显示“配置controller”部分的 Java 代码。
画面 14: 展示 PPT 页面，标题为“3.1 审批列表查询”，并显示“配置service”部分的 Java 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5 SQL:
```sql
SELECT manager_username, manager_id FROM co_department WHERE id = 2
```

画面 5 SQLyog 查询结果:
```
process_id         process_name     process_definition_id   process_state   user_id   username   handle_user_name
1175968095611101184 请假           2                       (NULL)          1066370498631486336  zbz        zbz
1175968095611101184 请假           4                       (NULL)          1066370498631486336  zbz        zbz
```

画面 10 SQLyog 查询结果:
```
name                  key     id
PROCESS LEAVE APPLY USERS   leaveApply   1175968095611101184
PROCESS LEAVE CUP USERS     leaveCup     1175968095611101184
PROCESS LEAVE OVERTIME USERS  leaveOverTime  1175968095611101184
```

画面 13 Java 代码:
```java
@RequestMapping("/process/instances")
public Result getProcessInstances(@RequestBody ProcInstance procInstance, int page, int size) {
    //1.调用service完成查询
    Page pageuser = auditService.getProcessInstances(procInstance, page, size);
    //2.构造返回结果
    PageResult pageResult = new PageResult(pageuser.getTotalElements(), pageuser.getContent());
    return new Result(Resultcode.SUCCESS, pageResult);
}
```

画面 14 Java 代码:
```java
//查询所有已发起的流程
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11 PPT 标题：“1.3 加班流程分析”
流程图结构：
- 开始 → 提交申请 → 部门审批 → 人事审批 → 结束

画面 13 PPT 标题：“3.1 审批列表查询”
子标题：“（1）配置controller”

画面 14 PPT 标题：“3.1 审批列表查询”
子标题：“（2）配置service”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
