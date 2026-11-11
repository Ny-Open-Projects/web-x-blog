# LeetCode 107573690. 抽象思维之对比算法,发现共性 (ts)

> 来源：[Wang's Blog](https://blog.csdn.net/tyro_java/article/details/107573690)
> 语言：**ts**（博客原文）

## 题目描述

(原始博客未提供题目描述)

## 示例

```
#include 
using namespace std;
int h;
int num;
struct position { int x; };
position dxy[] = {{1}, {2}, {3}}; 
position start_pos = {0}, goal_pos = {h};
position path[100];
/* --------------------- 辅助函数 开始 ------------------------ */
bool IsEq(position pos1, position pos2) { 
 return (pos1.x == pos2.x);
}
bool IsDone(position pos) {
 return IsEq(pos, goal_pos);
}
bool IsValid(position pos) {
 return (pos.x >=0) && (pos.x h);
}
position GetNewPos(position pos, int k) {
 position next_pos = {pos.x + dxy[k].x};
 return next_pos;
}
void LogStep(int step, position pos) {
 path[step] = pos;
}
void OutStep(position pos) { 
 cout pos.x ' ';
}
void OutAll(int step) {
 for (int i=0; istep; i++) {
 OutStep(path[i]);
 }
 cout endl;
}
/* --------------------- 辅助函数 结束 ------------------------ */
// 递归函数
void Jump(position pos, int step) {
 // 是否达到目标
 if(IsDone(pos)) {
 num++; // 方案数+1
 cout "当前位置" num ": ";
 OutAll(step); // 输出方案
 return;
 }
 // 遍历N种方案
 for (int k = 0; k sizeof(dxy) / sizeof(dxy[0]); k++) {
 position next_pos = GetNewPos(pos, k);
 if(!IsValid(next_pos)) {
 continue; // nex_pos是否可行？
 }
 LogStep(step, next_pos); // 记录方案
 Jump(next_pos, step + 1); // 走下一步
 }
}
// main函数
int main() {
 // 要求用户输入来更新最终位置
 cout "请输入楼梯台阶数："; 
 cin >> h;
 position h_num = {h};
 goal_pos = h_num;
 num = 0; // 初始方案数置0
 Jump(start_pos, 0); // 走第一步
 cout "总方案数: " num endl;
 return 0;
}
```

## 提示

(无)

## 进阶

(无)

## 解法列表

| 方案 | 文件 | 来源语言 |
| --- | --- | --- |
| 方案1 | `solution_1_方案1.ts` | cpp |
| 方案2 | `solution_2_方案2.ts` | cpp |
| 方案3 | `solution_3_方案3.ts` | cpp |
