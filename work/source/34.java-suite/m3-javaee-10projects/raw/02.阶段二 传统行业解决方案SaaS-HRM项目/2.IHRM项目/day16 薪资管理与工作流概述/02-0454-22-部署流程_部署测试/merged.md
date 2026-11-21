# 22-部署流程：部署测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\22-部署流程：部署测试_【海量资源尽在 ubkz.com】.mp4
- 时长 3分33秒（音频 214s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那咱们流程部署或者流程上传这些代码呢咱们已经写好了那接下来呢我们就可以把这个工程呢启动起来那用一个小小的案例咱们看一下能不能把流程部署上去那在这边呢我已经把这个工程呢刚刚已经给它启动起来了那启动起来了之后接着我们可以借助Postman
[00:27] 一起来进行测试那在这边我去打开Postman好了这个Postman呢已经打开成功了哎呦把这些没用的全部都清掉啊那接下来我们这边的请求路径哎是我们的127.0.0.1那冒号我们来看一下请求的端口注意我现在不借助晚关直接测试一下我们当前的这个工程究竟好不好用那我们的请求端口呢就是9007拿过来9007
[01:11] 那接下来呢找到我们对应请求的路径哎把这一段Ctrl C靠到这边当然了还有一个DeployOK好了把这个咱们写好了之后那我们这边呢请求的目前来说我请求的是哪种请求方式都行那我这边呢再来加一下就是Method咱们给它改成Post请求方式Post请求方式那接着我再去重新启动一下当前工程
[01:47] OK这个启动稍微有一点点慢我这边先暂停一下好了现在呢已经启动成功了那接着回到我们的Postman一起来试一下那我们现在请求方式是Post那我们这边需要添加对应的请求参数那请求参数呢我们用的是注意啊我们现在要上传一个文件那我们的请求的参数名称刚才说过了是不是应该叫这个Fill哎叫Fill那接下来呢这边呢请求的是什么类型是一个文件
[02:19] 所以我上去搞一个文件拿过来哎就是我们请假的这个单子OK打开那这样一来对应的我们这个流程呢咱们就可以一起来试一下了点击send好了这边告诉我已经操作成功那注意这个操作成功了之后我们可以一起来开下数据库那对于我们这个数据库呢刚刚我已经把所有的数据全部都清掉了就目前这个表呢目前还没有数据
[02:50] 注意有很多表那我们要看的表呢是这个ACTREDeployment代表的是部署的流程那目前这个表呢数据还没有我刷新一下可以发现我们刚刚自己部署的这个数据呢已经进来了没错吧好了当然它关联的很多表呢也会有这些数据比如说呢这边Beta Ray指的是你上传的这个文件它的类型比如说呢这边还有一些它的一些关联的一些表其实数据都已经有了
[03:20] 那并且呢需要跟各位一起注意的是那你上传过来这个文件咱们是不是通过一个TenID的形式已经把这个ID给它附上值了哎没错吧OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
 * 流程控制的Controller
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

