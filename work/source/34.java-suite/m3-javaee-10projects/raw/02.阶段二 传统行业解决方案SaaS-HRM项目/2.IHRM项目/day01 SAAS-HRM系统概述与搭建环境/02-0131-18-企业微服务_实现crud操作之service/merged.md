# 18-企业微服务：实现crud操作之service

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\18-企业微服务：实现crud操作之service_【海量资源尽在 ubkz.com】.mp4
- 时长 12分3秒（音频 723s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] DU层代码我们编写好了之后接下来我们就开始继续往下去搞我们的Service对于Service来说有了DUservice就比较简单了我们应该怎么做呢好了打开我们的idea在我们当前company工程下创建一个我们自己的Service来一class把它放到ser vse这个包下我就叫做company Service
[00:32] P-A-N-Ycompany的serviceS-E-R-V-I-C-EOK好了Service创建好了注意这是一个对象我们应该交给死亡人容器管理所以at Service进行一个创建对象的一个过程那接下来我这个Service当中呢可能还依赖于do所以at auto wear自动注入进来private我们的docompanycompanydo
[01:03] 好了那接下来我们在Service当中要完成的操作一共有这么几项首先呢第一个我们叫做保存企业还有第二个更新企业基本增长改查嘛好了那接下来第三个第三个呢我们叫做删除企业还有根据ID查询企业以及最后一个
[01:39] 我们叫做查询全部企业列表好了这是我们要完成的五个功能那我们一个一个的来首先保存那对于保存来说public will id我为了快速我这边就写了一个没有返回值那方法名呢叫做add那你可以把你所有传递过来的参数封装到一个company对象给我
[02:13] 那但是呢我想跟各位要声明的要声明的就是在我们完成保存操作的过程当中其中我们传递过来的这些参数可能没有ID那没有ID那我怎么做呢所以我需要对你的一些基本参数进行一个设置因为对于我们前端传递到后端的一些代码来说呢
[02:45] 他可能告诉我啊你要保存的这个企业名称是什么这个企业行业是什么但是他没有ID我们ID是不是借助ID生成器的形式给我们构造过来的那所以注意基本属性的设置我们设置就应该要把ID生成器通过ID生成器生成一个ID给他复制过来
[03:06] 那所以我们应该想方设法的能够在我当前的工程当中构造出ID生成器那ID生成器我们创建了一个对象这个对象呢在哪呢就是我们刚才写好的一个工具类把它放到common包下了我们一起来找一下ID worker那咱们需要把这个ID worker把它配置到我当前的这个系统当中那配置到当前系统当中我们要做的事情注意
[03:38] 首先呢第一件事就是配置ID worker到我们当前的工程中好了接下来在Service中呢我们注入ID worker好了接着第三件事通过ID worker生成ID好了接着最后一件事才是真正的我们叫做保存企业那好了我们一个一个来看配置ID worker到工程当中那我们可以把它
[04:15] 在我们的工程启动的过程当中以bin的方式爱他bin的方式把它配置到我们钢琴工程里那好了配置到钢琴工程啪啵立刻好了ID worker比如说就叫做ID worker了那好了里面写的代码相对来说比较简单returnnew一个ID workerOK那这样一来我的IT worker就已经出世话了
[04:44] 那ID Worker处理化之后在我的Servi当中就比较简单了那在Servi当中我们可以通过atAutoWearPrivateID WorkerID Worker注入进来我们刚才写的方法就相当于创建了一个对象创建交给Servi管理那接着这步我们第二步注入注入进来之后
[05:07] 我们设置属性的时候就可以通过ID worker打点它有一个方法叫做next id自动生成ID worker雪花算法刚才说过了好了它是一个死菌类型的注意这个next它其实得到的是一个lang类型的那我们需要把它转化成一个死菌类型很简单加OK那接着company打点set id把id复制进去即可
[05:39] 那当然了我们这个企业你保存的时候呢可能还有一些参数他不会告诉你比如说呢我们可以有一些默认的状态默认状态默认状态刚才我们看过了这个用户他究竟是否可用那我们可以对这个默认状态给他进行一个设置company.setstatestate有两个第一个叫做adult
[06:11] state这玩意儿代表的是否审核我们0代表未审核1代表审核通过所以我来个1配到这边来个1死去内向的好了当然了还有一个company.setstate这个state呢比如说0代表已激活1或者1代表已激活0代表未激活已激活好了上边这个0未审核1已审核
[06:57] 这个是我随便写的当然了我们真正保存进来肯定是一个未审核的一个记录啊OK那改成0吧未审核好了那这样一来呢我们基本的属性配置好属性配置好了接着第四步保存那保存企业借助do打点save方法完成保存操作company即可OK那这样一来这样一来我们基本的保存代码就已经写好了
[07:25] 那保存代码写好了之后咱们继续往下看继续往下看就是更新企业那对于更新企业来说呢我们写的步骤先跟各位来分析一下首先呢第一件事我们更新企业它给我传递过来的其实也是一个company对象我们的参数必然有就是你前端可能要输入很多的内容要输入很多的内容
[07:53] 那我们就开始更新那我们把所做的内容封装到一个对象当中就是company对象好那接下来我们操作如何去做呢但千万各位别忘了我们进行更新的过程永远都是先查再更所以我第二步就是根据ID先去查询出我们的企业对象那接下来在查询的对象的基础之上复职修改的属性值
[08:29] 好了接着第四步调用 deal完成更新操作好了那这个步骤呢我们做了一个分析那接下来呢我们就可以publicvoid我就叫update了同样的传递过来一个对象OK里面的这个代码的写法呢不难也比较简单参数我们写好了那接下来根据id查询company比如说我叫temp等于company deal打点
[09:06] 我们叫做find by id那company.getid.get注意company对象里面其实有id嘛更新看上有id那根据id查询出来查询出来之后呢temp打点可以设置一些它的属性比如说你要修改名称set name好了你要修改成什么样打点get name那比如说你还可以设置temp打点set
[09:40] 再来一个吧设置于什么呀比如说你的联系电话company打点get company phoneOK我们就先写两个我们先测试一下能不能用其实就可以了OK那这样一来我们把基本要修改的属性配置好了配置好了之后最后调用company do打点c5方法好了把time lake传进去即可那这个时候有朋友就疑问了上面叫c5底下也叫c5
[10:11] 它怎么就能区分出是保存还是更新呢其实对于Spring Data JPA它内部的执行流程先去根据你传的ID查一把如果能查出来代表要更新如果查不出来就代表要保存就是一个道理OK那到目前为止呢我两个方法已经写好了接着第三个方法删除这个删除比较简单咱们就直接把它写好了PUB LIC
[10:41] Viu ID delete注意delete我们根据ID审delete by ID那我传递过来就是一个死菌类型的ID即可刚才已经说过了删除很简单直接调用DO的方法打点delete by ID把ID传进去即可好了根据ID查询起列这个它有返回值了根据ID查询起列返回的其实就应该是我们的company对象就find by ID了
[11:12] 传递一个死菌类型的ID进来好了这边直接returncompany.do打点findbyid好了打点get注意这是它的一个特有的一种语法特征findbyid开始查从里面得到你要查询的对象这是它的固定的写法好了呢接下来还有最后一个查询企业列表company列表是一个例子集合company好了我叫findall
[11:43] 这个没有参数比较简单直接returncompany do打点叫做find all之前说过了OK那这样一来我们思维层的代码就已经写好了完成了保存更新删除根据ID查询以及查询列表的相关工作OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，如何在 Service 层通过注入 Dao 层，实现对 Company 实体的增删改查（CRUD）操作，并展示了如何使用 IdWorker 生成主键 ID。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了测试类 CompanyDaoTest.java，其中包含一个测试方法 test()，用于验证 companyDao.findById("1").get() 的功能。
- 代码中注释说明了 save、deleteById、findById、findAll 的功能。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/dao/CompanyDao.java 和 CompanyApplication.java。

