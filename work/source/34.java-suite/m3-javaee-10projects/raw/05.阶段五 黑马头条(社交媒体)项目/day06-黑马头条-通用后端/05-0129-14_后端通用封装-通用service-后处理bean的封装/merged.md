# 14_后端通用封装-通用service-后处理bean的封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\14_后端通用封装-通用service-后处理bean的封装【海量资源尽在 666java.com】.mp4
- 时长 6分31秒（音频 391s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们就继续写这个后续的变这个咱们来看一下咱们首先在这写一个do filter这个filter没有咱们就创建出来filter它需要传什么参数它需要传的是第一个是创建的一个dto然后第二个是一个名称这个名称咱们叫list好吧list因为目前的话咱们都是啥呢我们目前是查询的是列表如果说你要是修改咱们是update
[00:29] 好吧就是这么一个思路啊要删除的话那就是deleteok行那咱们下面就来去完成当前的一个do filter那这方法没有是吧没有的话就创建出来来那这个方法里边啊方法里边该怎么去写呢首先呢我们应该先去拿到当前的这种后处理后处理这个bin那后处理的bin咱们有吗来看一下啊这个是不是有一个叫bin common filter是不是它呀
[00:59] 这个呢其实就是一个后处理病的一个接口那目前的话呢它呢是没有的它是这个接口啊所以说啊咱们要去拿的时候呢咱们应该是从它的实现类中去取那这实现类什么时候有呢其实谁去想做扩展或谁想去做后处理那谁就去实现当前这个接口那这接口啊你的实现类啊必然要去放哪啊要去放到它的什么死分容器中
[01:27] 所以说咱们在这直接就可以写就可以干嘛呢就可以通过当前死人的容器中去获取当前的数据咱们在这再去加一个东西不加也行加上吧咱们就跟笔记中一样在这再去封装一个方法往上看我已经没找到在这咱们又去封装了一个方法咱们在这就写一下好这个就是一个什么就是find filter好
[02:01] 这个参数呢就是DTO然后它最终返回的呢就是当前的什么Pace Common FilterPace Common Filter然后这个呢就是Pace Common Filter就它那这个方法没有咱们就串联出来啊这个呢主要呢就是从指纹容器中去获取当前的什么filter好那这个那这个你要想去获取容器呢咱们首先呢得先去先去输入
[02:32] 给在在当前的一种啊去注入一个application在这啊咱们在上面再去注入一个吧在这privateapplicationcontext好吧叫context注入一下这时候呢咱们就可以拿到了啊往下走走走走走在这啊在这嗯然要去拿他的时候呢咱们需要先去判断一下所以说咱们先去拿到他的一个名称
[03:02] 咱们是按照名称去到词本容器中去查找所以说呢这个名称啊咱们在去写的时候呢咱们可以这样写get name就是当前的表名就是当前的表名啊行那这时候呢咱们就可以判断了按当前这个容器中context是否包含了当前这个binbin就是name然后呢咱们就可以如果说包含啊咱们就直接
[03:35] context.setbin然后第一个呢就是name第二个呢就是base column-filter.classOK那这样返回了啊没有的话咱们就直接return一个none好吧那这个咱们就算设置完了那你说这东西老师现在咱们也没放啊那什么时候放呢我再说一遍啊这个呢是一个后处理的一个bin是吧
[04:02] 那当你去调用完List之后我还想去做些其他业务的话呢比如说你查询List啊咱们可以再去找写一个类去实现当前这个Base Common Filter这时候呢容器中才有有的时候呢在这儿就能找得着那找得着的话咱们就在这儿就可以去处理那具体处理哪个呢这时候呢你就可以拿到这里边啊比如说你拿到了它Base它不等于呢然后呢咱们就可以去处理
[04:34] 具体的方法处理机体的方法啊那就那这个方法怎么处理呢咱们可以在这啊就看一看一下前那个name name啊这不是list啊这name啊你有可能list会调用那个update delete还有什么其他的不会调用这个啊都会调用当前那个do filter啊所以说咱们在这啊写写什么呢写什么呢insert.requels如果说他是啥呢他是当前新增这时候呢
[05:04] 我们就去调什么呢discolumn.r有一个叫do insert after这里边第一个参数呢是当前的用户用户没有的话呢在这啊先去拿到用户啊用户怎么拿adminstribe local.users.get user就是拿到了当前的user这时候呢我们就可以把当前那个get user放进去
[05:35] 第二个参数呢就是DTO好吧这时候呢咱们就算是做完了啊分别的咱们再去写四个啊写三个这是啥呢这是update这是update好了然后这个呢比如说叫list这啥呢是to list after然后这个呢是一个delete这时候呢咱们就是delete好吧那这样的话咱们这个方法就算是设置完了
[06:11] list里边咱们也调用了好吧当然目前的话并没有处理任何东西因为咱们当前这个base common filter并没有任何的实现类后期咱们业务增加的时候咱们会实现这个方法来去找具体的业务去做好吧行那这个咱们这个do filter咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中，演示如何在 CommonServiceImpl 类中实现一个通用的分页和条件查询过滤器，通过动态获取 BaseCommonFilter 实例并根据操作类型（insert/update/list/delete）调用其对应方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CommonServiceImpl.java 文件中 doFilter 方法的末尾，返回 ResponseResult.okResult(map)。代码中可见 List<?> list = null 的声明。
画面 2: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter(dto, list) 调用和 return ResponseResult.okResult(map)。
画面 3: 展示 Typora 中的课程大纲，当前章节为“6.2.1 MODEL 实例”，内容涉及通用分页和条件查询的实现。
画面 4: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter(dto, list) 调用和 return ResponseResult.okResult(map)。
画面 5: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 import 语句和 @Service 注解，以及 public class CommonServiceImpl implements CommonService 的类定义。
画面 6: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter 方法和 getWhere 方法的开头部分。
画面 7: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 findFilter 方法的开头部分，以及 getWhere 方法中 if(dto.getWhere() != null) 的条件判断。
画面 8: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 findFilter 方法中 String name = dto.getTableName() 的赋值语句。
画面 9: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 findFilter 方法中 if(context.containsBean(name)) 的条件判断。
画面 10: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 findFilter 方法中 return context.getBean(name, BaseCommonFilter.class) 的返回语句。
画面 11: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter 方法中 if(baseCommonFilter != null) 的条件判断。
画面 12: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter 方法中 if("insert".equals(name)) 的条件判断。
画面 13: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter 方法中 if("update".equals(name)) 的条件判断。
画面 14: 展示项目结构，选中 CommonServiceImpl.java 文件。代码中可见 doFilter 方法中 if("list".equals(name)) 的条件判断。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
List<?> list = null
```

画面 2:
```java
//后处理han
doFilter(dto, list);
return ResponseResult.okResult(map);
```

画面 3:
```markdown
6.2.1 MODEL 实例
```

画面 4:
```java
//后处理han
doFilter(dto, list);
return ResponseResult.okResult(map);
```

画面 5:
```java
import com.heima.admin.Service.impl.commilter.BaseCommonFilter;
import com.heima.model.admin.dtos.CommonDto;
import com.heima.model.common.dtos.ResponseResult;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@KpressEarnings("all")
public class CommonServiceImpl implements CommonService {
```

画面 6:
```java
private void doFilter(CommonDto dto, String list) {
```

画面 7:
```java
private BaseCommonFilter findFilter(CommonDto dto) {
    String name = dto.getTableName();
    if (context.containsBean(name)) {
```

画面 8:
```java
private BaseCommonFilter findFilter(CommonDto dto) {
    String name = dto.getTableName();
    if (context.containsBean(name)) {
```

画面 9:
```java
private BaseCommonFilter findFilter(CommonDto dto) {
    String name = dto.getTableName();
    if (context.containsBean(name)) {
```

画面 10:
```java
private BaseCommonFilter findFilter(CommonDto dto) {
    String name = dto.getTableName();
    if (context.containsBean(name)) {
        return context.getBean(name, BaseCommonFilter.class);
    }
    return null;
}
```

画面 11:
```java
private void doFilter(CommonDto dto, String name) {
    BaseCommonFilter baseCommonFilter = findFilter(dto);
    if (baseCommonFilter != null) {
```

画面 12:
```java
private void doFilter(CommonDto dto, String name) {
    BaseCommonFilter baseCommonFilter = findFilter(dto);
    if (baseCommonFilter != null) {
        if ("insert".equals(name)) {
            baseCommonFilter.doInsertAfter(adUser, dto);
        }
    }
}
```

画面 13:
```java
private void doFilter(CommonDto dto, String name) {
    BaseCommonFilter baseCommonFilter = findFilter(dto);
    if (baseCommonFilter != null) {
        if ("insert".equals(name)) {
            baseCommonFilter.doInsertAfter(adUser, dto);
        }
        if ("update".equals(name)) {
            baseCommonFilter.doUpdateAfter(adUser, dto);
        }
    }
}
```

画面 14:
```java
private void doFilter(CommonDto dto, String name) {
    BaseCommonFilter baseCommonFilter = findFilter(dto);
    if (baseCommonFilter != null) {
        if ("insert".equals(name)) {
            baseCommonFilter.doInsertAfter(adUser, dto);
        }
        if ("update".equals(name)) {
            baseCommonFilter.doUpdateAfter(adUser, dto);
        }
        if ("list".equals(name)) {
            baseCommonFilter.doListAfter(adUser, dto);
        }
        if ("delete".equals(name)) {
            baseCommonFilter.doDeleteAfter(adUser, dto);
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“6.2.1 MODEL 实例”，内容涉及通用分页和条件查询的实现。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

