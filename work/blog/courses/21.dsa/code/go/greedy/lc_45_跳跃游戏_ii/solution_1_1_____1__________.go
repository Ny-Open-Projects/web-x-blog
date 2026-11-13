// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241433
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func jump(nums []int) int { // 定义函数/方法 jump
	position := len(nums) - 1 // 把 长度(数组) 减 1 写入 position :
	steps := 0                // 把 0 写入 steps :
	for position > 0 {        // for position 超过 0 {
		for i := 0; i < position; i++ { // 让 下标 i 从 0 开始计数
			if i+nums[i] >= position { // 若 下标 i 加 数组[下标 i] 不低于 position
				position = i // 把 下标 i 写入 position
				steps++      // steps 加一
				break        // 跳出循环
			}
		}
	}
	return steps // 返回 steps
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 3, 1, 1, 4}, 2},
		{[]int{1}, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := jump(c.in); got != c.want { // 若 got : 赋值为 jump(字符.in); got 不等于 字符.want
			ok = false                                                  // 把 false 写入 ok
			fmt.Printf("FAIL jump(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
