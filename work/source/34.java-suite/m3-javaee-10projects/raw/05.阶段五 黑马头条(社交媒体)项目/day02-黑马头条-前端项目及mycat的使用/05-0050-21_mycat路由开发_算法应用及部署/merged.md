# 21_mycat路由开发_算法应用及部署

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\21_mycat路由开发_算法应用及部署【海量资源尽在 666java.com】.mp4
- 时长 5分14秒（音频 315s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢咱们是把当前这个算法给做出来了给写完了那写完之后呢这个到底该怎么去用呢用法是这样啊咱们首先呢是需要把当前这个工程啊给打一个包打一个包怎么打包啊还有印象吗是不是在这去选择一个package啊直接打包啊打包的时候他会去打到当前一个target的目录下边啊点一下包错了是吧我看看啊
[00:31] 这里边咱们有一个git的一个配置其实个差距的话咱们现在暂时用不着咱们这里边并没有去用做版本控制所以说咱们找到当前的复工程里边有一个plugin里边是有一个git的配置你把git这一块先给它注掉我看看到这从这把这东西都注掉注掉完之后你再来去试一下看看打包有没有不行点稍等好这样的话打包就结束了
[01:07] 这样的话他就是打包到了这个位置这个位置啊那你说那这东西该怎么去用呢现在我已经打完包了啊在他给的里边已经有了就这东西有他这是个jar 包这里边是不是封装了咱们自己的算法呀我看那这个你只需要把它呢拷贝到哪呢拷贝到当前的啊一个叫做什么当前买太太里边啊有一个配置有个内部啊内部里边的都是些jar 包你把它呢给考到这
[01:33] 好这儿你要是里边我里边已经考过来你可以看一下啊就是当前的Service-mycat就它你把它考过来之后呢这时候你再重启一下但是重启之前呢还需要有一些配置哪些配置呢好来看一下啊咱们还是打开当前的这三个配置文件啊应该是两个啊一个是 ruler ruler里边是不是咱们去说了一些这种什么分片的算法呀你看这块就是你可以在上面去定义
[02:01] 他的名称比如说上这块Burst 5050是吧还有Burst 4040还有一个是Burst 66这些呢都是自己定义的啊当然这个配置文件已经有了啊他引用的是谁呢引用的是当前的这个名称那这名称的话他对应的他就有一个Faction那Faction其实对应的就是你算法的类那就是这三个这三个啊这三个你看当前这个包
[02:28] 当前这个包是不是就咱们自己写的当前那个包下边是当前这个算法的类啊OK啊那这个类呢有了之后呢你可以去传三个参数你看每一个都要去传三个参数啊因为呢咱们当前算法里边可以看一下啊是不是就要求有这三个参数啊是不是这三个参数啊OK啊你看这块啊一定要写上并且这个名称呢你也不能随便写必须跟你的当前这个属性名称要对应上这样的话
[02:57] 他才能去注入进去好吧行啊那这个加进来之后呢那最终的是得让你的分片的表表去用所以说你还要再去打开谁呀打开SkymerSkymer里边呢你可以看找一找啊咱们目前其实也已经配置完了就是在下面找table里边找啊往上往上Burst这么可以去搜一下啊找不到的话就搜一下搜一下吧Burst 4040搜
[03:32] 好找到了啊我先就这块你看他这块呢就是用的当前的自己写的这个算法我看啊那这个名称不一下啊这个名称要跟你的谁啊要跟你的 ruler 里边当前定义的这块名称要对应上必须一致要不然的话他可能找不到你当前写的算法OK那这还有一个啊那这是4040他应该还有其他的啊怎么可以再再去搜一下然后是5050
[04:03] 搜一下看有没有不是5050也有啊是吧这边呢他是这几个表用的是当前的当前的Boss5050也是自己写的这个算法那这个算法呢就是为了能够更方便的进行扩容好吧行那这个弄完之后啊这个还有一个东西一定要去知道啊目前的话呢咱们这个表啊你看这里边并没有设置主件的自增
[04:30] 没有说主件自增也就是说呢在当前的servantsdbconfig里边呢你不应该配置当前的自增因为它这个主件生成的时候呢咱们是需要去手动维护的那怎么手动维护呢其实呢咱们到后边到后边啊到明天啊到明天会去专门去讲这个组keeper去生成一个分布式的主件的时候咱们还会再去把这一块内容再去讲了好吧
[04:56] 那行那这个看咱们继续看到当前的这个讲义里边啊首先的是当前这两个怎么配置刚才其实已经讲完了啊下面还有一个就是算法的测试那关于测试呢咱们一会儿再测好吧咱们先说到这啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置并执行 Maven 插件，编译打包 Java 项目，并展示相关的数据库分库分表规则配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中打开项目 `Service-mycat`，查看 `HeMaBurstRuleAlgorithm.java` 文件中的 `calculateRange` 方法，该方法用于计算分片范围。
画面 2: 在 IDEA 的终端中执行 Maven 命令 `mvn git-commit-id-plugin:revision`，但因未指定有效的 `.git` 目录而报错。
画面 3: 在 `pom.xml` 文件中查看 `maven-git-commit-id-plugin` 插件的配置，包含 `configuration` 节点下的 `dotGitDirectory`、`dateFormat`、`useNativeGit`、`abbrevLength` 和 `generateGitPropertiesFile` 等属性。
画面 4: 在 IDEA 中右键点击 `pom.xml` 文件，选择 `Maven` -> `Reimport`，触发 Maven 重新导入项目。
画面 5: Maven 构建成功，输出 `BUILD SUCCESS`，并生成了 `Service-mycat-1.0-SNAPSHOT.jar` 文件。
画面 6: 在 Notepad++ 中打开 `schema.xml` 文件，查看 `table` 节点定义，包括 `ap_user`、`ap_user_equipment`、`ap_user_search` 等表的 `dataNode`、`autoIncrement`、`primaryKey` 和 `rule` 属性。
画面 7: 在 Notepad++ 中打开 `rule.xml` 文件，查看 `tableRule` 节点定义，包括 `jch`、`burst5050`、`burst4040` 和 `burst66` 等规则的 `column` 和 `algorithm` 属性。
画面 8: 在 IDEA 中查看 `pom.xml` 文件，其中 `maven-git-commit-id-plugin` 插件的 `configuration` 节点被高亮显示。
画面 9: 在 IDEA 中查看 `HeMaBurstRuleAlgorithm.java` 文件，该类继承自 `AbstractPartitionAlgorithm` 并实现 `RuleAlgorithm` 接口，用于实现分片算法。
画面 10: 在 Notepad++ 中打开 `schema.xml` 文件，查看 `ad` 前缀的表定义，包括 `ad_user`、`ad_channel`、`ad_strategy_group` 等表的 `dataNode`、`autoIncrement`、`primaryKey` 和 `rule` 属性。
画面 11: 在 Notepad++ 中打开 `schema.xml` 文件，查看 `ap` 前缀的表定义，包括 `ap_user`、`ap_user_equipment`、`ap_user_search` 等表的 `dataNode`、`autoIncrement`、`primaryKey` 和 `rule` 属性。
画面 12: 在 Notepad++ 中打开 `rule.xml` 文件，查看 `tableRule` 节点定义，包括 `jch`、`burst5050`、`burst4040` 和 `burst66` 等规则的 `column` 和 `algorithm` 属性。
画面 13: 在 Notepad++ 中打开 `sequence_db_conf.properties` 文件，查看 `AP_ARTICLE_DNSQ`、`AP_USER_DNSQ` 等序列配置。
画面 14: 在 Typora 中打开 `day02.md` 文件，查看 `4.7 算法测试` 和 `4.7.1 工具测试` 小节，其中包含 `explain select id from ap_collection where burst in ('1-5','10-9')` 的 SQL 示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public Integer[] calculateRange(String beginValue, String endValue) {
    if(beginValue==null && endValue==null) {
        Integer begin = calculate(beginValue);
        Integer end = calculate(endValue);
        if(begin==null && end==null) {
            return new Integer[0];
        }
        if(end < begin) {
            int len = end - begin + 1;
            Integer[] re = new Integer[len];
            for(int i = 0; i < len; i++) {
                re[i] = begin + i;
            }
            return re;
        }
    }
}
```

画面 2:
```bash
mvn git-commit-id-plugin:revision
```

画面 3:
```xml
<configuration>
    <dotGitDirectory>../../.git</dotGitDirectory>
    <dateFormat>yyyy-MM-dd HH:mm:ss</dateFormat>
    <useNativeGit>true</useNativeGit>
    <abbrevLength>8</abbrevLength>
    <generateGitPropertiesFile>true</generateGitPropertiesFile>
