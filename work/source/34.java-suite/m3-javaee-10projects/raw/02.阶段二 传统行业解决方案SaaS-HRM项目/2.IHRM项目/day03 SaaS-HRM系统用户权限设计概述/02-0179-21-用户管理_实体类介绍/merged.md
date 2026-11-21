# 21-用户管理：实体类介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\21-用户管理：实体类介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 6分7秒（音频 368s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] OK系统为服务呢我们已经搭建好了那搭建好了之后呢咱们就可以编写点代码完成用户的基本增伤改善操作那还是跟之前的套路是一模一样的首先呢我们构造相应的实体类那这个实体类呢由于它自断设计的会比较多我其实在今天资料当中已经把我们后续全线管理用到的实体类都给各位准备好了在资源有一个工具代码
[00:35] 有一个实体类在这个实体类里面我已经把基本的全线管理里面的代码都给他搞定了Ctrl C把它copy到我们的公共的实体类模块当中OK 靠过来那靠过来之后呢我们可以简单的一起来看一下用户用户里面有ID手机号名字密码等等等等很多那我们都知道用户和角色是一个多对多关系所以我底下配置了一个用户到角色的多又多
[01:08] 多对多我们用的注解呢叫做many to manyok 还有一个join table一个join tableok 好了接下来呢这边有一个注解呢需要跟各位要简单的提一下就是一个json配置我们json转型的一个忽略转化因为对于因为对于我们进行一个微服搭建来说呢返回的全部都是json走串那他就可能会把用户
[01:43] 所有的内容转化成Jason那转化成Jason的过程当中如果说你这边不忽略Jason转化的话他会对set里面的角色也要进行一个转化那角色进行转化的时候这边也有多对多的一个配置这边也有到用户多对多的一个配置那这回他就会造成一个死循环所以对于我们来说如果你不忽略的话那他对那他对进行Jason转化的过程当中会对肉肉丝里面所有内容转然后呢肉丝又对U的转U的又对肉丝转
[02:13] 那它是不是就造成了一个死循环啊所以对于我们来说把它忽略掉那这边呢many to manydrawing table对应的是一个中间表那用户我们简单的看了一下那除了用户之外还有一个实体类就是角色那对于角色而言对应的是角色表好了get set方法里面有ID有角色名称有角色说明还有企业名称我们都知道角色划分为某一个企业的角色
[02:41] 不同的企业里面可能有不同的角色比如说你A企业叫人事经理那B企业叫人事总监它是不一样的所以是在不同的企业下那这边呢也有一个忽略好了还有一个many to many当然了这边many to many配置了my4to5也就是不维护中间表那交给我们的用户端去维护那好了接下来那我们还有根据RBAC模型我们得知用户
[03:13] 和全角色和权限之间也是多得多用户和权限之间也是多得多那这边呢也有一个用户和权限的一个配置这边有一个权限实体类permissionpermission那用户跟权限之间呢也是多得多那我们来看一下角色到权限那是一个权限集合那这边配置了中间表配置了中间表那我们来看一下权限权限的内容呢其实比较简单ID
[03:42] 全线名称全线类型注意全线类型一菜单二功能三一篇好了还有一个全线标志全线标志还有全线的一个描述当然了对于全线来说它有一个副ID的一个概念这个副ID我需要也跟各位简单的啰嗦两句那其实是这样的比如说呢一个全线它可能是一个菜单那在这个菜单的底下是不是可能有多个我们叫做按钮
[04:12] 那可能这个菜单下也没有按钮所以我们知道菜单和这个按钮之间可能也是一个从属机关系那菜单的这个按钮呢可能属于某一个菜单所以按钮和菜单之间可能也有一个父子关系嘛那当然了除了这些之外呢可能还有菜单或者按钮对应APIAPI权限API权限那你某一个菜单或者某一个按钮这边就是按钮
[04:45] 那某一个菜单或者某一个按钮里面又有可能要访问的API所以我们都知道一个权限下和这个API下可能它就从属于某一个按钮权限所以我们知道对于权限之间它其实也是一个父子的这么一个关系所以我加了一个PID那代表你究竟是属于哪一个菜单下的按钮究竟属于哪一个菜单或者哪一个按钮的API
[05:10] OK好了这个权限我们也看过了之后接下来呢还有这么三个实体类一个叫API一个叫menu一个叫pont那我们简单的打开来看一下menu比较好理解它代表的是菜单代表的是菜单那好了接下来呢还有一个叫做pont那这个pont代表的是我们叫做按钮那还有一个API这个其实代表的就是我们的API权限API资源API资源好了这边代表的是我们的菜单资源
[05:43] 那Pont代表的就是我们的按钮资源那对于这个按钮来说呢我们习惯叫做检查点或者全线点当然了这边其实可以把它理解成按钮就可以了那这边需要跟各位做一个简单的说明做一个简单的说明就是在全线这边全线API全线菜单和全线和我们的按钮它们之间都是一对一OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  //1.配置Spring Boot的包扫描
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

