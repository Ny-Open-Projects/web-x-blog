# 20-百万数据报表读取：代码实现以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\20-百万数据报表读取：代码实现以及总结_【海量资源尽在 ubkz.com】.mp4
- 时长 6分30秒（音频 390s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那对于最后我们要想去完成整个Excel的这个读取而言是这样的就是说呢我整个Excel报表呢其实它应该有很多个表格有很多个sheet那每一个sheet是不是都要进行一个读取的这么一个操作呀所以我们主行主取的条件是拿到一个一个sheet每一页都要进行读取所以呢我们还要对一页进行一个处理也就是对每一个sheet进行处理那如何进行处理呢很简单是我们这个reader对象
[00:30] XSSF Reader对象这个Reader对象呢不就是已经打开了我们这个整个文件吗这个文件里面其实就能够得到里面的每一个sheet那我们如何去做很简单Reader打点GetSheetsDate没问题这样一来得到所有页的数据那这样一来呢其实得到的是一个InputStream的这么一个Iterator迭代器那这个迭代器呢可以对它进行一个强制转型的这么一个处理把它转化成XSSF Reader
[01:02] XF Reader里面呢其实也包含一个叫做sheet迭代器OK那这边报错了我先给它写完整吧等于好了我就给它来一个sheet iterator看一下还好了吗没问题了OK那这个样一来呢其实我们就得到了一个基于每一个sheet的一个迭代器那剩下的事情就简单了Val循环判断一下是否还有多余的sheet
[01:31] 打点叫做has more elements按has next那接下来我们要做的事情就是得到每一页里面的流数据打点next好了这样一来注意它得到的是一个流数据好了这个是得到每一个sheet的流数据那得到了这个每一个sheet流数据接着呢我们需要进行循环迭代需要以sus的形式解析我们的xml那我们如何去做就不得不提一个叫做sus source这么一个方法
[02:10] 这么一个对象new一个inputsource好了输入源添加进去我们的输入源其实就是每一个sheet里面的所有的内容那这样一来我每一个sheet所有内容都已经给它填充过来了那剩下的事情我们借助reader对象也就是借助我们的事件处理器借助我们的channel handler这个对象把它全部都解析出来
[02:42] 就可以了那我们这边解析的过程也比较简单也比较简单我们可以通过XML Reader对象里面的一个方法打点Parse那我们解析的内容在哪呢注意是我们的数据来源把S传递进去它就开始进行解析那这个思路很简单是这样子那对于XML Reader呢它可以把这里面的每一个单sheet里面的所有内容都加载过来那加载过来之后
[03:13] 碰到其中的某一行那碰到某一行我就借助里面刚才写好的stardrawendraw和sale方法进行处理碰到一行掉一把碰到一行掉一把OK那好了我这个方法呢已经写好了那我们接下来就可以运行一把看一下这个方法能不能把数据给我解析出来看一下有没有问题来走
[03:41] 好了现在呢这个代码呢已经开始运行起来了那运行起来呢这边呢开始就是输出了各位来看为什么能够输出是不是这边呢我们写过开始行要干一件事结束行要把它打运出来当然我们可以在结束行里面天下自我业务操作那这里面是不是写里面的一个一个的数据的一个属性上面的一个复制那接下来呢我们可以打开我们的GVSO这个面板一起来观察一下我们执行的是PUI test06
[04:09] 看一下我这边的内存占用情况以及垃圾回收的一个情况这个不可能吧我这个已经执行完成了这个有点快啊好了我再去执行一下其实这个不执行也行其实我们已经看出来结果了这个能够执行成功并且不会抛出任何的问题那我们看一下我整个的内存占用情况你会发现这个内存占用呢其实蓝色线的是使用内存你发现最多也就二三百兆大概五百兆的样子那这边
[04:39] 不会出现任何的内存那个波浪当然了CPU占用也是比较平缓的OK那这样一来呢其实我们就已经通过这种事件模型的这种形式完成了百万数据报表的这么一个读取好了那这些我们都搞定了之后呢简单的对我们这些百万数据报表操作做一个简单总结其实我们可以看到看到基于事件的这种方式
[05:06] 虽然代码写起来有点啰嗦有点绕口可能还不太好理解但是它对于我们节省内存而言特别是对于百万数据的一个读取是不是更加良好啊OK那到目前为止呢我们今天的所有的内容就跟各位都讲过了我们今天的内容呢一共有这么几块首先呢第一个就是我们的报表的一个打印报表打印讲了一个传统的还讲了一个模板打印模板打印可以根据模板搞一些样式出来
[05:36] 那当然了我们还搞了几个自定义的工具类通过注解通过工具类的形式简化我们的代码开发的一个操作那这个自定义工具类呢特别这个自定义注解和我们一些反射的配合的一些用法还是希望各位能够掌握的那这块看过了之后接着就是我们的第三块版权数据报表我们要知道对于版权数据来说呢分为读取和我们的一个报表打印
[06:00] 那我们如何去解决这些方式呢通过这张图形特别是POI给我们提供的这张图形它提供了这么几个概念第一个用户模式第二个事件模式还有第三个SXSSF对象那事件模型是用来进行读取的这个对象是不是用来进行Excel报表生成的没错吧那接下来我们搞了一个百万数据的导出以及数据读取那这些原理性的内容和我们代码实现都希望各位能够实现都希望各位能够理解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apache POI 的事件模型（SAX）解析大型 Excel 文件，对比用户模型的内存占用，并介绍性能监控工具 VisualVM。

