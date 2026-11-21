# 09_后端通用封装-后置增强接口BaseCommonFilter

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\09_后端通用封装-后置增强接口BaseCommonFilter【海量资源尽在 666java.com】.mp4
- 时长 5分34秒（音频 335s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就继续啊继续就再去说一下当前有一个看着笔记啊里边还有个类咱们要去设置就是当前一个base common filter那这个类呢刚才说了这个类呢主要的作用是啥呢可以往这看啊可以看下图这个类的作用呢主要就是可以设置一些后置的增强后置增强比如说你这持久化完之后呢我这块还可以再做一些其他的事那这个类呢咱们可以先定义出来好吧
[00:30] 目前咱们封装的话主要的是增伤改查增伤改查啊所以说咱们在这啊去定义的时候在那去啊因为咱们现在封装的都是admin所以说咱们在这啊在于定义一些东西咱们会在当前Service包下边按表里边啊再去加一个包名叫啥呢咱们叫common filter叫base common
[01:02] 是一个接口为什么要定义成接口呢为方便扩展如果说他有具体业务的话咱们可以根据不同的表或者不同的业务去实现当前的接口再去增强你的功能听明白吧好了啊行那后期呢咱们会用会用到啊咱们用到的时候可以再去细讲这个类大概的功能你要先知道好吧怎么写呢首先这个类你要知道干嘛的就是通用的通用过滤
[01:36] 过滤类那就是说后置类啊后置增强类好这里边呢是一个接口咱们是要去针对于不同的方法都要去做啊咱们首先都是一些什么呢list filterafter它是一些增长改查所以说咱们都要去考虑到啊条件啥呢条件的话咱们首先呢是要登录啊dd user所以说你要去传个user过来第二个呢
[02:05] 你的条件要传过来有可能我增强的时候需要用得着ok这三个两个特殊你要有好吧行那下面呢咱们可以去拷贝一下啊分别呢是比如说咱们是list分别还有什么呢upload还有insert还有关键的delete好吧那这四个方法给你完了啊这边其实还有两个方法我们可以看一下啊
[02:35] 这两个方法呢就是说它可以获取更新字段里面的值和获取查询字段里面的值那这个呢在接口中呢咱们可以定义一些默认的方法啊这样的话呢随或者说某一些类去实现当前是接口的时候呢咱们可以直接去使用这也算是抽取了抽取了当前的方法到当前的接口中啊咱们可以去写一下啊我现在是debunk然后呢咱们要去
[03:06] commonware返回的是commonware啊commonware DTO然后呢是findupdateDVALUE是啥呢这个值的话就是string一个什么field就与某一个某一个字段啊去查询那查呢common DTO种好他需要去实现出来啊好这个类啊咱们写一下啊类呢就是这个方法啊获取更新字
[03:40] 里面的值好吧行那下面咱们就来去写一下我现在来判断一下判断当前DTO等于等于不等于呢不等于呢然后这时候呢咱们就可以去拿值了复合循环复合循环的话是这样怎么复合循环呢DTO.set因为set是一个集合看到了吗这时候呢可以再去循环
[04:12] 这样的话就能拿到具体的一个值了啊cw啊行有我们叫cw啊然后就判断呗判断目前的fields.equals如果说你的cw.getfields是一样一样的话呢这时候咱们就可以直接return cw就可以了ok那这个咱们就算是做完了啊非常简单啊下面还有一个如果说你找不着的话怎么办呢找不着就return none就可以了好吧
[04:49] 行那这是一个我们再来写第二个第二个跟他类似啊其实也是去查找这是啥呢空心自转制要查询自转获取查询自转查询的话呢咱们在这啊就写翻译到where就可以了where那这个值是不变的值不变的这个不是set思量这是啥呀get where好这样的话我们就算是结束了好吧这个是
[05:18] 从当前的查询自断中去获取然后这个呢是从当前的更新自断中去获取当前某一个自断值好吧行那这个啊这个basecommon filter咱们就先说到这它就是一个后置增强的类

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解通用过滤器接口 BaseCommonFilter 的定义与实现，包括其方法签名、默认方法 findUpdateValue 的逻辑，以及相关类的结构和作用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了代码编辑器中 BaseCommonFilter 接口的默认方法 findUpdateValue 的实现，以及其上方的四个方法签名（doListAfter, doUpdateAfter, doInsertAfter, doDeleteAfter）。
画面 2: 展示了 PPT 页面“4.1 类图说明”，包含一个类图，图中显示了 CommonWhereDto、CommonDto、CommonService、CommonController 等类之间的继承和依赖关系，并附有各类的说明。
画面 3: 展示了 IDE 中 CommonWhereDto.java 文件的代码，定义了字段 filed、type 和 value。
画面 4: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 5: 展示了 PPT 页面，说明 BaseCommonFilter 接口用于定义过滤器的默认方法，支持后续扩展。
画面 6: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 7: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 8: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 9: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 10: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 11: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 12: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 13: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。
画面 14: 展示了 IDE 中 BaseCommonFilter.java 文件，正在编辑接口定义，下方弹出 Java 类型建议列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
void doListAfter(AdUser user, CommonDto dto);
void doUpdateAfter(AdUser user, CommonDto dto);
void doInsertAfter(AdUser user, CommonDto dto);
void doDeleteAfter(AdUser user, CommonDto dto);

/**
 * 获取表字段里面的值
 * @param field
 * @param dto
 * @return
 */
default CommonWhereDto findUpdateValue(String field, CommonDto dto) {
    if(dto!=null){
        for (CommonWhereDto cw : dto.getSets()){
            if(field.equals(cw.getFiled())){
                return cw;
            }
        }
    }
    return null;
}

/**
 * 获取表字段里面的值
 * @param field
 * @param dto
 * @return
 */
default CommonWhereDto findWhereValue(String field, CommonDto dto) {
```

画面 2:
```text
CommonWhereEnum: 用于定义表名枚举支持通用操作，及开发的CRUD功能
CommonWhereDto: 用于接收前端传入的字段名或者条件参数
CommonDto: 用于接收前端传入的SQL拼接实现（包括CRUD接口的参数）
CommonDao: 持久层实现CRUD的通用操作处理
CommonServiceImpl: 用于实现CRUD的通用逻辑处理
BaseCommonFilter: 定义后端处理的接口方法（后置增加的BeanName意义为CommonTableEnum名称）
```

画面 3:
```java
package com.heima.model.admin.dtos;

import lombok.Data;

@Data
public class CommonWhereDto {
    private String filed;
    private String type="eq";
    private String value;
}
```

画面 4:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.pojs.AdUser;
import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 5:
```java
/**
 * 通用过滤器到接收
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);

    /**
     * 获取表字段里面的值
     * @param field
     * @param dto
     * @return
     */
    default CommonWhereDto findUpdateValue(String filed, CommonDto dto) {
        if(dto!=null){
            for (CommonWhereDto cw : dto.getSets()){
                if(field.equals(cw.getFiled())){
                    return cw;
                }
            }
        }
        return null;
    }
}
```

画面 6:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 7:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 8:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 9:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 10:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 11:
```java
package com.heima.admin.Service.impl.comfilter;

import com.heima.model.admin.dtos.CommonWhereDto;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.admin.pojs.AdUser;

/**
 * 通用过滤的过滤类，后置增头
 */
public interface BaseCommonFilter {
    void doListAfter(AdUser user, CommonDto dto);
    void doUpdateAfter(AdUser user, CommonDto dto);
    void doInsertAfter(AdUser user, CommonDto dto);
    void doDeleteAfter(AdUser user, CommonDto dto);
}
```

画面 12:
```java
package com.heima

