# 画面线理解：01-数据填充：数据填充的两种方式介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\01-数据填充：数据填充的两种方式介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:38, 01:48, 01:51, 01:52, 01:57, 02:23, 03:11, 03:16, 03:52, 03:59, 04:08, 04:14, 04:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:38:20

1) 这一组画面整体在讲什么（一句话）：
讲解如何使用 JasperReport 实现动态数据填充到 PDF 报表，重点介绍参数 Map 填充数据的方式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文件资源管理器，当前路径为“ihrm/day10”，其中包含“代码”、“测试”、“SaaS-HRM--第10章.pdf”等文件夹和文件。
画面2：PDF 文档第10章“用户档案PDF报表”的第1页，标题为“第10章 用户档案PDF报表”，列出学习目标：理解数据填充的两种方式、熟练构造分组报表、熟练构造Chart图形报表、实现个人档案的PDF输出。正文介绍将研究如何填充动态数据到PDF报表。
画面3：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2内容相同，但页面滚动条位置略有不同。
画面4：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3内容相同，但页面滚动条位置略有不同。
画面5：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4内容相同，但页面滚动条位置略有不同。
画面6：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，包含一个 @RestController 注解的类，其中定义了 createPdf 方法，用于生成 PDF 报表。
画面7：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，与画面6相同，但光标位置不同。
画面8：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4、5内容相同，但页面滚动条位置略有不同。
画面9：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4、5、8内容相同，但页面滚动条位置略有不同。
画面10：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，与画面6、7内容相同，但光标位置不同。
画面11：JasperSoft Studio 软件界面，显示项目结构“Project E”包含“MyReports”和“TestReports”两个文件夹。
画面12：JasperSoft Studio 软件界面，与画面11内容相同，但光标位置不同。
画面13：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，与画面6、7、10内容相同，但屏幕底部显示了多个窗口的预览，包括 JasperSoft Studio 和 PDF 文档。
画面14：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4、5、8、9内容相同，但页面滚动条位置略有不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6、7、10、13 中的代码：
```java
package cn.itcast.controller;

import org.springframework.web.bind.annotation.*;

@RestController
public class JasperController {

    @GetMapping("/test.jasper")
    public void createPdf(HttpServletResponse response) throws IOException {
        //1.引入jasper文件
        Resource resource = new ClassPathResource("templates/test.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        //2.创建JasperPrint,向jasper文件中填充数据
        ServletOutputStream os = response.getOutputStream();
        try {
            // fis: jasper 文件输入流
            // parameters: 向模板中输入参数
            // dataSource: 数据源
            JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
            //3.将JasperPrint PDF格式输出
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException e) {
            e.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2、3、4、5、8、9、14 中的 PPT 标题和内容：
- 标题：“第10章 用户档案PDF报表”
- 子标题：“1 数据填充”
- 子标题：“1.1 参数Map填充数据”
- 子标题：“1.1.1 模板制作”
- 子标题：“（1）创建新模板，删除不需要的Band”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
