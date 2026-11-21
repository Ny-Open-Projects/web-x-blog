# 11-百万数据报表：导出测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\11-百万数据报表：导出测试_【海量资源尽在 ubkz.com】.mp4
- 时长 4分45秒（音频 285s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的对这个百万的数据报表呢做了一个说明也说了一下这个这viso vm这个工具那接下来呢我们就可以在我们自己的程序上边给它构造一个百万数据py报表的一个导出来看一下它究竟会发生什么样的事情好了那如何去做呢因为我数据库的数据呢真的没有百万那没有百万那咋办注意我去改一下我这个
[00:33] 代码这个代码呢我现在就不用什么工具类了因为用工具类的看出来不太直观并且我这个数据量不太好修改我就用之前这段代码了好了那接下来那对于我这个百万数据呢我先做一个简单的构造那查询出来之后我这边给它来一个放循环int i 等于 0ok i 小于比如说呢一万一万吧一万好了那接下来 i 加加
[01:12] OK好了接下来把中间这个放循环再给它包裹出来那我们简单的说一下我为什么写了一个一万的这么一个循环是因为我们之前呢有些朋友应该能看出来我查询的是三月份的数据那三月份的数据在我数据库里面相对来说还是比较多的大概有90多条有90多条呢我乘以一万倍就是90多万条呗那90多万条呢其实去对于90多万条一个数据报表的一个导出来说呢就能看到效果了
[01:43] 那好了这边我把数据构造好了之后我们重点关注的是对于PUI来说它能不能够实现下载的这个功能好了这边我重新启动一下OK那重新启动之后呢我们就可以打开我们的浏览器再去重新的导出一下我们的数据注意我这边呢由于重新启动了刚才我这个服务由于重新启动了刚才我这个企业服务我还需要重新再打开一下好了监视各位来看
[02:18] 这个也是刚刚运行大概有20多秒好了接下来我们实现导出走各位现在呢程序呢说没执行嘛它真的一直在执行还是一直在执行着呢我们可以通过这个监控工具能够看到当前的一个执行情况那各位呢其实可以从这边直观的能够看到就当前来说我一点CPU它就开始有波动
[02:45] 并且呢右边我堆内存占用的大小也是开始有波动但是总体而言它趋向于越来越多没错吧并且呢它越来越占用我的内存越来越占用我的内存是意思吧那各位看的这个图怎么去看呢其实就是看的是蓝色线部分蓝色线部分指的是当前占用的或者已经使用的堆内存好了各位来看目前来说呢应该已经使用堆内存已经快两季了而且越来越多越来越多那各位
[03:17] 我当前还没下载呢还没有结束呢这个代表什么含义啊也就是说我们刚才处理百万数据的一个报表导出的话它对我的电脑性能有极高的影响或者有极高的要求也就是说你性能第一得多第二个就是说我们传统的方式去处理百万数据不太靠谱为什么它会不断的去占有我的内存
[03:42] 不断的去占有内存直到把我内存全部吃满抛出内存不足也就是我们的OOM的一个异常其实可以通过这张图形能够看出来它是一直在平稳的往上增长一直在去占有我的内存那这个程序我就把它停掉了就不让它再执行了其实这个最终它的效果必然会导致内存不足而变成一个异常OK当然了除了我们刚才演示的导出的功能
[04:14] 我们还有员工的一个叫做是不是一个员工导入的功能员工导入的功能如果你导入一个百万数据的一个报表你导入的话也会出现类似的这么一个效果也就是说你后台占用的内存越来越多直至内存一出我这边需要跟各位说明一下我这边是为了讲课去执行这种操作但是各位就不必了为什么因为它不断的占用内存这边CPU使用越来越高并且你CPU就比较热这边友情提示一下
[04:43] OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

