# 画面线理解：12-POI的入门：绘制图形

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\12-POI的入门：绘制图形_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:35, 01:07, 04:10, 04:49, 04:58, 05:37, 06:21, 07:15, 07:48, 08:32, 09:49, 10:27, 10:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:54:39

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
Exception in thread "main" java.io.FileNotFoundException: E:\excel\poi\test2.xlsx (另一个程序正在使用此文件，进程无法访问。)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
