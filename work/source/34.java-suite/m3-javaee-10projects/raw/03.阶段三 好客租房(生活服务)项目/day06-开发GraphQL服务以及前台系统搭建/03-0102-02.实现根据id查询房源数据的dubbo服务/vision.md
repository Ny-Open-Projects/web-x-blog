# 画面线理解：02.实现根据id查询房源数据的dubbo服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\02.实现根据id查询房源数据的dubbo服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:56, 01:10, 01:29, 01:42, 01:50, 02:04, 02:29, 02:40, 02:54, 03:15, 03:24, 03:38, 03:50, 04:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:06:18

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
画面 13: 展示 PDF 文档，内容为“1.2、引入graphql-java依赖”，但未显示具体依赖配置。
画面 14: 展示 PDF 文档，内容为“1.2、引入graphql-java依赖”，但未显示具体依赖配置。

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
package cn.itcast.haoke.dubbo.server.service.impl;

import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.service.HouseResourcesService;
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
标题：1.2、引入graphql-java依赖
内容：未显示具体依赖配置。

画面 14:
标题：1.2、引入graphql-java依赖
内容：未显示具体依赖配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
