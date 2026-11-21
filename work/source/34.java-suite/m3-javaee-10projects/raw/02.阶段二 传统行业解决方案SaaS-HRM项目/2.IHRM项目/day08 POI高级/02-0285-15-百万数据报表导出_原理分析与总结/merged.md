# 15-百万数据报表导出：原理分析与总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\15-百万数据报表导出：原理分析与总结_【海量资源尽在 ubkz.com】.mp4
- 时长 7分15秒（音频 436s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那对于这个SXSSF Workbook来说它究竟是怎么做到的能够对百万数据报表的一个支持那它有没有什么不好的地方那我们接下来呢就可以一起对它进行一个分析那首先呢我可以在这边再去重新导入一下我们这个数据报表并且呢导入的过程当中需要各位跟我一起来做一件事情
[00:30] 调出我们的命令行窗口在这边去找到系统当中的临时文件目录百分号temp百分号好了进入进来这个是我们的临时文件目录把里面的文件全部都给它删掉为了方便我们进行这个案例的演示和观察好了全部都删掉OK那好了接下来注意这门内容呢现在还没有什么我们可以值得关注的一些点那接下来在这边我再去生成
[01:02] 或者下载一个文件好了我点击了之后各位看内存开始有波来了有波动了有波动了接下来我们回到刚才的临时文件目录你发现多创建了这么一个临时文件这个临时文件叫做profile叫做profile好了接下来对于profile文件它是什么各位来看是不是一个XML的一个文件是一个XML文件并且这XML不断的在变大不断的在变大
[01:30] 好了我刷新了一下已经变大了那接着我把这个S苗打开各位看一下里面究竟有什么这个M苗打开还比较快啊来各位来看肉第一哎肉是不是代表行啊第一然后呢A1哎编号哎这不就是我们生成的S苗的这个头吗那底下是不是就是这些数据啊各位那我们就可以得知了对于好这边也可以下载了
[01:59] 对于我们这个XSF Workbook来说Workbook来说它是通过以XML的临时文件的形式帮助我们帮助我们存储临时的我们叫做内存变量内存对象没错吧好了刚才已经说过了它是通过临时文件的形式来帮助我们存储这些文件的存储这些内容的
[02:40] 那它是以X描的形式来进行存储那接下来呢看到了它究竟是如何做到的那接下来我们来分析一下就是对于这个对象它究竟是好还是坏我们使用的时候有没有需要注意的地方好了是这样的这边呢还是以一张图形的形式跟各位来进行一个分享首先呢这个同样也是我们的叫做程序的主线程好了这是我们的程序主线程
[03:10] 那成语主线程呢它就会去产生很多的报表的对象报表对象那创建报表对象的时候还是先把对象是不是放到我们的内存当中啊好了这个对象呢也有很多了包含了我们的肉包含了我们的sale当然还包含still等等等等我就写这么多了OK那接下来呢就是说在我们创建这个对象的时候可以确定一些预值
[03:45] 那这个域值呢我们给的它是一个100这个域值指的是当你对象的容量超过100的时候它是不是就开始往我们的磁盘当中写好了这边呢可以代表是我们的内存OK那当达到一定的数量之后这边呢它就开始写入到我们的磁盘文件当中换一个颜色磁盘文件XML那这边写入那接着我想跟各位来进行说明的就是说啊我们
[04:26] 主线程创建报表对象的时候你创建对象的过程它是比较快的因为我创建对象是不是直接就放到内存当中了直接就放到内存当中了那举一个最明显不过的例子比如说我这边一秒可以产生100个对象每秒那接着我这边是不是达到100的时候就开始往磁盘里写但是操作内存和操作我们的磁盘上的一个文件它的速度是不一样
[04:58] 那可能有一千倍的差别那这边不说一千倍就说一百倍一百倍什么意思就是说你这边一百一百个对象存到内存里了但是我是不是一秒只往我磁盘文件里面写了一个呀能理解这个啥意义吧所以你就会发现随着我这个对象或者我们这列表数据的不断增多如果它能支持一千万你会发现总有一天你内存还是会被承保也就是还会有我们叫做内存溢出的风险
[05:28] 因为你先放到内存里接着再写到磁盘文件里写到磁盘文件的时候一秒只写一个你这边创建了100个所以这是杯水车薪能理解吧各位所以我们刚才这张图形它的一个波动范围始终在波动始终在波动但是最终你占用的内存会是越来越多越来越多的什么一种情况直至你的内存增多那这样一来我们就可以得知了我们要想去解决
[05:57] 百万数据数据报表我们可以使用SXSSF Workbook来做但是对于使用它来说并不是万能的它并不是万能的我们要想真正的写入的话我们只有一个方法就是减少对象的产生所以我这边刚才说过了我们不要样式不要字体因为那些全部都是一些额外的对象的一些开销能理解吧各位
[06:23] OK好了这样一来呢咱们就已经把整个的百万数据报表导出的这些内容就跟各位都说过了对于这个百万数据报表的导出其实我们解决起来很简单使用一个对象即可那这个对象呢是用来替换我们之前的XSF Workbook那它呢是通过基于XML的这种临时文件的形式去减轻我们内存的压力也就是说把内存生平的一些对象给它写入到此外文件里共同的
[06:52] 在最后帮我们生成我们的报表那当然了对于它这个原理呢我们也知道了我们也知道对于它呢还有很多的不足的地方不足的地方就是说它不支持模板打印如果你写构造一个复杂报表的时候我们需要去写很多的样式但是违背了我们的初衷如果是百万报表真的有这种情况我们不需要写那些样式的一些内容OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

