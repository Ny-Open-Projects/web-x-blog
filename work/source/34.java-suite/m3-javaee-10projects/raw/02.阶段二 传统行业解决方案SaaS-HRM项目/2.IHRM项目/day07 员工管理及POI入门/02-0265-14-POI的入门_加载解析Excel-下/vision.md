# 画面线理解：14-POI的入门：加载解析Excel-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\14-POI的入门：加载解析Excel-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 02:28, 04:16, 05:00, 05:37, 06:33, 07:11, 07:39, 08:35, 09:09, 10:35, 10:54, 11:43, 12:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:55:51

1) 这一组画面整体在讲如何使用 Apache POI 库读取 Excel 文件中的数据并输出到控制台。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Excel 文件 "demo.xlsx"，其中包含序号、姓名、年龄、家庭住址、出生日期等列的数据。
画面 2: 展示了 POI 库中 CellType.class 的反编译代码，定义了单元格类型常量。
画面 3: 展示了在 IntelliJ IDEA 中编写 Java 代码，使用 switch 语句处理单元格类型。
画面 4: 展示了代码中获取工作表的行数并遍历每一行，获取单元格内容。
画面 5: 展示了代码中获取单元格类型并根据类型进行处理。
画面 6: 展示了代码中处理日期格式单元格的逻辑，使用 Date 类型。
画面 7: 展示了代码中处理日期格式单元格的逻辑，使用 Date 类型。
画面 8: 展示了代码中处理日期格式单元格的逻辑，使用 Date 类型。
画面 9: 展示了代码中处理日期格式单元格的逻辑，使用 Date 类型。
画面 10: 展示了代码中处理日期格式单元格的逻辑，使用 Date 类型。
画面 11: 展示了程序运行后，控制台输出了 Excel 文件中每一行每一列的数据。
画面 12: 展示了 Excel 文件 "demo.xlsx"，其中包含序号、姓名、年龄、家庭住址、出生日期等列的数据。
画面 13: 展示了 Excel 文件 "demo.xlsx"，其中包含序号、姓名、年龄、家庭住址、出生日期等列的数据。
画面 14: 展示了代码中获取工作表的行数并遍历每一行，获取单元格内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package org.apache.poi.ss.usermodel;
import org.apache.poi.util.internal;
public enum CellType {
    @internal
    since - "POI 3.15 beta 3"
    _NONE(1),
    NUMERIC(2),
    STRING(3),
    FORMULA(4),
    BLANK(5),
    BOOLEAN(4),
    ERROR(5);
```

画面 3:
```java
switch (celltype) {
case STRING:
```

画面 4:
```java
Sheet sheet = wb.getSheetAt(0); //参数，索引
//3.获取sheet中每一行，和每一个单元格
for (int rownum = 0; rownum < sheet.getLastRowNum(); rownum++) {
```

画面 5:
```java
switch (celltype) {
case STRING:
case BOOLEAN:
case NUMERIC:
```

画面 6:
```java
if (DateUtil.isCellDateFormatted(cell)) {
    value = cell.getDateCellValue();
} else {
    value = cell.getNumericCellValue();
}
```

画面 7:
```java
if (DateUtil.isCellDateFormatted(cell)) {
    value = cell.getDateCellValue();
} else {
    value = cell.getNumericCellValue();
}
```

画面 8:
```java
if (DateUtil.isCellDateFormatted(cell)) {
    value = cell.getDateCellValue();
} else {
    value = cell.getNumericCellValue();
}
```

画面 9:
```java
if (DateUtil.isCellDateFormatted(cell)) {
    value = cell.getDateCellValue();
} else {
    value = cell.getNumericCellValue();
}
```

画面 10:
```java
if (DateUtil.isCellDateFormatted(cell)) {
    value = cell.getDateCellValue();
} else {
    value = cell.getNumericCellValue();
}
```

画面 11:
```java
Process finished with exit code 0
```

画面 12:
```java
//1.根据excel文件创建工作簿
Workbook wb = new XSSFWorkbook(path: "E:\\excel\\poi\\demo.xlsx");
//2.获取sheet
Sheet sheet = wb.getSheetAt(0); //参数，索引
//3.获取sheet中每一行，和每一个单元格
for (int rownum = 0; rownum < sheet.getLastRowNum(); rownum++) {
    Row row = sheet.getRow(rownum); //根据索引获取每一行
    StringBuilder sb = new StringBuilder();
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum); //根据索引获取每一个单元格
        Object value = getCellValue(cell);
        sb.append(value).append(" ");
    }
    System.out.println(sb.toString());
}
```

画面 13:
```java
//1.根据excel文件创建工作簿
Workbook wb = new XSSFWorkbook(path: "E:\\excel\\poi\\demo.xlsx");
//2.获取sheet
Sheet sheet = wb.getSheetAt(0); //参数，索引
//3.获取sheet中每一行，和每一个单元格
for (int rownum = 0; rownum < sheet.getLastRowNum(); rownum++) {
    Row row = sheet.getRow(rownum); //根据索引获取每一行
    StringBuilder sb = new StringBuilder();
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum); //根据索引获取每一个单元格
        Object value = getCellValue(cell);
        sb.append(value).append(" ");
    }
    System.out.println(sb.toString());
}
```

画面 14:
```java
//1.根据excel文件创建工作簿
Workbook wb = new XSSFWorkbook(path: "E:\\excel\\poi\\demo.xlsx");
//2.获取sheet
Sheet sheet = wb.getSheetAt(0); //参数，索引
//3.获取sheet中每一行，和每一个单元格
for (int rownum = 0; rownum < sheet.getLastRowNum(); rownum++) {
    Row row = sheet.getRow(rownum); //根据索引获取每一行
    StringBuilder sb = new StringBuilder();
    for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
        Cell cell = row.getCell(cellNum); //根据索引获取每一个单元格
        Object value = getCellValue(cell);
        sb.append(value).append(" ");
    }
    System.out.println(sb.toString());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
