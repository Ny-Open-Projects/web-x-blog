# 89-规则引擎Drools-Drools实战（保险产品准入 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 接下来继续来看咱们这个实战

刚才呢我们是说到了这个决策表那对吧

这个决策表呢是我提前已经整理好的

并且刚才我们一块来看了一下

在这里边呢一共是设计了11条规则

对吧 11条规则

然后呢这些condition下边对应的这些呢

都是相关的一些约束条件

对吧 上面这一行呢

对应的是我们的这个什么呢

类型约束

然后下面这一行呢

是这个类型里边的属性约束

好 属性约束

跟这个condition平行的对吧

在这边呢就是action

就是具体这条规则成立之后啊

要做什么事

做的这个事呢其实都是一样的

都是像我们这个list的rules

这个全局变量里边

是不是来添加信息

只不过就是信息不一样

信息的内容不一样

你看我们是不是针对每一条规则

都对应的制定了不同的这个信息

你看交费方式必须是短交

或者是年交等等啊

就是这个提示信息不一样

好

接下来我们继续来看

下一步呢

我们需要来封装一个工具类啊

封装一个工具类

因为这块的操作啊

跟咱们前面的那些基于DRL规则文件的那些操作呢

不太一样

因为我们现在用的是这种excel文件

前面我们的API是不是也都讲过了

我们就需要把这些

比如说我把这个表格文件编译成我们的DRL

那种字符串的那方法

是不是要封装到这个工具类里面去

同时呢

获得session的那个方法呢

我们也封装到这个工具类里面去

来方便咱们的操作啊

因为我可能有多个地方都会用到它

所以我们先来封装出来这个工具类

先把这个包呢来创建一下

创建出来一个Utils这个包

然后这个工具类呢

就叫KIE Session Utils

把这个类创建出来

然后呢

我直接把这个类里边的内容啊

拷过来

其实这些代码呢

咱们应该都见过了

啊

在我们的工具类里面呢

我们就把这个代码呢

我们就把这个代码呢

把这个代码呢

在我们那个入门案例里面都已经见过了

只不过呢

我们现在呢

是把它封装了一下

把它封装到这个工具类里面来了

咱们可以来看一下

这个file呢

需要我们再手动导一下

其他的就没有了

然后呢

我们一块来大概读一下这个代码

首先呢

它是一个工具类对吧

一般情况下不用NEO

所以说呢

我把它这个构作方法变成私有的

这样你就NEO不了了

然后呢

这个地方封装了这么一个方法

叫做getDL

这个地方封装了这么一个方法

然后你看传进来是real path

它其实传进来的是我们的一个

磁盘上的一个excel文件

它的这个绝对路径对吧

磁盘路径

然后这段代码

咱们其实前面都已经见过了

最终呢

它会给我们返回这么一个字符串

这个字符串呢

代表的就是我们DRL

那个语法的这个字符串

然后在这呢

我们提供了这么一个方法

就是create session from DRL

这就是把咱们这个字符串

是不是给传进来

然后呢

通过这个

这个

kie helper

对吧

然后呢

最终来创建出来这么一个session

只不过在这儿的话

它在

我们多写了这么一句话

就是verify

这个其实就是校验

因为我们

有可能转换完的这个DRL文件呢

它的语法有问题

对吧

那这个时候呢

你的session肯定是创建不出来的

所以我们先来检查一下

校验一下

如果校验失败的话呢

它其实

它就会输出这样的异常信息

甚至呢

我们在这儿也可以往外抛异常

都是可以的

最后呢

把这个session给传进出来

都是可以的

然后呢

我们其实实际调的话呢

就可以直接调这个方法了

通过我们的工具类调这个方法就可以了

就是get kie session from xls

然后我们直接传进来一个什么呢

直接传进来咱们这个excel文件

它的磁盘路径

在这里边

你看它是先调了这个方法

get dr

这就是我们第一个方法

对吧

然后返回这个字符串

然后呢

在这儿是不是调了这个方法

其实就上面这个方法

最终返回这个session

好

这是关于咱们这个工具类呢

其实主要就是基于我们前面提到的这些API

来进行了一个封装

方便我们在项目当中来使用

好

那这样的话

我们这个工具类也有创建好了

再往下呢

我们就需要来创建一个ruler service了

因为我们具体跟这个规则引擎操作

