# 画面线理解：05-模板打印：代码实现-加载模板抽取公共样式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\05-模板打印：代码实现-加载模板抽取公共样式_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:27, 01:01, 01:26, 03:22, 04:23, 05:09, 05:43, 06:33, 06:54, 07:26, 07:49, 08:13, 09:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:07:20

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过读取 Excel 模板文件并填充数据，实现员工人事报表的导出功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“1.2 模板打印的操作步骤”和“1.3 代码实现”部分，列出导出操作的 8 个步骤，并展示代码中 @RequestMapping 注解和初步的 Java 代码。
画面 2: 在 IntelliJ IDEA 中展示 EmployeeController.java 文件，代码正在填充单元格，设置单元格值，如“编号”、“姓名”、“手机”等。
画面 3: 展示项目目录结构，选中“excel-template”文件夹，弹出“新建目录”对话框，准备创建新目录。
画面 4: 展示“复制文件”对话框，将“hr-demo.xlsx”复制到“excel-template”目录下。
画面 5: 展示项目目录结构，选中“excel-template”文件夹，文件列表中显示“hr-demo.xlsx”。
画面 6: 展示“重命名”对话框，将文件“hr-demo.xlsx”重命名为“excel-template”。
画面 7: 展示项目目录结构，选中“excel-template”文件夹，文件列表中显示“hr-demo.xlsx”，代码中正在创建 Workbook 对象。
画面 8: 展示代码中创建 Sheet 对象，使用 wb.getSheetAt(0) 获取第一个工作表。
画面 9: 展示 Excel 文件“hr-demo.xlsx”，内容为“2018年2月份人事报表”，包含“编号”、“姓名”、“手机”等列。
画面 10: 展示代码中调用 sheet.getCell() 方法，弹出“Quick Documentation View”显示方法签名。
画面 11: 展示代码中创建 CellStyle 对象，准备设置单元格样式。
画面 12: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 13: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 14: 展示代码中设置单元格样式，使用 CellStyle 对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId,month);
}
```

画面 2:
```java
cell = row.createCell(0);
cell.setCellValue(employeeReportResult.getUserId());
cell = row.createCell(1);
cell.setCellValue(employeeReportResult.getUsername());
cell = row.createCell(2);
cell.setCellValue(employeeReportResult.getMobile());
cell = row.createCell(3);
cell.setCellValue(employeeReportResult.getHighestDegreeEducation());
cell = row.createCell(4);
cell.setCellValue(employeeReportResult.getNationalArea());
cell = row.createCell(5);
cell.setCellValue(employeeReportResult.getPassportNo());
cell = row.createCell(6);
cell.setCellValue(employeeReportResult.getNativePlace());
cell = row.createCell(7);
cell.setCellValue(employeeReportResult.getBirthDay());
cell = row.createCell(8);
cell.setCellValue(employeeReportResult.getZodiac());
cell = row.createCell(9);
cell.setCellValue(employeeReportResult.getResignationTime());
```

画面 3:
```java
//1.获取未读数据
List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId,month);
Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet();
String [] titles = {"编号","姓名","手机","最高学历","国家地区","护照号","籍贯","生日","属相","入职时间","离职类型","离职原因","离职时间"};
```

画面 4:
```java
Copy file C:\Users\ThinkPad\Desktop\hrm\day\hr demo.xlsx
New name: hr-demo.xlsx
To directory: C:\Users\ThinkPad\workspace\hrm_parent\hrm_employee\src\main\resources\excel-template
```

画面 5:
```java
//参数：年月-月（2018-02）
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId,month);
}
```

画面 6:
```java
Rename file 'hr-demo.xlsx' and its usages to:
hr-demo.xlsx
```

画面 7:
```java
Resource resource = new ClassPathResource("excel-template/hr-demo.xlsx");
FileInputStream fis = new FileInputStream(resource.getFile());
Workbook wb = new XSSFWorkbook(fis);
```

画面 8:
```java
Sheet sheet = wb.getSheetAt(0);
```

画面 9:
```java
//2018年2月份人事报表
编号	姓名	手机	最高学历	国家地区	护照号	籍贯	生日	属相	入职时间	离职类型	离职原因	离职时间
1	张三	13800138000	本科	中国大陆	4	北京	1997/1/1	属相	2018/1/1	主动	无	2018/1/1
```

画面 10:
```java
sheet.getCell()
```

画面 11:
```java
CellStyle styles [] = new CellStyle[];
```

画面 12:
```java
for(int i=0;i<row.getLastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

画面 13:
```java
for(int i=0;i<row.getLastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

画面 14:
```java
for(int i=0;i<row.getLastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.2 模板打印的操作步骤”和“1.3 代码实现”。
画面 9: Excel 文件标题为“2018年2月份人事报表”，包含“编号”、“姓名”、“手机”等列。
画面 10: 弹出“Quick Documentation View”显示方法签名。
画面 11: 展示代码中创建 CellStyle 对象。
画面 12: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 13: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 14: 展示代码中设置单元格样式，使用 CellStyle 对象。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
