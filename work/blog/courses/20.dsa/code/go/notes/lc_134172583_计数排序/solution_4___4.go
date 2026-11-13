// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func countSort(nums []int) []int { // 定义函数/方法 countSort
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return []int{} // 返回 []int{}
	}
	mn, mx := nums[0], nums[0] // 把 数组[0], 数组[0] 写入 mn, mx :
	for _, v := range nums {   // 同时取 _ 与 值 遍历
		if v < mn { // 若 值 小于 mn
			mn = v // 把 值 写入 mn
		}
		if v > mx { // 若 值 超过 mx
			mx = v // 把 值 写入 mx
		}
	}
	cnt := make([]int, mx-mn+1) // 把 make([]int, mx 减 mn 加 1) 写入 cnt :
	for _, v := range nums {    // 同时取 _ 与 值 遍历
		cnt[v-mn]++ // 计数[值 减 mn] 加一
	}
	res := make([]int, 0, len(nums)) // 把 make([]int, 0, 长度(数组)) 写入 res :
	for j := 0; j < len(cnt); j++ {  // 让 下标 j 从 0 开始计数
		for k := 0; k < cnt[j]; k++ { // 让 下标 k 从 0 开始计数
			res = append(res, j+mn) // 把 append(结果, 下标 j 加 mn) 写入 结果
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := countSort(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL countSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
