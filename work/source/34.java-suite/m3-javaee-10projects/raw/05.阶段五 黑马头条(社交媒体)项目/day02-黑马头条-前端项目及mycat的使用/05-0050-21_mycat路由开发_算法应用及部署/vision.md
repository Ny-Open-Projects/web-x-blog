# 画面线理解：21_mycat路由开发_算法应用及部署

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\21_mycat路由开发_算法应用及部署【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:33, 00:48, 00:59, 01:16, 01:49, 02:10, 02:43, 02:54, 03:15, 03:22, 03:45, 04:34, 05:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:02:09

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置并执行 Maven 插件，编译打包 Java 项目，并展示相关的数据库分库分表规则配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中打开项目 `service-mycat`，查看 `HeMaBurstRuleAlgorithm.java` 文件中的 `calculateRange` 方法，该方法用于计算分片范围。
画面 2: 在 IDEA 的终端中执行 Maven 命令 `mvn git-commit-id-plugin:revision`，但因未指定有效的 `.git` 目录而报错。
画面 3: 在 `pom.xml` 文件中查看 `maven-git-commit-id-plugin` 插件的配置，包含 `configuration` 节点下的 `dotGitDirectory`、`dateFormat`、`useNativeGit`、`abbrevLength` 和 `generateGitPropertiesFile` 等属性。
画面 4: 在 IDEA 中右键点击 `pom.xml` 文件，选择 `Maven` -> `Reimport`，触发 Maven 重新导入项目。
画面 5: Maven 构建成功，输出 `BUILD SUCCESS`，并生成了 `service-mycat-1.0-SNAPSHOT.jar` 文件。
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
