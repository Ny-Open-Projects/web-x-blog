# 6.12 实时数据查询 - 开发Service程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.12 实时数据查询 - 开发Service程序_【海量资源尽在 666java.com】.mp4
- 时长 13分48秒（音频 828s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面我们来看一看我们这个代码的一个具体的一个实践我们来开发我们的servicemessage Service和message Service rmpl那么message Service里边我们要查询的是我们的实时数据这个表里边的数据我要给它查询出来同时按照分页来进行查询OK那么我们来开发我们的代码那首先的话我们要定义一个一个Service定义一个接口而这个接口的话接口里边会根据查询条件
[00:31] 来根据我们传输的参数来查询我们的分页分页的数据那么我们这个Service的名字其实就叫做com.itfema.code.monitor下面的Service这个包里边的我们把它叫做messageservice那么这个接口呢它需要attend我们的iService
[01:09] 它extend iService之后我们这个数据类型呢就是message entityOK那此时我们的这个数据这个接口它就已经现在包含了一些方法这个方法的话实际上是继承自我们的iService而这个iService里边的是我们MafiaDiskPlus里边的一个类这个一个接口包含了我们的增传感察是针对单表的增传感察
[01:38] 那么我们在我们这个工程里边我们需要查询我们的query message realtime我们要返回我们查询查询的时候我们要查询我们的传入参数而这个参数的话是一个string和一个object object类型okpair我们把参数传过来然后我们的rpg它的返回结果是一个rpg对吧这个rpg也是mybdxplus里边的那么下面
[02:23] 我们来开发我们这个Service的一个具体实现一个javamessage Service rmp rmp我们把它移到我们的这个包里边rmp我们把这个移到这个包里边去而这个的话它会实现我们这个Service这个接口
[02:59] 同时呢它还要实现我们的另外一个叫做serviceRMPL我们的这个serviceRMPL而这个Service的RMPL也是MavitisPlus里面的一个接口那么它是message.和我们的message.
[03:33] 但是他extend的这个serviceimpl然后要实现我们的这个message Service对不对这是我们在我们这个message serviceimpl这个方法里边那下一步我们把它这个类给它复写一下而这个类的话就是query message的readtimeok那此时我们可以看到我们在Service的message serviceimpl里边我们
[04:10] 实现了我们的这个接口定义的方法同时它还继承了我们的Service rmpl也就是说mybid is plus里Service rmpl的这个这个类那下一步我们就来开发我们的这个实体那么首先第一点来讲的话我们要组装组装查询条件是吧那下面来讲的话我们组装完查询条件之后
[04:43] 我要进行一个查询然后查询之后就返回我们的这个结果对吧那么返回结果我们可以看到我们当前因为它本身是已经实现了一些方法了我们返回这个配置而这个配置这个类似的话其实当前我们的这个类这个类里边已经实现了一些方法中间就有一个配置方法这配置方法的话我们可以new一个配置new配置的话这个配置类型是一个message
[05:19] 那下面的话是查询分页的数量假设是这个10条然后呢查询当前的页数是一个current是第一页size的话是第10条的那在这种情况下的话我们还能有个查询条件这个查询条件
[05:55] 而我们看一看这个查询条件其实就是一个wrapper对不对这个ipage里面的这个这个配置的类这个方法它的第三个查询条件是我们的queryquerywrapper实际上是一个wrapper也就是说我在这里边我要定义一个我们的querywrapper这querywrapper的话就是query我们要定义我们的querywrapper这querywrapper我们等于空
[06:28] 我回头我再给它设置上那么我们在这里边就是query wrapper这个就是我们的一个查询但是这个地方其实是稍微有点点问题的而这个问题在哪呢比如说在这儿我们的current timecurrent当前的页数其实是我们设定了是1和10而此时呢我们这个当前的页数和每页显示的数显示的数据我们是从前台来查询过来的所以说我要
[06:58] 给他定义啊从前台拿到的一个结果配置等于什么呢等于我们的Pyram.get我们get前台传过来的数据是叫配置然后我们把它改成.toDream对吧那么但是我们分页的页数它是一个呃它是一个int型的那我在这里边就把它转换一个int就把它转化成
[07:38] 一个字符型的转化成一个数字型的那么这个时候我们就可以用了配置了对不对那再一个size的话size一样也是前台传过来的数据那么当前的页数等于我们同样道理一样的integer.value25value25parameter我们全部参数参数的我们要获得获得我们的配置size
[08:12] 是吧我们toString因为它这个它这个object类型的那此时我们就把它放到我们的size里边OK没问题对不对我们当前这个分页查询那么它查询呢是按照我们的当前页数和一页有多少有多少个数量也就是说有多少个数量然后来查询按照这个查询条件来查询得到的一个结果而这个结果呢其实是一个message
[08:42] 这种类型的每一条数据都是这个类型的那下一步最重要的就是我们要创建我们的组装我们的查询条件了那这个查询条件我们可以单独的写一个方法那我们可以单独写一个方法而这个方法的话其实就是我们的这个比如说我们的privateprivatequerywrapper我要返回这个querywrapper对不对那么我要get
[09:16] message也是查询的参数参数的话是一个map对吧map的我们的里边类型是string和我们的这个object然后parameter那此时我们要我们定义一个定义一个这个query wrapperquery wrapper然后它的类型是message
[09:56] query wrapper等于new query wrapperOK那么我们再把它返回过来那此时我们就定义了这样的一个这个方法而这个方法呢我们就可以在这儿再用了对吧那所以说我们开发这个程序的时候它也是一层一层递进的我先想好这个结构是什么那么想好结构之后呢我的里边的程序我就可以把它封装上
[10:43] 那但是现在这个情况我要封装我们的这个方法而这个方法就是我们要根据条件来查询而这个条件的话我先举几个例子第一个例子举几个例子第一个的话是说我们要根据我们的这个company id对不对stringstring company id我等于什么呢我等于parametergetcompanycompany
[11:17] 这是前台传过来的如果它等于空的情况下那么我们就让它等于空的情况下我们实际上就不给它做任何变化否则情况下我要让它改成一个get company id然后给它toString然后再trim这是我们的company id那么如果我们的company id
[11:59] 不等于空那么此时呢我们要把query wrapper给它加上一个EQ这个EQ就是我们的company id参数我们学过Mapetus PlusMapetus Plus的这个query wrapper它里边如果我们前台传过来的是一个company id而这个company id如果它不为空也就是说是
[12:38] 这个参数值是传给我的传给我的时候我需要把这个查询的构造器查询条件的构造器我要添加一个字段而这个字段就叫common id对不对common id的字段的值等于这个数据的一个先前传过来参数的值那么此时我要我就得到了这个query wrapper那同样道理我还可以再添加什么呢我还可以再添加其他的一些参数添加其他添加其
[13:12] 其他的参数那么天下其他完参数之后呢下一步的话我们就能够封装好了我们的当前的这个这个这个这个查询条件了而这个查询条件我们被我们的这个Service实际来使用了我们这个其他的查询条件可以有很多的这是我们开发我们的这个message Service这个具体的Service接口和具体的一个实现
[13:47] 这样的一个开发过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中，通过定义接口和实现类，使用 MyBatis-Plus 的 QueryWrapper 来构建动态分页查询条件。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构和启动类 MonitorApplication，其中包含 @SpringBootApplication 和 @EnableDiscoveryClient 注解。
画面 2: 定义服务接口 MessageService，继承自 IService。
画面 3: 在 MessageService 接口中添加方法 queryMessageRealtime，参数为 Map<String, Object>。
画面 4: 创建实现类 MessageServiceImpl。
画面 5: 在 MessageServiceImpl 中声明继承关系，并引入 MyBatis-Plus 的 ServiceImpl 和实体类。
画面 6: 在 MessageServiceImpl 中重写 queryMessageRealtime 方法，使用 Page 和 QueryWrapper。
画面 7: 在 queryMessageRealtime 方法中，使用 QueryWrapper 的构造函数创建对象。
画面 8: 在 queryMessageRealtime 方法中，从参数中提取 page 和 size，并设置到 Page 对象。
画面 9: 在 queryMessageRealtime 方法中，使用 Ctrl+Shift+空格 自动补全 QueryWrapper 的方法。
画面 10: 在 queryMessageRealtime 方法中，定义私有方法 getMessageCondition。
画面 11: 在 getMessageCondition 方法中，使用 QueryWrapper 的 eq 方法设置条件。
画面 12: 在 getMessageCondition 方法中，对参数 company_id 进行非空判断。
画面 13: 在 getMessageCondition 方法中，使用 QueryWrapper 的 eq 方法设置 company_id 条件。
画面 14: 在 getMessageCondition 方法中，完成条件设置并返回 QueryWrapper。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```java
package com.ithema;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class MonitorApplication {
    public static void main(String[] args) {
        SpringApplication.run(MonitorApplication.class, args);
    }
}
```

