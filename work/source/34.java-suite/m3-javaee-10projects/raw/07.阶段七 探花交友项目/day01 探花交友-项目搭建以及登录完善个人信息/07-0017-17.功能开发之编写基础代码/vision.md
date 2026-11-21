# 画面线理解：17.功能开发之编写基础代码

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\17.功能开发之编写基础代码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 01:10, 01:47, 02:37, 03:41, 03:56, 04:20, 04:44, 05:28, 07:09, 07:48, 08:09, 08:38, 09:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:08:43

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

@MapperScan("com.tanhua.sso.mapper") //设置 mapper 接口的扫描包
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
