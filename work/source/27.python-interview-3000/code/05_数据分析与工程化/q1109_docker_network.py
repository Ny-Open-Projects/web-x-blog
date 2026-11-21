import shutil
import subprocess

def sh(cmd):
    print("$", cmd)
    if shutil.which("docker"):
        try:
            out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            print((out.stdout or out.stderr).strip()[:400])
        except Exception as e:
            print("docker 调用失败:", e)
    else:
        print("本机未安装 docker,仅演示命令")

if __name__ == "__main__":
    sh("docker network create app-net")
    sh("docker run -d --name web --network app-net -p 8080:80 nginx")
    sh("docker network inspect app-net")
    print("""
模式对比:
  bridge 默认 经 docker0 与 NAT 外部访问需 -p 端口映射
  host    共享宿主机网络栈 无 NAT 隔离弱
  none    仅 loopback 适合离线任务
  自定义网络内置 DNS 服务名互访
""")
