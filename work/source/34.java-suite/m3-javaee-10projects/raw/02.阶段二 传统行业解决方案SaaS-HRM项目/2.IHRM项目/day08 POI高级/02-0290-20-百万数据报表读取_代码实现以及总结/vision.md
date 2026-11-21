# 画面线理解：20-百万数据报表读取：代码实现以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\20-百万数据报表读取：代码实现以及总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:42, 01:31, 02:14, 02:30, 03:16, 03:26, 03:46, 03:53, 03:59, 04:14, 04:47, 05:54, 06:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:17:48

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
