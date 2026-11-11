// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595
// LeetCode 295. 数据流的中位数 — C++ 版（方案2）
#include <cassert>                 // 引入头文件
#include <cstdio>                  // 引入头文件
#include <iostream>                // 引入头文件
#include <queue>                   // 引入头文件
struct MedianFinder {              // 定义类型
    std::priority_queue<int> maxH; // std::priority_queue 小于 int 超过 maxH;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minH;
    void addNum(int num) { // 定义函数/方法 addNum
        if (maxH.empty() || num <= maxH.top())
            maxH.push(num); // 若 maxH 是否为空 或 num 不超过 maxH.top()) maxH 追加 num);
        else
            minH.push(num); // 否则
        if (maxH.size() > minH.size() + 1) {
            minH.push(maxH.top());
            maxH.pop();
        } else if (minH.size() > maxH.size()) {
            maxH.push(minH.top());
            minH.pop();
        }
    }
    double findMedian() const { // double findMedian() const {
        if (maxH.size() == minH.size())
            return (maxH.top() + minH.top()) / 2.0;
        return maxH.top(); // 返回 maxH.top()
    }
};
int main() {         // 程序入口：跑内嵌自测用例
    MedianFinder mf; // MedianFinder mf;
    for (int x : {1, 2, 3, 4, 5})
        mf.addNum(x);                 // for (int x : {1, 2, 3, 4, 5}) mf.addNum(x);
    assert(mf.findMedian() == 3.0);   // 断言校验
    MedianFinder mf2;                 // MedianFinder mf2;
    mf2.addNum(1);                    // mf2.addNum(1);
    mf2.addNum(2);                    // mf2.addNum(2);
    assert(mf2.findMedian() == 1.5);  // 断言校验
    mf2.addNum(3);                    // mf2.addNum(3);
    assert(mf2.findMedian() == 2.0);  // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
