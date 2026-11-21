# 07-自定义工具类：工具类介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\07-自定义工具类：工具类介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 9分26秒（音频 566s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经完成了报表的打印的工作不管是采用我们之前传统的方式还是模板打印的这种方式各位都会发现它有一个比较不好的一个点是什么就是我们今天要操作是人事报表的一些情况明天要操作其他报表如果都是基于模板打印的话你会发现我整个代码的操作逻辑基本上都是差不多首先第一件事加载模板
[00:31] 那加载好了模板接着第二件事根据模板是不是创建我们这个工作部那接下来呢读取工作表那抽取公共的样式这些代码是不是应该都是差不多的一些内容啊并且呢底下构造单元格的这些过程也都是差不多的甚至这个下载都是一模一样的那我们可不可以以工具类的形式哎把它封装起来呢各位
[00:56] 那当然可以了那只需要遵照我们的一定的约定比如说咱们就用模板打印举例那首先提供模板那在这边需要指定根据模板的文件流形成我们的工作部那接着根据你这个样式在那地底行我们去抽取公共的样式底下这是比较困难的一项也就是我们要抽取工具类上面这些都差不多但是我们对单元格的一个复制情况可能
[01:25] 就不太理想没错吧那所以我们要想抽取工具类重点关注的其实就是对单元格内容复制的这个流程那对单元格复制的这个流程呢其实到目前为止它还有一个比较大的一个问题是这样的就是说呢目前而言我们想要得到的人事报表的数据是这样的是这样的那我们从零到几一直复制到12你会发现这个代码写起来太啰嗦
[01:57] 没错吧那有的朋友就说了我现在呢通过模板这个是我们的一个模板当然这个模板看起来不太好看啊我们直接就定位到我们模板了那你会发现呢我们其实有一条模板数据那这个模板数据其实已经可以知道我的总的单元格的数量究竟是多少那能够得到单元格数量那我可不可以在这边以4循环的形式4循环动态的进行构造呢比如说呢写一个int
[02:28] 勾等于0勾小于比如说勾小于好了我们叫做注意勾小于什么可以小于我们叫做肉点get last cell number这不就可以了当然了你不想写肉也可以我们这个样式里面是不是也有这些相应的内容样式点lens都可以吗好了接着勾加加勾加加之后中间里面的代码部分要去创建每一个格子没问题根据勾创建
[02:59] 这个没问题那接着可以设置每一个格子的样式是不是也没问题这边写的就是勾了那接下来呢最主要的问题集中在哪就是这个单元格复制没错吧那对于这个单元格复制各位有什么想法你怎么就知道循环到0的时候应该要用到单元格里面的对象里面打点get idu的id
[03:33] 那你怎么知道到1的时候要用user id你怎么知道到2的时候要用username呢没错吧并且我们一会要封装对象要封装工具类那封装工具类的时候就不可能直接拿这个什么report result这个对象了你可能是别的对象是意思吧所以接下来考验我们工具类的就这么两个点第一个点就是我们的格子单元格格位置
[04:04] 和我们的属性要能挂钩第二个点考量的就是我们可以动态的使用对象属性复制那接下来我们就可以思考了这个单元格位置和属性如何挂钩那如何挂钩我可不可以在需要用到的属性上边写一个注解那这个注解里面呢是不是可以给它定义上我的位置那这个其实也能解决那第二个动态的使用对象属性那我们这边就不得不提反射
[04:36] 没错吧所以呢咱们要想对这个内容呢我们要做一个工具类的一个处理的话就需要各位满足反射满足自定义注解的一些常规的一些基础的一些应用好了这些呢我们对自定义的一些工具类的一些分析呢其实跟各位简单的说了一下那这个工具呢由于时间有限在这边呢就不带着各位一行一行去写了在今天的这个资料当中呢其实我已经把
[05:05] 我封装好的工具类给各位准备好了在代码当中工具类里面呢分成了这么三个其中第一个Excel AttributeExcel Attribute呢可以打开它简单的来看一下这个呢其实就是一个自定义注解那这个注解呢通过上面的声明运行时注解是定义到属性上边的那其中有一个Salt指的是我当前这个属性的序列号或者编号那也跟这个报表里面的有关系比如说呢U的ID
[05:36] 是一个属性我在属性上给它来一注解注解里面写一salt写上0那这样一来它是不是对应的就是低劣能理解吧好了那接下来呢还有两个工具类这两个工具类呢也简单的看一下还有一个叫做excelexportexcelimport那这两个工具类见名之意export是用来对应导出的好了这边import是用来进行我们叫导入的就是用来加载的OK那好了这些呢工具类呢和各位
[06:07] 简单的说了一下那我们如果要想使用的话很简单注意这个注解这个要放到什么地方啊因为我们知道对于注解的这个工具类呢对于注解哪使用是不是就是我们的模型对象里面所以我在模型对象当中把这个工具类导入进来了在模型的这个工程里面把这个工具类把这个注解导入进来了那接下来common包下是我们真真正正的导入和导出的
[06:38] 这么两个工具类那这个导入导出的工具类先看这个export那对于这个export来说呢这个里面的代码比较简单比较简单里面有rowindex有styleindex有class还有fields那这几个属性呢简单的和各位做一个交代rowindex啥意思指的是我写入数据的其实行那styleindex指的是我要抽取的样式所在的行也就是说前两个第一个
[07:07] 你要往这个模板里面写数据从第几行开始写01那我这边是不是就应该是第二行那我们的这些要抽取的公共样式在哪012是不是也在第二行OK那好了我们说过了用的反射就不得不提class字节码你要对使用哪个对象就把哪个对象的class字节码勾到过来还有failedfailed这个不需要我们关注我们通过字节码得到里面的所有属性了好了所以对于我们要想new这个对象直接new出来
[07:36] 好了NEO出来之后呢接下来底下呢就是我们进行文件导出的这么一个方法那文件导出的这个方法呢也是基于模板的形式来做的模板打印那模板打印首先你给我传递过来一个input stream这个是我们的模板的文件流这个不用解释了里面的代码基本上都是一模一样好了这边呢抽取公共样式抽取公共样式这个我抽取了一个小的方法和我们之前写的代码基本上都是一样的那中间这个部分就用到了反射
[08:06] 用到了反射用到了我们自定义注解比较各位注意来看这个比较就是说当前我循环的这个i各位来看这边不是跟我刚才给各位入门的那个跟各位引入的那个放循环一样吗i小于style.lengthstyle是我们所有的样式一共有几列一共有几个格子它就有多少个样式它就有多少长度那我这边小于开始做判断那接下来呢这边cell不说了create cell不说了
[08:37] 注意看底下这个异域化循环异域循环那i就是当前格子是第几个那ea.saltea就是我们属性上的注解那属性上面的注解如果它俩匹配的话我就反射调用它的get方法就用get方法把它转化成死菌类型
[08:59] 再对它进行复制其实就是这个意思OK好了这个工具类呢和各位简单的说了一下当然除了这个工具类还有一个就是import也就是叫做导入的这么一个工具类那对于这个导入的工具类呢其实这里面的代码呢比较简单这个比较简单也就不带着各位一行一行的去读取了其实也是借助注解和我们这边这个工具类的形式来做的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

