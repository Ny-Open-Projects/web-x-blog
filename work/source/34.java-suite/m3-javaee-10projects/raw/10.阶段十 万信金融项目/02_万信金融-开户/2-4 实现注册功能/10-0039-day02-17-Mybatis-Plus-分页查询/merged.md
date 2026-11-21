# day02-17-Mybatis-Plus-分页查询

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-17-Mybatis-Plus-分页查询_【海量资源尽在 666java.com】.mp4
- 时长 7分55秒（音频 475s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们给大家介绍了一个MP当中的条件勾到器这一块是一个重点内容当然我们举的例子都是以查询为例的将来你在进行修改和删除的时候如果也需要带条件那么道理都是一样的大家注意看因为它里边提供了一个delete的方法和一个update的方法这两个方法你看它后边是不是都是要一个Warp对象是不是因为我们也可以根据条件来进行更新操作或者删除操作嘛那跟查询一样你把这个条件封上了Warp对象里面
[00:30] 把这个对象扔给delete的话扔给update的方法就可以实现带条件的修改和什么呀删除操作这个呢我们今天不再演示了你有兴趣可以自己试一试我们后边用到的时候再说那接下来的话咱们要给大家讲一个也是重点的一个内容就是分线查询当然了这个东西对于大家来说也不陌生因为咱们前面在讲mybattles的时候呢也学习过这个分线查询
[00:57] 我们接下来看看MP当中的分页查询是怎么实现的首先MP给我们提供了一个方法叫SelectPage是专门用来实现分页查询的咱看一下这个方法的定义这个方法一共有两个参数大家看一下第一个参数就是IPage对象咱基本上能猜出来因为咱们之前学过分页查询这个对象一定是封装分页数据的比如说你要查询第几页数据
[01:27] 比如说一页要显示多少行数据这些值是不是应该是封装到这个对象里那第二个参考者是不是还是那个VARB对象是不是那当然了他肯定还是封装条件那也就是说呢咱这个MP提供的SLACK的配给方法是可以实现带条件的什么呀分解察觉的那有的学生会说老师我不需要带条件怎么办不需要带条件你第二个参考者给个NOW不就行了吗这不就是不带条件的分解察觉了对不对
[01:56] 然后这个的话反位值啊也是IP对不对这里边我们给你以往的经验它里边肯定封装了什么呀总记录说呀肯定封装了咱查出来的当前页的那个集合了是不是咱一般就是要这些数据的这是我们也知道啊MP提供了一个方法叫select配置专门实现这个分解查询那么在调这个方案之前呢我们还需要做一个配置加一个配置类搞一个B呢一个配置就是一个分解查件啊MP的一个分解查件
[02:27] 那这个呢我在这个咱这个入门案例当中其实已经提供过了啊在这这个类这个你也不用编写了你可以直接拿着用但是这个代码你也能看懂看到这个主页你应该知道咱这就是一个配置类嘛对不对啊然后配置类上需要加这个这个包扫描啊map 接口的这个包扫描然后呢里边呢核心代码就是这一块啊我们配置了一个 b 啊这个对象呢就是这个啊 intercept其实这个单词大家也认识是拦截器的意思
[02:58] 那我们提供这个对象干嘛这个对象呢就是分页的一个拦截器它有什么作用呢我简单跟大家说一说它的作用呢是在你进行分页查询的时候呢可以做一些前置或者说后置的一些一些自动化的一些工作就是不用我们管的一些工作比如说你的那些分页数据我们刚才说你是不是要把分页数据放到这里边这个数据它符合不符合规定对不对你比如说我要查第零页的数据
[03:28] 那就不合法了是不是像这种数据它会进行叫音它也就是查完之后它是不是要往这个IP对象里边进行封装这个封装这个事你也不用管你调完发之后直接就拿到这个对象它可以封装好像这些事情其实都有谁完成的对就是由这个拦截器完成所以说我们需要把这个拦截器给它作为B给它配好配好之后由MP这个框架自动去拿着用我们不用管所以说我们在进行分辨的时候需要先搞定这个事
[03:57] 这事搞定之后呢我们接下来就可以啊在测试类当中调用一下这个方法对不对演示一下分页的这个效果就像哦咱接下来的话还是在这个测试量当中啊再加一个测试方法演示这个分页上去public void test配置吧那这里边我们看讲义里边它是一个什么例子啊你看它是不是实现了一个带条件的分页查询
[04:32] 是不是年龄是大于什么样20岁的对不对然后呢这呢是封装分页的数据然后掉slag的配方进行带条件的分页查询然后我们接下来就写一下这个例子首先就是query对warp这个范形呢还是这个优越对象然后直接new对吧然后呢我们根据讲义的要求我们是不是封装了一个条件它是什么呀叫大于是不是
[05:03] 是年龄吧我记得啊年龄啊年龄大多少20岁GT啊20岁直接给个值就行我们就这一个条件啊这是条件封装号前面封装号之后我们进来是要封装这个什么呀分页的数据吗因为我跟大家说了swec配给这个方案就要这两个东西一个是条件咱已经有还有就是这个IP对象是不是就这个配对象那我们也是直接new一下配
[05:34] 看好这个配置别倒错包了我们要倒的是这个你看爆米豆是不是这是MP里边的一个配置对象啊他也需要范形U 是这儿那我们直接Nu啊Nu的时候呢我们是不是就把分页的这个数据给它封装进去了第一个参数表示第几页啊第二个参数表示一页显示多少行这个你说了算吧比如我想显示第一页的数据一页显示两可以吧这个你自己说了算
[06:04] 这数据就封装好封装好之后呢我们就可以调用Mapper的什么方法刚才说的叫叫SEECT这个是什么呀配给是不是然后先把这个配给对象给他扔进去然后再把这个对对象给他扔进去这就搞定啊搞定什么呀搞定带条件的分页查询然后他返回的是一个什么东西呀反而是一个IP的这样一个
[06:36] 一个一个对象啊我们接收一下就行了我们跟讲义保持一致吧是不是那然后呢这个这个IP里边都封装了啥都封装啥你可以看一下它的原码吗你看这不是我们应该能看出来这不就是我们查出来的那个当前一样的那个集合吗这不是总记录说吗是不是其他咱不用管咱其实用这两个就够了那他应该有给他三个方法了是不是你看讲义
[07:06] 是不是get total啊get配积啊对吧这是总条数啊这是总页数啊然后get records是不是那个集合这我就不再给大家敲了啊这些大家一看就明白是咋回事我们进来看效果就行好我们进来又执行一下啊应该是第一页几条两条是不是但是是20岁的啊超过超过20岁的是不是那这个我觉得大家下去给自己测试吧一共查出来五条是不是打印的在哪呢
[07:41] 目前是不是这这两条数据对吧也两条啊剩下的你可以自己改改这这两个值吧行不行大家自己改改自己测试测试就行这个就是我们给大家演示了一下MP当中的非验查询是如何实现

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 MyBatis-Plus 中配置分页插件并编写测试代码来验证分页功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 MyBatis-Plus 的分页查询文档，重点是 selectPage 方法的 JavaDoc 说明，包括参数 page 和 queryWrapper 的含义。
画面2: 在 IntelliJ IDEA 中打开 MyBatisPlusConfig.java 文件，展示配置分页插件的代码。
画面3: 展示 MyBatisPlusConfig.java 文件内容，包含 @Configuration 和 @MapperScan 注解，以及配置分页插件的方法。
画面4: 展示 MyBatisPlusConfig.java 文件内容，重点是 public PaginationInterceptor paginationInterceptor() 方法。
画面5: 展示 MyBatisPlusConfig.java 文件内容，光标位于方法结束处。
画面6: 展示 TestUserMapper.java 文件内容，光标位于 QueryWrapper 类的定义处。
画面7: 展示 TestUserMapper.java 文件内容，光标位于 QueryWrapper 类的 getSqlSelect 方法处。
画面8: 展示 MyBatis-Plus 的分页查询文档，包含多个服务模块的截图，以及测试代码中的 System.out.println("user = " + user);。
画面9: 展示 TestUserMapper.java 文件内容，包含 testOrderBy 和 testPage 方法的代码。
画面10: 展示 TestUserMapper.java 文件内容，光标位于 userMapper.selectPage(page, queryWrapper); 方法调用处。
画面11: 展示 MyBatis-Plus 的分页查询文档，包含多个服务模块的截图，以及测试代码中的 System.out.println("user = " + user);。
画面12: 展示 TestUserMapper.testPage() 方法的运行结果，显示“总页数：2”和“总数据：5”。
画面13: 展示 TestUserMapper.testPage() 方法的运行日志，显示 SQL 查询语句和参数。
画面14: 展示 TestUserMapper.testPage() 方法的运行结果，显示“总页数：2”和“总数据：5”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
/**
 * 根据 entity 条件，查询全部记录（并翻页）
 * @param page 分页查询条件（可以为 RowBounds.DEFAULT）
 * @param queryWrapper 实体对象封装操作类（可以为 null）
 * @return
 */
IPage<T> selectPage(IPage<T> page, @Param(Constants.WRAPPER) Wrapper<T> queryWrapper);
```

画面2:
```java
package cn.itcast.mp;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan("cn.itcast.mp.Mapper")
public class MybatisPlusConfig {
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
}
```

画面3:
```java
package cn.itcast.mp;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Bean;

@Configuration
@MapperScan("cn.itcast.mp.Mapper")
public class MybatisPlusConfig {
    /**
     * 分页插件
     */
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
}
```

画面4:
```java
package cn.itcast.mp;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Bean;

@Configuration
@MapperScan("cn.itcast.mp.Mapper")
public class MybatisPlusConfig {
    /**
     * 分页插件
     */
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
}
```

画面5:
```java
package cn.itcast.mp;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Bean;

@Configuration
@MapperScan("cn.itcast.mp.Mapper")
public class MybatisPlusConfig {
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
}
```

画面6:
```java
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.Assert;
import org.springframework.util.CollectionUtils;
import org.springframework.util.StringUtils;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestScope

