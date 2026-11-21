# 12-百万数据报表：分析以及解决办法

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\12-百万数据报表：分析以及解决办法_【海量资源尽在 ubkz.com】.mp4
- 时长 6分27秒（音频 388s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 其实通过刚才的测试结合我们这个JavaVisualVM这个工具各位就能够看出一些端倪了为什么最终会导致内存不足或者内存溢出的这么一个错误是由于我这个内存占用越来越多它的对象越来越多并且呢左边CPU的运行也佐证了我们刚才的这句话那CPU呢这边看蓝色线部分是不是一个垃圾回收的一个活动的一个状态这么一张图啊
[00:28] 那也就意味着你这边创建的对象越来越多达到一顶的值的话垃圾回收介入而你又回收不了所以你占用的内存越来越多而左边一直一直在垃圾回收那就造成了那内存一直不释放你占用的内存越来越多直至最后内存全部被你吃完抛出内存不足的这么一个错误那我们都知道了产生的对象太多了所以造成内存不足没错吧那我们回到我们的代码部分
[00:56] 来看一下我们究竟产生了多少个对象接着再来分析一下为什么它垃圾回收不能回收来各位我们的代码呢其实从上到下有很多有很多那各位我们关注的其实就是中间这个循环体部分那这边一万乘以各位这里面九十多也就是九十多万那九十多万的话肉行它是一个对象Sale我们叫做单元格也是一个对象
[01:26] 在这个里面呢各位来看我还要设置样式样式是不是也是一个对象样式里面是不是还有字体那这些字体等等是不是都是对象啊所以你会发现对于我们Excel报表导出而言它是把所有的对象全部都生产出来或者全部都创建出来那创建出来之后先放到内存里当你把所有的这些全部都加载完成全部都加载完成之后
[01:55] 我才最后以留的形式帮助你进行下载也就是说在下载之前我们产生的这些对象永不释放一直占用内存那这个也就比较明确了由于PUI操作Excel的时候内存占用实在太多最终导致了我们的内存不足那这个原因呢我们做了一个分析那接下来就是说我们要想解决这个问题如何去做如何着手好了其实呢在
[02:26] Apache POI它的官方网站也对我们提供大数据量的POI报表操作提供了一些解决的方法和一些解决的一些工具其实在我们POI操作Excel的时候如果面对大数据的话它分为了这么三种形式帮助我们进行操作这三种形式第一个叫做用户模式
[02:53] 那第一个是用户模式这个用户模式是什么意思啊其实我们操作操作Excel的时候我们之前写的那些代码都是基于用户模式的形式来做的那用户模式就是在PUI当中帮你封装好好多的方法帮你封装出很多的类封装出很多的工具让我们去使用那它付出的代价是什么呢就是里面封装的不透明而且里面产生了大量的对象所以这种方式去操作的话
[03:21] 比较耗脱存这是我们之前使用的方法就是一个叫做用户模式那除了用户模式之外它还提供了一个叫做事件模式那事件模式是什么呢事件模式其实是基于SaaS的方式去解析XML因为我们都知道我们现在讨论的都是2007那2007呢其实它的底层就是一个XML所以SaaS方式其实是基于SaaS的方式去解析XML那如果解析XML的话这个可能就快了很多了
[03:50] 那当然了这些事件模式呢它究竟底层原理是什么样的我们一会还会解释那除了这两种模式之外还有一个是一个对象这个对象叫做XSSFXSSF就SSXSSF这个对象念起来比较绕口啊那各位这个对象呢其实跟我们之前用到的一个对象比较像就是看后四个字母所以对于这个对象呢它也是用来处理2007版本的
[04:19] 而且这个对象它重点就是用来解决海量incel报表导出的所以这个就比较明确了我们一会就可以通过SXSSF对象去解决报表导出的这么一个问题那这个是如何去做的它其实就是借助临时文件那我们一会去详细的解释一下它究竟如何去做当了这边还给各位准备了一张图形
[04:48] 这一张图形是阿帕奇这个PUI官方提供的这么一张图它描述了用户模式事件模式以及使用这个SXSSF它那种方式对Excel操作的一个内存或者对于机器的一个使用情况的这么一个结构图那这张图里面分为两个部分首先203版本不在我们讨论的范围之内还有一个就是2007版本2007版本就正好佐证了我刚才跟各位分析的这三种方式
[05:18] 那有一个叫做event model事件模型还有一个叫做user model就是我们的用户模型还有一个就是我们的一个对象了OK这里一个对象呢里面呢占用的比如说这边有一个叫做CPU and memory就是我们的CPU和内存占用那各位来看goodgood没错啊也就是说基于SaaS模式的这种事件模型CPU占用和我们内存哎耗费比较低那同样的我们这边这个SX SSF对象同样的也是比较好的
[05:48] 那其中不太好的呢就是我们这个用户模型了那接下来呢就是说对于这三种模式事件模型它是干嘛的对于事件模型它是用来解析大数据量报表的它是用来解析的它用来读取的它用来导入的那接着对于XSSF这个对象它是用来干嘛的它是用来生成Excel的所以我们一会儿要完成百万数据导出各位我们用哪个对象大家就应该知道了就是这个XSSF
[06:18] 如果我们要想读取百万数据用什么各位应该也清楚了我们就要用事件模型了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apache POI 库在 Java 中导出员工报表到 Excel 文件，并分析了不同导出模式（用户模式、事件模式、SXSSF）的性能和功能特性。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 IntelliJ IDEA 中的 Java 应用程序运行监控界面，包含 CPU 使用率、内存使用率、线程和类的监控图表，以及项目结构视图。
画面2: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中导出 Excel 文件的代码片段，包含设置单元格样式和创建输出流的代码。
画面3: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中创建 Workbook、Sheet 和设置单元格样式等初始化代码。
画面4: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中设置单元格值的代码，包括用户 ID、姓名、手机号、最高学历、国籍、护照号、籍贯、生日等字段。
画面5: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中设置单元格值的代码，包括用户 ID、姓名、手机号、最高学历、国籍、护照号、籍贯、生日等字段。
画面6: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中设置单元格值的代码，包括用户 ID、姓名、手机号、最高学历、国籍、护照号、籍贯、生日等字段。
画面7: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中设置单元格值的代码，包括入职时间、离职原因、离职时间等字段。
画面8: 在 IntelliJ IDEA 中，展示了 EmployeeController.java 文件中设置单元格值的代码，包括用户 ID、姓名、手机号、最高学历、国籍、护照号、籍贯、生日等字段。
画面9: 展示了 PPT 页面，标题为“3.3 解决方案分析”，内容包括对 Apache POI 导出 Excel 的三种模式（用户模式、事件模式、SXSSF）的介绍和性能对比表格。
画面10: 展示了 PPT 页面，标题为“3.3 解决方案分析”，内容包括对 Apache POI 导出 Excel 的三种模式（用户模式、事件模式、SXSSF）的介绍和性能对比表格。
画面11: 展示了 PPT 页面，标题为“3.3 解决方案分析”，内容包括对 Apache POI 导出 Excel 的三种模式（用户模式、事件模式、SXSSF）的介绍和性能对比表格。
画面12: 展示了 PPT 页面，标题为“3.3 解决方案分析”，内容包括对 Apache POI 导出 Excel 的三种模式（用户模式、事件模式、SXSSF）的介绍和性能对比表格。
画面13: 展示了 PPT 页面，标题为“3.3 解决方案分析”，内容包括对 Apache POI 导出 Excel 的三种模式（用户模式、事件模式、SXSSF）的介绍和性能对比表格。
画面14: 展示了 PPT 页面，标题为“3.3 解决方案分析”，内容包括对 Apache POI 导出 Excel 的三种模式（用户模式、事件模式、SXSSF）的介绍和性能对比表格。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2:
```java
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
// 高职类型
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
// 高职原因
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
// 高职时间
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
}
// 下载
// 完成下载
ByteArrayOutputStream os = new ByteArrayOutputStream();
// response, returnName: month+"人事报表.xlsx";
```

