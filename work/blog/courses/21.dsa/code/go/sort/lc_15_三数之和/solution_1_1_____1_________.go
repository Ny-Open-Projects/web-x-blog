// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
	"sort"
) // 引入依赖

func threeSum(nums []int) [][]int { // 定义函数/方法 threeSum
	sort.Ints(nums)                      // sort.Ints(数组)
	ans := [][]int{}                     // 把 [][]int{} 写入 ans :
	n := len(nums)                       // 把 长度(数组) 写入 n :
	for first := 0; first < n; first++ { // 让 first 从 0 开始计数
		if first > 0 && nums[first] == nums[first-1] { // 若 first 超过 0 且 数组[first] 等于 数组[first 减 1]
			continue // 跳过本轮，进入下一次
		}
		third := n - 1                                  // 把 元素个数 减 1 写入 third :
		target := -nums[first]                          // 把 减 数组[first] 写入 target :
		for second := first + 1; second < n; second++ { // 把 first 加 1; second 小于 元素个数; second 加一 { 写入 for second :
			if second > first+1 && nums[second] == nums[second-1] { // 若 second 超过 first 加 1 且 数组[second] 等于 数组[second 减 1]
				continue // 跳过本轮，进入下一次
			}
			for second < third && nums[second]+nums[third] > target { // for second 小于 third 且 数组[third] 超过 目标值 {
				third-- // third 减一
			}
			if second == third { // 若 second 等于 third
				break // 跳出循环
			}
			if nums[second]+nums[third] == target { // 若 数组[second] 加 数组[third] 等于 目标值
				ans = append(ans, []int{nums[first], nums[second], nums[third]}) // 把 append(答案, []int{数组[first], 数组[second], 数组[third]}) 写入 答案
			}
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int   // in []int
		want [][]int // want [][]int
	}{ // }{
		{[]int{-1, 0, 1, 2, -1, -4}, [][]int{{-1, -1, 2}, {-1, 0, 1}}},
		{[]int{0, 0, 0}, [][]int{{0, 0, 0}}},
		{[]int{1, 2, 3}, [][]int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := threeSum(c.in); !reflect.DeepEqual(g, c.want) { // 若 g : 赋值为 threeSum(字符.in); 取反 reflect.DeepEqual(g, 字符.want
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
