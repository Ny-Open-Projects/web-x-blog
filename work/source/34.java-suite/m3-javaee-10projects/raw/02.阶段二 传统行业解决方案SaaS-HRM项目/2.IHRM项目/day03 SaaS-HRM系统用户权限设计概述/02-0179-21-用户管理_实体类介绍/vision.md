# 画面线理解：21-用户管理：实体类介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\21-用户管理：实体类介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:17, 00:50, 00:58, 01:14, 01:53, 02:14, 02:28, 03:20, 03:40, 05:10, 05:19, 05:33, 05:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:38:37

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，定义用户、角色、权限等实体类及其关联关系，用于构建 HRM 系统的后端数据模型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 IntelliJ IDEA 中的项目结构，选中模块 `ihrm_common_model`。
- 编辑器中显示 `SystemApplication.java`，其中包含 Spring Boot 启动类的代码。
- 代码内容：
  ```java
  package com.ihrm.system;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.boot.autoconfigure.domain.EntityScan;
  import org.springframework.context.annotation.Bean;
  //1.配置springboot的包扫描
  @SpringBootApplication(scanBasePackages = "com.ihrm")
  //2.设置包扫描的规则
  @EntityScan(values = "com.ihrm.domain.system")
  public class SystemApplication {
      //启动方法
      public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
      @Bean
      public IdWorker idWorker() {
          return new IdWorker();
      }
  }
  ```

画面 2：
- 显示 PPT 页面，标题为“4.3 后端用户基本操作”。
- 该页内容为“（1）实体类”，并列出相关导入语句。
- 代码内容：
  ```java
  import com.fasterxml.jackson.annotation.JsonIgnore;
  import lombok.Getter;
  import lombok.Setter;
  import javax.persistence.*;
  import java.io.Serializable;
  ```

画面 3：
- 显示 IntelliJ IDEA 中的项目结构，选中 `ihrm_common_model` 模块下的 `target` 目录。
- 弹出“Copy specified files”对话框，目标路径为 `ihrm-parent/ihrm-common-model/src/main/java/com/ihrm/domain/system`。

画面 4：
- 显示 `User.java` 文件内容，定义用户实体类。
- 代码内容：
  ```java
  private String mobile;
  //用户名称
  private String username;
  //密码
  private String password;
  //启用状态 0为禁用 1为启用
  private Integer enableState;
  //创建时间
  private Date createTime;
  private String companyId;
  private String companyName;
  //部门ID
  private String departmentId;
  ```

画面 5：
- 继续显示 `User.java` 文件，展示更多字段。
- 代码内容：
  ```java
  //管理形式
  private String formOfManagement;
  //工作城市
  private String workingCity;
  //转正时间
  private Date connectionLine;
  //在职状态 1.在职 2.离职
  private Integer inServiceStatus;
  private String departmentName;
  //JsonIgnore
  @ManyToMany
  @JoinTable(name="pe_user_role",joinColumns={@JoinColumn(name="user_id",referencedColumnName="id")},
  inverseJoinColumns={@JoinColumn(name="role_id",referencedColumnName="id")})
  private Set<Role> roles = new HashSet<>(); //用户与角色 多对多
  ```

画面 6：
- 显示 `Role.java` 文件内容，定义角色实体类。
- 代码内容：
  ```java
  @Entity
  @Table(name = "pe_role")
  @Getter
  @Setter
  public class Role implements Serializable {
      private static final long serialVersionUID = 594829328797158219L;
      @Id
      private String id;
      //角色名
      private String name;
      //说明
      private String description;
      //企业id
      private String companyId;
      @JsonIgnore
      @ManyToMany(mappedBy="roles")
      private Set<User> users = new HashSet<>(); //角色与用户 多对多
  }
  ```

画面 7：
- 继续显示 `User.java` 文件，展示 `roles` 字段的注解。
- 代码内容：
  ```java
  @JsonIgnore
  @ManyToMany
  @JoinTable(name="pe_user_role",joinColumns={@JoinColumn(name="user_id",referencedColumnName="id")},
  inverseJoinColumns={@JoinColumn(name="role_id",referencedColumnName="id")})
  private Set<Role> roles = new HashSet<>(); //用户与角色 多对多
  ```

画面 8：
- 显示 `Role.java` 文件，展示 `users` 字段的注解。
- 代码内容：
  ```java
  @JsonIgnore
  @ManyToMany(mappedBy="roles")
  private Set<User> users = new HashSet<>(); //角色与用户 多对多
  ```

画面 9：
- 继续显示 `Role.java` 文件，展示 `permissions` 字段的注解。
- 代码内容：
  ```java
  @JsonIgnore
  @ManyToMany
  @JoinTable(name="pe_role_permission",
  joinColumns={@JoinColumn(name="role_id",referencedColumnName="id")},
  inverseJoinColumns={@JoinColumn(name="permission_id",referencedColumnName="id")})
  private Set<Permission> permissions = new HashSet<>(); //角色与权限 多对多
  ```

画面 10：
- 显示 `Permission.java` 文件内容，定义权限实体类。
- 代码内容：
  ```java
  @DynamicUpdate(true)
  public class Permission implements Serializable {
      private static final long serialVersionUID = -499810027542971546L;
      @Id
      private String id;
      //权限名称
      private String name;
      //权限类型 1为菜单 2为功能（API）
      private Integer type;
      //权限编码
      private String code;
      //权限描述
      private String description;
      //一个权限
      //菜单 -- 多个按钮
      //按钮 -- api权限
      //接口 -- api权限
      private String pid;
  }
  ```

画面 11：
- 继续显示 `Permission.java` 文件，展示 `description` 字段。
- 代码内容：
  ```java
  //权限描述
  private String description;
  //一个权限
  //菜单 -- 多个按钮
  //按钮 -- api权限
  //接口 -- api权限
  private String pid;
  ```

画面 12：
- 显示 IntelliJ IDEA 中的项目结构，选中 `PermissionPoint.java`。
- 代码内容：
  ```java
  @Entity
  @Table(name = "pe_permission_point")
  @Getter
  @Setter
  public class PermissionPoint implements Serializable {
      private static final long serialVersionUID = 1802411498113957845L;
      @Id
      private String id;
      //权限代码
      private String pointClass;
      private String pointIcon;
      private String pointStatus;
  }
  ```

画面 13：
- 显示 `PermissionApi.java` 文件内容，定义权限接口实体类。
- 代码内容：
  ```java
  @Entity
  @Table(name = "pe_permission_api")
  @Getter
  @Setter
  public class PermissionApi implements Serializable {
      private static final long serialVersionUID = -1803315043290784820L;
      @Id
      private String id;
      //权限
      private String apiUrl;
      //请求类型
      private String apiMethod;
      //权限等级，1为通用接口权限，2为具体接口权限
      private String apiLevel;
  }
  ```

画面 14：
- 继续显示 `Permission.java` 文件，展示构造函数。
- 代码内容：
  ```java
  public Permission(String name, Integer type, String code, String description) {
      this.name = name;
      this.type = type;
      this.code = code;
      this.description = description;
  }
  ```
