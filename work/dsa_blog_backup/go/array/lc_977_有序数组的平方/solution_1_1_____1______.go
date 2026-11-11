// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func sortedSquares(nums []int) []int { // 定义函数/方法 sortedSquares
	ans := make([]int, len(nums)) // 把 make([]int, 长度(数组)) 写入 ans :
	for i, x := range nums {      // 同时取 下标 i 与 x 遍历
		ans[i] = x * x // 把 x 乘 x 写入 ans[i]
	}
	sort.Ints(ans) // sort.Ints(答案)
	return ans     // 返回 答案
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
