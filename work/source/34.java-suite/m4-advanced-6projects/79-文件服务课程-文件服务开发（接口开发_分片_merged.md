# 79-文件服务课程-文件服务开发（接口开发_分片 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个tranks merge啊,比如我们分片合并的这个方法,刚才呢,我们大体的逻辑呢,其实已经写的差不多了,还差最后一点点,就是需要对我们这个什么呢,传进来的这个trank files,其实是一个文件数组,文件集合,对吧,粒子集合这么一个对象,需要对这里边这些file进行一个排序,对吧,

嗯,但是这儿还有一个问题啊,我们刚才落了一句啊,咱们这不是获得锁对象了吗,对吧,哎,那么还需要来调用它的一个lock方法,来加锁,对吧,你看我们刚才是不是在这个finally里边来unlock啊,这是释放锁,这个是加锁,好,好,那么把这个给它放上就可以了,然后接下来呢,我们要做的就是这块啊,对我们集合中分片文件呢,进行排序,那么怎么排序呢,大家可以看一下,我们其实所有的分片文件呢,全都是用数字,

自命名的,哎,0,1,2,3,不管有多少个啊,全都是数字,所以说呢,我们在这个地方呢,就按照文件名,因为它是数字呢,所以按照文件名呢,进行一个排序就可以,好,你看我们为什么非得要把这个,呃,这些文件呢,把它封装成一个粒子的集合,而不是数组呢,其实就是想在这个地方呢,使用到我们这个集合它的一个sort啊,排序的方法,你看到没有,sort,排序的方法,然后呢,排序的话呢,咱们是不是要传进来一个comparator,对吧,这么一个对象,

啊,来进行排序,呃,在这个地方呢,我们还是使用这么一个拉姆的表达式啊,好,咱们这个地方,比方说有个f1,这代表第一个文件,对吧,还有一个是f2,这代表第二个文件,然后呢,他们具体这个排序的这个先后顺序是一个什么样的先后顺序呢,是不是应该是根据我们的这个什么,呃,根据我们这个文件名,对吧,因为文件名都是它的这个整形的一些数字,对吧,啊,所以说呢,我们直接啊,获得它这个文件名,来通过什么,

f1.什么get name,然后呢,还有f2.get name,然后呢,来通过我们这个指定的这个啊,叫做number helper,啊,helper,它这个工具类,对吧,然后呢,这个工具类里边有个叫做int value of,啊,然后呢,把我们这个name呢,给它转成什么呢,转成int类型,啊,转成int类型,因为呢,你直接get name,它是string四幅串,对吧,四幅串的话呢,没法比较,所以说呢,我们在这个地方呢,通过int value of,啊,

然后呢,把咱们这个f1.get name,获得到,对吧,然后呢,让它减去什么呢,哎,这个既然变成整形了,是不是,int类型了,是不是,就可以进行相减了,对吧,然后呢,number helper.什么int value of 0,然后呢,这个应该是f2.什么get name,好,大家来看一下,我们传进来的这一段,

嗯,当然我们这个地方呢,需要简单处理一下,这这个应该是,呃,不用咱们这个括号了,不用括号了,哎,直接这是相当于对应的就是一个表达式,对吧,而不是一个代码块,好,它是这么一个结构,大家来看,其实就是把我们第一个文件名,对吧,给它拿出来,然后转成int类型,然后呢,再把第二个文件名拿出来,转成int类型,然后呢,让第一个文件名是不是减去第二个文件名,哎,因为这个呢,是直接是我们整形数值的一个相减,对吧,通过这种方式呢,哎,

根据我们的文件名是不是来进行一个排序,啊,这个其实整个对应的,整个对应的就是我们这么一个叫做comparator,哎,这么一个对象,啊,传进来其实就这么一个对象,而这个呢,它是一个函数式接口,对吧,函数式接口,啊,然后呢,我们这里边相当于实现的就是这么一个comparer,compare,哎,这么一个方法,啊,然后传进来这么两个参数,啊,根据它返回的值来确定谁先谁后,对吧,啊,好,这个呢,这是根据我们的文件名,然后呢,进行一个排序,啊,这个呢,这是根据我们的文件名,然后呢,进行一个排序,啊,这个呢,这是根据我们的文件名,

排序,这个就搞定了,呃,然后呢,我们当前这个类呢,还有最后一个方法呢,我们没有实现,啊,就是清理相应的文件目录,啊,哎,这个方法就是我们刚才创建的叫做clear space,对吧,好,那接下来呢,我们把这个方法把它实现了,就可以了,好,那么这个方法相对来说是比较简单的,呃,这里边呢,我们主要删除的有这么两个,一个是咱们这个文件夹,对吧,还有一个就是这个临时文件,啊,那有的同学们呢,就会觉得这个方法是比较简单的,啊,那有的同学们呢,就会觉得这个方法是比较简单的,啊,那有的同学们呢,就会觉得这个

