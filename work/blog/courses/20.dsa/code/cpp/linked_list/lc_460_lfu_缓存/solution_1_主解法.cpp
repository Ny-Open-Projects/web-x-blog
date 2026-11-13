// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137295891
// LeetCode 460. LFU缓存 — C++ 版（方案1）
#include <cassert>                            // 引入头文件
#include <iostream>                           // 引入头文件
#include <unordered_map>                      // 引入头文件
struct LFUCacheSim {                          // 定义类型
    int cap;                                  // int cap;
    std::unordered_map<int, int> vals, freq;  // std::unordered_map 小于 int, int 超过 vals, 频次表;
    std::unordered_map<int, long long> stamp; // std::unordered_map 小于 int, long long 超过 stamp;
    long long clock_ = 0;                     // 把 0 存入 clock_
    explicit LFUCacheSim(int capacity)
        : cap(capacity) {}        // explicit LFUCacheSim(int capacity) : cap(capacity) {}
    int get(int key) {            // 定义函数/方法 get
        ++clock_;                 // 加一 clock_;
        auto it = vals.find(key); // 把 vals 查找 key) 存入 it
        if (it == vals.end())
            return -1;       // 若 it 等于 vals.终点()，直接返回 减 1
        ++freq[key];         // 加一 频次表[key];
        stamp[key] = clock_; // 把 clock_; 写入 stamp[key]
        return it->second;   // 返回 it 减 超过 second
    }
    void put(int key, int value) { // 定义函数/方法 put
        ++clock_;                  // 加一 clock_;
        auto it = vals.find(key);  // 把 vals 查找 key) 存入 it
        if (it != vals.end()) {    // 若 it 不等于 vals.终点(
            it->second = value;    // 把 value; 写入 it->second
            ++freq[key];           // 加一 频次表[key];
            stamp[key] = clock_;   // 把 clock_; 写入 stamp[key]
            return;                // return;
        }
        if (cap == 0)
            return;                                 // 若 cap 等于 0) return;
        if (static_cast<int>(vals.size()) == cap) { // 若 static_cast 小于 int 超过 (vals.大小()) 等于 cap
            int evict = -1;                         // 把 减 1 存入 evict
            long long bestF = -1, bestS = -1;       // 把 减 1, bestS 赋值为 减 1 存入 bestF
            for (auto &[k, v] : vals) {             // for (auto 按位与 [下标 k, 值] : vals) {
                long long f = freq[k], s = stamp[k]; // 把 频次表[下标 k], 字符串 赋值为 stamp[下标 k] 存入 f
                if (evict == -1 || f < bestF ||
                    (f == bestF &&
                     s < bestS)) { // 若 evict 等于 减 1 或 f 小于 bestF 或 (f 等于 bestF 且 字符串 小于 bestS
                    evict = k;
                    bestF = f;
                    bestS = s; // 把 下标 k; bestF 赋值为 f; bestS 赋值为 字符串; 写入 evict
                }
            }
            vals.erase(evict);
            freq.erase(evict);
            stamp.erase(evict); // vals 删除 evict); 频次表 删除 evict); stamp 删除 evict);
        }
        vals[key] = value;   // 把 value; 写入 vals[key]
        freq[key] = 1;       // 把 1; 写入 freq[key]
        stamp[key] = clock_; // 把 clock_; 写入 stamp[key]
    }
};
int main() {                          // 程序入口：跑内嵌自测用例
    LFUCacheSim lfu(2);               // LFUCacheSim lfu(2);
    lfu.put(1, 1);                    // lfu.put(1, 1);
    lfu.put(2, 2);                    // lfu.put(2, 2);
    assert(lfu.get(1) == 1);          // 断言校验
    lfu.put(3, 3);                    // lfu.put(3, 3);
    assert(lfu.get(2) == -1);         // 断言校验
    assert(lfu.get(3) == 3);          // 断言校验
    lfu.put(4, 4);                    // lfu.put(4, 4);
    assert(lfu.get(1) == -1);         // 断言校验
    assert(lfu.get(3) == 3);          // 断言校验
    assert(lfu.get(4) == 4);          // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
