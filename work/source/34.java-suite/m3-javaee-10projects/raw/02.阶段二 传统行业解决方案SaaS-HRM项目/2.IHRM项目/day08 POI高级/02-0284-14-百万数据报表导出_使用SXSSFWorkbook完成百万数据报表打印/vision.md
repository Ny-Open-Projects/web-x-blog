# 画面线理解：14-百万数据报表导出：使用SXSSFWorkbook完成百万数据报表打印

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\14-百万数据报表导出：使用SXSSFWorkbook完成百万数据报表打印_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:32, 00:57, 01:39, 02:37, 03:17, 03:41, 03:58, 04:27, 04:40, 04:58, 05:14, 06:21, 07:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:14:00

1) 这一组画面整体在讲如何使用 Apache POI 的 SXSSFWorkbook 类来解决大容量 Excel 报表导出时的内存溢出问题，并通过代码实现和性能监控演示其效果。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档，标题为“4.2 解决方案”，子标题“4.2.1 思路分析”和“4.2.2 原理分析”，内容说明基于 SXSSFWorkbook 导出 Excel 报表，通过设置内存中对象数量上限（默认100）来避免内存溢出。
画面2：展示 IntelliJ IDEA 中 EmployeeController.java 的代码，导出方法中使用了 ExcelExportUtil 工具类和 SXSSFWorkbook 创建工作簿。
画面3：展示代码中创建 SXSSFWorkbook 对象并设置标题行。
画面4：展示代码中创建 Sheet 并设置标题行，使用了 String[] titles 数组。
画面5：展示代码中遍历数据列表，为每一行设置单元格值。
画面6：展示代码中创建 SXSSFWorkbook 对象并设置 rowAccessWindowSize 为 100，用于控制内存中对象数量。
画面7：展示 HRM 系统的 Web 界面，显示工作日历和快速导航。
画面8：展示 VisualVM 中的性能监控界面，显示 CPU 使用率、内存使用情况等。
画面9：展示 VisualVM 中的性能监控界面，显示 CPU 使用率、内存使用情况等。
画面10：展示代码中创建 SXSSFWorkbook 对象并设置 rowAccessWindowSize 为 100。
画面11：展示代码中设置单元格值，包括手机号、最高学历、国家地区、护照号、生日、入职时间、离职原因等字段。
画面12：展示 VisualVM 中的 JVM 信息，显示 Java 版本、JVM 参数等。
画面13：展示 VisualVM 中的性能监控界面，显示 CPU 使用率、内存使用情况等。
画面14：展示导出的 Excel 文件内容，包含员工编号、姓名、部门、入职时间等数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.2 解决方案
4.2.1 思路分析
基于SXSSFWorkbook导出Excel报表，是通过将所有单元格对象保存到内存中，当所有的Excel单元格全部创建完成之后一次性写入Excel文件导出。当存在内存溢出时，需要表格的不断创建，内存中对象越来越多，直至内存溢出。Apache PoI提供了SXSSFWorkbook对象，专门用于处理大数据量Excel报表导出。
4.2.2 原理分析
在实现SXSSFWorkbook这个指定对象，可以指定在内存中所产生的POI对象的数量（默认100），一旦内存中的对象的个数达到这个指定值时，就可以将内存中的这些对象的内容写入磁盘中（XML的文件格式），就可以将这些对象从内存中销毁，以后只要达到这个值，就会以类似的处理方式处理，直至Excel导出完成。
4.3 代码实现
在原有代码的基础上替换之前的XSSFWorkbook，使用SXSSFWorkbook完成创建过程即可
```
画面2：
```
//...
new DownloadUtils().downloadFile(os, response, month + "人事报表.xlsx");
//...
/**
 * 导出报表
 * @param company_id
 * @param month
 * @return
 */
@GetMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId, month);
    //...
    // 通过工具类下载
    new ExcelExportUtil(EmployeeReportResult.class, 2, 2);
    export(response, list, month + "人事报表.xlsx");
    //...
}
```
画面3：
```
//...
@GetMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId, month);
    //...
    // 1.创建Excel
    Workbook wb = new XSSFWorkbook();
    //...
    String[] titles = "编号,姓名,手机,最高学历,国家地区,护照号,籍贯,生日,属相,入职时间,离职类型,离职原因,离职时间".split(",");
    //...
    int titleIndex = 0;
    for (String title : titles) {
        Cell cell = row.createCell(titleIndex++);
        cell.setCellValue(title);
    }
    //...
    int rowIndex = 1;
    for (EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
        cell = row.createCell(0);
        cell.setCellValue(employeeReportResult.getUserId());
        cell = row.createCell(1);
        cell.setCellValue(employeeReportResult.getUsername());
        cell = row.createCell(2);
        cell.setCellValue(employeeReportResult.getMobile());
        cell = row.createCell(3);
        cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
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
        cell.setCellValue(employeeReportResult.getTimeOfEntry());
        cell = row.createCell(10);
        cell.setCellValue(employeeReportResult.getTypoOfTurnover());
        cell = row.createCell(11);
        cell.setCellValue(employeeReportResult.getReasonsForLeaving());
        cell = row.createCell(12);
        cell.setCellValue(employeeReportResult.getTimeOfLeaving());
    }
}
```
画面4：
```
//...
@GetMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId, month);
    //...
    // 1.创建Excel
    Workbook wb = new XSSFWorkbook();
    //...
    String[] titles = "编号,姓名,手机,最高学历,国家地区,护照号,籍贯,生日,属相,入职时间,离职类型,离职原因,离职时间".split(",");
    //...
    int titleIndex = 0;
    for (String title : titles) {
        Cell cell = row.createCell(titleIndex++);
        cell.setCellValue(title);
    }
    //...
    int rowIndex = 1;
    for (EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
        cell = row.createCell(0);
        cell.setCellValue(employeeReportResult.getUserId());
        cell = row.createCell(1);
        cell.setCellValue(employeeReportResult.getUsername());
        cell = row.createCell(2);
        cell.setCellValue(employeeReportResult.getMobile());
        cell = row.createCell(3);
        cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
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
        cell.setCellValue(employeeReportResult.getTimeOfEntry());
        cell = row.createCell(10);
        cell.setCellValue(employeeReportResult.getTypoOfTurnover());
        cell = row.createCell(11);
        cell.setCellValue(employeeReportResult.getReasonsForLeaving());
        cell = row.createCell(12);
        cell.setCellValue(employeeReportResult.getTimeOfLeaving());
    }
}
```
画面5：
```
//...
@GetMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId, month);
    //...
    // 1.创建Excel
    Workbook wb = new XSSFWorkbook();
    //...
    String[] titles = "编号,姓名,手机,最高学历,国家地区,护照号,籍贯,生日,属相,入职时间,离职类型,离职原因,离职时间".split(",");
    //...
    int titleIndex = 0;
    for (String title : titles) {
        Cell cell = row.createCell(titleIndex++);
        cell.setCellValue(title);
    }
    //...
    int rowIndex = 1;
    for (EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
        cell = row.createCell(0);
        cell.setCellValue(employeeReportResult.getUserId());
        cell = row.createCell(1);
        cell.setCellValue(employeeReportResult.getUsername());
        cell = row.createCell(2);
        cell.setCellValue(employeeReportResult.getMobile());
        cell = row.createCell(3);
        cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
        cell = row.createCell(4);
        cell.setCellValue(employeeReportResult.getNationalArea());
        cell = row.createCell(5);
        cell.setCellValue(employeeReportResult.getPassportNo());
        cell = row.createCell(6);
        cell.setCellValue(employeeReportResult.getNativePlace());
        cell = row.createCell(7);
        cell.setCellValue(employeeReportResult.getBirthDay());
        cell = row.createCell(8);
        cell.setCellValue(employeeReportResult