画面3:
```java
//3.根据模板创建工作簿
Workbook wb = new XSSFWorkbook(fis);
//4.创建工作表
Sheet sheet = wb.getSheetAt(i);
//5.复制工作表样式
Row row = sheet.getRow(2);
CellStyle styles [] = new CellStyle[row.getlastCellNum()];
for(int i=0;i<row.getlastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
//6.设置单元格
int rowIndex = 2;
Cell cell=null;
for(int i=0;i<10000;i++) {
    row = sheet.createRow(rowIndex++);
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
    cell.setCellValue(employeeReportResult.getHighestDegreeOfEducation());
    cell.setCellStyle(styles[3]);
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
    cell.setCellValue(employeeReportResult.get***());
    cell.setCellStyle(styles[7]);
    cell = row.createCell(8);
    cell.setCellValue(employeeReportResult.get***());
    cell.setCellStyle(styles[8]);
}
```

画面4:
```java
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
// 高职类型
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
// 高职原因
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
// 高职时间
cell = row.createCell(i);
cell.setCellValue(employeeReportResult.get***());
cell.setCellStyle(styles[i]);
```

画面7:
```java
// 下载
// 完成下载
ByteArrayOutputStream os = new ByteArrayOutputStream();
wb.write(os);
new DownloadUtils().download(os, response, returnName: month+"人事报表.xlsx");
```