主要就是通过这些service类来进行操作了

咱们直接把这个包呢

先来创建一下

这是创建了一个service包

然后呢

我们来创建这么一个ruler service类

好

ruler service这个类就创建好了

具体代码呢

我就不写了

咱们直接抄过来

然后呢

一块读一下这个代码

首先加service入解

这不用说了

对吧

然后呢

我们在这里边提供了这么一个方法

叫做insurance info check

其实就是我们制定的这个什么呢

保险产品准入准则的一个检查

哎

然后呢

我们在这传进来一个实体类

这个实体类里边肯定就封装了相关的这些

这些参数了

对吧

这些属性都已经封装好了

然后呢

我们来看看在这来进行校验

看看能不能教练通过

如果教练通过的话呢

那就是准数成功了

否则呢

就准数失败了

这个地方呢

我们就直接写死了

实际呢

我们如果在真实的项目当中啊

应该是可配置的

就是我们这个excel文件呢

放在什么位置是可配置的

在这呢

我就简单处理了

我们就固定了

地盘跟目录下面去找这个文件

去加载这个文件就可以了

当然了

我咱们现在呢

需要来提供一下

就是这个文件

Ctrl C

我复制一下

把它放到我们的地盘跟目录

好

就这个文件

一会呢

我们就加载这个文件

然后呢

你看它是不是调用我们工具类的这个方法

来返回一个session对象

然后有了这个session之后呢

我们需要把这个组

让它获取焦点

你看咱们所有的规则

是不是都属于

所有的规则

都属于这个组

你看这不是agenda group吗

咱们是不是写的都是同一个组名

所以说这些规则呢

都属于这个组

那么要想让它们触发的话呢

首先必须让它们获得焦点

对吧

set focus

这个前面已经讲过了

然后接下来呢

我们把这个实体类

对吧

实体对象

把它添加到我们的工作内存里面去

然后呢

我们就会来给它设置

这是什么呀

全球变量对吧

全球变量必须得设置进来

这是在咱们这个地方

通过这个variable

是不是定义的这个全球变量

必须得给进来

好

否则它程序就要报错了

全球变量

然后呢

我们调用这个fair

all rulers

对吧

然后呢

把这个规则给它触发了

反正这少一句啊

咱们是不是忘了

把这个session给关闭了

对吧

session关闭一下

好

dispose

然后呢

我们直接返回这个list rulers

其实就是这个全球变量

对吧

那么我们如何来判断

它准入是成功还是失败呢

主要就是

靠这个全球变量

如果这个全球变量里边啊

没有设置任何元素

这应该是准入成功还是失败

诶

注意啊

如果它这个size等于0

没有添加任何信息进去

那就说明我们

把这些规则都匹配了一遍

没有一个匹配成功的

其实是准入成功

因为我们写的这些

都是准入失败的条件

对不对

都是准备失败的条件

你看这不是

perimeters不等于这个北京

然后呢

它同时还不等于天津

而我们这个

销售区域是不是要求是这两个

所以大家要注意这个逻辑啊

你看我们这儿

其实这些条件

全都是反着写的

这写的是不等于

所以说呢

如果这个条件成立了

反而是准入失败

所以这个逻辑关系

大家要捋清楚

也就是说啊

如果它的size

这个集合

它的size等于0

没有添加元素进去

那应该是准入成功的

好

这是咱们这个service

就已经创建好了

并且我们把这个代码

大概读了一下

再往下呢

我们需要来创建一个controller

创建一个controller

通过controller

是不是去调用我们的这个service

来进行操作

咱们呢

先把这个包来创建一个

创建一下

内名我们也考过来

就叫ruler controller

这块呢

我们是模拟了一些数据啊

咱们就没有设计专门的页面啊

因为这块参数比较多啊

所以说的话

我们

就模拟了一下我们这个参数

模拟的数据

对吧

实际呢

应该是页面传递过来的信息

最终了都封装到我们这个对象上

对吧

这个实体内上

那我先整个考过来

咱们把这个代码一块读一下就可以了

把这整个替换一下

再来看

一个是加rescontroller

request mapping

这就不用说了

对吧

然后呢

注入service

这不用说了

然后我们在这也是封装了这么一个方法

insurance info check

好

这是他的request mapping

所对应的值

然后呢

这扭了一个hashmap

