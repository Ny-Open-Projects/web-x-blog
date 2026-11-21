# 画面线理解：09-数据库设计：pd工程创建数据库表-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\09-数据库设计：pd工程创建数据库表-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:40, 01:09, 01:13, 02:06, 02:42, 03:15, 03:17, 03:21, 03:30, 03:47, 03:53, 04:13, 04:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:12:02

1) 这一组画面整体在讲如何使用 PowerDesigner 工具进行数据库建模，包括创建表、设置主键和外键关系，并最终生成对应的 SQL 脚本。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 在 PowerDesigner 中创建了两个表：企业表（co_company）和部门表（co_department）。
- 企业表字段：企业ID (varchar[40] <pk>)、企业名称 (varchar[40])、创建时间 (datetime)、状态 (int)。
- 部门表字段：部门ID (varchar[40] <pk>)、部门名称 (varchar[40])、所属企业id (varchar[40])。

画面 2:
- 打开“Table Properties - 部门表 (co_department)”对话框。
- 在“Columns”选项卡中，显示了部门表的字段：部门ID (varchar[40])、部门名称 (varchar[40])、所属企业id (varchar[40])。

画面 3:
- 在“Table Properties - 部门表 (co_department)”对话框中，选中“所属企业id”字段，准备设置其属性。

画面 4:
- 画面回到主建模界面，显示了企业表和部门表，尚未建立关系。

画面 5:
- 打开“Reference Properties - Reference_1”对话框。
- 在“Parent Table”选项卡中，选中“企业表”作为父表。
- 在“Child Table”选项卡中，选中“部门表”作为子表。
- 设置了外键关系：父表的“企业ID”字段指向子表的“所属企业id”字段。

画面 6:
- 在主建模界面中，显示了企业表和部门表之间的外键关系“FK_Reference_1”。
- 关系线从企业表的“企业ID”指向部门表的“所属企业id”。

画面 7:
- 打开“Database Generation - hrmm (hrmm)”对话框。
- 设置数据库类型为“MySQL 5.0”。
- 选择“Generate script”选项，准备生成 SQL 脚本。

画面 8:
- 在“Database Generation - hrmm (hrmm)”对话框中，显示了生成的 SQL 脚本。
- 脚本内容：
  ```sql
  drop table if exists co_company;
  create table co_company
  (
    id varchar(40) not null comment '企业ID',
    name varchar(40) comment '企业名称',
    create_time datetime comment '创建时间',
    status int comment '状态：0 不可用；1 可用',
    primary key (id)
  );
  ```

画面 9:
- 在“Database Generation - hrmm (hrmm)”对话框中，显示了生成的 SQL 脚本。
- 脚本内容：
  ```sql
  create_time datetime comment '创建时间',
  status int comment '状态：0 不可用；1 可用',
  primary key (id)
  );
  /* Table co_department */
  create table co_department
  (
    id varchar(40) not null comment '部门ID',
    name varchar(40) comment '部门名称',
    company_id varchar(40) comment '所属企业id',
    primary key (id)
  );
  ```

画面 10:
- 在“Database Generation - hrmm (hrmm)”对话框中，显示了生成的 SQL 脚本。
- 出现了一个确认对话框，提示“文件 C:\Program Files (x86)\Sybase\PowerDesigner 15\prebase.sql 已经存在。您想覆盖它吗？”
- 对话框选项：是(Y)、否(N)、取消。

画面 11:
- 显示了“黑马程序员”课程的 PPT 页面。
- 页面标题：“2.2.1 建模工具”。
- 内容：介绍了 PowerDesigner 是一个著名的建模工具，其易用性、功能、对流行技术框架的支持以及模型库的管理理念广受设计师喜欢。
- 提到其优势在于：不用使用 create table 等语句创建表结构，数据库设计人员只需关注如何进行数据库建模即可，将来数据库语句可以自动生成。

画面 12:
- 显示了“黑马程序员”课程的 PPT 页面。
- 页面标题：“2.1 数据库设计的三范式”。
- 内容：
  1. 第一范式（1NF）：确保每一列的原子性（做到每列不可拆分）。
  2. 第二范式（2NF）：在第一范式的基础上，非主字段必须依赖于主字段（一个表只做一件事）。
  3. 第三范式（3NF）：在第二范式的基础上，消除传递依赖。
  反三范式：基于第三范式调整的，没有冗余的数据库未必是最好的数据库，有时为了提高运行效率，就必须降低范式标准，适当保留冗余数据。

画面 13:
- 显示了“黑马程序员”课程的 PPT 页面。
- 页面标题：“2.2 数据库建模”。
- 内容：介绍了数据库建模的概念，包括确定最基本的数据结构和对约束建模。

画面 14:
- 画面回到 PowerDesigner 主建模界面，显示了企业表和部门表之间的外键关系“FK_Reference_1”。
- 画面与画面 6 内容相同，用于确认关系设置完成。
