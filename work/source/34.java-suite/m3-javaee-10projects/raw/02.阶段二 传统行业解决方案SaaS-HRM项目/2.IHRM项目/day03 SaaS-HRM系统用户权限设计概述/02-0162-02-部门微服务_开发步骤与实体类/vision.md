# 画面线理解：02-部门微服务：开发步骤与实体类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\02-部门微服务：开发步骤与实体类_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:27, 01:30, 01:36, 01:56, 02:08, 02:18, 02:22, 02:29, 02:45, 02:48, 02:52, 02:55, 03:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:27:22

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
