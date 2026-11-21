# 17-权限业务接口-Spring data Rest返回ID配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们再来学习

SpringDataRest的ID数据的返回处理

在实际增伤改查当中

我们需要知道具体的ID

才能做对应的操作

但是SpringDataRest

它默认了会将ID进行隐藏

不会做返回

这个时候咱们该怎么去处理呢

下面有提供两种办法

第一种我们可以将所有的资源

都暴露返回ID

它的具体配置就如下所示

我们要去添加一个配置类

在配置类当中

要去做以下的配置处理

我们可以看到

ConfigureExpose这个方法

它会去扫描咱们所有的实体信息

它做的是一个便利处理

这种配置适合通用的场景

但是如果是有特殊需求

只想暴露指定资源的ID

该怎么去配置呢

下面也提供了配置方法

在这里同样我们采用一个配置类

这个配置类的话

它就可以去指定你所需要

暴露指定资源的ID实体

比如说我想暴露菜单下面的ID信息

那么将这个菜单的class传入进去

这样就实现了

Spring Data Less的ID数据的返回

因为默认的情况下面

咱们可以看到这个豹文

它并没有返回对应的ID信息

这两种方式

咱们可以根据具体的场景

需求来采用不同的方式进行处理

好

那这讲的就是对Spring Data Less的返回ID数据的一个配置讲解

这讲的咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于 **Spring Data REST** 框架的一个高级用法教程，主要讲解如何解决在实际增删改查操作中，因框架默认隐藏实体 ID 而导致无法获取具体 ID 的问题。讲师通过代码演示，介绍了两种解决方案：

*   **方案一：** 通过自定义配置类 `RestEntityIdConfiguration`，利用 `EntityManager` 获取所有实体类，并调用 `exposeIdsFor` 方法，将所有资源的 ID 都暴露出来。
*   **方案二：** 通过自定义配置类 `ExposeEntityIdRestMvcConfiguration`，仅针对特定的实体类（如 `AuthorityMenu`）暴露其 ID。

视频内容旨在帮助开发者在使用 Spring Data REST 时，能够灵活地控制 ID 的暴露策略，以满足业务需求。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面是连续的，无法精确到秒，但可以按内容逻辑划分：

*   **00:00 - 00:05:** 视频开头，讲师介绍当前章节主题：“Spring data rest 返回ID数据”，并提出问题：在增删改查中，如何获取被隐藏的 ID？
*   **00:05 - 00:15:** 讲师介绍第一种解决方案：“将所有资源都暴露返回ID”，并展示第一个代码示例 `RestEntityIdConfiguration`。
*   **00:15 - 00:25:** 讲师展示并讲解第一个代码示例的完整实现，包括如何通过 `EntityManager` 获取所有实体并暴露其 ID。
*   **00:25 - 00:35:** 讲师过渡到第二种解决方案：“暴露指定资源的ID”，并展示第二个代码示例 `ExposeEntityIdRestMvcConfiguration`。
*   **00:35 - 00:45:** 讲师展示并讲解第二个代码示例的实现，重点是 `exposeIdsFor(AuthorityMenu.class)`，说明其只对特定实体生效。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 关键代码示例

**方案一：暴露所有资源的 ID**

```java
@Configuration
public class RestEntityIdConfiguration extends RepositoryRestConfigurerAdapter {

    @Autowired
    private EntityManager entityManager;

    @Override
    public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
        config.exposeIdsFor(entityManager.getMetamodel().getEntities()
                .stream()
                .map(e -> e.getJavaType())
                .collect(Collectors.toList())
                .toArray(new Class[0]));
    }
}
```

**方案二：暴露指定资源的 ID**

```java
@Component
public class ExposeEntityIdRestMvcConfiguration extends RepositoryRestConfigurerAdapter {

    @Override
    public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
        config.exposeIdsFor(AuthorityMenu.class);
    }
}
```

#### 关键概念

*   **Spring Data REST 默认行为：** 在进行增删改查操作时，框架会隐藏实体的 ID，不将其返回给客户端。
*   **`RepositoryRestConfigurerAdapter`：** 一个用于配置 Spring Data REST 行为的抽象类。
*   **`exposeIdsFor(Class<?>... classes)`：** 用于指定哪些实体类的 ID 应该被暴露出来。
*   **`EntityManager.getMetamodel().getEntities()`：** 获取当前应用中所有实体类的元数据。

---

### 4) 关键场景与演示描述

*   **场景一：问题引入**
    *   讲师首先展示了一个 JSON 响应片段，其中包含一个 `href` 链接，指向一个具体的资源（如 `/admin/authorityMenu/2`）。
    *   讲师指出，在实际操作中，如果需要知道这个资源的 ID（例如，用于后续的更新或删除操作），但框架默认不返回 ID，这就造成了问题。

*   **场景二：方案一演示**
    *   讲师在代码编辑器中创建并编写了 `RestEntityIdConfiguration` 类。
    *   他通过 `entityManager.getMetamodel().getEntities()` 获取所有实体类，然后使用 `stream().map().collect().toArray()` 将这些类转换为一个 `Class` 数组。
    *   最后，调用 `config.exposeIdsFor(...)` 方法，将这个数组中的所有实体类的 ID 都暴露出来。

*   **场景三：方案二演示**
    *   讲师在代码编辑器中创建并编写了 `ExposeEntityIdRestMvcConfiguration` 类。
    *   他直接调用 `config.exposeIdsFor(AuthorityMenu.class)`，只针对 `AuthorityMenu` 这一个实体类暴露其 ID。
    *   这种方式更加灵活，适用于只需要暴露特定资源 ID 的场景。

*   **场景四：对比与总结**
    *   讲师通过对比两个方案，强调了它们的区别：方案一适用于需要暴露所有资源 ID 的场景，而方案二则适用于需要精确控制 ID 暴露范围的场景。
    *   他总结了这两种方法的使用场景和优势，为观众提供了实用的解决方案。
