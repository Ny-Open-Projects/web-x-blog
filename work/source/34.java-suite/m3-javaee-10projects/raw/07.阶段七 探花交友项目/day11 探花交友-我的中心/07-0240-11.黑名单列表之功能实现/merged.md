# 11.黑名单列表之功能实现

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\11.黑名单列表之功能实现_【海量资源尽在 666java.com】.mp4
- 时长 10分22秒（音频 623s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来看一下我们的Mock接口然后呢我们来开发我们这个服务的接口好然后呢我们来找到我们这个Mock的一个接口啊那么就是我们这个黑名单的这个翻页列表然后呢它的地址呢就是这样的一个地址然后呢下面是它的一些这个参数啊Page by Page Size然后呢返回的是一个标准的一个分页这样的一个结构然后呢其中的这个Items呢是关键内容
[00:29] 有用户的ID有这个头像还有尼称性别还有年龄这么几个字段那么我们肯定的是要根据我们这个字段来去写一下什么我们的VO这个对象对吧好我们就接下来我们就先把VO对象的去来实现一下那么就是我们VO这个对象那么我们找到我们的这个server下面我们来找到VO再把它拷贝过来
[00:59] 就是我们的一个黑命蛋这样的一个VO那么接下来我们就来创建我们的这个Controller那么还是进入到我们的uruscontroller里面然后我们去找到我们这个urus的Controller然后是在这个里面然后我们其实可以看到这个里面是不是就接收了有两个这个参数配置和配置size然后
[01:28] 发起的是一个get请求然后呢我们去做一个查询最后响应的是一个我们的一个page result对象然后呢我们把这个方法呢给它来创建出来好那么到这走走走好嘞那么接下来呢我们就来做实现啊那么首先呢我们去拿到我们的这个usr就是等于usr stay local点点get
[01:56] 然后呢接下来呢我们去做一个查询那我们就通过this.那么我们那个就是blacklist的这个API呢这个Service呢还没有注入进来对吧那我们就来注一下那么在这blacklist Service把它注入进来注进来
[02:24] 然后我们继续往下面看在下面这个位置我们就调用我们的刚刚所写的这个方法叫做queryPagerList那么第一个参数是我们的用户ID第二个是Pager第三个参数是PagerSize然后我们就会得到我们的一个Pager对吧就是叫Pager应该叫什么就叫IPager
[02:53] 然后呢通过我们这个ipager那我们就能够拿到一些相关的一些数据啊所以说我们就来去定义我们的一个这个pager resultpager result等于new一个pager result然后呢我们去做一个返回那么我们给它去set一些值啊那么pager size那么就是我们的这个pager size
[03:22] 那么还有谁呢我们来看一下还有就是pay set这个pay者那就是这个pay者然后呢我们再来set一个我们的一个counts就是我们的数据总数那就通过这个ipay中能够拿到我们的一个total然后呢这个呢要注意它呢是一个楞类型我们需要去
[03:48] new一个lang把它丢进来然后呢再拿到一个int点intvalue这样的话才可以那么这个呢是counts那么还有一个叫pageresult点set一个pages就是我们的总页数那么这个呢也是通过我们的一个ipagerget一个pages能够拿到那么我们就给它来new一个lang传过来点
[04:18] 点intervalue好那么这样的话呢就拿到我们这个pages和counts啊那么这么几个资段呢是不是我们就都拿到了那么呃接下来呢我们就需要拿到我们的一个这个数据集对吧就通过我们的一个ipage点get一个records那么这个就是我们的数据集了那么我们来拿到它啊那么拿到这个records之后呢我们肯定先要去做一个
[04:46] 判断对吧那么就是判断是否是呃 唯空的那么如果唯空的话那我们肯定直接需要做一个return啊这个操作了那么就return我们这个配置啊result这样的一个对象那么接下来呢下面我们要查询用户相关的一些数据了那么下面呢我们来定义我们的一个就是uid啊这样的一个集合嗯然后呢ids等于new一个uiv list
[05:16] 然后我们去做一个迭代那么去迭代这个recode然后呢这个userid s这个集合呢我们就按着添加一个recode.get一个我们的一个blocker这个userid就是我们黑名单那么下面呢我们就通过我们的这个user info Service做一个query查询那么它需要一个
[05:47] 这个querywrap对象去分装一下那么就叫user info然后呢我们去设置一个querywrap等于new一个querywrap然后呢querywrap.in操作一个叫做user下滑线id然后呢逗号呢来一个就是userids这样的一个集合然后呢我们去做一个查询
[06:12] 然后他所拿到的就是我们U的info list然后接下来我们就需要去便利我们的U的info然后我们还需要定义一个集合就是我们的一个最终响应的一个集合就是blacklist vo这个集合vo list吧然后去new一个arriv list那么最后需要把我们这个new的这个集合然后set到我们的一个items中
[06:42] 去作为一个结果呢去返回然后呢我们来看一下这个里面呢我们就需要去每一次循环呢去new一个这个VO这个对象然后呢我们最后呢就来一个blacklist然后呢VO list点按的添加一个它好那么接下来呢我们只要完成数据的一个填充啊就可以了那么我们这个blacklist这个VO这个对象呢
[07:11] set一个 nickname那我们就拿到 your info里面的点get一个 nickname那么还有其他的我们来填充一下set一个这个 id呢就是我们的这个用户 id了get u id然后呢还有set我们的一个这个gender性别那么sex拿到他的一个名字啊去转成一个小写然后呢还有一个是什么呢
[07:39] 我们的一个这个头像还有吗还有来看一下set一个还有一个age还有一个get一个age好那么这样的话呢数据呢就已经填充完成了那么是不是就可以返回这个列表了接下来呢我们就来重新启动来测试一下好那么现在我们这个服务呢就已经跑起来了那么接下来我们来测试一下那么首先呢我们来做登录
[08:10] 那么发送验证码啊然后呢我们去做一个这个login啊这样的一个登录好那么就登录成功了然后呢再进入到这个里面呢我们去做一个查询那么我们把这个地址我们来拷问一下然后呢我们啊往这一丢去做一个查询走
[08:30] 查询我们当前用户的黑名单的列表那么可以看到是不是已经查询到了那么接下来我们就来整合到我们的手机来查看一下那么先把我们投屏的电脑端打开然后我现在去把我手机上面的它来启动一下然后我点击投屏然后它正在去做扫描我点击它
[08:58] 做一个手机的一个投屏OK那么其实可以看到我手机的屏幕了对吧然后呢我们打开这个探花然后呢看一下我们的服务地址没有问题是我们的酒吧这个地址然后呢我们再去做一个登录其实我们使用这个投屏呢就更加的简单了就不用占用我们的这个电脑这个资源了好那么它呢就会进入到我们的这个首页啊然后呢我们再看下面的一个
[09:29] 这个我的这个模块然后呢在这个里面呢我们去找到我们的一个通用设置然后呢这个里面会有一个黑名单那么其实可以看到是不是已经有三个啊这个用户了那么我们后面呢还有一个取消这个黑名单这个呢我们在后面的去完成这个功能啊好那么接下来呢我们来一起看一下我们的讲义啊那么这个是我们的Controller啊那么这个其实没什么好说的啊然后呢这个是我们的Vue
[09:56] 然后呢这个是下面的Service这个里面呢大家需要去按照我们所需要的一些这个逻辑的去编写这个Service那么最终呢就可以响应到我们所期望得到的一些这个数据了OK那么最终呢我们整合到我们的这个APP里面的一个显示呢就是这样的一个显示好嘞好那么关于我们这个黑名单列表的一个功能的一个开发呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在用户服务中实现黑名单分页查询功能，并通过 Mock 服务模拟接口数据。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Typora 文档中“2.7.5. mock接口”章节，包含 Mock 服务的接口基本信息和请求参数，Mock 地址为 https://mock.boxuegu.com/mock/164/users/blacklist。
画面 2: 展示 IntelliJ IDEA 中 BlackListVo.java 类的定义，包含 id、avatar、nickname、gender、age 等字段。
画面 3: 展示 UsersService.java 中 queryBlacklist 方法的代码，调用 blacklistService 的 queryPageList 方法。
画面 4: 展示 UsersService.java 中 queryBlacklist 方法的代码，调用 blacklistService 的 queryPageList 方法，并显示了 User 类的成员变量列表。
画面 5: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 PageResult 的 setPages 方法设置分页信息。
画面 6: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 PageResult 的 setPages 和 setTotal 方法设置分页信息。
画面 7: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 PageResult 的 setPages 和 setTotal 方法设置分页信息，并显示了 List 类的成员变量列表。
画面 8: 展示 UsersService.java 中 queryBlacklist 方法的代码，创建了 List<Long> userIds 并遍历 records 获取 userId。
画面 9: 展示 UsersService.java 中 queryBlacklist 方法的代码，使用 QueryWrapper 查询用户信息，并遍历结果。
画面 10: 展示 UsersService.java 中 queryBlacklist 方法的代码，创建 BlackListVo 对象并设置 nickname、id、avatar、gender、age 等属性。
画面 11: 展示 UsersService.java 中 queryBlacklist 方法的代码，设置 BlackListVo 的 age 属性。
画面 12: 展示 Mock 服务的接口详情页面，接口路径为 /users/blacklist，Mock 地址为 https://mock.boxuegu.com/mock/164/users/blacklist。
画面 13: 展示手机端应用的黑名单界面，显示了三个用户信息。
画面 14: 展示 Typora 文档中“2.8.1. UsersController”章节，包含黑名单列表的 UI 设计图。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```java
package com.tanhua.server.vo;
import ...
@Data
@AllArgsConstructor
@NoArgsConstructor
public class BlackListVo {
    private Long id;
    private String avatar;
    private String nickname;
    private String gender;
    private Integer age;
}
```

