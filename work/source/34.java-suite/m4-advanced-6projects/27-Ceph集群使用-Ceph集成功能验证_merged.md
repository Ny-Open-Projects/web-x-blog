# 27-Ceph集群使用-Ceph集成功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着对Safe的这个集成项目做个启动和验证

之前我们已经将代码做了具体实现

在这里面的话

我们可以看到它怎么做的

通过upload的操作去标示

我是要进行文件的上传

它的意思就是说将本地的文件上传到Safe集群当中

在这里我们指定了pass是我们本地的目录

然后axe是我们所传递的一个文件名称

那download的话是什么意思

是将这个Safe里面的指定文件就是axe

比如说我在这里面的话

我传了一个文件

这个文件的话是叫upload.txt

咱们写一下

是upload.txt

这个是咱们上传上去的文件

那么你下载的时候

你也要保持这个文件名

我们可以看到这两个参数就是一样的

对不对

如果说你上传是叫upload.txt

你下载的时候的话

你给它改了一个名字了

你下载的时候

你就不叫upload.txt

你另外起了一个名字叫upload.xt

那你想想

这个时候的话

它在Safe当中是找不到的

所以就不能下载成功

那这一点咱们要注意一下

这个就是一个上传还有下载的一个指定操作

那连接这一块是提供用户的名称

对不对

然后这个mode

连接IP信息

如果是我们有多台节点

在这里通过封号进行隔开

然后呢

冒号是IP和端口的一个连接配置

这个不要搞错

userkey的话

是你对应的这个user用户的

它的连接密钥信息

然后这个montpass

这个montpass的话

我们就让它再根据入境就可以了

好

那我们就来做一个上传和下载的测试验证

在启动验证之前呢

咱们要通过save demo打一个包

也就是maven

然后呢在这里面clean package

打成一个可以运行的加包

那我们呢在POM下面已经增加了Spring boot的构建插件

对不对

好

那这包打完之后呢

在它起的目录下面可以找到

好

找到这个save demo

加

那么呢要去copy它的一个路径

copy路径之后呢

我们就再去做一个测试验证

然后呢

然后将它上传到我们的主节点当中

因为我们之前呢

是在上面做了一个来钓死的客户端的连接验证

对不对

那同样我们在这里也做一个测试验证

大家可以看到

我已经呢将这个价包上传到呼吸当中了

如果是大家的话呢

第一次上传通过RJmini

然后将我们这个

啊

指定路径呢

填写

这样的话呢

就能够上传上去

好上传成功之后呢

咱们就可以呢

做一个测试验证

那首先呢

咱们的目录

本地目录呢

是在temp upload fs里面

也就是说我们是在这下面做了测试

save

temp

这里面的话呢

我们采用的是

upload fs进行了文件上传

那同样呢

它下载的时候呢

它是下载到temp download fs

这个呢

是在我们代码当中

做了一个指定

看到没有

已经是写死了一个配置

如果大家要去修改的话也可以

就是再增加一个参数就行了

那为了解密新鲜呢

咱们在这里是固定好了

路径

好

temp upload fs

在这里呢

之前已经是做过测试了

那我们可以呢

去temp

那咱们呢

再创建一个新的文件名称

就叫upload y.txt

那给它一个文件内容

就叫test idcast

123

这样呢

我们已经创建了一个新的文件

就可以进行一个上传验证

好

回到我们的目录

source

然后怎么去验证呢

通过java-mini

指向我们的demo

给它一个操作指定

对不对

upload

那么你还要给你上传的文件名称

你要上传哪个文件

好

这样呢

它就提示文件的传输成功

这个呢

上传就是ok的

那我们来验证一下

对吧

通过下载方法呢

来做一个测试

我们下载的话呢

就是download指定

同样的

这个文件名称不要搞错了

要保持一致

保证了它在save上面

是找不到这个文件的

我们点击下载

好

它提示呢

是100%

进度100%

已经是下载成功

那咱们就来看一下cat

save

test

temp

然后那个download

upload1.txt

好

这个时候可以看到内容是不是一致

好

在这里呢

我们来追一下

好像是多了一个对不对

多了这样一个特殊符

好

那我们来没关系

我们来验证看一下

uprod

然后呢fs

这个时候可以看到

因为我们在写的时候呢

不小心增加了一个特殊符

是吧

但是这个验证的话呢

是可以看到

上传跟下载内容其实是一致的

那就从中测试

从测试当中呢

就是上传跟下载的功能的话呢

都能够正常使用

通过这个演示呢

咱们可以看到

那个java client

在项目当中呢

是可以成功操作save机群的

那我们呢

多次上传

看一下是什么结果呢

upload

对吧

我再次进行上传

咱们就看一下结果

