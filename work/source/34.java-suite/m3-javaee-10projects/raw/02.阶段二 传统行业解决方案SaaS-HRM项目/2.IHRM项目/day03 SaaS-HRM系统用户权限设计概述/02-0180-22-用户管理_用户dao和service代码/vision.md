# 画面线理解：22-用户管理：用户dao和service代码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\22-用户管理：用户dao和service代码_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:52, 01:36, 02:39, 04:03, 04:45, 06:26, 07:09, 08:57, 11:38, 13:27, 15:02, 15:41, 16:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:39:29

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SaaS-HRM 系统中，通过 Spring Data JPA 的 Specification 方式实现用户实体的动态查询和分页功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示用户实体类 User.java 的代码，包含 @Entity、@Table 注解和 Lombok 的 Getter、Setter。
画面 2: 展示 UserDAO 接口，继承 JpaRepository，用于定义数据访问层。
画面 3: 展示 DepartmentService.java 中的 findALL 方法，用于根据公司ID查询部门。
画面 4: 展示用户新增接口的 API 文档，POST /user，请求体为 User 实体。
画面 5: 展示 UserServicе.java 中的 update 方法，用于更新用户信息。
画面 6: 展示 UserServicе.java 中的 findAll 方法，用于根据公司ID查询用户。
画面 7: 展示项目整体结构和相关工具（如 IntelliJ IDEA、SQLyog、Postman）的多窗口视图。
画面 8: 展示 UserServicе.java 中的 deleteById 方法，用于删除用户。
画面 9: 展示 UserServicе.java 中的 findAll 方法，用于查询用户列表。
画面 10: 展示 UserServicе.java 中的 toPredicate 方法，用于构建动态查询条件。
画面 11: 展示 UserServicе.java 中的 toPredicate 方法，继续构建动态查询条件。
画面 12: 展示 UserServicе.java 中的 toPredicate 方法，继续构建动态查询条件。
画面 13: 展示 UserServicе.java 中的 findAll 方法，用于分页查询用户。
画面 14: 展示 UserServicе.java 中的 findAll 方法，用于分页查询用户。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

/**
 * 用户实体类
 */
@Entity
@Table(name = "bs_user")
@Getter
@Setter
```

画面 2:
```java
package com.ihrm.system.dao;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserDao extends JpaRepository<User, String> {
}
```

画面 3:
```java
public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
    //根据企业id查询
    return cb.equal(root.get("companyId"), companyId);
}
```

画面 4:
```json
{
  "id": "string",
  "mobile": "string",
  "username": "string",
  "password": "string",
  "role": "string",
  "enableSource": "string",
  "createName": "string",
  "departmentId": "string",
  "fromEmployment": "string",
  "notMaintain": "string",
  "formOffHirement": "string",
  "workingDay": "string",
  "serviceStatus": "string",
  "company": "string",
  "upperDeptName": "string"
}
```

画面 5:
```java
public void update(User user) {
    //根据id查询用户
    User target = userDao.findById(user.getId()).get();
    //设置用户名
    target.setUsername(user.getUsername());
    //更新
    userDao.save(target);
}
```

画面 6:
```java
public List<User> findAll(String companyId) {
    //用户构造查询条件
    Specification<User> spec = new Specification<User>() {
        @Override
        public Predicate toPredicate(Root<User> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            //根据企业id查询
            return cb.equal(root.get("companyId").as(String.class), companyId);
        }
    };
    return userDao.findAll(spec);
}
```

画面 7:
```json
{
  "code": 0,
  "flag": true,
  "message": "string",
  "data": {
    "total": 0
  }
}
```

画面 8:
```java
public void deleteById(String id) {
    userDao.deleteById(id);
}
```

画面 9:
```java
public List<User> findAll(Map<String, Object> map) {
    //1.需要查询条件
    Specification<User> spec = new Specification<User>() {
        @Override
        public Predicate toPredicate(Root<User> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            return null;
        }
    };
    return userDao.findAll(spec);
}
```

画面 10:
```java
public Predicate toPredicate(Root<User> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
    List<Predicate> list = new ArrayList<>();
    if (!StringUtils.isEmpty(map.get("companyId"))) {
        list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String) map.get("companyId")));
    }
    return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
}
```

画面 11:
```java
public Predicate toPredicate(Root<User> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
    List<Predicate> list = new ArrayList<>();
    if (!StringUtils.isEmpty(map.get("companyId"))) {
        list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String) map.get("companyId")));
    }
    if (!StringUtils.isEmpty(map.get("departmentId"))) {
        list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String) map.get("departmentId")));
    }
    return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
}
```

画面 12:
```java
public Predicate toPredicate(Root<User> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
    List<Predicate> list = new ArrayList<>();
    if (!StringUtils.isEmpty(map.get("companyId"))) {
        list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String) map.get("companyId")));
    }
    if (!StringUtils.isEmpty(map.get("departmentId"))) {
        list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String) map.get("departmentId")));
    }
    if (StringUtils.isEmpty(map.get("hasDept")) || "0".equals((String) map.get("hasDept"))) {
        list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
    } else {
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    }
    return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
}
```

画面 13:
```java
public Page findAll(Map<String, Object> map, int page, int size) {
    //1.需要查询条件
    Specification<User> spec = new Specification<User>() {
        @Override
        public Predicate toPredicate(Root<User> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            List<Predicate> list = new ArrayList<>();
            if (!StringUtils.isEmpty(map.get("companyId"))) {
                list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String) map.get("companyId")));
            }
            if (!StringUtils.isEmpty(map.get("departmentId"))) {
                list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String) map.get("departmentId")));
            }
            if (StringUtils.isEmpty(map.get("hasDept")) || "0".equals((String) map.get("hasDept"))) {
                list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
            } else {
                list.add(criteriaBuilder.isNull(root.get("departmentId")));
            }
            return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
        }
    };
    return userDao.findAll(spec, new PageRequest(page, size));
}
```

画面 14:
```java
public Page findAll(Map<String, Object> map, int page, int size) {
    //1.需要查询条件
    Specification<User> spec = new Specification<User>() {
        @Override
        public Predicate toPredicate(Root<User> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            List<Predicate> list = new ArrayList<>();
            if (!StringUtils.isEmpty(map.get("companyId"))) {
                list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String) map.get("companyId")));
            }
            if (!StringUtils.isEmpty(map.get("departmentId"))) {
                list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String) map.get("departmentId")));
            }
            if (StringUtils.isEmpty(map.get("hasDept")) || "0".equals((String) map.get("hasDept"))) {
                list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
            } else {
                list.add(criteriaBuilder.isNull(root.get("departmentId")));
            }
            return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
        }
    };
    return userDao.findAll(spec, new PageRequest(page, size));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
