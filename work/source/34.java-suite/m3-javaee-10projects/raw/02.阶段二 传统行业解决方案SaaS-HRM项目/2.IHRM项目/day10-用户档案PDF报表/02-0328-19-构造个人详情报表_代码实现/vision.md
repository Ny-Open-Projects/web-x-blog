# 画面线理解：19-构造个人详情报表：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\19-构造个人详情报表：代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:35, 00:51, 01:19, 01:41, 02:07, 03:10, 03:32, 04:33, 05:12, 05:43, 06:08, 06:45, 07:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:48:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过控制器调用服务层数据，填充 Jasper 报表模板并导出 PDF 文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 EmployeeController.java 中，展示 pdf 方法的代码，用于读取 jasper 文件并导出 PDF。
画面 2: 在项目结构中，展示 templates 目录下的 profile.jrxml 文件，以及 application.yml 配置文件。
画面 3: 展示一个 Word 文档，内容为“员工的个人信息：下载员工的pdf详情资料”，并列出“1.模板”、“2.数据来源”、“3.填充数据”、“4.导出到map集合参数”等步骤。
画面 4: 在 EmployeeController.java 中，展示 pdf 方法的代码，注释中提到“用户岗位信息模板”。
画面 5: 在 EmployeeController.java 中，展示 pdf 方法的代码，通过 @Autowired 注入 ArchiveService，并弹出 UserCompanyPersonalService 的方法列表。
画面 6: 在 EmployeeController.java 中，展示 pdf 方法的代码，弹出 UserCompanyJobsService 的方法列表。
画面 7: 在数据库管理工具中，展示一个 Blob 字段的插入对话框，URL 为 http://pkbivgrm.bkt.cloudn.com/1063705989962275601rt=1645785077443。
画面 8: 在 EmployeeController.java 中，展示 pdf 方法的代码，使用 Map.putAll() 方法将数据合并到 params 中。
画面 9: 在 EmployeeController.java 中，展示 pdf 方法的代码，将用户个人数据和岗位信息填充到 params 中。
画面 10: 在 EmployeeController.java 中，展示 pdf 方法的代码，使用 BeanMapUtils 将对象转换为 Map 并合并到 params 中。
画面 11: 在项目结构中，展示 templates 目录下的 profile.jrxml 文件，以及 application.yml 配置文件。
画面 12: 在 HRM 系统的个人详情页面，显示用户名为 “aj123” 的用户信息。
画面 13: 在 HRM 系统的个人详情页面，鼠标悬停在“更新”按钮上。
画面 14: 在浏览器中，显示生成的 PDF 文件内容，标题为“岗位信息”，包含“岗位：文员”、“职级：null”、“招聘渠道：番头”、“转正评价：null”等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 2:
```yaml
# application.yml
```

画面 4:
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 5:
```java
@Autowired
private ArchiveService archiveService;

// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 6:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 7:
```sql
-- 插入 Blob 字段的 URL
http://pkbivgrm.bkt.cloudn.com/1063705989962275601rt=1645785077443
```

画面 8:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 9:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf(@PathVariable String id) throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    UserCompanyPersonal personal = userCompanyPersonalService.findById(id);
    UserCompanyJobs jobs = userCompanyJobsService.findById(id);
    //3.用户头像
    String staffPhoto = "http://pkbivgrm.bkt.cloudn.com/" + id;
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    params.put(key, "staffPhoto", staffPhoto);
}
```

画面 10:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf(@PathVariable String id) throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    UserCompanyPersonal personal = userCompanyPersonalService.findById(id);
    UserCompanyJobs jobs = userCompanyJobsService.findById(id);
    //3.用户头像
    String staffPhoto = "http://pkbivgrm.bkt.cloudn.com/" + id;
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    params.put(key, "staffPhoto", staffPhoto);
    Map<String, Object> map1 = BeanMapUtils.beanToMap(personal);
    Map<String, Object> map2 = BeanMapUtils.beanToMap(jobs);
    params.putAll(map1);
    params.putAll(map2);
}
```

画面 11:
```yaml
# application.yml
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 文档内容为“员工的个人信息：下载员工的pdf详情资料”，并列出“1.模板”、“2.数据来源”
