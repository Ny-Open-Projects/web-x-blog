# 画面线理解：11-POI的入门：单元格样式处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\11-POI的入门：单元格样式处理_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:35, 02:14, 03:22, 04:00, 05:10, 06:07, 07:01, 07:30, 07:58, 09:23, 10:37, 11:07, 11:44, 12:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:54:10

1) 这一组画面整体在讲什么（一句话）：
使用 Apache POI 库在 Java 中创建并格式化 Excel 文件，包括设置单元格边框、字体、对齐方式等样式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Excel 文件，单元格 C3 中有文字“传智播客”，用于演示最终生成的文件效果。
画面 2: 在 IntelliJ IDEA 中打开 `PoTest03.java`，代码中创建了 `HSSFWorkbook`，并设置了单元格值“传智播客”，但未设置样式。
画面 3: 查看 `BorderStyle.class` 的反编译代码，展示边框样式常量定义，如 `THIN`, `MEDIUM`, `THICK` 等。
画面 4: 在 `PoTest03.java` 中，为 `CellStyle` 设置边框样式，使用 `BorderStyle.THIN` 设置上下左右边框。
画面 5: 在 `PoTest03.java` 中，为 `CellStyle` 设置字体，使用 `Font` 类设置字体名称为“华文行楷”，字号为 28。
画面 6: 在 `PoTest03.java` 中，设置单元格对齐方式，使用 `style.setAlignment(HorizontalAlignment.CENTER)` 设置水平居中，`style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER)` 设置垂直居中。
画面 7: 在 `PoTest03.java` 中，设置行高和列宽，使用 `row.setHeightInPoints(50)` 设置行高，`sheet.setColumnWidth((short)2, (short)(31 * 256))` 设置列宽。
画面 8: 展示 Excel 文件，单元格 C3 中有文字“传智播客”，单元格 C5 有绿色边框，用于演示设置边框后的效果。
画面 9: 查看 `XSSFSheet.class` 的反编译代码，展示与列宽和隐藏相关的逻辑。
画面 10: 在 `PoTest03.java` 中，设置单元格对齐方式，使用 `style.setAlignment(HorizontalAlignment.CENTER)` 设置水平居中，`style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER)` 设置垂直居中。
画面 11: 在 `PoTest03.java` 中，设置行高和列宽，使用 `row.setHeightInPoints(50)` 设置行高，`sheet.setColumnWidth((short)2, (short)(31 * 256))` 设置列宽。
画面 12: 在 `PoTest03.java` 中，设置单元格对齐方式，使用 `style.setAlignment(HorizontalAlignment.CENTER)` 设置水平居中，`style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER)` 设置垂直居中。
画面 13: 在 `PoTest03.java` 中，代码已完整，运行后在终端显示“Process finished with exit code 0”，并展示 `day/` 和 `poi/` 目录结构。
画面 14: 展示 Excel 文件，单元格 C3 中有文字“传智播客”，单元格 C5 有绿色边框，用于演示设置边框后的效果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
public class PoTest03 {
    public static void main(String[] args) throws Exception {
        //创建工作簿 HSSFWorkbook - 2003版本
        Workbook wb = new HSSFWorkbook();
        //创建表单 sheet
        Sheet sheet = wb.createSheet("test");
        //创建行对象，参数，索引（从0开始）
        Row row = sheet.createRow(1);
        //创建单元格对象，参数，索引（从0开始）
        Cell cell = row.createCell(1);
        //把单元格写入内容
        cell.setCellValue("传智播客");

        //样式处理
        //创建样式对象
        CellStyle style = wb.createCellStyle();
        //设置边框
        style.setBorderTop(BorderStyle.THIN); //上边框
        style.setBorderBottom(BorderStyle.THIN); //下边框
        style.setBorderLeft(BorderStyle.THIN); //左边框
        style.setBorderRight(BorderStyle.THIN); //右边框

        //创建字体对象
        Font font = wb.createFont();
        font.setFontName("华文行楷"); //字体
        font.setFontHeightInPoints((short)28); //字号
        style.setFont(font);

        //行高和列宽
        row.setHeightInPoints(50); //行高
        sheet.setColumnWidth((short)2, (short)(31 * 256)); //列宽

        //刷出显示
        style.setAlignment(HorizontalAlignment.CENTER); //水平居中
        style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER); //垂直居中

