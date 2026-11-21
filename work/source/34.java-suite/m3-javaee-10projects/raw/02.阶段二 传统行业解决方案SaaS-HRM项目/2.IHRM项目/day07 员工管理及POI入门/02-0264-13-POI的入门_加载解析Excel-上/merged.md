# 13-POI的入门：加载解析Excel-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\13-POI的入门：加载解析Excel-上_【海量资源尽在 ubkz.com】.mp4
- 时长 10分56秒（音频 657s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那刚才呢和各位一直来聊的其实都是如何去创建一个Excel报表那其实我们刚才说过了对Excel报表来说除了去把数据写入到报表去创建一个报表之外还有一种情况就是把一个已经提供好的报表的内容给它读取出来接着去完成我们的业务操作那接下来呢我们能关注的就是这个入门操作里面最后一项就是如何把Excel
[00:28] 加载到我们的内存当中接着解析它获取里面的数据好了在这边呢我在今天的资料当中已经给各位准备好了这么一个小小的demo.xls这么一个文件那打开它各位来看这个是我们基本的一个Excel报表那这个Excel报表里面有这么几条数据I1234有序号姓名年龄等等等等这么几列那我们要做的事情关注的是不是就是
[00:58] 这四列里面的内容没错吧所以接下来我们来看一下如何通过Excel获取如何通过PUI获取到Excel当中的叫做内容或者我们的数据好了我们打开我这边的idea把这些呢没用的全部都关掉了那好了右键创建一个我们的class我叫做POI test05好了这个里面我们关注的是什么就是
[01:30] 读取excel并解析好了同样的跟之前一样psvm我们的闷方法进行测试那接下来我想跟各位来聊的就是说对于这边解析和创建的其实就不太一样了那我们要做的事情呢也需要跟各位要交代清楚那么要做的事情第一件事那不管要用不管是这个excel如何去使用
[01:58] 那我们通过PUI操作永远的别忘了应该就相当于先得到Workbook就是我们的工作簿得到工作簿接下来是不是拿到里面的sheet拿到里面的行拿到里面的我们叫单元格是不是就可以了这个跟刚才正好不太一样刚才我们是创建现在是不是叫做获取所以我们要做的事情就集中在如何去获取了首先第一件事就是根据我们的excel文件
[02:27] 创建工作部就是我们的Workbook因为我们现在是真的有一个文件啊好了那接下来第二件事那我们有了工作部之后我们要去获取叫做sheet那这个我们的表单那这个表单其实我们拿到的第一个第一页其实就可以了好那这个呢sheet我们拿到了之后接下来第三件事第三件事我们就可以获取我们叫做sheet
[03:02] 中的每一行和叫做每一行和每一个单元格的叫做内容了好了接下来我们来看一下如何去完成它根据Excel文件创建工作部这个比较简单工作部叫做Workbook大家会发现不管是自己创建一个Excel还是读取Excel工作部是最核心的这么一个API文档
[03:31] 或者一个API好了WB等于还是跟之前一样我们现在创建的是2007的XSS Workbook那需要跟各位声明一下这个XSS Workbook我为什么要写它呢是因为我这个Excel它真的是2007的如果你做测试的时候你是2003的你可别写XSSF我们是不是应该改成HSSF
[03:58] OK那好了这里面呢其实它可以接收一个我们叫做构造方法这构造方法里面有一个三数指的就是你这个Excel文件它的路径那我们的Excel文件路径呢在这边Ctrl C我把它拷过来叫做demo我也拷一下吧Ctrl C拷币过来好了这边呢会有一个小小的异常我做一个比较懒的一个处理直接抛出一个最大的就可以了
[04:27] 好了那这样一来工作部我们已经搞定了那搞定了之后我们要去根据工作部去获取或者读取到我们的这一个这一页吧就这一页那这一页呢各位可以发现我们的真正的一个Excel文档其实可能有很多恶事有很多那我们现在拿到的是第一页没错吧所以我们这边也可以根据我们叫做索引的形式
[04:50] 获取到我们的sheet那如何去做就是wb注意我们之前创建crate现在可不是创建了我们贬成获取就是get sheet好了注意get sheet我们用的是第二个方法get sheet at这个at里面接收一个我们叫做参数这个参数指的就是你sheet的索引好了对于我们来说呢索引一般都是从0开始的所以我写一个0ok那这样一来那这样一来我们的sheet已经获取到了
[05:25] 那获取到了之后我们接下来关注的其实就是拿到里面的每一行拿到里面的每一个格子那这里面的代码我们就设计到要进行我们叫做要进行循环因为里面的行内容有很多有很多行那有很多行那这边我们开始进行循环那循环的时候如何去做好了for循环先写好for循环
[06:00] 好了那这个里面我们要得到里面的叫做每一行那这个呢我就不这样写了我就开始int我叫row number吧row number等于注意等于0好了那接下来呢这里面row number小于那小于什么注意sheet打点get lastrow number那别叫sheet at了就叫sheet吧好了那这个代表什么意思可不可以解释一下这个代表的是获取
[06:37] 到最后一行那也就意味着我们现在这边呢0 1 2 3 4那它代表的get sheet这row number其实就是5因为最后一行是5那所以我写一个小于应该没问题没从0咱们今天一会要获取的时候其实所以从0开始的那这样一来OK我已经开始循环那我们i就是row number++那row number++那我们如何去
[07:09] 得到里面的每一行那得到每一行比较简单通过sheet打点get row那get row里面得到的其实写的就是根据索引根据索引叫做获取每一行好了那索引就是row numberOK那这样一来我们就能得到每一行的内容好了那这样一来呢我们开始循环我的思路其实这样从上面一行一行的拿一行一行的拿拿到之后
[07:42] 拿到第一行我们是不是再通过第一行得到里面的每一列的内容是不是就可以了所以接下来呢我们关注的列也有很多所以各位大家想到了也需要一个我们叫做循环那这个循环里面呢先来一索引这索引就是cell number好那这个cell number呢比如说你也可以写从零开始好那cell number小于什么
[08:12] 注意这边有朋友说了你可以获取到最大的行是多少那你能不能获取到最大列呢那最大列当然也可以了那通过row打点get last cell number这个其实就是得到最大的单元格的数量那好了接下来呢我们就可以cell number加加好了那这里面呢我们要干什么呢就是说我们根据索引获取每亿
[08:49] 个单元就是单元格那单元格如何获取呢sell等于肉打点get那这样一来就能根据所以获取到每一个单元格的内容了那当然有朋友说呢你会发现啊我所以是从零开始的比如说我以第一行为例第一行为例所以从零一
[09:25] 大家会发现01全都是空对于我们来说没什么含义那我可不可以直接从第三列拿呢那当然也可以那我们如何去做注意cell number从0我不从0了这不是0吗这不是1吗这不是2吗所以我从2开始获取哪有数据的是不是也可以啊OK那好了这样一来呢我们单元格的数据呢咱们就单元格呢已经获取到了那接下来我们关注的其实就是获取
[09:55] 每一个单元格的内容即可好了我想做的事情其实比较简单我获取到每一个单元格的内容之后把它拼接出来并且打印即可好了这边我用一个StringBuilder等于new一个我们叫做StringBuilder好了中间如何获取我们一会再说一会再说我先把我基本的结构给它写出来里面打印一下打点ToString即可各位来看
[10:28] 第一层放学款我们重点是不是就是获取每一行那每一行里面的有很多列那这些列所有给它拼接出来进行打印就可以了那我做到的效果拿到每一行通过每一行里面构造里面所有内容打印构造所有内容打印这个就是我想要的一个效果那接下来我们关注的问题就是如何获取每一个单元格的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apache POI 库读取 Excel 文件并遍历单元格内容。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目目录结构，包含多个 Excel 文件（demo.xlsx, test1.xlsx, test2.xlsx, test3.xlsx）和一个图片文件（logo.jpg）。
画面2：在 IntelliJ IDEA 中展示 PoITest04.java 代码，用于插入图片到 Excel 文件。
画面3：在 Excel 中展示多个窗口的嵌套视图，包括 Excel 文件、IDEA 项目、PDF 文档等。
画面4：在 Excel 中展示 demo.xlsx 文件内容，包含姓名、年龄、家庭住址、出生日期等数据。
画面5：在 IntelliJ IDEA 中展示 PoITest05.java 代码，用于读取 Excel 文件。
画面6：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在获取 Sheet 对象。
画面7：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在遍历行和单元格。
画面8：在 Excel 中展示多个窗口的嵌套视图，包括 Excel 文件、IDEA 项目、PDF 文档等。
画面9：在 Excel 中展示 demo.xlsx 文件内容，包含姓名、年龄、家庭住址、出生日期等数据。
画面10：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在遍历行和单元格。
画面11：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在获取单元格。
画面12：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在遍历行和单元格。
画面13：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在获取单元格内容。
画面14：在 IntelliJ IDEA 中展示 PoITest05.java 代码，正在打印单元格内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```java
public class PoITest04 {
    public static void main(String[] args) throws Exception {
        //创建工作簿
        HSSFWorkbook wb = new HSSFWorkbook(); //2007版本
        //创建表单
        Sheet sheet = wb.createSheet("test");

        //读取图片流
        FileInputStream stream = new FileInputStream(name: "E:\\excel\\poi\\logo.jpg");
        //转化二进制数组
        byte[] bytes = IOUtils.toByteArray(stream);
        //向内存中添加一张图片，该图片在图片中包含的全部
    }
}
```

