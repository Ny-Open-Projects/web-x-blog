// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239508
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func combinationSum(candidates []int, target int) [][]int { // 定义函数/方法 combinationSum
	sort.Ints(candidates)                                // sort.Ints(候选数组)
	result := [][]int{}                                  // 把 [][]int{} 写入 result :
	var backtrack func(start, remaining int, path []int) // var backtrack func(起点, remaining int, 当前路径 []int)
	backtrack = func(start, remaining int, path []int) { // 把 func(起点, remaining int, 当前路径 []int) { 写入 backtrack
		if remaining == 0 { // 若 remaining 等于 0
			result = append(result, append([]int{}, path...)) // 把 append(结果, append([]int{}, 当前路径...)) 写入 结果
			return                                            // return
		}
		for i := start; i < len(candidates); i++ { // 把 起点; 下标 i 小于 长度(候选数组); 下标 i 加一 { 写入 for i :
			if candidates[i] > remaining { // 若 候选数组[下标 i] 超过 remaining
				break // 跳出循环
			}
			backtrack(i, remaining-candidates[i], append(path, candidates[i]))
		}
	}
	backtrack(0, target, []int{}) // backtrack(0, 目标值, []int{})
	return result                 // 返回 结果
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
		cands  []int   // cands []int
		target int     // 目标值 int
		want   [][]int // want [][]int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 3, 6, 7}, 7, [][]int{{2, 2, 3}, {7}}},
		{[]int{2, 3, 5}, 8, [][]int{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := norm2D(combinationSum(c.cands, c.target)) // 把 norm2D(combinationSum(字符.cands, 字符.目标值)) 写入 got :
		want := norm2D(c.want)                           // 把 norm2D(字符.want) 写入 want :
		if !reflect.DeepEqual(got, want) {               // 若 取反 reflect.DeepEqual(got, want
			ok = false                                                                          // 把 false 写入 ok
			fmt.Printf("FAIL combinationSum(%v,%v)=%v want %v\n", c.cands, c.target, got, want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
