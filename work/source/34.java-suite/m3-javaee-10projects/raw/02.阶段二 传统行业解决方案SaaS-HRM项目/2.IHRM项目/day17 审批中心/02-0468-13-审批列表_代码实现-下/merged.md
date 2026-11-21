# 13-审批列表：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\13-审批列表：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 时长 7分32秒（音频 452s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们刚才呢简单的把查询的这个流程呢做了一个分析一共就三步那接下来呢我们就开始把这个代码呢给它实现出来那我们都知道要构造special case所以我就开始special case那在这边得到的是instance类型的special case好了spec等于new一个special case对象出来那接下来在重写的方法当中我们构造查询条件
[00:37] 那查询条件如果我们构造好了之后接下来呢调用do完成查询中间条件我们一会儿再说那最后一步比较简单do点我们叫做findall那翻到注意我们是带分页的翻到所以我来翻到方法在这放在这第一个咱们的special case第二个是不是需要一个分页的这么一个分页对象那咱们开始把spec传递过去那除了spec之外
[01:07] 还有我们的分页对象那分页对象咱们需要自己构造就是new一个page request这是我们的常规操作那接着把page和save传递过去就可以了当然了page我们需要a-1好了那现在呢咱们已经把对应的这些基本的简单流程呢已经搞定了这边加一个return好了那中间咱们需要构造这个传语条件那构造传语条件注意啊我们知道
[01:40] 我们传入的这个参数呢可能会比较多咱们说过了参数可能有这么三项所以我们构造产业条件的时候也是往这三项上面来进行靠拢那有多个产业条件那我们在上边就可以以list的形式咱们来接收多个条件predicate这是我们的条件好了来一个list等于new一个arree list
[02:12] 没错吧好了我们这个审批类型其实对应的是我们传递参数里面的这个标志key这边先说清楚好了审批状态其实对应的是我们这里面的state那接下来呢还有一个当前节点审批ID有这么三个那咱们一个一个来看审批类型那审批类型说过了它只有一个那所以这边呢我们先做一个判断if
[02:48] 你传递过来的instance.getPolicyKey它一定不等于NOW我们才能加条件所以streetUtils.isEmpty不为空不为空我们要加条件没错吧好了同理我们底下要加条件都是不为空getState不为空那接着代处理人同样的道理一个一个的给它添加过来点getPLC
[03:23] current node UID那接下来呢第一个那审批类型如果不为空的话我们就开始构造它这个审批的类型那审批类型呢我们就可以cb.ecos不是这边呢太长了我喜欢用cb啊咱们就是cb.用ecos的形式来进行查询那我们这里面的代码希望各位还知道希望各位还有印象怎么去写
[03:53] cb.ecos就是root.get那get的是什么就是你这边对应的字段名称ok.s把它理解为一个什么类型.s好了我们就说了是一个string.class好了那接下来第二个代表的是你的参数你的参数其实已经传递过来了没错了那我们可以把对应的这个条件呢
[04:27] 添加到list集合当中那这样一来这边list.add添加到我们这个list集合当中好了那审批类型我们处理完了之后还有一个就是审批状态这个审批状态这个相对来说麻烦一点我们先看这个处理人这个处理人相对来说比较简单跟上面就是一模一样一模一样都是ecos的形式来进行处理那注意了是这儿
[05:00] 如果各位用ecos的话这边呢可能会有一个小小的问题是这样的我们都知道咱们这边带审批的这个intens这个带审批人这个带审批人呢可能啊他有两个或者有三个因为之前有条件说了就是部门里面的任一个人员都可以审批所以这边呢咱们部门有仨我就把这三个人都可以给他放到这边
[05:31] 那这个怎么办那我们这边就不能用ECOS来查所以我们用一个like模糊查询那我们前面加上本号后边加上本号是不是就可以了好了那这个我们看过了之后接下来呢还有一个就是审批状态那审批状态这个就不言而喻了那就是说了这里面肯定是用逗号隔开所以肯定有多个这个审批状态那多个审批状态我们这边
[06:04] 就是这样写expressions expression死句类型的这个我来写就可以了esp等于root是死句类型的做一个范形的说明get好了pros state属性名称好了这个代表的是我要跟这个玩意里面要进行查询
[06:45] 好了,接下来这个查询方式,exp代表的是我一会儿要用in查询,所以我就exp.in的方式来进行查询,那in的方式查什么?
[06:56] 注意我们参数传递过来,是不是可能有123有多个,那里面接收的是一个数组,所以我需要进行isplit以逗号来进行处理,那这样一来,其实我代表的就是我要以这个字段进行in查询,
[07:12] 那硬查询这些数据在哪儿是传递过来的以逗号隔开所以我逗号一分割是不是构造了一个数组同样的list.add给它添加过来那这样一来我们当前的这个方法呢就已经全部都写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中，演示如何使用 Spring Data JPA 的 Specification 接口，通过 CriteriaBuilder 动态构建查询条件，实现对业务申请记录的条件查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：在 AuditService.java 中，定义了 getInstancesList 方法，使用 Specification 构造查询条件，代码中注释说明“使用Specification查询，构造Specification”。光标位于 `new Specification<ProcInstance>()` 后，IDE 提示补全 `NEW` 方法。
画面 2：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAll`、`findAny` 等。
画面 3：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 4：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 5：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 6：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 7：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 8：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 9：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 10：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 11：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 12：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 13：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。
画面 14：在 `getInstancesList` 方法中，光标位于 `return` 后，IDE 提示补全 `Predicate` 类型的方法，如 `findAny`、`findFirst` 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import com.ihm.audit.dao.ProcInstanceDao;
import com.ihm.audit.entity.ProcInstance;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;

@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询
        return procInstanceDao.findAll(spec, new Pageable(page - 1, size));
    }
}
```

画面 2：
```java
import javax.persistence.criteria.Root;
@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询
        return procInstanceDao.findAll(spec, new Pageable(page - 1, size));
    }
}
```

画面 3：
```java
import javax.persistence.criteria.Root;
@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询
        return procInstanceDao.findAll(spec, new Pageable(page - 1, size));
    }
}
```

画面 4：
```java
import javax.persistence.criteria.Root;
@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询
        return procInstanceDao.findAll(spec, new Pageable(page - 1, size));
    }
}
```

画面 5：
```java
import java.util.List;
@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询
        return procInstanceDao.findAll(spec, new Pageable(page - 1, size));
    }
}
```

画面 6：
```java
import java.util.List;
@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询
        return procInstanceDao.findAll(spec, new Pageable(page - 1, size));
    }
}
```

画面 7：
```java
import java.util.List;
@Service
public class AuditService {
    @Autowired
    private ProcInstanceDao procInstanceDao;

    /**
     * 查询所有的业务的申请情况
     */
    public Page getInstancesList(ProcInstance instance, int page, int size) {
        //1.使用Specification查询，构造Specification
        Specification<ProcInstance> spec = new Specification<ProcInstance>() {
            //2.定义查询条件（根据传入的参数动态构造）
            @Override
            public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
                return null;
            }
        };
        //3.调用dao进行Specification查询

