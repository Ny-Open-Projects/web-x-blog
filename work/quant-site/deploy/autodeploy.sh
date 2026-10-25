#!/bin/bash
# 无人值守：等 Docker daemon 恢复 → 构建 0.3.0 → 起容器接管 8098 → reload nginx → 自验
export PATH="/usr/local/bin:$PATH"
SITE=/Users/Wang/Code/github/web-x-blog/work/quant-site

echo "[$(date +%H:%M:%S)] 等待 Docker daemon 恢复（最长 50 分钟）..."
for i in $(seq 1 100); do
  if curl -s --max-time 2 --unix-socket /var/run/docker.sock http://localhost/version >/dev/null 2>&1; then
    echo "[$(date +%H:%M:%S)] daemon 就绪（第 $i 次检查）"; break
  fi
  sleep 30
done

if ! curl -s --max-time 3 --unix-socket /var/run/docker.sock http://localhost/version >/dev/null 2>&1; then
  echo "[$(date +%H:%M:%S)] daemon 仍未就绪，放弃本轮（需人工启动 Docker Desktop）"; exit 1
fi

echo "[$(date +%H:%M:%S)] 停止本地临时实例（释放 8098）"
lsof -ti:8098 | xargs kill 2>/dev/null
sleep 2

echo "[$(date +%H:%M:%S)] 构建 quant-site:0.3.0 ..."
cd "$SITE" && docker build -t quant-site:0.3.0 . 2>&1 | tail -3

echo "[$(date +%H:%M:%S)] 起容器（webfault-net / 8098）"
docker rm -f quant-site >/dev/null 2>&1
docker run -d --name quant-site --network webfault-net --restart unless-stopped -p 8098:3000 quant-site:0.3.0

echo "[$(date +%H:%M:%S)] nginx reload"
docker exec webfault-nginx nginx -s reload

sleep 8
echo "[$(date +%H:%M:%S)] 自验："
for u in "/" "/course" "/course/data-10" "/sim" "/sitemap.xml"; do
  curl -s -o /dev/null -w "  容器直连 %{http_code} $u\n" "http://127.0.0.1:8098$u"
done
curl -s -o /dev/null -w "  vhost http80 %{http_code}\n" -H "Host: quant.webfault.com" http://127.0.0.1/
curl -sk -o /dev/null -w "  vhost https443 %{http_code}\n" -H "Host: quant.webfault.com" https://127.0.0.1/
curl -s -m 20 "http://127.0.0.1:8098/api/board" | grep -oE '"volRatio":[0-9.]+|"power":"[^"]*"' | head -4
echo "[$(date +%H:%M:%S)] 完成"
