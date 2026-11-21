# 画面线理解：11.今日佳人功能实现之mock接口以及编写基础代码

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\11.今日佳人功能实现之mock接口以及编写基础代码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:30, 00:56, 01:01, 01:13, 01:31, 01:38, 01:44, 01:55, 02:04, 02:11, 02:15, 02:23, 02:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:24:49

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
