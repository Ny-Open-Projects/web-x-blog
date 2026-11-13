package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 丢失的数字：高斯求和 - 总和差值
// 忠实翻译 Python ref_missingNumber: n*(n+1)//2 - sum(nums)
func missingNumber(nums []int) int { // 定义函数/方法 missingNumber
	n := len(nums)           // 把 长度(数组) 写入 n :
	sum := 0                 // 把 0 写入 sum :
	for _, v := range nums { // 同时取 _ 与 值 遍历
		sum += v // 累计和累加 值
	}
	return n*(n+1)/2 - sum // 返回 元素个数 乘 (元素个数 加 1) 除以 2 减 累计和
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{3, 0, 1}, 2},
		{[]int{0, 1}, 2},
		{[]int{9, 6, 4, 2, 3, 5, 7, 0, 1}, 8},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := missingNumber(c.nums) // 把 missingNumber(字符.数组) 写入 got :
		if got != c.want {           // 若 got 不等于 字符.want
			fmt.Printf("FAIL: missingNumber(%v)=%d want %d\n", c.nums, got, c.want) // 打印输出
			ok = false                                                              // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
