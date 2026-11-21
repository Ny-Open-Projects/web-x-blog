# 06-代码生成器的实现：需求分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\06-代码生成器的实现：需求分析_【海量资源尽在 ubkz.com】.mp4
- 时长 9分14秒（音频 554s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经把这些数据模型都已经构造的差不多了那我们继续往下看咱们就去真正的实现我们这个代码生成器那对于这个代码生成器我们这个逻辑结构究竟是什么样的呢是这样咱们简单的以一张图形和各位做一个分析那首先对于我们代码生成器来说访问者其实就是我们的UI的这个界面UI的这个界面
[00:33] 那对于这个UI界面进行访问那你访问过来先去访问的是谁注意我这边呢先给他来一个统一的应用调用的入口程序那这个入口程序它的主要目的其实就是采集用户UI给我传递的这些所有的数据接着构造出模板所需要的数据模型那这个统一的UI入口程序我把它叫做GeneratorGenerator
[01:11] JENATORJENATORJENATOR那对于这个入口程序它的主要目的一共有这么几项我跟各位简单的写一下就是采集UI界面的输入数据那除了UI界面的输入数据之外还有第二个根据数据库信息获取我们的数据模型好了那接下来还有第三个
[01:44] 它是一个统一入口程序最终呢去生成文件不是通过这个入口程序来做的那第三个就是调用我们的核心生成器生成器生成器代码完成代码生成所以呢它不是我们的终点它只是中间一个过渡的一个程序方便前端UI型界面同时对数据进行一个整合的一个操作那好了接下来那通过统一入口程序Generator FaceAd
[02:16] 去调用调用到我们的核心核心类生成的代码生成核心处理类那这个核心处理类呢就叫做generatorok那这个generator它的主要目的其实很简单很简单它主要就是获取到所有的模板好了接着第二件事那获取到了所有模板之后接下来呢就是根据
[02:55] 我们这左边得到的数据模型和模板完成代码生成所以呢咱们的代码呢其实比较简单一共是分成这么两个类第一个统一调用的入口第二个就是统一的核心处理器通过这个处理类完成代码生成的这么一个工作那接下来呢就是在代码调用的过程当中可能会有一些参数传递的这么一些内容
[03:26] 那对于这个参数传递呢我们也来做一个简单的说明那这个UI界面呢我在之前的课程当中呢已经给各位下发过来了咱们可以打开看一下在前端UI我们能够获取到什么内容那DatabaseUtils这边执行里面的MEM方法集合好了这边选择MySQL用户名Root我的密码123456测试连接那比如说呢我这边呢就以IHRM举例下一步那各位来看
[03:56] 模板我们可以选择但是我选择的这个模板不是说Vue的前端模板或者什么sprintboot程序的前端模板这玩意儿其实代表的是一个文件夹说白了这玩意儿是不是代表的是一个当前这个模板所在的路径啊没错吧所以第一个我们指的是模板所在的路径那接着第二个那这个是不是代码生成的路径没错吧那底下这一块内容那这一块内容是不是代表的就是我们
[04:24] 用户对当前工程的一个配置那这个配置我们之前封装到了一个siting对象实体内当中还有印象吗那接下来底下这一块数据库相应的信息那数据库相应信息是不是就叫做database也是一个对象啊所以对于代码生成器前端我能够采集到的书记如下一共四个方面第一个模板路径第二个输出路径也就是说你代码生成器生成的代码
[04:54] 要把这个代码放到什么位置还有第三个我们的工程配置类工程配置对象好了以及第四个数据库配置对象OK那把这四个对象我都要传递给GenitorPesad这个对象当中能理解吧好了那接下来那接下来那在这个里面UI采集的基源数据呢就有1 2 3 4四块内容那接下来根据数据库信息获取模型
[05:22] 那根据数据库信息获取模型这个数据库配置对象我们已经得到了是不是可以调用我们刚才的调用我们刚才的写的那个database youtube通过那个里面是不是获取到所有的table列表那table列表获取到了之后是不是一个table代表的是一个表那其实它应该代表一套程序那根据一套table是不是调用一把genarator根据一套程序调用一把genarator真正完成代码生成的这么一个工作
[05:52] 这个希望各位都能理解好了这个跟各位简单的说了一下之后那也就意味着我的程序需要创建这么两个类那把这两个类先给它加载起来好在这边呢找到我们的代码我把这个呢放到一个新的包下就叫做core包下好了接下来呢new一个class这个class我就叫做generatorOK那对于这个类它的主要目的
[06:24] 一共有两项第一个采集用户UI界面输入的数据那这些数据呢包含我们的模板位置位置第二个呢代表的是我们的代码生成路径其实也是一个位置第三个是我们的工程配置对象SETTNG好了第四个是我们的数据库对象Data Base好了这一块内容我们获取到了之后接下来第二块
[07:02] 那第二块我们要做的事情呢其实就是准备数据模型那准备数据模型这个数据模型我们之前说过数据模型也是两方面第一方面第一方面代表的是我们的自定义配置好了第二方面代表的是我们的原数据那当然了我还可以给他多加一第三方面就是把这个工程对象也给他放到map里OK好了数据模型准备好了之后接着第三件事我们要做的事情其实就是调用
[07:34] 核心处理类完成代码生成工作当然了这个是我们需要配置一个方法那这个方法去调用的核心处理类核心处理类这ENERATOR好了这个核心处理类还没有Ctrl C拿过来在Core下也给它创建出来New一个Class好了这个就是我们代码生成器的核心处理类核心处理
[08:10] 类其实说白了这边就是借助free marker来做的完成文件生成那完成文件生成需要跟各位说了free marker讲究的有什么讲究的其实就是我们的数据模型加上加上我们的模板所以对于这个代码核心处理类当中它要求我们应该有这么三方面的数据这三方面的数据
[08:43] 简单的和各位写一下咱们一起来分析数据模型你得有那模板是不是应该有模板的位置没错吧好那接下来还有第三个就是你生成文件的路径OK这样一来其实我们就是对咱们代码生成器比较核心的两个类以及代码生成它的一个需求和各位做了一个简单的说明OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 Java 的数据库逆向工程代码生成器的架构设计与实现过程。