追加文件传输成功

如果咱们进行多次上传呢

咱们可以看一下它的实现逻辑

在这里面的话呢

有一个upload的方法

我们看一下upload它的处理流程

upload呢

它发现这个文件呢

如果是不存在就新增了

这个我们就不多讲

那么它如果是存在的话呢

在这里面

它又会进行一个写入

直接调用mount对象

再进行一个写入

mount对象的话

我们可以看到

它有个什么

last length

对不对

会获取你原来的这个文件大小

那么这样的话呢

它后面的数据呢

就是一个追加的方式写入

所以在下面我们可以看到

多次上传应该会进行一个追加

那是不是实际上是不是这样结果呢

咱们已经上传了两次对不对

按道理它应该要输入两行这个

好那我们就来重新下载一下

中国download

好

这样的话呢

我们把它删除吧

好了

让大家看起来更为直观一点

然后upload1.txt

咱们再下载一下

好download success

咱们再来看一下它的具体内容

是不是追加显示为两行

好这个时候可以看到

文件确实是追加进去的

好这个就是save的一个文件上传

和下载的操作演示

大家有兴趣的话

可以再多去研究它相关的API接口操作

就是加深对save这一块的运用和理解

好

在整个实践过程中

还会有很多的一些问题

如果运行过程当中出现

比如说GNI找不到动态库

需要安装相关的依赖

那怎么去安装呢

通过下面这个指令

然后去安装LiveSafeFS

这样的一些组件

这个也是老师在实践过程当中出现的一些坑

那大家如果是出现类似问题

就按照这个方法去做处理

在下面这个问题

如果Ledos玩宝是0.6.0的一个依赖

那么找不到的话怎么办

找不到我们可以

通过手工方式上传至Maven仓库

怎么手工上传呢

通过这个指令deploy

那么在那个Maven配置文件当中

大家一定要记得加上你的仓库的用户名和密码

这个话呢

我就不做过多赘述

大家可以通过这个指令进行一个上传

那Ledos 0.6.0这个价包呢

我倒是也会上传到咱们的课程资料当中

好

这个就是对save项目的集成的

功能测试验证

那这一讲咱们就先

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程演示了一个 Java 项目如何集成 Ceph 分布式文件系统（CephFS）进行文件上传和下载操作。核心内容包括：
- **项目构建**：使用 Maven 和 Spring Boot 插件构建项目，生成可执行的 JAR 文件。
- **CephFS 服务配置**：在 CentOS 7 服务器上配置 CephFS 服务，并设置上传/下载目录。
- **Java 服务实现**：编写 `CephOperator` 类，通过 `rados-java` 库与 CephFS 交互，实现文件上传和下载功能。
- **命令行测试**：通过命令行执行 JAR 文件，测试上传和下载功能，并验证文件内容。
- **常见问题处理**：演示了如何解决运行时因缺少 `libcephfs2` 库或 `rados` 版本不兼容导致的错误。

整个过程旨在展示如何将 CephFS 作为后端存储，集成到 Java 应用中，实现文件的管理。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **章节 1: 项目构建与打包 (00:00 - 00:30)**
  - 展示 `pom.xml` 文件，配置 Spring Boot 插件。
  - 通过 `mvn clean install` 命令生成 `ceph-demo.jar` 文件。

- **章节 2: 上传文件到 CephFS (00:30 - 00:50)**
  - 使用 `rz` 命令将 JAR 文件上传至远程服务器。
  - 在服务器上创建上传目录 `/temp_upload_fs` 并创建测试文件 `upload.txt`。
  - 使用 `java -jar ceph-demo.jar upload upload.txt` 命令执行上传。

- **章节 3: 下载文件从 CephFS (00:50 - 01:10)**
  - 使用 `java -jar ceph-demo.jar download upload.txt` 命令执行下载。
  - 验证下载的文件内容，确认文件完整无误。

- **章节 4: 代码实现与核心逻辑 (01:10 - 01:40)**
  - 展示 `CephDemoApplication.java` 的 `main` 方法，解析命令行参数并调用 `CephOperator`。
  - 展示 `CephOperator.java` 的 `uploadFileByPath` 方法，演示如何打开文件、读取数据并写入 CephFS。

- **章节 5: 常见问题与解决方案 (01:40 - 02:00)**
  - 解决 `libcephfs2` 库缺失问题，使用 `yum install` 命令安装。
  - 解决 `rados` 版本不兼容问题，演示如何手动上传依赖到 Maven 仓库。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT 页面标题**：`4. 测试验证`，`5. FAQ问题`。
