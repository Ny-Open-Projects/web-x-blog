# 画面线理解：6.13 实时数据查询 - 开发controller程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.13 实时数据查询 - 开发controller程序_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:07, 02:07, 02:49, 03:16, 05:25, 06:14, 07:15, 07:51, 08:52, 09:46, 10:24, 11:18, 11:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:37:38

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现仓库监控的分页查询功能，包括控制器层和业务层的代码编写。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中，右键点击 `com.ithema.cold.monitor.controller` 包，选择“New” -> “Java Class”，准备创建新的控制器类。
画面2：在 `MessageController.java` 文件中，输入 `@RestController` 注解，IDE 提示需要导入 `org.springframework.web.bind.annotation.RestController`。
画面3：在 `MessageController.java` 中，添加了 `@RequestMapping("/device/monitor")` 和 `@Autowired` 注解，并声明了 `private MessageService messageService;`。
画面4：在 `MessageController.java` 中，添加了 `@RequestMapping("/deviceList")` 方法，用于分页查询设备列表。
画面5：在 `MessageController.java` 中，为 `@RequestMapping("/deviceList")` 方法添加了 `@RequestParam Map<String, Object> params` 参数。
画面6：在 `MessageController.java` 中，为 `@RequestMapping("/deviceList")` 方法添加了 `@RequestBody` 注解，并开始编写业务逻辑。
画面7：在 `MessageController.java` 中，为 `@RequestMapping("/deviceList")` 方法编写了完整的分页查询逻辑，使用 `messageService.queryMessageRealTime(params).getRecords()` 获取数据。
画面8：切换到浏览器，显示了仓库监控的前端页面，展示了多个仓库的实时温度、湿度等数据。
画面9：在 `MessageController.java` 中，添加了 `@RequestMapping("/realtime")` 方法，用于查询实时监控数据。
画面10：在 `MessageController.java` 中，为 `@RequestMapping("/realtime")` 方法添加了 `@RequestBody` 注解，并开始编写业务逻辑。
画面11：在 `MessageController.java` 中，为 `@RequestMapping("/realtime")` 方法编写了完整的查询逻辑，使用 `messageService.queryMessageRealTime(params).getRecords()` 获取数据。
画面12：在 `MessageController.java` 中，为 `@RequestMapping("/realtime")` 方法添加了 `Page<MessageEntity> list = messageService.queryMessageRealTime(params);` 并使用 `list.getPages()` 获取分页信息。
画面13：切换到 `MessageServiceImpl.java` 文件，查看 `queryMessageRealTime` 方法的实现，该方法使用 `QueryWrapper` 进行条件查询。
画面14：在 `MessageController.java` 中，为 `@RequestMapping("/realtime")` 方法编写了完整的分页查询逻辑，使用 `messageService.queryMessageRealTime(params).getRecords()` 获取数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
无

画面2：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import org.springframework.web.bind.annotation.RestController;
```

画面3：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
}
```

画面4：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
    }
}
```

画面5：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
    }
}
```

画面6：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
}
```

画面7：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
}
```

画面8：
无

画面9：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
    @RequestMapping("/realtime")
    public R realtime(@RequestParam Map<String, Object> params) {
    }
}
```

画面10：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
    @RequestMapping("/realtime")
    public R realtime(@RequestParam Map<String, Object> params) {
    }
}
```

画面11：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
    @RequestMapping("/realtime")
    public R realtime(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
}
```

画面12：
```java
package com.ithema.com.ithema.cold.monitor.controller;
import com.ithema.cold.monitor.service.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/device/monitor")
public class MessageController {
    @Autowired
    private MessageService messageService;
    @RequestMapping("/deviceList")
    public R deviceList(@RequestParam Map<String, Object> params) {
        List<MessageEntity> list = messageService.queryMessageRealTime(params).getRecords();
        Map<String, Object> map = new HashMap<>();
        map.put("items", list);
        return R.ok(map);
    }
    @RequestMapping("/realtime")
    public R realtime(@RequestParam Map<String, Object> params) {
        Page<MessageEntity> list = messageService.queryMessageRealTime(params);
        Map<String, Object> map = new HashMap<>();
        map.put("total", list.getTotal());
        map.put("pages", list.getPages());
        map.put("items", list.getRecords());
        return
