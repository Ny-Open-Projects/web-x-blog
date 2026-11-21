import asyncio
import sys


async def run_quick() -> None:
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-c", "print(sum(range(1000)))",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate()
    print("正常命令 stdout:", out.decode().strip(), "returncode:", proc.returncode)


async def run_with_timeout() -> None:
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-c", "import time; print('start', flush=True); time.sleep(30)",
        stdout=asyncio.subprocess.PIPE,
    )
    try:
        await asyncio.wait_for(proc.communicate(), timeout=0.5)
    except asyncio.TimeoutError:
        proc.kill()          # SIGKILL
        await proc.wait()    # 收尸避免僵尸进程
        print("超时进程已 kill, returncode:", proc.returncode)


async def main() -> None:
    await run_quick()
    await run_with_timeout()


asyncio.run(main())
