import json
from dataclasses import dataclass


@dataclass
class QuotaConfig:
    daily_upload_mb: int
    max_file_size_mb: int
    allowed_types: list

    @classmethod
    def from_json(cls, raw: dict) -> "QuotaConfig":
        # 启动时校验,非法配置快速失败
        assert raw["daily_upload_mb"] > 0, "daily_upload_mb must be positive"
        assert raw["allowed_types"], "allowed_types cannot be empty"
        return cls(**raw)


CONFIG_JSON = '''
{"daily_upload_mb": 500, "max_file_size_mb": 20, "allowed_types": ["pdf", "png"]}
'''


def can_upload(cfg: QuotaConfig, used_mb: int, size_mb: int, ftype: str) -> bool:
    return (ftype in cfg.allowed_types
            and size_mb <= cfg.max_file_size_mb
            and used_mb + size_mb <= cfg.daily_upload_mb)


if __name__ == "__main__":
    cfg = QuotaConfig.from_json(json.loads(CONFIG_JSON))
    print(can_upload(cfg, 480, 15, "pdf"))  # True
    print(can_upload(cfg, 480, 30, "exe"))  # False
