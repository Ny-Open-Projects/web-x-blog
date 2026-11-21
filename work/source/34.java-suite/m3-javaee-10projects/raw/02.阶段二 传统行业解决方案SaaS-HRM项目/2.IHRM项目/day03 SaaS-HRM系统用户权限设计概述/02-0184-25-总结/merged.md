# 25-总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\25-总结_【海量资源尽在 ubkz.com】.mp4
- 时长 2分2秒（音频 123s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了到目前为止呢我们今天的所有内容就跟各位都聊过了其实对于我们今天来说呢完成了组织机构的一个增长改差当然这一块讲的内容会比较多因为我们从头到尾的看一下整个的模块是如何搭建出来的那我们以这个为基础其实去做我们的用户去做我们的角色就简单了很多那第二块我们讲的是一个RBAC的一个模型那这个模型是我们现在很多企业里面构造权限控制的依赖
[00:28] 现在都基本是用RBAC的形式来做的我们这边SaaS平台其实也是用RBAC这套模型来完成的我们的一个操作而已只不过会被这个操作进行了一个扩展我们把它分成了用户角色权限以及资源好了里面我们设计到了一些表我们可以简单的看一下用户角色权限权限又分为菜单页面元素和API两个多的多接下来我们快速的搭建了一个用户的管理
[00:58] 那这些我们看过了之后最后呢就是有这么一个作业那最后做一个作业呢是希望各位能够参照我给各位发的一些案例代码完成一个角色的基本增传改查其实这个也比较简单和用户基本上差不多各位以作业的形式咱们自己去完成一下就可以了当然了这个角色这个角色管理里面呢其实也给各位提供了什么需要一些实体类咱们都有
[01:23] 持久化层也是一模一样的思维层基本上都是差不多的就是完成基本的增深改查当然了最后还有一个控制器层那控制器层这边也有添加update delete根据ID查询以及find page和我们的用户实现起来都差不多当然了在今天资料当中呢也把我们
[01:45] 角色相关涉及到的一些前端代码给各位下发下去各位可以参照的这些前端代码在siting当中在siting当中各位可以参照的这些前端代码去把我们部门所涉及到的增深改查前端后端和我们的服务全把它搞定OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个 SaaS 系统中用户与角色管理模块的前后端实现，从数据库表结构分析到前端 Vue 代码编写。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Vue 项目中 details.Vue 文件的样式代码，包含 .logContent:before 的 CSS 样式定义，以及终端显示的编译成功信息和运行地址 http://localhost:8888。
画面 2: 展示了 PPT 的第 21 页，标题为“3.3 表结构分析”，内容是一个数据库表结构图，包含“菜单表”、“页面元素表”、“权限表”、“角色表”、“用户表”、“角色权限关联表”、“角色菜单关联表”等，图中用箭头表示表之间的外键关系，底部文字说明“这里要注意的是，权限表与权限菜单表、页面元素表与API接口表都是一对一的关系”。
画面 3: 展示了 PPT 的第 22 页，标题为“4 用户管理”，子标题“4.1 需求分析”，内容是用户表的 SQL 创建语句。
画面 4: 展示了 PPT 的第 36 页，标题为“5.1 需求分析”和“5.2 后端实现”，内容是实体类的 Java 代码，包含 import 语句和 @Entity、@Table 注解。
画面 5: 展示了 PPT 的第 37 页，内容是 Role 类的完整 Java 代码，包含 @Entity、@Table 注解和 public class Role implements Serializable。
画面 6: 展示了 PPT 的第 38 页，内容是 RoleDao 接口的定义，以及业务逻辑层的 Java 代码，包含 import 语句。
画面 7: 展示了 PPT 的第 39 页，内容是业务逻辑层的 Java 代码，包含 import 语句。
画面 8: 展示了 PPT 的第 39 页，内容是 RoleService 类的 Java 代码，包含 findById、delete、findSearch 方法。
画面 9: 展示了 PPT 的第 40 页，内容是控制器层的 Java 代码，包含 import 语句。
画面 10: 展示了 PPT 的第 40 页，内容是 RoleController 类的 Java 代码，包含 save、update、delete 方法。
画面 11: 展示了 PPT 的第 40 页，内容是 RoleController 类的 Java 代码，包含 findById、findSearch 方法。
画面 12: 展示了 PPT 的第 40 页，内容是 RoleController 类的 Java 代码，包含 findSearch 方法的完整实现，以及标题“5.3 前端实现”，并说明“学员参考资料自行实现”。
画面 13: 展示了文件资源管理器中 project-saas-hrm-Vue-master 项目的 config 文件夹，其中包含 dev.env.js、index.js、prod.env.js、test.env.js 四个文件。
画面 14: 展示了文件资源管理器中 hrm 文件夹，其中包含 day1、day2、day3 三个文件夹。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```css
.logContent:before {
  content: '';
  width: 14px;
  height: 14px;
  display: block;
  border-radius: 50%;
  position: absolute;
  left: 8%;
  top: 20%;
  z-index: 2;
  border: 1px solid #266e9e;
  background: #fff;
}
.logInfo:before {
  content: '';
  position: absolute;
  left: 18%;
  top: 15px;
  width: 2px;
  height: 40px;
  background-color: #266e9e;
}
```
画面 2:
```text
这里要注意的是，权限表与权限菜单表、页面元素表与API接口表都是一对一的关系
```
画面 3:
```sql
CREATE TABLE bs_user (
  'id' varchar(40) NOT NULL COMMENT 'ID',
  'mobile' varchar(40) NOT NULL COMMENT '手机号码',
  'username' varchar(255) NOT NULL COMMENT '用户名称',
  'password' varchar(255) DEFAULT NULL COMMENT '密码',
  'enable_state' int(2) DEFAULT '1' COMMENT '启用状态 0是禁用,1是启用',
  'create_time' datetime DEFAULT NULL COMMENT '创建时间',
  'department_id' varchar(40) DEFAULT NULL COMMENT '部门ID',
  'time_of_entry' datetime DEFAULT NULL COMMENT '入职时间',
  'form_of_employment' int(1) DEFAULT NULL COMMENT '聘用形式',
  'work_number' varchar(20) DEFAULT NULL COMMENT '工号',
  'form_of_management' varchar(8) DEFAULT NULL COMMENT '管理形式',
```
画面 4:
```java
package com.ihrm.domain.system;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;
@Entity
@Table(name = "pe_role")
```
画面 5:
```java
@Entity
@Table(name = "pe_role")
@Getter
@Setter
public class Role implements Serializable {
```
画面 6:
```java
public interface RoleDao extends JpaRepository<Role, String>,
JpaSpecificationExecutor<Role> {
}
```
画面 7:
```java
import com.ihrm.system.dao.RoleDao;
import com.ihrm.system.dao.UserDao;
import com.ihrm.system.domain.Company;
import com.ihrm.system.domain.Role;
import com.ihrm.system.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Predicate;
import javax.persistence.criteria.Root;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
```
画面 8:
```java
public Role findById(String id) {
  return roleDao.findById(id).get();
}

/**
 * 删除角色
 */
public void delete(String id) {
  roleDao.deleteById(id);
}

public Page<Role> findSearch(String companyId, int page, int size) {
```
画面 9:
```java
import com.ihrm.common.entity.PageResult;
import com.ihrm.common.entity.Result;
import com.ihrm.system.domain.Role;
import com.ihrm.system.domain.User;
import com.ihrm.system.Service.RoleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.web.bind.annotation.*;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Predicate;
import javax.persistence.criteria.Root;
import java.util.HashMap;
import java.util.Map;
```
画面 10:
```java
//更新角色
@RequestMapping(value = "/role/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(name = "id") String id, @RequestBody Role role)
throws Exception {
  roleService.update(role);
  return Result.SUCCESS();
}

//删除角色
@RequestMapping(value = "/role/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(name = "id") String id) throws Exception {
  roleService.delete(id);
  return Result.SUCCESS();
}
```
画面 11:
```java
//根据ID获取角色信息
@RequestMapping(value = "/role/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(name = "id") String id) throws Exception {
  Role role = roleService.findById(id);
  return new Result(ResultCode.SUCCESS, role);
}

//分页查询角色
@RequestMapping(value = "/role", method = RequestMethod.GET)
public Result findPage(int page, int pagesize, Role role) throws Exception {
  String companyId = "1";
  Page<Role> searchPage = roleService.findSearch(companyId, page, pagesize);
  PageResult<Role> pr = new PageResult<>(searchPage.getTotalElements(), searchPage.getContent());
  return new Result(ResultCode.SUCCESS, pr);
}
```
画面 12:
```text
5.3 前端实现
学员参考资料自行实现
```
画面 13:
```text
config
├── dev.env.js
├── index.js
├── prod.env.js
└── test.env.js
```
画面 14:
```text
hrm
├── day1
├── day2
└── day3
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 2: 标题“3.3 表结构分析”，图中包含“菜单表”、“页面元素表”、“权限表”、“角色表”、“用户表”、“角色权限关联表”、“角色菜单关联表”等实体，通过外键关系（如 FK_PE_ROLE_ID、FK_PE_MENU_ID 等）相互关联。
画面 3: 标题“4 用户管理”，子标题“4.1 需求

