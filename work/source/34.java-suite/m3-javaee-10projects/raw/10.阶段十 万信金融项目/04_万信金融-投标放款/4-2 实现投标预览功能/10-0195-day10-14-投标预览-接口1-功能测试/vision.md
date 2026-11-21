# 画面线理解：day10-14-投标预览-接口1-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-14-投标预览-接口1-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 02:02, 03:14, 04:21, 05:30, 05:59, 06:53, 07:44, 08:46, 09:39, 10:14, 10:32, 11:12, 12:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:25:41

1) 这一组画面整体在讲什么（一句话）：
演示交易中心服务如何通过查询项目ID列表，获取项目详情并计算剩余金额，最终返回给前端，涉及数据库操作、代码实现和API测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示交易中心服务的接口调用流程图，包含“调用端/APP”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”等模块，以及接口编号如“1.1 获取标的的信息”、“1.5 保存平台端投标信息”、“2.1 保存投标信息”等。
画面2：展示文档内容，标题为“2.2.2.2 功能测试”，说明由于未实现投标功能，需自己造测试数据，并指出分库分表策略：分库策略为“发标人ID % 2”，分表策略为“标的ID % 2”。下方是“2.2.3 交易中心查询投标记录接口(接口②)”和“2.2.3.1 功能实现”，代码片段为：
```java
/**
 * 根据标的id查询投标记录
 * @param id
 * @return
 */
```
画面3：与画面2内容相同，仅鼠标位置不同。
画面4：在SQLyog中展示数据库`p2p_transaction`的`tender`表，查询到两条记录，其中一条`PROJECT_ID`为`213948364380359657`。
画面5：在Swagger UI中展示“交易中心服务”的API文档，显示“transaction Transaction Controller”。
画面6：在Swagger UI中展示“GET /projects/{ids} 查询多个标的”接口，参数为`ids`，并点击“Execute”按钮。
画面7：在SQLyog中展示`tender`表，查询到两条记录，其中一条`PROJECT_ID`为`213948364380359657`。
画面8：在SQLyog中展示`tender`表，查询结果为空。
画面9：在IntelliJ IDEA中展示`ProjectServiceImpl.java`文件，代码片段为：
```java
queryWrapper.lambda().in(Project::getId, list) // ... where id in (1,2,3,4,5)
List<Project> projects = list(queryWrapper);
List<ProjectDTO> dtos = new ArrayList<>();
for (Project project : projects) {
    ProjectDTO projectDTO = DTOconvertProjectToDTO(project);
    // 2 转换为DTO对象
    projectDTO.setTenderCount(tenderMapper.selectCount(Wappers));
    dtos.add(projectDTO);
}
return dtos;
```
画面10：在IntelliJ IDEA中展示`ProjectServiceImpl.java`文件，代码片段为：
```java
projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
```
画面11：在IntelliJ IDEA中展示`ProjectDTO.java`文件，代码片段为：
```java
/**
 * 聚合金额
 */
private BigDecimal amount;
/**
 * 标的状态
 */
private String projectStatus;
/**
 * 创建时间
 */
```
画面12：在IntelliJ IDEA中展示`ProjectServiceImpl.java`文件，代码片段为：
```java
projectDTO.setTenderCount(tenderMapper.selectCount(Wappers));
```
画面13：在IntelliJ IDEA中展示`ProjectServiceImpl.java`文件，代码片段为：
```java
WHERE_PROJECT_ID = ?) , containStatus=false, firstSelectItemStartIndex=7, selectClientStartIndex=18, groupByLastIndex=0, items={AggregationSelectLeadType=COUNT, $project_id = ? : ... [12345678901234567890]
```
画面14：在Swagger UI中展示“GET /projects/{ids} 查询多个标的”接口的响应结果，响应体为：
```json
{
  "code": 0,
  "msg": "",
  "result": [
    {
      "id": "213948364380359657",
      "projectName": "测试项目",
      "projectStatus": "27",
      "projectAmount": "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
