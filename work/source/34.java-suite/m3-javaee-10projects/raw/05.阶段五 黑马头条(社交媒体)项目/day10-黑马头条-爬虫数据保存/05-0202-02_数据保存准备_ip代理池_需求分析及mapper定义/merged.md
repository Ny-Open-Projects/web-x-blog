# 02_数据保存准备_ip代理池_需求分析及mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\02_数据保存准备_ip代理池_需求分析及mapper定义【海量资源尽在 666java.com】.mp4
- 时长 4分30秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面的咱们就继续的这个数据保存的准备啊这个Service这块那个Map文件咱们还是要去写啊那这里边其实还有很多看到了吗有什么IP的那爬虫的是吧爬虫文章图文还有一个是评论还有一个文章啊首先呢咱们还是要去说一下这个IP代理池那IP代理池呢这块呢有个需求其实这个需求来说呢相对来说比较简单啊咱们只会干嘛呢针对于当前的IP代理池呢
[00:30] 做一个增长检查但这里边还有一个就是你可以设置当前IP可用或者不可用咱们要查询可用的并且呢如果说这个当前IP不能用的话咱们要设置为不可用有这个啊呃之前咱们讲爬虫系统的时候就说了啊这个呢咱们访问的时候尽量的使用这种代理的方式去访问那这个代理的IP在哪啊就是在咱们的表中去管理的
[00:54] 咱们每次都过去从表中去查看看到底哪个IP能用的话咱们就让他用当前的IP去发送请求好这个就是需求当然你也可以去查看一下当前这个表这个表其实就是叫CLIPPRO这里边是有一些字段咱们可以简单看一下目前咱们这个结合咱们这个Service从那块只涉及到这一张表
[01:21] 第一个是ID不用说了还有供应商目前的话咱们只有一个供应商其实你不用太多关注还有IP地址怎么样去设端口号是啥怎么样去设但是用户面面板咱们有的时候需要预设有的时候不需要OK咱们后续用的时候可以再说还有一个状态码是吧还有访问耗时多长时间错误信息如果说你这条信息不能用了咱们会有一个错误的信息提示还有是否启用当然它不能用的话咱们肯定是首先是把它给设置为first
[01:51] 是first不能用还有可用范围还有创建时间好吧行其实这几个字也比较好理解咱们就不再去说了它对应的当前的实体类就是当前的叫什么CLIP好去找到它就这个类这个类其实已经在这去设置完了也就对应上了也都对应上了咱们的表
[02:21] 好那这个呢其实就是当前的实体类啊我就不再去说了然后下一步啊下一步呢咱们要去创建mypro咱们可以先去简单的看一下当前这个mypro接口你看这里边有一个delete还有什么insert还有什么还是要新增是吧查询根据ID查询还有根据条件去修改这个也是根据条件修改啊下面还有一个查询所有
[02:48] 谈一所有还有是查询可用谈一用可用当然这个你也根据不同的条件呢嗯可以去查询好吧嗯行那这个呢其实就是咱们所有的mypro的接口啊你可以练啊可以把它直接拷过来啊嗯好到什么位置我把这个没用的都关了啊拷到当前model下边找到mypro4有一个叫做colorsok把它直接拷到这就可以了行那目前当前的这个接口啊算是练完了
[03:21] 那创建完之后那你这硬的是不是得去干嘛是不是得去在这去创建一个什么配置文件的也就是说咱们的映射文件需要拿回来拷贝拿过来之后你可以把内容一下子都粘过来当完之后这个内容咱们可以再看一眼稍等好拷贝一下然后是直接粘到这看看有没有报错做是检查一下来看一下当前的这个没有问题
[03:57] 好你看这些都能找得着也都没有问题这些都是自断的映射吧然后下面是有一个circle的片段还有就是它对应的这种查询的方法或者新增的方法啊OK这个都能去找得着这里有个箭头啊你可以去直接找到你对应的mypro接口中的文件或者叫方法名好吧那行那这个呢咱们就算是做完了做完了刚才说了啊就是咱们要去针对于当前的ib代理池呢进行一个增张改查
[04:26] 好那这个MIPRO啊咱们就说到这啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
构建一个用于管理IP代理池的Java后端系统，包括数据库表结构设计、实体类、Mapper接口定义和Service层代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Navicat for MySQL中“mycat-145”数据库的“ad_label”表结构，同时显示“cl_ip_pool”表的DDL创建语句，包含字段如id, supplier, ip, port, username, password, code, duration, error, is_enable, ranges, created_time等。
画面2：展示Typora中“day10”文档的“1.1 ip代理池”章节，其中“1.1.1 需求分析”描述了IP代理池管理需求，包括增删改查、设置可用/不可用IP；“1.1.2 实体类”部分显示了实体类“ClipPool”的Java代码，包含id, supplier, ip, port等字段。
画面3：展示IntelliJ IDEA中“AdLabelServiceTest”测试类的代码，其中包含对ClipPool对象的setCode, setDuration, setError等方法的调用。
画面4：展示Typora中“1.1.2 实体类”部分，显示了ClipPool类的代码，包括get/set方法。
画面5：展示Typora中“1.1.3 Mapper接口定义”部分，显示了“ClipPoolMapper.xml”文件的路径和部分SQL语句，包括“selectList”和“selectAvailableList”方法。
画面6：展示IntelliJ IDEA中项目结构，选中“heima-leadnews-model”模块。
画面7：展示IntelliJ IDEA中“ClipPoolMapper.java”文件，显示了Mapper接口定义，包含deleteByPrimaryKey, insert, selectByPrimaryKey, updateByPrimaryKeySelective等方法。
画面8：展示Typora中“1.1.3 Mapper接口定义”部分，显示了“ClipPoolMapper.xml”文件的XML配置，包含namespace和resultMap等。
画面9：展示IntelliJ IDEA中“ClipPoolMapper.java”文件，显示了“selectAvailableList”方法的实现。
画面10：展示Typora中“1.1.3 Mapper接口定义”部分，显示了“ClipPoolMapper.xml”文件的完整XML配置，包含delete, insert, update等SQL语句。
画面11：展示Typora中“1.1.4 Service代码”部分，显示了“CrawlerIpPoolService”接口的定义，包含saveCrawlerIpPool方法。
画面12：展示IntelliJ IDEA中“ClipPoolMapper.xml”文件，显示了“Base_Column_where”和“Base_Column_list”等SQL片段。
画面13：展示IntelliJ IDEA中“ClipPoolMapper.xml”文件，显示了“selectByPrimaryKey”方法的SQL语句。
画面14：展示IntelliJ IDEA中“ClipPoolMapper.xml”文件，显示了“updateByPrimaryKeySelective”方法的SQL语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE TABLE cl_ip_pool (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  supplier varchar(60) DEFAULT NULL COMMENT '代理供应商',
  ip varchar(60) DEFAULT NULL COMMENT 'IP地址',
  port int(11) DEFAULT NULL COMMENT '端口',
  username varchar(60) DEFAULT NULL COMMENT '用户名',
  password varchar(60) DEFAULT NULL COMMENT '密码',
  code int(11) DEFAULT NULL COMMENT '状态码',
  duration int(11) DEFAULT NULL COMMENT '有效时长',
  error varchar(255) DEFAULT NULL COMMENT '错误信息',
  is_enable tinyint(1) DEFAULT NULL COMMENT '是否可用',
  ranges varchar(255) DEFAULT NULL COMMENT '范围',
  created_time datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=146 DEFAULT CHARSET=utf8;

画面2：
public class ClipPool {
  private Integer id;
  private String supplier;
  private String ip;
  // 端口
  private int port;
  ...

画面3：
public Integer getCode() { return code; }
public void setCode(Integer code) { this.code = code; }
public Integer getDuration() { return duration; }
public void setDuration(Integer duration) { this.duration = duration; }
public String getError() { return error; }
public void setError(String error) { this.error = error; }

画面4：
public void setRanges(String ranges) {
  this.ranges = ranges;
}
public Date getCreatedTime() {
  return createdTime;
}
public void setCreatedTime(Date createdTime) {
  this.createdTime = createdTime;
}
public Integer getCode() {
  return code;
}
public void setCode(Integer code) {
  this.code = code;
}
public Integer getDuration() {
  return duration;
}
public void setDuration(Integer duration) {
  this.duration = duration;
}
public String getError() {
  return error;
}
public void setError(String error) {
  this.error = error;
}

画面5：
int updateByPrimaryKeySelective(ClipPool record);
// 查询所有数据
* @param record
* @return
/
List<ClipPool> selectList(ClipPool record);
// 查询可用的列表
* @param record
* @return
/
List<ClipPool> selectAvailableList(ClipPool record);

画面6：
无代码或配置。

画面7：
package com.heima.model.mappers.crawlers;
public interface ClipPoolMapper {
  int deleteByPrimaryKey(Integer id);
  int insert(ClipPool record);
  ClipPool selectByPrimaryKey(Integer id);
  int updateByPrimaryKeySelective(ClipPool record);
  int updateByPrimaryKey(ClipPool record);
}

画面8：
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.mappers.crawlers.ClipPoolMapper">
  <resultMap id="BaseResultMap" type="com.heima.model.crawler.pojos.ClipPool">
    <id column="id" property="id"/>
    <result column="supplier" property="supplier"/>
    <result column="ip" property="ip"/>
    <result column="port" property="port"/>
    <result column="username" property="username"/>
    <result column="password" property="password"/>
    <result column="code" property="code"/>
    <result column="duration" property="duration"/>
    <result column="error" property="error"/>
    <result column="is_enable" property="isEnable"/>
    <result column="ranges" property="ranges"/>
    <result column="created_time" property="createdTime"/>
  </resultMap>

画面9：
无代码或配置。

画面10：
<delete id="deleteByPrimaryKey" parameterType="java.lang.Integer">
  delete from cl_ip_pool
  where id = #{id}
</delete>

<insert id="insert" parameterType="com.heima.model.crawler.pojos.ClipPool"
        useGeneratedKeys="true" keyProperty="id">
  insert into cl_ip_pool (id, supplier, ip, port, username, password, code, duration, error, is_enable, ranges, created_time)
  values (#{id}, #{supplier}, #{ip}, #{port}, #{username}, #{password}, #{code}, #{duration}, #{error}, #{isEnable}, #{ranges}, #{createdTime})
</insert>

<insert id="insertSelective" parameterType="com.heima.model.crawler.pojos.ClipPool"
        useGeneratedKeys="true" keyProperty="id">
  insert into cl_ip_pool
  <trim prefix="(" suffixOverrides=",">
    id,
    supplier,
    ip,
    port,
    username,
    password,
    code,
    duration,
    error,
    is_enable,
    ranges,
    created_time
  </trim>
  <if test="supplier != null and supplier != ''">
    supplier = #{supplier},
  </if>
  <if test="ip != null and ip != ''">
    ip = #{ip},
  </if>
  <if test="port != null and port != ''">
    port = #{port},
  </if>
  <if test="username != null and username != ''">
    username = #{username},
  </if>
  <if test="password != null and password != ''">
    password = #{password},
  </if>
  <if test="code != null and code != ''">
    code = #{code},
  </if>
  <if test="duration != null and duration != ''">
    duration = #{duration},
  </if>
  <if test="error != null and error != ''">
    error = #{error},
  </if>
  <if test="is_enable != null and is_enable != ''">
    is_enable = #{isEnable},
  </if>
  <if test="ranges != null and ranges != ''">
    ranges = #{ranges},
  </if>
  <if test="created_time != null and created_time != ''">
    created_time = #{createdTime},
  </if>
  <if test="supplier != null and supplier != ''">
    supplier = #{supplier},
  </if>
  <if test="ip !=

