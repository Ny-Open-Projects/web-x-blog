# 08-自定义工具类：工具类测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\08-自定义工具类：工具类测试_【海量资源尽在 ubkz.com】.mp4
- 时长 7分31秒（音频 452s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那刚才的工具类呢和各位做了一个简单的介绍那接下来呢我们就可以使用这个工具类来去测试一把改造我们之前的导出的这个工程OK好了应该如何去做呢首先第一件事我们就需要是不是在这个对象上边使用注解的形式给他定义出来属性和我们Excel导出这个列的一个关系啊
[00:27] 那我们都知道对于第一连第一连来说第一连来说是我们的user id用户姓名那好了我们开始第一个我们用的是一个excel attribute这么一个注解好了里面有个salt属性等于我们来一个0就可以了好了那第一个我们搞定了那接下来呢就是第二个属性name来一一好了还有手机号来一二那接下来呢就是最高学历三继续国家地区四
[00:59] 护照号五好了还有机关六好了这边呢有生日跟属相七八好了那入职时间继续找一下入职时间入职时间这个属性实在是太多了这个这个这个这个找起来就有点麻烦啊入职time of在这呢这是第几忘了01
[01:51] 二三四五六七八九OK九太多了都有点乱了九好了那接下来呢继续咱们往下去添加注解离职时间十二最后一个嘛离职原因十一离职类型OK是那这样一来呢我这些全部都以注解的形式替换掉了那全部都搞好定了之后那我们接着就是把我们之前写过的这段代码呢就可以给它注释起来了
[02:25] 在这边就可以给它全部都注视起来了当然了我们要留下这么一些内容那首先呢我们需要数据那接着我们需要是不是这个文件的这个input stream这个输入流啊那接下来呢我们可以通过第三步通过工具类直接来下载文件那通过工具类下载文件其实比较简单直接new一个我们叫做excelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelexcelex
[03:01] 好了接下来这里面可以传递我们的构造参数class row跟style index我们都知道我们这边的要写入数据的行号来看要写入数据的行号012我们的模板的样式是不是也在第二行所以012后面写两个2接着我们添加了注解的类在哪就是我们要封装的对象Ctrl C拿过来打点class
[03:30] OK 逗号二 逗号二 OK那这样一来我们整个的工具类下载就已经搞好了那接下来呢我们可以重新启动一下好了 重新启动之后我们再去下载一下看一下咱们的测试工具类究竟好不好使那我们的注解呢都替换成功了之后接着呢我们就回到代码的这个部分好了 接下来呢回到我们的代码部分那我们现在对象上面的这些注解全部都定义好了
[04:26] 接下来回到我们的代码部分咱们就开始使用工具类的形式完成我整个Excel的一个导出基于导出这些代码我们就不需要了当然了我们前两步还需要因为我们的工具类其实还是需要数据还是需要我们的模板我们的文件输入流的好了接下来我们就剩第三件事要做了通过工具类完成下载
[04:54] 那通过工具类完成下载这个很简单new一个我们叫做excelexcelexportutu好了范型不要了注意里面呢需要一些构造方法这些构造方法的参数呢其中有我们配置了注解类的字节码还有我们我们设置数据的骑士行号以及我们采取采集样式的这个样式的行号那对于咱们这个案例来说其实就是第三行
[05:25] 那我们的样式也在第三行那看这个一个赛网呢可能对各位可能会造成一点点小小的困扰那在这边呢打开我们今天的这个资料这个里面才是我们真正的这个模板的这个样式啊好了各位来看我们要做的事情就是从从过第三行采取采集到样式接着我们一会写数据的时候第三行同样也要写入些新的数据嘛所以我这边写所以012是不是写两个2就可以啊
[05:54] 好了这边两个2给它设置上当然了第一个呢我们的class也应该写上配置了注解类的字节码打点classOK那这样一来我对象初始化已经搞定了剩下的就是调用它的方法isPart那我们这个一个Part的方法呢需要这么如下几个参数我把这些参数呢也copy过来OK好了第一个参数呢我们叫做responseresponse对象A能提供出来好了第二个就是我们的模板模板的输入流也有
[06:28] 好了接着第三个我们的数据list拿过来OK接着第四个就是我们输入的文件名称那输入的文件名称呢这个比较简单我们之前写过Ctrl C替换过来好了那这样一来我这个代码下载就已经搞定了那接下来的事情呢就是可以重新启动一下我们这个微服务来看一下效果如何OK这个启动稍微有点点长啊
[07:01] 各位耐心等待一下那我们现在先回到页面刷新一把静待它启动成功完成我们Excel导出的这个功能来321走抱歉系统繁忙来321走导出好了来我们一起看一下03那这样一来是不是数据也能够通过工具类把它导出诶折出来啊OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

