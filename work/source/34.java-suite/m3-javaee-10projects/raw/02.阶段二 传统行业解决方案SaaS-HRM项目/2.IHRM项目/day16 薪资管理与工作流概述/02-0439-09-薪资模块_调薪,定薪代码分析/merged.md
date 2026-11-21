# 09-薪资模块：调薪，定薪代码分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\09-薪资模块：调薪，定薪代码分析_【海量资源尽在 ubkz.com】.mp4
- 时长 3分29秒（音频 209s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们简单的看了一下列表的这个实现那接下来呢还有就是前端页面上这边呢有调心还有定心是两个不同类型的按钮各位应该能看到没错吧那究竟这两个按钮是怎么区分出来的咱们可以简单的一起来看一下那我这边的刷新一下页面我们来看一下刚才查询列表之后的咱们这个数据找到list在页面上的打开抱歉这个是pose提交哈
[00:33] 我们来看一下response得到这段数据那得到的数据呢其中有很多内容哎各位能看到有很多内容那这边呢会有他当前的这个工资的这个情况那是这样的如果说我们刚才在查询在这两个表和user表进行查询的时候我们用的是一个左外连接那左表是user那右表是不是就是我们这个薪资表啊
[01:00] 那薪资表如果没有数据那你查询的这个薪资必然是那没错吧也就是没有这个当前的这个工资那没有工资就需要进行设定就需要进行设定工资如果有工资我们这边显示的就是一个调薪所以这个是页面前端根据你这个工资的总额进行判断的如果你工资基数是零就说明还没有定薪如果工资基数大于零就需要进行薪资调整哎这个
[01:30] 咱们说清楚了之后那接下来呢还有就是相应的这几个功能那比如说定薪那点击过来之后注意点击过来之后进入到的是这个定薪页面那定薪页面指的是一个员工刚刚入职我们可以设置他的当前基本工资比如说100块当前岗位工资100块那转正之后呢可以是200块可以是200块
[01:54] 那注意啊当前是我们转正之前的工资转正之前的工资那转正之后的工资没错吧那同时我们刚才也看过这个人的薪资现在是零那接着我定心咱们来看一下100当前工资转正之前的转正之后200那接着点击确定哎你会发现公司基础是不是变成200因为我们现在还没有转正懂我意思吧那这个流程是怎么做到的很简单
[02:21] 回到我们的这个代码当中找到stall rate因为是跟薪资相关的定薪就是把这个数据传递过来那传递过来之后我们调用方法进行保存好了这个呢比较简单我们看过了这个定薪之后呢咱们接下来呢就来看一下这个调薪那这个调薪呢其实比较简单的就是把你这个一定的这个薪水啊进行一个更新是不是就可以了那我们可以以第一个为例啊就是这边有10块
[02:51] 那我们进行调薪那进入到这边呢他先是根据当前这个ID是把这个人的薪水已经查询出来了那我们同时在Control当中也配置了对应的方法好了这个Modify什么U的ID就是查询用户薪资好了查询出来之后呢5块5块10块那接着我们开始修整那之前总金额是10我们改成20当然了也是基本工资和岗位工资相加之后得的效果
[03:22] 来保存咱们来看一下现在这个薪资是不是也已经发生了变化

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
│   │               ├── Controller
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

