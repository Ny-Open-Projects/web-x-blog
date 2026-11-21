# 11-薪资模块：月报表-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\11-薪资模块：月报表-上_【海量资源尽在 ubkz.com】.mp4
- 时长 15分39秒（音频 939s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们现在呢已经完成了这个薪资模块的大部分功能当然了这些功能都比较简单跟我们之前写的都差不多所以这边呢咱们就简单的一概而过其实就可以了那除了这个功能之外呢还有一块就是这边有报表还有归档相亲的数据那这边呢比较重要的一块功能呢就是这个看一下我们当前的当月的薪资报表那当月的薪资报表涉及到我们的一个计算以及数据的一个来源我们一起来分析一下
[00:31] 那么可以点击过去一起来看一下那页面呢需要的内容呢还是比较多的比较多的那在这边以一张图形的形式和各位分析一下那我们这边呢需要的内容究竟有什么好了这个看起来呢还是不太直观的我们可以打开前端页面好了把这一段呢咱们拿过来做一个小小的分析好了各位会看到其实我们整个的这个前端页面需要的内容有用户
[01:05] 所需要的所以我们这边的数据呢第一部分内容呢就是我们的用户数据好了那接着第二部分内容你会发现说明有你公积金缴纳的还有我们这边社保缴纳的这些情况那第二部分呢其实代表的就是我们的社保相应的这个数据这个也没问题那接下来我们去来看这边什么基本工资岗位工资什么薪资福利那这些呢其实就是我们现在做的薪资和我们的这个
[01:34] 今天这些数据没错了好了那接着底下还有就是我们的考勤扣款那考勤扣款必然你要看一下当前这个人考勤究竟是上了十天班上了十五天班还是全勤的这么一个状态所以这边又涉及到我们的考勤考勤的相关数据没错了那底下这边是不是有应纳税额扣税多少实发工资是多少那这第五分数据从哪来的
[02:02] 好了那这第五个数据是不是就是通过你这个员工薪资和津贴以及你考勤相关数据我们计算出当月应该给你发的工资那既然呢根据国家的一些税收的政策计算出你应该缴纳的税收接着做出你最终实发的工资所以最后就是要去计算这些税等等这些内容所以我想说咱们要做这个内容呢涉及到的点呢相对来说会比较多
[02:31] 一共有这么几块那除了这几块之外呢接下来我们来分析一下这几块数据咱们要做的话从哪来那我们的数据社保肯定要有一个模块第一个就是社保的这个模块没错了好了除了社保模块之外薪资和津贴哎这个不需要了因为我们现在就在薪资这个模块里面开发所以我们直接调用Service就可以了那接着烤琴那烤琴也是一块
[02:58] 考勤模块所以我想说咱们现在要做的这个数据呢其实就是要通过社保以及考勤拿到一些相关的数据接着是不是再结合我们当前新字模块设置的一些数据就是计算出它最终的这些实发的这些工资的金额没错了所以呢这边呢咱们就需要跟各位做这么一个小小的数据上面的分析那这个数据我们分析过了之后那接下来
[03:29] 我们可以看一下页面上请求究竟发送到哪刷新一把各位发现这边请求其实请求的是我们的新字模块叫做Reports接着后面跟了一个参数201907这个代表的是月份没错吧注意后面又以请求参数的形式是不是加了一个Optab其实这个路径和我们之前做的社保这一块很相似我们打开F12一起来看一点击过来之后
[04:03] 社保模块请求对路径呢也是黑瓷水只不过名字叫黑瓷水啊这边是2017后面是不是也是一个optem哎没错吧各位那所以我想说这块这个路径请求上其实差不多的好了那接下来呢回到我们这边咱们就开始去完成哎这个新资阅读报表的一个哎代码开发好了首先呢这边请求到路径咱们拿过来OK
[04:37] Ctrl C那我们现在设置到的报表或者归档信息所以我把这个数据呢就写到咱们归档的Ctrl当中好了制作薪资报表好了那我们的请求的URL写到这边好了那注意啊这里面的参数呢有两类参数第一个参数呢是我们有一个地址参数地址参数指的是我们这个201907
[05:08] 现在制作7月份如果制作8月份就是08那还有一个就是我们的请求参数这是我个人习惯因为上面这个是在地址当中这个是挂了一个get方式的一个请求OK好了这边有一个叫做optab那这个optab呢我来解释一下如果是0代表的是新制作的新制作的报表那如果是1代表的是查询已归档的报表数据
[05:40] 所以这两个呢不太一样第一个我们归档数据里面没有那第二个数据表里面有我们直接查其实就行了哎抱歉这个正好写反了抱歉正好写反了其他如果是一时迅速的制作其他应该就是一归档的咱们查数据库就可以了好了那接下来我们可以补充对应的Controller好了public来起一个名字resultresult返回值好了那接下来呢咱们的对于这边
[06:10] 咱们的请求的这个方法名叫什么呢其实随便写了history detail这随便写的就是拿到我们的这个归档历史啊OK好了这边不报错呢为了不报错我拗一个result好了resultcode.succeed好了没问题那接下来呢咱们的请求路径at request myping来进请求那请求过来之后我们只需要关注后半部分就可以了好了
[06:44] 那这个2017代表的是一个地址参数我们可以来进行替换就叫做yearMouse这是一个参数好了那我们的请求方式究竟是什么刚才我们看过请求方式method就是get方式请求没错吧好了那接下来呢地址我们定义好了那接下来定义方法的参数那方法参数有两个第一个是地址参数at pass叫做variable死均类型的yearMouse那注意第二个参数
[07:16] 也是一个死菌类型的是不是就是一个1当然你可以把它理解成死菌也可以理解成一个int都可以为了我们一会儿方便做判断我们这边变成int类型的opptime好了这个就是我们的方法的一个接口写好了那接下来我们开始去完成里面的代码那完成代码很简单如果咱们就需要做判断就需要做判断其实里面的步骤很简单第一个判断一下
[07:48] 我们传递过来这个off type参数如果如果等于等于1我们需要自己去构造构造报报表数据好了如果这个等于等于2那这个时候我们就要查询归档历史表因为我们刚才说过了如果抱歉如果不等于不不等于1不等于1如果不等于1那其实就意味着你要去查询归档的那个历史表了没错了
[08:21] OK那接着我们开始判断写好了之后我们开始if为了方便呢我们把off type定义成数字了所以我们等于等于1的话我们自己去写else那如果是2的话我们开始调调用Service调用do我们完成基本的查询就可以了那根据我们现在来说呢第一步呢相对来说有点复杂我们先把第二步给它搞定因为我们要查询
[08:53] 比较简单那么查询的究竟是哪注意我们来看回到数据库我们说过了如果是一个已经归档的其实我们查询已归档的这个薪资归档表就可以了有两个SA第一个归档主表第二个是归档明细表那看到我们现在页面上显示的明显我们查询的是不是就应该是这个归档明细表没错了当然了我们可以先这样先查一下主表有没有数据主表有再去查明细表
[09:22] 这样一来呢看起来更加合理一些哎能理解吧OK好了回到这边呢我们开始去编写对应的方法好了在这边呢咱们刚才说过了咱们如果要查这个归档历史表的话咱们可以分成两个小的步骤来查先看一下主表有没有数据查询主表数据那件呢主表数据如果有我们再去根据主表的ID去查询明细表
[09:54] 的所有数据这是我们要关注的这两个小步骤那我们开始查询主表数据或者查询其他数据呢我们都是借助Service来进行查询就可以了at auto where那我们把归档Service诶归档Service注进来privateprivate归档serviceOK好了那接下来呢归档Service有了之后我们开始调用归档Service先查主表数据就是find
[10:28] 好了我们这个实体类叫什么名字呢我习惯就是实体类名字了回到我们这边来看一下salary就叫做salarysalary archive这么一个实体类当然这是我们的主表salary archive detail代表的是我们的名系所以我们先查第一个好了就是SE等于那我们的就是find salary archive就是
[10:56] 根据什么查咱们是不是要看一下当前这个年份所以我们想说的是咱们这边要查询这个数据库表回到这边来看我们要查询其实就是根据对应的表数据上面这个表根据这个里面的记录的时间来进行统计就可以了比如说我们看一下是有没有7月份的没错吧当然了我们有不同的企业所以要有企业ID要有这个year month
[11:26] 所以我们这边呢就是就这样吧find那接着把参数传递过去先传一个emounce再传一个company idok就可以了那Service呢这边呢第一个我们写好了之后那接下来呢还有第二个那第二个呢咱们要查询它的明细明细表呢咱们就可以这样先做一判断if sa呢不等于none不等于none那我们就可以拿到sa打点get
[11:57] ID是不是得到它的主件那接下来我们查询明细表是不是就以这个为参数来进行查询就可以了没错吧那我们要查询明细表返回值呢肯定是一个粒子集合同样的我们这边构造一个最上方的构造一个返回值类似类型的那么返回值不管是自己构造还是我们查询数据库其实都是一样的OKsalaryR5好了接着就是detail构造一个返回值list
[12:28] 等于 new 一个 arraylist 没问题那接下来呢我们就可以 list等于 se哎抱歉直接调用 Service 来查询我个人习惯先把一个方法写完再写另一个.find就叫做 detail 得了好了那我们传递的参数是不是就是这个 idea那最终为了别别别忘啊我一会先把这个 list 也返回过来
[13:01] 那这样一来呢我们第二步的这个control的代码已经写好了剩下是不是就是Service了那Service比较简单爱我的回车补充一下好了这边同样的爱我的回车补充一下那写下注释就是根据企业企业和我们的年月来年月来查询我们的归档主表数据好了那接着就是根据归档
[13:33] 的ID查询所有的归档明细记录OK那上面这个咱们就可以调用DU层方法那DU层方法同样的我们的归档主表点好了这个呢咱们可以在归档主表DU里面咱们来直接把这个方法先写出来因为这样你来呢在DU里面它会有相应的提示啊同样Fundby开头那Fundby我们说过了要根据company ID来查就是它
[14:07] 好了接着两个参数是不是还应该有一个叫做 year month没错了那接下来咱们就可以把这两个参数呢给它定义上来cmpy id好了死菌类型的死菌类型的month nthok那这个方法我们写好了直接咱们就可以return点find by把参数注意参数这个顺序别搞错啊
[14:43] 好了第一个方法我们搞定了那接来是不是要写第二个那第二个我们要查询的是明细那就找到明细DU补充方法类似的类型的哎范形给他补充上FindBy那我们这边呢打开这个实体来看一下这个实体里面归档ID哎是不是就是Archive ID啊所以我们这边就是根据这个ID来查就行了IDOK参数呢补充完整OK好了
[15:24] 回到Service直接return点OK把ID传进去那这样一来我们的下边这个流程是不是就已经下了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过 Spring Boot 后端代码实现“薪资归档”功能的前后端交互逻辑，包括控制器、服务层、数据访问层和数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面环境，显示“黑马程序员”和“博学谷”两个机构的Logo，用于课程开场。
画面2：在记事本中编辑一个 Vue.js 的 el-table-column 列配置代码，用于前端表格展示。
画面3：在浏览器中打开 iHRM 系统的“社保”模块页面，显示系统登录后的主界面。
画面4：在 IntelliJ IDEA 中打开项目结构，展示 iHRM 项目中与薪资归档相关的 Controller、Service、dao 等包结构。
画面5：在 ArchiveController.java 中，展示 historyDetail 方法的初步代码框架，包含注释说明请求参数。
画面6：在 ArchiveController.java 中，继续编写 historyDetail 方法，添加了 if (opType == 1) 的条件判断逻辑。
画面7：在 ArchiveController.java 中，对 else 分支进行注释说明，准备调用服务层方法。
画面8：在 ArchiveController.java 中，将 else 分支的代码改为调用 archiveService.find 方法。
画面9：在 Navicat for MySQL 中，查看并展示名为 “salary_archive” 的数据库表结构和部分数据。
画面10：在 ArchiveController.java 中，使用 Ctrl+空格自动补全 Java 类型，如 Long、String 等。
画面11：在 ArchiveService.java 中，展示 findSalaryArchive 和 findSalaryArchiveDetail 两个方法的定义。
画面12：在 ArchiveDao.java 中，定义了 JpaRepository 接口，用于查询 SalaryArchive 实体。
画面13：在 SalaryArchiveDetail.java 中，定义了实体类，包含 @Entity、@Data、@AllArgsConstructor 等注解。
画面14：在 ArchiveController.java 中，完成 historyDetail 方法的最终逻辑，调用服务层方法并返回结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```html
<el-table-column type="index" label="序号" center width="50"></el-table-column>
<el-table-column prop="username" label="姓名" width="150px"></el-table-column>
<el-table-column prop="workNumber" label="工号" width="150px"></el-table-column>
<el-table-column prop="departmentName" label="部门" width="150px"></el-table-column>
<el-table-column prop="identityStatus" label="身份状态" width="150px"></el-table-column>
<el-table-column prop="socialSecurityIndividual" label="公积金个人" width="150px"></el-table-column>
<el-table-column prop="socialSecurityEnterprise" label="公积金企业" width="150px"></el-table-column>
<el-table-column prop="totalSecurityProviderFundIndividual" label="公积金个人" width="150px"></el-table-column>
<el-table-column prop="currentBaseSalary" label="岗位工资" width="150px"></el-table-column>
<el-table-column prop="salaryChargeAmount" label="应扣金额" width="150px"></el-table-column>
<el-table-column prop="attendanceDurationMonthly" label="考勤天数" width="150px"></el-table-column>
<el-table-column prop="salaryFyTax" label="应纳税" width="150px"></el-table-column>
<el-table-column prop="tax" label="税" width="150px"></el-table-column>
<el-table-column prop="payment" label="实发工资" width="150px"></el-table-column>
```

