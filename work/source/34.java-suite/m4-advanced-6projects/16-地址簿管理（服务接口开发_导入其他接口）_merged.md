# 16-地址簿管理（服务接口开发_导入其他接口） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢我们是对第一个

也就是新增地址簿这个接口呢

进行了一个简单的测试

那么测试完了之后呢

接下来我们看下一个

就是根据ID来查询地址簿详情对吧

因为后边这些代码呢都比较简单

所以说我们就一次性的

把这些代码呢全都抄到我们这个开发工具当中

然后呢整体来测试一下

然后呢带着大家来简单读一下这个代码就可以了

好

下面这个呢是提供这么一个方法对吧

叫Detail

这就是查询我们这个地址簿的详情

然后呢传过来的是一个ID对吧

并且呢通过这个路径变量这种方式

Pass Variable对吧

加这个注解

然后呢从我们这个路径上来获取这个ID的值

好

然后呢拿到之后呢

首先我们肯定是先查缓存对不对

如果缓存不为空的话

直接返回缓存的数据

否则的话呢是不是再来Get By ID

其实这个Get By ID呢

不用我们在service里面自己去扩展了

因为我们是不是已经继承了

这个MyBetisPlus

给我们提供的接口

所以说直接调这个方法

就可以根据ID查询了

查完之后呢重新放回缓存

对吧

然后呢返回

那么整个呢方法非常简单

只要在这个Control了当中啊

我们这个提供这么一个方法就可以

service啊什么mypr都不用去写

就是因为我们现在调的呢

就是这个MyBetisPlus啊

给我们提供的这些方法

好

所以我们直接写到这就可以了啊

就这一个方法

好

就这个Detail

好

然后呢

下边这个呢

再往下呢

是分页查询对吧

这个分页的话也是比较简单的

就这一个方法

咱们直接抄过来啊

这个是基于什么呢

MyBetisPlus给我们提供的这个什么呢

mypr这个Page对吧

Page对象

来进行这个分页

好

直接全抄过来

大概来读一下

需要注意的就是什么呢

我们这个分页呢

统一都返回这个对象对吧

叫做Page response

Page response

分页数据统一对象

也就是说以后呢

所有的分页数据呢

最终呢都会包装成这么一个对象

然后来返回

这个对象里边呢

封装了跟分页相关的一些属性啊

比如说这个Counts对吧

总的条目数啊

还有Page size

页尺寸其实就是每页显示的记录数对吧

还有Pages就是总页数

还有当前页码

以及什么的列表数据

好

然后呢我们在这呢进行分页的话呢

其实是调的什么呢

是调的这个MyBetisPlus这个

给我们提供的这个Lambda query

对吧

然后呢去封装一些什么呢

封装一些这个过滤条件对吧

封装一些过滤条件

好

这些全都是过滤条件

最后呢

是不是来这个

调用配置方法进行分页

那么分页的时候呢

我们是不是需要先new一个配置对象对吧

把这个页码还有Page size都传进去

然后呢

接下来就是封装相应的过滤条件

最后呢调用配置方法

这样的话就把我们这个Page result

这个分页对象

是不是给返回

但是这个对象呢

注意

这个对象呢

它其实是什么呢

是MyBetisPlus呢

MyBetisPlus是不是给我们提供的这个分页对象

所以我们需要把它转一下

转成什么呢

转成我们这个Page result

我们是通过这个Builder构建器这种方式

把这里面的属性是不是全都给它设置好

最后呢调用Build方法

然后呢就可以构建一个Page response

这么一个对象

来返回

只不过这些呢全都是什么呢

这个条件对不对

全都是条件啊

那么根据Name来进行like查询

根据FullNumber like查询

对吧模糊查询

还有CompanyName

也是模糊查询

然后Uzid的话呢

这个是不是等值查询

等值查询

好那么这是咱们这个分页的方法了

大概来看一下就可以了

请求的路径呢就是这么一个路径

就是Page

然后请求方式呢是get方式

再往下呢是什么呢

是这个更新地址部

更新地址部的话呢

我们也是只要在Controller当中提供一个update的方法就可以了

需要更新的时候呢

直接调用updateByID这个方法

同样这个方法呢也是从myBadgePlus继承过来的