2) 按时间顺序列出每张画面的要点：
画面1：桌面环境，显示“黑马程序员”和“博学谷”标志，无其他操作。
画面2：在绘图工具中绘制一个矩形框，标注为“UI界面”。
画面3：在“UI界面”框右侧添加一个椭圆形框，标注为“GeneratorFacade”，并用箭头从“UI界面”指向“GeneratorFacade”，标注“统一调用的入口程序”。
画面4：在“GeneratorFacade”右侧添加另一个椭圆形框，标注为“Generator”，并用箭头从“GeneratorFacade”指向“Generator”，标注“代码生成核心处理类”。同时，在“Generator”框内添加文字说明：
1. 获取到所有的模板
2. 根据数据模型和模板完成代码生成
在“UI界面”框内添加文字说明：
1. 采集UI界面的输入数据
2. 根据数据传递获取数据模型
3. 调用核心生成代码完成代码生成
画面5：在 IntelliJ IDEA 中打开项目“codetutils”，显示项目结构和“DatabaseUtils.java”文件内容，其中包含数据库连接配置和获取表信息的代码。
画面6：在 IntelliJ IDEA 中显示“DatabaseUtil.java”文件内容，其中包含 GUI 界面的变量声明。
画面7：弹出“代码生成器 1.0”对话框，显示“项目名（英文）”、“包名”、“项目中文名称”、“作者”、“数据库”、“用户名”、“密码”等输入框，其中“用户名”和“密码”已填写。
画面8：在“代码生成器 1.0”对话框中，将“项目名（英文）”输入框中的内容修改为“item”，并点击“完成”按钮。
画面9：在绘图工具中，将“UI界面”框内的文字修改为“1. 选择模板 2. 输出路径 3. 工程配置对象 4. 数据库配置对接”。
画面10：在绘图工具中，将“UI界面”框内的文字修改为“1. 模板路径 2. 输出路径 3. 工程配置对象 4. 数据库配置对接”。
画面11：在绘图工具中，将“UI界面”框内的文字修改为“1. 模板路径 2. 输出路径 3. 工程配置对象 4. 数据库配置对接”。
画面12：在 IntelliJ IDEA 中，右键点击“DatabaseUtil.java”文件，弹出菜单，选择“Refactor”。
画面13：在 IntelliJ IDEA 中，弹出“Create New Class”对话框，用于创建新类。
画面14：在 IntelliJ IDEA 中，打开“Generator.java”文件，显示其内容。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面5：
```java
public static void main(String[] args) throws Exception {
    Database db = new Database(dbType, dbUrl, dbUserName, dbPassword);
    db.setUserName("root");
    db.setPassword("111111");
    List<Table> dbInfo = DataBaseUtils.getDbInfo(db);
    for (Table table : dbInfo) {
        System.out.println(table);
    }
}
```

画面6：
```java
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
//GEN-BEGIN:variables
// Variables declarations  do not modify
private JButton jButton1;
private JButton jButton2;
private JComboBox<String> jComboBox1;
private JLabel jLabel1;
private JLabel jLabel2;
private JLabel jLabel3;
private JLabel jLabel4;
private JLabel jLabel5;
private JTextField jTextField1;
private JTextField jTextField2;
private JTextField jTextField3;
// End of variables declaration //GEN-END:variables
```

画面7：
```java
// 项目名（英文）
// 包名
// 项目中文名称
// 作者
// 数据库
// 用户名 root
// 密码 111111
```

画面12：
```java
File -> New -> Class
```

画面14：
```java
package cn.itcast.generate.core;
public class Generator {
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面3：架构图结构：
- “UI界面” → “GeneratorFacade”
- “GeneratorFacade” → “Generator”

画面4：架构图结构：
- “UI界面” → “GeneratorFacade”
- “GeneratorFacade” → “Generator”

画面9：架构图结构：
- “UI界面” → “GeneratorFacade”
- “GeneratorFacade” → “Generator”

画面10：架构图结构：
- “UI界面” → “GeneratorFacade”
- “GeneratorFacade” → “Generator”

画面11：架构图结构：
- “UI界面” → “GeneratorFacade”
- “GeneratorFacade” → “Generator”

5) 无其他内容。

