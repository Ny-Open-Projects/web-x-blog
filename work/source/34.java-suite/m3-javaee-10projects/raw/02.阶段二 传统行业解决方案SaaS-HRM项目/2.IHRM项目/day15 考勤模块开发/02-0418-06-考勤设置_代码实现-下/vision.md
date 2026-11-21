# 画面线理解：06-考勤设置：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\06-考勤设置：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:51, 01:22, 03:33, 04:16, 05:12, 05:49, 06:24, 07:02, 07:41, 08:03, 08:23, 08:54, 09:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:32:11

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot + Shiro + Eureka 实现考勤配置的前后端交互与服务间调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE中展示ConfigController.java文件，其中定义了获取考勤配置的POST接口。
- 代码片段：
  ```java
  @RestController
  @RequestMapping("/cfg")
  public class ConfigController extends BaseController {
      @Autowired
      private ConfigurationService configurationService;
      ...
      @RequestMapping(value = "/atte/item", method = RequestMethod.POST)
      public Result atteConfig(String departmentId) {
          AttendanceConfig ac = configurationService.getAtteConfig(companyId, departmentId);
          return new Result(ResultCode.SUCCESS, ac);
      }
  ```

画面2：
- 浏览器中展示考勤设置页面，显示“部门”为“人力资源部”，“出勤时间”为“08:20-09:30”。
- 网络面板显示POST请求的Payload，包含departmentId和多个时间字段。

画面3：
- IDE中展示ConfigController.java文件，与画面1相同，但光标位置不同。

画面4：
- 浏览器中展示考勤设置页面，与画面2相同，但页面左下角有IDE窗口的缩略图。

画面5：
- IDE中展示ConfigurationService.java文件，光标位于第44行，显示了AttendanceConfig的DAO方法定义。

画面6：
- IDE中展示ConfigurationService.java文件，光标位于第54行，显示了find方法的实现，包含条件判断和返回值。

画面7：
- IDE中展示项目结构，选中了“ihrm_common_model”模块，下方显示了多个应用的运行日志。

画面8：
- IDE中展示ShiroConfiguration.java文件，定义了Realm和SecurityManager的配置。

画面9：
- IDE中展示application.yml文件，配置了多个服务的路径和敏感头信息。

画面10：
- IDE中展示项目结构，选中了“ihrm_gate”模块，下方显示了application.yml文件的内容。

画面11：
- IDE中展示GateApplication.java文件，显示了Spring Boot的启动类和日志信息。

画面12：
- 浏览器中显示空白页面，URL为“localhost:8080/#/attendances/index”。

画面13：
- 浏览器中展示考勤设置页面，与画面2相同，但“部门”为“研发部”，“出勤时间”为“08:20-09:30”。

画面14：
- 展示了一个PDF阅读器界面，显示“day15”文档，内容为空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.springframework.web.bind.annotation.RestController;

/**
 * 配置考勤设置的controller
 */
@RestController
@RequestMapping("/cfg")
public class ConfigController extends BaseController {
    @Autowired
    private ConfigurationService configurationService;

    /**
     * 获取考勤设置
     * cfg/atte/item
     * post
     * 参数 departmentId
     */
    @RequestMapping(value = "/atte/item", method = RequestMethod.POST)
    public Result atteConfig(String departmentId) {
        AttendanceConfig ac = configurationService.getAtteConfig(companyId, departmentId);
        return new Result(ResultCode.SUCCESS, ac);
    }
}
```

画面5：
```java
private ExtraDutyRuleDao extraDutyRuleDao;
private DayOffConfig dayOffConfigDao;
private IdWorker idWorker;
@Autowired
private ConfigurationService configurationService;

//保存或更新考勤设置
public void saveAtteConfig(AttendanceConfig attendanceConfig) {
    if (null != attendanceConfig) {
        attendanceConfig.setId(idWorker.nextId());
        attendanceConfig.setCompanyId(companyId);
        attendanceConfig.setDepartmentId(departmentId);
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendance
