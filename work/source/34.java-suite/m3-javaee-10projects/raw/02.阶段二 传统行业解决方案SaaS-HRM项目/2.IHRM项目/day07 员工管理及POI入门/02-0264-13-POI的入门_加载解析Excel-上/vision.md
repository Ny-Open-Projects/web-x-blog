# 画面线理解：13-POI的入门：加载解析Excel-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\13-POI的入门：加载解析Excel-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:35, 01:12, 02:50, 03:48, 04:24, 05:19, 06:21, 06:51, 07:37, 08:10, 09:01, 09:33, 10:14, 10:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:55:11

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
