# 画面线理解：18-企业微服务：实现crud操作之service

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\18-企业微服务：实现crud操作之service_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:56, 03:17, 04:22, 04:53, 05:33, 06:27, 08:36, 09:12, 10:03, 10:57, 11:19, 11:45, 11:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:00:20

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，如何在 Service 层通过注入 Dao 层，实现对 Company 实体的增删改查（CRUD）操作，并展示了如何使用 IdWorker 生成主键 ID。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了测试类 CompanyDaoTest.java，其中包含一个测试方法 test()，用于验证 companyDao.findById("1").get() 的功能。
- 代码中注释说明了 save、deleteById、findById、findAll 的功能。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/dao/CompanyDao.java 和 CompanyApplication.java。

画面 2：
- 展示了 Service 层的 CompanyService.java 文件，其中定义了 @Service 注解和一个私有成员变量 companyDao。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 3：
- 展示了 CompanyService.java 文件，其中定义了 add 方法，用于保存企业。
- 代码中注释说明了“保存企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/domain/company/Company.java。

画面 4：
- 展示了启动类 CompanyApplication.java，其中使用了 @SpringBootApplication 注解，并配置了 @EntityScan 和 @ComponentScan。
- 代码中注释说明了 Spring Boot 的自动配置和包扫描。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/CompanyApplication.java。

画面 5：
- 展示了 CompanyService.java 文件，其中定义了 add 方法，用于保存企业。
- 代码中注释说明了“保存企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 6：
- 展示了 CompanyService.java 文件，其中定义了 add 方法，用于保存企业。
- 代码中注释说明了“保存企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 7：
- 展示了 CompanyService.java 文件，其中定义了 add 方法，用于保存企业。
- 代码中注释说明了“保存企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 8：
- 展示了 CompanyService.java 文件，其中定义了 update 方法，用于更新企业。
- 代码中注释说明了“更新企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 9：
- 展示了 CompanyService.java 文件，其中定义了 update 方法，用于更新企业。
- 代码中注释说明了“更新企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 10：
- 展示了 CompanyService.java 文件，其中定义了 deleteById 方法，用于删除企业。
- 代码中注释说明了“删除企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 11：
- 展示了 CompanyService.java 文件，其中定义了 findById 方法，用于根据 ID 查询企业。
- 代码中注释说明了“根据 ID 查询企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 12：
- 展示了 CompanyService.java 文件，其中定义了 findAll 方法，用于查询所有企业。
- 代码中注释说明了“查询企业列表”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 13：
- 展示了 CompanyService.java 文件，其中定义了 findAll 方法，用于查询所有企业。
- 代码中注释说明了“查询企业列表”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

画面 14：
- 展示了 CompanyService.java 文件，其中定义了 findAll 方法，用于查询所有企业。
- 代码中注释说明了“查询企业列表”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/service/CompanyService.java。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
public class CompanyDaoTest {
    @Autowired
    private CompanyDao companyDao;

    @Test
    public void test() {
        Company company = companyDao.findById("1").get();
        System.out.println(company);
    }
}
```

画面 2：
```java
package com.ihrm.company.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;
}
```

画面 3：
```java
@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;

    /**
     * 保存企业
     */
    public void add(Company company) {
        // 基本属性的设置
    }
}
```

画面 4：
```java
package com.ihrm.company;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class CompanyApplication {
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }
}
```

画面 5：
```java
@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;
    @Autowired
    private IdWorker idWorker;

    /**
     * 保存企业
     * 1. 配置idworker工具
     * 2. 在service中注入idworker
     * 3. 通过idworker生成id
     * 4. 保存企业
     */
    public void add(Company company) {
        // 基本属性的设置
    }
}
```

画面 6：
```java
@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;
    @Autowired
    private IdWorker idWorker;

    /**
     * 保存企业
     * 1. 配置idworker工具
     * 2. 在service中注入idworker
     * 3. 通过idworker生成id
     * 4. 保存企业
     */
    public void add(Company company) {
        String id = idWorker.nextId() + "";
        company.setId(id);
        company.setAuditState("0"); // 0. 未审核，1. 已审核
        company.setState(1); // 0. 未激活，1. 已激活
        companyDao.save(company);
    }
}
```

画面 7：
```java
@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;
    @Autowired
    private IdWorker idWorker;

    /**
     * 保存企业
     * 1. 配置idworker工具
     * 2. 在service中注入idworker
     * 3. 通过idworker生成id
     * 4. 保存企业
     */
    public void add(Company company) {
        String id = idWorker.nextId() + "";
        company.setId(id);
        company.setAuditState("0"); // 0. 未审核，1. 已审核
        company.setState(1); // 0. 未激活，1. 已激活
        companyDao.save(company);
    }
}
```

画面 8：
```java
/**
 * 更新企业
 * 1. 参数：(company)
 * 2. 根据id查询企业对象
 * 3. 设置修改的属性
 * 4. 调用dao完成更新
 */
public void update(Company company) {
    Company temp = companyDao.findById(company.getId()).get();
    temp.setName(company.getName());
    temp.setCompanyPhone(company.getCompanyPhone());
    companyDao.save(temp);
}
```

画面 9：
```java
/**
 * 更新企业
 * 1. 参数：(company)
 * 2. 根据id查询企业对象
 * 3. 设置修改的属性
 * 4. 调用dao完成更新
 */
public void update(Company company) {
    Company temp = companyDao.findById(company.getId()).get();
    temp.setName(company.getName());
    temp.setCompanyPhone(company.getCompanyPhone());
    companyDao.save(temp);
}
```

画面 10：
```java
/**
 * 删除企业
 * 1. 参数：(id)
 * 2. 调用dao完成删除
 */
public void deleteById(String id) {
    companyDao.deleteById(id);
}
```

画面 11：
```java
/**
 * 根据id查询企业
 * 1. 参数：(id)
 * 2. 调用dao完成查询
