# 68-实现动态规则（实现步骤_4） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们是把这个command line runner这个类呢已经创建好了对吧

这个呢可以做到在我们项目启动的时候呢来执行我们这个run方法

这样的话呢它就会重新读取我们数据库中最新的规则对吧

然后呢把kiecontainer对象来创建出来

那接下来呢我们需要来创建一个controller

然后呢提供一个方法

这个就是什么呢当我们项目启动完成之后对吧

这个时候我如果希望这个我规则发生了变化对吧

比如说我数据库中的规则发生了变化

我只要执行一下这个调用一下这个controller的这个方法

然后呢就会重新是不是来执行我们这个reload的方法

然后呢这样就达到了什么呢

在我们不停服务的情况下来切换规则对吧

所以呢需要来提供这么一个controller

这个controller呢咱们就叫什么呢

叫做ruler reload controller

然后呢我们在这来创建这么一个controller

然后呢这个代码呢我就不再手敲了

咱们把这个

这个复制一下

然后呢这里边呢只要提供一个方法

就是reload的方法就可以对吧

然后呢这就相当于我们对外暴露的一个接口啊

先把这个刚才那个service注进来

是不是就是这个reload

reload

dioservice

把它注入一下

然后呢我们在这呢来提供这么一个方法

对吧提供这么一个方法

这个方法呢就是对外暴露成一个服务接口

然后呢我们如果

希望啊来这个重新加载对吧

重新加载直接调用一下这个reload的方法就可以啊

这个地方的报错呢是因为命名不一致啊

把它改一下就行了

所以这个代码呢还是非常简单的

应该reload啊

直接调用这个service reload的方法

这样的话我们的规则重新加载一遍对吧

然后呢container重新创建一遍

这样的规则呢就已经实现了动态规则了

好

这一步呢就已经搞定了

这个比较简单

然后接下来呢我们下一步呢

需要把这个什么呢

derose auto configuration啊

把这个自动配置类把它注释掉

为什么要注释掉它呢

因为我们现在呢

大家看我们这个kie container等等

这一套对象了

其实是在什么呢

是在我们这个service的这个方法上是不是来创建的

那么我们原先啊编写的这个derose auto configuration

其实这个配置类呢就不需要了

你看我们原先这个配置类呢

它加载规则文件是不是是从我们这个rules目录下边来加载

现在呢我们其实这些文件都不需要了对吧

甚至我都可以把它删掉

那么我们的规则内容呢全都是存在数据库里面

所以当前啊这个配置配置类

那么整个呢就不需要了

但是咱也不需要把它删掉啊

直接把这个什么呢

configuration啊

把这个注解给它注释起来

这样的话呢

它当前这个配置类呢

其实就不再生效了啊

把它注释起来就可以了

那么这个类呢我们就不把它删除了

就注释掉它

然后呢我们需要注意

在我们这个什么呢

service

就是order service mpr里边

咱们是不是来计算我们订单价格对吧

当时呢我们创建这个key session的时候呢

就需要来修改一下

咱们来看一下

找到这个类再说

在这个order service mpr

再来看啊

我们这个地方呢

是不是当时是获得了一个这个session对吧

而这个session的话是怎么来的呢

是通过我们这个key container创建的

而这个key container呢

这个key container怎么来的呢

我们是不是直接注入的

直接注入的

而现在呢我是不是已经把什么呢

把我们这个自动配置类是不是给这个注释起来了

那这样的话呢

在我们sprint容器里面还有这个什么container对象吗

很显然是没有了

对吧

就是这个key container

那么这个配置类呢

相当于就已经删除掉了

对吧

它已经不起作用了

那么这个时候呢

我们key container其实就没有了

没有的话

你在这儿

再通过autoware的注释之后呢

注入的话呢

很显然它其实就注不进来了

它就注不进来了

那这个怎么办呢

咱们是不是在我们刚才看到的这个reload的这个service里边提供了一个静态的对吧

所以现在呢

我们使用这个静态的这个container就可以了

所以你看啊

我们把这个session创建呢

使用这个reload的这个什么service

然后呢

使用它这个静态的container来创建

只要把这儿

在哪儿了

这儿呢

这儿呢

这儿呢

这儿呢

这儿呢

这儿呢

这儿呢

这儿呢

这儿呢

这儿呢

这边

这边

然后呢

