/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916 */
/* LeetCode 2454. 下一个更大元素 IV — C 版（方案2） */
#include <stdio.h>                                              // 引入头文件
static void second_greater(const int *nums, int n, int out[]) { // 定义函数/方法 second_greater
    for (int i = 0; i < n; i++)
        out[i] = -1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int s1[4096], t1 = 0, s2[4096], t2 = 0; // 把 0, s2[4096], t2 赋值为 0; 写入 int s1[4096], t1
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        while (t2 > 0 && nums[s2[t2 - 1]] < nums[i])
            out[s2[--t2]] = nums[i];
        while (t1 > 0 && nums[s1[t1 - 1]] < nums[i])
            s2[t2++] = s1[--t1];
        s1[t1++] = i; // 把 下标 i; 写入 s1[t1++]
    }
}
int main(void) {                                    // 程序入口：跑内嵌自测用例
    int out[4096];                                  // int out[4096];
    second_greater((int[]){2, 4, 0, 9, 6}, 5, out); // second_greater((int[]){2,4,0,9,6}, 5, out);
    if (!(out[0] == 9 && out[1] == 6 && out[2] == 6 && out[3] == -1 && out[4] == -1)) {
        printf("FAIL 1\n");
        return 1;
    }
    second_greater((int[]){5, 4, 3, 2, 1}, 5, out); // second_greater((int[]){5,4,3,2,1}, 5, out);
    if (!(out[0] == -1 && out[4] == -1)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS