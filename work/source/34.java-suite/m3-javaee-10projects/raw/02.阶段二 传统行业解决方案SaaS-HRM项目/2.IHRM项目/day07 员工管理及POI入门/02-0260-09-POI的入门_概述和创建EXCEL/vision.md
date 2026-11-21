# 画面线理解：09-POI的入门：概述和创建EXCEL

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\09-POI的入门：概述和创建EXCEL_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:41, 01:26, 01:56, 03:02, 03:56, 05:01, 06:02, 07:45, 08:13, 09:33, 10:28, 11:30, 12:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:52:29

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Apache POI 库在 Java 中创建和读取 Excel 文件，包括环境搭建、依赖配置、API 结构说明和基本操作示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面“3 POI的入门操作”，其中包含 POI 依赖的 Maven 配置代码块。
画面 2: 在 IntelliJ IDEA 中打开名为 “ihrm_parent” 的项目。
画面 3: 在 IntelliJ IDEA 中点击“File”菜单，准备进行项目设置或新建操作。
画面 4: 在 Notepad++ 中显示 POI 依赖的 Maven 配置代码，光标位于最后一个 </dependency> 标签后。
画面 5: 显示 Windows 桌面，桌面上有 “黑马程序员” 和 “博学谷” 的标志。
画面 6: 在 Windows 资源管理器中，显示 “excel” 文件夹，其中包含一个名为 “test.xlsx” 的文件。
画面 7: 展示 PPT 页面“3.4 基本操作”，其中包含一个表格，列出了 POI 的主要 API 及其对应含义。
画面 8: 在 PPT 页面“3.4 基本操作”上，鼠标悬停在 “CellStyle” 项上，同时任务栏中显示一个 IntelliJ IDEA 的窗口。
画面 9: 在 IntelliJ IDEA 中，显示 POI 的 Workbook 接口的反编译代码，其中包含常量定义和方法声明。
画面 10: 在 IntelliJ IDEA 中，显示 POI 的 Workbook 接口的反编译代码，鼠标悬停在 “XSSFWorkbook” 类上，下方显示其依赖的 Maven 依赖项。
画面 11: 在 Microsoft Excel 中，显示一个名为 “test”的工作簿，其中 A3 单元格包含文本“传智播客”。
画面 12: 在 IntelliJ IDEA 中，显示 Java 代码，用于创建一个 XSSFWorkbook 对象并创建一个名为 “test”的 Sheet。
画面 13: 在 IntelliJ IDEA 中，显示 Java 代码，用于读取一个名为 “E:\excel\poi\test.xlsx” 的文件并写入到工作簿中。
画面 14: 在 Windows 资源管理器中，显示 “test.xlsx” 文件，其大小已从 9 KB 更新为 4 KB，表明文件已被修改。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
<dependencies>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml-schemas</artifactId>
<version>4.0.1</version>
</dependency>
</dependencies>

画面 4:
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml</artifactId>
<version>4.0.1</version>
</dependency>
<dependency>
<groupId>org.apache.poi</groupId>
<artifactId>poi-ooxml-schemas</artifactId>
<version>4.0.1</version>
</dependency>
</dependencies>

画面 9:
package org.apache.poi.ss.usermodel;
import ...
public interface Workbook extends Closeable, IterableSheet {
int PICTURE_TYPE_EMBED = 2;
int PICTURE_TYPE_WMF = 4;
int PICTURE_TYPE_PICT = 5;
int PICTURE_TYPE_JPEG = 6;
int PICTURE_TYPE_PNG = 7;
int getActiveSheetIndex();
void setActiveSheet(int var1);
int getFirstVisibleTab();
void setFirstVisibleTab(int var1);
void setSheetOrder(String var1, int var2);
void setSelectedTab(int var1);
void setSheetName(int var1, String var2);
}

画面 10:
XSSFWorkbook (org.apache.poi.hssf.usermodel)
XSSFWorkbook (org.apache.poi.xssf.usermodel)
XSSFWorkbook (org.apache.poi.xssf.streaming)
XSSFWorkbook (org.apache.poi.xssf.usermodel)

画面 12:
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
/**
* 使用POI创建Excel
*/
public class PoITest01 {
public static void main(String[] args) throws FileNotFoundException {
//1.创建工作簿
Workbook wb = new XSSFWorkbook(); //2007版本
Sheet sheet = wb.createSheet("test");
//3.文件流
FileInputStream pis = new FileInputStream(name: ""); //4.写入文件
}

画面 13:
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
/**
* 使用POI创建Excel
*/
public class PoITest01 {
public static void main(String[] args) throws Exception {
//1.创建工作簿
Workbook wb = new XSSFWorkbook(); //2007版本
Sheet sheet = wb.createSheet("test");
//3.文件流
FileInputStream pis = new FileInputStream(name: "E:\\excel\\poi\\test.xlsx");
//4.写入文件
wb.write(pis);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7:
标题：3.4 基本操作
子标题：3.4.1 创建Excel
表格内容：
| API名称 | 含义 |
| --- | --- |
| Workbook | Excel的文档对象，针对不同的Excel类型分为：HSSFWorkbook (2003) 和 XSSFWorkbook (2007) |
| Sheet | Excel的表单 |
| Row | Excel的行 |
| Cell | Excel的格子单元 |
| Font | Excel字体 |
| CellStyle | 格子单元样式 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
