// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func longestMonotonicSubarray(nums []int) int { // 定义函数/方法 longestMonotonicSubarray
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	n := len(nums)           // 把 长度(数组) 写入 n :
	ans := 1                 // 把 1 写入 ans :
	length := 1              // 把 1 写入 length :
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		if nums[i] > nums[i-1] { // 若 数组[下标 i] 超过 数组[下标 i 减 1]
			length++          // 长度 加一
			if ans < length { // 若 答案 小于 长度
				ans = length // 把 长度 写入 答案
			}
		} else { // 否则
			length = 1 // 把 1 写入 长度
		}
	}
	length = 1               // 把 1 写入 长度
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		if nums[i] < nums[i-1] { // 若 数组[下标 i] 小于 数组[下标 i 减 1]
			length++          // 长度 加一
			if ans < length { // 若 答案 小于 长度
				ans = length // 把 长度 写入 答案
			}
		} else { // 否则
			length = 1 // 把 1 写入 长度
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 4, 3, 3, 2}, 2},
		{[]int{1, 2, 3, 4, 5}, 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := longestMonotonicSubarray(c.in); got != c.want { // 若 got : 赋值为 longestMonotonicSubarray(字符.in); got 不等于 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL longestMonotonicSubarray(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
