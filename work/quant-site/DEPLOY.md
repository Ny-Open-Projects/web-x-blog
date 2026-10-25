# 量化子站部署上线（quant.webfault.com）

> 2026-10-25 已上线：本机 webfault Docker 栈内运行，nginx 通配符证书（*.webfault.com）覆盖，HTTP/HTTPS 双通。
> 端口 8098 主机映射 + `webfault-net` 容器网络，nginx upstream 走容器名 `quant-site:3000`。

## 一、构建并运行容器

```bash
cd work/quant-site
docker build -t quant-site:0.2.0 .
docker run -d --name quant-site --network webfault-net --restart unless-stopped \
  -p 8098:3000 quant-site:0.2.0
# 验证：curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8098/   # 200
```

注意：
- 原计划端口 8093 已被 `webfault-search-web` 占用，实际用 **8098**；
- 容器必须加入 `webfault-net`，否则 nginx upstream `quant-site:3000` 无法解析；
- 镜像需含 `public/` 目录（缺失会导致 runner 阶段 `COPY /app/public` 失败）。

## 二、Nginx 子域反代（已完成）

1. upstream 已加入 `/Users/Wang/Code/webfault/infrastructure/docker/nginx/nginx.conf`（`quant_web_upstream` → `quant-site:3000 resolve`）。
2. vhost 已落在 `conf.d/quant.webfault.com.conf`，`include` 共享 `_ssl.conf`（通配符自签证书，自动覆盖 443）。
3. 使生效：
   ```bash
   docker exec webfault-nginx nginx -t
   docker exec webfault-nginx nginx -s reload
   ```
4. DNS：真实环境在域名服务商加 `quant.webfault.com A <服务器IP>`（与主站同 IP，nginx 按 server_name 分流）。本机验证在 `/etc/hosts` 加 `127.0.0.1 quant.webfault.com`。

## 三、HTTPS

无需额外操作：`_ssl.conf` 已为所有 vhost 挂上 `webfault.com.fullchain.pem`（自签通配符）。
生产环境换正式证书后全站统一生效。

## 四、与主站共存

- 本机 webfault 全栈（30+ 容器）共用 `webfault-nginx`，各子域独立 conf 分流，互不干扰。
- blog :8092、quant :8098，端口均为主机映射，容器间走网络别名。

## 五、运维

- 更新：`docker build -t quant-site:<新tag> .` → `docker stop/rm quant-site` → 新 tag `docker run`（参数同上）。
- 日志：`docker logs -f quant-site`。
- 数据源为腾讯公开接口，无需 API Key；接口限流时看板自动降级为模拟数据并在页首标注。
- 课程内容在 `content/{basics,quant,data}/*.md`，改完 `docker build` 即可（SSG 预渲染）。

## 合规

站点为量化方法学习/演示，不构成投资建议、不自动下单、仅模拟盘；页脚已带风险披露。
