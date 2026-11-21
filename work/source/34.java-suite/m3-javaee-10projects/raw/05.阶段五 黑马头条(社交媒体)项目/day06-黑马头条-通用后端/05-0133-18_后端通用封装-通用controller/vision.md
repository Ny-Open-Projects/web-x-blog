# 画面线理解：18_后端通用封装-通用controller

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\18_后端通用封装-通用controller【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:21, 00:48, 01:05, 01:31, 01:39, 02:00, 02:14, 02:40, 02:51, 03:03, 03:42, 03:52, 04:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:11:08

1) 这一组画面整体在讲什么（一句话）：
编写一个通用的 Spring Boot 控制器类 CommonController，用于处理通用的增删改查接口，并展示其开发过程和运行时日志。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程目录结构，当前位于“4.8 CommonController”章节，内容是创建 com.heima.admin.controller.v1.CommonController 类，实现 Service 的调用。
画面 2: IDE 中显示了项目结构，选中了 CommonController.java 文件，准备编写代码。
画面 3: 在代码编辑器中，开始编写类的包声明和导入语句，光标位于 package 声明后。
画面 4: 编写了类的注解和基础结构，包括 @RestController、@RequestMapping("/api/v1/admin/common") 和类声明。
画面 5: 定义了私有成员变量 commonService，并开始编写 list 方法。
画面 6: 为 list 方法添加了 @PostMapping("/list") 注解，并开始编写方法体。
画面 7: 在 list 方法中，光标位于 return 语句前，准备调用 commonService.list(dto)。
画面 8: 在 update 方法中，光标位于 return 语句前，准备调用 commonService.update(dto)。
画面 9: 在 delete 方法中，光标位于 return 语句前，准备调用 commonService.delete(dto)。
画面 10: 在 delete 方法中，光标位于 return 语句前，准备调用 commonService.delete(dto)。
画面 11: 在 delete 方法中，光标位于 return 语句前，准备调用 commonService.delete(dto)。
画面 12: 在项目结构中，选中了 AdminApplication 类，准备运行项目。
画面 13: 在控制台中，显示了项目启动日志，包括 HikariPool-1 的连接信息和 Hibernate 版本信息。
画面 14: 在控制台中，显示了项目启动日志，包括 HikariPool-1 的连接信息和 Hibernate 版本信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
4.8 CommonController
创建com.heima.admin.controller.v1.CommonController类，实现Service的调用。
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController{
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
    @PostMapping("/update")
    public ResponseResult update(@RequestBody CommonDto dto) {
        return commonService.update(dto);
    }
    @PostMapping("/delete")
    public ResponseResult delete(@RequestBody CommonDto dto) {
        return commonService.delete(dto);
    }
}
```

画面 2:
```
package com.heima.admin.controller.v1;
public class CommonController {
```

画面 3:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
```

画面 4:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
```

画面 5:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
```

画面 6:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
```

画面 7:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
    @PostMapping("/update")
    public ResponseResult update(@RequestBody CommonDto dto) {
        return commonService.update(dto);
    }
```

画面 8:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
    @PostMapping("/update")
    public ResponseResult update(@RequestBody CommonDto dto) {
        return commonService.update(dto);
    }
    @PostMapping("/delete")
    public ResponseResult delete(@RequestBody CommonDto dto) {
        return commonService.delete(dto);
    }
```

画面 9:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
    @PostMapping("/update")
    public ResponseResult update(@RequestBody CommonDto dto) {
        return commonService.update(dto);
    }
    @PostMapping("/delete")
    public ResponseResult delete(@RequestBody CommonDto dto) {
        return commonService.delete(dto);
    }
```

画面 10:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
    @PostMapping("/update")
    public ResponseResult update(@RequestBody CommonDto dto) {
        return commonService.update(dto);
    }
    @PostMapping("/delete")
    public ResponseResult delete(@RequestBody CommonDto dto) {
        return commonService.delete(dto);
    }
```

画面 11:
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v1/admin/common")
public class CommonController {
    @Autowired
    private CommonService commonService;
    @PostMapping("/list")
    public ResponseResult list(@RequestBody CommonDto dto) {
        return commonService.list(dto);
    }
    @PostMapping("/update")
    public ResponseResult update(@RequestBody CommonDto dto) {
        return commonService.update(dto);
    }
    @PostMapping("/delete")
    public ResponseResult delete(@RequestBody CommonDto dto) {
        return commonService.delete(dto);
    }
```

画面 12:
```
package com.heima.admin.controller.v1;
public class CommonController {
```

画面 13:
```
2019-06-27 14:48:14,150 [DEBUG] HikariPool-1 housekeeper [com.zaxxer.hikari.pool.HikariPool] - logState: HikariPool-1 - Before cleanup stats (total=0, active=0, idle=0, waiting=0)
2019-06-27 14:48:14,163 [DEBUG] HikariPool-1 connection adder [com.zaxxer.hikari.pool.HikariPool] - logState: HikariPool-1 - Added connection com.mysql.jdbc.JDBC4Connection@1d76283
2019-06-27 14:48:14,169 [DEBUG] HikariPool-1 connection adder [com.zaxxer.hikari.pool.HikariPool] - logState: HikariPool-1 - Added connection com.mysql.jdbc.JDBC4Connection@1d76283
2019-06-27 14:48:14,172 [DEBUG] HikariPool-1 connection adder [com.zaxxer.hikari.pool.HikariPool] - logState: HikariPool-1 - Added connection com.mysql.jdbc.JDBC4Connection@1d76283
2019-06-27 14:48:14,173 [DEBUG] HikariPool-1 connection adder [com.zaxxer.hikari.pool.HikariPool] - logState: HikariPool-1 - Added connection com.mysql.jdbc.JDBC4Connection@1d76283
2019-06-27 14:48:14,174 [DEBUG] HikariPool-1 connection adder [com.zaxxer.hikari.pool.HikariPool] - logState: HikariPool-1 - Added connection com.mysql.jdbc.JDBC4Connection@1d76283
2019-06-27 14:48:14,175 [DEBUG] HikariPool-1 connection adder [com.zaxxer.hikari.pool.HikariPool] - logState
