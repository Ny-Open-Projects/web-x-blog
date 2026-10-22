# 10. `.env` 外置配置与通义千问集成

## 纲要

- **为什么要外置**：密钥/网关/模型写死在 `application.yml` 不便切换、易误提交；抽成隐藏 `.env` 资源文件是 Spring 官方推荐做法（契合 12-Factor）
- **`.env` 格式**：`KEY=VALUE` 全大写、无引号、无空格（`OPENAI_API_KEY` / `OPENAI_BASE_URL` / `OPENAI_MODEL`）
- **读取依赖**：`io.github.cdimascio:dotenv-java`（课程用的 dotenv 读取包）
- **启动加载**：`DotEnv.configure().ignoreIfMissing().load()` 后遍历 `entries()` 调 `System.setProperty(key,value)`，让 yml 的 `${OPENAI_API_KEY}` 生效
- **多模型变体**：复制 `deepseek.env` / `qwen.env`，切换模型时覆盖主 `.env` 即可
- **集成通义千问**：base-url 用 OpenAI SDK 地址，**必须去掉 `/v1`**（阿里会自动补全，加了反而 404）；模型用 `qwen-plus`，也能用阿里的 `deepseek-v3`
- **404 大坑**：调用报 404 多半是 base-url 多了 `/v1`，删掉即好

> 本章代码基于课程标准工程（`com.itzixi` 包）按 SpringAI 1.0 API 重构，外部代码卷暂未挂载，重挂后可切换为逐文件提取的真实代码。

## 一、配置外置的动机

第 5-A 章把 `api-key` / `base-url` / `model` 直接写在 `application.yml`。老师说：「这种方式目前都不是特别推荐，要修改不方便。」正确姿势是抽成独立的环境资源文件（隐藏的 `.env`），让工程读取——这也是 Dify 等智能体平台、各类部署工具的标准做法。

## 二、创建 `.env` 与格式规范

在 `src/main/resources` 下右键新建文件，命名为 `.env`（隐藏文件）：

```properties
OPENAI_API_KEY=sk-你的deepseek密钥
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-chat
```

**格式三要点**（老师逐条强调）：

1. **键全大写**：环境变量惯例大写，如 `OPENAI_API_KEY`（老师用 `Cmd+Shift+U` 转大写）。
2. **无引号**：值不要加双引号/单引号。
3. **无空格**：`KEY=VALUE` 等号两侧无空格。

`application.yml` 改用 Spring 表达式读取：

```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      base-url: ${OPENAI_BASE_URL}
      chat:
        options:
          model: ${OPENAI_MODEL}
```

> 这是「键-值对（map）」映射：`${OPENAI_API_KEY}` 读取环境变量，yml 不再硬编码明文密钥。

## 三、引入 dotenv-java 读取

```xml
<dependency>
  <groupId>io.github.cdimascio</groupId>
  <artifactId>dotenv-java</artifactId>
  <version>3.0.0</version>     <!-- 课程用此包读取 .env；以实际可用版本为准 -->
</dependency>
```

> 课程里老师直接给了一段依赖（拿源码复制即可）。核心是 **dotenv-java**——名字就是 `.env` 的意思。装好后在 Maven 仓库刷新加载。

## 四、启动类加载 `.env` 到系统变量

光写 `.env` + yml 表达式还不够——`.env` 是纯文本，需主动读取并注入系统环境，Spring 才能识别。在启动类（或配置类）里：

```java
// com.itzixi.Application（或专门 Config）
import io.github.cdimascio.dotenv.DotEnv;

public class Application {
    public static void main(String[] args) {
        // 1. 加载 .env（缺失不报错）
        DotEnv dotenv = DotEnv.configure().ignoreIfMissing().load();

        // 2. 把 .env 中的变量设置到系统环境变量中
        dotenv.entries().forEach(entry -> {
            System.setProperty(entry.getKey(), entry.getValue());
        });

        SpringApplication.run(Application.class, args);
    }
}
```

> `ignoreIfMissing()`：某些参数为空时忽略，不影响启动（严格规范场景可去掉强制校验）。`entries()` 遍历键值对，`System.setProperty(k,v)` 让 `${OPENAI_API_KEY}` 这类表达式能读到值。