画面 2：
- 展示了 Service 层的 CompanyService.java 文件，其中定义了 @Service 注解和一个私有成员变量 companyDao。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

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
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 6：
- 展示了 CompanyService.java 文件，其中定义了 add 方法，用于保存企业。
- 代码中注释说明了“保存企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 7：
- 展示了 CompanyService.java 文件，其中定义了 add 方法，用于保存企业。
- 代码中注释说明了“保存企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 8：
- 展示了 CompanyService.java 文件，其中定义了 update 方法，用于更新企业。
- 代码中注释说明了“更新企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 9：
- 展示了 CompanyService.java 文件，其中定义了 update 方法，用于更新企业。
- 代码中注释说明了“更新企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 10：
- 展示了 CompanyService.java 文件，其中定义了 deleteById 方法，用于删除企业。
- 代码中注释说明了“删除企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 11：
- 展示了 CompanyService.java 文件，其中定义了 findById 方法，用于根据 ID 查询企业。
- 代码中注释说明了“根据 ID 查询企业”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 12：
- 展示了 CompanyService.java 文件，其中定义了 findAll 方法，用于查询所有企业。
- 代码中注释说明了“查询企业列表”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 13：
- 展示了 CompanyService.java 文件，其中定义了 findAll 方法，用于查询所有企业。
- 代码中注释说明了“查询企业列表”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

画面 14：
- 展示了 CompanyService.java 文件，其中定义了 findAll 方法，用于查询所有企业。
- 代码中注释说明了“查询企业列表”的步骤。
- 画面中显示了项目结构，包括 src/main/java/com.ihrm.company/Service/CompanyService.java。

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
package com.ihrm.company.Service;
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
     * 2. 在Service中注入idworker
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
     * 2. 在Service中注入idworker
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
     * 2. 在Service中注入idworker
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