画面4：
```
ihm_parent
├── ihm_common
├── ihm_company
├── ihm_employee
├── ihm_euroa
├── ihm_gate
├── ihm_salaries
│   ├── src
│   │   └── main
│   │       └── java
│   │           └── com.ihm.salaries
│   │               └── Controller
│   │               │   └── ArchiveController.java
│   │               └── Service
│   │               └── dao
│   └── resources
│       └── test
│       └── target
│       └── ihm_salaries.iml
│       └── pom.xml
└── ihm_social_security
```

画面5：
```java
package com.ihm.salaries.Controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.Controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    public Result historyDetail() {
        return new Result();
    }
```

画面6：
```java
package com.ihm.salaries.Controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.Controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    @RequestMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
    public Result historyDetail(@PathVariable String yearMonth, int opType) {
        return new Result(ResultCode.SUCCESS);
    }
```

画面7：
```java
package com.ihm.salaries.Controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.Controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    @RequestMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
    public Result historyDetail(@PathVariable String yearMonth, int opType) {
        if (opType == 1) {
            // 1.单向opType参数:如果=1,自己勾选报表数据
        } else {
            // 2.如果=1,查询归档历史表
            // 2.1 查询主表数据
            // 2.2 根据主表的id,查询明细表的所有数据
        }
        return new Result(ResultCode.SUCCESS);
    }
```

