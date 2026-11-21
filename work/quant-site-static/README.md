# 网锋量化 QuantSite —— 生产部署（静态站，Phase 0）

量化投资子站：**数据看板（模拟数据） + 量化课程**。纯静态站点，零运行时依赖，可投放生产。

## 本地预览
```bash
cd work/quant-site
python3 -m http.server 8080   # 打开 http://localhost:8080
```

## 方式一：Nginx 静态部署（推荐）
把本目录整体放到服务器，Nginx 指向它：
```nginx
server {
  listen 80;
  server_name quant.webfault.com;        # 或主域 /quant 子路径
  root /var/www/quant-site;
  index index.html;
  location / { try_files $uri $uri/ /index.html; }
}
```

## 方式二：Docker（与 web-x-blog 部署一致）
```bash
cd work/quant-site
docker build -t quant-site:0.1.0 .
docker run -d --name quant-site -p 8093:80 quant-site:0.1.0
```

## 作为 web-x-blog 子站
- **子域**：`quant.webfault.com` → Nginx server_name 指向本站（推荐，看板/课程独立演进）。
- **子路径**：主站 Nginx 加 `location /quant/ { alias /var/www/quant-site/; }`。

## 目录
```
quant-site/
├─ index.html      # 数据看板（模拟数据）
├─ course.html     # 量化课程大纲
├─ assets/
│  ├─ styles.css   # 深色主题（涨红跌绿）
│  └─ app.js       # 模拟数据 + 渲染（换真实数据只改此处 MOCK_* ）
├─ Dockerfile
├─ nginx.conf
└─ README.md
```

## 数据接入（后续）
当前 `assets/app.js` 内 `MOCK_MARKET` / `MOCK_PORTFOLIO` 为模拟值。接入真实行情时，用 JQData / Tushare / akshare 拉取日线/分钟线 → 计算指标 → 五维综合，替换这两个对象即可，视图层不变。

## 合规
站点为量化方法学习/演示，**不构成投资建议、不自动下单、仅模拟盘**；部署时保留页脚合规披露。
