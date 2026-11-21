# 09-POI的入门：概述和创建EXCEL

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\09-POI的入门：概述和创建EXCEL_【海量资源尽在 ubkz.com】.mp4
- 时长 12分20秒（音频 741s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 刚才呢我们对这个Excel报表做了一个简单的说明我们也说过了在Java当中呢可以使用PUI来操作Excel报表到了接来呢我们就可以一起来研究一下对于PU来说如何使用去操作我们的Excel那好了那在这边呢去玩一个Excel的一个入门的操作那不管做什么操作首先就是搭建环境导入相应的坐标
[00:32] 好了在这边我去创建一个新的工程咱们专门去玩一下我们的POI报表好了这边创建一个project我个人习惯的创建一个空的project好了点击next这个project的名称我们叫什么可以给它就叫做poi-test好了创造到什么位置就跟我们这边的保持一致就可以了workerspace hrmpoi
[01:07] 名称保持一致OK没问题好了点击finish让它去帮助我创建一个空的工程新的界面打开好了这边创建好了这么一个空的工程接下来我去创建一个我们叫模块new一个model好了没问model想都不要想接着点击next那好了在这边我们就比如说cn.itcastartifactid好了叫做poi-demo
[01:42] 这是我个人习惯用了一个中线py-demo没问题finish好了接下来这个工程创建好了导入箱子坐标这个坐标在今天资料当中在这边都有给各位也准备好了里面需要用到三个坐标Ctrl-C copy过来copy过来dependence这三个坐标先简单的跟各位做一个说明首先第一个我们用到的py是最新的版本4.0.1
[02:15] 4.0.1那第一个坐标呢其实是PUI它的核心坐标核心坐标好了第二个我们说过了对于现在来说呢Excel呢两个版本2003和2007那对于2007版本它其实是基于XML的这种形式来做的所以这玩意儿是对2007的一个支持那我这边呢也做一个简单的说明现在用2007比较多所以我们之后的案例呢全部都是基于2007的形式来做的所以导入的2007相应的
[02:44] 两个依赖坐标好了这两个依赖坐标我们也导入进来了那好了接下来我们就可以写一些代码来去生成Excel玩一下如何去做那在我们正式去写这个代码之前呢我们需要和各位呢简单的声明一下就是说呢比如说我自己要想去用手动的方式去创建Excel应该如何去做好了比如说呢我想去在我的一盘创建
[03:14] 一个Excel好了在里面我就可以右键创建一个我们叫做Excel文档Excel报表好了给它起一个名字叫做TestXLSX因为我刚才说过了我们现在都是使用2007这个版本好了接下来呢打开它比如说呢在这边我就可以去写一句话传至博客好了需要各位注意的这个其实不是说我教各位怎么去用Excel是这样的就是说呢对于
[03:47] POI来说它其实去生成一个cell和我们自己去用手动的方式其实大同小异差不多首先在这边我生成了一个报表接下来在报表里面各位这个是不是相当于第一个我们叫做sheetOK好了这个sheet也可以给它改一个名字接下来我们关注到了第一第二第三行在第三行里面找到了我们叫做第三个格子在第三个格子里面是不是输入了一点点内容
[04:18] 好了那接下来呢这个呢是我们手动操作和各位知道了对于我们要操作一个Excel来说手动的你要去创建这么一个报表接着里面创建一个sheet好了接着在里面创建一个行接着在里面找到一个格子里面写内容那对于用PUI操作差不多那在这边呢和各位简单的写代码之前说一下对于PUI操作Excel它呢有很多个API
[04:44] 这几个API非常典型和我刚才的操作一模一样首先第一个叫做Workbook那Workbook是什么它叫做工作部也叫做Excel文档对象所以这个Workbook一出厂意味着这么一个Excel文件创建出来那好了接下来它还有第二个这个对象就叫做Sheet那这个Sheet就是我们Excel的表单对象或者把它理解为我们当前的这一页那接下来第三个Row
[05:13] 那肉指的是Excel当中的一行刚才我说过了123第三行没错吧好了通过第三行我们是不是能找到第三也就是C这个格子好了各位来看格子Sale那好了剩下的事情就是这个格子里面你可以给它来一点点样式也可以给它设置比如说字体那不管是样式还是字体也是通过对象的形式来做的字体Font样式就是SaleSale
[05:42] 那所以呢通过刚才自己创建一个Excel形式和各位有一个类比大家都知道了这个APIWorkbookSheetRowCellFont还有CellStyle究竟什么意思好了这些和各位做过介绍之后那接下来我们就可以去创建一个Excel来跟各位来看一下如何去做打开我们的代码好了我就写到Test下了右键的创建一个Class
[06:12] cn.itcast.poi.test.比如说呢我就叫做poi test01OK好了这个里面我们要做的事情呢很简单我写一点点简单的注释要干嘛呢就是借助使用poi创建一个excel那如何去做呢很简单我这边呢使用闷方法的形式给各位来做说明好了对于我们这个闷方法来说首先我们要做的事情呢
[06:47] 第一件事叫做创建一个工作部好了创建了工作部接着第二件事我们要做做创建表单好了这些我们都做好了之后接着我们第三步那这样一来一个工作部有了里面有一页这个有了之后我们就可以把它输出出来也就是写入到文件里那在写入
[07:17] 文件那我们都知道对于写入文件呢其实我们是通过流的形式来做的所以这边呢还需要我们获取一个我们叫做文件流OK那好了接着我们一起来看一下如何去做好了创建一个工作簿很简单创建工作簿很简单那我们刚才知道了工作簿叫做Workbook好了WB好了那这个Workbook呢注意它是一个接口各位打开来看它是一个接口
[07:48] 那对于这个接口呢有很多个实现它有很多个实现好了我们一起来看一下用一下快捷键好了各位来看这个接口呢有很多个实现类其中有HSSF Workbook其中有SXSSF还有一个什么这些比较绕口还有一个XSSF那针对这几个究竟代表的什么意思各位也需要和各位做一个交代
[08:15] 那打开我们的讲义各位可以看一下在上边呢这边呢有一个它的结构说明刚才我说过很有好几个绕口的什么HSSF什么XSSF那这些它代表的含义是什么只要涉及到HSSF它其实操作的就是XLS这种格式说白了这个玩意儿操作的是我们2003版本那只要涉及到XSSF那各位来看它是我们OOXMLXLX
[08:45] 也就是这玩意操作的是我们的2007版本没错吧那这些我们看过了之后各位我们要做的事情就比较明确了那我们要创建一个等于new一个那我们用的是XSSFWorker好了那这样一来我们创建的其实就是2007版本好了这边也给各位简单的写一下SSFOK好了它是2003版本那我们现在创建的其实就是2007版本
[09:24] 那好了我们创建好了一个工作部那接下来呢我们就可以通过这个工作部里面去给它创建一个表单sheet其实就意味着我们这边可以起一个表单叫做test好了那接下来怎么做呢很简单只有在工作部里面是不是才有这个sheet这个表单啊所以我这边工作部打点它有一个方法叫做create我们创建的是什么sheet
[09:50] 那创建sheet两个方法第二个呢可以接受一个死菌类型的参数哎没错就是我们这个表单它的名称好了那这样一来我们这个sheet其实也就已经哎创建好了那创建好了之后我们就可以把这个简单的这个一个cell报表搞定了那我们接下来关注的就是如何把它输出保存下来那输出保存比较简单的就是用一个文件流就可以了fill output stream好了比如说我就叫做fis等于new一个fill output stream
[10:20] 好了接下来就是说呢我们可以把它保存到什么位置啊这个保存到什么位置我们一会再说好了那接下来保存到哪呢我们可以把它保存到我们刚才给各位举例的excel这个文件夹下可以给它创建一个叫做py下放到这里面好了这个目录这个地址呢我call一下control c贴到这边好了给它起一个名字就叫做txt.注意后缀名别写错xlsx2007万本
[10:51] 那好了文件流我们已经有了剩下的事情这个文件流里面现在所有内容都是空啊我们的流在哪呢工作部里面都有我们只需要把工作部里面的流信息写入到我的文件流就可以了打点retctrl c拿过来ctrl vok那好了这样一来呢我们这个基本的代码就写好了那其实还有一项各位千万别忘了各位千万别忘了这边抱歉抱歉这个写错了
[11:27] 这输入点我们应该用output streamoutput stream应该是一个输出文件流吧好了那接下来呢我们最后千万有一步别忘了就是要把这个流关闭啊ps.好了我们叫做clone好了那这样一来我这个第一个最基本的代码咱们已经搞定了那好了我就可以执行问方法走好了这边呢已经执行成功了并且没有包错那各位我们关注一下刚才我们生成的这个文件好了
[12:03] 一盘下Excel下的PUI下来了一个textOK打开给我来看这两个重名了好了把这个关掉了那我们来看走你会发现创建了这么一个工作部并且它是一个名词叫做testOK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Apache POI 库在 Java 中创建和读取 Excel 文件，包括环境搭建、依赖配置、API 结构说明和基本操作示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面“3 POI的入门操作”，其中包含 POI 依赖的 Maven 配置代码块。
画面 2: 在 IntelliJ IDEA 中打开名为 “ihrm_parent” 的项目。
画面 3: 在 IntelliJ IDEA 中点击“File”菜单，准备进行项目设置或新建操作。
画面 4: 在 Notepad++ 中显示 POI 依赖的 Maven 配置代码，光标位于最后一个 </dependency> 标签后。
画面 5: 显示 Windows 桌面，桌面上有 “黑马程序员” 和 “博学谷” 的标志。
画面 6: 在 Windows 资源管理器中，显示 “excel” 文件夹，其中包含一个名为 “test.xlsx” 的文件。
画面 7: 展示 PPT 页面“3.4 基本操作”，其中包含一个表格，列出了 POI 的主要 API 及其对应含义。
画面 8: 在 PPT 页面“3.4 基本操作”上，鼠标悬停在 “CellStyle” 项上，同时任务栏中显示一个 IntelliJ IDEA 的窗口。
画面 9: 在 IntelliJ IDEA 中，显示 POI 的 Workbook 接口的反编译代码，其中包含常量定义和方法声明。
画面 10: 在 IntelliJ IDEA 中，显示 POI 的 Workbook 接口的反编译代码，鼠标悬停在 “XSSFWorkbook” 类上，下方显示其依赖的 Maven 依赖项。
画面 11: 在 Microsoft Excel 中，显示一个名为 “test”的工作簿，其中 A3 单元格包含文本“传智播客”。
画面 12: 在 IntelliJ IDEA 中，显示 Java 代码，用于创建一个 XSSFWorkbook 对象并创建一个名为 “test”的 Sheet。
画面 13: 在 IntelliJ IDEA 中，显示 Java 代码，用于读取一个名为 “E:\excel\poi\test.xlsx” 的文件并写入到工作簿中。
画面 14: 在 Windows 资源管理器中，显示 “test.xlsx” 文件，其大小已从 9 KB 更新为 4 KB，表明文件已被修改。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
<dependencies>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml-schemas</artifactId>
<version>4.0.1</version>
</dependency>
</dependencies>

