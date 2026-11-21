# 12-POI的入门：绘制图形

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\12-POI的入门：绘制图形_【海量资源尽在 ubkz.com】.mp4
- 时长 10分52秒（音频 652s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经对单元格的样式呢做了一个处理那其实呢对于我们操作单元格呢还有这么一种比较特殊的情况就是说呢要把一张图片写入到这个Excel报表当中那针对图片的这个处理我们又该如何去做呢那我们接下来关注的就是如何向Excel当中添加一张图片好在这边呢跟之前的逻辑一样Ctrl C Ctrl Vcopy一个工程我们这边呢是第四个案例
[00:29] 好了那我们现在要做的事情就是向单元格当中插入图片那对于这个插入图片那我就不需要这么复杂的这些内容了不需要这些复杂内容了我们关注的就是有了一个shade之后向shade当中插入两图片那么要想去插入图片那应该如何去做呢首先我们应该把图片给它准备好没错吧那这个图片呢在今天资料当中呢也给各位随便的准备了一张Ctrl C
[00:59] 我把它放置到我们刚才的这个目录下放到这就这么一张传知博客的logo图片好了我们应该如何去对它进行处理首先第一件事我们应该叫做读取这张图片流读取我们的图片的数据流那读取到图片数据流接下来要做的事情要干嘛就是要把这个图片给它转化成二进制数组OK好了其实这个就是大同小异的一个过程
[01:40] 那这些如果都准备好了那其实我们的图片就基本上准备好了那只是把图片的流给它搞定了那图片流已经有了之后接下来我们要完成的这个就稍微有一点点复杂是在Excel当中它集中管理所有的图片它在内存当中集中管理那你如果想要保存一张图片你就需要把你的图片放到Excel它的图片的集合当中或者把它放到内存里面这个PY帮助我们统一管理
[02:09] 所以我们接下来要做的事情就是像我们的POI内存中添加一张图片它是内存管理的很多的图片如果你有十张它就十张那一会儿你要用到的时候你怎么就能定位到你要用第一张或者用第二张呢那这个时候你像POI内存当中添加图片的时候它会返回我们图片在图片在我们这个图片因为说过很多图片就是一个图片集合中的
[02:43] 下标或者所以OK那好了这些都已经准备好了内存当中已经有了图片已经加载进去了那接下来我们就关注如何把图片绘制到我们的一个表格当中那我们这边借助的是绘制图片的工具类那要借助它的图片工具类来进行绘制那这个图片工具类我们都已经准备好了之后那我们可以通过图片工具类创建
[03:15] 一个我们叫做绘图对象那这个绘图对象呢也是Excel里面独有的一些内容当然它都是PUI提供的那好了这些图片对象这是绘制图片的这个对象借助这个对象去开始真正真正的把图片画到我们的Excel报表当中那你画报表的时候往里画那究竟把这个图片插入到第几行它的位置是什么它的下标究竟设置到什么地方所以接下来要关注的就是创建我们叫做锚点
[03:44] 其实就是设置图片的坐标好了那这个坐标我们设置好了之后接下来才是真真正正的创建图片或者我们叫做绘制图片就是这么一个流程那我们接下来把这个代码呢给它填充过来首先呢就是一个图片流那这个图片流呢比较简单它是一个图片文件嘛所以我们用的是注意这回别跟刚才一样写错了FillInt
[04:15] input stream一个文件的输入流好了就比如说就叫stream了等于new一个fill input stream那这个图片呢我刚才已经把它copy到了我这边的文件夹里logo.gopd好了logo.gopdOK那这样一连呢我的图片流呢已经读取进来了那读取进来之后呢还应该把它转化成我们的二进制数组那转化成二进制数组这个比较简单
[04:48] PUI当中提供了一个工具类叫做IOUtilsPUI提供的工具类别选错IOUtils打点to byte read直接把流拿过来这样一来就能得到我们的二进制直接数组那得到数组之后把它读取进去stream.readby bytes好了那这样一来呢我们的
[05:25] bytes数组当中已经有了当前图片的二进字文二进字数组信息了那好了接下来我们关注的就是如何把一张图片放到我们的py的内存当中那这个呢比较简单wb我们的工作部那通过工作部打点叫做add有一个方法叫做pictureaddpicture那addpicture的时候呢注意它有两个参数参数一指的是我们图片的
[05:58] 二进制数组好了参数二指的是我们当前的这个图片的类型好了那接下来呢我们就可以往里进行填充by次好了那第二个参数呢在PUI当中呢其实它也是封装以美举的形式为我们提供的就是workbookworkbook哎各位来看第一个提示其实就有了就是picture tabgopgok那这样一来呢我们就会往内存当中压入了一张图片
[06:35] 那压入图片之后呢它会给我们返回一个我们图片所在的所有位置index好了那这样一来我们内存已经有图片那剩下就是想方设法的把图片给它绘制到我们的Excel报表那绘制的过程当中要借助它的工具类这个工具类如何获取WB还是我们的工作部工作部打点get我们叫做creation helper就是这么一个绘图工具
[07:07] 那这个绘图工具我们准备好了之后接下来就是关注如何去绘制一张图片了那绘制图片好了咱们是往某一个表格当中进行绘制那sheet打点create join就它那这样一来我的绘图对象也准备好了
[07:36] 好了会图对象准备好了之后接下来就是创建锚点就是其实设置图片的对付坐标那设置图片坐标我们如何去做借助helper它就能够帮助我们去做了那我们如何去做呢helper打点create clientclandclandcland就是它这是我们的一个锚点对象这个锚点对象它的主要目的是设置图片的坐标的那这个锚点做对象如何去创建呢就是根据我们的工具类来做
[08:05] 通过工具类创建锚点在锚点里面我们可以设置打点比如说可以设置setcol可以set row1那这个代表的什么含义呢就是说你这个图片要从第几行开始好了从第零行开始注意它是从零开始的好了还可以去设置我们的锚点打点setcolumn
[08:37] 这个1代表什么意思注意这个1代表是从谁开始那我们也是从0开始也就是说从第0个单元格从第0个从第0行第0个单元格进行绘制图形好了那我们的坐标已经搞定了接下来就是真真正正的把这个图片给它画出来那画出来呢可以借助我们刚才的绘图对象绘图对象打点createpicture就是真真正正的往里面去画了
[09:06] 那画图的时候呢注意我们首先呢是不是应该告诉他你画的这个图这个图片的究竟在什么位置那位置我们的锚点已经设置好了好了第一个参数就是你图片的位置那第二个参数是什么注意第二个参数指的是你刚才传到内存当中图片的我们叫做索引那这个索引叫做index那这样一来它其实就是
[09:38] 借助内存当中的这张图片二进制字符流把它写到相应的Excel在某一个位置当中其实就可以了当然了这样一来就能得到我们的一张图片得到图片之后它可以自适应你图片的相应的一些配置打点resist就可以了好了这个代表的是渲染自适应渲染图片好了这样一来我其实代表的含义是什么就是从
[10:15] 第0个单元格开始往里面保存一张图片OK那好了代码我们都已经搞定了我们可以运行一把抱歉啊这边是说了我这个生成的这excel是2啊因为我这个2其实刚才已经还打开着呢所以它有一个错误那我不要2了我叫3吧走好了这边呢执行成功我们来看一下3走各位来看从第0个格子开始创建创建创建哎绘制了这么一张图片OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apache POI 库在 Java 中向 Excel 文件插入图片。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Excel 文件界面，其中单元格 C15 内有文字“传智播客”，同时任务栏显示 IntelliJ IDEA 和 Excel 窗口。
画面2：IntelliJ IDEA 中展示 PoTest04.java 代码，创建了 Workbook 和 Sheet，设置单元格样式并写入“传智播客”。
画面3：显示“传智播客”网站的加载界面。
画面4：在 PoTest04.java 中，光标位于创建 FileInputStream 的位置，准备读取图片文件。
画面5：在 PoTest04.java 中，光标位于 FileInputStream 的声明后，准备读取图片文件。
画面6：在 PoTest04.java 中，光标位于创建 FileOutputStream 的位置，准备写入 Excel 文件。
画面7：在 PoTest04.java 中，光标位于创建 CreationHelper 的位置，准备创建绘图工具类。
画面8：在 PoTest04.java 中，光标位于创建 Drawing 对象的位置，准备创建绘图对象。
画面9：在 PoTest04.java 中，光标位于创建 ClientAnchor 对象的位置，准备创建锚点。
画面10：在 PoTest04.java 中，光标位于创建 Picture 对象的位置，准备绘制图片。
画面11：在 PoTest04.java 中，光标位于创建 Picture 对象的位置，准备绘制图片。
画面12：在 PoTest04.java 中，光标位于创建 Picture 对象的位置，准备绘制图片。
画面13：在 PoTest04.java 中，运行后出现异常，提示“另一个程序正在使用此文件，进程无法访问”。
画面14：展示 Excel 文件界面，其中单元格 C16 内有文字“传智播客”，同时任务栏显示 IntelliJ IDEA 和 Excel 窗口。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2：
```java
public class PoTest04 {
    public static void main(String[] args) throws Exception {
        //创建工作簿
        Workbook wb = new XSSFWorkbook(); //2007版本
        //创建表单sheet
        Sheet sheet = wb.createSheet("test");
        //样式处理
        CellStyle style = wb.createCellStyle();
        style.setBorderTop(BorderStyle.THIN); //上边框
        style.setBorderBottom(BorderStyle.THIN); //下边框
        style.setBorderLeft(BorderStyle.THIN); //左边框
        style.setBorderRight(BorderStyle.THIN); //右边框
        //设置字体
        Font font = wb.createFont();
        font.setFontName("华文行楷"); //字体
        font.setFontHeightInPoints((short)28); //字体大小
        style.setFont(font);
        //写入单元格
        Cell cell = row.createCell(i+2);
        cell.setCellValue("传智播客");
    }
}
```

画面4：
```java
FileInputStream stream = new FileInputStream(name: "E:\\excel\\poi\\logo.jpg");
```

画面5：
```java
byte[] bytes = IOUtils.toByteArray(stream);
```

画面6：
```java
FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test2.xlsx");
```

画面7：
```java
CreationHelper helper = wb.getCreationHelper();
```

画面8：
```java
Drawing<?> patriarch = sheet.createDrawingPatriarch();
```

画面9：
```java
ClientAnchor anchor = helper.createClientAnchor();
```

画面10：
```java
Picture picture = patriarch.createPicture(anchor, index);
```

画面11：
```java
Picture picture = patriarch.createPicture(anchor, index);
```

画面12：
```java
Picture picture = patriarch.createPicture(anchor, index);
```

画面13：
```java
Exception in Thread "main" java.io.FileNotFoundException: E:\excel\poi\test2.xlsx (另一个程序正在使用此文件，进程无法访问。)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