画面5代码：
```java
package cn.itcast.poi.test;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.IOException;

public class PoITest05 {
    public static void main(String[] args) throws Exception {
        //1.根据excel文件创建工作簿
        Workbook wb = new XSSFWorkbook(path: "E:\\excel\\poi\\demo.xlsx");
        //2.获取Sheet
        Sheet sheet = wb.getSheetAt(0); //参数：索引
        //3.获取Sheet中的每一行，和每一个单元格
    }
}
```

画面6代码：
```java
Sheet sheetAt = wb.getSheetAt(0); //参数：索引
```

画面7代码：
```java
for (int rowNum = 0; rowNum < sheet.getLastRowNum(); rowNum++) {
    Row row = sheet.getRow(rowNum); //根据索引获取某一行
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum);
    }
}
```

画面10代码：
```java
for (int rowNum = 0; rowNum < sheet.getLastRowNum(); rowNum++) {
    Row row = sheet.getRow(rowNum); //根据索引获取某一行
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum);
    }
}
```

画面11代码：
```java
Cell cell = row.getCell(cellNum);
```

画面12代码：
```java
for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
    Cell cell = row.getCell(cellNum);
}
```

画面13代码：
```java
StringBuilder sb = new StringBuilder();
for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
    Cell cell = row.getCell(cellNum);
    //获取每一个单元格的内容
}
```

画面14代码：
```java
System.out.println(sb.toString());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

