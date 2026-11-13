// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
package main // 引入依赖

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
) // 引入依赖

func largestNumber(nums []int) string { // 定义函数/方法 largestNumber
	strs := make([]string, len(nums)) // 把 make([]string, 长度(数组)) 写入 strs :
	for i, v := range nums {          // 同时取 下标 i 与 值 遍历
		strs[i] = strconv.Itoa(v) // 把 strconv.Itoa(值) 写入 strs[i]
	}
	sort.SliceStable(strs, func(i, j int) bool { // sort.SliceStable(strs, func(下标 i, 下标 j int) bool {
		return strs[i]+strs[j] > strs[j]+strs[i] // 返回 strs[下标 i] 加 strs[下标 j] 超过 strs[下标 j] 加 strs[下标 i]
	}) // })
	if len(strs) > 0 && strs[0] == "0" { // 若 长度(strs) 超过 0 且 strs[0] 等于 「0」
		return "0" // 返回 「0」
	}
	return strings.Join(strs, "") // 返回 strings.Join(strs, 「」)
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int  // in []int
		want string // want string
	}{ // }{
		{[]int{1, 2, 3}, "321"},
		{[]int{10, 2}, "210"},
		{[]int{3, 30, 34, 5, 9}, "9534330"},
		{[]int{0, 0}, "0"},
		{[]int{30, 3, 34, 5, 9}, "9534330"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := largestNumber(c.in); got != c.want { // 若 got : 赋值为 largestNumber(字符.in); got 不等于 字符.want
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL largestNumber(%v)=%q want %q\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
