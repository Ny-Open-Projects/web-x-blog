"""3.9 的 removeprefix/removesuffix:替代裸切片与 strip 误用。"""
import sys

if __name__ == "__main__":
    print("Python 版本:", sys.version.split()[0])
    filename = "report_2024_final.pdf"
    print("removeprefix:", filename.removeprefix("report_"))
    print("removesuffix:", filename.removesuffix(".pdf"))
    print("前缀不存在原样返回:", "data.csv".removeprefix("report_"))

    old = filename[len("report_"):] if filename.startswith("report_") else filename
    print("旧写法等价但啰嗦:", old)

    print("lstrip 按字符集剥离会剥过头:", "testest_value".lstrip("test_"))
    print("removeprefix 语义精确:", "testest_value".removeprefix("test_"))

    for name in ["a.tar.gz", "b", "c.txt"]:
        print(name, "->", name.removesuffix(".gz").removesuffix(".tar"))
