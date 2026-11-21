# 19-用户信息管理（导入功能代码） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么接下来呢

咱们来看一下我们用户信息管理的服务接口开发

这块呢 由于也是啊

这个本身代码呢 比较简单

所以我们这块呢

还是啊 把它一次性把它导入到我们这个工程当中来

一会儿呢 我们整体来测试一下这个代码就可以了

好 首先呢 我们先来看啊

第一个接口呢 是新增用户信息 对吧

其实就是提供一个member controller

然后呢 再提供一个save方法

整个代码写起来还是非常简单的

咱们先把这个member controller来创建一下

在controller包下边

好 然后呢 整个把这个代码拷过来

好 这是第一步

但是它这是报错 对吧

因为呢 我们需要这么一个接口

叫做imember service

所以接下来呢 我们把这个接口来创建一下

放在这个service包下边来

然后呢 这个里边呢

需要让它继承什么呢

继承咱们这个iservice

也就是我们mybattletool

plus给咱们提供的

好 然后这个member呢

需要导入一下 import

导入一下这个member

这是咱们这个实体类 对吧

好 然后接下来呢 是service的实现类

实现类呢 叫做这个名字

放在impl这个实现包里面去

然后具体代码呢

我就直接从这儿来复制一下

因为这个呢 对于我们目前来说呢

没有任何难度啊

所以我们就不再去一句手敲了就啊

整个复制过来

好 然后呢 这儿是不是需要一个

这个member mapper 对吧

member mapper

好 在这儿来创建这个接口

叫做member mapper

然后别忘了 这个mapper的话呢

需要继承什么呢

继承base mapper

这都是按照mybattletool plus

给我们提供的规范呢

好 这是mapper注解

然后呢 这是实体类

来导入一下 别导错了

我们自己的这个实体类

最后呢 还有一个应使文件 对吧

还有一个应使文件

这个应使文件呢

叫做mapper

叫member mapper.xml

放在resource这个下边

这个刚才没有复制的有问题啊

好 复制一下

这个好像还直接复制

它总是复制那个内容啊

不知道怎么回事

这位是可以了

刚才有点问题

然后呢 我们把这个mapper文件啊

其实就是把这个结构 对吧

把它标签结构给它拷过来就可以了

好 这个呢 是咱们这个

这个第一个 新增

新增一个用户信息

从什么呢

从我们这个controller到service到mapper 对吧

最后呢 到这个应使文件

好 这个呢 因为比较简单

所以我们就不再解释了

下一个呢 是根据ID查询详情 对吧

这个呢 也复制一下

复制

只要在这个controller当中啊

来提供这么一个方法就可以了

好

因为我们调用的这个getByID呢

前面已经解释过了

这是由mybyteplus提供的啊

这是由mybyteplus提供的啊

所以说呢 我们service呢

不用再做扩展了

然后呢 分页查询也是类似的

直接拿过来

这个配置呢 需要咱们手动来导一下

不要导错了

导的是我们mybyteplus

给我们提供的这个配置对象

然后呢 更新

也复制过来

然后呢 还有最后一个就是删除 对吧

把这个删除也复制过来

咱们呢 就是从讲义上啊

一次性的把咱们相关的

这应该是五个接口 对吧

全都复制过来

一会儿呢 我们整体来

测试一下

这些呢 都是一些比较简单的代码

但是呢 还必须有它

因为后边呢 我们是不是在项目当中

都会调用到这些代码

所以说呢 我们一次性给它导入就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”第3章“用户服务开发”中“5.4 服务接口开发”部分的教程。课程主要演示了如何在 Spring Boot 项目中，为用户信息模块开发一套完整的 RESTful API 接口。开发流程遵循标准的分层架构，从控制器（Controller）层开始，逐步向下创建服务（Service）层和数据映射（Mapper）层，并配置相应的 XML 映射文件。整个过程使用了 MyBatis-Plus 框架进行数据库操作，并通过 Swagger UI 进行接口测试和文档展示。视频内容涵盖了新增、根据ID查询、分页查询、更新和删除用户信息等核心功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程引入，展示项目结构和当前开发章节“5.4 服务接口开发”。
*   **00:05 - 00:15**: **第一步：创建 MemberController 并提供 save 方法**。在 `MemberController` 中定义 `@PostMapping` 的 `save` 方法，接收 `Member` 实体并调用服务层的 `save` 方法。
*   **00:15 - 00:25**: **第二步：创建 MemberService 接口**。定义 `IMemberService` 接口，声明 `save` 方法。
*   **00:25 - 00:35**: **第三步：创建 MemberServiceImpl 实现类**。实现 `IMemberService` 接口，继承 `ServiceImpl` 并注入 `MemberMapper`。
*   **00:35 - 00:45**: **第四步：创建 MemberMapper 接口**。定义 `MemberMapper` 接口，继承 `BaseMapper<Member>`。
*   **00:45 - 00:55**: **第五步：创建 XML 映射文件**。在 `resources/mapper` 目录下创建 `MemberMapper.xml` 文件，并配置 `namespace`。
*   **00:55 - 01:05**: **第六步：在 MemberController 中创建 detail 方法**。定义 `@GetMapping("/detail/{id}")` 的 `detail` 方法，用于根据ID查询用户详情。
*   **01:05 - 01:15**: **第七步：在 MemberController 中创建 page 方法**。定义 `@GetMapping("/page")` 的 `page` 方法，用于分页查询用户信息，使用 `Page<Member>` 和 `LambdaQueryWrapper`。
*   **01:15 - 01:25**: **第八步：在 MemberController 中创建 update 方法**。定义 `@PutMapping("/update/{id}")` 的 `update` 方法，用于更新用户信息。
*   **01:25 - 01:35**: **第九步：在 MemberController 中创建 del 方法**。定义 `@DeleteMapping("/delete/{id}")` 的 `del` 方法，用于删除用户信息。
*   **01:35 - 01:45**: **第十步：演示接口测试**。使用 Swagger UI 测试所有创建的接口，展示请求和响应。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   项目结构导航：`品达物流TMS项目` -> `第3章 用户服务开发` -> `5.4 服务接口开发` -> `5.4.1 新增用户信息` 等。
    *   代码注释：如 `// 用户前端控制器`、`// 新增`、`// 分页查询` 等。
    *   接口路径：`/member`、`/detail/{id}`、`/page`、`/update/{id}`、`/delete/{id}`。