- **PPT 内容**：
  - `测试验证`：通过 `maven` 命令 `clean install` 打包生成 `ar` 文件。
  - `上传至cephfs服务`：使用 `java -jar ceph-demo.jar upload upload.txt` 命令。
  - `下载cephfs文件`：使用 `java -jar ceph-demo.jar download upload.txt` 命令。
  - `FAQ问题`：
    1. 安装 `libcephfs2` 库：`yum -y install libcephfs2 libcephfs_jni-devel`。
    2. 手动上传 `rados` 依赖到 Maven 仓库。

#### 代码关键内容

- **`pom.xml` 配置**：
  ```xml
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>
  ```

- **`CephDemoApplication.java` 主方法**：
  ```java
  public static void main(String[] args) {
      String opt = (args == null || args.length < 1) ? args[0] : args[0];
      CephOperator cephOperate = new CephOperator(username, monIp, userKey, mountPath);
      if ("upload".equals(opt)) {
          cephOperate.uploadFileByPath(filePath, "/temp_upload_fs", args[1]);
      } else if ("download".equals(opt)) {
          cephOperate.downloadFileByPath(filePath, "/temp_download_fs", args[1]);
      } else {
          System.out.println("Unrecognized Command! Usage opt[upload|download] filename");
      }
  }
  ```

- **`CephOperator.java` 核心方法 `uploadFileByPath`**：
  ```java
  public void uploadFileByPath(String filePath, String fileName) {
      // 打开文件
      this.mount.stat(fileName, stat);
      long lastLen = stat.size;
      int fd = this.mount.open(fileName, CephMount.O_RDWR, mode: 0);

      // 读取文件内容
      byte[] bytes = new byte[1024];
      long uploadLength = 0;
      while ((length = fis.read(bytes, 0, bytes.length)) != -1) {
          // 写入 CephFS
          this.mount.write(fd, bytes, length, lastLen);
          // 更新上传进度
          uploadLength += length;
          // 输出传输速率
          float rate = (float) uploadLength * 100 / (float) fileLength;
          String rateValue = (int) rate + "%";
      }
  }
  ```

#### 命令行关键内容

- **Maven 打包命令**：
  ```bash
  mvn clean install
  ```

- **上传 JAR 文件**：
  ```bash
  rz
  ```

- **创建上传目录与文件**：
  ```bash
  mkdir -p /temp_upload_fs
  echo "abc123" > /temp_upload_fs/upload.txt
  ```

- **执行上传命令**：
  ```bash
  java -jar ceph-demo.jar upload upload.txt
  ```

- **执行下载命令**：
  ```bash
  java -jar ceph-demo.jar download upload.txt
  ```

- **验证文件内容**：
  ```bash
  cat /temp_download_fs/upload.txt
  ```

- **解决库依赖问题**：
  ```bash
  yum -y install libcephfs2 libcephfs_jni-devel
  ln -s /usr/lib/libcephfs_jni.so.2 /usr/lib64/libcephfs_jni.so.2
  ```

---

### 4) 关键场景与演示描述

- **场景 1: Maven 项目打包 (00:00 - 00:30)**
  - **描述**：讲师在 IntelliJ IDEA 中打开 `pom.xml` 文件，展示 Spring Boot 插件配置。随后在终端执行 `mvn clean install` 命令，成功生成 `ceph-demo.jar` 文件，并在文件列表中展示其文件信息。

- **场景 2: 上传文件至 CephFS (00:30 - 00:50)**
  - **描述**：讲师在 CentOS 7 服务器的终端中，使用 `rz` 命令将 JAR 文件上传至服务器。接着，创建上传目录 `/temp_upload_fs`，并创建一个名为 `upload.txt` 的测试文件，内容为 `abc123`。然后，执行 `java -jar ceph-demo.jar upload upload.txt` 命令，终端显示“文件传输成功！”。

- **场景 3: 下载文件从 CephFS (00:50 - 01:10)**
  - **描述**：讲师执行 `java -jar ceph-demo.jar download upload.txt` 命令，终端显示“Download Success!”。随后，使用 `cat` 命令查看下载目录 `/temp_download_fs` 中的文件内容，确认文件内容与上传时一致。

- **场景 4: 代码逻辑演示 (01:10 - 01:40)**
  - **描述**：讲师在 IntelliJ IDEA 中打开 `CephDemoApplication.java`，展示 `main` 方法如何解析命令行参数并调用 `CephOperator`。接着，打开 `CephOperator.java`，展示 `uploadFileByPath` 方法的核心逻辑，包括打开文件、读取数据、写入 CephFS 和计算传输速率。

- **场景 5: 常见问题处理 (01:40 - 02:00)**
  - **描述**：讲师在终端中演示如何解决 `libcephfs2` 库缺失问题，使用 `yum install` 命令安装库，并创建软链接。接着，演示如何解决 `rados` 版本不兼容
