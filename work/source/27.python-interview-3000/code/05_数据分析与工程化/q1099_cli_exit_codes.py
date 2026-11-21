import sys

EX_OK, EX_GENERAL, EX_USAGE, EX_CONFIG = 0, 1, 2, 3

class AppError(Exception):
    exit_code = EX_GENERAL

class ConfigError(AppError):
    exit_code = EX_CONFIG

def load_config(path):
    if path is None:
        raise ConfigError("缺少配置文件路径,用 --config 指定")
    return {"path": path}

def main(argv):
    if "--help" in argv:
        print("用法: app [--config FILE]")
        return EX_OK
    try:
        path = argv[argv.index("--config") + 1] if "--config" in argv else None
        cfg = load_config(path)
        print("运行成功", cfg)
        return EX_OK
    except AppError as e:
        print(f"错误: {e}", file=sys.stderr)
        return e.exit_code

if __name__ == "__main__":
    code = main(sys.argv[1:])
    print(f"退出码 {code}(0 成功 1 一般 2 用法 3 配置)")
