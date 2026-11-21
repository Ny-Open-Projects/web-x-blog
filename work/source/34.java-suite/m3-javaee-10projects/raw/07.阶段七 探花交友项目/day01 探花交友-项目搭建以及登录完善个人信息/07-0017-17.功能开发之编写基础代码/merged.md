# 17.功能开发之编写基础代码

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\17.功能开发之编写基础代码_【海量资源尽在 666java.com】.mp4
- 时长 9分42秒（音频 583s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来编写一些基础性的一些代码那么首先第一个呢是我们来去编写的这个呢是美举啊就是性别的这个美举啊那么其实可以看到在这个里面呢我们和数据库是有对应的就是这个一啊代表是男二代表是女三呢代表是未知然后呢在这个位置我们的这个美举需要去继承啊买Bitplus所提供的啊这样的一个美举
[00:29] 这样的话就可以很方便的在我们的这个数据库在交互的时候啊使用这个美举啊呃那么呃好那么我们就直接来使用了那么我们把它呢就拷贝到我们刚刚所创建的这个包里面来好这个美举呢我们就已经是搞定了那么这个美举中的一些这个写法或者说怎么样去使用它这个呢
[00:51] 或者怎么在买杯的这plus中啊去使用他的话那么这个呢我就不讲了啊如果说对这块还不是很了解的话可以看一下前面的一些这个相关的一些资料啊好呃然后呢我们接下来呢去创建我们的一些这个实体那我们把这个pojo啊这个包呢我们先创建出来那我们在这个位置来创建一个这个pojo这个包呃然后呢我们把这个代码拷贝过来啊
[01:18] 然后首先第一个是我们需要给我们所有的这个Pozole去创建一个BasePozole这样的一个附类那么为什么要创建呢原因是我们会对我们所有的表都会有两个字段一个就是这个Create和一个Update那么这两个字段代表分别代表是创建时间和更新时间
[01:40] 那么有了这两个那么这两个是在所有的表中都有那么所以我们需要把它抽取出来然后我们去创建一个base puzzle这样的一个类那么要注意的是在这个位置我们去设置了base puzzle是一个抽象类然后我们给它设置了两个属性一个是created一个是update那么这两个都标记为是一个table field并且去做一个什么自动填充
[02:07] 也就是说这个使用的也是MyBedisPlus所提供的一个自动填充的这样的一个功能那么Creator是在我们做数据叉误的时候去做一个自动填充那么我们的更新是在update的时候insert和update的时候做一个更新做一个自动填充好那么有了这个类之后那么下面我们就可以去写相关的一些我们具体的实体了比如说这个user那么我们来把它来call一下
[02:36] 把它一丢那么这个就是我们这个u的对象它是继承于我们这个base puzzle然后这个里面的一些字段那么所对应的就是我们表中的一些字段那么要注意的是在这个对象中我们并没有去写 tburl而是我们直接写入的那么前面我们说过在我们的配置文件中是不是我们指定了这个表的前缀对吧
[03:02] 默认就会找到我们的这个tp消费者优劣了这是第一个点那么第二个点是在我们这个优的对象上面去添加了这么几个注解那么分别是谁叫做date还有什么这个是没有参数的勾找方法还有一个全参数的勾找方法这个所使用的是Lambook的所提供的这样的一些注解那么就可以去简化我们这个Java并的去编写那么其实当我们加入date之后它就自动会给我们去
[03:32] 自动可以在这可以看到是不是就已经有了这个get和set的方法了就没有必要写那么一堆的这个get和set了ok好那么这个我们就搞定了那么下面我们来看一下这个user info那么我们把它也call过来那么这个都是比较基础的一些代码
[03:51] 那么在这个里面呢其实我们可以看到是不是跟我们的数据库的字段呢要做一些这个映射啊做一些对应同样的也是使用这个Lambook所提供的一些这个注解来完成简化我们这个Pozole的这样的一个目的啊那么这个就不一一去解释了这个大家都能够看懂哦
[04:10] 那么接下来我们来处理前面我们所写的自动填充的逻辑那么在前面我们是不是给我们的base puzzle中是不是添加了一个自动填充的这样的一个注解那么并不是说你添加一个自动填充它就能够生效而是说我们需要去自己写这个业务逻辑那么这个逻辑我们把它放到这个SSO下面这个handle这个里面那么我们来看一下
[04:37] 这个代码大家一看应该能够看懂之前应该也使用过这样的这样的一些用法那我们把它拷贝过来然后来看一下那么在这个中我们其实可以看到那么首先我们是需要把我们的这个类去添加一个component这样一个注解是不是就会去载入到Spring的容器对吧
[05:01] 然后我们这个内去实现Meta Object Handler这样的一个接口然后实现完成之后就会去实现两个方法一个是叫Insert For还有一个叫做Update For那么Insert这个就是做一个什么做一个自动的一个填充自动就是插入的自动填充而这个Update是在我们更新的时候去做一个自动填充的那么要注意的是前面我们其实可以看到
[05:31] 那么在我们的这个basepos中呢那么我们这个update是不是在在我们这个insert和update的时候都会去更改这个update这个字段而我们created呢只是在插入的时候去插入好那我们来看一下这个逻辑啊有没有问题呢那么在我们去做insert操作的时候呢我们先去拿到我们一个对象中的一个created
[05:58] 那么拿到它之后呢如果判断这个自占为空那我们就给它去设置值这个值的默认值是不是就是一个当前的这个时间呢对吧然后呢我们再去拿到我们这个对象中的这个update然后呢这个如果也是为none的话那我们就给它去做一个填充填充的也是当前这个时间那么这样的话是不是就完成了我们插入数据时候的一个自动填充的一个逻辑那么如果是在我们更新的时候它逻辑是这样的
[06:27] 那我们就需要去拿到我们update这个字段然后呢我们去判断它是不是为空那么如果不是为空的话那我们就去做一个这样的一个更新了对吧ok好那么这样的话呢我们是不是就实现了我们这个逻辑了那么其实我们这个update这个逻辑它是有一点点问题的大家可以想一下那么我们在更新数据的时候其实无论你这个是否为none那么我都要去给你去更新这个
[06:56] 当前的这个时间这个逻辑是不是才对并不需要做判断了所以说我们和这个叉误的时候是不一样的所以这个我们就要把它去掉了就是说我们直接拿到这个update那我们直接就要去做什么做更新了可以看到那么如果拿到它我们就直接去做更新那这个我们也不需要去拿了对吧我们直接直接去去给他去做一个填充就可以了
[07:25] 就是我们把这个呢来改一下啊这个就是什么呢就是我们更新数据更新数据时呢就是直接啊更新这个字段啊不需要做判断了啊这个要注意啊那么OK我们把这个蒋一中这个代码呢也来修改一下啊那么要注意了这个不需要做判断了因为我们在更新数据的时候直接要把这个update这个字段去做一个更新啊就OK了好嘞好那么到这呢我们这个逻辑是不是就搞定了
[07:54] 那么接下来呢我们把这个相关的这个Mapper也写出来那么我们需要呢去创建一个这个Mapper这样的一个包那么写我们的一些这个Mapper好那么这个里面呢我们需要写的一个接口叫什么呢就叫usermapper那么这个Mapper呢其实它是需要去继承谁呢继承这个mybattisplastic插件
[08:22] 叫什么呢叫做base什么呢map进生它那么这个t是谁呢那就是刚刚我们所写的这个url这个对象ok那么有了这个map之后url map之后啊那么我们是不是就会使用这个base map中所提供的一系列这样的一些方法了ok好那么有了它之后呢就ok了对吧那么最后一个呢我们将编写我们的一个这个启动的一个application那么叫什么呢叫myapplication那么我们就
[08:52] 把它来靠一下那么我们就需要在哪是不是在这个里面直接去粘贴一下好那么我们的spin boot的启动类是不是就搞定了这是一个非常标准的启动类那么要注意的是在这个位置那么我们需要设置我们的mybattis Mapper的一个接口
[09:14] 去扫描扫描包那么这个接口是不是就刚刚我们所写Urmapper所在的包来看一下对不对那么是不是就是在这个里面别搞错com 探花 sso 没有问题然后我们给它加一个sprint boot application写这样的run方法就可以去启动了ok好那么到这里我们的基础性的代码是不是就已经搞定了好那么关于基础代码的编写那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 MyBatis Plus 的用户信息管理系统项目搭建过程，包括枚举类、POJO实体类、元对象处理器和启动类的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 SexEnum.java 文件内容，定义了性别枚举类，包含 MAN、WOMAN、UNKNOWN 三个常量。
画面2：在 IntelliJ IDEA 中右键点击 SexEnum.java，弹出菜单，选中“Replace in Path...”选项，准备进行全局替换。
画面3：展示 day01 项目文档中 3.5.2 User, UserInfo 节点，以及 BasePojo.java 文件的开头部分，包含 @TableField 注解。
画面4：在 IntelliJ IDEA 中，项目结构视图中选中 pojo 包，准备创建或查看相关类。
画面5：展示 User.java 文件内容，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 注解，以及 id、mobile、password 等字段。
画面6：展示 UserInfo.java 文件内容，包含 id、userId、nickName、logo、tags、sex、age、edu、city、birthday、coverPic、industry、income、marriage 等字段。
画面7：展示 BasePojo.java 文件内容，包含 created 和 updated 两个 Date 类型字段，以及 @TableField 注解。
画面8：展示 day01 项目文档中 3.5.3 MyMetaObjectHandler 节点，以及 MyMetaObjectHandler.java 文件的开头部分。
画面9：展示 MyMetaObjectHandler.java 文件内容，包含 insertFill 方法，用于在插入时自动填充 created 字段。
画面10：展示 MyMetaObjectHandler.java 文件内容，继续展示 insertFill 方法，用于在插入时自动填充 created 字段。
画面11：展示 MyMetaObjectHandler.java 文件内容，展示 updateFill 方法，用于在更新时自动填充 updated 字段。
画面12：在 IntelliJ IDEA 中右键点击 MyMetaObjectHandler.java，弹出菜单，选中“Show in Explorer”选项。
画面13：展示 BaseMapper.java 文件内容，包含 delete、deleteBatchIds、updateById、update 等方法的 Javadoc 注释。
画面14：展示 MyApplication.java 文件内容，包含 @MapperScan 注解和 SpringBootApplication 注解，以及 main 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhua.sso.enums;

import com.baomidou.mybatisplus.core.enums.ILenum;

public enum SexEnum implements IEnum<Integer> {
    MAN(1, "男"),
    WOMAN(2, "女"),
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

画面3：
```java
package com.tanhua.sso.pojo;

import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.annotation.TableField;
import java.util.Date;

public abstract class BasePojo {
    @TableField(fill = FieldFill.INSERT) //自动填充
    private Date created;
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private Date updated;
}
```

画面5：
```java
package com.tanhua.sso.pojo;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class User extends BasePojo {
    private Long id; //手机号
    private String mobile; //密码，json序列化时忽略
}
```

画面6：
```java
package com.tanhua.sso.pojo;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserInfo extends BasePojo {
    private Long id;
    private String userId; //用户ID
    private String nickName; //昵称
    private String logo; //用户头像
    private String tags; //用户标签，多个用逗号分隔
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

画面7：
```java
package com.tanhua.sso.pojo;

import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.annotation.TableField;
import java.util.Date;

public abstract class BasePojo {
    @TableField(fill = FieldFill.INSERT) //自动填充
    private Date created;
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private Date updated;
}
```

画面8：
```java
package com.tanhua.sso.handler;

import com.baomidou.mybatisplus.core.handlers.MetaObjectHandler;
import org.apache.ibatis.reflection.MetaObject;
import org.springframework.stereotype.Component;

@Component
public class MyMetaObjectHandler implements MetaObjectHandler {
```

画面9：
```java
@Override
public void insertFill(MetaObject metaObject) {
    Object created = getFieldValByName("created", metaObject);
    if (null == created) {
        //字段为空，可以进行填充
        setFieldValByName("created", new Date(), metaObject);
    }
}
```

画面10：
```java
Object updated = getFieldValByName("updated", metaObject);
if (null == updated) {
    //字段为空，可以进行填充
    setFieldValByName("updated", new Date(), metaObject);
}
```

画面11：
```java
@Override
public void updateFill(MetaObject metaObject) {
    Object updated = getFieldValByName("updated", metaObject);
    if (null == updated) {
        //字段为空，可以进行填充
        setFieldValByName("updated", new Date(), metaObject);
    }
}
```

画面13：
```java
int delete(@Param(Constants.WRAPPER) Wrapper<T> wrapper);
//删除（根据ID删除记录）
@Param idList 主键ID列表(不能为 null 以及 empty)
int deleteBatchIds(@Param(Constants.COLLECTION) Collection<? extends Serializable> idList);
//根据 ID 修改
@Param entity 实体对象
int updateById(@Param(Constants.ENTITY) T entity);
//根据 whereEntity 条件，更新记录
@Param entity 实体对象（set 条件值，可以为 null），@Param updateWrapper 实体对象封装转换类（可以为 null，且的 entity 用于生成 where 条件）
int update(@Param(Constants.ENTITY) T entity, @Param(Constants.WRAPPER) Wrapper<T> updateWrapper);
```

画面14：
```java
package com.tanhua.sso;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan("com.tanhua.sso.Mapper") //设置 Mapper 接口的扫描包
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：PPT标题为“3.5.2. User, UserInfo”，内容为 BasePojo.java 文件的开头部分。
画面8：PPT标题为“3.5.3. MyMetaObjectHandler”，内容为 MyMetaObjectHandler.java 文件的开头部分。
画面14：PPT标题为“3.5.5. MyApplication”，内容为 MyApplication.java 文件的开头部分。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

