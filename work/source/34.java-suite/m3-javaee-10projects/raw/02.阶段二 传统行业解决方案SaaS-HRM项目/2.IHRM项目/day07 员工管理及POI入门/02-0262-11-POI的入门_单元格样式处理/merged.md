# 11-POI的入门：单元格样式处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\11-POI的入门：单元格样式处理_【海量资源尽在 ubkz.com】.mp4
- 时长 12分22秒（音频 743s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们已经把内容写到这个单元格当中了但是呢其实在某些情况下对于这个单元格呢可能还有一个样式的一个要求比如说呢我就以这边的举例我这边可以对它进行一个处理那首先呢我就给它加上一个框线那加这个框线呢可以加上下左右等等都可以加好了所有都有那比如说呢除了这个之外呢还可以比如说可以给它设置这个字体比如说呢这个字体呢我就给它设置成28号字
[00:31] 好了叫做随便来一个吧就来一个华文型凯好了那这个我们看过了之后那就是说呢对于这个字体你会发现啊它太长了那我可以给它设置一下比如说呢叫做列宽好了列宽我就给它设置成比如说31OK那还有比如说我还可以给它设置航高那航高比如说给它设置成50哎OK那这玩意儿搞定了还有一个就是说呢
[01:01] 对于这一个SEL可能还有要求那比如说水平去重OK那针对这种比较特殊的这种样式我们又该通过PUI如何进行处理呢好了那接下来我们来看一下如何去做打开我们的代码通过之前的案例Ctrl C Ctrl V Copy这是我们今天的第三个案例那这个第三个案例我们重点围绕的就是单元格样式
[01:32] 那对于这个单元格样式处理来说首先注意工作部必须得有sheet必须都有那同时呢行对象单元格对象都要有我们关注的是不是就是这个单元格当中的样式以及这个传制博客它的字体啊那对于这个单元格样式处理如何去做那接下来我们关注的就是样式处理那这个样式处理首先那这个样式对象我们应该获取到好了创建样式对象
[02:05] 那样式对象创建好了之后我们还可以设置字体所以我们要设置创建我们的字体对象那好了我们一个一个来看那创建样式对象这个样式对象其实是我们单元格的相关的功能所以我要通过wb单元格打点打点create注意sell styleOK那这样一来我的样式对象创建好了
[02:32] 那创建好了之后我们关注一下刚才我们这个案例这个单元格里面呢首先有边框那我们处理边框那边框怎么处理它是样式的一部分所以样式打点set好了我们set它是边框边框呢其实翻译成英文呢就是border那各位来看这边有border什么topborderbottom还有border leftborder right等等所以我们一个一个来设置就可以了
[03:03] 好了这边设置我们的上边框上边框当然了除了上边框下边框左边框右边框都有那里面设置的值是什么注意用的是border style那这个border style里面全部都是我这个边框的一些枚举的一些类型啊比如说我用个比较细的一条细线c当然你想用什么都可以这些呢你可以一个一个去试啊去试就可以了好了这边呢我随便来一个打点哎就它了
[03:41] 细线好了除了上面框之外呢我们还可以去设置它的下边框等等打点set border bottom好了同样的细线好了呢还有set点setleft点setright里面的值基本都是一样的咱们都用细线就可以了Ctrl C Ctrl V哎上边框下边框左哎和右OK
[04:21] 那边框我们已经搞定了那接下来呢就是说呢我们还有一个字体那对于这个字体如何去做呢其实也是创建一个字体对象那这个字体对象同样也是通过我们这个工作部来创建的打点create各位会发现对于皮卧来说它有一个特点需要什么对象create创建出来就可以那字体对象create font
[04:50] OK那字体对象已经有了那接下来呢就可以设置比如说呢font打点set font name可以设置你这个字体究竟叫什么我们刚才举的案例字体呢叫做华文型凯Ctrl C拿过来Ctrl V那这样一来字体设置好了那还可以设置它的字号打点好了set font high end point
[05:18] 这个其实设置就是字号需要各位注意啊这个字号里面接收的是short类型的我做一个转型28刚才我们设置的就是28这个设置字体好了这边字号ok字号ok那好了这个字体这些我们创建好了那创建好了之后还没有设置到单元格里面所以我们接下来要做的事情style打点set font把方对象创建
[05:51] 放进去其实就可以了那这样一来边框已经有了字体其实也已经处理好了那这些处理好了之后注意我们刚才是不是设置还设置过航高和列宽呀那航高和列宽处理好了之后接下来还有一个我们还设置了一个叫做居中显示那针对这些又是如何去做的呢我们来看一下那航高和列宽它其实是两个不同的类型首先航高
[06:25] 航高其实就是对某一航进行设置所以是肉肉打点打点我们叫做set high poundshigh in pounds好了这个航高我们刚才设置的是50所以我这边设置50即可除了航高是不是还应该有一个叫做列宽列宽大家都知道列就是sheet抱歉
[06:59] 这个列宽不是sheet创建的不是我们叫做cell创建的是通过sheet创建的sheet打点setcolumn widthok好了设置列宽需要跟各位做一个简单的说明了设置一个列宽刚才我发现它是通过sheet来创建sheet创建创建的列宽组合去做sheet是整个表单我们是不是要定位到某一列再去设置它的宽度
[07:33] 所以我关注的就是012我就要对第二列设置宽度这个宽度如何去设置注意这边我们刚才可以看一下列宽叫做31各位来看我如果写31的话其实它就有问题了为什么有问题我们可以点进它代码当中和各位做一个简单的说明这个是没有关联源它是自动下载的这个没有没有的话我简单的说一下设置的列宽
[08:08] 宽度它其实指的是字符宽度那这个字符宽度呢其实和我们常见的这个和我们刚才Excel这边设置的31它不是一个内容但是它相似那看一下它的原码是如何处理的各位来看你如果传递一个宽度的话它底下会对这个宽度除以256那所以如果对于我们来说想要设置31个字符宽度那怎么做
[08:39] 那很简单我们可以设置成31是不是去乘以256那这个乘法各位应该都会一乘再除是不是就没有了所以对于我们来说设置宽度这边一定要注意31要乘以256OK那这样一来我们这个行高和列宽已经搞定了接下来就是一个居中显示那对于这些居中显示来说其实就是设置我们单元格的样式上面的一些内容那居中显示很简单了
[09:09] 按sell打点我们可以设置set我们先来一个叫做水平居中那水平居中里面填的内容应该是什么呢注意好了各位来看这边其实就是对于水平居中它里面的一些可以选择的我们打开来看其实是可以选择的一些美举比如说呢我想让左边我想让它居中我想让它以右边那怎么去选择我们就用美举点center我们是水平居中OK好了那接下来呢
[09:45] 这边写点注释啊水平居中水平居中那除了水平居中呢还有一个垂直居中垂直居中同样的道理打点再打Varity哎没错就是它里面写的内容呢基本上都是大同小异的OK那这样一来我们就已经垂垂直垂
[10:20] 直居中OK那这样一来呢我们就已经把这个样式处理其实已经搞定了各位会发现其实对于Excel来说操作很简单难得其实就是它的样式好了我们来走去创建一个哦抱歉在这边呢我给它来一个就是Test2了Test2来走OK创建好了我们打开来看一下Test2打开各位来看好了大家会发现呢这个已经创建出来了但是
[10:52] 它只有航高和这个列宽也就是这个样式还没有啊我们检查一下代码好了这边回来呢可以做一个简单的查看把它关掉那各位来看呢就是说呢我这个样式呢已经创建出来了但是这个样式还没有设置到这个格子里吧那所以接下来呢就是说呢我们就是像单元格设置样式单元格设置样式那这个比较简单
[11:25] 是我们刚才设置的单元格打点set still它真有好了那我们把样式放进去OK再去重新生成一下走好了我们直接找到我们生成的一个sell打开各位来看这样一来呢我们这个单元格就已经设置好了和我们刚才这个大同小异大同小异但是呢还是有差距的
[11:58] 差距在哪我跟各位说一下差距就在列宽我们现在的列宽是31但是通过我代码生成的这个列宽各位来看30.38我们刚才说过了这个列宽POI处理的有一点点问题POI是以字符宽度来做的而我们在这里面真正的其实是以像素宽度来做的所以它有不同的地方OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
使用 Apache POI 库在 Java 中创建并格式化 Excel 文件，包括设置单元格边框、字体、对齐方式等样式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Excel 文件，单元格 C3 中有文字“传智播客”，用于演示最终生成的文件效果。
画面 2: 在 IntelliJ IDEA 中打开 `PoTest03.java`，代码中创建了 `HSSFWorkbook`，并设置了单元格值“传智播客”，但未设置样式。
画面 3: 查看 `BorderStyle.class` 的反编译代码，展示边框样式常量定义，如 `THIN`, `MEDIUM`, `THICK` 等。
画面 4: 在 `PoTest03.java` 中，为 `CellStyle` 设置边框样式，使用 `BorderStyle.THIN` 设置上下左右边框。
画面 5: 在 `PoTest03.java` 中，为 `CellStyle` 设置字体，使用 `Font` 类设置字体名称为“华文行楷”，字号为 28。
画面 6: 在 `PoTest03.java` 中，设置单元格对齐方式，使用 `style.setAlignment(HorizontalAlignment.CENTER)` 设置水平居中，`style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER)` 设置垂直居中。
画面 7: 在 `PoTest03.java` 中，设置行高和列宽，使用 `row.setHeightInPoints(50)` 设置行高，`sheet.setColumnWidth((short)2, (short)(31 * 256))` 设置列宽。
画面 8: 展示 Excel 文件，单元格 C3 中有文字“传智播客”，单元格 C5 有绿色边框，用于演示设置边框后的效果。
画面 9: 查看 `XSSFSheet.class` 的反编译代码，展示与列宽和隐藏相关的逻辑。
画面 10: 在 `PoTest03.java` 中，设置单元格对齐方式，使用 `style.setAlignment(HorizontalAlignment.CENTER)` 设置水平居中，`style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER)` 设置垂直居中。
画面 11: 在 `PoTest03.java` 中，设置行高和列宽，使用 `row.setHeightInPoints(50)` 设置行高，`sheet.setColumnWidth((short)2, (short)(31 * 256))` 设置列宽。
画面 12: 在 `PoTest03.java` 中，设置单元格对齐方式，使用 `style.setAlignment(HorizontalAlignment.CENTER)` 设置水平居中，`style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER)` 设置垂直居中。
画面 13: 在 `PoTest03.java` 中，代码已完整，运行后在终端显示“Process finished with exit code 0”，并展示 `day/` 和 `poi/` 目录结构。
画面 14: 展示 Excel 文件，单元格 C3 中有文字“传智播客”，单元格 C5 有绿色边框，用于演示设置边框后的效果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
public class PoTest03 {
    public static void main(String[] args) throws Exception {
        //创建工作簿 HSSFWorkbook - 2003版本
        Workbook wb = new HSSFWorkbook();
        //创建表单 sheet
        Sheet sheet = wb.createSheet("test");
        //创建行对象，参数，索引（从0开始）
        Row row = sheet.createRow(1);
        //创建单元格对象，参数，索引（从0开始）
        Cell cell = row.createCell(1);
        //把单元格写入内容
        cell.setCellValue("传智播客");

        //样式处理
        //创建样式对象
        CellStyle style = wb.createCellStyle();
        //设置边框
        style.setBorderTop(BorderStyle.THIN); //上边框
        style.setBorderBottom(BorderStyle.THIN); //下边框
        style.setBorderLeft(BorderStyle.THIN); //左边框
        style.setBorderRight(BorderStyle.THIN); //右边框

        //创建字体对象
        Font font = wb.createFont();
        font.setFontName("华文行楷"); //字体
        font.setFontHeightInPoints((short)28); //字号
        style.setFont(font);

        //行高和列宽
        row.setHeightInPoints(50); //行高
        sheet.setColumnWidth((short)2, (short)(31 * 256)); //列宽

        //刷出显示
        style.setAlignment(HorizontalAlignment.CENTER); //水平居中
        style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER); //垂直居中

