# 14-百万数据报表导出：使用SXSSFWorkbook完成百万数据报表打印

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\14-百万数据报表导出：使用SXSSFWorkbook完成百万数据报表打印_【海量资源尽在 ubkz.com】.mp4
- 时长 7分14秒（音频 435s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的分析了一下百万数据报表导出的这么一个解决方法接下来我们就可以使用Apache的SXSSF Workbook去处理百万数据导出的这么一个案例对于这个对象如何去使用其实非常简单我们只需要打开我们的代码部分做一点点简单的改造其实就可以了首先需要跟各位做一个简单的声明
[00:29] 就是说呢对于这个SX SSF我写到上边F对象它呢不支持模板打印它不支持模板打印所以对于我们来说呢我们举行的案例就不能用这个模板打印的这个案例来做了那我们应该用什么来做呢其实就是我们最原始的之前的这种写法就是在上边那我再把上边的这段代码呢再给它打开好了这个就有点稍微有点麻烦啊各位耐心等待一下好了上面这个呢打开之后
[01:03] 那我们重点关注的只有一个方面就是这个创建Workbook的一个对象那我们现在使用的是SXSSF WorkbookKWRKBook好了它是专门用来处理百万数据报表的OK那好了接着呢我们就可以替换掉这个Workbook好了SXSSF WorkbookWBWB等于New一个
[01:38] SXWorkbook那注意我创建这个对象的时候呢其实这边呢可以借助它的构造方法往里面存入一些预定的一些值比如说呢我在这边可以给它设置100可以给它设置200那都可以这个值呢这边已经有体现了就是Row of SizeWindow Size这个代表了什么含义呢其实这个指的是一个预值预值这个预值代表的含义是这样的就是当
[02:10] 内存中的对象数量就是指的是内存当中对象的最大数最大数量当你到达了这个最大数量它就会把剩下的这些对象存入到一个临时文件当中了那这个阈值呢我们写什么比较合适呢其实你可以用默认即可它默认的是100默认是100那这样一来其实我这个方法就已经咱们改造好了那改造好了之后
[02:38] 注意那这个方法里面呢我其实没有写任何的就是样式的一些内容因为我们刚才分析过对于百万数据报表来说呢我们需要减少对象的一个产生那减少对象的产生就是这些样式对象或者这些字体对象我们一般就把它都省略的把它都省略掉了是因为这些对象呢其实还就是为了美化一些但是呢它对于我们产生数据报表来说的影响比较大当然刚才也说过了因人而异如果你的
[03:05] 项目当中需要的话你还可以自己进行设置当然了这个进行设置的时候稍微有点麻烦因为它不支持模板打印的这种方式OK那好了我们把这个代码部分呢基本上都已经改造好了其实就这么一个对象的一个替换即可那我这边再去启动一下我们的这个员工微服务好了这边让它去重新启动那接下来呢回到我们的浏览器好了我这边呢还是手动输入一下03好了刷新一下
[03:35] 告诉我没登录啊重新跳转登录了好了那接下来呢重新登录一下用02账号登录进去员工好了按月份报表数据当然了这边还是重新输入一下03当然了为了以保万全啊我这边重新刷新一下那我这边的程序呢应该已经启动成功了那各位我再去导出一下在导出之前还是跟之前一样打开我们这边的监控工具好了已经启动成功了Eploid ApplicationOK
[04:08] 接着监视一下我的内存和我的CPU情况各位来说就目前来说还没有打印它占用的内存还是比较少的就200多兆我看到这边的CPU基本上没有产生任何的影响接着我在这边开始进行导出好了这边我一点击导出按钮不应该这么快不应该这么快各位这个数据有问题是因为我们这边没有给它进行一个百万数据的这么一个循环操作
[04:40] 没错吧好了把这个循环操作呢再给它补上放循环int i 等于0i 小于小于1万十百千万好了i 加加好了这边就快一点了OK好了再去重新启动一下这个就有点麻烦了好了再去重新启动那在这边呢监视的时候呢同样也要重新关掉再去打开我们新启动的Apply Application好了还是跟刚才一样这边已经启动成功了刚刚启动会有一点点波波澜
[05:20] 那最终是会趋于平稳的OK那好了接着我回到浏览器接着我再去进行导出走好了各位我现在已经点击了导出按钮那我们看一下内存监控的一个情况那各位来看这回这边内存占用的它的波折线各位应该能看到它是一个波折的这么一个曲线为什么是因为它产生一定数量的对象之后它是不是写入到内存里了写入到文件里写入到文件当然不会占用任何内存了
[05:50] 接着又产生一定数量的又写入到文件里又产生一定数量的写入到文件产生产生好了写入文件那各位会发现这个其实就是一个波折曲线的这么一种情况继续往后台进行执行当然了我们可以耐心等待一会儿其实这个报表就会让我们去进行一个打印了OK各位再耐心等待一下各位来看现在其实这个报表已经生成出来并且我们可以把它下载到我们的本地电脑里
[06:20] 好了保存那各位来看通过这个SXSSF Workbook对于百万数据量报表的产生它这回占用的内存是不是就少了很多并且能够完整的把我们这个文件下载下来那文件下载下来之后我们把它打开看一下好了这个文件相对来说还是有一点点多的因为它打开也比较慢40多兆刚才我们也看过了好了各位跟我一样耐心等待一下
[06:53] 好了这边已经打开成功了我们可以一起看一下有多少数据一直往下拖一直往下拖好了有96万号OK这个其实也就已经证明了我们这种方案是可行的并且能够支持百万数据量的这么一个情况对我们的内存占用来说也是可以接受的这么一个范畴

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

