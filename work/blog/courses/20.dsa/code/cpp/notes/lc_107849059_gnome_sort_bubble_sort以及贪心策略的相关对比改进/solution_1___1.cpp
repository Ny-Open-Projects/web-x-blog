// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
// Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比
#include <algorithm> // 引入头文件
#include <cassert>   // 引入头文件
#include <iostream>  // 引入头文件
#include <vector>    // 引入头文件

static void gnome_sort_inplace(std::vector<int> &a) { // 定义函数/方法 gnome_sort_inplace
    size_t i = 0;                                     // 把 0; 写入 size_t i
    while (i < a.size()) { // 循环，直到不满足「下标 i 小于 数组.大小(」
        if (i == 0 || a[i] >= a[i - 1])
            i++; // 若 下标 i 等于 0 或 数组[下标 i] 不低于 数组[下标 i 减 1]) 下标 i 加一 ;
        else {
            std::swap(a[i - 1], a[i]);
            i--;
        } // 否则
    }
}

static void bubble_sort_inplace(std::vector<int> &a) { // 定义函数/方法 bubble_sort_inplace
    bool swapped = true;                               // 把 true 存入 swapped
    while (swapped) {                                  // 循环，直到不满足「swapped」
        swapped = false;                               // 把 false; 写入 swapped
        for (size_t i = 0; i + 1 < a.size();
             i++) { // 让 下标 i 从 0 开始计数，下标 i 加 1 小于 数组.大小() 就继续
            if (a[i] > a[i + 1]) {
                std::swap(a[i], a[i + 1]);
                swapped = true;
            }
        }
    }
}

static int coin_change(std::vector<int> coins, int amount) { // 定义函数/方法 coin_change
    std::sort(coins.begin(), coins.end(),
              std::greater<int>()); // std::sort(硬币面额 迭代位置 , 硬币面额.终点(), std::greater 小于 int
                                    // 超过 ());
    int remaining = amount, count = 0; // 把 目标金额, 计数 赋值为 0 存入 remaining
    for (int coin : coins)             // for (int coin : 硬币面额)
        while (remaining >= coin) {
            remaining -= coin;
            count++;
        } // 循环，直到不满足「remaining 不低于 coin) { remaining 累减 coin; 计数 加一 ; }」
    return remaining == 0 ? count : -1; // 返回 remaining 等于 0 ? 计数 : 减 1
}

int main() {                                      // 程序入口：跑内嵌自测用例
    std::vector<int> a{3, 2, 1};                  // std::vector 小于 int 超过 数组{3, 2, 1};
    gnome_sort_inplace(a);                        // gnome_sort_inplace(数组);
    assert((a == std::vector<int>{1, 2, 3}));     // 断言校验
    std::vector<int> b{3, 2, 1};                  // std::vector 小于 int 超过 b{3, 2, 1};
    bubble_sort_inplace(b);                       // bubble_sort_inplace(b);
    assert((b == std::vector<int>{1, 2, 3}));     // 断言校验
    assert(coin_change({1, 5, 10, 25}, 63) == 6); // 断言校验
    std::cout << "PASS" << std::endl;             // 全部用例通过，输出 PASS
    return 0;                                     // 返回 0
}
