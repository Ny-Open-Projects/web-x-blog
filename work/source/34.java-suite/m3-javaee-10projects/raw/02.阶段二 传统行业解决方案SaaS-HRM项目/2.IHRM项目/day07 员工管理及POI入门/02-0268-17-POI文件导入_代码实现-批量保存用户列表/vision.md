# 画面线理解：17-POI文件导入：代码实现-批量保存用户列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\17-POI文件导入：代码实现-批量保存用户列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:07, 01:37, 02:25, 03:06, 03:25, 03:59, 04:17, 04:50, 05:42, 06:21, 06:59, 07:55, 08:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:57:54

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码读取 Excel 文件中的用户数据，并批量保存到数据库，涉及用户服务层、数据转换和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 UserController.java 中，展示从 Excel 读取数据后调用 userService.saveAll() 方法批量保存用户。
画面 2: 在 UserController.java 中，展示 saveAll 方法的实现，其中包含对用户对象的属性设置，并调用 userService.saveAll。
画面 3: 在 UserService.java 中，展示 save 方法的实现，其中设置用户 ID、密码、部门等属性。
画面 4: 在 UserService.java 中，展示 findUserByMobile 方法的实现，用于根据手机号查找用户。
画面 5: 在 UserService.java 中，展示 setMobile 方法的实现，用于设置用户手机号。
画面 6: 在 UserService.java 中，展示 setDepartmentId 方法的实现，用于设置用户部门 ID。
画面 7: 在 UserService.java 中，展示 setEnableState 方法的实现，用于设置用户状态。
画面 8: 在 UserController.java 中，展示 getCellValue 方法的实现，用于获取单元格的值。
画面 9: 展示 Excel 文件“导入测试模板.xlsx”，其中包含用户数据，如用户名、手机号、工号、聘用形式、入职时间、部门编码。
画面 10: 在 SQLyog 中，展示查询用户表（b_user）的 SQL 语句，用于验证数据。
画面 11: 展示 Excel 文件“导入测试模板.xlsx”，其中部门编码列被选中。
画面 12: 在 User.java 中，展示构造函数的实现，用于从数组中解析用户属性。
画面 13: 在 User.java 中，展示构造函数的实现，其中使用 DecimalFormat 格式化工号。
画面 14: 在 SQLyog 中，展示查询用户表（b_user）的 SQL 语句，用于验证数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
return new Result(ResultCode.SUCCESS);
```
画面 2:
```java
for(int cellNum=1; cellNum <= row.getLastCellNum(); cellNum++) {
    (cell cell = row.getCell(cellNum);
    Object value = getCellValue(cell);
    values[cellNum] = value;
}
User user = new User(values);
list.add(user);
//3.批量保存用户
userService.saveAll(list,companyId,companyName);
return new Result(ResultCode.SUCCESS);
```
画面 3:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 4:
```java
//根据mobile查找用户
public User findByMobile(String mobile) { return userDao.findByMobile(mobile); }
//批量保存用户
public void saveAll(List<User> list, String companyId, String companyName) {
    for (User user : list) {
        user.setPassword(new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString());
        user.setId(IdWorker.nextId()+"");
        user.setCompanyId(companyId);
        user.setCompanyName(companyName);
        user.setServiceStatus(1);
        user.setEnableState(1);
        user.setLevel("user");
    }
}
```
画面 5:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 6:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 7:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 8:
```java
public static Object getCellValue(Cell cell) {
    //获取单元格属性类型
    CellType cellType = cell.getCellType();
    Object value = null;
    switch (cellType) {
        case STRING:
            value = cell.getStringCellValue();
            break;
        case BOOLEAN:
            value = cell.getBooleanCellValue();
            break;
        case NUMERIC:
            value = cell.getNumericCellValue();
            break;
        case FORMULA:
            value = cell.getCellFormula();
            break;
        case BLANK:
            value = "";
            break;
        case ERROR:
            value = cell.getErrorCellValue();
            break;
    }
    return value;
}
```
画面 9:
（无代码）
画面 10:
```sql
SELECT * FROM em_company_personnel a, b_user b WHERE a.user_id = b.user_id AND a.resignation_time BETWEEN '2018-01-01' AND '2018-12-31'
```
画面 11:
（无代码）
画面 12:
```java
public User(Object[] values) {
    //用户名
    this.username = values[1].toString();
    //手机号
    this.mobile = values[2].toString();
    //工号
    this.workNumber = values[3].toString();
    //聘用形式
    this.formOfEmployment = (Double) values[4].intValue();
    //入职时间
    this.timeOfEntry = (Date) values[5];
    //部门编码
    this.departmentId = values[6].toString();
}
```
画面 13:
```java
public User(Object[] values) {
    //用户名
    this.username = values[1].toString();
    //手机号
    this.mobile = values[2].toString();
    //工号
    this.workNumber = new DecimalFormat(pattern: "0000000000").format(values[3]).toString();
    //聘用形式
    this.formOfEmployment = (Double) values[4].intValue();
    //入职时间
    this.timeOfEntry = (Date) values[5];
    //部门编码
    this.departmentId = values[6].toString();
}
```
画面 14:
```sql
SELECT * FROM em_company_personnel a, b_user b WHERE a.user_id = b.user_id AND a.resignation_time BETWEEN '2018-01-01' AND '2018-12-31'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无 PPT、架构图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
