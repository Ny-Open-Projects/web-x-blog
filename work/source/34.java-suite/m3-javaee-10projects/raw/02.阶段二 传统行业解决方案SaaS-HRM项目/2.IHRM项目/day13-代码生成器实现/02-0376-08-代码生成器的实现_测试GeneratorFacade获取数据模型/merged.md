# 08-代码生成器的实现：测试GeneratorFacade获取数据模型

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\08-代码生成器的实现：测试GeneratorFacade获取数据模型_【海量资源尽在 ubkz.com】.mp4
- 时长 7分6秒（音频 426s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 这个入口程序呢我们已经写的差不多了但是这个代码究竟写的对不对或者说这个数据模型里面的数据究竟是不是就是我们想要的我们可以一起来简单的测试一下OK好了这边呢我们都知道通过Generator by Database这个方法可以真正的对数据库里面的每一个表进行代码生成那这边构造了数据模型那接着我先把这个数据模型打印出来来看一下我们的效果来个放行玩
[00:32] 好了map.entryStringObjectENTRY循环看一下效果dataENTRY好了datamodel.entrysetsot我们可以打印一下就是ENTRY.getkey加上ENTY打点getvalue
[01:06] 好了那接下来这个方法呢我们写好了那接下来就是说在哪去调用我们这个generator facet好了在哪调用呢这个就从我们的UI进行说起在我们的UI通过database youtube界面点击了下一步之后进入到code youtube在code youtube当中有一个代码生成的这么一个按钮就是在这边叫做生成代码的这么一个按钮
[01:36] 这个生成代码的按钮呢各位点击了之后它会触发最后一个方法最后一个方法就叫做generator方法这个方法是我们调用UI的一个程序入口的一个方法好了那接下来我们在这边是不是就可以去调用generator飞萨的没错吧好了那我们要做的事情很简单new一个generator飞萨的好了在我们new的过程当中它需要这么几个构造的参数
[02:09] 好了把这几个构造参数拿过来各位发现需要模板路径好了模板路径已经给我传递过来了那需要你输出的路径也已经传递过来了好了settings我们也准备好了当了还有一个是不是叫做dbdb是不是也准备了OK好了那这样一来我们拗出了对象先抛一个异常啊这边这个参数名字不对啊把这个代表写改一下
[02:51] 注视也改一下OK那这样一来我们对象创建好了接着调用对象里面发SR的方法打点叫做GenerateByDatabase好了这边调用的过程当中呢会有一个异常我用TryCatch进行一个处理好那这样一来我们的UI调用程序入口咱们已经搞定了那好了再回到DatabaseUtil我们重新去执行一下当前的MEM方法
[03:18] 咱们一起来看一下能不能够把数据模型全部给我传输出来好了这边走调用出UI界面这边可以选择root123456测试好了没问题随便选择一个IHM点击下一步好了这边模板随便选主要是为了要它的路径好代码生成的路径我也随便选比如说我就到泰斯特目录下好了
[03:49] 项目名IHRM包名比如说我就叫做com.ihrm.sostmsystem项目中文名称呢我把它称之为SaaSIHRM人力资源系统作者ITCASOK这些都没问题当我生成代码的时候它是不是会触发刚才我们写过的这个genus的方法接着调用我们的入口程序在入口程序当中
[04:20] 放循环拿到每一个table接着对每一个table里面构造出它的数据模型啊好了我们一起来看一下有没有效果走生成代码好了各位会发现现在呢已经把所有相应的这些资讯这些信息全部给我们打印出来了由于这个内容实在是有点多啊实在有点多为了看起来更加清晰一些呢我这边呢画一条线OK这边呢我再点击代码生成这个看起来不太清晰啊
[04:58] 把这个关的这回再重来一下走mycircleroot123456测试连接好了im下一步随便选一模板生成路径随便选择一下一盘泰斯特ok没问题项目名称im包名com.im.比如说sostm这个模块项目中名人力资源管理系统
[05:30] 好了itcast没问题好了接着生成代码好了那接下来关门我们来看一下数据一个横线里面的一大堆好了首先上边这些是我们配置相应的一些内容好了接着接着有pass1代表我们传递的那个包名没错吧好了这是包相关的好了继续再来是我们的中文项目名称好了有classnameclassname是我们
[06:01] 专门存放的一个类的名称然后这边还写了一个test key是不是验证一下我这个自定义的配置内容啊自定义的数据好了接下来table这边呢是我们替换的一些内容OK那接下来这些看过了之后最重要的是table那table里面有table的名称有类名当然了我这个表没写注释还有我们的主件common id好了主件这个common id是主件那接下来就是对这个
[06:32] 每一列进行一个处理在每一列进行处理的时候第一列它的名称叫做company id属性名company id它的java类型死剧数据库类型whatcha它的注释其id并且column是一个primary是我们的主件那接下来后面这个就不说了后面这个它就不是主件是不是就是一个noun值啊ok那好了这样一来呢其实我们这个入口
[07:01] 获取数据模型的内容咱们就已经搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Java 的数据库逆向工程代码生成器的实现，包括核心生成逻辑、数据模型构建、UI 界面调用及配置文件的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 GeneratorFacade.java 文件中构造函数和 generatorByDatabase 方法的代码，注释说明了“准备数据模型”和“调用核心处理类完成代码生成”。
画面 2: 在 generatorByDatabase 方法中，光标位于 for 循环的开始处，IDE 显示了 Map.Entry 的自动补全建议。
画面 3: 光标移动到 for 循环的末尾，IDE 显示了 Map.Entry 的方法列表，如 getkey()、getValue() 等。
画面 4: 光标在 for 循环内部，调用 entry.getKey() 和 entry.getValue()，并打印输出。
画面 5: 展示项目结构，选中了 CodeUtil.java 文件，终端显示了运行命令。
画面 6: 展示 CodeUtil.java 文件中 generator 方法的代码，注释说明了参数含义。
画面 7: 光标在 generator 方法的末尾，准备添加代码。
画面 8: 展示项目结构，选中了 DatabaseUtil.java 文件，终端显示了运行命令。
画面 9: 展示 DatabaseUtil.java 文件中 main 方法的代码，注释说明了参数含义。
画面 10: 光标在 main 方法中，准备添加代码。
画面 11: 展示项目结构，选中了 custom.properties 文件，终端显示了编译成功。
画面 12: 展示 GeneratorFacade.java 文件中 generator 方法的代码，注释说明了“根据 Table 对象获取数据模型”。
画面 13: 展示一个“代码生成器 1.0”的弹窗界面，用户输入了项目名、包名、作者等信息。
画面 14: 展示 custom.properties 文件的内容，其中定义了数据库字段类型映射和项目配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private String outPath;
private Settings settings;
private DataBase db;

