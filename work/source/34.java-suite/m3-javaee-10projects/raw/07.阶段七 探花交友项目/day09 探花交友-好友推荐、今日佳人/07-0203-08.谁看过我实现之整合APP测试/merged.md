# 08.谁看过我实现之整合APP测试

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\08.谁看过我实现之整合APP测试_【海量资源尽在 666java.com】.mp4
- 时长 1分21秒（音频 81s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢我们就整合到我们的APP里面啊我们来测试一下我们的这个推荐好友的列表和我们谁看过我这个功能啊那我们已经呢我这里呢已经就整合成功了那么其实可以看到在这个位置啊是不是有一个最近六人来访啊快去查看然后呢下面的这个呢是今日佳人然后呢再往下面走呢这一块呢就是我们的推荐的列表了但是呢我们需要注意一下就是那么这个推荐列表它是有一些这个筛选
[00:29] 那么如果我们要去增加这个筛选条件的话
[00:55] 那么我们就去把这个条件打开呢就可以了那么只要他能够去找到满足我们条件的一些这个数据他就能够去响应出来所以说我们现在暂时呢先去看一下这个效果啊这样的一个这个效果了OK这就是我们去整合了我们首页的一些这个接口之后的一个首页这样的一个效果OK好那么关于我们这个整合的一个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个交友App的前端界面交互与后端Java服务代码逻辑，重点展示用户推荐列表、筛选功能及对应的后端查询条件构建。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示Typora编辑器中Java类`VisitorsVo`的代码，用于定义用户推荐数据结构。
画面2：展示Genymotion模拟器中App的首页，包含“桃花”、“附近”、“桃花传音”等标签页和“今日佳人”推荐卡片。
画面3：在App首页，点击“今日佳人”卡片，页面跳转至用户详情页。
画面4：在用户详情页，点击“推荐”按钮，页面跳转至推荐列表页。
画面5：在推荐列表页，点击“筛选”按钮，弹出筛选面板，包含性别、最近活跃时间、年龄、居住地等筛选条件。
画面6：切换至IntelliJ IDEA，显示`TodayBestService.java`文件，代码中构建`QueryWrapper`用于查询用户信息。
画面7：在IDEA中，代码高亮显示`queryWrapper.in(column: "user_id", userIds);`，用于根据用户ID集合查询。
画面8：在App中，点击“筛选”面板的“确认”按钮，页面返回推荐列表页。
画面9：在IDEA中，代码高亮显示`if (StringUtils.isNotEmpty(queryParam.getCity())) {`，用于根据城市条件查询。
画面10：在App中，点击“筛选”面板的“确认”按钮，页面返回推荐列表页。
画面11：在App中，点击“筛选”面板的“确认”按钮，页面返回推荐列表页。
画面12：在App中，点击推荐列表页的某个用户卡片，页面跳转至该用户详情页。
画面13：在App中，点击“推荐”按钮，页面跳转至推荐列表页。
画面14：在App中，点击“推荐”按钮，页面跳转至推荐列表页。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhua.server.vo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class VisitorsVo {
    private Long id;
    private String avatar;
    private String nickname;
    private String gender;
    private Integer age;
    private String[] tags;
    private Integer fateValue;
}
```

画面6：
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds); //用户id
if (queryParam.getAge() != null) {
    //queryWrapper.lt("age", queryParam.getAge()); //年龄
}
```

画面7：
```java
List<Long> userIds = new ArrayList<>();
for (RecommendUser record : records) {
    userIds.add(record.getUserId());
}

QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds); //用户id
if (queryParam.getAge() != null) {
    //queryWrapper.lt("age", queryParam.getAge()); //年龄
}
if (StringUtils.isNotEmpty(queryParam.getCity())) {
    //queryWrapper.eq("city", queryParam.getCity()); //城市
}
//需要查询用户的信息，并且按照条件查询
List<UserInfo> userInfos = this.userInfoService.queryUserInfoList(queryWrapper);
List<TodayBest> todayBests = new ArrayList<>();
for (UserInfo userInfo : userInfos) {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

