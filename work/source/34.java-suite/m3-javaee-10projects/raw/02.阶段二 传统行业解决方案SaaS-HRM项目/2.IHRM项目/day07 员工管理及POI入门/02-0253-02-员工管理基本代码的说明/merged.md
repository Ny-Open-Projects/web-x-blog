# 02-员工管理基本代码的说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\02-员工管理基本代码的说明_【海量资源尽在 ubkz.com】.mp4
- 时长 7分40秒（音频 461s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 对于员工管理刚才说过的这些基础功能比如说呢入职转正离职调岗还有员工的一些基础信息详细信息的一些展示都比较简单就是对数据库的一个增深改查那为了我们节省时间呢这些代码呢就不再跟各位一行一行的去写在今天资料当中呢其实已经把相应的这些内容呢都给各位提供了资源里面都有有前端代码有后端代码还有我们员工管理相应的一些Circle
[00:32] 那这些呢我已经在我的idea和我的VS Code里面已经把前后端的代码全部都导入过来了还是那句话我们重点看一下后端的代码前端代码呢咱们知道它怎么写的其实都是大同小异跟之前的做法是一模一样的即可好了这边呢我们来看一下对于员工管理呢我是又启动了一个新的微服务叫做IHM IE Pro
[00:58] 这是一个新的微服务里面记录的全是员工管理相应的这些内容那在我们之前的开发流程当中涉及到的所有实体类都放到model下了所以在model下我呢也搞了很多个实体类那这些实体类里面呢比如说呢第一个这是员工归档的还是员工归档的实体类好了那接着第二个第二个呢其实就是员工转证申请的这么一个实体类
[01:30] 好了那接下来呢第三个第三个呢其实是我们的叫做员工离职申请员工离职申请的这么一个实体类好了那接着第四个第四个就是调岗申请调岗申请的实体类好了那接下来再来好了这个就是岗位信息的实体类那接下来呢第五个就是员工在我们企业当中的详情诶实体类
[02:10] 好了这些内容都比较简单接下来还有一个除了实体类部分还有一个就是我们代码里面各位来看有DODO没什么可说的就是基本的DO的一些实现DO的一些基本的实现各位应该都能看懂而且也都不难好了
[02:35] 那除了DO之外呢底下呢就是我们的Service这Service也是跟我们之前写的一样大同小异好了里面有sale方法呢还有什么fund out方法等等等等跟我们之前写的基本上都是大同小异的那我们关注的其实就是这个Controller那Controller呢只有一个employee Controller里面就是我们整个员工管理里面涉及到的所有的接口首先呢各位来看在我的页面部分呢
[03:05] 一个以来看首先呢在我的页面部分有一个叫做查看按钮这个查看按钮我们之前呢做过一个登录账户的一个设置里面呢可以去设置这个登录当前登录的这个人他的一个密码当然这个是供给我们真正员工登录进来来看的那接下来呢还有一个就是个人详情那有的朋友就说了有的朋友就说了那你这边呢之前有一个叫做新增员工
[03:33] 那这个新增员工新增的是什么其实新增的是一个首先第一个你新增的是登录我们当前这个系统的一个人员以及他的一些基础信息为了方便我们在页面进行一个管理那如果说一个员工添加了一个员工之外那我们的一些人事专员还要做什么紧接着添加了员工点击查看去补充你这个员工的详细信息就是去补充一下你这个员工他的学历是什么
[04:02] 去补充一下他的一些通信信息账号信息等等究竟是什么当然了这里面的信息也可能去做修改那需要各位注意的是上面这一部分内容公号姓名等等上面这一部分内容其实就是这个员工的基础信息就是我们刚才新增员工添加的那些你可以做更新等等这边我加了一个员工照片这个员工照片是为我们之后的课程打基础的有没有之后课程要导出pdf
[04:31] 可能要带员工的照片那还有呢我们之后可能要做刷脸登录那也应该要有员工的照片所以是为我们之后的课程打基础的我就放到这了先不解释好了那接下来对于员工个人详细信息来说呢首先呢你进来之后进来之后如果有详细信息就读取如果没有详细信息那就是空呗那所以这边必然有一个接口就是要读取详细信息那我们一起来找一下我们的空着气
[05:00] 在里面有一个员工个人信息的一个读取这个个人信息读取其实就是拿到你传递过来的这个员工的ID然后呢去我们刚才这个user company person是不是员工详细信息这个表里面去查去查查到了之后返回过来并填充数据是不是就可以了好了那接下来如果你这边的随便填点内容护照号001身份证号001
[05:28] 当然了这边呢我都没有做身份验证啊这个身份验证呢都没做好了籍贯呢比如说呢就是香港好了民族呢就不写了未婚随便填点吧好了这边保存好了保存更新之后然后呢我再刷新一下页面会发现这些呢都已经有了那我这个保存是怎么做到的注意还是看我们的这个方法好了个人信息保存那同样的同样的把你传递的这些内容
[06:03] 它传递一个map结合过来传递的内容封装成我们的个人详细信息然后呢借助我们的Service进行一个保存操作其实就可以了所以这个都没什么难度那当然除了这个之外呢还有我们这边有一个岗位信息那岗位信息也是一样的首先查没有就是空然后呢你底下进行更新好了这边呢也是两个接口第一个查询第二个更新OK那这两个我们看过了之后接下来还有一部分内容就是对于员工的一个基础的一个
[06:34] 转正调杠离职的一些说明对于转正而言你点进进来之后这里面其实保留的是你转正那个表里面相应的一些信息或者一些数据其实也就意味着你点转正那这里面他会告诉你你当前转正因为说过了你只是提交的一个是申请你会发现你点进来之后如果已转正了这边可能就是你的状态
[07:01] 变成已转正如果没转正就是把你当时提交的那些内容给你显示出来所以这个里面也意味着是什么呢你一点转正如果有信息读取没有信息你填是不是就可以啊所以对于员工转正而言呢也是对应的是两个接口一个是转正这个表单查询好了还有一个就是转正表单的保存这个都比较简单当然了还有一个调杠和离职这些都是
[07:30] 一模一样的先查询出来接着对它进行一个保存或者更新其实即可所以这里面的代码呢没有什么难度

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个员工管理系统的前后端开发流程，包括数据库表结构、Java实体类、DAO层、Service层、Controller层的代码实现，以及前端页面的展示和操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 内容：课程PPT页面，标题为“1.3 代码实现”，下方有“1.3.1 服务端实现”小节。
- 要点：介绍员工管理系统的数据库表结构，列出6张表及其说明：em_archive（月度员工归档表）、em_positive（转正申请表）、em_resignation（离职申请表）、em_transferposition（员工调岗申请表）、em_user_company_jobs（员工岗位信息表）、em_user_company_personal（员工详细信息表）。
- 画面序号：1

