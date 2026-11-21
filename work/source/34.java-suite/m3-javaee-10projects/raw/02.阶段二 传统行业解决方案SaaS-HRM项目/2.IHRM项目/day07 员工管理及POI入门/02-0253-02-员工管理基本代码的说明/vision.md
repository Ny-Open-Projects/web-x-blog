# 画面线理解：02-员工管理基本代码的说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\02-员工管理基本代码的说明_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:47, 01:22, 02:05, 02:35, 02:45, 02:59, 03:56, 04:46, 05:45, 06:13, 06:28, 07:08, 07:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:48:00

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
