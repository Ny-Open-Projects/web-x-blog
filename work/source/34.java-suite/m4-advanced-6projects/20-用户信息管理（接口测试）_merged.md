# 20-用户信息管理（接口测试） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才咱们这个member controller

这里边这五个方法

对吧 都已经导入完了

那接下来我们就整体来测试一下

咱们把服务停掉

然后重新启动一下

好 咱们这个服务已经启动成功了

然后回到我们

Swagger接口文档这个页面

咱们刷新一下这个页面

来看 它是不是多出来这么一个

叫做member controller

对吧 里边有五个接口

首先我们先来测试一下这个save

save try it out

咱们来保存一个数据

对吧 保存一个数据

但这个因为都是假数据

我这个其实也可以不改

不改我们直接点执行

这样的话它就会像什么

像我们这个member表

来看PD users数据库里面的

PD member这个表里面来插入数据

我们这里边数据比较多

咱们来看一下

现在一共是有35条数据

对吧 35条数据

然后我们来执行一下

执行完了

你看它返回success

然后到这边来刷信息

我们看一下这个

变成了36条 对吧

变成36条

那么我们这边比较乱

我们就不再找它具体添加的那条了

应该是最后这个

应该是最后这个

因为我刚才没有改

那么都是string 对吧

所以从这能看到

这个呢这是咱们这个新增

然后呢我们再来一个什么呢

这个就按咱们这个顺序吧

根据ID查询 对吧

根据ID查询

根据ID查询的话

应该就是这个

然后呢try it out

这个ID的话呢

我们可以从这随便来考一个

比如就这个ID

我复制一下

然后呢把这个ID呢

直接粘在这个位置来执行一下

好 你看它是不是已经给我查出来了

这是根据ID呢来查询

然后还有什么呢

分页 对吧

然后我们来测一下这个分页

分页的话是这个

配置这个

好 try it out

然后呢输入页码

然后呢输入这个

这个总的这个每页显示记录数对吧

page size

然后呢执行一下

好 你看一共是36条对吧

然后呢page size是10

分成了4页

当前是第1页

然后下面这是数据列表

好 这都比较简单

再往下呢是这个更新

更新的话呢我们可以

找到这个更新啊

应该是这个对吧

更新 try it out

好 咱们就更新什么呢

就更新我们刚才自己这个造的这条数据对吧

你看这个ID呢

我是不是写的string啊

然后呢我们就根据它来更新

咱们来改一下

ID呢就不用改了

是string

然后呢auth id呢

我们给它改成100

然后呢这个呢改成101

好

然后呢这个改成1

这个for number对吧

随便改一个

好 我就随便写一个

因为我们这个接口呢直接调用

没有做这个

没有做校验对吧

所以说呢其实你输入什么呢

什么值它都能保存进去啊

好 然后呢注意这个地方是不是ID

这个ID呢是通过路径变量对吧

通过路径给它传过去

好 然后呢我们在这来复制一下

把ID给它放在这儿

它是根据ID来改的

所以说这里边这个

因为我们当前这个json对象呢

是要封装成我们这个实体的对不对

那么我们真正改呢

其实是根据这个ID来改

所以说这个地方这个ID

你传不传都可以

重点是这个ID

它是根据这个ID来进行改

好 执行一下

好 然后呢我们再来改这个ID呢

执行完了

执行完了之后呢

咱们把这个表呢来刷新一下

你看看它有没有给我改过来

是不是这已经都改对了

好 这也没问题

然后呢最后呢还有一个删除对吧

我们再来测一下删除这个接口

删除接口就是这个

好 try it out

咱们这个ID的话呢

是不是就是string啊

就是string

把它给删掉

执行

又返回success

然后呢我们把这个数据呢

来刷新一下注意看

现在是36条数据

刷新一下

哎这不变成35条

那条数据已经删掉了

好

那么这是咱们这个五个接口

导入的这五个接口呢