画面 3:
```java
public PageResult queryBlacklist(Integer page, Integer pagesize) {
    User user = UserThreadLocal.get();
    return null;
}
```

画面 4:
```java
User user = UserThreadLocal.get();
this.blacklistService.queryPageList(user.getId(), page, pagesize);
```

画面 5:
```java
this.blacklistService.queryPageList(user.getId(), page, pagesize);
```

画面 6:
```java
PageResult pageResult = new PageResult();
pageResult.setPagesize(pagesize);
pageResult.setPage(page);
pageResult.setCounts(new Long(iPage.getTotal()).intValue());
pageResult.setPages(new Long(iPage.getPages()).intValue());
```

画面 7:
```java
PageResult pageResult = new PageResult();
pageResult.setPagesize(pagesize);
pageResult.setPage(page);
pageResult.setCounts(new Long(iPage.getTotal()).intValue());
pageResult.setPages(new Long(iPage.getPages()).intValue());
List<BlackList> records = iPage.getRecords();
```

画面 8:
```java
List<Long> userIds = new ArrayList<>();
for (BlackList record : records) {
    userIds.add(record.getBlackUserId());
}
```

画面 9:
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in("user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryUserInfoList(queryWrapper);
```

画面 10:
```java
List<BlackListVo> blackListVoList = new ArrayList<>();
for (UserInfo userInfo : userInfoList) {
    BlackListVo blackListVo = new BlackListVo();
    blackListVo.setNickname(userInfo.getNickName());
    blackListVo.setId(userInfo.getId());
    blackListVo.setAvatar(userInfo.getAvatar());
    blackListVo.setGender(userInfo.getGender());
    blackListVo.setAge(userInfo.getAge());
    blackListVoList.add(blackListVo);
}
```

画面 11:
```java
blackListVo.setAge(userInfo.getAge());
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“2.7.5. mock接口”，包含“基本信息”和“请求参数”两个部分。
画面 12: PPT 标题为“接口列表”，包含“接口名称”、“接口路径”、“Mock地址”、“状态”、“创建人”、“更新时间”等字段。
画面 14: PPT 标题为“2.8.1. UsersController”，包含“黑名单列表”和“移除黑名单”两个部分。

5) 无。