        //文件流
        FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test1.xlsx");
        //写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 3:
```java
package org.apache.poi.ss.usermodel;

public enum BorderStyle {
    NONE(0),
    THIN(1),
    MEDIUM(2),
    DASHED(3),
    DOTTED(4),
    THICK(5),
    DOUBLE(6),
    HAIR(7),
    MEDIUM_DASHED(8),
    DASH_DOT(9),
    MEDIUM_DASH_DOT(10),
    DASH_DOT_DOT(11),
    MEDIUM_DASH_DOT_DOT(12),
    SLANTED_DASH_DOT(13);

    private final short code;
    private static final BorderStyle[] _table = new BorderStyle[14];
    private BorderStyle(int code) { this.code = (short)code; }
    public short getCode() { return this.code; }
    public static BorderStyle valueOf(short code) { return table[code]; }
}
```

画面 4:
```java
public class PoTest03 {
    public static void main(String[] args) throws Exception {
        //创建工作簿 HSSFWorkbook - 2003版本
        Workbook wb = new HSSFWorkbook();
        //创建表单 sheet
        Sheet sheet = wb.createSheet("test");
        //创建行对象，参数，索引（从0开始）
        Row row = sheet.createRow(1);
        //创建单元格对象，参数，索引（从0开始）
        Cell cell = row.createCell(1);
        //把单元格写入内容
        cell.setCellValue("传智播客");

        //样式处理
        //创建样式对象
        CellStyle style = wb.createCellStyle();
        //设置边框
        style.setBorderTop(BorderStyle.THIN); //上边框
        style.setBorderBottom(BorderStyle.THIN); //下边框
        style.setBorderLeft(BorderStyle.THIN); //左边框
        style.setBorderRight(BorderStyle.THIN); //右边框

        //创建字体对象
        Font font = wb.createFont();
        font.setFontName("华文行楷"); //字体
        font.setFontHeightInPoints((short)28); //字号
        style.setFont(font);

        //行高和列宽
        row.setHeightInPoints(50); //行高
        sheet.setColumnWidth((short)2, (short)(31 * 256)); //列宽

        //刷出显示
        style.setAlignment(HorizontalAlignment.CENTER); //水平居中
        style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER); //垂直居中

        //文件流
        FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test1.xlsx");
        //写入文件
        wb.write(pis);
        pis.close();
    }
}
```

画面 5:
```java
//创建样式对象
CellStyle style = wb.createCellStyle();
//设置边框
style.setBorderTop(BorderStyle.THIN); //上边框
style.setBorderBottom(BorderStyle.THIN); //下边框
style.setBorderLeft(BorderStyle.THIN); //左边框
style.setBorderRight(BorderStyle.THIN); //右边框

//创建字体对象
Font font = wb.createFont();
font.setFontName("华文行楷"); //字体
font.setFontHeightInPoints((short)28); //字号
style.setFont(font);

//行高和列宽
row.setHeightInPoints(50); //行高
sheet.setColumnWidth((short)2, (short)(31 * 256)); //列宽

//刷出显示
style.setAlignment(HorizontalAlignment.CENTER); //水平居中
style.setVerticalAlignment(VERTICAL_ALIGNMENT.CENTER); //垂直居中

//文件流
FileOutputStream pis = new FileOutputStream(name: "E:\\excel\\poi\\test1.xlsx");
//写入文件
wb.write(pis);
pis.close();
```

画面 6:
```java
//创建样式对象
CellStyle style = wb.createCellStyle();
//设置边框
style.setBorderTop(BorderStyle.THIN); //上边框
style.setBorderBottom(BorderStyle.THIN); //下边框
style.setBorderLeft(BorderStyle.THIN); //左边框
style.setBorderRight(BorderStyle.THIN); //右边框

//创建字体对象
Font font = wb.createFont();
font.setFontName("华文行楷"); //字体
font.setFontHeightInPoints((short)28); //字号
style.setFont(font);

//行高和列宽
row.setHeightInPoints(5