2) 按时间顺序列出每张画面的要点：
画面1：展示主程序 PoTest06.java，初始化 OPCPackage、XSSFRReader、SharedStringsTable、StyleTable，并创建 XMLReader 和 SheetHandler，准备解析 Excel。
画面2：展示 XMLReader 的方法列表，说明其用于处理 XML 数据流。
画面3：展示 SheetIterator 的方法列表，说明其用于遍历工作表。
画面4：在主程序中创建 SheetIterator 并进入 while 循环，准备逐个处理每个 sheet。
画面5：在循环中创建 InputSource，准备解析每个 sheet 的 XML 数据流。
画面6：展示 SheetHandler 类的定义，实现 XSSFSheetXMLHandler.SheetContentsHandler 接口，用于处理 XML 解析事件。
画面7：在 SheetHandler 中实现 startRow 方法，初始化 PoEntity 对象。
画面8：在 SheetHandler 中实现 cell 方法，根据列名（A-E）设置 PoEntity 对象的相应属性。
画面9：在 SheetHandler 中实现 endRow 方法，打印当前解析的 PoEntity 对象。
画面10：在 SheetHandler 中实现 endRow 方法，打印当前解析的 PoEntity 对象。
画面11：展示 VisualVM 工具界面，监控程序运行时的 CPU 和内存使用情况。
画面12：展示 PPT 标题“5.3.3 对比测试”，介绍用户模式和事件模式解析 Excel 的内存占用差异。
画面13：展示 PPT 标题“3.2 JDK性能监控工具介绍”，介绍 VisualVM 工具。
画面14：展示 PPT 标题“5.3.5 对比测试”，对比用户模型和事件模型的性能，展示不同 API 类型的效率和功能支持。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
public class PoTest06 {
    public static void main(String[] args) throws Exception {
        // 1. 读取excel文件
        String path = "C:\\Users\\ThinkPad\\Desktop\\lirm\\dev8\\资源\\百万的腺瘤样本\\demo.xlsx";
        OPCPackage opcPackage = OPCPackage.open(path, PackageAccess.READ);
        XSSFRReader reader = new XSSFRReader(opcPackage);
        // 2. 获取共享字符串表
        SharedStringsTable table = reader.getSharedStringsTable();
        // 3. 获取样式表
        StyleTable styleTable = reader.getStylesTable();
        // 4. 创建xmlReader对象
        XMLReader xmlReader = XMLReaderFactory.createXMLReader();
        XSSFSheetXMLHandler xmlHandler = new XSSFSheetXMLHandler(styleTable, table, new SheetHandler());
        xmlReader.setContentHandler(xmlHandler);
        // 5. 获取sheet迭代器
        XSSFRReader.SheetIterator sheetIterator = (XSSFRReader.SheetIterator) reader.getSheetsData();
        while (sheetIterator.hasNext()) {
            InputStream stream = sheetIterator.next();
            InputSource is = new InputSource(stream);
        }
    }
}
```

画面6：
```java
import org.apache.poi.xssf.eventusermodel.XSSFEventModel;
import org.apache.poi.xssf.usermodel.XSSFComment;

