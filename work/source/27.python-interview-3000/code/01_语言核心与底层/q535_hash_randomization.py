import sys

if __name__ == "__main__":
    print("randomization on:", sys.flags.hash_randomization)
    print("hash('python') =", hash("python"), "(differs across runs)")
    print("hash(42) =", hash(42), "(int hash is stable)")
    print("same within this process:", hash("a") == hash("a"))

    d = {}
    for i in range(1000):
        d[f"key{i}"] = i
    print("dict still O(1) on average:", len(d), "keys")

    print("rule: persist digests via hashlib, never via hash()")
