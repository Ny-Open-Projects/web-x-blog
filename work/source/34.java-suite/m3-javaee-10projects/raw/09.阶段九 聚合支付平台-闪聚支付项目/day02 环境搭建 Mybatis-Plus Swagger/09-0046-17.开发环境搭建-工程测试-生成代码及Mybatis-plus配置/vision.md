# 画面线理解：17.开发环境搭建-工程测试-生成代码及Mybatis-plus配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\17.开发环境搭建-工程测试-生成代码及Mybatis-plus配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:27, 02:05, 03:03, 04:00, 04:54, 05:59, 07:08, 08:10, 09:23, 11:04, 12:16, 13:17, 14:11, 15:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:45:27

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 代码生成器自动生成商户服务的实体、Mapper 等文件，并配置 Nacos 作为配置中心管理 Spring Boot 项目配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程大纲，当前章节为“1.7 工程测试”，子章节“1.7.1 生成代码”，并显示了修改数据源配置的代码片段。
画面 2：展示文件资源管理器，路径为“.../output/dao02/资料/工程测试/generator”，目录下有“src”、“target”和“generator.ini”文件。
画面 3：在课程大纲中，显示了“3) 运行生成类，输入模块名：merchant”的提示，并在代码编辑器中高亮了“merchant”。
画面 4：在 IntelliJ IDEA 中，显示了 MyBatis-Plus 代码生成器的 Java 类 `MyBatisPlusGenerator.java`，其中包含 `initMap()` 方法和 `outputFile()` 方法的代码。
画面 5：在 IntelliJ IDEA 中，显示了 `App.java` 文件，其中定义了 `@TableField` 注解的 `appId` 和 `appname` 字段。
画面 6：在 IntelliJ IDEA 中，显示了 `StaffMapper.java` 文件，其中定义了 `StaffMapper` 接口，继承自 `BaseMapper<Staff>`。
画面 7：在课程大纲中，显示了“1.7.2.1 配置连接池Druid”的子章节，并高亮了 Druid 数据源配置的代码片段。
画面 8：在 Nacos 配置管理页面，显示了“删除配置成功”的提示，配置 ID 为 `merchant-service`，分组为 `SHANJUPAY_GROUP`。
画面 9：在 IntelliJ IDEA 中，显示了 `bootstrap.yml` 文件，其中配置了 Dubbo 的 `scan`、`protocol`、`name`、`port` 和 `registry` 等属性。
画面 10：在 Nacos 配置管理页面，显示了“新建配置”的表单，Data ID 为 `spring-boot-mybatis-plus.yaml`，Group 为 `COMMON_GROUP`。
画面 11：在 IntelliJ IDEA 中，显示了 `bootstrap.yml` 文件，其中配置了多个 `data-id` 和 `group`，用于加载不同的配置文件。
画面 12：在 Nacos 配置管理页面，显示了配置列表，包括 `spring-boot-http.yaml`、`merchant-application.yaml`、`spring-boot-starter-druid.yaml`、`merchant-service.yaml` 和 `spring-boot-mybatis-plus.yaml`。
画面 13：在 IntelliJ IDEA 中，显示了 MyBatis-Plus 代码生成器的 Java 类 `MyBatisPlusGenerator.java`，其中包含 `outputFile()` 方法的代码。
画面 14：在 IntelliJ IDEA 中，显示了 `AppMapper.java` 文件，其中定义了 `AppMapper` 接口，继承自 `BaseMapper<App>`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
// 商户服务
dataSourceConfig
    .setUrl("jdbc:mysql://127.0.0.1:3306/shanjupay_merchant_service?"
            + "serverTimezone=Asia/Shanghai");
```
画面 3：
```java
// 生成包配置
PackageConfig packageConfig = new PackageConfig();
packageConfig.setParent("com.shanjupay");
```
画面 4：
```java
@Override
public void initMap() {
    // to do nothing
}

// 如果模板引擎是 freemarker
String templatePath = "/templates/mapper.xml.ftl";

// 自定义输出配置
List<FileOutConfig> focList = new ArrayList<>();
// 自定义配置会被优先输出
focList.add(new FileOutConfig(templatePath) {
    @Override
    public String outputFile(TableInfo tableInfo) {
        return "/mapper" + tableInfo.getEntityName() + "Mapper.java";
    }
});
```
画面 5：
```java
public class App implements Serializable {
    private static final long serialVersionUID = 1L;
    @TableField(value = "ID", type = IdType.ID_WORKER)
    private Long id;
    @TableField("APP_ID")
    private String appId;
    // 商户名称
    @TableField("APP_NAME")
    private String appname;
}
```
画面 6：
```java
public interface StaffMapper extends BaseMapper<Staff> {
}
```
画面 7：
```yaml
type: com.alibaba.druid.pool.DruidDataSource
driver-class-name: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/oauth?useUnicode=true
username: root
password: yourpassword
druid:
  initial-size: 5
  min-idle: 5
  max-active: 20
  max-wait: 60000
  time-between-eviction-runs-millis: 60000
  min-evictable-idle-time-millis: 300000
  validation-query: SELECT 1 FROM DUAL
  test-while-idle: true
  test-on-borrow: true
  test-on-return: false
  pool-prepared-statements: true
  max-pool-prepared-statement-per-connection-size: 20
  filter:
    stat:
      slow-sql-millis: 1
      log-slow-sql: true
    filters: config,stat,wall,log4j2
    web-stat-filter:
      enabled: true
```
画面 9：
```yaml
file-extension: yaml
namespace: f5ec3c1-4f05-40cd-964a-8444742ab4
group: SHANJUPAY_GROUP # spring boot 业务分组
ext-config:
  refresh: true
  data-id: spring-boot-http.yaml # spring boot http配置
  group: SHANJUPAY_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-starter-druid.yaml # spring boot starter druid配置
  group: COMMON_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-mybatis-plus.yaml # spring boot mybatis-plus配置
  group: COMMON_GROUP # 通用配置组
dubbo:
  scan: # dubbo 服务扫描包
    base-packages: com.shanjupay
  protocol:
    name: dubbo
    port: 20880
  registry:
    address: nacos://127.0.0.1:8848
```
画面 11：
```yaml
file-extension: yaml
namespace: f5ec3c1-4f05-40cd-964a-8444742ab4
group: SHANJUPAY_GROUP # spring boot 业务分组
ext-config:
  refresh: true
  data-id: spring-boot-http.yaml # spring boot http配置
  group: SHANJUPAY_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-starter-druid.yaml # spring boot starter druid配置
  group: COMMON_GROUP # 通用配置组
  refresh: true
  data-id: spring-boot-mybatis-plus.yaml # spring boot mybatis-plus配置
  group: COMMON_GROUP # 通用配置组
dubbo:
  scan: # dubbo 服务扫描包
    base-packages: com.shanjupay
  protocol:
    name: dubbo
    port: 20880
  registry:
    address: nacos://127.0.0.1:8848
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：PPT 标题为“1.7 工程测试”，子标题“1.7.1 生成代码”，内容为“通过一个案例‘根据id查询商户’的开发去熟悉项目架构的基本开发方法”。
画面 8：Nacos 配置管理页面，显示“删除配置成功”，配置 ID 为 `merchant-service`，分组为 `SHANJUPAY_GROUP`。
画面 12：Nacos 配置管理页面，显示配置列表，包括 `spring-boot-http.yaml`、`merchant-application.yaml`、`spring-boot-starter-druid.yaml`、`merchant-service.yaml` 和 `spring-boot-mybatis-plus.yaml`。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
