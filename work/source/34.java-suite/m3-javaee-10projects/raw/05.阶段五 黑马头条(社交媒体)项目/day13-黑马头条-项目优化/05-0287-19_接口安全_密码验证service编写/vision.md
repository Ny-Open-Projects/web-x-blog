# 画面线理解：19_接口安全_密码验证service编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\19_接口安全_密码验证service编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:28, 00:45, 01:06, 03:04, 03:54, 04:28, 04:44, 05:09, 05:23, 05:43, 06:02, 06:20, 06:31, 06:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:58:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在登录服务中实现基于DES算法的密码校验功能，包括接口定义、实现类编写及工具类调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Mapper接口定义，包含注释“通过手机号查询用户”，并列出方法签名 `ApUser selectByAppPhone(String phone);`，以及对应的XML映射文件 `ApUserMapper.xml` 内容：
```xml
<select id="selectByAppPhone" resultMap="BaseResultMap">
    <include refid="Base_Column_List" />
    from ap_user where phone = #{phone} limit 1;
</select>
```

画面2：展示项目结构，选中模块 `service-mycat`，并显示其内部的 `pom.xml` 文件。

画面3：展示 `ValidateService.java` 接口文件，定义了 `validateDES` 方法的签名。

画面4：在 `ValidateService.java` 中，为 `validateDES` 方法添加了 `@Override` 注解。

画面5：在 `ValidateService.java` 中，为 `validateDES` 方法添加了 `@Service` 注解。

画面6：在 `ValidateService.java` 中，导入了 `com.heima.login.service.ValidateService`、`com.heima.model.user.pojos.ApUser` 和 `com.heima.utils.common.DESUtil`。

画面7：展示 `ValidateServiceImpl.java` 文件，定义了 `validateDES` 方法的实现。

画面8：在 `ValidateServiceImpl.java` 中，为 `validateDES` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面9：在 `ValidateServiceImpl.java` 中，编写了 `validateDES` 方法的校验逻辑，使用 `DESUtil.encode` 对用户密码进行加密并比较。

画面10：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解。

画面11：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面12：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面13：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面14：在 `ValidateServiceImpl.java` 中，编写了 `validateWithSalt` 方法的完整校验逻辑，使用 `DESUtil.encodeWithSalt` 对用户密码进行加密并比较。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第2点中各画面的要点描述。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
