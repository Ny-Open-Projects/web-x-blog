# 画面线理解：day10-12-投标预览-接口1-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-12-投标预览-接口1-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:46, 01:51, 04:23, 07:13, 09:12, 10:10, 11:05, 11:27, 11:43, 12:10, 14:18, 14:56, 15:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:24:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在万向金融P2P交易系统中，通过Java代码查询项目信息、计算剩余金额并封装返回DTO，涉及数据库表结构、SQL查询及MyBatis映射。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法用于查询项目ID列表。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面2：
- 显示数据库管理工具（SQLyog）中p2p_transaction_0数据库的表结构。
- 列出数据库中的6张表：claim_0, claim_1, project_0, project_1, tender_0, tender_1。

画面3：
- 显示PPT页面，标题为“用户投标业务流程图”。
- 图中包含多个模块：浏览器/App、交易中心、用户服务、存管代理服务、存管系统。
- 从“浏览器/App”指向“交易中心”，再指向“用户服务”，最后指向“存管系统”。
- 从“用户服务”指向“存管代理服务”，再指向“存管系统”。
- 图中包含多个步骤，如“1.1 获取标的的信号”、“1.2 项目标的的信号”、“1.3 项目标的的信号”、“2.5 预处理添加投标成功”、“10. 更新交易记录，状态为：已同步”。

画面4：
- 显示数据库管理工具中“tender”表的结构。
- 表结构包含字段：ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL。
- 表中数据为空。

画面5：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面6：
- 显示数据库管理工具中“tender”表的查询结果。
- 查询条件为：WHERE PROJECT_ID = 1 AND STATUS = 1。
- 查询结果为空。

画面7：
- 显示数据库管理工具中“tender”表的查询结果。
- 查询条件为：WHERE PROJECT_ID = 1 AND STATUS = 1。
- 查询结果为空。

画面8：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面9：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面10：
- 显示IDE中ProjectServiceImp.java文件，其中createProject方法的代码。
- 代码中使用RestResponse获取用户信息，设置项目状态为COLLECTING，设置项目状态为STATUS_OUT，设置项目创建时间。
- 代码注释说明：1. 获取用户信息；2. 设置项目状态；3. 设置项目状态；4. 设置项目创建时间。

画面11：
- 显示PPT页面，标题为“黑马程序员”。
- 页面内容包括：获取标的的ID，在线查询已投资金额，计算剩余金额。
- 代码中使用BigDecimal进行金额计算，通过tenderMapper.selectAmountInvestedByProjectId查询已投资金额。
- 代码注释说明：1. 根据标的的ID在线查询已投资金额；2. 计算剩余金额。

画面12：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面13：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

画面14：
- 显示IDE中ProjectServiceImp.java文件，其中queryProjectsIds方法的代码。
- 代码中使用QueryWrapper进行SQL条件构建，通过split解析ids字符串，然后调用lambda表达式进行in查询。
- 代码注释说明：1. 查询项目的ID；2. 获取项目信息；3. 转换为DTO对象；4. 查询出借人数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 1.查询项目的ID
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    List<Long> list = new ArrayList<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        list.add(Long.parseLong(str));
    });
    queryWrapper.lambda().in(Project::getId, list);  // ... where id in (1,2,3,4,5)
    List<Project> projects = list(queryWrapper);
    List<ProjectDTO> dtos = new ArrayList<>();
    // 2.转换为DTO对象
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3.获取剩余额度
        // 4.查询出借人数
    }
    return dtos;
}
```

画面4：
```sql
SELECT ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL
FROM tender
WHERE PROJECT_ID = 1 AND STATUS = 1;
```

画面5：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 1.查询项目的ID
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    List<Long> list = new ArrayList<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        list.add(Long.parseLong(str));
    });
    queryWrapper.lambda().in(Project::getId, list);  // ... where id in (1,2,3,4,5)
    List<Project> projects = list(queryWrapper);
    List<ProjectDTO> dtos = new ArrayList<>();
    // 2.转换为DTO对象
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3.获取剩余额度
        // 4.查询出借人数
    }
    return dtos;
}
```

画面6：
```sql
SELECT ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL
FROM tender
WHERE PROJECT_ID = 1 AND STATUS = 1;
```

画面7：
```sql
SELECT ID, CONTAINER_ID, CONSUMER_ID, CONSUMER_USERNAME, PROJECT_ID, NAME, DESCRIPTION, TYPE, PERIOD, AMOUNT, RATE, BORROWER, AUDIT_RATE, COMMISSION, APPROVAL
FROM tender
WHERE PROJECT_ID = 1 AND STATUS = 1;
```

画面8：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String ids) {
    // 1.查询项目的ID
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    List<Long> list = new ArrayList<>();
    Arrays.asList(ids.split(",")).forEach(str -> {
        list.add(Long.parseLong(str));
    });
    queryWrapper.lambda().in(Project::getId, list);  // ... where id in (1,2,3,4,5)
    List<Project> projects = list(queryWrapper);
    List<ProjectDTO> dtos = new ArrayList<>();
    // 2.转换为DTO对象
    for (Project project : projects) {
        ProjectDTO projectDTO = convertProjectEntityToDTO(project);
        // 3.获取剩余额度
        // 4.查询出借人数
    }
    return dtos;
}
```

画面9：
```java
@Override
public List<ProjectDTO> queryProjectsIds(String
