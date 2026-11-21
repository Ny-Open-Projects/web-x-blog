# 画面线理解：07-自定义工具类：工具类介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\07-自定义工具类：工具类介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:48, 01:23, 02:00, 02:27, 03:29, 05:02, 05:44, 06:08, 06:37, 07:07, 08:03, 09:01, 09:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:09:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java项目中使用Apache POI库实现Excel文件的导出功能，包括控制器层调用、工具类编写、注解定义及模板文件的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码：在EmployeeController.java中，定义了导出Excel的@RequestMapping方法。
- 代码：使用@PathVariable接收月份参数，并调用userService的findByReport方法获取数据。
- 代码：创建Resource对象指向模板文件“excel-template/hr-demo.xlsx”。
- 代码：创建Workbook和Sheet对象，设置单元格样式并填充数据。
- 代码：使用DownloadUtils工具类完成文件下载。

画面2：
- 代码：在EmployeeController.java中，完成下载部分的代码。
- 代码：创建ByteArrayOutputStream对象。
- 代码：调用Workbook的write方法将数据写入输出流。
- 代码：调用DownloadUtils的download方法，传入响应对象、输出流和文件名。

画面3：
- 代码：在EmployeeController.java中，循环遍历数据列表，为每一行创建单元格并设置值。
- 代码：使用CellStyle设置单元格样式。
- 代码：设置单元格值，包括用户ID、用户名、手机号、最高学历、国家地区、护照号、薪资、生日、属相、入职时间、离职类型、离职原因、离职时间等字段。

画面4：
- 展示了生成的Excel文件“2018年2月份人事报表”。
- 表格包含：编号、姓名、手机、最高学历、国家地区、护照号、薪资、生日、属相、入职时间、离职类型、离职原因、离职时间等列。
- 数据示例：编号1，姓名test01，手机1300000001，最高学历初中，国家地区中国大陆，护照号1234，薪资1234，生日1994，属相牛，入职时间2018-03-01，离职类型未离职，离职原因未离职，离职时间未离职。

画面5：
- 代码：在EmployeeController.java中，使用IDE的自动补全功能。
- 代码：提示用户选择建议或插入点后缀。

画面6：
- 代码：在EmployeeController.java中，继续编写循环代码。
- 代码：设置单元格值，包括用户ID、用户名、手机号、最高学历、国家地区、护照号、薪资、生日、属相、入职时间、离职类型、离职原因、离职时间等字段。

画面7：
- 展示了桌面，有“黑马程序员”和“博学谷”的标志。
- 桌面上有“hrm”文件夹和“2018-03人”文件。

画面8：
- 代码：在Notepad++中编写ExcelAttribute.java文件。
- 代码：定义了@ExcelAttribute注解，包含name、sort、format三个属性。
- 代码：注解的Retention为RUNTIME，Target为FIELD。

画面9：
- 展示了文件夹结构，包含“ExcelAttribute.java”、“ExcelExportUtil.java”、“ExcelImportUtil.java”等文件。

画面10：
- 展示了项目结构，包含“ExcelAttribute.java”、“ExcelExportUtil.java”、“ExcelImportUtil.java”等文件。

画面11：
- 代码：在ExcelExportUtil.java中，定义了导出Excel的工具类。
- 代码：定义了rowIndex、styleIndex、clazz、fields等私有变量。
- 代码：定义了export方法，接收响应对象、输入流、对象列表和文件名。

画面12：
- 代码：在ExcelExportUtil.java中，继续编写导出Excel的代码。
- 代码：获取模板样式，创建行和单元格，设置单元格值。
- 代码：使用ExcelAttribute注解判断字段是否需要特殊处理。
- 代码：设置响应头，完成文件下载。

画面13：
- 代码：在ExcelExportUtil.java中，继续编写导出Excel的代码。
- 代码：设置响应头，完成文件下载。

