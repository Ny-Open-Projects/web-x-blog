# 10.黑名单列表之表结构以及查询

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\10.黑名单列表之表结构以及查询_【海量资源尽在 666java.com】.mp4
- 时长 7分13秒（音频 433s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下黑名单列表那么也就是我们的黑名单的这个功能那么下面我们首先来看一下我们的表结构然后呢我们来看一下这张表叫什么呢tb black list然后呢有这么几个制度啊有id用户id还有我们的黑名单的这个用户idcreate和update
[00:23] 然后呢我们去给我们的这个ID呢去设置为我们的一个组件当然了我们还是需要去把这个UID给它设置一个索引的这样的话我们在做查询的时候呢就会更快一些好那么我们把这个表结构呢我们就来执行一下然后呢还是找到我们的这个就是麦炭花的这个表里面然后呢我们去执行一个我们的一个这个Circle语句
[00:49] 走那么可以看到呢我们这个表结构呢是不是就搞定了然后呢我们接下来呢来设计下这张表给它去添加一个索引那么就是给我们这个UID呢去添加一个索引这样的话呢就它查询的更快一点然后呢我们把这个来拷贝一下给大家给大家把这个我们的就是这个讲义呢我们来修改一下
[01:17] 好那么这样的话呢就是我们的这样的一个表结构了那么接下来呢我们像我们这个表里面呢插入三条测试数据然后呢我们来看一下这个数据啊那么是不是我们给这个用户ID唯一的这个用户啊添加了有三个这个黑名单啊就是222324大概就是这样的一个数据了那么接下来呢我们就来开发我们的这个功能那么首先呢我们来编写我们的这个puzzle啊
[01:48] 跟我们的这个表结构呢是一样的这样的一个结构啊然后呢我们来拷贝一下还是呢去进入到我们的server啊这个工程里面来找到这个podio然后呢我们往这一丢然后呢去继承这个basic podio啊设置我们三个字段啊这样的话就ok了那么接下来呢我们肯定要去设置我们的Mapper那么就是我们那个blacklist一个mappermapper
[02:16] 然后我们去是一个interface然后我们去做一个继承叫base Mapper t那就是我们的一个blacklist这样的一个对象好那么我们的就是map就搞定了那么下面我们来看一下我们的Service那么在下面这个位置来设置一个我们的一个blacklist一个Service
[02:44] 然后呢把它标记为呢这是一个Service那么接下来呢我们就需要把我们的这个Mapper呢注入进来把它注入进来好那么注入进来之后呢就可以去使用这个里面的CIUD的方法了那么接下来呢我们就来实现我们具体的一个查询的一个逻辑啊
[03:06] 那么首先呢我们是需要通过我们的用户ID呢去做一个分页的一个查询那么这样我们就直接来写这个方法吧那么就写一个public那么返回值呢返回我们的是一个叫ipage就是在mybattles中啊myplus中啊会有这样的一个对象啊叫ipage那么这个类型呢就是我们的一个了blacklist然后呢叫做
[03:35] query我们的一个pager list这个名字呢大家可以自己去做一个定义啊那么显然呢他肯定是需要传递有三个参数对吧第一个呢就是我们的UID那么第二个呢就是我们的一个pager然后呢第三个呢就是我们的一个pager sizesize这样的一些这个参数好那么接下来呢我们来看一下这个怎么样去做一个实现
[04:05] 那么首先呢在这个位置我们是需要通过谁呢通过我们这个Mapper它有一个叫做selectPager这个方法那么selectPager它需要传递有两个参数那么一个是我们的一个这个Pager一个呢就是我们的一个这个QueryWrap就是条件啊所以说呢我们需要给它构造这两个条件那么首先呢我们先来构造我们的一个QueryWrap这样的一个对象吧那么
[04:33] 我们去构造一下它然后呢叫queryrop等于new一个queryrop然后呢这是我们的第二个这个条件对吧那我们先设置为那了然后呢给它去做一个传递然后呢我们来给它设置条件那肯定是根据什么呢根据我们的然后呢EQ相等对吧相等谁呢就是我们的U的
[04:59] user id然后呢我们去再更换一个谁呢就是我们的user id了这是我们的第一个这个条件那么第二个呢我们是需要给它设置一个排序就是我们要根据我们的一个创建时间去做一个倒序倒序的一个排序那么通过这个query然后呢写一个order by desc
[05:26] 谁呢我们去给他写一个字段就是我们的createdcreated去做一个倒序的一个排序那我们这个查询条件是不是就搞定了那么接下来呢我们就需要去去new一个谁呢我们那个pager这个对象那么这个设置就是blacklist然后呢这个pager那么就pager吧然后呢去new一个这个pager然后呢他呢需要有两个这个参数这个是
[05:55] 没导入进来吗那我们来看一下啊就是它然后呢需要有两个参数那么可以看到第一个参数呢哎那么哎这个我们是不是导错包了呃配置然后呢需要有两个参数那么第一个这个参数呢我们来看一下它呢就是当前的一个页数第二个呢就是每页显示的一个条数所以说呢我们在这个位置啊那么就
[06:23] 给他去直接做一个传递就好了那就配置和配置赛事啊这样的话是不是就OK了啊然后呢我们把它就往这一丢然后呢我们最后呢return一下啊return那么这个呢就是什么呢我们的这个分页的一个参数啊分页的一些这个参数了好嘞好那么这样的话呢我们这个
[06:48] 查询呢是不是就搞定了那么我们后面呢肯定会根据用户ID呢是不是去做一个这个数据的一个查询啊OK好的吧关于我们这个列表的这个一个服务的这样的一个编写的那我们就先讲到这里后面呢我们就来整合到我们的一个APP的一个这样的一个接口呢我们再去调用它啊OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.tanhua.server.Mapper;
import com.fasterxml.jackson.databind.Base;
public interface BlackListMapper extends Base<BlackList> {

画面 7：
2.7.4. BlackListService
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.tanhua.server.Mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
}

画面 8：
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
import com.tanhua.server.pojo.BlackList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class BlackListService {
@Autowired
private BlackListMapper blackListMapper;
public IPage<BlackList> queryPageList(Long userId, Integer page, Integer pageSize) {

画面 9：
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
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
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
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
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
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
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
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
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
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
package com.tanhua.server.Service;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tanhua.server.Mapper.BlackListMapper;
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

