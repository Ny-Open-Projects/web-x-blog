# 画面线理解：17_爬虫文章审核_修改文章&文本和图片解析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\17_爬虫文章审核_修改文章&文本和图片解析【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:16, 00:36, 00:51, 01:07, 01:32, 01:58, 02:21, 02:50, 03:03, 03:29, 03:42, 04:04, 04:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:26:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现对文章文本和图片的审核功能，通过调用阿里云的文本和图片审核 API，并更新数据库中的文章状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了项目结构，选中了 `AliyunTextScanRequest` 类，右侧编辑器显示了 `ReviewCrawlerArticleService.java` 中的文本审核逻辑，包括日志记录、文本内容解析和审核失败时的更新操作。
画面 2: 选中了 `AliyunImageScanRequest` 类，右侧编辑器显示了图片审核的逻辑，包括调用图片审核 API 和审核失败时的更新操作。
画面 3: 在 `handlerTextAndImages` 方法中，光标位于 `cNews.setStatus(0);` 语句，显示了修改文章状态的代码。
画面 4: 在 `handlerTextAndImages` 方法中，光标位于 `cNewsMapper.updateNews(cNews);` 语句，显示了更新数据库中文章信息的代码。
画面 5: 展示了 `handlerTextAndImages` 方法的完整结构，包括参数声明和方法体。
画面 6: 在 `handlerTextAndImages` 方法中，光标位于 `if(null != jsonArray)` 语句，准备开始遍历 JSON 数组。
画面 7: 在 `handlerTextAndImages` 方法中，光标位于 `for (Object obj : jsonArray)` 语句，开始遍历 JSON 数组。
画面 8: 在 `handlerTextAndImages` 方法中，光标位于 `String type = (String) jsonObject.get("type");` 语句，获取图片或文本的类型。
画面 9: 在 `handlerTextAndImages` 方法中，光标位于 `if("image".equals(type))` 语句，判断当前对象是否为图片。
画面 10: 在 `handlerTextAndImages` 方法中，光标位于 `String value = (String) jsonObject.get("value");` 语句，获取图片或文本的值。
画面 11: 在 `handlerTextAndImages` 方法中，光标位于 `images.add(value);` 语句，将图片 URL 添加到图片列表中。
画面 12: 在 `handlerTextAndImages` 方法中，光标位于 `sb.append(value);` 语句，将文本内容追加到 StringBuilder 中。
画面 13: 在 `handlerTextAndImages` 方法中，光标位于 `cNews.setStatus(9);` 语句，将文章状态更新为审核通过。
画面 14: 在 `handlerTextAndImages` 方法中，光标位于 `cNewsMapper.updateNews(cNews);` 语句，更新数据库中的文章信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
Log.info("开始文本内容的审核");
List<String> images = new ArrayList<>();
StringBuilder sb = new StringBuilder();
JSONArray jsonArray = JSON.parseArray(content);
handlerTextAndImages(images, sb, jsonArray);
```

画面 2:
```java
String imageResponse = aliyunImageScanRequest.imageScanRequest(images);
if(null == imageResponse || imageResponse.equals("pass")) {
    updateNews(cNews, message, "图片内容审核失败");
    return;
}
```

画面 3:
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    // 修改文章信息
    // 参数 cNews
    // 文章内容或标题为空
    cNews.setStatus(0);
}
```

画面 4:
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    // 修改文章信息
    // 参数 cNews
    // 文章内容或标题为空
    cNewsMapper.updateNews(cNews);
}
```

画面 5:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    // 修改文章信息
    // 参数 cNews
    // 文章内容或标题为空
    cNews.setStatus(0);
    cNewsMapper.updateNews(cNews);
}
```

画面 6:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 7:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 8:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 9:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 10:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 11:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 12:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 13:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 14:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value
