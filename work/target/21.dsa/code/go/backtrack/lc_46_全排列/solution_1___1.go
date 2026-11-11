// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134689827
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func permute(nums []int) [][]int { // 定义函数/方法 permute
	res := [][]int{}                // 把 [][]int{} 写入 res :
	used := make([]bool, len(nums)) // 把 make([]bool, 长度(数组)) 写入 used :
	var backtrack func(path []int)  // var backtrack func(当前路径 []int)
	backtrack = func(path []int) {  // 把 func(当前路径 []int) { 写入 backtrack
		if len(path) == len(nums) { // 定义函数/方法 len
			res = append(res, append([]int{}, path...)) // 把 append(结果, append([]int{}, 当前路径...)) 写入 结果
			return                                      // return
		}
		for i := 0; i < len(nums); i++ { // 让 下标 i 从 0 开始计数
			if used[i] { // 若 已用标记[下标 i]
				continue // 跳过本轮，进入下一次
			}
			used[i] = true                   // 把 true 写入 used[i]
			backtrack(append(path, nums[i])) // backtrack(append(当前路径, 数组[下标 i]))
			used[i] = false                  // 把 false 写入 used[i]
		}
	}
	backtrack([]int{}) // backtrack([]int{})
	return res         // 返回 结果
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
	got := norm2D(permute([]int{1, 2, 3})) // 把 norm2D(permute([]int{1, 2, 3})) 写入 got :
	want := norm2D([][]int{{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}})
	ok := reflect.DeepEqual(got, want) // 把 reflect.DeepEqual(got, want) 写入 ok :
	if !ok {                           // 若 取反 ok
		fmt.Printf("FAIL permute([1,2,3])=%v want %v\n", got, want) // 打印输出
		os.Exit(1)                                                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
