# 画面线理解：10.黑名单列表之表结构以及查询

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\10.黑名单列表之表结构以及查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:07, 01:27, 01:54, 02:23, 02:44, 03:03, 03:30, 04:09, 04:33, 05:21, 05:43, 06:02, 06:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:43:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 MyBatis-Plus 框架下，通过 Service 层调用 Mapper 层，实现对黑名单表（black_list）的分页查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：Navicat 数据库管理工具界面，显示数据库 mytanhua 中的表 tb_question，包含两条记录，id 为 1 和 2。
画面 2：Navicat 中显示表 tb_black_list 的结构，其 DDL 语句被高亮选中，包含字段 user_id、black_user_id、created、updated，主键为 id，引擎为 InnoDB，字符集为 utf8，注释为“黑名单”。
画面 3：Navicat 中显示表 tb_black_list 的结构，其 SQL 创建语句被高亮选中，内容与画面 2 的 DDL 语句一致。
画面 4：IntelliJ IDEA 中显示 QuestionService.java 文件，save 方法中根据用户 ID 查询问题，若存在则更新，否则新建并插入。
画面 5：IntelliJ IDEA 中显示 BlackListMapper.java 文件，其内容为一个继承自 BaseMapper 的接口，用于定义黑名单相关的数据库操作。
画面 6：IntelliJ IDEA 中显示 BlackListService.java 文件，其内容为空白，准备编写服务层逻辑。
画面 7：Typora 中显示 day11 识义.md 文档，其中 2.7.4 节为 BlackListService 的代码，包含 Service 注解、Autowired 注解、BlackListMapper 类型的私有成员变量、以及 queryPageList 方法的声明。
画面 8：IntelliJ IDEA 中显示 BlackListService.java 文件，正在编写 queryPageList 方法，方法签名已定义。
画面 9：IntelliJ IDEA 中显示 BlackListService.java 文件，正在编写 queryPageList 方法，方法体已开始。
画面 10：IntelliJ IDEA 中显示 BlackListService.java 文件，正在编写 queryPageList 方法，创建 QueryWrapper 对象并设置条件。
画面 11：IntelliJ IDEA 中显示 BlackListService.java 文件，正在编写 queryPageList 方法，设置排序条件。
画面 12：IntelliJ IDEA 中显示 BlackListService.java 文件，正在编写 queryPageList 方法，创建 Page 对象。
画面 13：IntelliJ IDEA 中显示 BlackListService.java 文件，正在编写 queryPageList 方法，调用 selectPage 方法。
画面 14：IntelliJ IDEA 中显示 BlackListService.java 文件，queryPageList 方法已编写完成，返回 PageBlackList 对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
CREATE TABLE `tb_black_list` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`user_id` bigint(20) DEFAULT NULL,
`black_user_id` bigint(20) DEFAULT NULL,
`created` datetime DEFAULT NULL,
`updated` datetime DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `user_id` (`user_id`),
ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='黑名单';

画面 3：
[SQL]CREATE TABLE `tb_black_list` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`user_id` bigint(20) DEFAULT NULL,
`black_user_id` bigint(20) DEFAULT NULL,
`created` datetime DEFAULT NULL,
`updated` datetime DEFAULT NULL,
PRIMARY KEY (`id`),
ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='黑名单';

画面 4：
public void save(Long userId, String content) {
//判断问题是否存在，如果存在，进行修改，如果不存在，新增操作
Question question = this.queryQuestion(userId);
if(null != question) {
question.setTxt(content);
this.questionMapper.updateById(question);
}else{
question = new Question();
question.setUserId(userId);
question.setTxt(content);
this.questionMapper.insert(question);
}
}

画面 5：
package com.tanhua.server.mapper;
import com.fasterxml.jackson.databind.Base;
public interface BlackListMapper extends Base<BlackList> {

画面 7：
2.7.4. BlackListService
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
}

画面 8：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {

画面 9：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {
this.blackListMapper.

画面 10：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {
QueryWrapper<BlackList> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column: "user_id", userId);

画面 11：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {
QueryWrapper<BlackList> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column: "user_id", userId);
//排序，根据创建时间倒序排序
queryWrapper.orderByDesc(column: "created");

画面 12：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {
QueryWrapper<BlackList> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column: "user_id", userId);
//排序，根据创建时间倒序排序
queryWrapper.orderByDesc(column: "created");
//分页的参数
Page<BlackList> pager = new Page<>(page, pageSize);

画面 13：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {
QueryWrapper<BlackList> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column: "user_id", userId);
//排序，根据创建时间倒序排序
queryWrapper.orderByDesc(column: "created");
//分页的参数
Page<BlackList> pager = new Page<>(page, pageSize);
this.blackListMapper.selectPage(pager, queryWrapper);

画面 14：
package com.tanhua.server.service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {
QueryWrapper<BlackList> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column: "user_id", userId);
//排序，根据创建时间倒序排序
queryWrapper.orderByDesc(column: "created");
//分页的参数
Page<BlackList> pager = new Page<>(page, pageSize);
return this.blackListMapper.select
