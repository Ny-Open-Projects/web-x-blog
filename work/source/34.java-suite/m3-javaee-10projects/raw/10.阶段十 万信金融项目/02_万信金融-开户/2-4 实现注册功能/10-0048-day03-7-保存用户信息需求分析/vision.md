# 画面线理解：day03-7-保存用户信息需求分析

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-7-保存用户信息需求分析_【海量资源尽在 666java.com】.mp4
- 抽帧：11 帧 @ 01:11, 01:40, 01:50, 01:57, 01:59, 02:02, 02:04, 02:13, 04:24, 04:26, 04:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:31:55

1) 这一组画面整体在讲什么（一句话）：
讲解用户注册功能中，Consumer微服务与Account微服务分别存储用户信息和账户信息的数据库设计与分离架构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容“4.6 注册3：保存账号信息”，说明Consumer微服务保存用户信息到p2p_consumer数据库的consumer表，Account微服务保存账户信息到p2p_account数据库的account表，采用用户-账号分离设计。
画面2：显示SQLyog工具界面，连接到p2p_uaa数据库，准备进行数据库操作。
画面3：在SQLyog中查看p2p_account数据库的account表结构，包含字段：ID, USERNAME, MOBILE, PASSWORD, SALTS, STATUS, IDENTITY。
画面4：在SQLyog中切换到p2p_consumer数据库。
画面5：在SQLyog中查看p2p_consumer数据库的空表结构。
画面6：在SQLyog中查看p2p_consumer数据库的consumer表结构，包含字段：ID, USERNAME, FULLNAME, ID_NUMBER, USER_ID, USER_TYPE, ROLE, ACCOUNT_LIST, LOAN_AMOUNT。
画面7：在SQLyog中查看p2p_consumer数据库的consumer表结构，鼠标悬停在ROLE字段上，显示注释“用户角色, 个人cc企业, 贷款人”。
画面8：再次展示PPT内容“4.6 注册3：保存账号信息”，强调用户-账号分离设计的好处。
画面9：在Windows资源管理器中显示“wanntop2p/day02/资料”文件夹，其中包含“开户流程图.jpg”、“注册登录流程图.jpg”等文件。
画面10：在Windows资源管理器中选中“注册登录流程图.jpg”文件。
画面11：屏幕变灰，无内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT标题：
- 4.6 注册3：保存账号信息
- 前端页面发起的请求会先访问Consumer微服务，然后远程调用Account微服务，从而分别实现各自的信息保存。

表格数据：
- 画面3中account表字段：
  - Field: ID, Type: bigint(20) NOT NULL, Comment: 主键
  - Field: USERNAME, Type: varchar(50) NULL, Comment: 用户名
  - Field: MOBILE, Type: varchar(50) NULL, Comment: 手机号
  - Field: PASSWORD, Type: varchar(50) NULL, Comment: 密码
  - Field: SALTS, Type: varchar(4) NULL, Comment: 盐值
  - Field: STATUS, Type: varchar(8) NOT NULL, Comment: 状态
- 画面6中consumer表字段：
  - Field: ID, Type: bigint(20) NOT NULL, Comment: 主键
  - Field: USERNAME, Type: varchar(50) NOT NULL, Comment: 用户名
  - Field: FULLNAME, Type: varchar(50) NULL, Comment: 姓名
  - Field: ID_NUMBER, Type: varchar(50) NULL, Comment: 身份证号
  - Field: USER_ID, Type: varchar(50) NULL, Comment: 用户编号
  - Field: USER_TYPE, Type: varchar(50) NULL, Comment: 用户类型, 个人cc企业, 贷款人
  - Field: ROLE, Type: varchar(50) NULL, Comment: 用户角色, 个人cc企业, 贷款人
  - Field: ACCOUNT_LIST, Type: varchar(50) NULL, Comment: 账户列表
  - Field: LOAN_AMOUNT, Type: decimal(10,0) NULL, Comment: 贷款金额

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
