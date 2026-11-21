# 24-热点商品抢单-抢单测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,我们开始测试一下这个脚本

那么测试之前呢

我们先简单检查一遍

从这里我们来简单说一下

第一个这个是获取请求头

开始识别用户的身份

如果用户是已登录

那这里返回200

那这个正确的

紧接着我们会获取用户名

这应该是Locker

对吧

获取用户名之后

开始去看一下

当前用户是否已经购买过该商品

这个呢应该是用User Key

就是这一块

往后面走

如果说没有买过该商品

我们就直接去抢单了

如果说买了

我们就进入到热点商品抢单

如果说该商品存在库存

也就是它代理人有库存

那么就进入到热点商品抢单排队

排队呢

你当前如果没有排队

那自身一之后返回的值是一

应该是横等一

那么就开始进行排队

如果你之前已经排队了

我就直接响应信息

给你就可以了

好

这是这一块

还有可能库存不足

刚才说了

如果这里小于得于0

库存不足

那就走这一个

对吧

没有登录就返回这个信息给你

好OK

我们来测试一次

看看效果

先把这里已经有的订单

全部给干掉

我们重新启动一下

我们当前的Nginx

加载一下配置文件吧

Reload

好

开始测试一下这个商品

这个商品呢

我们看一下是192测试一次

下单成功

对吧

我们看有没有

有了

我们再来测试一次

大家看

你已经下单过了

请商货再来

24小时再来

我们刷新一下

看这里数据

就多了一个数据记录

拿着这个

好

刚才这个是非热点商品抢单

我们在整个热点商品抢单

看这个怎么样

这个好

好

有个S

把它给整到这里来

开始执行一次抢单

大家看一下效果

热点商品抢单一次

正在排队

对吧

这是这一块正在排队

OK

那你再怎么整

它还是在排队

好

这个是我们这个热点商品和非热点商品抢单的一个测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个高并发场景下，如何通过 Nginx + Redis + Kafka 的组合架构来实现商品限购和排队功能。核心逻辑是：用户请求购买商品时，首先验证用户身份（JWT），然后检查该用户在24小时内是否已购买过该商品（Redis）。如果未购买，系统会根据商品的热度进行分流处理：对于非热门商品，直接下单；对于热门商品，用户需进入排队队列（通过 Redis 的 `hincrby` 原子操作记录排队状态），并将排队信息通过 Kafka 发送到消息队列，由下游服务处理。整个流程旨在解决高并发下的库存超卖和排队管理问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示 Nginx 配置文件 `auth_verify.lua` 的代码，介绍这是用于处理用户身份验证和商品限购逻辑的 Lua 脚本。
*   **00:05 - 00:15**: 详细讲解代码逻辑。首先获取请求头中的 JWT Token，调用 `jwt_token.check` 进行验证。如果验证通过，提取用户 ID 和商品 ID。
*   **00:15 - 00:25**: 逻辑分支一：检查用户在24小时内是否购买过该商品。通过 Redis 的 `hget` 命令查询 `hasbuy` 哈希表。如果未购买（`hasbuy` 不存在或为 `nil`），进入下一步。
*   **00:25 - 00:35**: 逻辑分支二：检查商品库存。通过 Redis 的 `hget` 命令查询 `num` 字段。如果库存为 `nil` 或 `null`，表示商品已售罄，直接返回错误码 `405`。
*   **00:35 - 00:45**: 逻辑分支三：处理热门商品的排队逻辑。如果商品库存充足，系统会检查用户是否已在排队（`hincrby` 原子操作）。如果用户未在排队，系统会创建一个排队对象，包含用户名和商品 ID，并通过 Kafka 发送消息。
*   **00:45 - 00:55**: 逻辑分支四：处理非热门商品的直接下单逻辑。如果商品非热门，系统会直接调用 `/api/order/` 接口进行下单。
*   **00:55 - 01:05**: 展示 Postman 测试结果。演示了用户在24小时内重复购买同一商品时，系统返回 `415` 错误码，提示“您已经在24小时内购买该商品，请稍后再来”。
*   **01:05 - 01:15**: 展示 Postman 测试结果。演示了商品库存不足时，系统返回 `405` 错误码，提示“库存不足”。
*   **01:15 - 01:25**: 展示 Postman 测试结果。演示了用户成功排队后，系统返回 `200` 状态码和成功消息。
*   **01:25 - 01:35**: 展示 Redis Desktop Manager，演示了 `hasbuy` 和 `num` 字段在 Redis 中的存储状态，验证了逻辑的正确性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 (Nginx Lua 脚本)**:
    ```lua
    local auth_header = ngx.var.http_Authorization
    local result = jwt_token.check(auth_header)
    if result.code == 200 then
        local headers = ngx.req.get_uri_args()
        local id = headers["id"]
        local username = result["body"]["payload"]["username"]
        local userKey = "USER_"..username.."_id"
        local key = "SKU_"..id
        local hasbuy = redis.get(userKey)
        local response = {}
        if hasbuy == nil or hasbuy[1] == nil or hasbuy[1] == ngx.null then
            local num = redis.hget(key, "num")
            if num == nil or num == ngx.null then
                response["code"] = 405
                response["message"] = "库存不足"
                ngx.say(cjson.encode(response))
                return
            else
                num = tonumber(num)
                if num > 0 then
                    local inc = redis.hincrby(key, userKey, 1)
                    if inc == 1 then
                        local userorder = {}
                        userorder["username"] = username
                        userorder["id"] = id
                        kafka.send("neworder", cjson.encode(userorder))
                        response["code"] = 200
                        response["message"] = "您正在排队抢购中"
                        ngx.say(cjson.encode(response))
                        return
                    else
                        response["code"] = 405
                        response["message"] = "库存不足"
                        ngx.say(cjson.encode(response))
                        return
                    end
                else
                    response["code"] = 415
                    response["message"] = "您已经在24小时内购买该商品，请稍后再来"
                    ngx.say(cjson.encode(response))
                    return
                end
            end
        else
            response["code"] = 415
            response["message"] = "您已经在24小时内购买该商品，请稍后再来"
            ngx.say(cjson.encode(response))
            return
        end
    end
    ```