就可能说,那这里边这个临时文件呢,其实我们直接把上一层这个文件夹把它删除掉,里边的临时文件呢,一块也就删除掉了,所以说我们在这个地方主要删除的一个是删除什么呢,删除我们存放什么,呃,我们这个分片文件的这个目录,呃,然后呢,还要删除什么呢,删除我们那个,呃,点tmp的这个临时文件,对吧,临时文件,好,然后这个目录的话呢,是比较简单的,咱们是不是

把它封装成一个java.io.file对象,对吧,这是我们的目录啊,咱们就叫folder吧,好,等于什么呢,呃,直接直接我们来new一个,呃,这不能叫folder了,因为这个也叫folder,对吧,好,这这叫我们这个trunk吧,trunk folder,好,直接new一个java.io.file,好,呃,这个路径的话呢,注意,这个路径的话是不是应该就是我们path叫folder,

对吧,刚才我们也说过了,path呢,对应的是到我们这个月份这层目录,对吧,而那个folder呢,对应的是咱们这个文件夹名字,哎,所以说呢,把它俩加一块啊,啊,应该是path加上我们这个就可以了,呃,这个路径呢,我们还是使用这个path来拼一下get,这样呢,是比较准确的,一个是path,然后一个是folder,好,然后呢,别忘了去tostring,对吧,给它转成字母串,这样的话呢,我们这个文件夹是不是对象就已经构造好了,构造好之后呢,我们呢,就可以去tostring,对吧,给它转成字母串,这样的话呢,我们这个文件夹是不是对象就已经构造好了,�

我们直接调用什么呢,直接调用它的一个delete quietly,这么一个方法就可以了,啊,叫做delete,啊,我们也可以直接使用工具类啊,咱们在工具类里面,这个fileutils啊,我们是不是有这个工具类的吧,叫做fileutils.delete quietly,然后呢,把咱们这个fang,啊,trunk folder,喊进去,好,这样呢,就是删除我们整个这个文件夹,包括里边的这个临时文件呢,

这个分片文件呢,也就一块删除掉了,然后接下来呢,我们可以来删除这个临时文件,对吧,这个临时文件的话呢,它其实是什么呢,大家需要注意啊,它的构成是在我们当前这个path下边,文件名呢,应该是文件夹,那个folder,然后加上一个.tmp,对吧,它是这么一个构成啊,所以我们接下来呢,需要把这个对象呢,来构造一下,啊,这是我们那个临时文件,它其实也是一个java.io.file,对吧,

这是我们那个tmpfile吧,啊,等于new一个什么呢,呃,java.io.file,好,然后呢,它这个路径呢,是这样拼的,也是通过path,对吧,.什么呢,呃,get,然后呢,第一个是我们的path,然后呢,是加上我们的这个folder,对吧,然后呢,再加上什么呢,这个folder加上一个.tmp,对吧,这是咱们这个构成的规则,哎,别忘了啊,to string一下,

好,这样呢,其实就把我们整个这个,呃,把这个临时文件是不是给找到了,然后找到之后呢,我们把它删了就可以了,直接也是通过我们这个file.utils,啊,delete,quietly,然后呢,把这个tmpfile传进去,好,这个呢,就是把我们这两部分文件是不是都给它删除掉,就可以了,好,那么到这儿的话呢,我们整个啊,咱们这个,呃,抽象类,对吧,这是我们这个分片处理的抽象类,

已经写完了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个 Java 项目中文件分片合并功能的代码实现教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `AbstractFileChunkStrategy` 类中实现文件分片合并的核心逻辑。主要内容包括：
- **文件分片合并的条件判断**：检查实际分片数量是否等于预期数量。
- **并发控制**：使用 `FileLock` 对文件夹进行加锁，确保操作的原子性。
- **分片文件排序**：使用 `Stream` API 和 `Comparator` 对分片文件按名称进行排序，以便后续合并。
- **分片合并**：调用子类实现的 `merge` 方法进行实际的文件合并操作。
- **资源清理**：合并完成后，清理临时文件和分片文件夹。
- **异常处理**：对合并过程中的异常进行捕获并记录日志。

