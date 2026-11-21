# 画面线理解：08-自定义工具类：工具类测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\08-自定义工具类：工具类测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:34, 01:07, 01:29, 01:48, 02:19, 02:57, 03:37, 04:01, 04:29, 05:21, 05:55, 06:55, 07:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:09:52

1) 这一组画面整体在讲如何使用 Java 代码结合 Excel 模板实现员工数据的导出功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 EmployeeReportResult 类的定义，包含多个私有字段，如 postalAddress、contactMobilePhone、personalMailbox 等。
画面2：展示 EmployeeReportResult 类的注解，包括 @AllArgsConstructor、@NoArgsConstructor、@Getter、@Setter、@ToString 等。
画面3：展示 Excel 文件“2018年2月份人事报表”，包含员工编号、姓名、手机、最高学历、国家地区、护照号、薪资、生日、属相、入职时间、离职类型、离职原因、离职时间等字段。
画面4：展示 EmployeeReportResult 类的字段定义，包括 emergencyContact、emergencyContactNumber、socialSecurityComputerNumber、providentFundAccount 等。
画面5：展示 Excel 文件“2018年2月份人事报表”，鼠标光标位于“薪资”列的单元格上。
画面6：展示 ExcelExportUtil 类的导出方法，包括创建工作簿、读取模板样式、设置单元格值等。
画面7：展示 EmployeeController 类的导出方法，使用 ExcelExportUtil 工具类进行导出。
画面8：展示 EmployeeController 类的导出方法，使用 ClassPathResource 加载模板文件。
画面9：展示 ExcelExportUtil 类的构造方法，用于初始化类的属性。
画面10：展示 EmployeeController 类的导出方法，使用 ExcelExportUtil 工具类进行导出。
画面11：展示 ExcelExportUtil 类的构造方法，用于初始化类的属性。
画面12：展示 ExcelExportUtil 类的构造方法，用于初始化类的属性。
画面13：展示 EmployeeController 类的导出方法，使用 ExcelExportUtil 工具类进行导出。
画面14：展示 Excel 文件“2018年2月份人事报表”，鼠标光标位于“姓名”列的单元格上。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```java
package com.ihrm.domain.employee.response;
import com.ihrm.domain.EmployeeReportResult;
@AutoWired (org.springframework.beans.factory.annotation)
@NoArgsConstructor
@RequiredArgsConstructor
@RequestMapping
@CrossOrigin
@Query
@PathVariable
@Configuration
@ExcelAttribute
@Setter
@Getter
@ToString
```
画面2：
```java
@AutoWired (org.springframework.beans.factory.annotation)
@NoArgsConstructor
@RequiredArgsConstructor
@RequestMapping
@CrossOrigin
@Query
@PathVariable
@Configuration
@ExcelAttribute
@Setter
@Getter
@ToString
```
画面3：
无代码。
画面4：
```java
private String postalAddress;
private String contactMobilePhone;
private String personalMailbox;
private String emergencyContact;
private String emergencyContactNumber;
private String socialSecurityComputerNumber;
private String providentFundAccount;
```
画面5：
无代码。
画面6：
```java
public void export(HttpServletResponse response, InputStream is, List<T> objs, String fileName) throws Exception {
    //1.根据模板创建工作簿
    XSSFSheet workbook = new XSSFSheet(is);
    //2.读取工作表
    Sheet sheet = workbook.getSheetAt(index);
    //3.提取公共的样式
    CellStyle[] styles = getTemplateStyles(sheet.getRow(styleIndex));
    //4.获取公共的样式
    AtomicInteger dataSI = new AtomicInteger(rowIndex);
    for (T t : objs) {
        //获取数据行
        Row row = sheet.createRow(dataSI.getAndIncrement());
        //获取单元格
        for (int i = 0; i < styles.length; i++) {
            Cell cell = row.createCell(i);
            cell.setCellStyle(styles[i]);
            for (Field field : fields) {
                if (field.isAnnotationPresent(ExcelAttribute.class)) {
                    field.setAccessible(true);
                    ExcelAttribute ea = field.getAnnotation(ExcelAttribute.class);
                    if (a == ea.sort()) {
                        cell.setCellValue(field.get(t).toString());
                    }
                }
            }
        }
    }
    fileName = URLEncoder.encode(fileName, "UTF-8");
    response.setContentType("application/octet-stream");
    response.setHeader("content-disposition", "attachment;filename=" + new String(fileName.getBytes(), "ISO8859-1"));
    workbook.write(response.getOutputStream());
}
```
画面7：
```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.ss.usermodel.CellStyle;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.XSSFCell;
import org.apache.poi.ss.usermodel.XSSFRow;
import org.apache.poi.ss.usermodel.XSSFSheet;
import org
