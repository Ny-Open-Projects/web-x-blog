# 画面线理解：06.商户资质申请-系统交互流程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\06.商户资质申请-系统交互流程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:42, 00:48, 00:54, 01:31, 02:05, 05:00, 05:12, 05:46, 05:52, 06:39, 06:48, 07:11, 07:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:04:42

1) 这一组画面整体在讲商户资质申请的系统交互流程与数据库表结构设计。

2) 按时间顺序列出每张画面的要点：
画面1：展示“3.1.1 系统交互流程”PPT，图示商户资质申请流程，涉及“浏览器/APP”、“商户平台应用”、“商户服务”、“七牛云”四个组件，流程步骤包括上传证件信息、请求七牛云保存图片、保存图片、返回图片标识、提交商户资质申请、请求保存资质信息、保存成功、保存资质申请信息、资质申请成功。
画面2：PPT内容与画面1相同，鼠标在“商户平台应用”节点上。
画面3：切换到另一个系统交互流程图，涉及“浏览器/APP”、“商户平台应用”、“商户服务”、“Seas平台”、“证明服务”五个组件，流程步骤包括插入手机号码验证、获取验证码、新建商户、绑定商户、更新商户信息、注册成功。
画面4：回到“3.1.1 系统交互流程”PPT，鼠标在“商户服务”节点上。
画面5：PPT内容与画面1相同，鼠标在“商户平台应用”节点上。
画面6：PPT内容与画面1相同，鼠标在“商户平台应用”节点上。
画面7：切换到数据库管理界面，显示“merchant”表的数据，包含ID、MERCHANT_NAME、MERCHANT_ID、MERCHANT_ADDRESS、MERCHANT_TYPE、BUSINESS_LICENSES_IMG、ID_CARD_FRONT_IMG、ID_CARD_AFTER_IMG、USERNAME、MOBILE、CONTACTS_ADDRESS等字段。
画面8：在数据库管理界面，显示“merchant”表的DDL创建语句：
CREATE TABLE merchant (
ID bigint(20) NOT NULL COMMENT '主键',
MERCHANT_NAME varchar(50) DEFAULT NULL COMMENT '商户名称',
MERCHANT_ID bigint(20) DEFAULT NULL COMMENT '企业编号',
MERCHANT_ADDRESS varchar(255) DEFAULT NULL COMMENT '企业地址',
MERCHANT_TYPE varchar(50) DEFAULT NULL COMMENT '商户类型',
BUSINESS_LICENSES_IMG varchar(100) DEFAULT NULL COMMENT '营业执照（企业证明）',
ID_CARD_FRONT_IMG varchar(100) DEFAULT NULL COMMENT '法人身份证正面照片',
ID_CARD_AFTER_IMG varchar(100) DEFAULT NULL COMMENT '法人身份证反面照片',
USERNAME varchar(50) DEFAULT NULL COMMENT '联系人姓名',
MOBILE varchar(50) DEFAULT NULL COMMENT '联系人手机号（关联一张号）',
CONTACTS_ADDRESS varchar(255) DEFAULT NULL COMMENT '联系人地址'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
画面9：PPT内容与画面1相同，鼠标在“商户平台应用”节点上。
画面10：PPT内容与画面1相同，鼠标在“商户平台应用”节点上。
画面11：PPT内容与画面1相同，鼠标在“浏览器/APP”节点上。
画面12：切换到“3.1.2 资质信息存储”PPT，展示“商户表”的字段结构，包括ID、MERCHANT_NAME、MERCHANT_ID、MERCHANT_ADDRESS、MERCHANT_TYPE、BUSINESS_LICENSES_IMG、ID_CARD_FRONT_IMG、ID_CARD_AFTER_IMG、USERNAME、MOBILE、CONTACTS_ADDRESS等字段及其类型和注释。
画面13：PPT内容与画面12相同，鼠标在“商户表”字段“MOBILE”上。
画面14：PPT内容与画面12相同，鼠标在“商户表”字段“MOBILE”上。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面8的SQL语句：
CREATE TABLE merchant (
ID bigint(20) NOT NULL COMMENT '主键',
MERCHANT_NAME varchar(50) DEFAULT NULL COMMENT '商户名称',
MERCHANT_ID bigint(20) DEFAULT NULL COMMENT '企业编号',
MERCHANT_ADDRESS varchar(255) DEFAULT NULL COMMENT '企业地址',
MERCHANT_TYPE varchar(50) DEFAULT NULL COMMENT '商户类型',
BUSINESS_LICENSES_IMG varchar(100) DEFAULT NULL COMMENT '营业执照（企业证明）',
ID_CARD_FRONT_IMG varchar(100) DEFAULT NULL COMMENT '法人身份证正面照片',
ID_CARD_AFTER_IMG varchar(100) DEFAULT NULL COMMENT '法人身份证反面照片',
USERNAME varchar(50) DEFAULT NULL COMMENT '联系人姓名',
MOBILE varchar(50) DEFAULT NULL COMMENT '联系人手机号（关联一张号）',
CONTACTS_ADDRESS varchar(255) DEFAULT NULL COMMENT '联系人地址'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1标题：“3.1.1 系统交互流程”。
流程图结构：从左到右依次为“浏览器/APP” → “商户平台应用” → “商户服务” → “七牛云”。
步骤1：浏览器/APP → 商户平台应用：上传证件信息（接口①）。
步骤2：商户平台应用 → 七牛云：请求七牛云保存图片。
步骤3：七牛云 → 商户平台应用：保存图片。
步骤4：七牛云 → 商户平台应用：返回图片标识。
步骤5：商户平台应用 → 浏览器/APP：返回证件标识。
步骤6：浏览器/APP → 商户平台应用：提交商户资质申请（接口③）。
步骤7：商户平台应用 → 商户服务：请求保存资质信息（接口②）。
步骤8：商户服务 → 商户平台应用：保存资质申请信息。
步骤9：商户服务 → 商户平台应用：保存成功。
步骤10：商户平台应用 → 浏览器/APP：资质申请成功。
画面12标题：“3.1.2 资质信息存储”。
表格数据：
| Field | Type | Comment |
|-------|------|---------|
| ID | bigint(20) | 主键 |
| MERCHANT_NAME | varchar(50) | 商户名称 |
| MERCHANT_ID | bigint(20) | 企业编号 |
| MERCHANT_ADDRESS | varchar(255) | 企业地址 |
| MERCHANT_TYPE | varchar(50) | 商户类型 |
| BUSINESS_LICENSES_IMG | varchar(100) | 营业执照（企业证明） |
| ID_CARD_FRONT_IMG | varchar(100) | 法人身份证正面照片 |
| ID_CARD_AFTER_IMG | varchar(100) | 法人身份证反面照片 |
| USERNAME | varchar(50) | 联系人姓名 |
| MOBILE | varchar(50) | 联系人手机号（关联一张号） |
| CONTACTS_ADDRESS | varchar(255) | 联系人地址 |

5) 无。