画面 2:
```java
package com.ithema.com.ithema.cold.monitor.Service;
import com.baidou.mybatplus.extension.Service.IService;
public interface MessageService extends IService {
}
```

画面 3:
```java
package com.ithema.com.ithema.cold.monitor.Service;
import com.baidou.mybatplus.extension.Service.IService;
import com.ithema.cold.common.netty.MessageEntity;
public interface MessageService extends IService<MessageEntity> {
    IPage queryMessageRealtime(Map<String, Object> params);
}
```

画面 4:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
public class MessageServiceImpl {
}
```

画面 5:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
}
```

画面 6:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        return this;
    }
}
```

画面 7:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        return this.page(new Page<MessageEntity>(1, 10), queryWrapper);
    }
}
```

画面 8:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
}
```

画面 9:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
}
```

画面 10:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
    private QueryWrapper getMessageCondition(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        return queryWrapper;
    }
}
```

画面 11:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
    private QueryWrapper getMessageCondition(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        String companyId = params.get("companyId") == null ? params.get("companyId").toString().trim() : "";
        return queryWrapper;
    }
}
```

画面 12:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.Service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
    private QueryWrapper getMessageCondition(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        String companyId = params.get("companyId") == null ? params.get("companyId").toString().trim() : "";
        if (companyId != null && !"".equals(companyId)) {
            queryWrapper.eq("company_id", companyId);
        }
        return queryWrapper;
    }
}
```

画面 13:
```java
package com.ithema.com.ithema.cold.monitor.Service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.Service.impl.ServiceImpl;
import com.ithema.cold.common.netty

