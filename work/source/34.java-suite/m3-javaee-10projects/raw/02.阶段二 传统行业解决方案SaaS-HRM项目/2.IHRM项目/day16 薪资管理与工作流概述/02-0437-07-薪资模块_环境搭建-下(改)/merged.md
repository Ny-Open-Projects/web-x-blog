# 07-薪资模块：环境搭建-下(改)

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\07-薪资模块：环境搭建-下(改)_【海量资源尽在 ubkz.com】.mp4
- 时长 10分21秒（音频 622s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好了我们现在已经把这些基本的该导入的都已经导入了那接下来还有一部分是我们接下来要关注的是这样子我们之前说过咱们这里面的基本上的大部分功能都是跟之前社保和考勤相似或者类似的那里面的逻辑也都是差不多所以这些代码咱们就不需要从无到有再去写了那在今天的工程当中把这些最基础的DO Service以及Controller都给各位准备好了
[00:29] 那我们只需要把今天资料当中相应的这些内容给它拷到我们的项目当中让它跑起来那我们只关注里面比较重要的一两个功能其实就可以了好了那接下来呢回到我们这边找到今天的这个资料那首先呢咱们先去考对应的实体类Ctrl C把对应的实体类拷到我们拷到咱们对应的工程的部分model当中
[01:00] 好了在这边呢我去创建一个新的包就叫salarys-a-l-a-r-y-s-a没错好了接着点击ok那把实体类呢control v 拷过来好了这几个实体类呢简单的来说一下分别对应我们数据库里面的这张表比如说我们user salary代表的是用户薪资的相配置里面有当前工资里面有比如说他的转正工资等等那接下来呢继续再来看
[01:29] 还有一个代表的是company setting这个company setting代表的是企业是否或者说企业他已经设置过的这个或者正在设置的这个一个企业的一个月份比如说你要设置九月份的薪资那这边就需要在数据库里面给他配置成相应的九月份等等等等就这个意思那接下来呢还有还有就是一个叫做salary
[01:59] 这个代表的是我们的企业的规档以及规档明细这个都比较清晰了好了那接着还有一个setting这个setting这样的就是在企业当中的可能有很多的不同的津贴或者福利津贴那比如说有参补等等其他的一些补助那这个呢是在setting当中咱们需要进行配置好了那其实这个实体类呢都比较简单我们已经给它copy过来了那除了实体类之外
[02:27] 那实体类对应的必然还有有DL所以我在这边再去创建一个包注意这回回到我们的工程了丢在丢这个包下咱们继续把给各位提供好的操作代码DL把里面这几个代码Ctrl C靠到我们的工程里那由于我们是死不认对他这一批所以我靠过来的这些代码呢特别是DL都比较简单全部都是哎就搞这么一个DL然后呢实现这么一个接口等等等等
[02:57] 好了那这边呢其中有一个啊就是我们这边UserServiceDU那这边呢是为了我们进行数据库列表查询我玩了一个Circle语句那这个呢是因为咱们这个业务比较特殊它设计的表呢有两张表要关联查所以我专门以Circle语句的形式来写的其实这个和我们之前做社保那个呢是一模一样的OK那DU我们说过了之后接下来呢还有Service同样的回到我们这边
[03:25] Service里面的代码control c同样的在这边配置一个包se2vse代表Service那把Service也copy进去好了在Service当中呢注意这边有一个归档Service归档Service呢不需要我们现在进行编写啊是因为这个里面呢有一块核心逻辑我们刚才说过了归档里面要计算它的金额所以这个是我们今天一个核心逻辑现在呢咱们先别管那除了这个之外company setting Service
[03:57] 其实就是一个根据ID查接着这边呢就是做一个保存就是这么两个方法好了这边有一个异常我把这个先去掉好了那继续再来还有一个salary Service这个salary Service里面的内容其实比较简单第一个就是保存C5当然这边叫保存或者更新那其实对应的就是我们这边有定薪或者调薪的这么一个工作定薪指的是你新入职一个员工你还没有薪水
[04:26] 还没有所以我往数据库里面给你保存一条那调薪更不用说了你之前是100块这回给你调成200所以说白了就是保存或者更新没错吧好了接下来呢咱们在保存和更新之前习惯是不是先根据ID查所以这边就是根据ID查询那这边呢还有一个分页的列表展示OK这边也有多余的这么一些内容我把它删掉OK好了那接下来呢还有一个Service叫做siting Service那这个siting Service我简单再来说一下这个是我们的
[05:00] 福利福利津贴那福利津贴Service这样的不同的企业呢可能会对不同的企业当中的这个津贴的进行设置有按周结算有按日结算有按月结算等等等等所以呢这边呢咱们也可以进行设置那设置之前先查接着这边保存或更新没错吧所以这几个Service或者DO的方法呢都是比较简单的它对应的都是一个单表
[05:31] 好了那除了这个Service之外呢接下来呢咱们就应该有Controller在这边呢去创建一个包我们叫做Controller里面开始去写我们或者去导入我们Controller相关的这些基础代码OK回到我们的资料当中呢把这个Controller相关的代码呢也给他拿过来就在这边Controller里面四个controllercontrollerc靠到这边好了靠过来之后呢简单的来说一下其中第一个
[06:04] 是我们的归档Controller咱们的归档相代码呢就写到这个Controller当中了说过了这个是我们一会儿要自己实现的功能还有就是company Controller这个是我们的企业设置那主要是为了设置企业它目前正在目前呢正在核算的这个薪资月份那
[06:32] 里面呢这个方法呢也比较简单是否已经设置过这个当月工资然后呢保存企业这个工资的设置那构造新报表跟之前一样的其实说白了就是哎在页面部分如果呢开始做如果你没有做过就让你开始填填了之后呢在这个数据库里面记录一下你现在制作是哪点月份的工资那如果你正在做这个八月份工资直接进入到页面就显示的是八月那
[06:58] 注意在归档的时候有一个新报表一点新报表其实就相当于把这个08是不是改成09就是这么一个套路而已好了那除了这个之外接下来salary Controller这个salary Controller指的是当前员工的所有薪资的一些数据比如说当前张三员工他每个月基本工资是多少他的岗位工资是多少合计工资是多少就这么一个工资的一个设置当了有工资的列表
[07:28] 要查询当然了对于新员工可以定薪老员工可以调薪我们还可以去查询这个用以某一个员工他的薪资根据ID来进查询那注意还有一个就是这边有津贴的Controller那对于这个津贴Controller其实就是这样的去设置一个企业它的所有福利津贴那里面呢根据ID查那查询这个企业的所有津贴那接下来呢
[08:02] 进行设置保存或者更新一个方法搞定好了这个就是我们一些基本的一些代码OK把这个咱们启动起来来看一下效果先走OK好了这边程序在启动它启动稍微有一点点慢啊OK我这边先暂停一下等它起来之后咱们再来看效果好了这边的程序已经启动成功了回到我们的页面咱们一起来看一下效果咱们的页面部分呢先登录进去
[08:48] 好了那接下来呢找到我们的工资模块各位发现直接就进入到了我们的系统当中为什么在我们的数据库里给我来看找到SAcompany setting这边是不是制作到了19年7月份他这个薪资啊当然你把这条数据给他删掉那删掉之后那在我们的页面当中各位就会发现一刷新抱歉不应该这样的重新进来一下吧
[09:25] 刷新各位发现这回是不是让你去填写你要制作多少份几月份的这个工资啊我们填上201907那颠的点击确定哎各位发现是不是又进来了好了那同时我们的数据库刷新一把你发现这个值又回来了那这个是怎么做到的其实企业一启动他就会访问我们这边的company setting Controller那在company setting Controller先去获取企业是否设置过这个工资的月份
[09:55] 如果你查询出来了有值直接进入到页面里面如果没有值让你填写你要设置什么那你填写的过程当中就刚才我们填写月份其实就进入到了保存这个月份你点保存月份数据库相应填写上设置的月份同时页面进行跳转到列表就是这么一个逻辑OK那这样一来其实我们这个环境搭建咱们就已经全部都搭建好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示薪资模块的开发流程，包括创建实体类、数据访问层、服务层、控制器层，并最终启动项目并展示前端页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示薪资模块的前端页面，包含“开始年”输入框和“确定”按钮。
画面2：在IDEA中，打开项目结构，准备创建新包。
画面3：展示实体类 SalaryArchiveDetail 的代码，包含公司ID、是否设置、当前显示报表月份等字段。
画面4：展示项目文件夹结构，包含 CompanySettings.java、SalaryArchive.java 等文件。
画面5：展示 UserSalaryDao 接口代码，包含查询和分页方法。
画面6：展示 ArchiveService.java 服务层代码，包含对 ArchiveDao 和 IdWorker 的注入。
画面7：展示 SalaryService.java 服务层代码，包含对 UserSalaryDao、UserSalaryChangeDao 等的注入。
画面8：在IDEA中，展开项目结构，显示 salaries 模块下的 Controller、Service、dao 等包。
画面9：展示 CompanySettingsController.java 控制器代码，包含获取和保存企业设置、新建报表的方法。
画面10：展示 SalaryController.java 控制器代码，包含修改用户薪资、初始化薪资、查询列表的方法。
画面11：展示 SalariesApplication.java 启动类，包含 @SpringBootApplication 注解和 main 方法。
画面12：展示前端薪资列表页面，显示员工信息和操作按钮。
画面13：展示 SalariesApplication.java 启动类，包含 @Bean 注解的 IdWorker 实例。
画面14：展示前端薪资列表页面，显示“本月：入职/离职/调薪/中退”按钮和员工列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@Entity(name = "sa_company_settings")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CompanySettings implements Serializable {
    private static final long serialVersionUID = -262868884659248618L;
    @Id
    private String companyId;
    /**
     * 是否设置 0为未设置，1为已设置
     */
    private Integer isSettings;
    /**
     * 当前显示报表月份
     */
    private String monthAll;
}
```

画面5：
```java
package com.lhrm.salaries.dao;
import com.lhrm.salaries.entity.UserSalary;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import java.util.List;
public interface UserSalaryDao extends JpaRepository<UserSalary, Long>, JpaSpecificationExecutor<UserSalary> {
    @Query(value = "select bu.id,bu.username,bu.mobile,bu. bu_in_service_status inServiceStatus, bu.form_of_employment formOfEmployment, count(*) from bs_user bu where bu.id = ?1")
    Page<Map> findPage(String companyId, PageRequest page);
}
```

画面6：
```java
package com.lhrm.salaries.Service;
import com.lhrm.salaries.dao.ArchiveDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class ArchiveService {
    @Autowired
    private ArchiveDao archiveDao;
    @Autowired
    private ArchiveDetailDao archiveDetailDao;
    @Autowired
    private IdWorker idWorker;
}
```

画面7：
```java
package com.lhrm.salaries.Service;
import com.alibaba.fastjson.JSON;
import com.lhrm.common.entity.Result;
import com.lhrm.domain.wte.Bo.AtteSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserCompanyPersonal;
import com.lhrm.domain.wte.Bo.UserSalaryDetail;
import com.lhrm.domain.wte.Bo.UserSalary;
import com.lhrm.domain.wte.Bo.UserSalaryChange;
import com.lhrm.domain.wte.Bo.UserSalaryStatistics;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.User