画面14：
- 代码：在ExcelImportUtil.java中，编写导入Excel的代码。
- 代码：定义了convertAttrType方法，用于将单元格值转换为对象属性值。
- 代码：判断字段类型，如果是String类型，则调用getValue方法获取值。
- 代码：将值添加到列表中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    //1.调用业务层
    List<EmployeeReportResult> list = userService.findReport(companyId, month);
    //2.加载模板
    Resource resource = new ClassPathResource("excel-template/hr-demo.xlsx");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //3.创建工作簿
    Workbook wb = new XSSFWorkbook(fis);
    //4.获取工作表
    Sheet sheet = wb.getSheetAt(0);
    //5.抽取公共样式
    Row row = sheet.getRow(0);
    CellStyle styles[] = new CellStyle[15];
    for(int i=0;i<row.getLastCellNum();i++) {
        Cell cell = row.getCell(i);
        styles[i] = cell.getCellStyle();
    }
    //6.填充数据
    int rowIndex = 2;
    for(EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
        Cell cell = null;
        for(int i=0;i<15;i++) {
            cell = row.createCell(i);
            cell.setCellValue(employeeReportResult.getUserID());
            cell.setCellStyle(styles[i]);
        }
    }
    //7.完成下载
    ByteArrayOutputStream os = new ByteArrayOutputStream();
    wb.write(os);
    DownloadUtils.download(os, response, returnName + "人事报表.xlsx");
}
```

画面2：
```java
//7.完成下载
ByteArrayOutputStream os = new ByteArrayOutputStream();
wb.write(os);
DownloadUtils.download(os, response, returnName + "人事报表.xlsx");
```

画面3：
```java
//6.填充数据
int rowIndex = 2;
Cell cell = null;
for(EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserID());
    cell.setCellStyle(styles[0]);
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    cell.setCellStyle(styles[1]);
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    cell.setCellStyle(styles[2]);
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    cell.setCellStyle(styles[3]);
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    cell.setCellStyle(styles[4]);
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
    cell.setCellStyle(styles[5]);
    cell = row.createCell(6);
    cell.setCellValue(employeeReportResult.getSalary());
    cell.setCellStyle(styles[6]);
    cell = row.createCell(7);
    cell.setCellValue(employeeReportResult.getBirthDay());
    cell.setCellStyle(styles[7]);
    cell = row.createCell(8);
    cell.setCellValue(employeeReportResult.getZodiac());
    cell.setCellStyle(styles[8]);
    cell = row.createCell(9);
    cell.setCellValue(employeeReportResult.getEntryTime());
    cell.setCellStyle(styles[9]);
    cell = row.createCell(10);
    cell.setCellValue(employeeReportResult.getLeaveType());
    cell.setCellStyle(styles[10]);
    cell = row.createCell(11);
    cell.setCellValue(employeeReportResult.getReasonsForLeaving());
    cell.setCellStyle(styles[11]);
    cell = row.createCell(12);
    cell.setCellValue(employeeReportResult.getResignationTime());
    cell.setCellStyle(styles[12]);
}
```

画面4：
- 无代码，为Excel表格。

画面5：
- 无代码，为IDE自动补全提示。

画面6：
- 无代码，为IDE自动补全提示。

画面7：
- 无代码，为桌面截图。

画面8：
```java
package com.ihrm.domain.poi;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface ExcelAttribute {
    /** 对应的列名称 */
    String name() default "";

    /** 列序号 */
    int sort() default 0;

    /** 字段类型对应的格式 */
    String format() default "";
}
```

画面9：
- 无代码，为文件夹结构截图。

画面10：
- 无代码，为项目结构截图。

画面11：
```java
package com.ihrm.common.poi;

import java.lang.reflect.Field;
import java.util.List;

/**
 * 基于模板打印的方式导出
 */
public class ExcelExportUtil<T> {
    private int rowIndex; // 表头行索引
    private int styleIndex; // 样式索引
    private Class<T> clazz; // 对象中的所有属性
    private Field fields[]; //
