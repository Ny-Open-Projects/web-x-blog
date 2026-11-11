// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233874
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
	"sort"
) // 引入依赖

func permuteUnique(nums []int) [][]int { // 定义函数/方法 permuteUnique
	sort.Ints(nums)                // sort.Ints(数组)
	n := len(nums)                 // 把 长度(数组) 写入 n :
	used := make([]bool, n)        // 把 make([]bool, 元素个数) 写入 used :
	ans := [][]int{}               // 把 [][]int{} 写入 ans :
	var backtrack func(path []int) // var backtrack func(当前路径 []int)
	backtrack = func(path []int) { // 把 func(当前路径 []int) { 写入 backtrack
		if len(path) == n { // 若 长度(当前路径) 等于 元素个数
			ans = append(ans, append([]int{}, path...)) // 把 append(答案, append([]int{}, 当前路径...)) 写入 答案
			return                                      // return
		}
		for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
			if used[i] { // 若 已用标记[下标 i]
				continue // 跳过本轮，进入下一次
			}
			if i > 0 && nums[i] == nums[i-1] && !used[i-1] { // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1] 且 取反 已用标记[下标 i 减 1]
				continue // 跳过本轮，进入下一次
			}
			used[i] = true                 // 把 true 写入 used[i]
			np := append([]int{}, path...) // 把 append([]int{}, 当前路径...) 写入 np :
			np = append(np, nums[i])       // 把 append(np, 数组[下标 i]) 写入 np
			backtrack(np)                  // backtrack(np)
			used[i] = false                // 把 false 写入 used[i]
		}
	}
	backtrack([]int{}) // backtrack([]int{})
	return ans         // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int   // in []int
		want [][]int // want [][]int
	}{ // }{
		{[]int{1, 1, 2}, [][]int{{1, 1, 2}, {1, 2, 1}, {2, 1, 1}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := permuteUnique(c.in); !reflect.DeepEqual(g, c.want) {
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