整体来测试一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于一个名为“品达物流订单模块”的 Java 后端项目，主要演示了如何在 `MemberController` 中实现用户信息的增删改查（CRUD）功能。讲师通过 IntelliJ IDEA 开发环境编写控制器代码，并结合 Swagger UI 进行接口测试，同时展示了数据库表结构。课程内容涵盖了 Spring Boot 的 `@RestController`、`@PostMapping`、`@PutMapping`、`@DeleteMapping` 等注解的使用，以及如何通过 `PageResponse` 进行分页查询。整个过程旨在教授如何将业务逻辑封装为 RESTful API，并通过文档化接口供前端调用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:02:00**：课程开场，讲师介绍本节内容是关于用户信息管理的接口开发，主要涉及 `MemberController`。
*   **00:02:00 - 00:05:00**：演示如何在 `MemberController` 中创建 `save` 方法，用于新增用户。代码中使用 `@PostMapping` 注解，并通过 `@RequestBody` 接收 JSON 数据。
*   **00:05:00 - 00:08:00**：讲师切换到 Swagger UI，演示如何调用 `POST /member/save` 接口，并展示成功返回的 JSON 响应。
*   **00:08:00 - 00:10:00**：讲师展示 `GET /member/detail/{id}` 接口，用于根据 ID 查询用户详情，并演示了如何在 Swagger 中传入参数。
*   **00:10:00 - 00:12:00**：讲师讲解 `PUT /member/{id}/update` 接口，用于更新用户信息，并在 Swagger 中演示了如何调用。
*   **00:12:00 - 00:14:00**：讲师讲解 `DELETE /member/{id}/del` 接口，用于删除用户信息，并在 Swagger 中演示了如何调用。
*   **00:14:00 - 00:16:00**：讲师展示 `PageResponse` 的使用，讲解如何在 `MemberController` 中创建 `page` 方法实现分页查询。
*   **00:16:00 - 00:18:00**：讲师在 PPT 中展示 `update` 方法的代码，并讲解其逻辑。
*   **00:18:00 - 00:20:00**：讲师在 PPT 中展示 `del` 方法的代码，并讲解其逻辑。
*   **00:20:00 - 00:22:00**：讲师展示数据库表 `pd_member` 的结构，说明其字段含义。
*   **00:22:00 - 00:24:00**：讲师总结本节内容，强调接口开发的完整流程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`5.4.3 分页查询用户信息`、`5.4.4 更新用户信息`、`5.4.5 删除用户信息`。
    *   **代码片段**：
        *   **分页查询方法**：
            ```java
            @GetMapping("page")
            public PageResponse<Member> page(Integer page, Integer pageSize) {
                Page<Member> iPage = new Page(page, pageSize);
                LambdaQueryWrapper<Member> queryWrapper = new LambdaQueryWrapper<>();
                Page<Member> pageResult = memberService.page(iPage, queryWrapper);
                return PageResponse.<Member>builder()
                        .items(pageResult.getRecords())
                        .page(page)
                        .pageSize(pageSize)
                        .pages(pageResult.getPages())
                        .counts(pageResult.getTotal())
                        .build();
            }
            ```
        *   **更新方法**：
            ```java
            @PutMapping("update")
            public Result update(@PathVariable(name = "id") String id, @RequestBody Member entity) {
                entity.setId(id);
                boolean result = memberService.updateById(entity);
                if (result) {
                    return Result.ok();
                }
                return Result.error();
            }
            ```
        *   **删除方法**：
            ```java
            @DeleteMapping("del")
            public Result del(@PathVariable(name = "id") String id) {
                boolean result = memberService.removeById(id);
                if (result) {
                    return Result.ok();
                }
                return Result.error();
            }
            ```
    *   **图表**：Swagger UI 界面截图，展示了 `POST /member/save`、`GET /member/detail/{id}`、`PUT /member/{id}/update`、`DELETE /member/{id}/del` 等接口的详细信息。

*   **代码**：
    *   **`MemberController.java`**：
        ```java
        @RestController
        @RequestMapping("member")
        public class MemberController {
            @Autowired
            private MemberService memberService;

            @PostMapping("")
            public Result save(@RequestBody Member entity) {
                boolean result = memberService.save(entity);
                if (result) {
                    return Result.ok();
                }
                return Result.error();
            }
        }
        ```
    *   **`MemberService.java`**：未在画面中直接展示，但其方法如 `save`、`updateById`、`removeById` 等被 `MemberController` 调用。

---

### 4) 关键场景与演示描述

*   **场景一：创建新增接口**
    *   **描述**：讲师在 IntelliJ IDEA 中编写 `MemberController` 的 `save` 方法。他使用 `@PostMapping` 注解定义一个 POST 请求，接收一个 `Member` 对象作为请求体。方法内部调用 `memberService.save(entity)` 保存数据，并根据返回结果返回 `Result.ok()` 或 `Result.error()`。
    *   **演示**：讲师切换到 Swagger UI，点击 `POST /member/save` 接口，输入 JSON 数据并执行，成功返回 `{"msg": "success", "code": 0}`。

*   **场景二：创建查询接口**
    *   **描述**：讲师在 PPT 中展示 `PageResponse` 的使用，并在代码中编写 `page` 方法。该方法接收 `page` 和 `pageSize` 参数，使用 `LambdaQueryWrapper` 构建查询条件，调用 `memberService.page` 方法进行分页查询，并将结果封装成 `PageResponse` 返回。
    *   **演示**：讲师在 Swagger UI 中点击 `GET /member/detail/{id}` 接口，输入 ID 并执行，成功返回用户详情。

*   **场景三：创建更新接口**
    *   **描述**：讲师在 PPT 中展示 `update` 方法的代码。该方法使用 `@PutMapping` 注解定义一个 PUT 请求，接收 `id` 和 `Member` 对象。方法内部将 `id` 设置到 `entity` 中，调用 `memberService.updateById(entity)` 更新数据，并返回相应结果。
    *   **演示**：讲师在 Swagger UI 中点击 `PUT /member/{id}/update` 接口，输入 ID 和更新数据并执行，成功返回 `{"msg": "success", "code": 0}`。

*   **场景四：创建删除接口**
    *   **描述**：讲师在 PPT 中展示 `del` 方法的代码。该方法使用 `@DeleteMapping` 注解定义一个 DELETE 请求，接收 `id`。方法内部调用 `memberService.removeById(id)` 删除数据，并返回相应结果。
    *   **演示**：讲师在 Swagger UI 中点击 `DELETE /member/{id}/del` 接口，输入 ID 并执行，成功返回 `{"msg": "success", "code": 0}`。

*   **场景五：数据库表结构展示**
    *   **描述**：讲师打开数据库管理工具，展示 `pd_member` 表的结构。表包含 `id`、`authId`、`id_card_no`、`id_card_no_verify`、`phone` 等字段，用于存储用户信息。
    *   **演示**：讲师在数据库工具中执行 `SELECT * FROM pd_users LIMIT 1000` 查询语句，展示表中的数据。

---

以上是根据视频画面整理出的技术课程结构化分析。
