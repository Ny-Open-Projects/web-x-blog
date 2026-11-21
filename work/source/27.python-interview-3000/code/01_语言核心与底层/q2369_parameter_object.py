"""参数对象的引入时机:同组参数收成 frozen dataclass 值对象。"""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class RetryPolicy:
    """一组总是一起传递的参数收成一个值对象。"""
    attempts: int = 3
    backoff: float = 0.5
    jitter: bool = True
    retry_on: tuple = ("TimeoutError",)


def fetch(url, policy):
    print(f"fetch {url} attempts={policy.attempts} backoff={policy.backoff}")


def fetch_all(urls, policy):
    for url in urls:
        fetch(url, policy)


if __name__ == "__main__":
    policy = RetryPolicy()
    fetch("/a", policy)
    fetch_all(["/b", "/c"], policy)

    aggressive = RetryPolicy(attempts=8, backoff=0.1, jitter=False)
    fetch("/heavy", aggressive)

    no_retry = replace(policy, attempts=1)
    print("派生策略:", no_retry)
