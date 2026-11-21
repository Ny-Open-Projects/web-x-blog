# 77-规则引擎Drools-Drools实战（个人所得税计 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才呢咱们是把我们这个静态资源文件呢已经拷进来了

拷进来了一个ATML页面

咱们大概来打开看一下

这个页面呢其实还是非常简单的

上面呢就一个表格对吧

这是表头这是我们的这个一个标题

个人所得税计算器2011版

然后呢税前月收入

税前月收入这是一个输入框对吧

然后呢我们这儿呢使用到的是我们VOE啊

它这个V-model

然后进行这个数据绑定的

然后下边呢有一个计算的按钮

一点击它呢会触发这么一个方法

叫calculate这个方法

calculate这个方法

这块呢的报错呢

是因为我们当前使用到的这个语法呢

是比较新的这个ECS6的语法

我们可以把它来切换一下

ECM script 6对吧

给它切换一下

这样它就能识别这种语法了

好

然后呢这个地方呢

我们是不是调用到这个方法

然后呢首先来判断一下

我们输入的这个税前月收入啊

是否小于等于3500

因为这个地方呢

如果你是小于3500的话

其实都不用计算

因为你根本就不用交税对吧

不用交税的话还有什么要算的吗

所以说如果判断一下

小于等于3500

我们直接alert一下

然后呢return

后边就不再执行了

如果你输入的是大于等于3500

大于3500的情况了

这个时候呢

它就会发一个一步请求

一价格请求

然后呢这个路径呢

正好匹配到的

就是咱们刚才编写的这个control了

你看这个路径

并且呢把我们这个位置

也就是我们的税前

这个月收入

对吧

给传过来

传过来之后呢

咱们是不是

在这个zend

这就是我们阿达克斯

相当于它的回调方法

对吧

在这里边呢

把我们的结果取到

取到之后呢

付给我们当前这个对象

这个对象是谁呢

是我在这定义的

而这个对象呢

你看它这里边

是不是对应的

就是我们这些属性啊

税后工资啊

什么扣税额啊

等等这些

通过我们为这个对象付值

然后呢

通过voe的数据绑定啊

它就可备了

可以自动显示到我们对应的

这些输入框里面去了

这是关于前端的一些东西啊

咱们大概读一下这个代码就可以

接下来呢

我们就来测试一下

代码我们目前都已经完成了

接下来呢

我们来启动一下咱们这个项目

要启动的话呢

我们直接啊

因为它是一个spring boot的工程

直接啊

来运行一下这个min方法

就可以了

那么这个启动过程呢

我们需要来稍等它一下

先观察一下控制台

是不是能启动成功

好这已经跑起来了

没有报错

如果没有报错的话

那说明我们应该编写的还可以啊

然后呢

我们来执行一下

打开一个浏览器

当前呢

我们使用的端口呢

是8080端口啊

logo host的

然后呢

端口号是8080

再往后应该是什么呢

再往后

咱们来看一下我们的control了

是不是应该就是ruler

对吧

ruler

再往后呢

是不是就是我们的calculate啊

呃

不是这个啊

不用我们直接访问control了

对吧

咱们直接访问我们的页面就可以啊

咱们这个页面是不是就叫calculation.html

所以我们不用访问control了

直接访问我们的页面

这个页面呢

就叫calculation

对吧

calculation.html

好

先访问一下这个页面

你看现在我们是不是已经访问到这个页面了

访问到这个页面之后呢

我们在这来输入税前月收入

比如说我输入一个300对吧

哎

这个时候呢

肯定是提示呀

然后呢

我们在这输入个1万

然后呢

计算

哎

你可以看到他下边是不是已经计算完了

呃

是745

这是扣税额

然后呢

税后工资是9255啊

然后看我们的控制台呢

其实也有输出

这个就是从哪输出的呢

就是在我们的规则文件里边

对吧

我在这是不是输出了一堆啊

然后还有一句输出啊

下面这句输出呢