这个map是干什么用的呢

其实是给我们这个页面用的

最终我会把这个map返回个页面

页面的通过查看这个map里边设置的值

他就知道是准入成功还是失败了

好

然后接下来呢

我们在这是不是构造了一个假数据

对吧

实际当中啊

这些参数

这些值

对吧

我选中的这些值应该都是页面给我们提交过来的

因为我们在这呢

没有设计页面

所以说我们就在这啊

模拟了一下

用了一些模拟数据

然后接下来呢

我们把这个对象相当于就封装好了

对吧

封装好之后

调用service

把这个对象传进去

最后他会给我返回这个list的集合

这个其实对应的就是我们那个全局变量

对吧

然后呢

我们刚才也分析了

如果他不等于空

然后他的size大于0

这说明什么呢

我们在这里边是不是设置了信息

设置了信息

那就意味着准入是失败的

所以你看我map点put

这个

这个

check result等于false

没有检查通过

对吧

准入失败了

这个message呢

就是准入失败

并且呢

把我们这个详细信息

放进去

放进去的就是这个list集合

好

else的话呢

那就是准入成功

对吧

所以你看这个check result呢

这个key所对应的值呢

就是true

然后呢

具体的提示信息呢

就是准入成功

好

最终把这个map是不是返回

如果cat说明出异常了

对吧

出异常的话呢

应该就是我们意料之外的错误

这个写的是

这个未知错误

最终呢

都是把这个map返回给页面

OK

这块呢

我们是简单处理了一下

主要就是这个模拟假数据这块

咱们没有提供真实的页面

好

这是关于controller

就已经提供好了

最后呢

咱们是不是再编写一个什么呢

启动类就可以了

编写一个启动类

就叫derose application

把这个启动类创建出来

整个这块我复制一下

好

那么关于咱们这个案例啊

代码开发部分呢

我们先说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为一个关于 **Drools 规则引擎在 Spring Boot 项目中实战应用** 的教学片段。课程通过一个“保险产品准入规则”的具体案例，演示了如何将业务规则从 Excel 表格中提取并编译为 DRL（Drools Rule Language）文件，然后通过 Java 代码加载、执行规则，并最终通过 REST API 接口对外提供服务。整个过程涵盖了项目结构搭建、规则文件创建、工具类开发、服务层实现和控制器层开发等关键步骤，旨在教授学员如何将复杂的业务逻辑通过规则引擎进行解耦和动态管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 课程开场，展示 Excel 文件 `insuranceInfoCheck.xls`，其中包含保险规则的定义表。
*   **00:00:05 - 00:00:15**: 展示 DRL 规则文件的结构，说明规则的条件和结论部分。
*   **00:00:15 - 00:00:30**: 开始讲解“第五步：封装工具类 `KieSessionUtils`”，在 IntelliJ IDEA 中编写 Java 代码，用于将 Excel 文件解析为 DRL 字符串，并创建 KieSession。
*   **00:00:30 - 00:00:45**: 继续编写 `KieSessionUtils` 类，实现 `getKieSessionFromXLS` 方法，用于从 Excel 文件加载规则并返回 KieSession。
*   **00:00:45 - 00:01:00**: 讲解“第六步：创建 `RuleService` 类”，在 IntelliJ IDEA 中创建新的 Java 类。
*   **00:01:00 - 00:01:15**: 在 `RuleService` 类中定义 `InsuranceInfo` 实体类，用于封装保险产品的各项参数。
*   **00:01:15 - 00:01:30**: 在 `RuleService` 类中编写核心业务逻辑，包括创建 KieSession、插入事实对象、执行所有规则并返回结果。
*   **00:01:30 - 00:01:45**: 展示 Excel 文件中“保险期间与交费期间特殊搭配规则”的内容。
*   **00:01:45 - 00:02:00**: 讲解“第七步：创建 `RuleController` 类”，在 IntelliJ IDEA 中创建新的 Java 类。
*   **00:02:00 - 00:02:15**: 在 `RuleController` 类中编写 REST API 接口，模拟前端传入的保险信息。
*   **00:02:15 - 00:02:30**: 在 `RuleController` 类中编写业务逻辑，调用 `RuleService` 的方法，并根据返回结果构建响应数据。
*   **00:02:30 - 00:02:45**: 展示 `DroolsApplication` 启动类，用于启动 Spring Boot 项目。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **文档标题**: `视频Drools讲义.md`，其中包含详细的课程大纲，如“8.3.1 创建空间、项目”、“9.1 个人所得税计算器”、“9.3 保险产品准入规则”等。
    *   **规则表结构**: 在 Excel 文件中，规则表包含“规则”、“保险公司Code”、“销售区域”、“投保年龄”、“保险期间”、“交费期间”、“交费方式”、“保险期间与交费期间特殊搭配规则”等列。
    *   **规则示例**:
        *   `规则1`: `param1 = "picc"` (保险公司Code)
        *   `规则2`: `param2 = "北京"`, `param2 = "天津"` (销售区域)
        *   `规则3`: `param5 = 0.17` (投保年龄)
        *   `规则4`: `param6 = 20,25,30` (保险期间)
        *   `规则5`: `param7 = 1,3,5,10,15,20` (交费期间)
        *   `规则6`: `param8 = 1,2` (交费方式)