        //文件流
        FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test1.xlsx");
        //写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 3:
```java
package org.apache.poi.ss.usermodel;

public enum BorderStyle {
    NONE(0),
    THIN(1),
    MEDIUM(2),
    DASHED(3),
    DOTTED(4),
    THICK(5),
    DOUBLE(6),
    HAIR(7),
    MEDIUM_DASHED(8),
    DASH_DOT(9),
    MEDIUM_DASH_DOT(10),
    DASH_DOT_DOT(11),
    MEDIUM_DASH_DOT_DOT(12),
    SLANTED_DASH_DOT(13);

    private final short code;
    private static final BorderStyle[] _table = new BorderStyle[14];
    private BorderStyle(int code) { this.code = (short)code; }
    public short getCode() { return this.code; }
    public static BorderStyle valueOf(short code) { return table[code]; }
}
```

画面 4:
```java
public class PoTest03 {
    public static void main(String[] args) throws Exception {
        //创建工作簿 HSSFWorkbook - 2003版本
        Workbook wb = new HSSFWorkbook();
        //创建表单 sheet
        Sheet sheet = wb.createSheet("test");
        //创建行对象，参数，索引（从0开始）
        Row row = sheet.createRow(1);
        //创建单元格对象，参数，索引（从0开始）
        Cell cell = row.createCell(1);
        //把单元格写入内容
        cell.setCellValue("传智播客");

        //样式处理
        //创建样式对象
        CellStyle style = wb.createCellStyle();
        //设置边框
        style.setBorderTop(BorderStyle.THIN); //上边框
        style.setBorderBottom(BorderStyle.THIN); //下边框
        style.setBorderLeft(BorderStyle.THIN); //左边框
        style.setBorderRight(BorderStyle.THIN); //右边框

        //创建字体对象
        Font font = wb.createFont();
        font.setFontName("华文行楷"); //字体
        font.setFontHeightInPoints((short)28); //字号
        style.setFont(font);

        //行高和列宽
        row.setHeightInPoints(50); //行高
        sheet.setColumnWidth((short)2, (short)(31 * 256)); //列宽

        //刷出显示
        style.setAlignment(HorizontalAlignment.CENTER); //水平居中
        style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER); //垂直居中

        //文件流
        FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test1.xlsx");
        //写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 5:
```java
//创建样式对象
CellStyle style = wb.createCellStyle();
//设置边框
style.setBorderTop(BorderStyle.THIN); //上边框
style.setBorderBottom(BorderStyle.THIN); //下边框
style.setBorderLeft(BorderStyle.THIN); //左边框
style.setBorderRight(BorderStyle.THIN); //右边框

//创建字体对象
Font font = wb.createFont();
font.setFontName("华文行楷"); //字体
font.setFontHeightInPoints((short)28); //字号
style.setFont(font);

//行高和列宽
row.setHeightInPoints(50); //行高
sheet.setColumnWidth((short)2, (short)(31 * 256)); //列宽

//刷出显示
style.setAlignment(HorizontalAlignment.CENTER); //水平居中
style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER); //垂直居中

//文件流
FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test1.xlsx");
//写入文件
wb.write(pis);
pis.close();
```

画面 6:
```java
//创建样式对象
CellStyle style = wb.createCellStyle();
//设置边框
style.setBorderTop(BorderStyle.THIN); //上边框
style.setBorderBottom(BorderStyle.THIN); //下边框
style.setBorderLeft(BorderStyle.THIN); //左边框
style.setBorderRight(BorderStyle.THIN); //右边框

//创建字体对象
Font font = wb.createFont();
font.setFontName("华文行楷"); //字体
font.setFontHeightInPoints((short)28); //字号
style.setFont(font);

//行高和列宽
row.setHeightInPoints(5

