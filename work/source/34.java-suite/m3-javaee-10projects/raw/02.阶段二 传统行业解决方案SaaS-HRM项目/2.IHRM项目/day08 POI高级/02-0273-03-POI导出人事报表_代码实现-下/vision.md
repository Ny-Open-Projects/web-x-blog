# 画面线理解：03-POI导出人事报表：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\03-POI导出人事报表：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:40, 02:02, 02:28, 03:13, 03:52, 04:43, 05:11, 05:41, 06:37, 07:24, 08:14, 08:53, 09:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:05:50

1) 这一组画面整体在讲如何在Java项目中编写导出员工信息到Excel表格的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个名为“2018-03人员信息.xlsx”的Excel文件，其中包含“编号”、“姓名”、“手机”、“最高学历”、“国家地区”、“护照号”、“籍贯”、“生日”、“入职时间”等列，第一行数据为“test1”、“13000000001”、“初中”、“中国大陆”、“abc”、“北京”、“2018-03-01”。
画面2：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中包含一个for循环遍历employeeReportResult列表，并调用split方法按逗号分割字符串，用于处理离职类型、离职原因、离职时间。
画面3：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中包含一个for循环遍历employeeReportResult列表，用于创建Excel表格的行和单元格。
画面4：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面5：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面6：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面7：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面8：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面9：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面10：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面11：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面12：在浏览器中，展示HRM系统的“03月人员报表”页面，包含“姓名”、“性别”、“手机”、“在职状态”、“出生日期”、“最高学历”、“籍贯地区”、“身份证号”等筛选条件，以及“导出”按钮。
画面13：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面14：展示“2018-03人员信息.xlsx”文件，其中包含“编号”、“姓名”、“手机”、“最高学历”、“国家地区”、“护照号”、“籍贯”、“生日”、“入职时间”等列，数据已填充，例如“test1”、“13000000001”、“初中”、“中国大陆”、“abc”、“北京”、“2018-03-01”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2：
```java
String[] titles = "离职类型,离职原因,离职时间".split( regex: ",");
```
画面3：
```java
int titleIndex=0;
for (String title : titles) {
    cell = row.getCell(titleIndex++);
    cell.setCellValue(title);
}
int rowIndex = 1;
for (EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    Cell cell = null;
    // 编号
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserId());
    // 姓名
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    // 手机
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    // 最高学历
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    // 国家地区
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    // 护照号
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
    // 籍贯
    cell = row.createCell(6);
    cell.setCellValue(employeeReportResult.getNativePlace());
    // 生日
    cell = row.createCell(7);
    cell.setCellValue(employeeReportResult.getBirthDay());
    // 血型
    cell = row.createCell(8);
    cell.setCellValue(employeeReportResult.getZodiac());
    // 入职时间
    cell = row.createCell(9);
    cell.setCellValue(employeeReportResult.getTimeOfEntry());
    // 离职类型
    cell = row.createCell(10);
    cell.setCellValue(employeeReportResult.getTypeOfTurnover());
    // 离职原因
    cell = row.createCell(11);
    cell.setCellValue(employeeReportResult.getReasonsForLeaving());
    // 离职时间
    cell = row.createCell(12);
    cell.setCellValue(employeeReportResult.getResignationTime());
}
```
画面4：
```java
cell.setCellValue(employeeReportResult.getUserId());
```
画面5：
```java
cell.setCellValue(employeeReportResult.getUserId());
```
画面6：
```java
cell.setCellValue(employeeReportResult.getNationalArea());
```
画面7：
```java
cell.setCellValue(employeeReportResult.getBirthDay());
```
画面8：
```java
cell.setCellValue(employeeReportResult.getNativePlace());
```
画面9：
```java
cell.setCellValue(employeeReportResult.getBirthDay());
```
画面10：
```java
cell.setCellValue(employeeReportResult.getResignationTime());
```
画面11：
```java
cell.setCellValue(employeeReportResult.getResignationTime());
```
画面12：
```java
// 导出
```
画面13：
```java
cell.setCellValue(employeeReportResult.getNationalArea());
```
画面14：
```java
// 数据已填充
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
