# 画面线理解：17-企业微服务：实现crud操作之dao接口

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\17-企业微服务：实现crud操作之dao接口_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:04, 01:28, 02:02, 02:35, 02:46, 03:11, 03:25, 03:52, 04:11, 04:36, 04:55, 05:38, 07:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:59:28

1) 这一组画面整体在讲如何为 Spring Boot 项目中的 Company 实体编写 DAO 层接口和对应的单元测试，并解决因实体类缺少无参构造器导致的测试失败问题。

2) 按时间顺序列出每张画面的要点：
画面1：在 IDEA 中右键点击 Company.java，弹出菜单，准备进行重构或运行测试。
画面2：打开 CompanyDao.java 文件，显示其初始状态，仅包含 extends JpaRepository 的声明。
画面3：在 CompanyDao.java 中修改接口，指定泛型为 Company 和 String。
画面4：在 CompanyDao.java 中继续修改，添加了 JpaSpecificationExecutor 接口，以支持更复杂的查询。
画面5：打开 CompanyDaoTest.java 文件，显示其初始状态，包含 SpringBootTest 和 @SpringBootApplication 注解。
画面6：在 CompanyDaoTest.java 中，添加了 @Autowired 注解，用于注入 CompanyDao。
画面7：在 CompanyDaoTest.java 中，编写测试方法 test()，调用 companyDao.findById("1")。
画面8：在 CompanyDaoTest.java 中，为 test() 方法添加了 @Test 注解。
画面9：在 CompanyDaoTest.java 中，执行测试，控制台显示测试通过。
画面10：在 CompanyDaoTest.java 中，测试失败，错误信息为“Exception: No default constructor for entity: ...Company”。
画面11：在 Company.java 中，为实体类添加了 @AllArgsConstructor 注解，以提供无参构造器。
画面12：在 CompanyApplication.java 中，配置了 @EntityScan 注解，指定扫描包路径。
画面13：在 CompanyDaoTest.java 中，测试通过，控制台显示测试成功。
画面14：在 CompanyDaoTest.java 中，测试通过，控制台显示测试成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2：
```java
package com.ihrm.company.dao;
import org.springframework.data.jpa.repository.JpaRepository;
public interface CompanyDao extends JpaRepository<Company, String> {
}
```

画面3：
```java
package com.ihrm.company.dao;
import org.springframework.data.jpa.repository.JpaRepository;
public interface CompanyDao extends JpaRepository<Company, String> {
}
```

画面4：
```java
package com.ihrm.company.dao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
public interface CompanyDao extends JpaRepository<Company, String>, JpaSpecificationExecutor<Company> {
}
```

画面5：
```java
package com.ihrm.company;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.annotation.Configuration;
@SpringBootTest
class CompanyDaoTest {
}
```

画面6：
```java
package com.ihrm.company;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
class CompanyDaoTest {
    @Autowired
    private CompanyDao companyDao;
}
```

画面7：
```java
package com.ihrm.company;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
class CompanyDaoTest {
    @Autowired
    private CompanyDao companyDao;
    @Test
    public void test() {
        companyDao.findById("1");
    }
}
```

画面8：
```java
package com.ihrm.company;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
class CompanyDaoTest {
    @Autowired
    private CompanyDao companyDao;
    @Test
    public void test() {
        Company company = companyDao.findById("1").get();
    }
}
```

画面10：
```java
@Test
public void test() {
    Company company = companyDao.findById("1").get();
}
```

画面11：
```java
@Entity
@Table(name = "co_company")
@Data
@AllArgsConstructor
public class Company implements Serializable {
    private static final long serialVersionUID = 594829320797158219L;
    @Id
    private String id;
    @Column
    private String name;
}
```

画面12：
```java
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
@SpringBootApplication
@EntityScan(value = "com.ihrm.company")
public class CompanyApplication {
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
