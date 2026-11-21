# 90-规则引擎Drools-Drools实战（保险产品准入 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么刚才呢

咱们这个实战案例啊

我们这个代码呢

已经开发完了

但是这个地方呢

好像有一点错误啊

就这个地方

咱们现在读取的是

地盘下边的这个

rules

这个文件对吧

而我们刚才真正考过来的是

这个文件啊

所以这个文件名呢

我改一下啊

咱们现在希望让他读取的是

这个文件

好

从咱们刚刚考过来的

这个文件里面来进行读取

OK

那接下来呢

我们就可以来启动一下

咱们这个项目来测试一下了

直接来跑一下

我们这个main方法

这个端口号呢

还是8080

好

那接下来呢

我们来访问一下

咱们是不是要访问的

应该是我们的这个

controller吧

对吧

这个controller的这个方法

好

我们把这个地址呢

来写一下

应该是

localhost

然后是端口号是8080

后边应该是ruler

再往后呢

应该是跟着这个

这段

好

现在我们直接回车

好

大家看这个数据呢

已经返回回来了

而返回来的这个数据是什么呢

它其实是我们这个map

其实是这个map

你看我最终是不是返回了这个map

然后呢

它转成了json

为什么会转成json呢

就是因为我们这儿

是不是加了这个

rest controller注解

这样的话呢

它就会把这个返回值

转换成json

然后呢

通过输出流的方式

写回到我们的

浏览器页面上

好

咱们来看啊

这里边呢

你看这个message

msg对吧

是准入失败

这说明什么呢

说明应该是我们

这个if成立了

对吧

if成立了

所以你看我这个

msg是不是设置的是准入失败

并且呢

这个check result呢

是不是设置的是false

你看check result

设置的是false

然后呢

detail

detail对应的是谁呢

detail对应的应该是

这个list的集合

其实就是我们设置的

那个全局变量

对吧

全局变量

对吧

然后这里边呢

应该是已经有了很多信息

有了很多信息

你看一个是销售区域不正确

仅支持北京和天津

投报年龄在0到17岁之间

这些呢

因为什么呢

你看我们当前准备的这个数据

我这是不是设置的是上海啊

你看parameter4

代表的是这个销售区域

对吧

这个地方我设置的是上海

而我们仅支持北京和这个天津

比如说我现在啊

我想让上海也支持

那怎么办呢

哎

我们其实不用做任何这个代码上来说

不用做任何修改

我们只要修改一下这个规则文件

或者这个决策表这个文件就可以了

我想把上海也加进来

哎

怎么玩呢

非常简单

我们把这儿

哎

把上海给它添加上

上海

呃

注意啊

光添加这个还不行

因为这个地方呢

我们还得再来加一个逗号

然后呢

parameter4

然后不等于

哎

不等于

这应该是dollars3

dollars3是不是对应的

就是从上海这个地方来取值

好

咱们保存一下就可以了

保存完这个表格之后呢

我们这个项目也不用重启

也不用做任何修改

直接重新再来请求一下

注意看

哎

你看那条规则是不是就没有了

哎

那条就没有了

这就说明上海也支持了

对不对

哎

那么我们设置上海也是可以的

也是可以准入的

但是呢

因为年龄也不对

年龄也不对

嗯

所以说呢

他最终还是失败的

因为我们前面也提到过了

我们

设置的这11条规则

只要有任意一条触发了

那么都是准入失败的

都是准入失败的

你看我这样要求的头发年龄

是0到17岁之间

对吧

而这个地方我们设置的年龄

年龄是parameter5

这个parameter5

我给的是101

对吧

但是比较夸张了

比较夸张

哎

那也是说

不在他的年龄范围之内

如果说我希望什么呢

这一条也

也能符合他的要求

对吧

哎

那么我可以怎么做呢

嗯

把这块

这个年龄

这个我给你改成

比方说你改成102

哎

正好在我这个范围之内

啊

我这不是设置的是101吗

好

我把这改成102保存一下

重新我们再来执行一下这个规则

你看那条是不是也就没有了

好

以此类推啊

就是这个意思

所以说呢

我们使用这种

呃

决策表这种

呃

方式呢

