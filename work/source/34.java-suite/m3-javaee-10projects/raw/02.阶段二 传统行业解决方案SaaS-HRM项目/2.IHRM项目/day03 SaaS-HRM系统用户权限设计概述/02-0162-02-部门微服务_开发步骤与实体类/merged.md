# 02-部门微服务：开发步骤与实体类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\02-部门微服务：开发步骤与实体类_【海量资源尽在 ubkz.com】.mp4
- 时长 3分6秒（音频 186s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了这个基本的需求和表呢我们都已经搞定了那接下来呢就是我们在微服务这端去实现它那我先过滤掉一截啊就是这个抽取公共代码咱们一会儿再说咱们先看一下不抽取它有什么问题那最后呢我们再引申出如何进行一个抽取的这么一个工作那咱们来看一下就是如何去实现基本CIOD其实比较简单咱们Java开发遵守的是这么三层约定那首先呢我们得有实体类
[00:31] 实体类之后呢三层,第五层,四位层,还有我们的Controller层那接下来呢咱们一个一个来看首先创建实体类那创建实体类呢其实比较简单了数据库表有了咱们就可以结合数据库表把实体类给它构造出来那在这边呢为了不浪费各位的时间在今天第三天的资源当中有一个工具代码其中呢把今天要用的实体类都给各位准备好了
[01:00] 那我现在要用的就是一个department,control C把它拿到,打开我的idea,找到我们放所有模型的这个公共的模块当中,OK,那我们这个部门管理呢,其实也是放到企业当中的一部分,也算企业管理这个微服务的一部分,所以我实体内就放到企业微服务的这个包下,OK,control V扔过来,好了。
[01:31] 那这个实体类我们已经构建成功了那实体类构建成功了那接下来第二件事我们就可以结合着API咱们先把Controller去写好那写Controller的过程当中可能会用到了Service可能会用到do那咱们一个一个的进行补充就可以了那这边我们说过要结合一下API
[01:54] 那API呢在之前的代码已经给各位准备了当然了这个API呢我今天还会再给各位下发一次因为今天内容会比较多那我们现在关注的是一个组织架构的这么一个管理打开咱们来看一下其中呢有新增那新增这些字段呢ID等等等等这些字段其实跟我实体类里面的这些字段基本上都是保持一致的那除了新增之外呢还有查询列表那各位来看
[02:25] 查询列表都比较好理解得到一个数据列表但是得到数据列表我们看它的返回那返回有codesuccessmessage还有data等等这个数据结构好像就有点复杂了OK那好了接下来还有比如说根据ID我们查询这个比较好理解根据ID查询那其中还有修改以及删除其实还是跟我们之前代码那一套差不多就是完成一个基本的增删改查的这么一套逻辑
[02:56] OK API我们看过了咱们大致的知道了要做什么那么我们接下来就可以去一点一点的编写我们的代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 SAAS-HRM 系统中部门（Department）实体的 Java 类设计、项目结构、以及对应的 RESTful API 文档（Swagger）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前选中“1.2.2 去除公共代码”章节，表明即将讲解如何将公共代码从模块中移除。
画面 2: 在 IntelliJ IDEA 中，将 `Department.java` 文件从 `ihrm_common_model` 模块复制到 `ihrm_parent` 模块的 `src/main/java/com/ihrm/domain/company` 目录下，准备进行代码调整。
画面 3: 显示 `Department.java` 类的源码，包含 `@Entity`、`@Table`、`@AllArgsConstructor`、`@NoArgsConstructor` 注解，以及 `id`、`pid`、`companyId`、`name`、`code`、`managerId`、`manager`、`introduce`、`createTime` 等字段。
画面 4: 在项目结构中选中 `ihrm_common_model` 模块，准备进行后续操作。
画面 5: 打开 SAAS-HRM 系统的 API 文档页面，页面为空白，等待加载或用户操作。
画面 6: API 文档页面加载完成，显示部门模块的 API 列表，包括 POST（添加）、GET（全部列表）、GET（根据ID查询）、PUT（修改）和 DELETE（删除）操作。
画面 7: 在 IDEA 中查看 `Department.java` 类的源码，聚焦于 `manager` 和 `introduce` 字段的注释。
画面 8: API 文档页面显示“API-Department 1.0.0”，并列出部门模块的 API 操作。
画面 9: API 文档页面显示“GET /department”操作，用于获取部门列表。
画面 10: API 文档页面显示“GET /department/{departmentId}”操作，用于根据 ID 查询部门。
画面 11: API 文档页面显示“PUT /department/{departmentId}”操作，用于修改部门信息。
画面 12: API 文档页面显示“DELETE /department/{departmentId}”操作，用于删除部门。
画面 13: API 文档页面显示“POST /department”操作，用于添加部门。
画面 14: API 文档页面显示“GET /department/{departmentId}”操作，用于根据 ID 查询部门。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
@Entity
@Table(name = "Lo_department")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Department implements Serializable {
    private static final long serialVersionUID = -908433249532844895531L;
    @Id
    private String id;
    //父级ID
    private String pid;
    //企业ID
    private String companyId;
    //部门名称
    private String name;
    //部门编码，同级部门不可重复
    private String code;
    //负责人ID
    private String managerId;
    //负责人名称
    private String manager;
    //介绍
    private String introduce;
    //创建时间
    private Date createTime;
}
```

画面 2:
```
Copy file C:\Users\ThinkPad\Desktop\ihrm\day3\部门\部门实体类\Department.java
New name: Department.java
To directory: 'm_parent\ihrm_common_model\src\main\java\com\ihrm\domain\company'
Use Alt+Shift for path completion
```

画面 6:
```
POST /department 添加Department
GET /department Department全部列表
GET /department/{departmentId} 根据ID查询department
PUT /department/{departmentId} 修改Department
DELETE /department/{departmentId} 根据ID删除Department
```

画面 13:
```
POST /department 添加Department
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

