# 画面线理解：01-课程介绍与POI导出人事报表：需求说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\01-课程介绍与POI导出人事报表：需求说明_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:44, 03:42, 04:41, 04:55, 05:09, 06:05, 06:56, 07:33, 08:05, 08:39, 09:36, 10:38, 13:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:04:25

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何使用POI技术实现人事报表的导出功能，包括需求分析、代码实现和数据库查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT页面，标题为“5 POI报表导出”，子标题“5.1 需求分析”，内容为“完成当月人事报表的导出：包含当月入职员工信息，离职员工信息”，并展示一个“导出”按钮。
画面2：展示人事报表导出的前端界面，标题为“03月人事报表”，包含“导出”按钮。
画面3：展示PPT页面，标题为“5.1 需求分析”，内容与画面1相同。
画面4：展示PPT页面，标题为“5.2 人事报表导出”，子标题“5.2.1 步骤分析”，列出步骤：“构造Excel表格数据”、“创建工作簿”、“创建sheet”、“创建行对象”、“创建单元格对象”、“填充数据，设置样式”。
画面5：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_common_model/src/main/java/com/hrm/common/domain/response/ProfileResult.java`，代码内容为：
```java
@poran
public ProfileResult(User user, List<Permission> list) {
    this.mobile = user.getMobile();
    this.company = user.getCompanyName();
    this.companyId = user.getCompanyId();
    this.userId = user.getId();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    for (Permission perm : list) {
        if (perm.getType() == 1) {
            menus.add(code);
        } else if (perm.getType() == 2) {
            points.add(code);
        } else {
            apis.add(code);
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}
```
画面6：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_employee/src/main/java/hrm/employee/controller/EmployeeController.java`，代码内容为：
```java
@RequestMapping(value = "/{id}/positive", method = RequestMethod.GET)
public Employee findPositive(@PathVariable(name = "id") String uid) throws Exception {
    EmployeePositive positive = positiveService.findById(uid);
    if (positive == null) {
        return new Result(ResultCode.SUCCESS, positive);
    }
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer type) throws Exception {
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.PUT)
public Result saveArchives(@PathVariable(name = "month") String month) throws Exception {
    return new Result(ResultCode.SUCCESS);
}
```
画面7：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_employee/src/main/java/hrm/employee/controller/EmployeeController.java`，代码内容为：
```java
@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer page, @RequestParam(name = "page") Integer page) throws Exception {
    Map<String, Object> map = new HashMap<>();
    map.put("year", year);
    map.put("companyId", companyId);
    map.put("company", company);
    map.put("month", month);
    PageResult<EmployeeArchive> pr = new PageResult<EmployeeArchive>(searchPage.getTotalElements(), searchPage.getContent());
    return new Result(ResultCode.SUCCESS, pr);
}
```
画面8：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_employee/src/main/java/hrm/employee/controller/EmployeeController.java`，代码内容为：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) {
    //1.获取数据
    //2.将数据写入Excel
    //3.完成下载
}
```
画面9：展示课程PPT页面，标题为“第7章 POI报表的入门”，子标题“1 员工管理”，内容为“1.1 需求分析”和“1.2 数据库表概述”。
画面10：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据。
画面11：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，但未显示具体数据。
画面12：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，其中`time_of_entry`字段值为“2018-03-01”。
画面13：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，其中`time_of_entry`字段值为“2018-03-01”。
画面14：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，其中`time_of_entry`字段值为“2018-03-01”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面5：
```java
@poran
public ProfileResult(User user, List<Permission> list) {
    this.mobile = user.getMobile();
    this.company = user.getCompanyName();
    this.companyId = user.getCompanyId();
    this.userId = user.getId();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    for (Permission perm : list) {
        if (perm.getType() == 1) {
            menus.add(code);
        } else if (perm.getType() == 2) {
            points.add(code);
        } else {
            apis.add(code);
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}
```
画面6：
```java
@RequestMapping(value = "/{id}/positive", method = RequestMethod.GET)
public Employee findPositive(@PathVariable(name = "id") String uid) throws Exception {
    EmployeePositive positive = positiveService.findById(uid);
    if (positive == null) {
        return new Result(ResultCode.SUCCESS, positive);
    }
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer type) throws Exception {
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.PUT)
public Result saveArchives(@PathVariable(name = "month") String month) throws Exception {
    return new Result(ResultCode.SUCCESS);
}
```
画面7：
```java
@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer page, @RequestParam(name = "page") Integer page) throws Exception {
    Map<String, Object> map = new HashMap<>();
    map.put("year", year);
    map.put("companyId", companyId);
    map.put("company", company);
    map.put("month", month);
    PageResult<EmployeeArchive> pr = new PageResult<EmployeeArchive>(searchPage.getTotalElements(), searchPage.getContent());
    return new Result(ResultCode.SUCCESS, pr);
}
```
画面8：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) {
    //1.获取数据
    //2.将数据写入Excel
    //3.完成下载
}
```
画面10：
```sql
SELECT * FROM em_user_company_personal
```
画面12：
```sql
SELECT * FROM em_user_company_personal WHERE resignation_time LIKE '2018-03%'
```
画面14：
```sql
SELECT * FROM em_user_company_personal WHERE resignation_time LIKE '2018-03%'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5 POI报表导出”，子标题“5.1 需求分析”，内容为“完成当月人事报表的导出：包含当月入职员工信息，离职员工信息”。
画面3：PPT标题为“5.1 需求分析”，内容与画面1相同。
画面4：PPT标题为“5.2 人事报表导出”，子标题“5.2.1 步骤分析”，列出步骤：“构造Excel表格数据”、“创建工作簿”、“创建sheet”、“创建行对象”、“创建单元格对象”、“填充数据，设置样式”。
画面9：PPT标题为“第7章 POI报表的入门”，子标题“1 员工管理”，内容为“1.1 需求分析”和“1.2 数据库表概述”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）