*   **代码关键内容**:

    **1. MemberController.java**
    ```java
    @RestController
    @RequestMapping("member")
    public class MemberController {
        @Autowired
        private IMemberService memberService;

        // 新增
        @PostMapping("")
        public Result save(@RequestBody Member entity) {
            boolean result = memberService.save(entity);
            if (result) {
                return Result.ok();
            }
            return Result.error();
        }

        // 根据id查询
        @GetMapping("detail/{id}")
        public Member detail(@PathVariable(name = "id") String id) {
            Member Member = memberService.getById(id);
            return Member;
        }

        // 分页查询
        @GetMapping("page")
        public PageResponse<Member> page(Integer page, Integer pageSize) {
            Page<Member> iPage = new Page<>(page, pageSize);
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

        // 更新
        @PutMapping("/update/{id}")
        public Result update(@PathVariable(name = "id") String id, @RequestBody Member entity) {
            entity.setId(id);
            boolean result = memberService.updateById(entity);
            if (result) {
                return Result.ok();
            }
            return Result.error();
        }

        // 删除
        @DeleteMapping("/delete/{id}")
        public Result del(@PathVariable(name = "id") String id) {
            boolean result = memberService.removeById(id);
            if (result) {
                return Result.ok();
            }
            return Result.error();
        }
    }
    ```

    **2. IMemberService.java**
    ```java
    package com.itheima.pinda.service;
    import com.baomidou.mybatisplus.extension.service.IService;
    import com.itheima.pinda.entity.Member;
    public interface IMemberService extends IService<Member> {
    }
    ```

    **3. MemberServiceImpl.java**
    ```java
    package com.itheima.pinda.service.impl;
    import com.itheima.pinda.mapper.MemberMapper;
    import com.itheima.pinda.service.IMemberService;
    import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
    import org.springframework.stereotype.Service;
    @Service
    public class MemberServiceImpl extends ServiceImpl<MemberMapper, Member> implements IMemberService {
    }
    ```

    **4. MemberMapper.java**
    ```java
    package com.itheima.pinda.mapper;
    import com.baomidou.mybatisplus.core.mapper.BaseMapper;
    import com.itheima.pinda.entity.Member;
    import org.apache.ibatis.annotations.Mapper;
    @Mapper
    public interface MemberMapper extends BaseMapper<Member> {
    }
    ```

    **5. MemberMapper.xml**
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="com.itheima.pinda.mapper.MemberMapper">
    </mapper>
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建 Controller 层**
    *   **描述**: 教师在 IntelliJ IDEA 中创建 `MemberController` 类，使用 `@RestController` 和 `@RequestMapping` 注解。在类中定义 `save` 方法，使用 `@PostMapping` 注解，并通过 `@RequestBody` 接收 `Member` 实体对象，调用服务层方法。
    *   **演示**: 展示了如何在 IDE 中创建类、添加注解、编写方法体，并在 `MemberController` 中调用 `memberService.save(entity)`。

*   **场景二：创建 Service 层**
    *   **描述**: 教师创建 `IMemberService` 接口，声明 `save` 方法。随后创建 `MemberServiceImpl` 实现类，继承 `ServiceImpl` 并注入 `MemberMapper`。
    *   **演示**: 展示了如何定义接口和实现类，并通过 `@Service` 注解标记服务类。

*   **场景三：创建 Mapper 层**
    *   **描述**: 教师创建 `MemberMapper` 接口，继承 `BaseMapper<Member>`。并创建对应的 XML 映射文件 `MemberMapper.xml`。
    *   **演示**: 展示了如何在 `resources/mapper` 目录下创建 XML 文件，并配置 `namespace`。

*   **场景四：实现分页查询**
    *   **描述**: 在 `MemberController` 中创建 `page` 方法，使用 `Page<Member>` 和 `LambdaQueryWrapper` 进行分页查询。
    *   **演示**: 展示了如何使用 `Page` 对象和 `LambdaQueryWrapper` 构建查询条件，并返回 `PageResponse` 对象。

*   **场景五：接口测试**
    *   **描述**: 教师使用 Swagger UI 测试所有创建的接口，包括新增、查询、分页、更新和删除。
    *   **演示**: 展示了 Swagger UI 的界面，输入请求参数并查看返回结果，验证接口
