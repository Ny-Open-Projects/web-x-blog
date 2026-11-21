# 画面线理解：06-模板打印：代码实现和总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\06-模板打印：代码实现和总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:43, 01:11, 01:28, 01:47, 02:11, 02:21, 02:31, 02:57, 03:08, 03:21, 03:43, 03:56, 04:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:08:10

1) 这一组画面整体在讲如何使用 Apache POI 库，通过读取 Excel 模板并填充数据，实现动态生成人事报表的功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个名为“2018年2月份人事报表”的 Excel 文件，其中包含员工编号、姓名、手机、最高学历、国家地区、护照号、籍贯、生日、属相、入职时间、离职类型、离职原因、离职时间等字段，第一行数据已填充。
画面2：在 Excel 文件基础上，切换到 IntelliJ IDEA 开发环境，显示了项目结构和两个终端窗口，其中一个终端显示了项目路径。
画面3：在 IntelliJ IDEA 中，展示 EmployeeController.java 文件的代码，其中定义了 Workbook 和 Sheet 对象，并通过循环设置单元格值。
画面4：继续展示代码，设置单元格样式和值，包括员工编号、姓名、手机、最高学历、国家地区、护照号等字段。
画面5：继续展示代码，设置单元格样式和值，包括籍贯、生日、属相等字段。
画面6：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面7：继续展示代码，设置单元格样式和值，包括籍贯、生日、属相等字段。
画面8：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面9：继续展示代码，设置单元格样式和值，包括籍贯、生日、属相等字段。
画面10：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面11：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面12：切换到桌面，显示了“黑马程序员”和“博学谷”的标志。
画面13：展示了一个 PPT 页面，标题为“1 模板打印”，子标题为“1.1 概述”、“1.2 模板打印的操作步骤”和“1.3 代码实现”，其中“1.3 代码实现”部分展示了 @RequestMapping 注解和 public void export 方法的代码。
画面14：继续展示 PPT 页面，内容与画面13相同，但滚动到了“1.3 代码实现”的下一部分，展示了 List<EmployeeReportResult> list = userCompanyPersonalService.findBByReport(companyId, month) 的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet();
String [] titles = "编号,姓名,手机,最高学历,国家地区,护照号,籍贯,生日,属相,入职时间,离职类型,离职原因,离职时间".split(",");
Row row = sheet.createRow(0);
int titleIndex=0;
for (String title : titles) {
    cell = row.createCell(titleIndex++);
    cell.setCellValue(title);
}
int rowIndex = 1;
Cell cell=null;
for (EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    //编号
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserId());
    //姓名
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    //手机
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    //最高学历
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    //国家地区
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    //护照号
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
}
```

画面4：
```java
//设置单元格样式
CellStyle styles[] = new CellStyle[row.getLastCellNum()];
for(int i=0;i<row.getLastCellNum();i++){
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
//设置单元格
int rowIndex = 2;
Cell cell=null;
for (EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    //编号
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserId());
    cell.setCellStyle(styles[0]);
    //姓名
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    cell.setCellStyle(styles[1]);
    //手机
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    cell.setCellStyle(styles[2]);
    //最高学历
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    cell.setCellStyle(styles[3]);
    //国家地区
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    cell.setCellStyle(styles[4]);
    //护照号
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
    cell.setCellStyle(styles[5]);
    //籍贯
    cell = row.createCell(6);
    cell.setCellValue(employeeReportResult.getNativePlace());
    cell.setCellStyle(styles[6]);
    //生日
    cell = row.createCell(7);
    cell.setCellValue(employeeReportResult.getZodiac());
    cell.setCellStyle(styles[7]);
    //属相
    cell = row.createCell(8);
    cell.setCellValue(employeeReportResult.getBirthDay());
    cell.setCellStyle(styles[8]);
    //入职时间
    cell = row.createCell(9);
    cell.setCellValue(employeeReportResult.getTimeOfEntry());
    cell.setCellStyle(styles[9]);
    //离职类型
    cell = row.createCell(10);
    cell.setCellValue(employeeReportResult.getTypeOfTurnover());
    cell.setCellStyle(styles[10]);
    //离职原因
    cell = row.createCell(11);
    cell.setCellValue(employeeReportResult.getReasonsForLeaving());
    cell.setCellStyle(styles[11]);
    //离职时间
    cell = row.createCell(12);
    cell.setCellValue(employeeReportResult.getResignationTime());
    cell.setCellStyle(styles[12]);
}
```

画面10：
```java
//3.下载
ByteArrayOutputStream os = new ByteArrayOutputStream();
wb.write(os);
new DownloadUtils().download(os, response, returnName + "人事报表.xlsx");
```

画面11：
```java
/**
 * 采用模板打印的形式完成报表生成
 * @param month
 * @return
 */
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    //1.加载模板
    Resource resource = new ClassPathResource("excel-template/hr-demo.xlsx");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.读取模板
    Workbook wb = new XSSFWorkbook(fis);
    //3.读取工作表
    Sheet sheet = wb.getSheetAt(0);
    //4.读取行
    Row row = sheet.getRow(2);
    CellStyle styles[] = new CellStyle[row.getLastCellNum()];
    for(int i=0;i<row.getLastCellNum();i++){
        Cell cell = row.getCell(i);
        styles[i] = cell.getCellStyle();
    }
    //5.设置单元格
    int rowIndex = 2;
    Cell cell=null;
    for (EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
        //编号
        cell = row.createCell(0);
        cell.setCellValue(employeeReportResult.getUserId());
        cell.setCellStyle(styles[0]);
        //姓名
        cell = row.createCell(1);
        cell.setCellValue(employeeReportResult.getUsername());
        cell.setCellStyle(styles[1]);
        //手机
        cell = row.createCell(2);
        cell.setCellValue(employeeReportResult.getMobile());
        cell.setCellStyle(styles[2]);
        //最高学历
        cell = row.createCell(3);
        cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
        cell.setCellStyle(styles[3]);
        //国家地区
        cell = row.createCell(4);
        cell.setCellValue(employeeReportResult.getNationalArea());
        cell.setCellStyle(styles[4]);
        //护照号
        cell = row.createCell(5);
        cell.setCellValue(employeeReportResult.getPassportNo());
        cell.setCellStyle(styles[5]);
        //籍贯
        cell = row.createCell(6);
        cell.setCellValue(employeeReportResult.getNativePlace());
        cell.setCellStyle(styles[6]);
        //生日
        cell = row.createCell(7);
        cell.setCellValue(employeeReportResult.getZodiac());
        cell.setCellStyle(styles[7]);
        //属相
        cell = row.createCell(8);
        cell.setCellValue(employeeReportResult.getBirthDay());
        cell.setCellStyle(styles[8]);
        //入职时间
        cell = row.createCell(9);
        cell.setCellValue(employeeReportResult.getTimeOfEntry());
        cell.setCellStyle(styles[9]);
        //离职类型
        cell = row.createCell(10);
        cell.setCellValue(employeeReportResult.getTypeOfTurnover());
        cell.setCellStyle(styles[10]);
        //离职原因
        cell = row.createCell(11);
        cell.setCellValue(employeeReportResult.getReasonsForLeaving());
        cell.setCellStyle(styles[11]);
        //离职时间
        cell = row.createCell(12);
        cell.setCellValue(employeeReportResult.getResignationTime());
        cell.setCellStyle(styles[12]);
    }
}
