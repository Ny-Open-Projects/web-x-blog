# 18_后端通用封装-通用controller

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\18_后端通用封装-通用controller【海量资源尽在 666java.com】.mp4
- 时长 4分8秒（音频 249s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去说一下当前那个通用的Controller的编写啊那这个呢其实也比较简单了啊那咱们就在这直接去写了啊呃打开当前的admin端然后在这去创建一个Controller在这去创建一个类这个类呢叫common Controller然后呢写上之后呢咱们在这啊去加上一些东西叫request mapping rest Controller啊好是request mapping
[00:31] 好的这个路径咱们还是按照之前的路径一样写API是吧然后是v1然后是admin然后下面是common好吧行下面咱们就可以去注入当前咱们写通用的serviceprivatecommon Service好common Service注入一下注入进来之后咱们在这就可以去写方法了首先咱们是要去写三个方法就可以
[01:01] 好吧三个三个方法啊第一个呢是public response result现在是listlist里边咱们可以去设置很多是吧你是哪种方式比如说你要是统计啊还是说按条件查询呢还是没条件啊咱们都可以在这去设置需要看你的参数是啥request body这里边有个common dtodto好完事啊那这在这你就可以直接干嘛呢直接去订当前的common
[01:31] Service.list把DTO装进去在上面咱们也可以去带一个Boss mapping这里边咱们可以设置一个叫list好吧叫list行那这个就算是完了然后下面还有还有两个方法是吧咱们再进一下public什么 response result是叫update然后这里边还是commentDTO
[02:01] 然我在前面你还要再去加什么东西一个requestreqrequest body然后调用Service直接加就可以了直接调用就可以了return common Service.update当然这个update咱们也知道这边它其实具有两种功能是吧一个啥呢一个是新增二个是修改是吧也是根据你反正过来到一个model来去区分也是新增和修改
[02:32] 这个怎么叫update好吧主要是根据当前的参数区分可以是新增或修改还有最后一个是吧叫public response result然后是delete然后这里边其实就跟应该是最简单的一个request body然后还是当前什么common-dtl好dtl最终的你在这去丢就可以了return什么return当前的common-Service.delete
[03:03] DTO好吧在这啊加上PostPostMapping这是叫Delete诶?
[03:12] 找个坏了Delete这个的话咱们就算是做完了啊做完之后呢咱们一会儿啊就可以去基层前端来去测一下刚才我说的那三个功能是吧比如说分别是什么用户列表什么敏感词还有什么频道
[03:32] 咱们这时候看看好用还是不好用是吧那这时候咱们可以去重启一下启动一下当前的项目看看有没有问题好吧直接右键debug收到好正在启动看看有没有报错没有报错就没有问题好这个好像是没有问题他没有报错那这时候咱们通用的comment通用的这种后端的这种接口咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
编写一个通用的 Spring Boot 控制器类 CommonController，用于处理通用的增删改查接口，并展示其开发过程和运行时日志。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程目录结构，当前位于“4.8 CommonController”章节，内容是创建 com.heima.admin.Controller.v1.CommonController 类，实现 Service 的调用。
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
创建com.heima.admin.Controller.v1.CommonController类，实现Service的调用。
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
package com.heima.admin.Controller.v1;
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
package com.heima.admin.Controller.v1;
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

