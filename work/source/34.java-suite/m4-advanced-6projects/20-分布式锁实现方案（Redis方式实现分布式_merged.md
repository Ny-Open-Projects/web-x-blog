# 20-分布式锁实现方案（Redis方式实现分布式 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看基于Redis这种方式来实现分布式锁

接下来我们来看版本三

版本三的话,它也是针对版本二做了一点优化

就是什么呢,加锁还有解锁必须是同一个客户端

或者说应该是同一个现成

所以在加锁的时候我们可以设置什么呢,当前现成的ID

你看我们前面这个set

set它的key是mylock

它的value是不是也是mylock

而现在我就可以把这个value给它改成什么呢

改成我们当前现成的ID

然后当我删除锁的时候也来判断一下

是否是同一个现成

如果是同一个现成,我们再来释放

这其实就是什么呢,加锁和解锁必须是同一个客户端

或者说应该是同一个现成

那么这个代码写起来其实也是比较简单的

咱们只是在这个地方

我们可以把这个代码写起来

这个我就不再手敲了

我们把这个现成的ID来获取一下

你看thread.currentthread.getID

然后呢

给它加一个空串

因为什么呢

这个ID呢

它返回的其实是一个lang形

对吧

然后呢

我给它转成string类型

因为我们这个地方呢

其实是使用的这个set命令

设置的这个值呢

是string类型的

所以这个地方呢

我们就可以给它改成什么呢

这个threadID

好

现成ID作为这个值

对吧

作为value

然后的话呢

我们在这个地方呢

释放锁的时候呢

就不要直接去释放了

而是来判断一下

对吧

判断一下

就是我们当前这个现成的ID

那么跟我们这个

也就是判断一下

我们这个当前现成ID

跟我们这个获取出来的这个值

是否相等

因为我们存进去的

是不是就是现成ID

所以这个地方呢

我们需要给它来获取一下

在这个地方呢

来获取一下

好

这样

然后你看

我们是不是先来get

mylock

然后呢

把存的这个值拿出来

存的值拿出来

然后呢

如果它等于当前现成

这个时候呢

我们是不是再来释放

就可以了

这个代码的话呢

我们就不再测试了

大概读一下就行了

其实就是说明了一个什么问题呢

就是我们这个

加锁

还有释放锁

必须是同一个客户端

对吧

你不能说

这个现成把其他的人家那个锁给释放了

对吧

保证是同一个

加锁和解锁必须是同一个现成

所以说呢

我们在释放锁的时候

来判断一下就可以了

这就是咱们第三个版本

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”第9章“后台管理端开发”的一部分，主题为“分布式锁”的实现。讲师正在讲解如何使用 Redis 实现一个更健壮的分布式锁，重点是“版本三”的优化方案。该方案的核心思想是：在加锁时记录当前线程的 ID，然后在释放锁时，通过比对存储的线程 ID 来判断锁是否由当前线程持有，从而避免“误删”其他线程的锁，提高系统的安全性。讲师通过在 IntelliJ IDEA 中展示 Java 代码，并在 Typora 文档中同步展示代码逻辑和注释，进行详细讲解。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **章节 1: 课程引入与目录概览 (0:00 - 0:30)**
    *   展示了课程的 Typora 文档大纲，明确指出本节内容为“2.3.3 版本三”。
    *   讲师介绍了本节要讲解的优化方案。

*   **章节 2: 版本三核心逻辑讲解 (0:30 - 2:00)**
    *   讲师在 Typora 文档中展示并解释了“版本三”的核心思想：加锁时设置当前线程 ID，释放锁时验证线程 ID。
    *   展示了对应的 Java 代码片段，重点讲解了 `setIfAbsent` 方法和后续的 `get` 方法用于验证。

*   **章节 3: 代码实现与调试 (2:00 - 4:00)**
    *   讲师切换到 IntelliJ IDEA，展示 `StockController.java` 文件中的完整代码。
    *   通过鼠标悬停和代码高亮，详细解释了 `redisTemplate.opsForValue().setIfAbsent("mylock", threadId, 5, TimeUnit.SECONDS);` 这行代码的作用。
    *   讲师重点讲解了 `if (threadId.equals(myValue))` 这个条件判断语句，说明了其在防止“误删”锁中的关键作用。

