# 画面线理解：22-部署流程：部署测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\22-部署流程：部署测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:32, 00:42, 00:47, 00:53, 01:07, 01:15, 01:23, 01:39, 01:51, 02:04, 02:20, 03:00, 03:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:58:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写 Spring Boot 控制器代码，并使用 Postman 发送 HTTP 请求上传文件，最后在数据库中查看上传记录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 `ProcessController.java` 文件，其中定义了 `@RequestMapping("/deploy")` 的 POST 方法，用于接收文件上传。
画面 2: 在 IntelliJ IDEA 中，切换到项目视图，准备进行后续操作。
画面 3: 在 Postman 中，显示初始界面，正在加载。
画面 4: 在 Postman 中，设置一个 GET 请求，URL 为 `127.0.0.1:9007/user/process/deploy`，并配置了继承父级的授权。
画面 5: 在 Postman 中，显示一个错误提示：“There was a problem logging in to Sync. Please restart the app without logging out”。
画面 6: 在 IntelliJ IDEA 中，鼠标悬停在 `application.yml` 文件上，准备查看或编辑配置。
画面 7: 在 IntelliJ IDEA 中，显示 `application.yml` 文件内容，但未展示具体配置。
画面 8: 在 IntelliJ IDEA 中，同时显示 `ProcessController.java` 和 `application.yml`，并弹出 Postman 窗口，准备发送请求。
画面 9: 在 IntelliJ IDEA 中，使用 IDEA 的代码提示功能，查看 `@RequestMapping` 注解的参数选项。
画面 10: 在 IntelliJ IDEA 中，将 `@RequestMapping` 的 `method` 属性设置为 `RequestMethod.POST`，完成方法定义。
画面 11: 在 Postman 中，将请求方法改为 POST，URL 为 `127.0.0.1:9007/user/process/deploy`。
画面 12: 在 Postman 中，切换到 Body 标签页，选择 `form-data`，并弹出文件选择对话框。
画面 13: 在 SQLyog 数据库管理工具中，打开 `wms_deployment` 数据库。
画面 14: 在 SQLyog 数据库管理工具中，显示 `wms_deployment` 数据库中的 `wms_deployment` 表，其中有一条记录，ID 为 `20230724-4155-1103-4465-33`，CATEGORY 为 `BPM`，DEV 为 `BPM`，IDENTITY_ID 为 `BPM`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 流程控制的controller
 */
@CrossOrigin
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

    @Autowired
    private ProcessService processService;

    /**
     * 部署流程
     * 请将经审核的流程模型图(bpmn)文件上传到方括号
     * 变量：上传的文件
     * @param file
     * @return
     */
    @RequestMapping("/deploy")
    public Result deployProcess(@RequestParam("file") MultipartFile file) throws IOException {
        processService.deployProcess(file, companyid: "占位插值");
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面 6:
```yaml
# application.yml
```

画面 10:
```java
@RequestMapping(value = "/deploy", method = RequestMethod.POST)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
