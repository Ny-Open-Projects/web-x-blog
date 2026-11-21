# 02.实现根据id查询房源数据的dubbo服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\02.实现根据id查询房源数据的dubbo服务【海量资源尽在 ubkz.com】.mp4
- 时长 4分4秒（音频 244s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来使用GrabQL来开发我们的房源的接口那么在前面呢我们也说过啊就是这个房源的接口开发呢
[00:11] 我们会涉及到两个接口的开发第一个呢就是根据ID去做一个查询第二个呢就是我们查询房源的一个列表OK那么其实在我们前面在做double服务实现的时候啊我们并没有去写这个根据ID去做查询这样的一个接口服务所以接下来我们首先要去做的呢就是实现
[00:31] 根据ID去查询的这样的一个double的一个服务注意是double的服务OK那么在我们后面去做一些这个开发的时候我们将会涉及到WebQ跟我们的Spring Boot整合的一个这个知识这个点需要我们到后面的时候特别要注意一下OK好那么我们首先先把这个给他先做完这个功能比较简单我们就快速的来做一下
[00:56] 那么我们找到我们的工程这个工程下面我们首先找到我们的是 interface对吧那么在 interface 下面我们去定义一个接口中定义一个方法那么就在这个下面对吧然后我们来定义一个方法好那么下面我们定义一个返回值那就是这个 host 什么 resource叫做 query host resource by 什么 id 对吧然后我们给他传递一个参数就叫 id
[01:26] 然后我们去给他写一个注释这个就叫根据ID查询我们的房源数据OK好嘞那么这个就搞定那么下面我们就需要在这个Service下面这个工程下面是不是找到具体对应的实现类然后在这个里面去做一个具体的实现然后把这个方法给他创建出来那么在这个方法里面我们将调用我们具体的业务的Service是不是去做一个实现那么所以我们就调用this.
[01:56] house resource Service.是不是就叫queryhouse resource by id然后把 id给他传递过去那么接下来我们就需要在Service中是不是做一个定义那么首先先进入他的接口在接口中去做这样的一个定义好嘞那么这样去写是不是就根据房源房源 id查询房源的一个数据ok
[02:25] 好那么这样的话我们接口是不是定义好了那么接下来呢我们将进入的是这个接口它的一个实现类那么我们进入这个resource在这那么在这个里面呢我们将去那么在这个里面呢我们是不是做一个具体的一个实现那么我们在这呢来给它去去实现它的一个方法ok
[02:49] 好那么在这个里面呢我们其实要用它的serverserver的query by d那么这样的话我们其实就实现了那么在这个里面呢有一个小的一个细节呢就是在我们之前写这个代码的时候我们在这个位置并没有去指定这个范形的t
[03:06] 那么如果你不指定的话那么他就会在这个位置会报一个类型转换一个错误那么如果你做一个强转他也是没有问题的但是这样的太麻烦了所以我们统一的是在上面这个位置我们给他去做一个范型定义那么就说 t就是base Service中 t他就是我们的所指定的house resource
[03:27] 那么这样的话我们查询到了这个t对吧你看这个里面反复这个t那么类型就已经指定好了就不需要做一个强转好嘞那么现在我们是不是已经把这个接口服务就已经搞定了注意这个接口服务仅仅是什么服务是double的服务对吧ok好我们来看一下首先第一接口然后我们去做一个接口的实现然后我们去编写具体的业务的一个Service
[03:50] 调用它就可以了那么在这个里面有个小的细节就是刚刚我们所说的这个范形这个一定要注意好嘞那么关于我们根据这个ID去查询房源的这个double的服务我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在基于 Dubbo 的房屋资源管理系统中，通过实现接口方法来完成分页查询和根据 ID 查询房屋资源的功能，并涉及 GraphQL 接口的定义与实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: IDE 主界面，显示项目结构，当前无代码编辑。
画面 2: 展示项目结构，定位到 `ApiHouseResourcesService` 接口，其中包含 `queryHouseResourcesList` 和 `queryHouseResourcesById` 方法。
画面 3: 展示 `ApiHouseResourcesService` 接口的详细方法签名，包括分页查询和根据 ID 查询的注释。
画面 4: 在项目结构中，定位到 `itcast-haoke-dubbo-server` 模块下的 `src/main/java` 目录。
画面 5: 展示 `ApiHouseResourcesServiceImpl` 类，其中 `queryHouseResourcesById` 方法返回 `null`。
画面 6: 在 `queryHouseResourcesById` 方法中，将返回值改为调用 `this.houseResourcesService.queryHouseResourcesById(id)`。
画面 7: 展示项目结构，定位到 `itcast-haoke-dubbo-server` 模块下的 `src/main/java` 目录。
画面 8: 展示 `HouseResourcesServiceImpl` 类中 `queryHouseResourcesList` 方法的实现，使用 `QueryWrapper` 进行分页查询。
画面 9: 展示 `queryHouseResourcesById` 方法的实现，调用 `super.queryById(id)`。
画面 10: 在 `saveHouseResources` 方法中添加了对标题为空的校验逻辑。
画面 11: 展示 `HouseResourcesServiceImpl` 类的完整代码，包括导入包和类定义。
画面 12: 展示 PDF 文档，内容为“1.1.1、定义接口方法”，其中包含 `queryHouseResourcesById(Long id)` 方法的注释。
画面 13: 展示 PDF 文档，内容为“1.2、引入GraphQL-java依赖”，但未显示具体依赖配置。
画面 14: 展示 PDF 文档，内容为“1.2、引入GraphQL-java依赖”，但未显示具体依赖配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
/**
 * 分页查询房源列表
 * @param page 当前页
 * @param pageSize 页面大小
 * @param queryCondition 查询条件
 * @return
 */
PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize,
                                                 HouseResources queryCondition);

/**
 * 根据id查询房源数据
 * @param id
 * @return
 */
HouseResources queryHouseResourcesById(Long id);
```

画面 3:
```java
/**
 * 分页查询房源列表
 * @param page 当前页
 * @param pageSize 页面大小
 * @param queryCondition 查询条件
 * @return
 */
PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize,
                                                 HouseResources queryCondition);

/**
 * 根据id查询房源数据
 * @param id
 * @return
 */
HouseResources queryHouseResourcesById(Long id);
```

画面 4:
```java
itcast-haoke-dubbo-server
├── src
│   └── main
│       └── java
│           └── cn.itcast.haoke.dubbo.server
│               └── api
│                   └── ApiHouseResourcesService
```

画面 5:
```java
public class ApiHouseResourcesServiceImpl implements ApiHouseResourcesService {

    @Autowired
    private HouseResourcesService houseResourcesService;

    @Override
    public int saveHouseResources(HouseResources houseResources) {
        return this.houseResourcesService.saveHouseResources(houseResources);
    }

    @Override
    public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources queryCondition) {
        return this.houseResourcesService.queryHouseResourcesList(page, pageSize, queryCondition);
    }

    @Override
    public HouseResources queryHouseResourcesById(Long id) {
        return null;
    }
}
```

画面 6:
```java
@Override
public HouseResources queryHouseResourcesById(Long id) {
    return this.houseResourcesService.queryHouseResourcesById(id);
}
```

画面 7:
```java
itcast-haoke-dubbo-server
├── src
│   └── main
│       └── java
│           └── cn.itcast.haoke.dubbo.server
│               └── api
│                   └── ApiHouseResourcesService
```

画面 8:
```java
@Override
public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources queryCondition) {
    QueryWrapper queryWrapper = new QueryWrapper();
    // 根据数据的更新时间倒序排序
    queryWrapper.orderByDesc("_columns: \"updated\"");

    IPage iPage = super.queryPageList(queryWrapper, page, pageSize);

    return new PageInfo<HouseResources>(Long.valueOf(iPage.getTotal()).intValue(), page, pageSize, iPage.getRecords());
}
```

画面 9:
```java
@Override
public HouseResources queryHouseResourcesById(Long id) {
    return super.queryById(id);
}
```

画面 10:
```java
if (StringUtils.isBlank(houseResources.getTitle())) {
    return -1;
}
return super.save(houseResources);
```

画面 11:
```java
package cn.itcast.haoke.dubbo.server.Service.impl;

import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.Service.HouseResourcesService;
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class HouseResourcesServiceImpl extends BaseServiceImpl<HouseResources> implements HouseResourcesService {

    @Override
    public int saveHouseResources(HouseResources houseResources) {
        // 添加校验或者其他的一些逻辑
        return super.save(houseResources);
    }

    @Override
    public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources queryCondition) {
        QueryWrapper<HouseResources> queryWrapper = new QueryWrapper<>();
        // 根据数据的更新时间倒序排序
        queryWrapper.orderByDesc("updated");

        IPage<IPage> iPage = super.queryPageList(queryWrapper, page, pageSize);

        return new PageInfo<HouseResources>(Long.valueOf(iPage.getTotal()).intValue(), page, pageSize, iPage.getRecords());
    }

    @Override
    public HouseResources queryHouseResourcesById(Long id) {
        return super.queryById(id);
    }
}
```

画面 12:
```java
/**
 * 根据id查询房源数据
 * @param id
 * @return
 */
HouseResources queryHouseResourcesById(Long id);
```

画面 13:
```java
@Override
public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources queryCondition) {
    QueryWrapper queryWrapper = new QueryWrapper();
    // 根据数据的更新时间倒序排序
    queryWrapper.orderByDesc("_columns: \"updated\"");

    IPage iPage = super.queryPageList(queryWrapper, page, pageSize);

    return new PageInfo<HouseResources>(Long.valueOf(iPage.getTotal()).intValue(), page, pageSize, iPage.getRecords());
}

@Override
public HouseResources queryHouseResourcesById(Long id) {
    return super.queryById(id);
}
```

画面 14:
```java
@Override
public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources queryCondition) {
    QueryWrapper queryWrapper = new QueryWrapper();
    // 根据数据的更新时间倒序排序
    queryWrapper.orderByDesc("_columns: \"updated\"");

    IPage iPage = super.queryPageList(queryWrapper, page, pageSize);

    return new PageInfo<HouseResources>(Long.valueOf(iPage.getTotal()).intValue(), page, pageSize, iPage.getRecords());
}

@Override
public HouseResources queryHouseResourcesById(Long id) {
    return super.queryById(id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12:
标题：1.1.1、定义接口方法
内容：在 `itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface` 中定义接口方法 `queryHouseResourcesById(Long id)`。

画面 13:
标题：1.2、引入GraphQL-java依赖
内容：未显示具体依赖配置。

画面 14:
标题：1.2、引入GraphQL-java依赖
内容：未显示具体依赖配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