画面2：
- 内容：前端Vue项目代码，显示员工详情页面的表单结构。
- 要点：展示前端页面的HTML结构，包含用户名、密码输入框，以及“保存”按钮，绑定到“/employees/index”路由。
- 画面序号：2

画面3：
- 内容：Java后端代码，显示EmployeePositive实体类。
- 要点：展示Java类EmployeePositive的字段，包括userId、dateOfCorrection、correctionEvaluation、enclosure、ostatus、createTime等。
- 画面序号：3

画面4：
- 内容：Java后端代码，显示UserCompanyPersonal实体类。
- 要点：展示Java类UserCompanyPersonal的字段，包括id、userId、username、departmentName、mobile、timeOfEntry、companyID、companyName、position、status、createTime、updateTime等。
- 画面序号：4

画面5：
- 内容：Java后端代码，显示UserCompanyJobsDao接口。
- 要点：展示DAO层接口，定义了findByUserId方法。
- 画面序号：5

画面6：
- 内容：Java后端代码，显示ArchiveService类。
- 要点：展示Service层代码，包含createSpecification方法，用于构建动态查询条件。
- 画面序号：6

画面7：
- 内容：Java后端代码，显示EmployeeController类。
- 要点：展示Controller层代码，包含savePersonalInfo方法，用于保存员工个人信息。
- 画面序号：7

画面8：
- 内容：前端页面，显示员工个人详情页。
- 要点：展示员工基本信息，包括工号、姓名、入职时间、部门、手机号等。
- 画面序号：8

画面9：
- 内容：前端页面，显示员工个人详情页的“基础信息”部分。
- 要点：展示员工的最高学历、国家地区、护照号、身份证号、籍贯、婚姻状况、生日、民族等信息。
- 画面序号：9

画面10：
- 内容：前端页面，显示员工个人详情页的“账号信息”和“教育信息”部分。
- 要点：展示员工的社保账号、公积金账号、银行卡号、开户行、学历类型、毕业学校、入学时间、毕业时间、专业等信息。
- 画面序号：10

