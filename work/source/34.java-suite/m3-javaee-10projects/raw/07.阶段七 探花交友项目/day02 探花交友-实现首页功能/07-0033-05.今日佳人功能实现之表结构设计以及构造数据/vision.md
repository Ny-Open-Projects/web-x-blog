# 画面线理解：05.今日佳人功能实现之表结构设计以及构造数据

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\05.今日佳人功能实现之表结构设计以及构造数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 03:52, 04:33, 05:31, 07:11, 08:20, 09:01, 09:26, 10:01, 10:27, 10:43, 11:09, 11:24, 11:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:20:08

1) 这一组画面整体在讲什么（一句话）：
演示如何设计 MongoDB 和 MySQL 数据库表结构，并通过 Java 代码生成测试数据插入数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 Typora 中的课程大纲，当前章节为“2.2、表结构设计”，并显示了 MongoDB 的“Users”集合结构和 Java 代码示例。
画面 2：展示 Typora 中的 Java 代码，用于在 MongoDB 的 recommend_user 集合中插入测试数据。
画面 3：展示 Typora 中的 Java 代码，继续插入 MongoDB 的 recommend_user 集合数据。
画面 4：展示 Robo 3T 数据库客户端，选中了“recommend_user”集合，准备执行操作。
画面 5：展示 Robo 3T 中执行了 find() 操作，显示了 recommend_user 集合中的文档列表。
画面 6：展示 Typora 中的 Java 代码，用于生成并打印插入 MySQL tb_user 和 tb_user_info 表的 SQL 语句。
画面 7：展示 EditPlus 编辑器中的 SQL 插入语句文件，内容为插入 tb_user 和 tb_user_info 表的数据。
画面 8：展示 Navicat Premium 中 MySQL 的 tb_user_info 表结构，包含字段定义和注释。
画面 9：展示 Navicat Premium 中 MySQL 的 tb_user 和 tb_user_info 表的记录数。
画面 10：展示 Navicat Premium 中 MySQL 的空白查询界面。
画面 11：展示 Navicat Premium 中 MySQL 的 tb_user_info 表结构，与画面 8 相同。
画面 12：展示 Typora 中的 Java 代码，用于生成插入 MySQL tb_user 和 tb_user_info 表的 SQL 语句。
画面 13：展示 Typora 中的 Java 代码，用于生成插入 MongoDB recommend_user 集合的测试数据。
画面 14：展示 Typora 中的“2.2、表结构设计”章节，显示了 MongoDB 的 Users 集合结构和 Java 代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```json
{
"userId":1001,  #推荐的用户id
"touserId":1002,  #用户id
"score":90,  #推荐得分
"date":"2019/1/1"  #日期
}
```
```java
//生成数据代码
@Test
public void testMongoDBData() {
    for (int i = 2; i < 100; i++) {
        int score = RandomUtils.nextInt(10, 99);
        System.out.println("db.recommend_user.insert({\"userId\": " + i + ", \"touserId\":1, \"score\": " + score + ", \"date\":\"2019/1/1\"})");
    }
}
```
画面 2：
```java
//生成数据代码
@Test
public void testMongoDBData() {
    for (int i = 2; i < 100; i++) {
        int score = RandomUtils.nextInt(10, 99);
        System.out.println("db.recommend_user.insert({\"userId\": " + i + ", \"touserId\":1, \"score\": " + score + ", \"date\":\"2019/1/1\"})");
    }
}
```
画面 3：
```java
//生成数据代码
@Test
public void testMongoDBData() {
    for (int i = 2; i < 100; i++) {
        int score = RandomUtils.nextInt(10, 99);
        System.out.println("db.recommend_user.insert({\"userId\": " + i + ", \"touserId\":1, \"score\": " + score + ", \"date\":\"2019/1/1\"})");
    }
}
```
画面 4：
```
db.getCollection('recommend_user').find({})
```
画面 5：
```
db.recommend_user.find({})
```
画面 6：
```java
System.out.println("INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('1', '13800000000', 'e10adc3949ba59abbe56e057f204c373', '2019-08-02 16:43:46', '2019-08-02 16:43:46');");
for (int i = 3; i < 100; i++) {
    String mobile = "13" + RandomStringUtils.randomNumeric(9);
    System.out.println("INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('" + i + "', '" + mobile + "', 'e10adc3949ba59abbe56e057f204c373', '2019-08-02 16:43:46', '2019-08-02 16:43:46');");
}
System.out.println("INSERT INTO tb_user_info (id, user_id, nick_name, logo, tags, sex, age, edu, city, birthday, cover_pic, industry, income, marriage, created, updated) VALUES ('1', '1', 'heima', 'https://itcast-tanhuu.oss-cn-shanghai.aliyuncs.com/images/logo/21.jpg', '身高,本科,年龄相仿', '1', '30', '本科', '北京市-北京城区-东城区', '2019-08-01', 'https://itcast-tanhuu.oss-cn-shanghai.aliyuncs.com/images/logo/21.jpg', '计算机行业', '30', '已婚', '2019-08-02 16:44:23', '2019-08-02 16:44:23');");
for (int i = 3; i < 100; i++) {
    String logo = "https://itcast-tanhuu.oss-cn-shanghai.aliyuncs.com/images/logo/" + RandomUtils.nextInt(1, 20) + ".jpg";
    System.out.println("INSERT INTO tb_user_info (id, user_id, nick_name, logo, tags, sex, age, edu, city, birthday, cover_pic, industry, income, marriage, created, updated) VALUES ('" + i + "', '" + i + "', 'heima', '" + logo + "', '身高,本科,年龄相仿', '1', '30', '本科', '北京市-北京城区-东城区', '2019-08-01', '" + logo + "', '计算机行业', '30', '已婚', '2019-08-02 16:44:23', '2019-08-02 16:44:23');");
}
```
画面 7：
```
INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('1', '13800000000', 'e10adc3949ba59abbe56e057f204c373', '2019-08-02 16:43:46', '2019-08-02 16:43:46');
INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('2', '13800074175', 'e10adc3949ba59abbe56e057f204c373', '2019-08-02 16:43:46', '2019-08-02 16:43:46');
INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('3', '13800000000', 'e10adc3949ba59abbe56e057f204c373', '2019-08-02 16:43:46', '2019-08-02 16:43:46');
INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('4', '13800000000', 'e10adc3949ba59abbe56e057f204c373', '2019-08-02 16:43:46', '2019-08-02 16:43:46');
INSERT INTO tb_user (id, mobile, password, created, updated) VALUES ('5