找到这个地方

大家来看

我们现在使用的就是这个reload the rules

对吧

然后它这里边

这就是我们定义的这个静态的这个container

好

然后使用它来创建一个session

那这样的话

我们上面这个container其实就没有用了

咱们给它注释起来就可以了

好

注释一下

OK

那么整个呢

我们这个动态规则呢

其实就已经搞定了

一会儿呢

我们来整体测试一下

测试一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程讲解了如何在 Spring Boot 项目中集成 Drools 规则引擎，并实现规则的动态加载与执行。课程通过一个“品达物流 TMS 项目”的实例，逐步演示了从创建一个用于启动时加载规则的 `CommandLineRunner`，到创建一个 HTTP 接口用于触发规则重载，再到配置 `DroolsAutoConfiguration` 自动化加载规则文件，最后修改业务服务层 `OrderServiceImpl` 中的 `calculateAmount` 方法，将规则引擎的 `KieSession` 注入并用于实际的订单价格计算。整个过程旨在展示如何将业务规则与代码解耦，实现业务规则的灵活配置和动态更新。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从截图中获取精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **章节 1: 创建启动时加载规则的组件 (00:00:00 - 00:02:00)**
    *   在 `src/main/java/com/itheima/pinda/service/impl/` 目录下创建 `CommandLineRunnerImpl.java`。
    *   代码中使用 `@Component` 注解，实现 `CommandLineRunner` 接口。
    *   在 `run` 方法中调用 `rules.reload()` 来触发规则的重新加载。

*   **章节 2: 创建 HTTP 接口用于触发规则重载 (00:02:00 - 00:04:00)**
    *   在 `src/main/java/com/itheima/pinda/controller/` 目录下创建 `RulesReloadController.java`。
    *   使用 `@Controller` 和 `@RequestMapping("/rules")` 注解。
    *   定义 `reload` 方法，通过 `@ResponseBody` 返回 "ok"，并调用 `rules.reload()`。

*   **章节 3: 配置 Drools 自动化加载 (00:04:00 - 00:07:00)**
    *   在 `src/main/java/com/itheima/pinda/config/` 目录下创建 `DroolsAutoConfiguration.java`。
    *   使用 `@Configuration` 注解。
    *   定义 `kieFileSystem` Bean，用于扫描 `src/main/resources/rules/` 目录下的规则文件。
    *   定义 `kieContainer` Bean，用于构建 Drools 的容器。
    *   定义 `kieBase` 和 `kieSession` Bean，分别用于获取规则库和会话。

*   **章节 4: 修改业务服务层以使用规则引擎 (00:07:00 - 00:10:00)**
    *   在 `src/main/java/com/itheima/pinda/service/impl/` 目录下修改 `OrderServiceImpl.java`。
    *   在 `calculateAmount` 方法中，注入 `kieContainer`。
    *   通过 `kieContainer.newKieSession()` 获取 `KieSession`。
    *   创建 `AddressRule` 对象并设置参数。
    *   将对象插入会话，并调用 `fireAllRules()` 触发规则。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容:**
    *   **第五步:** 创建 `CommandLineRunnerImpl`，用于项目启动时加载最新规则。
    *   **第六步:** 创建 `RulesReloadController`，用于提供 HTTP 接口。
    *   **第七步:** 注解 `DroolsAutoConfiguration`，实现规则的自动化加载。
    *   **第八步:** 修改 `OrderServiceImpl` 中的 `calculateAmount` 方法，修改 `KieSession` 的获取方式。

