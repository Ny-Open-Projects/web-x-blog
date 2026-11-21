# 画面线理解：04.Graphql中的变量参数的服务端处理

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\04.Graphql中的变量参数的服务端处理【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:38, 04:38, 05:55, 07:03, 07:58, 09:39, 10:39, 11:52, 13:06, 14:51, 16:31, 18:14, 19:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:20:29

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中通过 GraphQL 实现服务端参数处理，包括 GET 和 POST 请求的变量解析与执行。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“2.3、服务端处理参数”章节，其中包含 GraphQL 变量示例 `{ "id": 8 }`。
画面2：展示 `GraphQLController.java` 文件中 `@GetMapping` 方法，接收 `query` 和 `variables` 参数，调用 `graphQL.execute`。
画面3：展示 `GraphQLController.java` 文件中 `@GetMapping` 方法，使用 `ExecutionInput` 构建并执行 GraphQL 查询。
画面4：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试将 `variablesJson` 反序列化为 `Map<String, Object>`。
画面5：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试将 `variablesJson` 反序列化为 `Map<String, Object>`，并构建 `ExecutionInput`。
画面6：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，使用 `JsonNode` 解析 JSON，提取 `query` 字段。
画面7：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，使用 `param.get` 获取 `query`、`variables`、`operationName`。
画面8：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，调用 `this.executeQuery` 方法。
画面9：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试调用 `this.executeQuery` 方法，但出现语法错误。
画面10：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，调试时查看变量值，`variablesJson` 为 `{"id":8}`。
画面11：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，调试时查看变量值，`variablesJson` 为 `{"id":8}`。
画面12：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试调用 `this.executeQuery` 方法，但出现语法错误。
画面13：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试调用 `this.executeQuery` 方法，但出现语法错误。
画面14：展示 PDF 文档中返回的 GraphQL 查询结果，包含 `HouseResources` 对象的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
{
  "id": 8
}
```

画面2：
```java
package cn.itcast.haoke.api.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import graphql.GraphQL;
import graphql.ExecutionInput;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GraphQLController {

    private GraphQL graphQL;

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @GetMapping
    public Map<String, Object> query(@RequestParam("query") String query,
                                     @RequestParam(value = "variables", required = false)String variables,
                                     @RequestParam(value = "operationName", required = false)String operationName) {
        return this.graphQL.execute(query).toSpecification();
    }

    @PostMapping
    @ResponseBody
    public Map<String, Object> postQuery(@RequestBody String json) {
        try {
            return this.graphQL.execute(json).toSpecification();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
```

画面3：
```java
@GetMapping
public Map<String, Object> query(@RequestParam("query") String query,
                                 @RequestParam(value = "variables", required = false)String variables,
                                 @RequestParam(value = "operationName", required = false)String operationName) {
    ExecutionInput executionInput = ExecutionInput.newExecutionInput()
            .query(query)
            .operationName(operationName)
            .variables(variables)
            .build();
    return this.graphQL.execute(executionInput).toSpecification();
}
```

画面4：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody String json) {
    try {
        Map<String, Object> variables = MAPPER.readValue(json, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        Input executionInput = ExecutionInput.newExecutionInput()
                .query(query)
                .operationName(operationName)
                .variables(variables)
                .build();
        return this.graphQL.execute(executionInput).toSpecification();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面5：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody String json) {
    try {
        Map<String, Object> variables = MAPPER.readValue(json, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        ExecutionInput executionInput = ExecutionInput.newExecutionInput()
                .query(query)
                .operationName(operationName)
                .variables(variables)
                .build();
        return this.graphQL.execute(executionInput).toSpecification();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面6：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody String json) {
    try {
        JsonNode jsonNode = MAPPER.readTree(json);
        if (jsonNode.has("query")) {
            String query = jsonNode.get("query").textValue();
            return this.graphQL.execute(query).toSpecification();
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面7：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        Map<String, Object> variables = MAPPER.readValue(variablesJson, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        JsonNode jsonNode = MAPPER.readTree(json);
        if (jsonNode.has("query")) {
            String query = jsonNode.get("query").textValue();
            return this.graphQL.execute(query).toSpecification();
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面8：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        Map<String, Object> variables = MAPPER.readValue(variablesJson, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        ExecutionInput executionInput = ExecutionInput.newExecutionInput()
                .query(query)
                .operationName(operationName)
                .variables(variables)
                .build();
        return this.graphQL.execute(executionInput).toSpecification();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面9：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variablesJson);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面10：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variablesJson);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面11：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variablesJson);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面12：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        Map variables = (Map) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variables);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面13：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try
