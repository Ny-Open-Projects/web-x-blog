// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244140
package main // 引入依赖

import (
	"fmt"
	"os"
	"sort"
) // 引入依赖

func eraseOverlapIntervals(intervals [][]int) int { // 定义函数/方法 eraseOverlapIntervals
	if len(intervals) == 0 { // 若 长度(intervals) 等于 0
		return 0 // 返回 0
	}
	sort.Slice(intervals, func(i, j int) bool { return intervals[i][1] < intervals[j][1] })
	count := 1                            // 把 1 写入 count :
	end := intervals[0][1]                // 把 intervals[0][1] 写入 end :
	for i := 1; i < len(intervals); i++ { // 让 下标 i 从 1 开始计数
		if intervals[i][0] >= end { // 若 intervals[下标 i][0] 不低于 终点
			count++               // 计数 加一
			end = intervals[i][1] // 把 intervals[下标 i][1] 写入 终点
		}
	}
	return len(intervals) - count // 返回 长度(intervals) 减 计数
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   [][]int // in [][]int
		want int     // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[][]int{{1, 2}, {2, 3}, {3, 4}, {1, 3}}, 1},
		{[][]int{{1, 2}, {1, 2}, {1, 2}}, 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := eraseOverlapIntervals(c.in); got != c.want { // 若 got : 赋值为 eraseOverlapIntervals(字符.in); got 不等于 字符.want
			ok = false                                                                   // 把 false 写入 ok
			fmt.Printf("FAIL eraseOverlapIntervals(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
