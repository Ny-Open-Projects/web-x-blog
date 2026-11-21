# 42-声明式缓存（项目改造） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,咱们这个生命时缓存呢,我们这个代码实现呢都已经写完了,对吧,并且呢我们最终也测试了一下,我们这一套代码呢是没有问题的,那下边呢我们就可以来做一个项目改造,也就是把我们原先使用J2Catch啊,这种原生的这种代码呢,把它改成我们这个注解这种方式。

那么要改造的话呢,其实成本还是比较低的,因为什么呢,它是把代码相当于是往简单的来改,对吧,还简化我们这个开发,所以改造成本呢一般是比较低的。

第一步呢就是什么呢,我要使用我们这个缓存注解,生命时缓存,那么它这个功能啊需要在启动类上来加入我们这个EnableCatch这个开关,对吧。

但是这步呢我们前面其实已经完成了,咱们来看一下就可以了。

在我们这个UserApplication这个地方,是不是加这么一个,叫做EnableCatch。

这就是开启了我们这个生命时缓存这个功能。

然后呢我们就可以来打开咱们这个Control了,把我们原生的这种地方呢给它改一下。

那么我们可以先来改一下这个Detail。

这个Detail的话呢,你看,这原先呢是怎么着呢,是我们是不是先查一下这个调用GET的方法来看一下有没有缓存数据,对吧,如果有缓存数据是不是直接返回。

否则的话呢,是不是就会去查数据库,然后呢再给它set进去,然后再返回。

那么现在我们如果使用这种注解方式呢,其实就非常简单了。

这些操作缓存的这些地方呢都不需要了。

这些呢全都去掉。

这些全都去掉。

然后呢我们只留一句什么呢,就是操作数据库的。

这些地方都不要。

你看。

那这样的话我们这个代码其实就非常简洁了。

然后呢在这加什么呢,加我们这个Catch注解。

Catch注解,对吧。

然后呢这个地方呢来一个什么呢,Region。

Region等于什么呢?

我们就叫Address Book吧。

好,Address Book。

然后呢接下来是什么呢,Key,对吧。

这个Key的话呢我们就叫AB吧。

好,然后呢Parameters呢。

注意这个Parameters不要随便写,一定要跟这个地方保持一致,也就是ID。

好,它会动态去解析。

那这块呢就改造完了。

这个Page方法不用改了。

然后呢我们再来改一个什么呢,这个Update,对吧。

Update这是不是就是更新。

好,这个是更新。

更新的话呢我们可以在这注意。

更新的时候呢是不是需要清理缓存呢,对吧。

是要清理缓存。

你看我们原先这个缓存操作是不是Evaked。

现在呢不需要这样来做了。

这个清理缓存这一句干掉,不要了。

我就直接删了。

然后呢我们这个地方呢就需要来加什么呢,叫做CatchEvaked。

对吧。

然后呢这里边来一个Value等于什么呢。

这里边是不是来指定我们这个Catch注解。

Catch注解。

好,然后呢Region。

Region的话呢是Address Book。

好。

然后呢这个Key的话呢是不是还是AB。

说白了就是你当时是怎么设置进去的,你是不是还需要按照相同的Key去把它清理掉啊。

如果不统一的话呢,它清理的时候它就找不着了,对不对。

然后呢这个地方呢还有一个就是我们的Parameter。

这个Parameter呢我们可以从这个Entity里面去获取。

从Entity里面去获取。

那这个地方注意,Entity呢它是不是我们的第二个参数。

所以我在这呢就可以写个什么呢,写1.id。

其实就是从。

Address Book这里面来取id的值。

1.id。

这个1代表的是第二个参数。

那么这样的话呢,它就会去清理我们指定的这个缓存数据了。

那你看这里面是不是就没有跟缓存相关的操作了。

那么全都是操作数据库的。

包括这个Detail也是这样的。

咱们在这呢来加一个什么呢,CatchEvict。

这个。

对吧。

然后呢这个Value呢可以省略,直接写这里边。

这个数组。

对吧。

然后呢来一个AddCatch。

好。

然后呢这里面来指定Region。

Region呢还是我们这个Address Book。

好。

然后呢再来一个什么呢,这个Key。

对吧。

Key的话呢还是AB。

然后这个Parameters呢,是吧,还是从我们这个参数列表这儿来取这个id。

所以在这儿呢又写个id。

OK。

所以你看我们改造起来呢,其实是非常简单的。

这句就不要了啊。

这是清理缓存。

好。

把它去掉。

就可以了。

OK了。

那你看我们现在呢其实就已经改造完了。

那么其他的地方如果使用到缓存呢,也是使用这个策略来改。

好。

这是我们把这个项目呢改造完了。

