# 画面线理解：19-社保管理：分页-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\19-社保管理：分页-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 02:02, 02:53, 04:22, 05:34, 06:23, 07:08, 08:37, 08:53, 09:26, 10:08, 10:45, 11:06, 11:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:22:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过自定义 SQL 查询和分页功能，实现对用户社交数据的查询，并最终在前端页面展示分页结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 `UserSocialService.java` 文件，其中 `findALL` 方法调用 `userSocialSecurityDao.findPage`，并使用 `PageResult` 包装返回值。
画面 2: 在 SQLyog 中，执行 SQL 查询 `SELECT * FROM hs_user LEFT JOIN ss_user_social_security ...`，查询用户社交数据。
画面 3: SQLyog 查询结果展示，显示了多条用户记录，包含用户名、手机号、部门、入职时间等字段。
画面 4: 在 IntelliJ IDEA 中，展示 `UserSocialSecurityDao.java` 文件，其中 `Page<T>` 类型的返回值被选中，用于定义分页方法。
画面 5: 在 IntelliJ IDEA 中，展示 `UserSocialSecurityDao.java` 文件，定义了 `findPage` 方法，使用 `@Query` 注解。
画面 6: 在 IntelliJ IDEA 中，`@Query` 注解的 `nativeQuery` 属性被设置为 `true`，并准备编写 SQL。
画面 7: 在 IntelliJ IDEA 中，编写了 `@Query` 注解的 `value` 属性，用于查询用户社交数据的 SQL。
画面 8: 在文件资源管理器中，展示项目结构，`SocialSecurityController.java` 文件位于 `controller` 目录下。
画面 9: 在 SQLyog 中，执行 SQL 查询 `SELECT bu.username, bu.mobile, ...`，查询用户社交数据。
画面 10: 在 IntelliJ IDEA 中，编写了 `findPage` 方法的完整 SQL 查询语句，包含 `SELECT` 和 `LEFT JOIN`。
画面 11: 在 IntelliJ IDEA 中，展示 `UserService.java` 文件，其中定义了 `findUserByMobile` 方法和 `departmentFeignClient` 字段。
画面 12: 在 IntelliJ IDEA 中，`UserSocialService.java` 文件中，`findPage` 方法的返回值被设置为 `PageResult`。
画面 13: 在 IntelliJ IDEA 中，展示项目结构，`SocialSecurityApplication.java` 文件位于 `src/main/java` 目录下。
画面 14: 在浏览器中，展示前端页面，显示了分页查询结果，包含用户信息和分页控件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.ihrm.social.service;
import ...
@Service
public class UserSocialService {
    @Autowired
    private UserSocialSecurityDao userSocialSecurityDao;
    //分页查询用户的社交数据
    public PageResult findAll(Integer page, Integer pageSize, String companyId) {
        //需要借助Feign调用远程服务获取用户的数据
        //直接获取社交数据信息
        return ;
    }
}
```

画面 2:
```sql
SELECT * FROM hs_user LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?
```

画面 3:
```sql
SELECT * FROM hs_user LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?
```

画面 4:
```java
public Page<T> findPage(String companyId, Pageable pageable);
```

画面 5:
```java
@Query
public Page findPage(String companyId, Pageable pageable);
```

画面 6:
```java
@Query(nativeQuery = true,
       value = "",
       countQuery = "")
```

画面 7:
```java
@Query(nativeQuery = true,
       value = "SELECT COUNT(*) FROM hs_user u LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?1",
       countQuery = "SELECT COUNT(*) FROM hs_user u LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?1")
public Page findPage(String companyId, Pageable pageable);
```

画面 8:
```
controller
├── SocialSecurityController.java
```

画面 9:
```sql
SELECT bu.username, bu.mobile, bu.work_number, bu.department_name, bu.time_of_entry, bu.time_of_dimission, bu.participating_in_the_city, bu.participating_in_the_city_id, bu.providing_fund_city_id, bu.providing_fund_city_name, bu.social_security_base, bu.social_security_base_id, bu.providing_fund_base FROM hs_user bu LEFT JOIN ss_user_social_security ss ON bu.id = ss.user_id WHERE company_id=?
```

画面 10:
```java
@Query(nativeQuery = true,
       value = "SELECT bu.id, bu.username, bu.mobile, bu.work_number, bu.department_name, bu.time_of_entry, bu.time_of_dimission, bu.participating_in_the_city, bu.participating_in_the_city_id, bu.providing_fund_city_id, bu.providing_fund_city_name, bu.social_security_base, bu.social_security_base_id, bu.providing_fund_base FROM hs_user bu LEFT JOIN ss_user_social_security ss ON bu.id = ss.user_id WHERE company_id=?1",
       countQuery = "SELECT COUNT(*) FROM hs_user bu LEFT JOIN ss_user_social_security ss ON bu.id = ss.user_id WHERE company_id=?1")
public Page<Map> findPage(String companyId, Pageable pageable);
```

画面 11:
```java
@Service
public class UserService extends BaseService {
    @Autowired
    private UserDao userDao;
    @Autowired
    private RoleDao roleDao;
    @Autowired
    private IdWorker idWorker;
    //根据手机号查询用户
    public User findByMobile(String mobile) { return userDao.findByMobile(mobile); }
    @Autowired
    private DepartmentFeignClient departmentFeignClient;
    //批量保存用户
}
```

画面 12:
```java
return new PageResult(page.getTotalElements(), page);
```

画面 13:
```
src/main/java
├── com.ihrm.system
│   ├── client
│   ├── controller
│   ├── dao
│   ├── service
│   ├── constant
│   ├── domain
│   └── vo
└── SocialSecurityApplication.java
```

画面 14:
```
// 前端页面内容
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
