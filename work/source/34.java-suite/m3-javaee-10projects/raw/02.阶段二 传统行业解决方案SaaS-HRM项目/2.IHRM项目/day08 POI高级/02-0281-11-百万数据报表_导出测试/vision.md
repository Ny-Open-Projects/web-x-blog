# 画面线理解：11-百万数据报表：导出测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\11-百万数据报表：导出测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:17, 00:30, 00:42, 00:51, 01:14, 01:20, 01:35, 01:46, 02:02, 02:16, 02:31, 04:02, 04:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:11:50

1) 这一组画面整体在讲如何使用 Apache POI 库在 Java 中导出大量员工数据到 Excel 文件，并通过 VisualVM 监控程序性能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 VisualVM 中的 CPU 和内存监控图表，程序正常运行10分钟，CPU使用率0.7%，内存使用量约150MB。
画面2：展示 HRM 系统前端界面，显示“03月人事报表”页面，包含筛选条件和“导出”按钮。
画面3：展示 IntelliJ IDEA 中的 ExcelExportUtil.java 文件，定义了导出工具类的构造方法。
画面4：展示 EmployeeController.java 文件中导出方法的实现，包括创建输出流和下载文件。
画面5：展示 EmployeeController.java 文件中循环设置单元格值的代码，包含注释说明。
画面6：展示 EmployeeController.java 文件中循环设置单元格值的代码，包含注释说明。
画面7：展示 EmployeeController.java 文件中导出方法的实现，包括加载模板文件和创建工作簿。
画面8：展示 EmployeeController.java 文件中循环设置单元格值的代码，包含注释说明。
画面9：展示 EmployeeController.java 文件中循环设置单元格值的代码，包含注释说明。
画面10：展示 PDF 文档中关于 Apache POI 导出 Excel 的三种解决方案分析，包含表格对比 Streaming、In memory tree 和 Buffered Streaming。
画面11：展示 VisualVM 中的堆内存快照，显示 JVM 启动参数和内存配置。
画面12：展示 HRM 系统前端界面，显示“03月人事报表”页面，包含筛选条件和“导出”按钮。
画面13：展示 VisualVM 中的 CPU 和内存监控图表，程序运行2分20秒，CPU使用率约0.3%，内存使用量约4.5GB。
画面14：展示 VisualVM 中的 CPU 和内存监控图表，程序运行2分25秒，CPU使用率约0.3%，内存使用量约4.5GB。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
public class ExcelExportUtil<T> {
    private int rowIndex; //写入数据的起始行
    private int styleIndex; //需要提取的样式所在的行号
    private Class<T> clazz; //对象的所有属性
    private Field fields[];
    @Setter
    public ExcelExportUtil(Class<T> clazz,int rowIndex,int styleIndex) {
        this.clazz = clazz;
        this.rowIndex = rowIndex;
        this.styleIndex = styleIndex;
        fields = clazz.getDeclaredFields();
    }
    //基于注解导出
    @Setter
    public void export(HttpServletResponse response,InputStream is, List<T> objs,String fileName) throws Exception {
        //1.根据注解创建工作簿
        Workbook wb = new XSSFWorkbook(is);
        //2.创建sheet
        Sheet sheet = wb.getSheetAt(0);
        //3.抽取公共样式
        CellStyle styles [] = new CellStyle[row.getlastCellNum()];
        for(int i=0;i<row.getlastCellNum();i++){
            Cell cell = row.getCell(i);
            styles[i] = cell.getCellStyle();
        }
        //4.填充单元格
        int rowIndex = 2;
        Cell cell = null;
        for(int i=0;i<10000;i++){
            row.createCell(i);
            cell.setCellValue(objs.get(i).getUserName());
            cell.setCellStyle(styles[1]);
        }
    }
}
```

画面4：
```java
// 高离职原因
cell = row.createCell(11);
cell.setCellValue(employeeReportResult.getReasonsForLeaving());
cell.setCellStyle(styles[11]);
// 高辞职时间
cell = row.createCell(12);
cell.setCellValue(employeeReportResult.getResignationTime());
cell.setCellStyle(styles[12]);
// 3.下载
ByteArrayOutputStream os = new ByteArrayOutputStream();
wb.write(os);
new DownloadUtils().download(os,response,month+"人事报表.xlsx");
```

画面5：
```java
for(int i=0;i<row.getlastCellNum();i++){
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

画面6：
```java
cell = row.createCell(0);
cell.setCellValue(employeeReportResult.getUserId());
cell.setCellStyle(styles[0]);
cell = row.createCell(1);
cell.setCellValue(employeeReportResult.getUsername());
cell.setCellStyle(styles[1]);
cell = row.createCell(2);
cell.setCellValue(employeeReportResult.getMobile());
cell.setCellStyle(styles[2]);
cell = row.createCell(3);
cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
cell.setCellStyle(styles[3]);
cell = row.createCell(4);
cell.setCellValue(employeeReportResult.getNationalArea());
cell.setCellStyle(styles[4]);
cell = row.createCell(5);
cell.setCellValue(employeeReportResult.getPassportNo());
cell.setCellStyle(styles[5]);
```

画面7：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = resourceCompanyPersonalService.findDBByReport(companyId,month);
    //1.加载模板
    Resource resource = new ClassPathResource("excel-template/hr-demo.xlsx");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.通过模板完成下载
    Workbook wb = new XSSFWorkbook(fis);
    Sheet sheet = wb.getSheetAt(0);
    //3.抽取公共样式
    CellStyle styles [] = new CellStyle[row.getlastCellNum()];
    for(int i=0;i<row.getlastCellNum();i++){
        Cell cell = row.getCell(i);
        styles[i] = cell.getCellStyle();
    }
    //4.填充单元格
    int rowIndex = 2;
    Cell cell = null;
    for(int i=0;i<10000;i++){
        row.createCell(i);
        cell.setCellValue(objs.get(i).getUserName());
        cell.setCellStyle(styles[1]);
    }
}
```

画面8：
```java
for(int i=0;i<10000;i++){
    row.createCell(i);
    cell.setCellValue(objs.get(i).getUserName());
    cell.setCellStyle(styles[1]);
}
```

画面9：
```java
cell = row.createCell(4);
cell.setCellValue(employeeReportResult.getNationalArea());
cell.setCellStyle(styles[4]);
cell = row.createCell(5);
cell.setCellValue(employeeReportResult.getPassportNo());
cell.setCellStyle(styles[5]);
cell = row.createCell(6);
cell.setCellValue(employeeReportResult.getNativePlace());
cell.setCellStyle(styles[6]);
cell = row.createCell(7);
cell.setCellValue(employeeReportResult.getBirthDay());
cell.setCellStyle(styles[7]);
cell = row.createCell(8);
cell.setCellValue(employeeReportResult.getTimeEntry());
cell.setCellStyle(styles[8]);
cell = row.createCell(9);
cell.setCellValue(employeeReportResult.getTypeOfTurnover());
cell.setCellStyle(styles[9]);
cell = row.createCell(10);
cell.setCellValue(employeeReportResult.getReasonsForLeaving());
cell.setCellStyle(styles[10]);
cell = row.createCell(11);
cell.setCellValue(employeeReportResult.getResignationTime());
cell.setCellStyle(styles[11]);
```

画面10：
```markdown
| API Type | Streaming (ala SAX) | In memory tree (ala DOM) | Streaming (ala SAX) | In memory tree (ala DOM) | Buffered Streaming |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面10：
标题：3.3 解决方案分析
表格数据：
| API Type | Streaming (ala SAX) | In memory tree (ala DOM) | Streaming (ala SAX) | In memory tree (ala DOM) | Buffered Streaming |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