public GeneratorFacade(String templatePath, String outPath, Settings settings, DataBase db) {
    this.templatePath = templatePath;
    this.outPath = outPath;
    this.settings = settings;
    this.db = db;
}

/**
 * 1.准备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public void generatorByDatabase() throws Exception {
    List<Table> tables = DataBaseUtils.getDbInfo(db);
    for (Table table : tables) {
        //对每一个Table对象进行代码生成
        //读取模型
        //调用Generator核心处理类
        Map<String, Object> dataModel = getDataModel(table);
        for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
    }
}
```

画面 2:
```java
for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
    System.out.println(entry.getKey() + "--" + entry.getValue());
}
```

画面 3:
```java
for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
    System.out.println(entry.getKey() + "--" + entry.getValue());
}
```

画面 4:
```java
for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
    System.out.println(entry.getKey() + "--" + entry.getValue());
}
```

画面 5:
```java
//UI调用程序入口
/**
 * @param templatePath
 * 模板所在路径
 * @param outpath
 * 选择代码生成路径
 * @param settings
 * 工程配置对象
 * @param db
 * 数据库信息
 */
private void generator(String templatePath, String outpath, Settings settings, DataBase db) {
    System.out.println(templatePath);
    System.out.println(outpath);
    System.out.println(settings);
    System.out.println(db);
    GeneratorFacade gf = new GeneratorFacade(templatePath, outpath, settings, db);
    gf.generatorByDatabase();
}
```

画面 6:
```java
/**
 * @param templatePath
 * 模板所在路径
 * @param outpath
 * 选择代码生成路径
 * @param settings
 * 工程配置对象
 * @param db
 * 数据库信息
 */
private void generator(String templatePath, String outpath, Settings settings, DataBase db) {
    System.out.println(templatePath);
    System.out.println(outpath);
    System.out.println(settings);
    System.out.println(db);
    GeneratorFacade gf = new GeneratorFacade(templatePath, outpath, settings, db);
    gf.generatorByDatabase();
}
```

画面 7:
```java
/**
 * @param templatePath
 * 模板所在路径
 * @param outpath
 * 选代码生成路径
 * @param settings
 * 工程配置对象
 * @param db
 * 数据库信息
 */
private void generator(String templatePath, String outpath, Settings settings, DataBase db) {
    GeneratorFacade facade = new GeneratorFacade(templatePath, outpath, settings, db);
    facade.generatorByDatabase();
}
```

画面 8:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 9:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 10:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 11:
```properties
author=itcast
CHAR=String
project=String
BIGINT=Long
TEXT=String
VARCHAR=String
INT=Integer
path1=String
path2=String
path3=String
projectComment=String
table=Table(name='sys_file', name2='SysFile', comment='', keys='id', columns=[Column(columnName='id', columnName2='id', columnType='String')
author=itcast
project=String
```

画面 12:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 13:
```java
//代码生成器 1.0
模板: Spring Boot模板的模板
代码生成路径: E:\test
项目名（英文）:
包名:
项目中文名称:
作者:
数据库名: itim
用户名: root
密码: 111111
生成代码
关闭
```

画面 14:
```properties
author=itcast
CHAR=String
project=String
BIGINT=Long
TEXT=String
VARCHAR=String
INT=Integer
path1=String
path2=String
path3=String
projectComment=String
table=Table(name='sys_file', name2='SysFile', comment='', keys='id', columns=[Column(columnName='id', columnName2='id', columnType='String')
author=itcast
project=String
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

