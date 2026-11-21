# 02-POI导出人事报表：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\02-POI导出人事报表：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 时长 13分58秒（音频 838s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了对于构造数据呢我们这个数据的来源呢也做了一个简单的分析那接下来呢我们就可以把这个第一件事先给它搞定那对于我们而言对于我们而言首先呢我们要查询的内容呢它的返回的数据比较多你会发现有用户的详细信息的还有离职相的内容那他们之前的分属在两个不同的实体类当中那我在这边要去构造一个新的实体类注意我这个实体类也跟各位已经提供好了在这边
[00:32] employee有一个response好了employee responseresult好了这个里面呢各位来看这里面呢有很多的字段上面这些字段是我们用户详细信息里面的对应的属性跟我们用户详细信息一模一样那底下这些是我们用户离职相应的所有属性跟我们离职的一模一样这都是一模一样的各位放心好了那接下来呢就是说我又写了一个构造方法
[01:04] 那这个构造方法你给我传递两个对象传递一个用户详细信息对象传递一个用户的离职对象那通过这两个对象我快速的把里面的所有属性复制上那我构造的是通过BUTLOScopy同名属性的方式来做的好那这样一来你传递一个Personal我们的用户详细信息你传递过来一个离职的这么一个对象那通过copycopy对象属性拷贝那这样一来我是不是把这个对象就已经给它复上职了
[01:31] 好了那这个呢我们做了一个简单的介绍那接下来那我们这边获取报表数据我们说过了报表数据得到的是一个list集合那list集合我们把报表数据封装到我们刚才写到的这个工具类当中list好那这个list的这个数据从哪来获取我们呢可以通过用户详细信息Service用户详细信息Service
[02:00] 打点给他写一个方法比如说呢这个方法呢就叫做find by reportfind by report那我这个find by report里面要添加的参数应该有什么呢注意对于我们而言参数有两个第一个参数注意company id应该根据企业id进行查询不同的企业那第二个参数呢就是我们这个month你传递的年份月份
[02:27] 好了接下来我们在user company Service当中补充这么一个方法OK定位到Service补充一个方法方法的返回值我这边也call一下方法的返回值call比过来那好了我们这个方法里面呢需要两个参数第一个参数死菌类型的company id好了第二个类型month好了那对于这个方法而言那对于这个方法而言我们如何去获取数据很简单借助do进行查询就可以了
[03:07] 打点Find By那这个对于这个DU而言呢我就跟他的名字一样了参数直接通过Service传导到DU即可Return那各位就目前而言呢这个DU呢我还没写那没写也一样啊那咱们这个就写到DU接口里面就可以了呗同样的返回值跟这个是一模一样的跟这个是一模一样的好了那接下来注意注意这回呢我们就开始
[03:41] 要去进行查询那要进行查询在SpringDataGPA里面呢有很多种书写方式那在这边我就可以使用ETAQuery的形式自己去写语句那这个语句应该如何去写呢注意注意这语句呢我们刚才其实已经写出来了写出来了那我其实想把这个语句呢再做一个进一步的处理这个其实是一个Circle语句那对于我们封装对象来说呢还是比较麻烦的那我不想用Circle语句怎么办
[04:14] 我可以用HQL或者JPQL来做那怎么办Select new一个我们要封装的对象是不是叫做Apply report result当然了对于这个对象而言呢最好是写全限定类名的形式啊OK那接着就是你new这个对象的时候我们需要注意new这个对象其实相当于构造相当于调用调用这个对象的构造方法
[04:48] 这个对象的构造方法需要一个Personal需要一个我们这离职对象OK各位来看我这个语句应该如何继续往下写好了接下来我们要写的就是from注意就是把Circle语句转化成JPQL这个对象注意一会再补充好了from哪其实就是我们的User CompanyPersonal这玩意这对象是不是对应的是这张表接着给它起一个名字叫做A
[05:19] 剩下的事情呢基本上是一模一样的left join好了left joinjoin的是什么注意是不是就应该是我们的离职的这个对象imploringemp好了我这个离职对象我我我考一下吧ok拿过来那这样一来代表的其实就是我们的第二张表那这样一来我这个搜索语句其实替换已经替换到这个程度了已经替换到这个程度了这个叫做b
[05:57] 那剩下的事情一模一样啊A点user id等于B点user id一模一样的好了那只不过呢我们sql去写的是字段那我们现在写的其实就是属性了好了接下来呢还有添加条件A点commy id c o m p id那对于我们来说等于问号1第一个参数好了接下来呢还有and那and是什么a点time of entry好了like
[06:33] 问号二好了注意还有一个all就是咱们其实就是想方设法的进行替换就可以了按B点我们叫做这个B这个对象呢从里面的属性我们抄一下吧打开它Ctrl C拷过来抄一下好了like问号二OK那这样这个语句呢其实我已经写好了只不过刚才这边遗留了一个就是调用这个构造方法那调用这个构造方法
[07:06] 注意这勾搭方法两个参数一个参数呢代表的是我这个Postal对象一个代表的是我们这个离职对象那这两个对象呢其实我们刚才已经用到了比如说A代表的不就是我们Postal对象B其实代表的就是我们另一个离职对象OK那这样一来我这个JPQL语句其实也就已经搞定了那各位会发现其实我写的这个JPQL就是根据我们的Circle语句演化过来的
[07:34] 就是做了一个转型把伺候语句转化成我们JPQL的一种写法好了这个也是用了它的一个走外连接的一种形式抱歉这边刚才换行的时候多了一个逗号把这个逗号去掉OK那我们的伺候语句已经写好了之后其实还是有一些其他的问题在困扰着我们这个问题在哪呢其实就在于我们这个user company personal Service那是什么问题是各位来看就是我们传递说过了请就过来
[08:00] 传递过来的这个month是一个201802的这么一种形式但是我数据库里保存的是不是应该是这个0几0几所以我用的是一个模糊查询模糊匹配那模糊查询或者模糊匹配我们是不是应该用右边用百分号的形式来做啊那所以接下来我去简单的修改一下我的思维层的这个代码好了首先呢前面给它加上public公共的方法那这回我往后台传递的时候是不是就可以加一个百分号这种形式往后台传递数据是不是就可以了
[08:30] OK我们第一件事搞定了那接下来关注的就是第二件事去构造Excel表格那构造Excel表格呢这个步骤呢相对来说有一点点我们叫做稍微有点点麻烦啊那构造这个表格呢我们里面的一个构造步骤希望各位还有印象那首先呢我们要做的事情就是创建工作部那工作部呢我们创建好了之后接下来呢就是第二件事
[09:03] 我们就开始构造sheet那sheet写好了之后我们接下来关注的不就是创建创建叫做单元格好了接着创建我们的sale错了上面是创建行好了底下是创建单元格接着就是对单元格进行复制还有印象吧好了接下来我们关注的就是解决这几个问题那构造工作簿如何去构造这个比较简单workbookwork
[09:46] WorkbookOKWB等于注意我们说过了我们关注的其实都是2007这个版本所以new一个XSF WorkbookOK好了Workbook我们有了之后接着就是创建我们的sheet那这个也比较简单wb.create sheetOK那我们的单元我们的每一个页其实已经有了那剩下的事情呢就是创建行那么创建行首当其冲的各位千万别忘了
[10:13] 对于我们下载的一个工作部来说呢首先是不是应该有一个叫做标题啊所以呢我们先去构造一个标题的相关的这么一个内容等于那我在构造这个标题的时候呢这个标题究竟有什么呢我们可以看一下在今天的资料当中呢给各位准备了一个就是我要打印的一个人员信息的这么一个表这个其实就是一个案例那我要做到的是其中要有编号姓名等等这一些内容那接着底下呢是不是就是每一行的数据
[10:46] 那所以对于我们而言Ctrl C拿过来我就开始去构造这个标题好了做一替换好了这个就是一个体力活了OK这是一字符串好了那这边呢注意搞一竖组是为了我一会儿方便操作那这是一个字符串那怎么变成竖组Split一下就可以了根据逗号好了分成竖组那这样一来我们的所有标题也已经准备好了那接下来我们就可以去构造单元格
[11:31] 根据我们的先把标题创建出来接下来就可以往里面填充相的数据了没错吧接下来就是标题的处理我们应该如何去做处理标题对于标题处理来说显然它应该是我们Excel里面的第一行要对第一行里面的每一列要做一个处理的过程我们这边很简单处理标题处理标题的时候首先得到我们标题的肉
[12:11] 我们都知道标题呢应该是在第一行我们去处理它好了那对于这个行来说如何去获取也比较简单Shit打点我们叫做CreatorRow就是去创建第一行那还记着我们刚才的练习第一行应该是0才对那在这个0里面呢我们要做的事情就是对这个第一行里面的每一个格子给它设置上我们这个标题的这个内容是不是就可以了
[12:39] 所以我在这里面ITR4循环去循环一把我这个抬头去循环一下我这个抬头那好了接下来这个里面我应该如何去进行设置也比较简单sell等于肉打点get sell那我们get sell的时候这边是不是就是编号应该对应的是第一个格子姓名第二个第三个第四个第五个等等一次来推那对于我这边要处理起来相对来说
[13:11] 这边就可能要有一个值不断的叠加是不是就这样那对于这个值呢我们可以给这边呢设置一个索引比如说intindex等于等于哎我就是零了index等于零当然了我可以给他来一个title index好了那这边我要做的事情就是indextitle index加加不断的叠加不断的叠加直到把这个里面全部叠加完成OK那好了接下来呢我们这边呢就是
[13:43] 单元格创建出来了那对单元格里面的这个内容进行复制倒就比较简单了sell打点我叫做set sell叫做valueOK那我们存储把title放进去就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 Controller 层调用 Service 层，最终使用 Apache POI 库将员工档案数据导出为 Excel 文件。

2) 按时间顺序列出每张画面的要点：
画面1：展示 EmployeeController.java 中的 export 方法，用于导出员工档案，调用 archiveService.findSearch 方法获取数据。
画面2：展示 EmployeeReportResult.java 中的字段，用于封装导出的员工档案数据，包括银行账号、开户行、学历类型、毕业时间等。
画面3：展示 EmployeeReportResult.java 中的构造方法，用于合并个人基本信息和离职信息。
画面4：展示 EmployeeController.java 中的 save 方法，用于保存员工个人信息。
画面5：展示 UserCompanyPersonalService.java 中的 save 方法，调用 UserCompanyPersonalDao.save 方法保存数据。
画面6：展示 UserCompanyPersonalDao.java 中的 findByUserId 方法，用于根据用户 ID 查询员工个人信息。
画面7：展示 EmployeeReportResult.java 中的字段，包括用户名、部门名称、手机号、入职时间、离职原因等。
画面8：展示 UserCompanyPersonalDao.java 中的 findByReport 方法，用于根据公司 ID 和月份查询员工档案。
画面9：展示 EmployeeController.java 中的 export 方法，调用 userCompanyPersonalService.findDBReport 方法获取数据。
画面10：展示 EmployeeController.java 中的 export 方法，开始创建 Workbook 对象。
画面11：展示 Excel 文件界面，显示导出的员工档案数据，包含姓名、手机、入职时间等字段。
画面12：展示 EmployeeController.java 中的 export 方法，使用 Workbook 对象创建 Sheet。
画面13：展示 EmployeeController.java 中的 export 方法，使用 for 循环遍历数据并设置单元格值。
画面14：展示 EmployeeController.java 中的 export 方法，完成 Excel 文件的创建和下载。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) {
    //1.获取数据
    PageResult<EmployeeArchive> pr = new PageResult<>(searchPage.getTotalElements(), searchPage.getContent());
    return new Result(ResultCode.SUCCESS, pr);
}
```

画面2：
```java
private String providentFundAccount;
/** 银行卡号 */
private String bankCardNumber;
/** 开户行 */
private String openingBank;
/** 学历类型 */
private String educationalType;
/** 职业学校 */
private String graduateSchool;
/** 入学时间 */
private String enrollmentTime;
/** 毕业时间 */
private String graduationTime;
/** 专业 */
private String major;
```

画面3：
```java
public EmployeeReportResult(UserCompanyPersonal personal, EmployeeResignation resignation) {
    BeanUtils.copyProperties(personal, target: this);
    if(resignation != null) {
        BeanUtils.copyProperties(resignation, target: this);
    }
}
```

画面4：
```java
@RequestBody Map map) throws Exception {
    if (sourceInfo == null) {
        sourceInfo = BeanUtils.mapToBean(map, UserCompanyPersonal.class);
    }
}
```

画面5：
```java
@Service
public class UserCompanyPersonalService {
    @Autowired
    private UserCompanyPersonalDao userCompanyPersonalDao;