> 老师说：「这是 Spring 官方推荐的方式，官方文档很多加载配置都通过 `.env` 读取。」

## 五、多模型 env 变体（一键切换）

模型切换频繁（DeepSeek ↔ 通义千问 ↔ 其他），建议复制多份：

```
resources/
├── .env            # 当前生效（开发期指向 deepseek）
├── deepseek.env    # DeepSeek 配置
└── qwen.env       # 通义千问配置
```

切换时把 `qwen.env` 内容覆盖进 `.env` 即可。老师：「后续要切换，只需把内容复制出来，非常方便。」

## 六、集成通义千问（Qwen）

通义千问同样兼容 OpenAI 协议，迁移成本极低。步骤：

1. 打开 `tongyi.aliyun.com` → 登录 → 控制台 → 模型服务（阿里文档较绕，要点「API」→ 账号设置 → 前往 API Key → 创建）。
2. 创建密钥（课程描述填 `springAI实战`）→ 复制。
3. 覆盖进 `.env` 的 `OPENAI_API_KEY`。
4. 模型名：课程用 `qwen-plus`（通义千问 Plus）；模型列表里还有 turbo / max / 多模态（文生图、语音）等可选。
5. base-url：看文档「首次调用通义千问 API」→ OpenAI SDK 地址（Python 示例里的那个 URL）。

```properties
# qwen.env
OPENAI_API_KEY=sk-你的通义千问密钥
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_MODEL=qwen-plus
```

> ⚠️ **404 大坑（重点）**：老师实测切换通义千问后首次调用报 **404**（地址/端口/方法名错）。根因：文档示例 URL 带 `/v1`，但阿里通义千问**要求把 `/v1` 去掉**——它会自动补全，加了反而 404。删掉 `/v1` 重启即正常。

**阿里版 deepseek 也可用**：通义千问模型列表里搜得到阿里的 DeepSeek（`deepseek-v3` 普通模型、`deepseek-r1` 推理模型）。注意阿里对 DeepSeek 的命名与 DeepSeek 官方不同（官方不叫 v3），切换时看清。

```properties
# 在通义千问平台用 deepseek-v3
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_MODEL=deepseek-v3
```

> 老师最后恢复成 DeepSeek（「我还是会使用 deepseek」）——两者都行，按你偏好。关键差异就是 base-url 去 `/v1` 这一处。

## 七、完整 application.yml（外置版）

```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      base-url: ${OPENAI_BASE_URL}
      chat:
        options:
          model: ${OPENAI_MODEL}
server:
  port: 8080
```

## 八、关联代码文件（本章重构）

| 文件 | 作用 |
|---|---|
| `mcp-client/src/main/resources/.env` | 隐藏环境变量（密钥/base-url/model） |
| `mcp-client/src/main/resources/deepseek.env` | DeepSeek 配置副本 |
| `mcp-client/src/main/resources/qwen.env` | 通义千问配置副本 |
| `mcp-client/pom.xml` | 加 `dotenv-java` 依赖 |
| `mcp-client/src/main/java/com/itzixi/Application.java` | 启动类加载 `.env` → `System.setProperty` |
| `mcp-client/src/main/resources/application.yml` | 改用 `${...}` 表达式 |

## 九、FAQ

**Q1：`.env` 和 `application.yml` 谁优先？**
`.env` 先被读入系统属性，yml 的 `${OPENAI_API_KEY}` 从系统属性取值；若系统已有同名变量（如 CI 注入），以系统为准。

**Q2：`.env` 要进 git 吗？**
**绝不**。`.gitignore` 加 `.env`，用 `.env.example` 留模板（空值）给同事。密钥进 git 等于公开。

**Q3：dotenv-java 的 groupId 是哪个？**
课程用的是 `io.github.cdimascio:dotenv-java`。若版本有变，以 Maven 中央库最新为准，API（`DotEnv.configure()...load()`）基本一致。

**Q4：通义千问 404 一定是 /v1 问题吗？**
最常见是 URL 多了 `/v1`；其次检查 key 是否覆盖进 `.env`、base-url 是否整段替换（别只改 model）。