</configuration>
```

画面 4:
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.0</version>
    <configuration>
        <sourceEncoding>${project.build.sourceEncoding}</sourceEncoding>
        <targetJdk>${java.version}</targetJdk>
        <printFailingErrors>true</printFailingErrors>
        <rulesets>
            <ruleset>rulesets/java/all-concurrent.xml</ruleset>
            <ruleset>rulesets/java/all-constant.xml</ruleset>
        </rulesets>
    </configuration>
</plugin>
```

画面 5:
```bash
BUILD SUCCESS
```

画面 6:
```xml
<table name="ap_user" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_realname" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_info" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_equipment" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_channel" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_dynamic_list" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_letter" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_search" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ap_user_feedback" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
```

画面 7:
```xml
<tableRule name="jch">
    <column>id</column>
    <algorithm>jump-consistent-hash</algorithm>
</tableRule>

<tableRule name="burst5050">
    <column>burst</column>
    <algorithm>burst5050</algorithm>
</tableRule>

<tableRule name="burst4040">
    <column>burst</column>
    <algorithm>burst4040</algorithm>
</tableRule>

<tableRule name="burst66">
    <column>burst</column>
    <algorithm>burst66</algorithm>
</tableRule>
```

画面 8:
```xml
<configuration>
    <dotGitDirectory>../../.git</dotGitDirectory>
    <dateFormat>yyyy-MM-dd HH:mm:ss</dateFormat>
    <useNativeGit>true</useNativeGit>
    <abbrevLength>8</abbrevLength>
    <generateGitPropertiesFile>true</generateGitPropertiesFile>
</configuration>
```

画面 9:
```java
package com.heima;

import io.mycat.config.model.ruleAlgorithm;
import io.mycat.route.function.AbstractPartitionAlgorithm;
import io.mycat.route.function.RuleAlgorithm;

public class HeMaBurstRuleAlgorithm extends AbstractPartitionAlgorithm implements RuleAlgorithm {
    private Long volume;
    private Integer step;
    private Integer mod;

    @Override
    public Integer calculate(String columnValue) {
        if(columnValue==null) {
            return null;
        }
        // 分片ID = (dataID/volume) * step + dataID%mod
        // ...
    }
}
```

画面 10:
```xml
<table name="ad_user" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ad_user_equipment" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ad_user_search" dataNode="DNAP $0-39" autoIncrement="true" primaryKey="id" rule="mod-long40">
<table name="ad_user_feedback" dataNode="DNAP $0-39" auto

