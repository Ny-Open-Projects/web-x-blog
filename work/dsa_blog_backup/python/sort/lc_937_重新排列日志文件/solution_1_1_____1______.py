# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374559
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from functools import cmp_to_key  # from functools import cmp_to_key


def reorderLogFiles(logs):  # 定义函数 reorderLogFiles（参数：logs）
    def is_digit(s):  # 定义函数 is_digit（参数：字符串）
        return s[0].isdigit()  # 返回 字符串[0].isdigit()

    def split_log(log):  # 定义函数 split_log（参数：log）
        idx = log.index(" ")  # 把 log.index(' ') 存入 idx
        return log[:idx], log[idx + 1 :]  # 返回 log[:idx], log[idx 加 1:]

    def log_compare(a, b):  # 定义函数 log_compare（参数：数组, b）
        id1, content1 = split_log(a)  # 把 split_log(数组) 写入 id1, content1
        id2, content2 = split_log(b)  # 把 split_log(b) 写入 id2, content2
        d1 = is_digit(content1)  # 把 is_digit(content1) 存入 d1
        d2 = is_digit(content2)  # 把 is_digit(content2) 存入 d2
        if d1 and d2:  # 若 d1 and d2
            return (content1 > content2) - (
                content1 < content2
            )  # 返回 (content1 超过 content2) 减 (content1 小于 content2)
        if not d1 and not d2:  # 若 not d1 and not d2
            if content1 != content2:  # 若 content1 不等于 content2
                return (content1 > content2) - (
                    content1 < content2
                )  # 返回 (content1 超过 content2) 减 (content1 小于 content2)
            return (id1 > id2) - (id1 < id2)  # 返回 (id1 超过 id2) 减 (id1 小于 id2)
        return -1 if not d1 else 1  # 返回 减 1 if not d1 else 1

    digit_logs = []  # 把 [] 存入 digit_logs
    letter_logs = []  # 把 [] 存入 ter_logs
    for log in logs:  # 逐个取出 logs 的元素（log）
        _, content = split_log(log)  # 把 split_log(log) 写入 _, content
        if is_digit(content):  # 若 is_digit(content
            digit_logs.append(log)  # 把 log 追加到列表尾部
        else:  # 否则
            letter_logs.append(log)  # 把 log 追加到列表尾部

    letter_logs.sort(key=cmp_to_key(log_compare))  # 排序
    return letter_logs + digit_logs  # 返回 letter_logs 加 digit_logs


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorderLogFiles(logs))  # 打印输出
