# 703 Go HTTP 表单处理 · 深挖

## 思路与架构
Go 处理表单是「路由 → 方法分支 → 解析 → 取值」四步。net/http 用默认多路复用器（或显式 ServeMux）把路径绑到 Handler；Handler 按 r.Method 分流。取值体系分两套接口：字段式 `r.Form`/`r.PostForm`（惰性 map，需先解析）与方法式 `r.FormValue`/`r.PostFormValue`（按 key 直接取）。解析是惰性的——只有调用 Value 方法（内部 ParseMultipartForm）才填充 map。Form 数据源含 POST 体 + URL 参数，PostForm 仅 POST 体。

## 方案取舍
- **默认复用器 vs 显式 ServeMux**：`nil` 用全局 DefaultServeMux 简单但易污染；显式 `http.NewServeMux()` 隔离更安全，推荐生产用。
- **map vs Value 方法**：map 适合批量遍历且需先 ParseForm；Value 方法简洁、按需解析、返回首值，日常首选。
- **FormValue vs PostFormValue**：需连同 URL 参数用 FormValue；只处理表单体用 PostFormValue，避免误拿 query。
- **text/template vs html/template**：渲染用户输入必用 html/template 自动转义防 XSS。

## 答题技巧
答表单题按「起服务（ListenAndServe）→ 路由（HandleFunc）→ 方法分支（r.Method）→ 渲染/取值」串。高频追问：① Form 为何有时 nil（惰性，需先 Parse）；② FormValue 与 PostFormValue 区别（范围：是否含 URL 参数；都仅 POST/PUT/PATCH）；③ 模板路径相对执行目录。收尾点出：显式 ServeMux + html/template + 按需 Value 方法是工程稳妥组合。