所以你看我们后边这几个方法呢

其实只需要什么呢

在Controller当中提供一个方法就可以

并不需要在什么Service当中再去扩展方法了

同样这个更新的时候呢

这一句呢跟我们新增的时候是

类似的

是类似的

就是大家看这一块对吧

这个就是什么呢

如果说我们当前修改的

这个地址部

信息呢

它的这个isDefault等于1

这就表示什么呢

当前这一条是不是应该是

是默认的对吧

默认的地址信息

那么我们就需要什么呢

把其他的

关于这个人的这些地址部

全都给它改成什么呀

改成0

isDefault改成0

这就表示其他的应该全不是默认了

因为默认的只能有一条对吧

然后呢再往下是不是就调用

updateByID这个方法

然后进行更新就可以了

注意什么呢更新完之后呢

我们是不是需要把原先的这个缓存数据把它清理掉

原先的缓存数据给它清理掉

evac了就可以了

然后再往下呢是什么删除地址部对吧

删除地址部呢

其实就是调用什么呢

removeByID

这个方法

这也是mybyDplus给我们提供的

同样的删除完之后呢别忘了去清理缓存数据

所以这块呢从代码上来说其实还是非常简单的

主要就是大家别忘了去什么呢

处理缓存该清理的时候是不是需要清理

要不然的话呢就会出现一些什么

这个脏数据的

对吧

相当于我们的缓存数据跟数据库里面数据不同步

这肯定是不行的

所以说呢当我们把数据删掉之后

缓存呢也需要清理掉

好

这是关于我们这一块啊

另外的几个接口

咱们直接一次性的把这个代码全都导到我们项目当中

一会儿呢我们整体来测试一下这几个接口

就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是“品达物流TMS项目”第三章“用户服务开发”中关于“地址簿管理”模块的开发教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 `AddressBookController` 中实现四个核心的 HTTP 接口：根据 ID 查询地址簿详情（`detail`）、分页查询地址簿（`page`）、更新地址簿（`update`）和删除地址簿（`del`）。整个过程强调了缓存（`cacheChannel`）的使用，包括查询时的缓存命中、更新时的缓存清除以及删除时的缓存清除，以实现高性能的读写操作。视频内容以代码演示为主，辅以 PPT 大纲导航，旨在教授学生如何在实际项目中实现带缓存的 CRUD 操作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示课程大纲，定位到“4.4 服务接口开发”下的“4.4.2 根据id查询地址簿详情”。
*   **00:05 - 00:15**: 演示 `detail` 方法的实现，展示如何从缓存中读取数据，如果缓存不存在则调用服务层获取数据并写入缓存。
*   **00:15 - 00:25**: 展示 `page` 方法的实现，演示如何构建分页查询条件，使用 `LambdaQuery` 进行条件过滤，并构建 `PageResponse` 返回结果。
*   **00:25 - 00:35**: 展示 `update` 方法的实现，演示如何更新数据库记录，并在更新后清除缓存。
*   **00:35 - 00:45**: 展示 `del` 方法的实现，演示如何删除数据库记录，并在删除后清除缓存。
*   **00:45 - 00:50**: 结束本节，过渡到下一章“5. 用户信息管理”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 大纲内容

*   **项目结构**: `品达物流TMS项目` -> `第3章 用户服务开发(pd-user)` -> `4. 地址簿管理` -> `4.4 服务接口开发`。
*   **核心章节**:
    *   `4.4.2 根据id查询地址簿详情`
    *   `4.4.3 分页查询地址簿`
    *   `4.4.4 更新地址簿`
    *   `4.4.5 删除地址簿`
    *   `5. 用户信息管理` -> `5.1 业务需求和产品原型`

#### 代码关键内容

*   **`detail` 方法** (缓存读取与写入)
    ```java
    @GetMapping("/detail/{id}")
    public AddressBook detail(@PathVariable(name = "id") String id) {
        // 查询缓存
        CacheObject cacheObject = cacheChannel.get(region, id);
        if (cacheObject.getValue() != null) {
            return (AddressBook) cacheObject.getValue();
        }
        // 从服务层获取数据
        AddressBook addressBook = addressBookService.getById(id);
        // 写入缓存
        if (addressBook != null) {
            cacheChannel.set(region, id, addressBook);
        }
        return addressBook;
    }
    ```

