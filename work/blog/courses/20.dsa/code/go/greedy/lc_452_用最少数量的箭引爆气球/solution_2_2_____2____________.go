// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244333
package main // 引入依赖

import (
	"fmt"
	"os"
	"sort"
) // 引入依赖

func findMinArrowShots(points [][]int) int { // 定义函数/方法 findMinArrowShots
	if len(points) == 0 { // 若 长度(points) 等于 0
		return 0 // 返回 0
	}
	sort.Slice(points, func(i, j int) bool { return points[i][1] < points[j][1] })
	arrows := 1                    // 把 1 写入 arrows :
	end := points[0][1]            // 把 points[0][1] 写入 end :
	for _, p := range points[1:] { // 同时取 _ 与 节点 遍历
		if p[0] > end { // 若 节点[0] 超过 终点
			arrows++   // arrows 加一
			end = p[1] // 把 节点[1] 写入 终点
		}
	}
	return arrows // 返回 arrows
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   [][]int // in [][]int
		want int     // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[][]int{{10, 16}, {2, 8}, {1, 6}, {7, 12}}, 2},
		{[][]int{{1, 2}, {3, 4}, {5, 6}, {7, 8}}, 4},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findMinArrowShots(c.in); got != c.want { // 若 got : 赋值为 findMinArrowShots(字符.in); got 不等于 字符.want
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL findMinArrowShots(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
