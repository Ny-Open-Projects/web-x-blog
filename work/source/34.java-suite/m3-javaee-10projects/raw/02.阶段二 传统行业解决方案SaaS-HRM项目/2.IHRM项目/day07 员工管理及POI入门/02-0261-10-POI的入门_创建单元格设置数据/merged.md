# 10-POI的入门：创建单元格设置数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\10-POI的入门：创建单元格设置数据_【海量资源尽在 ubkz.com】.mp4
- 时长 4分5秒（音频 245s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们现在只是创建了一个空的一个Cell文档那接下来如果想往里面填充数据那怎么做呢好了我们再回到我们的代码部分好了Ctrl CCtrl Vcopy文件是我们今天的第二个案例而这个里面我们要做的事情呢就是想方设法的去创建单元格写入一些内容写入我们的内容好了那这个怎么做呢其实跟之前这个内容基本上都差不多
[00:33] 都差不多这边我就不标序号了那我们创建到了sheet创建到了sheet好了这个我把它留到这那创建好了sheet就相当于我当前这一页已经有了那接下来我们关注的是不是应该定位到行那定位到行之后通过这里行定位到我们的某一个单元格呀所以接下来我们如果想要去写入内容的话咱们接下来要做的事情还有两件事好了创建行对象
[01:07] 行对象那行对象有了之后我们接下来要关注就是创建单元格对象那单元格对象如果也创建出来之后要做的事情就是向单元格中写入我们的内容好那这个又如何去做呢也是比较简单的首先创建行那我们都知道这一行呢其实是通过这个sheet里面的某一行没错吧所以我们这边从哪创建可以从sheet
[01:37] 创建就可以了sheet打点create诶注意肉那创建肉的时候呢这边有一个参数各位那这个参数代表什么意思它指的是我们这个行的索引那这个索引大家都知道是从零开始的是从零开始的比如说呢我要做的事情是在这写出我们的传职博客四个字好了那我怎么去做呢那我们创建行
[02:08] 这是第一行第二行第三行那就是012那我们要写的就是2好了这个所以从0开始OK那这样一来我们的行对象已经有了那行对象已经有了之后创建单元格对象那这个单元格对象那我们都知道了这每一个行里面它有不同的格子那所以这个单元格是不是通过行创建出来那所以通过行拿到我们创建格子那怎么去创建呢很简单肉打点
[02:41] 就是create cell那create cell的时候各位来看它cell指的是单元格那它接收的其实也是一个int类型的参数那这个参数也是所以同样也是从0开始那我们关注一下0 1 2所以我这边2这样一来我们的第二个格子就已经创建出来了那这个格子创建出来之后往里面写入内容比较简单cell打点downside的方法
[03:13] 那set的是什么就是我们叫做sell valuesell value好了比如说呢我里面就可以写一句话了专业播客OK好了那这样一来我这个等约格已经设置好了那我们把它起一个名字我就叫做test1了test1好了走好了程序在执行呢并且已经执行成功了我们再回到文件这边各位来看test1已经有了打开好了这边已经打开了各位来看
[03:57] 我这个真的是两个两个是一模一样一个是我手写的一个是通过程序创建出来的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Apache POI 库在 Java 中创建并写入 Excel 文件，包括创建工作簿、表单、行、单元格，并设置单元格内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Excel 程序界面，同时任务栏中显示两个窗口：一个为 Excel，另一个为 IntelliJ IDEA 项目窗口，表明正在准备操作环境。
画面 2: 显示 IntelliJ IDEA 中的 Java 代码，内容为创建一个 HSSFWorkbook 对象，创建一个名为 "test" 的 Sheet，并准备写入文件。
画面 3: 代码中添加了注释，说明创建 Sheet 后需要创建行对象。
画面 4: 代码中添加了注释，说明创建行对象后需要创建单元格对象。
画面 5: 代码中添加了注释，说明创建单元格对象后需要设置单元格值。
画面 6: 显示 Excel 程序界面，其中 A1 单元格显示“传智播客”，表明文件已成功创建并写入内容。
画面 7: 代码中添加了注释，说明创建单元格对象后需要设置单元格值。
画面 8: 显示 Excel 程序界面，其中 C3 单元格显示“传智播客”，表明文件已成功创建并写入内容。
画面 9: 显示 IntelliJ IDEA 中的 Java 代码，内容为设置单元格值的方法。
画面 10: 代码中添加了注释，说明设置单元格值后需要写入文件。
画面 11: 代码中添加了注释，说明设置单元格值后需要写入文件。
画面 12: 显示 Excel 程序界面，其中 C3 单元格显示“传智播客”，表明文件已成功创建并写入内容。
画面 13: 显示 Excel 程序界面，同时任务栏中显示两个窗口：一个为 Excel，另一个为 IntelliJ IDEA 项目窗口，表明正在准备操作环境。
画面 14: 显示 Excel 程序界面，同时任务栏中显示两个窗口：一个为 Excel，另一个为 IntelliJ IDEA 项目窗口，表明正在准备操作环境。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 使用poi创建excel
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
    }
}
```

画面 3:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 4:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 5:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 6:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 7:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 8:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 9:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 10:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 11:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //4.写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 12:
```java
package cn.itcast.poi.test;
import cn.itcast.poi.test;
/*
 * 创建单元格写入内容
 */
public class PoITest02 {
    public static void main(String[] args) throws Exception {
        //1.创建工作簿 HSSFWorkbook -- 2003版本
        Workbook wb = new HSSFWorkbook();
        //2.创建表单 sheet
        Sheet sheet = wb.createSheet();
        //3.文件流
        FileOutputStream pis = new FileOutputStream("E:\\excel\\poi\\test.xlsx");
        //