*   **`page` 方法** (分页查询与条件过滤)
    ```java
    @GetMapping("/page")
    public PageResponse<AddressBook> page(Integer page, Integer pageSize, String userId, String keyword) {
        Page<AddressBook> iPage = new Page<>(page, pageSize);
        Page<AddressBook> pageResult = addressBookService.lambdaQuery()
            .eq(StringUtils.isNotEmpty(userId), AddressBook::getUserId, userId)
            .and(StringUtils.isNotEmpty(keyword), wrapper ->
                wrapper.like(AddressBook::getName, keyword).or()
                .like(AddressBook::getPhoneNumber, keyword).or()
                .like(AddressBook::getCompanyName, keyword))
            .page(iPage);
        return PageResponse.<AddressBook>builder()
            .items(pageResult.getRecords())
            .page(page)
            .pageSize(pageSize)
            .pages(pageResult.getPages())
            .counts(pageResult.getTotal())
            .build();
    }
    ```

*   **`update` 方法** (更新与缓存清除)
    ```java
    @PutMapping("/id")
    public Result update(@PathVariable(name = "id") String id, @RequestBody AddressBook entity) {
        entity.setId(id);
        if (1 == entity.getIsDefault()) {
            addressBookService.lambdaUpdate().set(AddressBook::getIsDefault, 0)
                .eq(AddressBook::getUserId, entity.getUserId()).update();
        }
        boolean result = addressBookService.updateById(entity);
        if (result) {
            // 清理缓存
            cacheChannel.evict(region, id);
            return Result.ok();
        }
        return Result.error();
    }
    ```

*   **`del` 方法** (删除与缓存清除)
    ```java
    @DeleteMapping("/id")
    public Result del(@PathVariable(name = "id") String id) {
        boolean result = addressBookService.removeById(id);
        if (result) {
            // 清理缓存
            cacheChannel.evict(region, id);
            return Result.ok();
        }
        return Result.error();
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：缓存读取与写入 (`detail` 方法)**
    *   讲师在 IDEA 中打开 `AddressBookController.java` 文件。
    *   他首先展示 `detail` 方法的初始代码，重点讲解 `cacheChannel.get(region, id)` 如何从缓存中获取数据。
    *   他演示了 `if (cacheObject.getValue() != null)` 的逻辑，如果缓存命中，直接返回数据。
    *   他接着演示了 `addressBookService.getById(id)` 的调用，并在获取到数据后，通过 `cacheChannel.set(region, id, addressBook)` 将数据写入缓存，以备下次查询。

*   **场景二：分页查询与条件过滤 (`page` 方法)**
    *   讲师切换到 `page` 方法的代码。
    *   他演示了 `lambdaQuery()` 的使用，通过 `.eq()` 和 `.and()` 方法构建查询条件。
    *   他重点讲解了 `wrapper.like(...)` 的用法，用于实现对 `name`、`phoneNumber` 和 `companyName` 字段的模糊查询。
    *   他展示了如何使用 `PageResponse.builder()` 构建返回结果，并设置分页信息（`page`, `pageSize`, `pages`, `counts`）。

*   **场景三：更新与缓存清除 (`update` 方法)**
    *   讲师展示 `update` 方法的代码。
    *   他演示了 `lambdaUpdate()` 的用法，用于更新数据库记录。
    *   他特别强调了 `if (1 == entity.getIsDefault())` 的逻辑，用于处理默认地址的特殊更新。
    *   他讲解了 `cacheChannel.evict(region, id)` 的作用，即在更新后清除对应缓存，确保数据一致性。

*   **场景四：删除与缓存清除 (`del` 方法)**
    *   讲师展示 `del` 方法的代码。
    *   他演示了 `removeById(id)` 的调用，用于删除数据库记录。
    *   他讲解了 `cacheChannel.evict(region, id)` 的作用，即在删除后清除对应缓存，确保数据一致性。
    *   他强调了 `Result.ok()` 和 `Result.error()` 用于返回操作结果。

整个视频通过代码逐行演示和讲解，清晰地展示了如何在 Spring Boot 项目中实现带缓存的地址簿管理功能。