其实有一个好处就是什么呢

我们的规则

呃

我们的规则是在这个excel文件里边的

对吧

那么我们只要修改这些指标值

然后呢

我们的规则马上就可以生效

对吧

你看咱们的程序是不是也不用做任何修改

并且呢

也不用重启

好

这是我们这个呃

实战呢

就已经说完了

并且呢

测试也是没有问题的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程旨在演示如何在 Java Web 项目中集成 DROOLS（一个基于规则的引擎）来实现业务规则的动态管理。课程通过一个“保险信息准入检查”的具体案例，从项目搭建、规则定义、服务层实现到控制器调用，完整地展示了 DROOLS 的应用流程。核心内容包括：
- **技术栈**：Spring Boot + DROOLS + Java。
- **核心概念**：将复杂的业务规则（如投保年龄、地区、缴费方式等）从代码中剥离，存放在外部文件（如 Excel 表格）中，通过规则引擎进行动态执行。
- **实现步骤**：创建 Spring Boot 项目、定义实体类、编写规则服务（RuleService）、创建控制器（RuleController）调用服务、并最终通过浏览器访问接口。
- **演示重点**：如何通过 `KieSession` 加载规则文件、插入数据、执行规则并返回结果。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下章节按画面出现的逻辑顺序排列，并标注了关键操作。

1.  **项目初始化与结构搭建 (0:00 - 0:30)**
    - 展示 IntelliJ IDEA 中的项目结构，包含 `src/main/java` 和 `src/main/resources`。
    - 重点展示 `DroolsApplication.java`，这是一个 Spring Boot 的启动类，用于启动整个应用。

2.  **创建实体类 (InsuranceInfo) (0:30 - 1:00)**
    - 展示 `InsuranceInfo.java` 文件，定义了保险信息的实体类，包含 `param1` 到 `param13` 等字段，用于存储投保人信息。

3.  **创建控制器 (RuleController) (1:00 - 1:30)**
    - 展示 `RuleController.java` 文件，定义了 HTTP 接口 `/insuranceInfoCheck`。
    - 代码中模拟了数据，创建 `InsuranceInfo` 对象并设置参数。
    - 通过 `@Autowired` 注入 `RuleService`，并调用其 `insuranceInfoCheck` 方法。

4.  **创建服务层 (RuleService) (1:30 - 2:00)**
    - 展示 `RuleService.java` 文件，这是业务逻辑的核心。
    - 代码中通过 `KieSessionUtils.getKieSessionFromLS("D:\\rules.xls")` 加载规则文件。
    - 使用 `session.insert(insuranceInfo)` 将数据插入到规则引擎中。
    - 使用 `session.fireAllRules()` 执行所有规则。
    - 通过 `session.getGlobal("listRules", List.class)` 获取规则执行结果。

5.  **规则定义 (Excel 文件) (2:00 - 2:30)**
    - 展示 Excel 文件 `insuranceInfoCheck.xls`，其中定义了具体的业务规则。
    - 规则以表格形式呈现，例如：
        - 检验保险公司 Code：`param1 == "picc"`
        - 检验销售区域：`param4 == "北京" || param4 == "天津" || param4 == "上海"`
        - 检验投保年龄：`Integer.parseInt(param5) >= 0 && Integer.parseInt(param5) <= 17`
        - 检验保险期间：`param6 == "20" || param6 == "25" || param6 == "30"`
        - 检验交费期间：`param7 == "1" || param7 == "2"`
        - 检验缴费方式：`param8 == "1" || param8 == "2"`

6.  **前端调用与结果展示 (2:30 - 3:00)**
    - 展示浏览器访问 `http://localhost:8080/rule/insuranceInfoCheck`。
    - 页面返回 JSON 数据，包含 `checkResult`（true/false）和 `msg`（“准入成功”或“准入失败”）以及 `detail`（失败原因列表）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **PPT / 文档内容**

- **课程大纲**：在 Typora 中展示的课程大纲，包含“9. DROOLS 实战”章节，其中“9.3 保险产品准入规则”是本次课程的核心。
- **规则定义表**：在 Excel 中展示的规则表，是 DROOLS 规则的来源。表格结构清晰，包含“规则”、“条件”、“结果”等列。