public class SheetHandler implements XSSFSheetXMLHandler.SheetContentsHandler {
    private PoEntity entity;
    @Override
    public void startRow(int i) {
        if(i>0) {
            entity = new PoEntity();
        }
    }
    @Override
    public void cell(String cellReference, String value, XSSFComment xssfComment) {
        if(entity != null) {
            String pix = cellReference.substring(0, 1);
            switch (pix) {
                case "A":
                    entity.setId(value);
                    break;
                case "B":
                    entity.setBreast(value);
                    break;
                case "C":
                    entity.setAdipocytes(value);
                    break;
                case "D":
                    entity.setNegative(value);
                    break;
                case "E":
                    entity.setStaining(value);
                    break;
                case "F":
                    entity.setSupportive(value);
                    break;
                default:
                    break;
            }
        }
    }
    @Override
    public void endRow(int i) {
        System.out.println(entity);
    }
}
```

画面8：
```java
public class PoTest06 {
    public static void main(String[] args) throws Exception {
        String path = "C:\\Users\\ThinkPad\\Desktop\\lirm\\dev8\\资源\\百万的腺瘤样本\\demo.xlsx";
        OPCPackage opcPackage = OPCPackage.open(path, PackageAccess.READ);
        XSSFRReader reader = new XSSFRReader(opcPackage);
        // 5. 获取sheet迭代器
        XSSFRReader.SheetIterator sheetIterator = (XSSFRReader.SheetIterator) reader.getSheetsData();
        while (sheetIterator.hasNext()) {
            InputStream stream = sheetIterator.next();
            InputSource is = new InputSource(stream);
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面12：
标题：5.3.3 对比测试
内容：
- 用户模式下读取测试Excel文件直接存进内存，测试Excel文件映射到内存中还是占用了不少内存；事件模式下可以流畅的运行。
- （1）使用用户模型解析
- （2）使用事件模型解析

画面13：
标题：3.2 JDK性能监控工具介绍
内容：
- 没有性能监控工具，一切都能停留在理论阶段，我们可以使用java的性能监控工具来监控程序的运行情况，包括CPU垃圾回收、内存的分配和使用情况，这让程序的运行阶段变得更加可控，也可以用来证明我们的推测。这里我们使用JDK自带的性能监控工具VisualVM来监控程序运行。
- 3.2.1 Jvisualvm概述
- VisualVM是Netbeans的profile子项目，已在JDK6.0 update 7 中自带，能够监控线程、内存情况，查看方法的调用情况。

画面14：
标题：5.3.5 对比测试
内容：
- 对于官方的POI读取Excel与导出，共计论基于Excel2007对象模型，在Apache POI官方提供了对操作大数据量的导入导出的工具和解决方案，可以分为三种模式：
  - 用户模式：用户模式有许多封装好的方法操作简单，但创建太多的对象，非耗内存（之前使用的方法）。
  - 事件模式：基于SAX方式解析XML，SAX全称Simple API for XML，它是一个接口，也是一个软件包。它是一种XML解析的替代方法，不同于DOM解析XML文档时把所有内容一次性加载到内存中的方式，它逐行扫描文档，一边扫描，一边解析。
  - XSSFS对象：是用来生成或读取excel数据文件，主要原理是借助临时存储空间生成excel。
- 表格数据：
| API Type | eventmodel | usermodel | Streaming (as SAX) | In memory tree (as DOM) | Streaming (as SAX) | In memory tree (as DOM) | XSSFS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CPU and Memory Efficiency | Good | Varies | Good | Varies | Good | Good |
| Forward Only | Yes | No | Yes | No | Yes | No |
| Read Files | Yes | Yes | Yes | Yes | Yes | Yes |
| Write Files | No | Yes | No | Yes | No | Yes |
| Features | | | | | | | |
| create sheets / rows / cells | No | Yes | No | Yes | No | Yes |
| styling cells | No | Yes | No | Yes | No | Yes |
| delete sheets / rows / cells | No | Yes | No | Yes | No | Yes |
| shift rows | No | Yes | No | Yes | No | Yes |
| during sheets | No | Yes | No | Yes | No | Yes |
| formula evaluation | No | Yes | No | Yes | No | Yes |
| cell comments | No | Yes | No | Yes | No | Yes |

5) 无其他内容。

