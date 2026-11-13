// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301
// LeetCode 380. O(1)时间插入删除和获取随机元素 — C++ 版（方案1）
#include <cassert>                       // 引入头文件
#include <iostream>                      // 引入头文件
#include <unordered_map>                 // 引入头文件
#include <vector>                        // 引入头文件
struct RandomizedSet {                   // 定义类型
    std::vector<int> vals;               // std::vector 小于 int 超过 vals;
    std::unordered_map<int, size_t> pos; // std::unordered_map 小于 int, size_t 超过 pos;
    bool insert(int val) {               // 定义函数/方法 insert
        if (pos.count(val))
            return false;       // 若 pos.计数(值)，直接返回 false
        pos[val] = vals.size(); // 把 vals.大小(); 写入 pos[val]
        vals.push_back(val);    // vals 追加 值);
        return true;            // 返回 true
    }
    bool remove(int val) {       // 定义函数/方法 remove
        auto it = pos.find(val); // 把 pos 查找 值) 存入 it
        if (it == pos.end())
            return false;        // 若 it 等于 pos.终点()，直接返回 false
        size_t idx = it->second; // 把 it 减 超过 second; 写入 size_t idx
        int last = vals.back();  // 把 vals.back() 存入 last
        vals[idx] = last;        // 把 last; 写入 vals[idx]
        pos[last] = idx;         // 把 idx; 写入 pos[last]
        vals.pop_back();         // 弹出栈顶元素
        pos.erase(it);           // pos 删除 it);
        return true;             // 返回 true
    }
    int getRandom() { return vals[0]; } // int getRandom() { return vals[0]; }
};
int main() {                    // 程序入口：跑内嵌自测用例
    RandomizedSet s;            // RandomizedSet 字符串;
    assert(s.insert(1));        // 断言校验
    assert(!s.remove(2));       // 断言校验
    assert(s.insert(2));        // 断言校验
    int r = s.getRandom();      // 把 字符串.getRandom() 存入 右指针
    assert(r == 1 || r == 2);   // 断言校验
    assert(s.remove(1));        // 断言校验
    assert(!s.insert(2));       // 断言校验
    assert(s.getRandom() == 2); // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS