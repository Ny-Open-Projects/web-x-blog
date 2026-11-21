# 画面线理解：10-POI的入门：创建单元格设置数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\10-POI的入门：创建单元格设置数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:17, 00:56, 01:38, 01:43, 02:10, 02:37, 02:55, 03:11, 03:18, 03:29, 03:45, 03:58, 04:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:53:18

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
