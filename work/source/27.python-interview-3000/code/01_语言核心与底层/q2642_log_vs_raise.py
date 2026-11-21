"""日志与异常的分层:库层只抛,边界层记并收口,中间层有恢复才记。"""
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("app")


class Repo:
    """库层:只抛,不记——它不知道上层想怎么办。"""

    def fetch(self, key):
        raise ConnectionError(f"repo 不可达: {key}")


def get_user(repo, key):
    """中间层:能降级才有资格记日志。"""
    try:
        return repo.fetch(key)
    except ConnectionError:
        log.warning("主库不可达, 降级为默认用户 key=%s", key)
        return {"name": "guest"}


class BrokenRepo(Repo):
    """故障超出中间层的降级能力:只能上抛,由边界层收口。"""

    def fetch(self, key):
        raise RuntimeError("未知故障")


def main(repo):
    """应用边界:统一收口未处理异常,只记一次。"""
    try:
        return get_user(repo, "u1")
    except Exception:
        log.exception("任务失败")
        return None


if __name__ == "__main__":
    print(main(Repo()))
    print(main(BrokenRepo()))
