// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func sortArrayByParity(nums []int) []int { // 定义函数/方法 sortArrayByParity
	n := len(nums)             // 把 长度(数组) 写入 n :
	res := make([]int, n)      // 把 make([]int, 元素个数) 写入 res :
	index := 0                 // 把 0 写入 index :
	for _, num := range nums { // 同时取 _ 与 num 遍历
		if num%2 == 0 { // 若 num 对…取模 2 等于 0
			res[index] = num // 把 num 写入 res[index]
			index++          // index 加一
		}
	}
	for _, num := range nums { // 同时取 _ 与 num 遍历
		if num%2 == 1 { // 若 num 对…取模 2 等于 1
			res[index] = num // 把 num 写入 res[index]
			index++          // index 加一
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{2, 1, 3}},
		{[]int{3, 1, 2, 4}, []int{2, 4, 3, 1}},
		{[]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := sortArrayByParity(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL sortArrayByParity(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