画面9-14:
```markdown
3.3 解决方案分析

对于百万数据量的Excel导入导出，只讨论基于Excel2007的解决方法。在Apache POI 官方提供了对操作大数据量的导入导出的工具和解决方法，操作Excel2007使用SXSSF对象，可以分为三种模式：

- 用户模式：用户模式有许多封装好的方法操作简单，但创建太多的对象，非耗内存（之前使用的方法）。
- 事件模式：基于SAX方式解析XML，SAX全称Simple API for XML，它是一个接口，也是一个软件包，它是一种XML解析的替代方法，不同于DOM解析XML文档时把所有内容一次性加载到内存中的方式，它逐行扫描文档，一边扫描，一边解析。
- SXSSF对象：是用来生成海量excel数据文件，主要原理是借助临时存储空间生成excel

API Type
| HSSF (.xls) | XSSF (.xlsx) |
| --- | --- |
| eventmodel | usermodel | eventmodel | usermodel |
| Streaming (as SAX) | In memory tree (as DOM) | Streaming (as SAX) | In memory tree (as DOM) |
| Buffered Streaming |  |  |  |
| CPU and Memory Efficiency | Good | Varies | Good | Varies | Good |
| Forward Only | Yes | No | Yes | No | Yes |
| Read Files | Yes | Yes | Yes | Yes | No |
| Write Files | No | Yes | No | Yes | No |
| Feature: |
| create sheets / rows / cells | No | Yes | No | Yes | Yes |
| styling cells | No | Yes | No | Yes | Yes |
| delete sheets / rows/cells | No | Yes | No | Yes | No |
| shift rows | No | Yes | No | Yes | No |
| cloning sheets | No | Yes | No | Yes | No |
| formula evaluation | No | Yes | No | Yes | Yes |
| cell comments | No | Yes | No | Yes | Yes |
| pictures | No | Yes | No | Yes | Yes |
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面9-14:
标题：3.3 解决方案分析
内容：
- 用户模式：用户模式有许多封装好的方法操作简单，但创建太多的对象，非耗内存（之前使用的方法）。
- 事件模式：基于SAX方式解析XML，SAX全称Simple API for XML，它是一个接口，也是一个软件包，它是一种XML解析的替代方法，不同于DOM解析XML文档时把所有内容一次性加载到内存中的方式，它逐行扫描文档，一边扫描，一边解析。
- SXSSF对象：是用来生成海量excel数据文件，主要原理是借助临时存储空间生成excel

表格数据：
| API Type | HSSF (.xls) | XSSF (.xlsx) |
| --- | --- | --- |
| eventmodel | usermodel | eventmodel | usermodel |
| Streaming (as SAX) | In memory tree (as DOM) | Streaming (as SAX) | In memory tree (as DOM) |
| Buffered

