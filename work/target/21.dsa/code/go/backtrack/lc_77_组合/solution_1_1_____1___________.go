// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240015
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func combine(n, k int) [][]int { // 定义函数/方法 combine
	result := [][]int{}                       // 把 [][]int{} 写入 result :
	var backtrack func(start int, path []int) // var backtrack func(起点 int, 当前路径 []int)
	backtrack = func(start int, path []int) { // 把 func(起点 int, 当前路径 []int) { 写入 backtrack
		if len(path) == k { // 若 长度(当前路径) 等于 下标 k
			result = append(result, append([]int{}, path...)) // 把 append(结果, append([]int{}, 当前路径...)) 写入 结果
			return                                            // return
		}
		for i := start; i <= n; i++ { // 把 起点; 下标 i 不超过 元素个数; 下标 i 加一 { 写入 for i :
			path = append(path, i)    // 把 append(当前路径, 下标 i) 写入 当前路径
			backtrack(i+1, path)      // backtrack(下标 i 加 1, 当前路径)
			path = path[:len(path)-1] // 把 当前路径[:长度(当前路径) 减 1] 写入 当前路径
		}
	}
	backtrack(1, []int{}) // backtrack(1, []int{})
	return result         // 返回 结果
}

func norm2D(s [][]int) [][]int { // 定义函数/方法 norm2D
	out := make([][]int, len(s)) // 把 make([][]int, 长度(字符串)) 写入 out :
	for i := range s {           // 把 range 字符串 { 写入 for i :
		out[i] = append([]int{}, s[i]...) // 把 append([]int{}, 字符串[下标 i]...) 写入 out[i]
		sort.Ints(out[i])                 // sort.Ints(out[下标 i])
	}
	sort.Slice(out, func(a, b int) bool { // sort.Slice(out, func(数组, b int) bool {
		return fmt.Sprint(out[a]) < fmt.Sprint(out[b]) // 返回 fmt.Sprint(out[数组]) 小于 fmt.Sprint(out[b])
	}) // })
	return out // 返回 out
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n, k int     // 元素个数, 下标 k int
		want [][]int // want [][]int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{4, 2, [][]int{{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}}},
		{1, 1, [][]int{{1}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := norm2D(combine(c.n, c.k))   // 把 norm2D(combine(字符.元素个数, 字符.下标 k)) 写入 got :
		want := norm2D(c.want)             // 把 norm2D(字符.want) 写入 want :
		if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL combine(%d,%d)=%v want %v\n", c.n, c.k, got, want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
