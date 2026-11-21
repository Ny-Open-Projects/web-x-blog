# 画面线理解：13-审批列表：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\13-审批列表：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 00:50, 01:12, 01:49, 02:21, 02:50, 03:12, 03:38, 03:57, 04:36, 05:36, 06:14, 06:29, 07:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:09:11

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