应该是在咱们的controller里边吧

看一下

controller里边有一句输出一句啊

好

然后呢

我们也可以换一个

比如说我把这改成1万5对吧

改成1万5

然后呢

重新计算一下

你可以看到他是不是又重新计算了

啊

1万5的时候呢

他的这个应纳税所得额呢

就是这么多

对吧

然后税率呢

是0.25

素算扣除数就是这个啊

扣税额呢

就是这个

税后工资呢

就是这个

这个规则呢

就是根据我们在规则文件里边

是吧

定的这些规则来计算的

其实实际计算的过程啊

核心的逻辑都是在规则文件里边

啊

这些页面展示的呢

只是把我们计算的结果

给我们展示一下而已

好

这是关于咱们这个个人计算

个人所得税啊

计算器就已经完成了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频演示了一个基于 **Spring Boot** 和 **Drools** 规则引擎的个人所得税计算器的完整开发与运行流程。核心内容包括：
*   **前端界面**：使用 **Vue.js** 框架（通过 `v-model` 绑定数据）构建一个简单的 HTML 表单，用于用户输入税前工资、税率、速算扣除数等信息。
*   **后端逻辑**：通过 **Vue.js** 的 `axios` 库向后端发起 HTTP 请求，调用 **Drools** 规则引擎进行计算。
*   **规则引擎**：在 **Drools** 的 `.drl` 文件中定义了计算规则，该规则根据输入的工资、税率和速算扣除数，计算出应纳税所得额、扣税额和税后工资。
*   **后端服务**：使用 **Spring Boot** 框架，通过 `@RestController` 和 `@PostMapping` 等注解，提供一个 RESTful API 接口，接收前端请求并调用 Drools 引擎进行计算。
*   **演示结果**：最终在浏览器中展示计算结果，验证了整个系统的正确性。

整个过程展示了如何将前端、后端和规则引擎集成在一起，实现一个动态的、可配置的业务计算系统。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: 项目结构概览。展示 IntelliJ IDEA 中的项目结构，包括 `src/main/java`、`src/main/resources` 等目录，以及 `DroolsApplication.java`、`calculation.html`、`calculation.drl` 等核心文件。
*   **00:15 - 00:30**: 前端 HTML 页面开发。在 `calculation.html` 文件中，使用 HTML 和 Vue.js 指令（如 `v-model`）创建表单，定义了“税前月收入”、“税率”、“速算扣除数”等输入框和“计算”按钮。
*   **00:30 - 00:45**: 前端 JavaScript 逻辑。在 `<script>` 标签中，编写了 Vue 实例的 `calculate` 方法。该方法首先检查税前收入是否大于 3500，然后使用 `axios` 发起一个 POST 请求到 `/rule/calculate` 接口，将 `cal.wage` 作为参数传递。
*   **00:45 - 01:00**: 后端服务启动。在 `DroolsApplication.java` 中，通过 `SpringApplication.run()` 启动 Spring Boot 应用。在终端中可以看到应用启动日志，确认服务已成功启动。
*   **01:00 - 01:15**: Drools 规则文件开发。在 `calculation.drl` 文件中，定义了一个名为“个人所得税：计算税后工资”的规则。规则的条件是 `wage > 0 && wagemore > 0 && cess > 0`，执行体中包含计算逻辑，如 `wageminus = ...` 和 `actualwage = ...`。
*   **01:15 - 01:30**: 规则执行与调试。在 `calculation.drl` 文件中，添加了 `System.out.println(...)` 语句用于调试，打印出计算过程中的各个变量值。在终端中可以看到打印的计算结果。
*   **01:30 - 01:45**: 前端页面展示。在浏览器中打开 `localhost:8080/calculation.html`，输入税前工资 15000，点击“计算”按钮，页面自动填充计算结果，包括应纳税所得额、税率、速算扣除数、扣税额和税后工资。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **前端 HTML 代码**：
    ```html
    <input type="text" v-model="cal.wage">
    <input type="button" value="计算" @click="calculate()">
    <input type="text" v-model="cal.wagemore">
    <input type="text" v-model="cal.cess">
    <input type="text" v-model="cal.preminus">
    <input type="text" v-model="cal.wageminus">
    <input type="text" v-model="cal.actualwage">
    ```

