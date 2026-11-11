// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func sortedSquares(nums []int) []int { // 定义函数/方法 sortedSquares
	n := len(nums)           // 把 长度(数组) 写入 n :
	ans := make([]int, n)    // 把 make([]int, 元素个数) 写入 ans :
	i, j, pos := 0, n-1, n-1 // 把 0, 元素个数 减 1, 元素个数 减 1 写入 i, j, pos :
	for i <= j {             // 把 下标 j { 写入 for i <
		si := nums[i] * nums[i] // 把 数组[下标 i] 乘 数组[下标 i] 写入 si :
		sj := nums[j] * nums[j] // 把 数组[下标 j] 乘 数组[下标 j] 写入 sj :
		if si > sj {            // 若 si 超过 sj
			ans[pos] = si // 把 si 写入 ans[pos]
			i++           // 下标 i 加一
		} else { // 否则
			ans[pos] = sj // 把 sj 写入 ans[pos]
			j--           // 下标 j 减一
		}
		pos-- // pos 减一
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{1, 4, 9}},
		{[]int{-4, -1, 0, 3, 10}, []int{0, 1, 9, 16, 100}},
		{[]int{-7, -3, 2, 3, 11}, []int{4, 9, 9, 49, 121}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := sortedSquares(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL sortedSquares(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