*   **图表/界面**:
    *   **Redis Desktop Manager**: 用于查看 Redis 数据库中的 `hasbuy` 和 `num` 字段，验证数据一致性。
    *   **Postman**: 用于模拟 HTTP 请求，测试不同场景下的 API 响应。
    *   **数据库管理界面**: 展示了 `order_general_order` 表，用于查看订单数据。

---

### 4) 关键场景与演示描述

*   **场景一：用户身份验证与商品限购检查**
    *   **演示**: 视频展示了 Nginx Lua 脚本如何解析 JWT Token，提取用户信息，并通过 Redis 检查用户是否在24小时内购买过该商品。
    *   **关键点**: 通过 `redis.get` 和 `redis.hget` 命令查询 Redis 数据库，确保用户限购逻辑的准确性。

*   **场景二：商品库存检查与排队逻辑**
    *   **演示**: 视频展示了如何通过 Redis 的 `hget` 命令查询商品库存，并根据库存情况决定是直接下单还是进入排队。
    *   **关键点**: 使用 `hincrby` 原子操作来记录用户排队状态，确保并发场景下的数据一致性。

*   **场景三：Kafka 消息队列**
    *   **演示**: 视频展示了当用户成功排队后，系统如何通过 Kafka 发送消息，将排队信息发送给下游服务。
    *   **关键点**: Kafka 用于解耦排队服务和下单服务，提高系统的可扩展性和稳定性。

*   **场景四：Postman 测试**
    *   **演示**: 视频通过 Postman 发送 HTTP 请求，测试了不同场景下的 API 响应。
    *   **关键点**: 测试了用户重复购买、库存不足和成功排队等场景，验证了系统的功能正确性。

*   **场景五：Redis 数据验证**
    *   **演示**: 视频通过 Redis Desktop Manager 查看 Redis 数据库中的 `hasbuy` 和 `num` 字段，验证了数据的一致性。
    *   **关键点**: 通过直接查看 Redis 数据，确认了 Lua 脚本的逻辑正确性。

---

以上是根据视频画面进行的结构化技术分析，希望能帮助您更好地理解该技术课程的内容。
