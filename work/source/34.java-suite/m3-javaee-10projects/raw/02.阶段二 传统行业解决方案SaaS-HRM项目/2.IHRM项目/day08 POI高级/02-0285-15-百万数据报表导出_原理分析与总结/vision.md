# 画面线理解：15-百万数据报表导出：原理分析与总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\15-百万数据报表导出：原理分析与总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:38, 00:59, 01:34, 01:54, 02:54, 03:21, 04:00, 04:29, 05:06, 05:29, 05:52, 06:30, 07:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:14:50

1) 这一组画面整体在讲如何使用 Apache POI 的 SXSSFWorkbook 类来高效导出百万级数据到 Excel，通过将对象写入临时 XML 文件以减少内存占用。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 EmployeeController.java 中导出 Excel 的 Java 代码，其中定义了标题数组并循环设置单元格值。
画面2: 展示了 Windows 文件资源管理器中 Temp 文件夹的目录结构。
画面3: 在文件资源管理器中，弹出并打开了一个命令行窗口，显示了正在运行的 Redis 服务。
画面4: 在文件资源管理器中，选中了名为 "pol-ssxf-sheet7039257060504777641.xml" 的 XML 文件。
画面5: 使用 Notepad++ 打开并显示了该 XML 文件的内容，包含大量 <c t="inlineStr"><is><v>testXX</v></is></c> 标签。
画面6: 展示了一个流程图，描述了主线程创建报表对象，然后将 row、cell、style、font 对象写入磁盘文件，最终生成 Excel 文件。
画面7: 在流程图中，右侧新增了一个“主线程”节点，表示另一个处理路径。
画面8: 在右侧流程图中，新增了“内存”框，表示在内存中创建 row、cell、style 对象。
画面9: 在右侧流程图中，新增了“xml磁盘文件”框，并添加了从“内存”指向“xml磁盘文件”的“写入”箭头。
画面10: 在右侧流程图中，将“内存”框中的对象数量标注为“100/s对象”，表示每秒处理100个对象。
画面11: 在右侧流程图中，将“内存”框中的对象数量标注为“100/s对象”，并添加了“1/s”的时间间隔标注。
画面12: 在右侧流程图中，对“xml磁盘文件”框进行了选中操作。
画面13: 展示了 PPT 页面，标题为“4 百万数据报表导出”，并列出了“4.1 需求分析”、“4.2 解决方案”、“4.2.1 思路分析”、“4.2.2 原理分析”、“4.3 代码实现”等小节。
画面14: 展示了 PPT 页面中“4.3 代码实现”部分的代码片段，包括 AtomicInteger datasAi 的声明和循环设置单元格值的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
String [] titles = "编号,姓名,手机,最高学历,回家地区,护照号,薪资,生日,雇用,入职时间,离职类型,离职原因,离职时间".split(",");
Row row = sheet.createRow(0);
int titleIndex=0;
for (String title : titles) {
    cell = row.createCell(titleIndex++);
    cell.setCellValue(title);
}
int rowIndex = 1;
Cell cell = null;
for(int i=0;i<10000;i++){
    for (EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
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
        cell.setCellValue(employeeReportResult.getTheHighestDegreesOfEducation());
    }
}
```

画面5:
```xml
<row r="64">
  <c t="inlineStr"><is><v>"B64"</v></is></c>
  <c t="inlineStr"><is><v>"test58"</v></is></c>
  <c t="inlineStr"><is><v>"B65"</v></is></c>
  <c t="inlineStr"><is><v>"test59"</v></is></c>
  <c t="inlineStr"><is><v>"B66"</v></is></c>
  <c t="inlineStr"><is><v>"test60"</v></is></c>
  <c t="inlineStr"><is><v>"B67"</v></is></c>
  <c t="inlineStr"><is><v>"test61"</v></is></c>
  <c t="inlineStr"><is><v>"B68"</v></is></c>
  <c t="inlineStr"><is><v>"test62"</v></is></c>
  <c t="inlineStr"><is><v>"B69"</v></is></c>
  <c t="inlineStr"><is><v>"test63"</v></is></c>
  <c t="inlineStr"><is><v>"B70"</v></is></c>
  <c t="inlineStr"><is><v>"test64"</v></is></c>
  <c t="inlineStr"><is><v>"B71"</v></is></c>
  <c t="inlineStr"><is><v>"test65"</v></is></c>
  <c t="inlineStr"><is><v>"B72"</v></is></c>
  <c t="inlineStr"><is><v>"test66"</v></is></c>
  <c t="inlineStr"><is><v>"B73"</v></is></c>
  <c t="inlineStr"><is><v>"test67"</v></is></c>
  <c t="inlineStr"><is><v>"B74"</v></is></c>
  <c t="inlineStr"><is><v>"test68"</v></is></c>
  <c t="inlineStr"><is><v>"B75"</v></is></c>
  <c t="inlineStr"><is><v>"test69"</v></is></c>
  <c t="inlineStr"><is><v>"B76"</v></is></c>
  <c t="inlineStr"><is><v>"test70"</v></is></c>
  <c t="inlineStr"><is><v>"B77"</v></is></c>
  <c t="inlineStr"><is><v>"test71"</v></is></c>
  <c t="inlineStr"><is><v>"B78"</v></is></c>
  <c t="inlineStr"><is><v>"test72"</v></is></c>
  <c t="inlineStr"><is><v>"B79"</v></is></c>
  <c t="inlineStr"><is><v>"test73"</v></is></c>
  <c t="inlineStr"><is><v>"B80"</v></is></c>
  <c t="inlineStr"><is><v>"test74"</v></is></c>
  <c t="inlineStr"><is><v>"B81"</v></is></c>
  <c t="inlineStr"><is><v>"test75"</v></is></c>
  <c t="inlineStr"><is><v>"B82"</v></is></c>
  <c t="inlineStr"><is><v>"test76"</v></is></c>
  <c t="inlineStr"><is><v>"B83"</v></is></c>
  <c t="inlineStr"><is><v>"test77"</v></is></c>
  <c t="inlineStr"><is><v>"B84"</v></is></c>
  <c t="inlineStr"><is><v>"test78"</v></is></c>
  <c t="inlineStr"><is><v>"B85"</v></is></c>
  <c t="inlineStr"><is><v>"test79"</v></is></c>
  <c t="inlineStr"><is><v>"B86"</v></is></c>
  <c t="inlineStr"><is><v>"test80"</v></is></c>
  <c t="inlineStr"><is><v>"B87"</v></is></c>
  <c t="inlineStr"><is><v>"test81"</v></is></c>
  <c t="inlineStr"><is><v>"B88"</v></is></c>
  <c t="inlineStr"><is><v>"test82"</v></is></c>
  <c t="inlineStr"><is><v>"B89"</v></is></c>
  <c t="inlineStr"><is><v>"test83"</v></is></c>
  <c t="inlineStr"><is><v>"B90"</v></is></c>
  <c t="inlineStr"><is><v>"test84"</v></is></c>
  <