*   **章节 4: 代码优化与总结 (4:00 - 结束)**
    *   讲师在 Typora 文档中再次强调了“版本三”的优势。
    *   展示了最终的、包含完整逻辑的 Java 代码。
    *   通过多窗口（IDEA、Redis Desktop Manager、JMeter）的切换，暗示了后续可能进行的性能测试或实际部署。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容 (Typora):**
    *   **标题:** “2.3.3 版本三”
    *   **核心文字:** “针对前面版本二还有一点需要优化，就是加锁和解锁必须是同一个客户端，所以在加锁时可以设置当前线程id，在释放锁时判断是否为当前线程加的锁，如果是再释放锁即可。”
    *   **代码片段:**
        ```java
        @GetMapping("/stock")
        public String stock() {
            try {
                String threadId = Thread.currentThread().getId() + "";
                // 尝试加锁
                Boolean locked = redisTemplate.opsForValue().setIfAbsent("mylock", threadId, 5000, TimeUnit.MILLISECONDS);
                if (locked) { // 加锁成功
                    int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
                    if (stock > 0) {
                        stock--;
                        redisTemplate.opsForValue().set("stock", stock + "");
                        System.out.println("库存扣减成功，剩余库存：" + stock);
                    } else {
                        System.out.println("库存不足！！！");
                    }
                } else {
                    System.out.println("没有获得锁，不能执行减库存操作！！！");
                }
                // 释放锁
                String myValue = redisTemplate.opsForValue().get("mylock");
                if (threadId.equals(myValue)) {
                    redisTemplate.delete("mylock");
                } else {
                    System.out.println("没有获得锁，不能执行减库存操作。。。");
                }
            } catch (Exception ex) {
                System.out.println("出现异常！！！");
            }
            return "OK";
        }
        ```

*   **代码 (IntelliJ IDEA):**
    *   **文件:** `StockController.java`
    *   **关键方法:** `public String stock()`
    *   **关键逻辑:**
        *   **加锁:** `boolean locked = redisTemplate.opsForValue().setIfAbsent("mylock", threadId, 5, TimeUnit.SECONDS);`
        *   **获取库存并扣减:** `int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));`
        *   **释放锁:** `String myValue = redisTemplate.opsForValue().get("mylock"); if (threadId.equals(myValue)) { redisTemplate.delete("mylock"); }`
        *   **异常处理:** `catch (Exception ex) { System.out.println("出现异常！！！"); }`

---

### 4) 关键场景与演示描述

*   **场景 1: 代码逻辑对比与讲解 (Typora)**
    *   讲师在 Typora 文档中，通过高亮和滚动，对比了“版本二”和“版本三”的代码差异。
    *   重点讲解了“版本三”中新增的 `String myValue = redisTemplate.opsForValue().get("mylock");` 和 `if (threadId.equals(myValue))` 语句，说明了其在防止“误删”锁中的作用。

*   **场景 2: IDE 代码调试与高亮 (IntelliJ IDEA)**
    *   讲师在 IntelliJ IDEA 中，将鼠标悬停在 `redisTemplate.opsForValue().setIfAbsent("mylock", threadId, 5, TimeUnit.SECONDS);` 这行代码上，IDE 自动弹出方法的详细说明，帮助观众理解其功能。
    *   讲师通过高亮 `if (threadId.equals(myValue))` 这行代码，强调了其在释放锁时的判断逻辑。

*   **场景 3: 多窗口切换与系统集成 (多窗口)**
    *   讲师在 Typora 文档中展示了多个窗口，包括 IntelliJ IDEA、Redis Desktop Manager 和 JMeter。
    *   这暗示了该分布式锁的实现不仅限于代码层面，还需要配合 Redis 数据库进行存储和管理，并且可以用于性能测试。

*   **场景 4: 代码优化与最终展示 (Typora)**
    *   讲师在 Typora 文档中，最终展示了完整的“版本三”代码，并对其中的关键逻辑进行了总结。
    *   通过滚动和高亮，确保观众能够清晰地看到整个代码的结构和流程。