*   **前端 JavaScript 代码**：
    ```javascript
    calculate() {
        if(this.cal.wage <= 3500) {
            alert("税前月收入需要大于3500!");
            return;
        }
        axios.get('/rule/calculate?wage=' + this.cal.wage).then((res) => {
            console.log(res);
            this.cal = res.data;
        });
    }
    ```

*   **Drools 规则文件 (calculation.drl) 代码**：
    ```drl
    rule "个人所得税：计算税后工资"
    salience 80
    when
        $cal : Calculation(wage > 0 && wagemore > 0 && cess > 0)
    then
        // 扣税额
        double wageminus = $cal.getWagemore() * $cal.getCess() - $cal.getPreminus();
        double actualwage = $cal.getWage() - wageminus;
        $cal.setWageminus(wageminus);
        $cal.setActualwage(actualwage);
        System.out.println("税前工资：" + $cal.getWage());
        System.out.println("应纳税所得额：" + $cal.getWagemore());
        System.out.println("税率：" + $cal.getCess());
        System.out.println("速算扣除数：" + $cal.getPreminus());
        System.out.println("扣税额：" + $cal.getWageminus());
        System.out.println("税后工资：" + $cal.getActualwage());
    end
    ```

*   **后端 Java 代码 (DroolsApplication.java)**：
    ```java
    @SpringBootApplication
    public class DroolsApplication {
        public static void main(String[] args) {
            SpringApplication.run(DroolsApplication.class);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:00-00:15)**
    *   **描述**：讲师在 IntelliJ IDEA 中展示了项目的整体结构，包括 `src/main/java`、`src/main/resources` 等目录。重点突出了 `DroolsApplication.java`、`calculation.html`、`calculation.drl` 等核心文件，为后续开发做铺垫。

*   **场景二：前端页面开发 (00:15-00:30)**
    *   **描述**：讲师在 `calculation.html` 文件中，使用 HTML 标签和 Vue.js 指令创建了一个简单的表单。通过 `v-model` 将输入框与 Vue 实例的数据属性（如 `cal.wage`）绑定，实现了数据的双向绑定。

*   **场景三：前端计算逻辑 (00:30-00:45)**
    *   **描述**：讲师在 `<script>` 标签中编写了 Vue 实例的 `calculate` 方法。该方法首先进行输入校验，然后使用 `axios` 发起一个 GET 请求到 `/rule/calculate` 接口，将 `cal.wage` 作为参数传递。请求成功后，将服务器返回的数据赋值给 Vue 实例，从而更新页面显示。

*   **场景四：后端服务启动 (00:45-01:00)**
    *   **描述**：讲师在 `DroolsApplication.java` 中，通过 `SpringApplication.run()` 启动 Spring Boot 应用。在终端中，可以看到应用启动日志，确认服务已成功启动并监听 8080 端口。

*   **场景五：Drools 规则开发 (01:00-01:15)**
    *   **描述**：讲师在 `calculation.drl` 文件中，定义了一个名为“个人所得税：计算税后工资”的规则。规则的条件是 `wage > 0 && wagemore > 0 && cess > 0`，执行体中包含计算逻辑，如 `wageminus = ...` 和 `actualwage = ...`。讲师还添加了 `System.out.println(...)` 语句用于调试。

*   **场景六：规则执行与结果展示 (01:15-01:30)**
    *   **描述**：讲师在终端中运行了 `calculation.drl` 文件，可以看到打印的计算结果。结果包括税前工资、应纳税所得额、税率、速算扣除数、扣税额和税后工资。

*   **场景七：前端页面最终演示 (01:30-
