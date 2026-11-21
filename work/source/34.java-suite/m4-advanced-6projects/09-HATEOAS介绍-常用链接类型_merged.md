# 09-HATEOAS介绍-常用链接类型 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着学习一下HeadOS的常用链接类型。

那在这里呢,有一个列表,

这里呢,列出了HeadOS的对应的链接类型,

以及呢,它的详细说明。

我们可以看一下,在这里有哪些呢?

像Self,它的意思呢,是指向当前资源本身的链接。

Edit呢,它是指向一个可以编辑当前资源的链接。

Connection呢,如果是当前资源包含在某个集合当中呢,

它是指向该集合的一个链接。

Search呢,是指向一个可以搜索当前资源,

并且呢,与其相关资源的一个链接。

那么Related呢,是指向一个与当前资源的相关链接。

在这里呢,还有什么?

First, Last,以及呢, Previous。

这个呢,就是它的一个集合便利所对应的指向性的操作链接。

比如说,First呢,

是指向第一个,对不对?

Last呢,是指向最后一个。

Previous呢,是上一个。

Next呢,就是下一个。

那么我们看一下,具体事例是怎样的呢?

比如说,这里抓取了一个HitOS的软块的数据包。

这个数据包里面的话呢,我们可以看到,

最外层呢,有List,对吧?

然后呢,有Device。

Device下面的话有什么?有Link。

那在Link的话呢,我们可以看到,

这个Rail呢,就是我们所描述的常用的链接类型。

这个Rail,我们可以看到,

有很多种,对不对?

那在这里呢,

事例当中是一个Self。Self代表是什么意思呢?

它代表就是指向当前

资源本身的链接。

也就是说,这个链接的话呢,

就是它资源本身呢,所提供出来的。

那么Next的话呢,

是什么意思呢?是指向下一个。

比如说,我这个接口呢,

换回到了这个数据,对不对?

那么的话呢,

这个是当前资源的链接。

如果说,我这边的话呢,

还要请求,下一个资源呢,

那么它在这里呢,

给出了你对应的提示,就是Next。

然后呢,你拿了这个

接口地址去做请求,就可以了。

好,这样的话呢,是不是就

比较直观?甚至呢,

可以去省略对应的API

接口文档。这个呢,

也就是HeadOS为什么会这么去

设计,也是它的一些

优势和作用。

那这一讲呢,咱们先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面内容，进行的结构化中文输出：

---

### 1) 视频摘要

本视频片段来自一门关于 RESTful API 设计的课程，具体讲解的是 HATEOAS（Hypermedia as the Engine of Application State，超媒体作为应用状态的引擎）的核心概念。讲师通过展示一个银行账户资源的 XML 响应示例，引出 HATEOAS 的核心思想：API 不仅返回数据，还应提供指向相关操作和资源的链接，从而引导客户端的下一步操作。视频的主要内容是详细介绍 HATEOAS 中常用的链接类型（REL），包括 `SELF`、`edit`、`collection`、`search`、`related`、`first`、`last`、`previous` 和 `next` 等，并通过一个设备列表的 XML 示例来说明 `next` 链接如何用于分页。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供具体的时间戳，以下章节结构是基于画面内容推断的逻辑顺序：

*   **00:00 - 00:05**: 课程大纲展示，当前位于“讲解”部分的“3.3 HATEOAS常用链接类型”。
*   **00:05 - 00:15**: 讲师展示一个银行账户的 XML 响应示例，其中包含多个 `link` 元素，用于演示 HATEOAS 的工作方式。
*   **00:15 - 00:30**: 讲师开始讲解“3.3 HATEOAS常用链接类型”表格，逐行介绍 `SELF`、`edit`、`collection`、`search`、`related` 等链接的含义。
*   **00:30 - 00:45**: 讲师讲解集合遍历相关的链接类型，包括 `first`、`last`、`previous` 和 `next`，并解释它们的作用。
*   **00:45 - 01:00**: 讲师展示一个设备列表的 XML 示例，其中包含 `self` 和 `next` 链接，用以说明分页机制。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **核心图表**: 一个名为“3.3 HATEOAS常用链接类型”的表格，包含两列：“REL”和“说明”。
    *   **表格内容**:
        *   `SELF`: 指向当前资源本身的链接。
        *   `edit`: 指向一个可以编辑当前资源的链接。
        *   `collection`: 如果当前资源包含在某个集合中，指向该集合的链接。
        *   `search`: 指向一个可以搜索当前资源与其相关资源的链接。
        *   `related`: 指向一个与当前资源相关的链接。
        *   `first`: 集合遍历相关的类型，指向第一个资源的链接。
        *   `last`: 集合遍历相关的类型，指向最后一个资源的链接。
        *   `previous`: 集合遍历相关的类型，指向上一个资源的链接。
        *   `next`: 集合遍历相关的类型，指向下一个资源的链接。

*   **代码示例**:
    *   **银行账户 XML 示例**:
        ```xml
        <account>
          <account_number>12345</account_number>
          <balance currency="usd">100.00</balance>
          <link rel="deposit" href="https://bank.example.com/accounts/12345/deposit" />
          <link rel="withdraw" href="https://bank.example.com/accounts/12345/withdraw" />
          <link rel="transfer" href="https://bank.example.com/accounts/12345/transfer" />
          <link rel="close" href="https://bank.example.com/accounts/12345/status" />
        </account>
        ```
    *   **设备列表 XML 示例**:
        ```xml
        <list>
          <device>
            ...
            <link rel="self" href="http://host:port/res/device/11"/>
          </device>
          ...
          <link rel="next" href="http://host:port/res/device?start=10&size=10"/>
        </list>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：HATEOAS 原理演示**
    *   **描述**: 讲师首先展示了一个 HTTP 响应，其内容类型为 `application/xml`，并展示了一个 XML 响应体。该响应体中包含一个 `<account>` 资源，以及多个 `<link>` 元素，分别指向 `deposit`、`withdraw`、`transfer` 和 `close` 等操作。这直观地演示了 HATEOAS 的核心思想：资源不仅包含数据，还包含指向其相关操作和资源的链接，从而引导客户端的下一步操作。

*   **场景二：常用链接类型讲解**
    *   **描述**: 讲师切换到“3.3 HATEOAS常用链接类型”表格，逐行讲解每种链接的含义。例如，`SELF` 链接用于指向当前资源本身，`edit` 链接用于指向编辑当前资源的接口，`collection` 链接用于指向包含当前资源的集合，`search` 链接用于指向搜索相关资源的接口，`related` 链接用于指向与当前资源相关的其他资源，`first`、`last`、`previous` 和 `next` 链接则用于集合的分页遍历。

*   **场景三：分页示例演示**
    *   **描述**: 讲师展示了一个设备列表的 XML 示例。该示例中，第一个 `<device>` 资源包含一个 `self` 链接，指向该设备的详细信息。在列表的末尾，有一个 `next` 链接，其 `href` 属性值为 `http://host:port/res/device?start=10&size=10`，表示可以通过该链接获取下一页的设备列表。这清晰地演示了如何使用 `next` 链接进行分页。