*   **关键代码片段:**

    **1. `CommandLineRunnerImpl.java` (第五步)**
    ```java
    package com.itheima.pinda.service.impl;

    import com.itheima.pinda.service.ReloadDroolsRulesService;
    import org.springframework.boot.CommandLineRunner;
    import org.springframework.stereotype.Component;
    import javax.annotation.Resource;

    @Component
    @Slf4j
    public class CommandLineRunnerImpl implements CommandLineRunner {
        @Resource
        private ReloadDroolsRulesService rules;

        @Override
        public void run(String... args) throws Exception {
            rules.reload();
        }
    }
    ```

    **2. `RulesReloadController.java` (第六步)**
    ```java
    package com.itheima.pinda.controller;

    import com.itheima.pinda.service.impl.ReloadDroolsRulesService;
    import org.springframework.stereotype.Controller;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.ResponseBody;

    @Controller
    @RequestMapping("/rules")
    public class RulesReloadController {
        @Resource
        private ReloadDroolsRulesService rules;

        @ResponseBody
        @RequestMapping("/reload")
        public String reload() throws IOException {
            rules.reload();
            return "ok";
        }
    }
    ```

    **3. `DroolsAutoConfiguration.java` (第七步)**
    ```java
    package com.itheima.pinda.config;

    import org.kie.api.KieServices;
    import org.kie.api.KieContainer;
    import org.kie.api.KieBase;
    import org.kie.api.KieSession;
    import org.kie.api.builder.KieBuilder;
    import org.kie.api.builder.KieFileSystem;
    import org.kie.api.builder.KieRepository;
    import org.kie.api.runtime.KieContainer;
    import org.kie.api.runtime.KieSession;
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.Configuration;
    import org.springframework.context.annotation.ConditionalOnMissingBean;
    import org.springframework.context.annotation.Scope;
    import org.springframework.context.annotation.ScopedProxyMode;
    import org.springframework.core.io.Resource;
    import org.springframework.core.io.ResourceLoader;
    import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
    import org.springframework.core.io.support.ResourcePatternResolver;
    import org.springframework.stereotype.Component;
    import org.springframework.stereotype.Service;
    import org.springframework.web.context.annotation.RequestScope;

    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;

    @Configuration
    public class DroolsAutoConfiguration {

        @Value("${rules.path:rules}")
        private String RULES_PATH;

        @Bean
        @ConditionalOnMissingBean(KieFileSystem.class)
        public KieFileSystem kieFileSystem() throws IOException {
            KieFileSystem kieFileSystem = getKieServices().newKieFileSystem();
            for (Resource file : getRulesFiles()) {
                kieFileSystem.write(ResourceFactory.newClassPathResource(path: RULES_PATH + "/" + file.getFilename()));
            }
            return kieFileSystem;
        }

        private Resource[] getRulesFiles() throws IOException {
            ResourcePatternResolver resourcePatternResolver = new PathMatchingResourcePatternResolver();
            return resourcePatternResolver.getResources("classpath*:" + RULES_PATH + "/*.drl");
        }

        @Bean
        @ConditionalOnMissingBean(KieContainer.class)
        public KieContainer kieContainer() throws IOException {
            KieRepository kieRepository = getKieServices().getRepository();
            kieRepository.addModule(getReleaseId() -> return kieRepository.getDefaultReleaseId());
            KieBuilder kieBuilder = getKieServices().newKieBuilder(kieFileSystem());
            kieBuilder.buildAll();
            KieContainer kieContainer = getKieServices().newKieContainer(kieRepository.getDefaultReleaseId());
            return kieContainer;
        }

        private KieServices getKieServices() {
            return KieServices.Factory.get();
        }

        @Bean
        @ConditionalOnMissingBean(KieBase.class)
        public KieBase kieBase() throws IOException {
            return kieContainer().getKieBase();
        }

        @Bean
        @ConditionalOnMissingBean(KieSession.class)
        public KieSession kieSession() throws IOException {
            return kieContainer().newKieSession();
        }
    }
    ```

    **4. `OrderServiceImpl.java` (第八步)**
    ```java
    package com.itheima.pinda.service.impl;

    import com.itheima.pinda.entity.Order;
    import com.itheima.pinda.entity.OrderDTO;
    import com.itheima.pinda.mapper.OrderMapper;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Service;

    import java.util.HashMap;
    import java.util.Map;

    @Service
    public class OrderServiceImpl implements OrderService {

        @Autowired
        private KieContainer kieContainer;

        @Override
        public Map calculateAmount(OrderDTO orderDTO) {
            // 计算订单距离
            orderDTO.setDistance(this.getDistance(orderDTO));

            // 创建规则对象
            AddressRule addressRule = new AddressRule();
            addressRule.setTotalWeight(orderDTO.getTotalWeight().doubleValue());
            addressRule.setDistance(orderDTO.getDistance().doubleValue());

            // 创建结果对象
            AddressCheckResult addressCheckResult = new AddressCheckResult();

            // 创建会话
            KieSession session = kieContainer.newKieSession();

            // 插入对象
            session.insert(addressRule);
            session.insert(addressCheckResult
