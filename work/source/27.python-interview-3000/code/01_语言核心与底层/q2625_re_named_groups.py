"""re 命名组:定义、groupdict、模式内回引与替换引用。"""
import re

LOG = re.compile(
    r"(?P<level>INFO|WARN|ERROR) (?P<ts>\d{4}-\d{2}-\d{2}) (?P<msg>.*)"
)

if __name__ == "__main__":
    m = LOG.match("ERROR 2026-11-05 db connection lost")
    print("groupdict:", m.groupdict())
    print("单组取值:", m.group("level"), m.group("ts"))

    # 模式内回引:匹配重复单词
    dup = re.compile(r"(?P<word>\w+) (?P=word)")
    print("回引命中:", dup.search("hello hello world").group("word"))

    # 替换串里引用命名组
    print("日期换位:",
          re.sub(r"(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})",
                 r"\g<d>/\g<m>/\g<y>", "2026-11-05"))

    # 无命名组不进 groupdict
    plain = re.match(r"(\w+) (?P<last>\w+)", "Ada Lovelace")
    print("groupdict 只含命名组:", plain.groupdict())