整个过程体现了面向对象设计、策略模式的应用，以及 Java 8+ Stream API 和集合框架的使用。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:05**: 展示 `AbstractFileChunkStrategy.java` 文件中 `merge` 方法的入口，条件判断 `if (chunks == chunksNum)`。
*   **0:05 - 0:10**: 代码块中添加 `try-catch` 块，并实例化 `FileLock` 对象。
*   **0:10 - 0:15**: 在 `try` 块中调用 `lock.lock()` 进行加锁。
*   **0:15 - 0:20**: 调用 `getChunks` 方法获取所有分片文件的 `List<File>`。
*   **0:20 - 0:25**: 使用 `Stream` API 对 `chunkFiles` 进行排序，调用 `sort` 方法。
*   **0:25 - 0:30**: 为 `sort` 方法提供 `Comparator`，使用 `NumberHelper.intValueOf` 方法比较文件名的整数值。
*   **0:30 - 0:35**: 展示 `Comparator` 接口的定义，解释其作用。
*   **0:35 - 0:40**: 回到主方法，调用 `merge` 方法进行文件合并。
*   **0:40 - 0:45**: 调用 `cleanSpace` 方法清理临时文件和分片文件夹。
*   **0:45 - 0:50**: 展示 `cleanSpace` 方法的实现，创建 `chunkFolder` 对象。
*   **0:50 - 0:55**: 使用 `delete()` 方法删除临时文件夹。
*   **0:55 - 1:00**: 展示 `cleanSpace` 方法中导入的包和类，如 `java.io.File`。
*   **1:00 - 1:05**: 展示 `merge` 方法的抽象定义，以及 `cleanSpace` 方法的参数和注释。
*   **1:05 - 1:10**: 展示 `AbstractFileChunkStrategy` 类的结构，包括 `@Autowired` 注解和 `merge` 方法的实现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (文件分片合并条件)**:
    ```java
    if (chunks == chunksNum) {
        // 数量足够，可以进行分片的合并操作
        Lock lock = FileLock.getLock(folder);
        try {
            lock.lock();
            // 获取所有分片文件
            List<java.io.File> chunkFiles = this.getChunks(Path.get(path, folder).toString());
            // 对chunkFiles集合中的分片文件进行排序
            chunkFiles.sort((f1, f2) -> {
                NumberHelper.intValueOf(f1.getName()) - NumberHelper.intValueOf(f2.getName());
            });
            // 调用子类具体分片合并方式实现分片的合并
            R<File> result = this.merge(chunkFiles, fileName, fileChunksMergeDTO);
            // 清理分片文件、目录、临时文件
            this.cleanSpace(folder, path);
            return result;
        } catch (Exception ex) {
            log.error("分片合并失败");
        }
    }
    ```

*   **代码片段 2 (Comparator 接口定义)**:
    ```java
    @FunctionalInterface
    public interface Comparator<T> {
        /**
         * Compares its two arguments for order. Returns a negative integer,
         * zero, or a positive integer as the first argument is less than,
         * equal to, or greater than the second.
         *
         * In the foregoing description, the notation
         * <tt>sgn(<tt>i</tt>expression<i></tt>)</tt> designates the mathematical
         * <tt>signum</tt> function, which is defined to return one of
         * <tt>-1</tt>, <tt>0</tt>, or <tt>1</tt> according to whether the value of
         * <tt>expression<i></tt> is negative, zero or positive.
         */
        int compare(T o1, T o2);
    }
    ```

*   **代码片段 3 (getChunksNum 方法)**:
    ```java
    public int getChunksNum(String path) {
        java.io.File folder = new java.io.File(path);
        java.io.File[] files = folder.listFiles();
        if (file.isDirectory()) {
            return false;
        }
        return files.length;
    }
    ```

*   **代码片段 4 (cleanSpace 方法)**:
    ```java
    public void cleanSpace(String folder, String path) {
        // 删除存放分片文件的目录
        java.io.File chunkFolder = new java.io.File(Path.get(path, folder).toString());
        // 删除临时文件
        chunkFolder.delete();
    }
    ```

*   **代码片段 5 (merge 方法的抽象定义)**:
    ```java
    protected abstract R<File> merge(List<java.io.File> files, String fileName, FileChunksMergeDTO fileChunksMergeDTO);
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 文件分片合并逻辑的实现**
    讲师在 `AbstractFileChunkStrategy.java` 文件中，从 `if (chunks == chunksNum)` 条件开始，逐步添加 `try-catch` 块和 `FileLock` 对象，演示了如何确保文件合并操作的线程安全。

*   **场景 2: 使用 Stream API 对分片文件排序**
    讲师将光标移动到 `chunkFiles.sort(...)` 方法，并使用 `Stream` API 进行排序。他通过 `NumberHelper.intValueOf` 方法将文件名转换为整数，以便进行数值比较，从而实现按文件名排序。

*   **场景 3: Comparator 接口的使用**
    讲师切换到 `Comparator.java` 文件，展示了 `Comparator` 接口的定义和 `compare` 方法的作用，解释了其在排序中的重要性。

*   **场景 4: 清理临时文件和分片文件夹**
    讲师演示了 `cleanSpace` 方法的实现，通过创建 `File` 对象并调用 `delete()` 方法，实现了对临时文件夹的清理。

*   **场景 5: 代码结构与注释**
    讲师展示了 `AbstractFileChunkStrategy` 类的结构，包括 `@Autowired` 注解和 `merge` 方法的实现，强调了策略模式的应用和代码的可扩展性。

整个视频通过代码演示和注释，清晰地讲解了文件分片合并的核心逻辑和实现细节。
