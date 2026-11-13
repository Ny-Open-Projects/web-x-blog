// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
// 实现LRU缓存算法功能 — C++ 版（方案3）
#include <cassert>                        // 引入头文件
#include <iostream>                       // 引入头文件
#include <list>                           // 引入头文件
#include <unordered_map>                  // 引入头文件
struct NoteLru {                          // 定义类型
    int cap;                              // int cap;
    std::list<std::pair<int, int>> items; // std::列表 小于 std::pair 小于 int, int 超过 超过 items;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> pos;
    explicit NoteLru(int capacity) : cap(capacity) {} // explicit NoteLru(int capacity) : cap(capacity) {}
    int get(int key) {                                // 定义函数/方法 get
        auto it = pos.find(key);                      // 把 pos 查找 key) 存入 it
        if (it == pos.end())
            return -1; // 若 it 等于 pos.终点()，直接返回 减 1
        items.splice(items.begin(), items,
                     it->second);  // items.splice(items 迭代位置 , items, it 减 超过 second);
        return it->second->second; // 返回 it 减 超过 second 减 超过 second
    }
    void put(int key, int value) {      // 定义函数/方法 put
        auto it = pos.find(key);        // 把 pos 查找 key) 存入 it
        if (it != pos.end()) {          // 若 it 不等于 pos.终点(
            it->second->second = value; // 把 value; 写入 it->second->second
            items.splice(items.begin(), items,
                         it->second); // items.splice(items 迭代位置 , items, it 减 超过 second);
            return;                   // return;
        }
        if (static_cast<int>(items.size()) == cap) { // 若 static_cast 小于 int 超过 (items.大小()) 等于 cap
            pos.erase(items.back().first);           // pos 删除 items.back().first);
            items.pop_back();                        // 弹出栈顶元素
        }
        items.emplace_front(key, value); // items.emplace_front(key, value);
        pos[key] = items.begin();        // 把 items 迭代位置 ; 写入 pos[key]
    }
};
int main() {                // 程序入口：跑内嵌自测用例
    NoteLru c(2);           // NoteLru 字符(2);
    c.put(1, 1);            // 字符.put(1, 1);
    c.put(2, 2);            // 字符.put(2, 2);
    assert(c.get(1) == 1);  // 断言校验
    c.put(3, 3);            // 字符.put(3, 3);
    assert(c.get(2) == -1); // 断言校验
    c.put(4, 4);            // 字符.put(4, 4);
    assert(c.get(1) == -1); // 断言校验
    assert(c.get(3) == 3);  // 断言校验
    assert(c.get(4) == 4);  // 断言校验
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS