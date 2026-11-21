# 画面线理解：20_mycat路由开发_算法代码实现

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\20_mycat路由开发_算法代码实现【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:22, 01:57, 04:56, 06:43, 07:33, 08:14, 10:07, 11:07, 12:41, 13:32, 14:23, 15:36, 16:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:01:11

1) 这一组画面整体在讲如何实现一个自定义的分库分表规则算法（HeMaBurstRuleAlgorithm），并展示其在数据库表结构和配置文件中的应用。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 MySQL 数据库的表结构，包含多个以 "ap_" 和 "admin_" 开头的表，如 ap_article, ap_user, ap_user_identity 等，以及对应的触发器和存储过程。
画面2: 显示数据库中名为 "ap_behavior_entry" 的表结构，包含多个字段如 id, dataId, dataNode, type, createTime 等。
画面3: 显示一个 XML 配置文件，定义了多个表的分库分表规则，如 ap_article_content, ap_user, ap_user_identity 等，配置了 dataNode、autoincrement、primaryKey 和 rule。
画面4: 显示 IntelliJ IDEA 中的 Java 代码，定义了一个名为 HeMaBurstRuleAlgorithm 的类，它实现了 RuleAlgorithm 接口。
画面5: 显示一个 XML 配置文件，定义了多个分片规则，如 burst166, burst4040, burst5050, cron2slot, hash-int, rang-long 等，配置了 class、volume、step、mod 等属性。
画面6: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面7: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面8: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面9: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面10: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面11: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面12: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculateRange 方法，用于计算分片范围。
画面13: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculateRange 方法，用于计算分片范围。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面3:
<?xml version="1.0" encoding="UTF-8"?>
<rule>
    <table name="ADMIN_QRTZ_BLOB_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_CALENDARS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_CRON_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_FIRED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_LOCKS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_PAUSED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_SCHEDULER_STATE" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_SIMPLE_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_TRIGGERS" dataNode="DNSQ" type="global"/>
    <!-- --app_info-->
    <table name="ap_article" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_article_config" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_dynamic" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_identity" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_realname" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_follow" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_equipment" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_article_list" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>

画面5:
<?xml version="1.0" encoding="UTF-8"?>
<rule>
    <function name="burst166" class="com.heima.HeMaBurstRuleAlgorithm">
        <property name="volume">60000000</property><!-- 单组容量 -->
        <property name="step">66</property><!-- 单组节点数 -->
        <property name="mod">66</property><!-- 单组数据mod -->
    </function>
    <function name="burst4040" class="com.heima.HeMaBurstRuleAlgorithm">
        <property name="volume">40000000</property><!-- 单组容量 -->
        <property name="step">40</property><!-- 单组节点数 -->
        <property name="mod">40</property><!-- 单组数据mod -->
    </function>
    <function name="burst5050" class="com.heima.HeMaBurstRuleAlgorithm">
        <property name="volume">50000000</property><!-- 单组容量 -->
        <property name="step">50</property><!-- 单组节点数 -->
        <property name="mod">50</property><!-- 单组数据mod -->
    </function>
    <function name="cron2slot" class="io.mycat.route.function.PartitionByCRC32PreSlot">
        <property name="mount">2</property><!-- 一要分片的数据节点数量，必须指定，否则没法分片 -->
    </function>
    <function name="hash-int" class="io.mycat.route.function.PartitionByFileMap">
        <property name="mapFile">partition-hash-int.txt</property>
    </function>
    <function name="rang-long" class="io.mycat.route.function.PartitionByFileMap">
        <property name="mapFile">partition-hash-long.txt</property>
    </function>
</rule>

画面6:
public Integer calculate(String s) {
    return null;
}

@Override
public Integer[] calculateRange(String beginValue, String endValue) {
    return super.calculateRange(beginValue, endValue);
}

public void setVolume(Long volume) {
    this.volume = volume;
}

public void setStep(Integer step) {
    this.step = step;
}

public void setMod(Integer mod) {
    this.mod = mod;
}

画面7:
private Long volume;
private Integer step;
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    return null;
}

@Override
public Integer[] calculateRange(String beginValue, String endValue) {
    return super.calculateRange(beginValue, endValue);
}

画面8:
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    if (columnValue != null) {
        String[] temp = columnValue.split(regex);
        if (temp.length != 2) {
            long dataId = Long.valueOf(temp[0]);
            int pos = (int) (dataId / volume) * step + mod;
            return null;
        }
    }
    return null;
}

画面9:
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    if (columnValue != null) {
        String[] temp = columnValue.split(regex);
        if (temp.length != 2) {
            long dataId = Long.valueOf(temp[0]);
            long burstId = Long.valueOf(temp[1]);
            int group = (int) (dataId / volume) * step;
            int pos = group + (int) (burstId / mod);
            return null;
        }
    }
    return null;
}

画面10:
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    if (columnValue != null) {
        String[] temp = columnValue.split(regex);
        if (temp.length != 2) {
            long dataId = Long.valueOf(temp[0]);
            long burstId = Long.valueOf(temp[1]);
            int group = (int) (dataId / volume) * step;
            int pos = group + (int) (burstId / mod);
            System.out.println("HEIMA RULE INFO [" + columnValue + "]-[[" + pos + "]]");
            return pos;
        }
    }
