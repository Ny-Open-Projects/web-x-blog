# 模板、数据、填充：JasperReports 生成 PDF 的五步开发清单

生命周期三阶段（设计、执行、输出）听懂了，落到动手开发时又冒出一堆新问题：模板文件从哪来？编译是不是每次都要写代码？数据从哪构造？真正要让业务代码操心的只有哪几步？把课程 demo 从编译到预览完整跑一遍，产物一个一个看清楚，再对着完整流程清单收拢，这几个问题就有了明确答案。

## 先给结论

- 完整开发流程五步：制作模板、模板编译、构造数据、填充模板、输出预览。
- 编译与预览两步由 Jaspersoft Studio 工具代劳，业务代码里真正常写的只有三件事：画模板、构造数据、填充。
- 一套流程产出三种文件：`.jrxml`（XML 模板）、`.jasper`（编译后的二进制）、`.jrprint`（填充完数据的打印对象）。
- 生命周期底层不过三件事：解析 XML、处理二进制模板数据、操作输出流，demo 代码以后基本不用再手写。
- Web 应用里最常见的形态是：classpath 读 `.jasper`，`JasperFillManager.fillReport` 填充，`JasperExportManager.exportReportToPdfStream` 直接写进响应流。

## 一、把 demo 跑一遍，产物逐个看清楚

核心骨架是三个方法加一个 `main`（课程真实代码，包名改为 `com.example.jr`，文件路径改为中性写法）：

```java
package com.example.jr;

import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.view.JasperViewer;

import java.util.HashMap;

public class PDFTest {

    public static void main(String[] args) {
        //依次执行：编译 → 填充 → 预览
        createJasper();
        createJrprint();
        showPdf();
    }

    //1.将 jrxml 模板编译为 jasper 文件
    public static void createJasper(){
        try{
            String path = "D:/data/test01.jrxml";
            JasperCompileManager.compileReportToFile(path);
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    //2.将 jasper 文件和数据进行填充，获取 jrprint
    public static void createJrprint(){
        try{
            String path = "D:/data/test01.jasper";
            //通过空参数和空数据源进行填充
            JasperFillManager.fillReportToFile(path,new HashMap(),new JREmptyDataSource());
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    //3.预览
    public static void showPdf(){
        try{
            String path = "D:/data/test01.jrprint";
            JasperViewer.viewReport(path,false);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
```

按顺序执行，磁盘上的文件一步步变化：

**第一，`createJasper` 之后多出 `test01.jasper`。** 它是把 XML 模板编译出来的二进制文件，此时 PDF 的雏形已经有了，只是里面还没有数据。

**第二，`createJrprint` 之后多出 `test01.jrprint`。** `JasperFillManager.fillReportToFile` 的三个参数分别是模板路径、参数 Map、数据源；演示阶段用空 `HashMap` 和 `JREmptyDataSource` 占位，填完数据 `.jrprint` 就成了包含全部内容的报表打印对象。三个文件表面看都是二进制，代表的却是三个不同阶段的产物，不能混着用。

**第三，`showPdf` 弹出预览窗口。** 页头是模板里声明的图片和标题文字，页脚输出一行小字，和 JRXML 里设计的内容一一对应。

```mermaid
flowchart LR
    A["test01.jrxml<br/>XML 模板"] -->|JasperCompileManager 编译| B["test01.jasper<br/>二进制模板"]
    B -->|JasperFillManager 填充数据| C["test01.jrprint<br/>报表打印对象"]
    C -->|JasperViewer 预览或导出| D["PDF、HTML、XLS 等"]
    style A fill:#eef,stroke:#88f
    style D fill:#efe,stroke:#8c8
```

这张图串起了整条产物流水线，每一个箭头都对应 demo 里的一个方法调用。躲在箭头背后的工作是：编译时解析 XML，填充时处理二进制模板与数据，输出时做流的读写。理解这三层成本，才能明白为什么引擎要把一次设计编译后反复填充，而不是每次都从头解析模板。

## 二、五步流程清单：谁做、要不要关注

把 demo 的经验收拢成完整开发流程，每一步的性质并不相同：

| 步骤 | 做什么 | 产物 | 谁来做 | 重点关注 |
|---|---|---|---|---|
| 1 制作模板 | 画布局：页头、页脚、详情区、字体 | `.jrxml` | 开发者用 Jaspersoft Studio | 是 |
| 2 模板编译 | XML 编译成二进制 | `.jasper` | 工具自动完成 | 否 |
| 3 构造数据 | 准备 Map、JavaBean 或 SQL 结果集 | 数据集合 | 开发者写业务代码 | 是 |
| 4 填充模板 | 数据灌进模板 | `.jrprint` | 开发者调 `JasperFillManager` | 是 |
| 5 输出预览 | 导出 PDF 或弹窗预览 | 目标文件 | 工具或导出 API | 视场景 |

**第一，模板不做不行。** 报表长什么样、哪里放字段、哪里放统计图，全在设计阶段定死，这一步谁都替代不了。

**第二，编译不用操心。** Jaspersoft Studio 在图形化界面里画完模板就能预览，保存时自动完成编译，手写 `JasperCompileManager` 的调用在工程里几乎没有出场机会。

**第三，数据和填充才是日常代码的主战场。** 数据从哪来、按什么结构组织，是业务问题；用哪种 `JRDataSource` 实现接住这些数据，是工程问题。这两步的代码天天在写，也是排错最集中的地方。

