# 19-百万数据报表读取：代码实现及测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\19-百万数据报表读取：代码实现及测试_【海量资源尽在 ubkz.com】.mp4
- 时长 9分20秒（音频 560s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们完成了这个自定义的事件处理器那其实它就是我们整个代码的一个最核心的一个组件那这个写好了之后接下来呢我们就可以写一个测试类咱们一起完成整个百万数据报表的一个解析工作而这边呢在TESTS包下我去写我自己的一个测试类我就叫做TESTS06这边使用事件模型事件模型
[00:34] 解析百万数据数据报表好了同样的这个代码呢我也是以问方法的形式来做的psvm问方法那首先呢第一件事来一个pass就是说我要解析哪个文件先把这个路径先给它写好和这个文件路径呢我们一起把它抄过来就可以了Ctrl C拿过来这边Ctrl VOK我这个文件的名称demo我也抄过来了Ctrl C demoOK好了那接下来呢就是说一下
[01:13] 对于我整个使用事件模型这个它的一个操作的一个步骤那对于这个操作步骤来说呢首先第一件事第一件事我们要做的事情呢就是根据我们的Excel报表注意这回呢要获取一个基于事件模型的一个对象它叫做OPC Package要得到这么一个对象那这个OPC Package获取到了之后接着第二件事那第二件事呢就是用于创建
[01:48] 一个叫做XSF ReaderOK那接着第三件事第三件事呢我们要去获取一些这个叫做获取SharedAREDSharedStream Table这个其实获取一个表格对象获取一个表格对象那这个获取表格对象获取到了之后接着第四件事要去获取一个叫做StealthTable对象
[02:22] 好了我想说一下这几个对象呢我们是获取到但是基本上我们也不会用到的其实因为我一会要注册事件的时候需要用到这些基本的参数OK好了那这个我们搞定了之后接下来第五件事第五件事要创建一个最重要的对象这个是基于SARS的XML Reader对象那可以这样理解之前的这几步呢其实还是POI为我们提供的
[02:57] 底下这个SuxReader对象这些其实才是我们真正的Sux模式或者Sux事件模型的一些比较重要的一些对象才会出场好了这个我们搞定了之后接着第六件事这个是Sux它具有事件驱动的这么一个能力但事件驱动执行到某一个事件的时候要去触发你的一个叫做一个事件处理器所以我们这边有必要把你的事件注册到我们这个SuxReader上所以这边我要注册事件处理器OK
[03:34] 那好了接下来呢就可以做第七件事了第七件事就开始主行读取了OK那我们接着就是把这些基本的代码呢给他都写出来好了这几个代码呢其实比较简单第一件事它是用来做什么的呢我们可以这样去理解我们不是要去处理这个Excel报表吗那这个Excel报表它是不是以XML的形式读取啊咱们仔细看它是XML吗不是
[04:03] 那我们之前做过演示是不是可以以压缩包的形式来进行读取啊所以对于第一件事他干嘛呢就是把这个Cell报表以XML的形式压缩包的形式给他打开就这么一件事就是把这个XML的文件以压缩包的形式给他打开所以呢这里面我们这个代码如何去写各位就有灵感了OPC PackageOPC Package它有一个静态方法打点叫做Open叫做Open
[04:32] 那其实就是以XML的形式打开一个文件那这个文件的路径pass拿过来接着你打开这个文件可以给它指定你是用来干嘛的你是用来读的你是用来取的你是用来写的那我们这边是以只读形式打开packageassize.read也就意味着我当前是以只读形式给它打开这个文件那这样一来有一个异常呢我做一个处理
[05:01] 那这样一来我们就能得到我们的OBC package对象好了那这个OBC package对象我们获取到了之后接着根据这个对象创建一个我们的XSS ReaderOK那这一步其实也是比较简单READR等于直接NU出来就可以那NU的时候其实就意味着我们借助这个Reader对象可以去读取这个压缩包了
[05:30] OK这些我们基本的这两步其实是比较专业关键或者比较重要的两步剩下的一些就是要获取什么sharing screen table获取什么样式表格的一些样式表格这些内容都是我们不太关注的一些点它的代码写起来基本上都是类似的直接通过reader打点获取就可以get share screen table注意得到表格好了底下同样的screen打点get
[06:03] 这回得到的是注意这回得到的是一个style table我们来找一下在这找到了style tableOK这两步我们做过了之后其实就是为我注册事件的时候打一个基础里面需要用到这些属性好了接下来第五件事就是要创建一个XML reader这么一个对象这个XML reader叫做XML readerXML readerOK各位别捣错包
[06:43] org.xml.sux这个包下的因为我们是用sux这种方式基于事件模型的形式来做的OK可以给它起一个名字就叫xml reader了那这个xml reader如何获取其实它是我们通过有一个叫做xml reader的这么一个工厂有专门这么一个工厂这个工厂就是用来产生基于sux这种的一个reader对象的factory打点correctOK那这样一来我的
[07:15] 比较关键的Suxreader对象已经创建好了创建好了之后我们要做的事情就叫做注册时间处理器注册时间处理器注册时间处理器可以借助XMLreader的一个方法来做打点setContentHandler这个setContentHandler里面接收的是一个contentHandler注意这个contentHandler是一个接口是一个接口在这个接口当中
[07:46] PUI已经实现了一个基于SuxReader的这种接口那如何去写呢我们注意这边呢其实就可以自己定义出来我们基于PUI的一个时间处理器那这个时间处理器new xsf sheet xmlhandler这个是PUI里面的一个时间处理器那这个时间处理器里面注意这个时间处理器里面我们可以设置一些内容
[08:18] 生成内容有什么注意第一个就是style tables好了第二个就是s我们叫做table前面这两个基本的一些数据这两个数据我说过了我们一般不用就是因为我这个注册处理器的时候时间处理器的时候我要自己去写那除了这两个参数之外还有第三个参数第三个参数就是我们自己写的sheet handler这个是最关键的一个new一个sheet handler过来好了接下来还有一个我们写一个false
[08:49] 这边有一个错误就是说这边注意第一个是我们的样式表格第二个是我们的死菌表注意应该把table靠过来才对OK那这样一来我们自己写了一个基于PUI的这么一个时间处理器那这个时间处理器需要注册到XML Reader当中注册很简单把它放置过来就可以了那这样一来我时间注册的处理器就已经注册好了那接下来最后一件事就开始逐行进行读取

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apache POI 的事件模型（Event Model）解析 Excel 文件，重点是通过 XMLReader 和 XSSFSheetXMLHandler 来处理 Excel 的 XML 内容。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了在 IntelliJ IDEA 中，通过右键点击 `SheetHandler.java` 文件，弹出的上下文菜单，其中包含“重构”、“优化导入”、“删除”等选项，以及“构建模块 'poi-demo'”等构建操作。画面中显示了 `SheetHandler` 类的代码片段，其中包含 `implements XSSFSheetXMLHandler` 和 `PoIEntity entity;` 等内容。
画面 2: 显示了 `PoITest06.java` 文件的初始状态，其中 `main` 方法中仅定义了 `String path = "";`，尚未填写具体路径。
画面 3: 在 `main` 方法中，将 `path` 变量赋值为一个具体的 Excel 文件路径：`String path = "C:\\Users\\ThinkPad\\Desktop\\lihrm\\day8\\资源\\百万数据报表\\demo.xlsx";`。
画面 4: 在代码编辑器中，光标位于 `String path = ...` 行后，下方显示了三个 PPT 页面的缩略图，标题分别为“无标题 - 图图”、“无标题 - 图图”、“无标题 - 图图”，内容涉及“事件模型解析 Excel”。
画面 5: 在 `main` 方法中，添加了注释“//1. 根据excel路径获取OPCPackage”，并开始编写代码 `OPCPackage opcPackage = OPCPackage.open(path, PackageAccess.READ);`。
画面 6: 在 `main` 方法中，添加了注释“//2. 创建XSSFReader对象”，并编写了 `XSSFReader reader = new XSSFReader(opcPackage);`。
画面 7: 在 `main` 方法中，添加了注释“//3. 获取SharedStringsTable对象”，并编写了 `SharedStringsTable table = reader.getSharedStringsTable();`。
画面 8: 在 `main` 方法中，添加了注释“//4. 获取styleTable对象”，并编写了 `StylesTable stylesTable = reader.getStylesTable();`。
画面 9: 在 `main` 方法中，添加了注释“//5. 创建Sax的XMLReader对象”，并编写了 `XMLReader xmlReader = XMLReaderFactory.createXMLReader();`。
画面 10: 在 `main` 方法中，添加了注释“//6. 注册事件处理器”，并编写了 `xmlReader.setContentHandler(new XSSFSheetXMLHandler(stylesTable, stylesTable, new SheetHandler(), false));`。
画面 11: 在 `main` 方法中，添加了注释“//7. 运行读取”，并编写了 `xmlReader.parse(new InputSource(new FileInputStream(path)));`。
画面 12: 在 `main` 方法中，添加了注释“//7. 运行读取”，并编写了 `xmlReader.parse(new InputSource(new FileInputStream(path)));`。
画面 13: 在 `main` 方法中，添加了注释“//7. 运行读取”，并编写了 `xmlReader.parse(new InputSource(new FileInputStream(path)));`。
画面 14: 在 `main` 方法中，添加了注释“//7. 运行读取”，并编写了 `xmlReader.parse(new InputSource(new FileInputStream(path)));`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import org.apache.poi.xssf.eventusermodel.XSSFEventModel;
import org.apache.poi.xssf.usermodel.XSSFComment;
```
```java
class SheetHandler implements XSSFSheetXMLHandler {
    private PoIEntity entity;
```
画面 2:
```java
package cn.itcast.poi.test;
public class PoITest06 {
    public static void main(String[] args) {
        String path = "";
    }
}
```
画面 3:
```java
String path = "C:\\Users\\ThinkPad\\Desktop\\lihrm\\day8\\资源\\百万数据报表\\demo.xlsx";
```
画面 4:
```java
//1. 根据excel路径获取OPCPackage
//2. 创建XSSFReader对象
//3. 获取SharedStringsTable对象
//4. 获取styleTable对象
//5. 创建Sax的XMLReader对象
//6. 注册事件处理器
//7. 运行读取
```
画面 5:
```java
OPCPackage opcPackage = OPCPackage.open(path, PackageAccess.READ);
```
画面 6:
```java
XSSFReader reader = new XSSFReader(opcPackage);
```
画面 7:
```java
SharedStringsTable table = reader.getSharedStringsTable();
```
画面 8:
```java
StylesTable stylesTable = reader.getStylesTable();
```
画面 9:
```java
XMLReader xmlReader = XMLReaderFactory.createXMLReader();
```
画面 10:
```java
xmlReader.setContentHandler(new XSSFSheetXMLHandler(stylesTable, stylesTable, new SheetHandler(), false));
```
画面 11:
```java
xmlReader.parse(new InputSource(new FileInputStream(path)));
```
画面 12:
```java
xmlReader.parse(new InputSource(new FileInputStream(path)));
```
画面 13:
```java
xmlReader.parse(new InputSource(new FileInputStream(path)));
```
画面 14:
```java
xmlReader.parse(new InputSource(new FileInputStream(path)));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: PPT 页面标题为“无标题 - 图图”，内容涉及“事件模型解析 Excel”，但未显示具体架构图或流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。