**Q5：能不能不用 dotenv，直接用系统环境变量？**
可以——直接在 OS / CI 设 `OPENAI_API_KEY` 等，yml 同样能读。`.env` 只是本地开发便利。

**Q6：多环境（dev/test/prod）怎么管？**
除 `.env` 外，结合前述的 `application-{profile}.yml` 多环境切换；生产用 CI Secret / 配置中心注入，不依赖本地 `.env`。

**Q7：阿里的 deepseek-v3 和 DeepSeek 官方 deepseek-chat 一样吗？**
模型权重同源但入口不同：阿里通过通义千问平台代理，base-url 与命名（`deepseek-v3`）不同，需按平台文档填。

## 十、面试高频问答

**1. 为什么大模型密钥要外置，有哪些方案？**
硬编码易泄露、不便切换且违反 12-Factor。方案：`.env`（本地）+ 系统环境变量（CI）+ 配置中心/Secret（生产，如 Vault / K8s Secret）。

**2. Spring 的 `${}` 占位符如何解析来源？**
解析顺序：系统属性（`System.getProperty`）→ 环境变量 → `application.yml` / properties → 配置中心。`.env` 经 dotenv 注入系统属性后即被 `${}` 读到。

**3. 通义千问兼容 OpenAI 协议意味着什么？**
同一套 `spring-ai-starter-model-openai` 代码，只改 `base-url` 与 `model` 即可切换厂商，无需改业务代码——这是 OpenAI 协议标准化的红利。

**4. 切换模型报 404 如何快速定位？**
看 base-url 是否带多余路径段（`/v1`）；核对 key 是否覆盖；用 `curl` 直连 API 验证网关连通，再回查 yml 表达式是否取到值。

**5. `.env` 与多环境 profile 如何协同？**
`.env` 管密钥等敏感变量（不进 git），`application-{profile}.yml` 管非敏感环境差异（端口、数据源）；两者互补，生产以 Secret 注入覆盖。

**6. 如何防止密钥误提交？**
`.gitignore` 屏蔽 `.env`；CI 加 secret 扫描（如 gitleaks）；提供 `.env.example` 模板；code review 拦明文。

## 十一、各厂商 base-url / model 速查表

切换模型只改这两值，照表填即可：

| 厂商 | base-url（注意去 /v1） | 常用 model | 备注 |
|---|---|---|---|
| **DeepSeek** | `https://api.deepseek.com` | `deepseek-chat` / `deepseek-reasoner` | 官网 API 文档复制，无 `/v1` |
| **通义千问** | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` / `qwen-max` / `deepseek-v3` | **必须去掉尾部多余 `/v1`**，保留中间这一处 |
| **OpenAI** | `https://api.openai.com/v1` | `gpt-4o` / `gpt-4o-mini` | 原生带 `/v1` |
| **Ollama(本地)** | `http://localhost:11434` | `qwen2.5:7b` 等 | 本地免费，见第十三节 |
| **硅基流动/其他** | 各平台兼容地址 | 视平台 | 都兼容 OpenAI 协议 |

> 通义千问的 base-url 里**已含一个 `/v1`**（compatible-mode 路径），不要画蛇添足再追加；DeepSeek / OpenAI 因厂商而异，照官方文档。404 先查这里。

## 十二、本地模型 Ollama 集成（免密钥、零成本）

不想花钱可跑本地模型，Ollama 一键起，同样兼容 OpenAI 协议：

```bash
# 安装 Ollama 后拉模型
ollama pull qwen2.5:7b
ollama run qwen2.5:7b    # 本地对话验证
```

```properties
# local.env
OPENAI_API_KEY=ollama      # 本地可随便填，Ollama 不校验
OPENAI_BASE_URL=http://localhost:11434
OPENAI_MODEL=qwen2.5:7b
```

> 本地模型免费、数据不出内网，适合学习与隐私场景；缺点是 7B 级别能力弱于云端大模型，复杂推理吃力。内网互通在这里也适用（前端 host 写内网 IP）。

## 十三、配置加载校验与可观测

避免「配置没生效却不知道」：启动类打印已加载的关键变量（敏感 key 只打前几位）：

