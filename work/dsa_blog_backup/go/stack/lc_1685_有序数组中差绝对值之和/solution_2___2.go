// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374997
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func getSumAbsoluteDifferences(nums []int) []int { // 定义函数/方法 getSumAbsoluteDifferences
	prefix := []int{0}               // 把 []int{0} 写入 prefix :
	for i := 0; i < len(nums); i++ { // 让 下标 i 从 0 开始计数
		prefix = append(prefix, prefix[i]+nums[i]) // 把 append(prefix, prefix[下标 i] 加 数组[下标 i]) 写入 prefix
	}
	ans := []int{}           // 把 []int{} 写入 ans :
	n := len(nums)           // 把 长度(数组) 写入 n :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		x := nums[i]            // 把 数组[下标 i] 写入 x :
		left := i*x - prefix[i] // 把 下标 i 乘 x 减 prefix[下标 i] 写入 left :
		right := prefix[n] - prefix[i+1] - x*(n-1-i)
		ans = append(ans, left+right) // 把 append(答案, 左边界 加 右边界) 写入 答案
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{3, 2, 3}},
		{[]int{1, 4, 6, 8, 10}, []int{24, 15, 13, 15, 21}},
		{[]int{2, 3, 5}, []int{4, 3, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := getSumAbsoluteDifferences(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                       // 把 false 写入 ok
			fmt.Printf("FAIL getSumAbsoluteDifferences(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
