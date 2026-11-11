// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// LeetCode 933. 最近的请求次数 — C++ 版
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件

// 方案2：front 指针懒删除（不真正移除元素，仅移动队头下标）
class RecentCounter {       // 定义类型
    std::vector<int> queue; // std::vector 小于 int 超过 队列;
    size_t front = 0;       // 把 0; 写入 size_t front

  public:                                 // public:
    int ping(int t) {                     // 定义函数/方法 ping
        queue.push_back(t);               // 队列 追加 另一字符串);
        while (queue[front] < t - 3000) { // 循环，直到不满足「队列[front] 小于 另一字符串 减 3000」
            ++front;                      // 加一 front;
        }
        return static_cast<int>(queue.size() -
                                front); // 返回 static_cast 小于 int 超过 (队列.大小() 减 front)
    }
};

int main() { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    RecentCounter c; // RecentCounter 字符;
    int got[4] = {c.ping(1), c.ping(100), c.ping(3001), c.ping(3002)};
    int want[4] = {1, 2, 3, 3};    // 把 { 1, 2, 3, 3 }; 写入 int want[4]
    for (int i = 0; i < 4; ++i) {  // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        assert(got[i] == want[i]); // 断言校验
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
