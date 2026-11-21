# 11.今日佳人功能实现之mock接口以及编写基础代码

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\11.今日佳人功能实现之mock接口以及编写基础代码_【海量资源尽在 666java.com】.mp4
- 时长 2分42秒（音频 162s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下我们的这个今日家人的这个功能的一个实现啊那么首先呢我们来看一下它的一个MOOC的一个服务地址呢是在这里那么我们其实我们可以打开来看一下啊那么这个呢就是我们作为前后端进行做一个连条的这样的一个接口的一个定义啊然后呢这个是它的一个请求的方式啊然后呢get请求这个是它的一个地址
[00:27] 然后呢这个是他的一个绝对的这样的一个路径然后呢我们可以看到请求参数呢其实就只有一个啊就是我们的一个登录之后的一个token啊放到一个这个请求头里面去传递啊然后呢我们来看一下他的一个返回的一个数据啊大概是这样的一个结构有这个ID啊有ID有这个头像有这个Name 名称啊性别年龄啊还有Tax
[00:57] 就是这个标签然后呢还有一个原份值大概就这么几个啊那么我们就需要按照这个结构和这个地址呢然后去实现这样的一个接口然后呢就可以跟我们的前端的去做一个对接了那么接下来呢我们来看一下这个该如何去做一个实现呢那么接下来呢我们先把一些基础的代码呢我们都写好啊那么首先第一个呢是我们的一个
[01:23] 美举就是一个性别的一个美举啊那我们把这个美举这个包呢我们先创建出来这个呢跟我们之前写SSO里面的是一样的那我们就直接去做一个拷贝了把它拷贝过来在这那么这个就是我们性别的这样的一个美举那么接下来呢我们来看一下我们的一些相关的一些pojo那么首先呢就是这个base pojo啊这个呢是
[01:50] 跟我们之前写的SSO也是一样的我们就直接来写了叫podio然后把basepodio拷过来然后丢到里面来OK那么这个就搞定了那么下面我们来写这个user跟我们之前那个也是一样的就直接来拷贝了就是这个user然后还有什么的user info这是我们的用户信息这个大家应该是
[02:20] 也是比较熟悉的啊这样的一些这个信息了那么我们到这呢我们这个这个pozo啊基本是不是就搞定了OK那么这个就是我们一些基础性的一些这种代码那么下面呢我们是不是就可以实现一些相关的一些这种功能了对吧OK好那么关于这个基础代码的一个编写呢那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Mock 服务定义接口，并在后端 Java 项目中通过实体类和枚举类型实现“今日佳人”服务的数据模型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Mock 服务界面，接口名称为“今日佳人（前端已联调）”，状态为“已完成”，接口路径为“GET /tanhua/todayBest”，Mock 地址为“https://mock.boxuegu.com/mock/164/tanhua/todayBest”。
画面 2: 展示 Mock 服务的“请求参数”部分，Headers 中包含 Content-Type: application/json 和 Authorization: eyJ...（截断）。
画面 3: 展示 Mock 服务的“返回数据”部分，字段包括 id、avatar、nickname、gender、age、tags、fateValue，其中 tags 字段的校验规则为“最小值: 1, 元素是否都不同: true, Item 类型: string”。
画面 4: 展示 Mock 服务的“返回数据”部分，字段包括 id、avatar、nickname、gender、age、tags、fateValue，其中 tags 字段的校验规则为“最小值: 1, 元素是否都不同: true, Item 类型: string”。
画面 5: 展示 Typora 文档“day02.md”，章节“2.5.1. mock服务”，内容与画面 1 的 Mock 服务信息一致。
画面 6: 展示 IntelliJ IDEA 中的 Java 代码，`RecommendUserApiImpl.java` 类中的 `queryPageInfo` 方法，使用 `Criteria.where("toUserId").is(userId)` 查询推荐用户。
画面 7: 展示 IntelliJ IDEA 项目结构，选中 `com.tanhua.server` 包下的 `enums` 文件夹。
画面 8: 展示 Typora 文档“day02.md”，章节“2.5.2.2. BasePojo”，内容为 `BasePojo` 类的导入语句。
画面 9: 展示 IntelliJ IDEA 中的 `SexEnum.java` 文件，定义了 `MALE(1, "男")`、`FEMALE(2, "女")`、`UNKNOWN(3, "未知")` 三个枚举值。
画面 10: 展示 Typora 文档“day02.md”，章节“2.5.2.2. BasePojo”，内容为 `BasePojo` 类的导入语句。
画面 11: 展示 IntelliJ IDEA 中的 `User.java` 文件，`@Data`、`@NoArgsConstructor`、`@AllArgsConstructor` 注解，以及 `private Long id;`、`private String mobile;`、`@JsonIgnore private String password;` 字段。
画面 12: 展示 IntelliJ IDEA 中的 `User.java` 文件，`@JsonIgnore` 注解用于 `password` 字段。
画面 13: 展示 Typora 文档“day02.md”，章节“2.5.4. UserInfo”，内容为 `UserInfo` 类的导入语句。
画面 14: 展示 Typora 文档“day02.md”，章节“2.5.3. 实现功能”，内容为“2.5.3.1. TodayBest”部分，包含 `UserInfo` 类的字段定义，如 `private Long userId;`、`private String nickname;`、`private String logo;`、`private String tags;`、`private SexEnum sex;`、`private Integer age;`、`private String edu;`、`private String city;`、`private String birthday;`、`private String coverPic;`、`private String industry;`、`private String income;`、`private String marriage;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 代码：
```java
return this.mongoTemplate.findOne(query, RecommendUser.class, RecommendUser.class);
// 推荐用户的列表查询
@Override
public PageInfo recommendUser(Long userId, Integer pageNum, Integer pageSize) {
    Criteria criteria = Criteria.where("toUserId").is(userId);
    Pageable pageable = PageRequest.of(pageNum - 1, pageSize, Sort.Direction.DESC, "id");
    Query query = Query.query(criteria).with(pageable);
    List<RecommendUser> recommendUsers = this.mongoTemplate.find(query, RecommendUser.class);
    // 说明：数据总条数，暂时不提供，如果需要的话再提供
    return new PageInfo<>(total, pageNum, pageSize, recommendUsers);
}
```

画面 9 代码：
```java
package com.tanhua.server.enums;
import com.baomidou.mybatisplus.core.enums.IEnum;
public enum SexEnum implements IEnum<Integer> {
    MALE(1, "男"),
    FEMALE(2, "女"),
    UNKNOWN(3, "未知");
    private int value;
    private String desc;
    SexEnum(int value, String desc) {
        this.value = value;
        this.desc = desc;
    }
    @Override
    public Integer getValue() {
        return this.value;
    }
    @Override
    public String toString() {
        return this.desc;
    }
}
```

画面 11 代码：
```java
package com.tanhua.server.pojo;
import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User extends BasePojo {
    private Long id;
    private String mobile; //手机号
    @JsonIgnore
    private String password; //密码，json序列化时忽略
}
```

画面 13 代码：
```java
package com.tanhua.server.pojo;
import com.tanhua.server.enums.SexEnum;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
public class UserInfo extends BasePojo {
    private Long userId; //用户id
    private String nickname; //昵称
    private String logo; //用户头像
    private String tags; //用户标签：多个标签用分隔
    private SexEnum sex; //性别
    private Integer age; //年龄
    private String edu; //学历
    private String city; //城市
    private String birthday; //生日
    private String coverPic; //封面图片
    private String industry; //行业
    private String income; //收入
    private String marriage; //婚姻状态
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5: PPT 标题为“2.5.1. mock服务”，下方显示“地址：https://mock.boxuegu.com/project/164/interface/api/64568”。
画面 14: PPT 标题为“2.5.3. 实现功能”，下方列出“实现描述”：
- 需要根据前端定义的接口结构定义java对象
- 根据sso系统提供的接口访问当前登录用户的信息
- 根据dubbo系统提供的服务进行查询今日佳人数据
并列出子章节“2.5.3.1. TodayBest”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