#### **代码关键内容**

- **`DroolsApplication.java` (Spring Boot 启动类)**：
    ```java
    @SpringBootApplication
    public class DroolsApplication {
        public static void main(String[] args) {
            SpringApplication.run(DroolsApplication.class);
        }
    }
    ```

- **`InsuranceInfo.java` (实体类)**：
    ```java
    public class InsuranceInfo {
        private String param1; // 保险公司
        private String param2; // 方案代码
        private String param3; // 保单号
        private String param4; // 销售区域
        private String param5; // 投保年龄
        private String param6; // 保险期间
        private String param7; // 缴费方式
        private String param8; // 保障类型
        private String param9; // 等待期
        private String param10; // 等待期
        private String param11; // 职业类型
        private String param12; // 保额限制
        private String param13; // 保额限制
    }
    ```

- **`RuleController.java` (控制器)**：
    ```java
    @RequestMapping("/insuranceInfoCheck")
    public Map insuranceInfoCheck() {
        Map map = new HashMap();
        InsuranceInfo insuranceInfo = new InsuranceInfo();
        insuranceInfo.setParam1("picc");
        insuranceInfo.setParam4("上海");
        insuranceInfo.setParam5("101");
        insuranceInfo.setParam6("12");
        insuranceInfo.setParam7("222");
        insuranceInfo.setParam8("1");
        insuranceInfo.setParam13("3");

        try {
            List<String> list = ruleService.insuranceInfoCheck(insuranceInfo);
            if (list != null && list.size() > 0) {
                map.put("checkResult", false);
                map.put("msg", "准入失败");
                map.put("detail", list);
            } else {
                map.put("checkResult", true);
                map.put("msg", "准入成功");
            }
            return map;
        } catch (Exception e) {
            // 处理异常
        }
    }
    ```

- **`RuleService.java` (服务层)**：
    ```java
    @Service
    public class RuleService {
        public List<String> insuranceInfoCheck(InsuranceInfo insuranceInfo) throws Exception {
            KieSession session = KieSessionUtils.getKieSessionFromLS("D:\\rules.xls");
            session.getAgendaGroup("sign").setFocus();

            session.insert(insuranceInfo);

            List<String> listRules = new ArrayList<>();
            session.setGlobal("listRules", listRules);

            session.fireAllRules();

            return listRules;
        }
    }
    ```

#### **公式 / 图表**

- **规则引擎核心公式**：
    - 规则引擎通过 `KieSession` 加载规则文件，执行规则时，会根据条件对插入的数据进行匹配和处理。
    - 规则执行结果通过 `setGlobal` 方法设置到全局变量中，供后续代码使用。

---

### 4) 关键场景与演示描述

1.  **场景一：项目结构与启动类演示**
    - **描述**：讲师在 IntelliJ IDEA 中展示项目结构，重点讲解 `DroolsApplication.java` 是 Spring Boot 的启动类，用于启动整个应用。
    - **演示**：在 `main` 方法中调用 `SpringApplication.run(DroolsApplication.class)`，并成功启动应用。

2.  **场景二：实体类与控制器代码演示**
    - **描述**：讲师展示 `InsuranceInfo.java`，说明其用于存储投保人信息。接着展示 `RuleController.java`，说明其负责接收 HTTP 请求并调用服务层。
    - **演示**：在控制器中模拟数据，创建 `InsuranceInfo` 对象并设置参数，然后调用 `ruleService.insuranceInfoCheck(insuranceInfo)`。

3.  **场景三：服务层与规则引擎交互演示**
    - **描述**：讲师展示 `RuleService.java`，说明其负责执行规则引擎。
    - **演示**：通过 `KieSessionUtils.getKieSessionFromLS("D:\\rules.xls")` 加载规则文件，然后调用 `session.insert(insuranceInfo)` 插入数据，`session.fireAllRules()` 执行规则，最后通过 `session.getGlobal("listRules", List.class)` 获取结果。

4.  **场景四：规则定义与结果展示**
    - **描述**：讲师展示 Excel 文件 `insuranceInfoCheck.xls`，说明其中定义了具体的业务