*   **代码关键内容**:
    *   **`KieSessionUtils.java`**:
        ```java
        public static String getDRL(String realPath) throws FileNotFoundException {
            File file = new File(realPath);
            InputStream is = new FileInputStream(file);
            SpreadsheetCompiler compiler = new SpreadsheetCompiler();
            String drl = compiler.compile(is, InputType.XLS);
            System.out.println(drl);
            return drl;
        }

        public static KieSession createKieSessionFromDRL(String drl) throws Exception {
            KieHelper kieHelper = new KieHelper();
            kieHelper.addContent(drl, ResourceType.DRL);
            Results results = kieHelper.verify(Message.Level.WARNING, Message.Level.ERROR);
            if (results.hasMessages(Message.Level.WARNING, Message.Level.ERROR)) {
                List<Message> messages = results.getMessages(Message.Level.WARNING, Message.Level.ERROR);
                for (Message message : messages) {
                    System.out.println("Error: " + message.getText());
                }
                throw new IllegalStateException("Compilation errors were found. Check the logs.");
            }
            return kieHelper.build().newKieSession();
        }

        public static KieSession getKieSessionFromXLS(String realPath) throws Exception {
            return createKieSessionFromDRL(getDRL(realPath));
        }
        ```
    *   **`RuleService.java`**:
        ```java
        public List<String> insuranceInfoCheck(InsuranceInfo insuranceInfo) throws Exception {
            KieSession session = KieSessionUtils.getKieSessionFromXLS(realPath);
            session.getAgenda().getAgendaGroup(name: "sign").focus();
            session.insert(insuranceInfo);
            List<String> listRules = new ArrayList<>();
            session.setGlobal("listRules", listRules);
            session.fireAllRules();
            return listRules;
        }
        ```
    *   **`RuleController.java`**:
        ```java
        @RestController
        public class RuleController {
            @Autowired
            private RuleService ruleService;

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
                insuranceInfo.setParam3("3");
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
                } catch (Exception e) {
                    e.printStackTrace();
                    map.put("checkResult", false);
                    map.put("msg", "未知错误");
                }
                return map;
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：规则定义与解析** (00:00:00 - 00:00:30)
    *   **演示**: 展示 Excel 文件 `insuranceInfoCheck.xls`，其中包含“RuleTable insurance-rules”表。表中定义了多个规则，如“保险公司Code”、“销售区域”等，并在“CONDITION”列中用公式（如 `param1 = "picc"`）表示规则条件。
    *   **关键动作**: 通过 `SpreadsheetCompiler` 工具类，将 Excel 文件解析为 DRL 字符串，为后续规则引擎的加载做准备。

*   **场景二：工具类开发** (00:00:30 - 00:01:00)
    *   **演示**: 在 IntelliJ IDEA 中编写 `KieSessionUtils` 类。该类包含两个核心方法：`getDRL` 用于将 Excel 文件解析为 DRL 字符串，`createKieSessionFromDRL` 用于创建 KieSession 并进行规则编译验证。
    *   **关键动作**: 代码中展示了如何使用 `KieHelper` 和 `SpreadsheetCompiler` 来加载和验证规则，确保规则语法正确。

*   **场景三：服务层实现** (00:01:00 - 00:01:30)
    *   **演示**: 在 IntelliJ IDEA 中创建 `RuleService` 类。该类负责调用 `K