画面8：
```java
package com.ihm.salaries.Controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.Controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    @RequestMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
    public Result historyDetail(@PathVariable String yearMonth, int opType) {
        if (opType == 1) {
            // 1.单向opType参数:如果=1,自己勾选报表数据
        } else {
            // 2.如果=1,查询归档历史表
            // 2.1 查询主表数据
            // 2.2 根据主表的id,查询明细表的所有数据
            archiveService.find();
        }
        return new Result(ResultCode.SUCCESS);
    }
```

画面9：
```sql
SELECT * FROM salary_archive;
```

画面10：
```java
// Ctrl+空格自动补全
Long (java.lang)
lazy (org.springframework.context.annotation)
Lazy (org.springframework.data.util)
LinkageError (java.lang)
LeaveConfig (com.ihm.domain.attle.enum)
LambdaConversionException (java.lang.invoke)
LambdaDataFactory (java.lang.invoke)
Layout (com.sony.java.util)
LayoutStyle (java.awt)
Label (java.awt)
LabelPoem (java.awt)
Label (java.awt)
```

画面11：
```java
@Service
public class ArchiveService {
    @Autowired
    private ArchiveDao archiveDao; // 归档主表dao
    @Autowired
    private ArchiveDetailDao archiveDetailDao; // 归档明细dao
    @Autowired
    private UserSalaryDao userSalaryDao; // 员工薪资设置dao
    @

