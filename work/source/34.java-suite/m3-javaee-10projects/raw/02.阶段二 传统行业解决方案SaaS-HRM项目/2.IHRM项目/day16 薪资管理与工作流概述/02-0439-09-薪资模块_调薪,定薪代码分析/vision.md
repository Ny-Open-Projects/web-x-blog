# 画面线理解：09-薪资模块：调薪，定薪代码分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\09-薪资模块：调薪，定薪代码分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:20, 00:27, 00:29, 00:34, 00:48, 01:11, 01:36, 02:05, 02:23, 02:32, 02:53, 03:03, 03:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:48:37

1) 这一组画面整体在讲什么（一句话）：
演示薪资管理模块的前端页面交互、后端接口调用及对应的 Java 代码实现逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：薪资列表页，显示员工信息，筛选条件为“正式”、“在职”，部门为“test1”，当前页码为1，共10条/页。
画面 2：浏览器开发者工具 Network 面板，显示页面加载的资源列表，包括 app.js、profile、department 等。
画面 3：开发者工具 Network 面板，选中了“/api/salary/list”接口，显示其响应数据为 JSON 格式，包含 success、code、message、data 字段。
画面 4：浏览器地址栏显示正在加载 API 接口，页面为空白。
画面 5：开发者工具 Network 面板，选中了“/api/salary/list”接口，显示其响应数据为 JSON 格式，包含 success、code、message、data 字段。
画面 6：薪资列表页，鼠标悬停在“test001”员工的“修改”按钮上，同时任务管理器显示 IntelliJ IDEA 进程。
画面 7：薪资列表页，鼠标悬停在“test003”员工的“修改”按钮上。
画面 8：薪资列表页，点击“修改”按钮，弹出修改薪资的模态框，显示员工信息。
画面 9：薪资列表页，鼠标悬停在“test003”员工的“删除”按钮上。
画面 10：IntelliJ IDEA 中，项目结构视图，选中了 `SalaryController` 类。
画面 11：IntelliJ IDEA 中，`SalaryService.java` 文件，显示 `saveUserSalary` 方法和 `findUserSalary` 方法。
画面 12：薪资列表页，点击“修改”按钮，弹出修改薪资的模态框，显示员工信息。
画面 13：IntelliJ IDEA 中，`SalaryController.java` 文件，显示 `modify`、`init` 方法的注解和实现。
画面 14：薪资列表页，点击“修改”按钮，弹出修改薪资的模态框，显示员工信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 10：
```
ihm_parent
├── .idea
├── ihm_attendance
├── ihm_common
├── ihm_company
├── ihm_employees
├── ihm_eureka
├── ihm_gate
├── ihm_salaries
│   ├── src
│   │   └── main
│   │       └── java
│   │           └── com.ihm.salaries
│   │               ├── controller
│   │               │   ├── ArchiveController
│   │               │   └── CompanySettingsController
│   │               └── SalaryController
│   │               └── SettingsController
│   │               └── SalaryService
│   │               └── SalariesApplication
│   │               └── ShiroConfiguration
│   └── target
```

画面 11：
```java
@Service
public class SalaryService {
    @Autowired
    private UserSalaryDao userSalaryDao;

    // 定义或者修改
    public void saveUserSalary(UserSalary userSalary) {
        userSalaryDao.save(userSalary);
    }

    // 查询用户薪资
    public UserSalary findUserSalary(String userId) {
        Optional<UserSalary> optional = userSalaryDao.findById(userId);
        return optional.isPresent() ? optional.get() : null;
    }

    // 分页查询当前薪资列表
    public PageResult findAll(Integer page, Integer pageSize, String companyId) {
        Pageable pageable = PageRequest.of(page - 1, pageSize);
        Page<UserSalary> page1 = userSalaryDao.findAll(companyId, pageable);
        return new PageResult(page1.getTotalElements(), page1.getContent());
    }
}
```

画面 13：
```java
public class SalaryController extends BaseController {

    @Autowired
    private SalaryService salaryService;

    // 查询单个薪资
    @RequestMapping(value = "/modify/{userId}", method = RequestMethod.GET)
    public Result modify(@PathVariable(value = "userId") String userId) throws Exception {
        UserSalary userSalary = salaryService.findUserSalary(userId);
        return new Result(ResultCode.SUCCESS, userSalary);
    }

    // 修改
    @RequestMapping(value = "/modify/{userId}", method = RequestMethod.POST)
    public Result modify(@RequestBody UserSalary userSalary) throws Exception {
        salaryService.saveUserSalary(userSalary);
        return new Result(ResultCode.SUCCESS);
    }

    // 初始化
    @RequestMapping(value = "/init/{userId}", method = RequestMethod.POST)
    public Result init(@RequestBody UserSalary userSalary) {
        userSalary.setFixedBasicSalary(userSalary.getCurrentBasicSalary());
        userSalary.setFixedPostage(userSalary.getCurrentPostage());
        salaryService.saveUserSalary(userSalary);
        return new Result(ResultCode.SUCCESS);
    }

    // 查询列表
    @RequestMapping(value = "/list", method = RequestMethod.GET)
    public Result list(@RequestParam(value = "page", defaultValue = "1") Integer page,
                       @RequestParam(value = "pageSize", defaultValue = "10") Integer pageSize,
                       @RequestParam(value = "companyId", defaultValue = "") String companyId) {
        PageResult pageResult = salaryService.findAll(page, pageSize, companyId);
        return new Result(ResultCode.SUCCESS, pageResult);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