所以日常开发的关注点可以压成一句话：模板用工具画，数据自己构造，填充自己调用。手写 JRXML 的苦力活交给了工具，生命周期代码只在理解原理时写一遍。

## 三、工程里的形态：填充加导出两行核心

真实 Web 工程里，编译已被工具完成，剩下的就是读模板、填充、往响应流里写。课程配套的 Spring Boot 工程给出了标准形态（包名改为 `com.example`）：

```java
@RestController
public class JasperController {

    @GetMapping("/testJasper")
    public void createPdf(HttpServletResponse response) throws IOException {
        //1.读取 classpath 下的 jasper 模板（编译工作已在工具里完成）
        Resource resource = new ClassPathResource("templates/test.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        ServletOutputStream os = response.getOutputStream();
        try {
            //2.填充数据：参数 Map 加数据源，得到 JasperPrint
            JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
            //3.以 PDF 形式输出到响应流
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException e) {
            e.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

和 demo 相比有两处变化：模板不再从磁盘路径读，而是从 classpath 加载，随工程一起打包发布；产物不再落盘成 `.jrprint` 文件，而是留在内存里由导出器直接写进 HTTP 响应，浏览器收到 `Content-Type: application/pdf` 的流即可预览或下载。这正是五步流程在服务端的真实投影：设计、编译、预览三步在工具里，构造数据、填充输出两步在代码里。

## 常见误区

- **在代码里维护模板样式。** 用字符串拼 JRXML、或者每次调 `JasperCompileManager` 现场编译，都是把工具的活揽回自己身上。正确姿势是模板交给 Jaspersoft Studio 画好、编译好，代码只负责填充。
- **拿 `.jrxml` 直接去填充。** `fillReport` 系列方法吃的是编译后的 `.jasper`（或内存中的 `JasperReport` 对象），直接传 XML 模板路径会报错。模板改过之后必须重新编译，预览和运行用的都是新编译产物。
- **把报表数据源当成数据库连接池。** JasperReports 语境里的「数据源」指填充内容的来源，`JREmptyDataSource`、`JRBeanCollectionDataSource`、JDBC 连接都是它的实现，选型依据是数据形态，与项目的数据库连接池是两回事。
- **中文输出空白或方块。** 模板指定了华文宋体，但运行环境没有注册字体扩展，PDF 渲染不出来。需要把字体文件、`fonts.xml`、`jasperreports_extension.properties` 一起放进 classpath。

## 面试可能被问到的问题

1. 面试官追问：「用 JasperReports 生成一份 PDF 报表，完整流程是什么？」
   答：五步。用 Jaspersoft Studio 制作模板得到 `.jrxml`；工具自动编译成 `.jasper`；业务代码构造数据（Map、JavaBean 集合或 SQL 结果集）；调用 `JasperFillManager` 把数据填充进模板得到 `JasperPrint`；最后按需导出 PDF 或写进响应流。开发者重点关心的只有模板、数据、填充三件事。

2. 面试官追问：「Jaspersoft Studio 在流程里承担了哪些工作？」
   答：它以图形化方式绘制模板，替代手写 JRXML；同时承担了模板编译和本地预览。也就是说生命周期里设计、编译、输出预览三个环节都可在工具内完成，业务代码只保留构造数据与填充输出。

3. 面试官追问：「`.jasper` 和 `.jrprint` 的区别是什么？」
   答：`.jasper` 是模板编译后的二进制文件，只有布局没有数据；`.jrprint` 是数据填充完成后得到的报表打印对象，布局与数据齐备，只有它能直接被导出或预览。前者是骨架，后者才是成品。

4. 面试官追问：「模板改了，页面输出却没变化，怎么排查？」
   答：常见原因是改的是 `.jrxml` 而工程加载的还是旧的 `.jasper`。模板修改后要在工具里重新编译并更新发布到 classpath 的编译产物；确认代码加载的路径指向新文件后再验证输出。

5. 面试官追问：「Web 应用里 PDF 报表一般怎么输出给用户？」
   答：从 classpath 读取编译好的 `.jasper`，用 `JasperFillManager.fillReport` 填充数据得到 `JasperPrint`，再由 `JasperExportManager.exportReportToPdfStream` 写进 `HttpServletResponse` 的输出流，浏览器直接预览或下载，全程不产生中间落盘文件。

6. 面试官追问：「生命周期 demo 那套编译填充代码，实际工程还要写吗？」
   答：编译基本不写了，由模板工具完成；填充和导出是核心，但要按工程形态封装，比如统一加载模板、按数据类型选择数据源实现、异常与流关闭集中处理。写 demo 的价值在于看清每一步产物，出了问题能定位到具体阶段。

## 配套资料

- 生命周期演示代码：`materials/code/02/day09 图片上传及Jasper/图片上传及Jasper/资源/资源/生命周期测试/PDFTest.java`
- Spring Boot 报表工程：`materials/code/02/day10-用户档案PDF报表/day10-用户档案PDF报表/代码/jasper-springboot/`
  （含 `pom.xml`、`JasperController.java`、`JasperApplication.java`，文中包名已改为 `com.example`）
- 中文字体扩展配置：`materials/code/02/day09 图片上传及Jasper/图片上传及Jasper/资源/资源/乱码问题/`