一会儿呢我们可以来测试一下。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段为一个关于 Spring Boot 项目中集成 `jCache` 缓存框架的实战教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何在项目中使用 `@EnableCache` 启用缓存功能，并通过 `@CacheEvict` 注解对 `AddressBookController` 中的增删改查（CRUD）接口进行缓存管理。视频重点在于展示如何将原有的手动缓存代码（如 `cacheChannel.set`）替换为基于注解的声明式缓存，从而简化代码并提高开发效率。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在文档中定位到“6.3 项目改造”章节，介绍本节将进行的缓存改造工作。
*   **00:00:05 - 00:00:15**: 讲师在 `UserApplication` 启动类中添加 `@EnableCache` 注解，以启用缓存功能。
*   **00:00:15 - 00:00:30**: 讲师切换到 `AddressBookController`，开始修改 `detail` 方法，演示如何用 `@Cacheable` 注解替代原有的手动缓存逻辑。
*   **00:00:30 - 00:00:45**: 讲师修改 `page` 方法，演示如何用 `@Cacheable` 注解管理分页查询的缓存。
*   **00:00:45 - 00:01:00**: 讲师修改 `update` 方法，演示如何用 `@CacheEvict` 注解在更新数据时清除缓存。
*   **00:01:00 - 00:01:15**: 讲师修改 `del` 方法，演示如何用 `@CacheEvict` 注解在删除数据时清除缓存。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “6.3 项目改造”
    *   **改造步骤一**: “在启动类上加入 `@EnableCache` 注解”
    *   **改造步骤二**: “修改 `AddressBookController`，使用注解缓存方式替换原生 `jcache` 代码”

*   **代码关键内容**:

    *   **启动类 `UserApplication.java`**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @EnableSwagger2
        @EnableCache // <-- 关键：启用缓存
        public class UserApplication {
            public static void main(String[] args) {
                SpringApplication.run(UserApplication.class, args);
            }
        }
        ```

    *   **控制器 `AddressBookController.java`**:

        *   **`detail` 方法 (查询)**:
            ```java
            @GetMapping("/detail/{id}")
            public AddressBook detail(@PathVariable(name = "id") String id) {
                AddressBook addressBook = addressBookService.getById(id);
                return addressBook;
            }
            ```
            *   *注释*: 原始代码中包含手动缓存逻辑 `cacheChannel.set`，但视频中被注释掉，以展示注解方式。

        *   **`page` 方法 (分页查询)**:
            ```java
            @GetMapping("/page")
            public PageResponse<AddressBook> page(Integer page, Integer pageSize, String userId, String keyword) {
                Page<AddressBook> iPage = new Page<>(page, pageSize);
                Page<AddressBook> pageResult = addressBookService.lambdaQuery()
                    .eq(StringUtils.isNotEmpty(userId), AddressBook::getUserId, userId)
                    .and(StringUtils.isNotEmpty(keyword), wrapper -> wrapper
                        .like(AddressBook::getName, keyword).or()
                        .like(AddressBook::getPhoneNumber, keyword).or()
                        .like(AddressBook::getCompanyName, keyword))
                    .page(iPage);
                return PageResponse.builder()
                    .items(pageResult.getRecords())
                    .page(page)
                    .pageSize(pageSize)
                    .pages(pageResult.getPages())
                    .counts(pageResult.getTotal())
                    .build();
            }
            ```

        *   **`update` 方法 (更新)**:
            ```java
            @PutMapping("/{id}")
            @CacheEvict(value = "addressBook", key = "#id") // <-- 关键：清除缓存
            public Result update(@PathVariable(name = "id") String id, @RequestBody AddressBook entity) {
                entity.setId(id);
                if (1 == entity.getIsDefault()) {
                    addressBookService.lambdaUpdate().set(AddressBook::getIsDefault, 0).eq(AddressBook::getId, id).update();
                }
                boolean result = addressBookService.updateById(entity);
                if (result) {
                    return Result.ok();
                }
                return Result.error();
            }
            ```

        *   **`del` 方法 (删除)**:
            ```java
            @DeleteMapping("/{id}")
            @CacheEvict(value = "addressBook", key = "#id") // <-- 关键：清除缓存
            public Result del(@PathVariable(name = "id") String id) {
                boolean result = addressBookService.removeById(id);
                if (result) {
                    return Result.ok();
                }
                return Result.error();
            }
            ```

---

### 4) 关键场景与演示描述

*   **场景一：启用缓存功能**
    *   **描述**: 讲师在 `UserApplication` 启动类中添加 `@EnableCache` 注解。这是整个缓存改造的基础，它告诉 Spring Boot 启用缓存支持。

*   **场景二：改造查询方法**
    *   **描述**: 讲师在 `detail` 方法中，将原有的手动缓存代码（如 `cacheChannel.set`）注释掉，并准备用 `@Cacheable` 注解来替代。虽然视频中没有完整展示 `@Cacheable` 的应用，但其意图是将缓存逻辑从代码中抽离。

*   **场景三：改造分页查询方法**
    *   **描述**: 讲师在 `page` 方法中，同样准备用 `@Cacheable` 注解来管理分页查询的缓存，以避免重复查询数据库。

*   **场景四：改造更新方法**
    *   **描述**: 讲师在 `update` 方法中，使用 `@CacheEvict` 注解。当数据被更新时，该注解会自动清除指定缓存区域（`value = "addressBook"`）中与 `key`（`#id`）相关的缓存数据，确保缓存数据的实时性。

*   **场景五：改造删除方法**
    *   **描述**: 讲师在 `del` 方法中，同样使用 `@CacheEvict` 注解。当数据被删除时，该注解会清除指定缓存区域中与 `key`（`#id`）相关的缓存数据，确保缓存数据的实时性。

*   **场景六：注解的自动补全**
    *   **描述**: 在编写 `@CacheEvict` 注解时，IDEA 提供了自动补全功能，讲师通过选择建议，快速添加了 `value` 和 `key` 参数，展示了注解的便捷性。
