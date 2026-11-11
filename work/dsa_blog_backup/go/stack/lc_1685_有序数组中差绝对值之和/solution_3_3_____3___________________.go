// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374997
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func getSumAbsoluteDifferences(nums []int) []int { // 定义函数/方法 getSumAbsoluteDifferences
	n := len(nums)           // 把 长度(数组) 写入 n :
	ans := make([]int, n)    // 把 make([]int, 元素个数) 写入 ans :
	sumTotal := 0            // 把 0 写入 sumTotal :
	for _, v := range nums { // 同时取 _ 与 值 遍历
		sumTotal += v // sumTotal累加 值
	}
	ans[0] = sumTotal - nums[0]*n // 把 sumTotal 减 数组[0] 乘 元素个数 写入 ans[0]
	for i := 1; i < n; i++ {      // 让 下标 i 从 1 开始计数
		d := nums[i] - nums[i-1]      // 把 数组[下标 i] 减 数组[下标 i 减 1] 写入 d :
		ans[i] = ans[i-1] - (n-2*i)*d // 把 答案[下标 i 减 1] 减 (元素个数 减 2 乘 下标 i) 乘 d 写入 ans[i]
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