画面 4:
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml-schemas</artifactId>
<version>4.0.1</version>
</dependency>
</dependencies>

画面 9:
package org.apache.poi.ss.usermodel;
import ...
public interface Workbook extends Closeable, IterableSheet {
int PICTURE_TYPE_EMBED = 2;
int PICTURE_TYPE_WMF = 4;
int PICTURE_TYPE_PICT = 5;
int PICTURE_TYPE_JPEG = 6;
int PICTURE_TYPE_PNG = 7;
int getActiveSheetIndex();
void setActiveSheet(int var1);
int getFirstVisibleTab();
void setFirstVisibleTab(int var1);
void setSheetOrder(String var1, int var2);
void setSelectedTab(int var1);
void setSheetName(int var1, String var2);
}

画面 10:
XSSFWorkbook (org.apache.poi.hssf.usermodel)
XSSFWorkbook (org.apache.poi.xssf.usermodel)
XSSFWorkbook (org.apache.poi.xssf.streaming)
XSSFWorkbook (org.apache.poi.xssf.usermodel)

画面 12:
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
/**
* 使用POI创建Excel
*/
public class PoITest01 {
public static void main(String[] args) throws FileNotFoundException {
//1.创建工作簿
Workbook wb = new XSSFWorkbook(); //2007版本
Sheet sheet = wb.createSheet("test");
//3.文件流
FileInputStream pis = new FileInputStream(name: ""); //4.写入文件
}

画面 13:
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
/**
* 使用POI创建Excel
*/
public class PoITest01 {
public static void main(String[] args) throws Exception {
//1.创建工作簿
Workbook wb = new XSSFWorkbook(); //2007版本
Sheet sheet = wb.createSheet("test");
//3.文件流
FileInputStream pis = new FileInputStream(name: "E:\\excel\\poi\\test.xlsx");
//4.写入文件
wb.write(pis);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7:
标题：3.4 基本操作
子标题：3.4.1 创建Excel
表格内容：
| API名称 | 含义 |
| --- | --- |
| Workbook | Excel的文档对象，针对不同的Excel类型分为：HSSFWorkbook (2003) 和 XSSFWorkbook (2007) |
| Sheet | Excel的表单 |
| Row | Excel的行 |
| Cell | Excel的格子单元 |
| Font | Excel字体 |
| CellStyle | 格子单元样式 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

