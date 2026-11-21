def bad(item, bucket=[]):
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

if __name__ == "__main__":
    print(bad(1), bad(2))       # [1] [1, 2]  共享同一个 list
    print(good(1), good(2))     # [1] [2]     每次新建

    print(bad.__defaults__)     # ([1, 2],)  默认值就存在这里