画面11：
- 内容：前端页面，显示员工个人详情页的“基础信息”部分。
- 要点：展示员工的最高学历、国家地区、护照号、身份证号、籍贯、婚姻状况、生日、民族等信息。
- 画面序号：11

画面12：
- 内容：Java后端代码，显示EmployeeController类。
- 要点：展示Controller层代码，包含saveLeave方法和findLeave方法，用于处理员工离职相关操作。
- 画面序号：12

画面13：
- 内容：前端页面，显示员工列表页。
- 要点：展示员工列表，包括序号、姓名、手机号、工号、聘用形式、部门、操作等列。
- 画面序号：13

画面14：
- 内容：前端页面，显示员工列表页。
- 要点：展示员工列表，包括序号、姓名、手机号、工号、聘用形式、部门、操作等列。
- 画面序号：14

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
package com.ihrm.common.model;
import java.util.Date;
/**
 * @author: 111
 * @date: 2018/10/11 10:53
 */
public class EmployeePositive {
    @Id
    private String userId;
    @Column(name = "dateOfCorrection")
    private Date dateOfCorrection;
    @Column(name = "correctionEvaluation")
    private String correctionEvaluation;
    @Column(name = "enclosure")
    private String enclosure;
    @Column(name = "ostatus")
    private Integer ostatus;
    @Column(name = "createTime")
    private Date createTime;
}
```

画面4：
```java
package com.ihrm.domain.employee;
import javax.persistence.*;
import java.util.Date;
@Entity
@Table(name = "em_user_company_personal")
@Data
@org.springframework.data.jpa.domain.support.AuditingEntityListener
public class UserCompanyPersonal implements Serializable {
    @Id
    private String id;
    private String userId;
    private String username;
    private String departmentName;
    private String mobile;
    private String timeOfEntry;
    private String companyID;
    private String companyName;
    private String position;
    private String status;
    private Date createTime;
    private Date updateTime;
}
```

画面5：
```java
package com.ihrm.employee.dao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.stereotype.Repository;
import com.ihrm.employee.entity.UserCompanyJobs;
@Repository
public interface UserCompanyJobsDao extends JpaRepository<UserCompanyJobs, String>, JpaSpecificationExecutor<UserCompanyJobs> {
    UserCompanyJobs findByUserId(String userId);
}
```

画面6：
```java
private Specification<EmployeeArchive> createSpecification(Map<String, Object> searchMap) {
    return new Specification<EmployeeArchive>() {
        @Override
        public Predicate toPredicate(Root<EmployeeArchive> root, CriteriaQuery<?> query, CriteriaBuilder cb) {
            List<Predicate> predicateList = new ArrayList<>();
            // 企业ID
            if (searchMap.get("companyId") != null && !"".equals(searchMap.get("companyId"))) {
                predicateList.add(cb.like(root.get("companyID").as(String.class), "%" + searchMap.get("companyId") + "%"));
            }
            // 年份
            if (searchMap.get("year") != null && !"".equals(searchMap.get("year"))) {
                predicateList.add(cb.like(root.get("year").as(String.class), "%" + searchMap.get("year") + "%"));
            }
            return cb.and(predicateList.toArray(new Predicate[predicateList.size()]));
        }
    };
}
```

画面7：
```java
@RequestBody Map map) throws Exception {
    UserCompanyPersonal sourceInfo = BeanMapUtils.mapToBean(map, UserCompanyPersonal.class);
    if (sourceInfo == null) {
        sourceInfo = new UserCompanyPersonal();
    }
    sourceInfo.setUserId(uid);
    sourceInfo.setCompanyId(super_companyId);
    userCompanyPersonalService.save(sourceInfo);
    return new Result(ResultCode.SUCCESS);
}
```

画面12：
```java
@RequestMapping(value = "/{id}/leave", method = RequestMethod.PUT)
public Result saveLeave(@PathVariable(name = "id") String uid, @RequestBody EmployeeResignation resignation) throws Exception {
    resignation.setUserId(uid);
    resignationService.save(resignation);
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/{id}/leave", method = RequestMethod.GET)
public Result findLeave(@PathVariable(name = "id") String uid) throws Exception {
    EmployeeResignation resignation = resignationService.findById(uid);
    if (resignation == null) {
        resignation = new EmployeeResignation();
    }
    resignation.setUserId(uid);
    return new Result(ResultCode.SUCCESS, resignation);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- PPT标题：“1.3 代码实现”
- 子标题：“1.3.1 服务端实现”
- 内容：数据库表结构说明，表格包含“数据库表名称”和“说明”两列。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