    public void save(UserCompanyPersonal personalInfo) {
        userCompanyPersonalDao.save(personalInfo);
    }

    public UserCompanyPersonal findById(String userId) {
        return userCompanyPersonalDao.findById(userId);
    }
}
```

画面6：
```java
public interface UserCompanyPersonalDao extends JpaRepository<UserCompanyPersonal, String>, JpaSpecificationExecutor<UserCompanyPersonal> {
    UserCompanyPersonal findByUserId(String userId);
}
```

画面7：
```java
package com.ihm.domain.employee.response;

import lombok.*;
import java.util.Date;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class EmployeeReportResult {
    private String userId;
    private String username;
    private String departmentName;
    private String mobile;
    private String timeOfEntry;
    private String companyId;
    private String cex;
    /** 出生日期 */
    private String dateOfBirth;
    /** 最高学历 */
    private String theHighestDegreeOfEducation;
    /** 国家地区 */
    private String nationalArea;
}
```

画面8：
```java
@Query(value = "SELECT new com.ihm.domain.EmployeeReportResult " +
        "LEFT JOIN EmployeeResignation er ON a.user_id = er.user_id " +
        "WHERE a.time_of_entry LIKE '%2018-02%' OR a.time_of_entry LIKE '%2018-03%'")
List<EmployeeReportResult> findByReport(String companyId, String month);
```

画面9：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    //1.获取数据
    List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
    //2.创建Excel
    Workbook wb = new XSSFWorkbook();
    //3.创建Sheet
    Sheet sheet = wb.createSheet();
}
```

画面10：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
```

画面11：
（无代码，为 Excel 文件界面）

画面12：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
```

画面13：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
//4.设置标题行
String[] titles = {"姓名", "手机", "入职时间", "离职原因", "离职时间"};
for (int i = 0; i < titles.length; i++) {
    Row row = sheet.createRow(i);
    Cell cell = row.createCell(i);
    cell.setCellValue(titles[i]);
}
```

画面14：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
//4.设置标题行
String[] titles = {"姓名", "手机", "入职时间", "离职原因", "离职时间"};
for (int i = 0; i < titles.length; i++) {
    Row row = sheet.createRow(i);
    Cell cell = row.createCell(i);
    cell.setCellValue(titles[i]);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
（无 PPT 标题、架构图/流程图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

