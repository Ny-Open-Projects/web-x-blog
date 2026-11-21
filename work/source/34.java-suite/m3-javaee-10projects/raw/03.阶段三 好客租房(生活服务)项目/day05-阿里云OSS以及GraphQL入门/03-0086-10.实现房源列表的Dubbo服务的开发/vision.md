# 画面线理解：10.实现房源列表的Dubbo服务的开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\10.实现房源列表的Dubbo服务的开发【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:22, 02:47, 03:55, 04:54, 05:43, 07:15, 08:51, 10:39, 12:15, 12:58, 14:16, 15:23, 16:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:55:07

1) 这一组画面整体在讲什么（一句话）：
实现房屋资源列表服务的 Dubbo 接口定义、服务实现与服务注册。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PDF 文档，标题为“5. 房源列表服务”，并指出接下来要实现房源列表服务。同时显示了项目结构，当前位于“5.1、定义dubbo服务”。
画面 2: 显示 `ApiHouseResourcesService` 接口定义，包含 `saveHouseResources` 和 `queryHouseResourcesList` 方法。
画面 3: 显示 `PageInfo` 类的定义，包含 `total`、`pageNum`、`pageSize` 和 `records` 字段。
画面 4: 显示项目结构，突出 `PageInfo.java` 文件位于 `vo` 包下，并显示了 `@Data` 注解的 `PageInfo<T>` 类定义。
画面 5: 显示 `HouseResourcesServiceImpl` 类，实现了 `saveHouseResources` 方法，包含对标题为空的校验逻辑。
画面 6: 显示 `ApiHouseResourcesServiceImpl` 类，使用 `@Service(version = "1.0.0")` 注解，并注入 `HouseResourcesService`。
画面 7: 显示 `queryHouseResourcesList` 方法的实现，目前仅返回 `null`。
画面 8: 展示 PDF 文档“5.3、启动服务”章节，内容为“5.3、启动服务”标题和黑马程序员的页脚。
画面 9: 显示 `queryHouseResourcesList` 方法的实现，使用 `QueryWrapper` 构建查询条件并调用 `super.queryPageList`。
画面 10: 显示 `queryHouseResourcesList` 方法的实现，返回 `new PageInfo<>` 对象。
画面 11: 显示 `queryHouseResourcesList` 方法的实现，使用 `QueryWrapper` 设置排序条件并调用 `super.queryPageList`。
画面 12: 展示 PDF 文档“5.3、启动服务”章节，内容为“5.3、启动服务”标题和黑马程序员的页脚。
画面 13: 显示 Dubbo OPS 界面，展示服务提供者信息，IP 为 192.168.40.1，端口为 20880。
画面 14: 展示 PDF 文档“5.3、启动服务”章节，内容为“5.3、启动服务”标题和黑马程序员的页脚。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package cn.itcast.haoke.dubbo.server.api;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
public interface ApiHouseResourcesService {
    /**
     * 新增房源
     * @param houseResources
     * @return -1:输入的参数不符合要求，0：数据插入数据库失败，1：成功
     */
    int saveHouseResources(HouseResources houseResources);
    /**
     * 分页查询房源列表
     * @param page 当前页
     * @param pageSize 页大小
     * @param queryCondition 查询条件
     * @return
     */
    PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize,
            HouseResources queryCondition);
}
```

画面 3:
```java
import java.util.Collections;
public class PageInfo {
    /**
     * 总条数
     */
    private Integer total;
    /**
     * 当前页
     */
    private Integer pageNum;
    /**
     * 一页显示的大小
     */
    private integer pageSize;
    /**
     * 数据列表
     */
    private List<T> records = Collections.emptyList();
}
```

画面 4:
```java
package cn.itcast.haoke.dubbo.server.vo;
import lombok.Data;
import java.util.Collections;
import java.util.List;
@Data
public class PageInfo<T> {
    /**
     * 总条数
     */
    private Integer total;
    /**
     * 当前页
     */
    private Integer pageNum;
    /**
     * 页显示的大小
     */
    private integer pageSize;
    /**
     * 数据列表
     */
    private List<T> records = Collections.emptyList();
}
```

画面 5:
```java
import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
@Service
@Transactional
public class HouseResourcesServiceImpl extends BaseServiceImpl implements HouseResourcesService {
    /**
     * @param houseResources
     * @return -1:输入的参数不符合要求，0：数据插入数据库失败，1：成功
     */
    @Override
    public int saveHouseResources(HouseResources houseResources) {
        // 添加校验或者其他的逻辑
        if (StringUtils.isBlank(houseResources.getTitle())) {
            // 不符合要求
            return -1;
        }
        return super.save(houseResources);
    }
}
```

画面 6:
```java
@Service(version = "1.0.0")
public class ApiHouseResourcesServiceImpl implements ApiHouseResourcesService {
    @Autowired
    private HouseResourcesService houseResourcesService;
    @Override
    public int saveHouseResources(HouseResources houseResources) {
        return this.houseResourcesService.saveHouseResources(houseResources);
    }
}
```

画面 7:
```java
@Override
public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources query) {
    return null;
}
```

画面 9:
```java
QueryWrapper<T> queryWrapper = new QueryWrapper<>();
// 根据数据的更新时间倒序排序
queryWrapper.orderByDesc(...columns: "updated");
IPage<IPage> iPage = super.queryPageList(queryWrapper, page, pageSize);
return new PageInfo<>(iPage.getTotal(), page, _);
```

画面 10:
```java
return new PageInfo<>();
```

画面 11:
```java
QueryWrapper queryWrapper = new QueryWrapper();
// 根据数据的更新时间倒序排序
queryWrapper.orderByDesc(...columns: "updated");
IPage<IPage> iPage = super.queryPageList(queryWrapper, page, pageSize);
return new PageInfo<>(iPage.getTotal(), page, _);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PDF 文档标题为“5. 房源列表服务”，并指出接下来要实现房源列表服务。
画面 8: PDF 文档标题为“5.3、启动服务”。
画面 12: PDF 文档标题为“5.3、启动服务”。
画面 14: PDF 文档标题为“5.3、启动服务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