```java
log.info("模型={}, base-url={}, key={}***",
    System.getProperty("OPENAI_MODEL"),
    System.getProperty("OPENAI_BASE_URL"),
    mask(System.getProperty("OPENAI_API_KEY")));
```

- 用 Actuator `/env` 端点（生产关掉或鉴权）核对生效值。
- 单元测试：用 `@TestPropertySource` 注入假 key，验证 `System.setProperty` 路径通。

> 配置问题占联调故障大半，启动即打印可秒级定位「key 没覆盖 / url 多 v1」。

## 十四、密钥轮换与安全流程

密钥泄露（误提交/前员工）必须能快速轮换：

1. **平台侧吊销旧 key、生成新 key**（DeepSeek/通义千问控制台）。
2. **只改 `.env` / CI Secret**，不碰代码。
3. **滚动重启**服务加载新 key。
4. **审计**：查 git 历史是否泄露，必要时历史改写（BFG）+ 告警。

> `.env` 永不进 git + 用 `.env.example` 模板，是防误提交第一道防线；CI 加 secret 扫描（gitleaks）第二道。

## 十五、与配置中心（Nacos / Apollo）对比

| 方案 | 适用 | 优点 | 缺点 |
|---|---|---|---|
| `.env` 本地 | 开发、单机 | 简单、零依赖 | 不便团队统一、不进 git |
| 系统环境变量 | CI、容器 | 与平台集成好 | 散落、难管理 |
| **Nacos / Apollo** | 微服务生产 | 动态推送、灰度、加密 | 需额外组件 |
| **Vault / K8s Secret** | 云原生 | 加密强、审计全 | 运维成本 |

> 课程用 `.env` 教学；生产微服务直接上 Nacos/Apollo（配合前述 profile 切换），密钥走 Vault/Secret 不落盘。

## 十六、配置故障排查 SOP

模型调不通，自顶向下：

1. **启动日志**：key/model/base-url 是否打印正确？（十三届）
2. **curl 直连**：`curl -H "Authorization: Bearer $KEY" $BASEURL/models` 看 200/404。
3. **404**：base-url 多 `/v1` → 删掉（通义千问）。
4. **401**：key 错/没覆盖进 `.env` → 重填、确认 `System.setProperty` 路径。
5. **超时**：网络受限/代理 → 服务器部署或配代理。
6. **返回乱码**：Controller `setCharacterEncoding("UTF-8")` 漏了（前述上讲过）。

## 十七、.gitignore 与 .env.example 模板

防止密钥误提交的两道防线：

```gitignore
# 忽略真实配置
.env
*.env
# 保留模板
!.env.example
```

```properties
# .env.example（提交到 git，供团队复制改名）
OPENAI_API_KEY=请替换为你的密钥
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-chat
```

> IDEA 装 `.env` 插件可获得高亮与自动补全（老师没装也行，纯文本照样用）。新人 clone 后 `cp .env.example .env` 填 key 即可跑。

## 十八、配置演化路线总结

配置管理随项目成长演进：

```
硬编码 yml  ──→  ${} 表达式 + .env  ──→  多 env 变体 / profile  ──→  Nacos/Apollo + Vault
  (不便切换)      (本地安全, 教学用)        (多模型/多环境)          (生产动态+加密)
```

> 课程停在 `.env` + profile（前述）这一层，已足够学习；生产直接跳到最后一层。理解演进，才知道每一步解决什么问题。

## 十九、ops 提示（安全红线）

> **`.env` 永不进 git**：写进 `.gitignore`；提供 `.env.example`（空值模板）供团队复制。一旦密钥提交，立即吊销并轮换。
>
> **切换模型先验证连通**：换 `qwen.env` 后先 `curl` 直连 base-url 确认 200，再启动工程，避免反复重启排查。
>
> **base-url 去 `/v1`**：通义千问 / 部分兼容平台会自动补全 `/v1`，手写 URL 务必去掉，否则 404。
>
> **多份 env 管理**：`deepseek.env` / `qwen.env` 留底，主 `.env` 指向当前；CI 用变量注入，不依赖文件。
>
> **成本与限额**：通义千问按 token 计费、有免费额度；上线前设调用限额与缓存，防刷爆账单。

