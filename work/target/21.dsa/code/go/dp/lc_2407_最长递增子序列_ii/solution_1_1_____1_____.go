// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144827578
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

func max2(a, b int) int { // 定义函数/方法 max2
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

// bisectLeft 在升序 arr 中查找第一个 >= target 的下标。
func bisectLeft(arr []int, target int) int { // 定义函数/方法 bisectLeft
	lo, hi := 0, len(arr) // 把 0, 长度(数组) 写入 lo, hi :
	for lo < hi {         // for 左边界 小于 右边界 {
		mid := (lo + hi) / 2   // 把 (左边界 加 右边界) 除以 2 写入 mid :
		if arr[mid] < target { // 若 数组[中点] 小于 目标值
			lo = mid + 1 // 把 中点 加 1 写入 左边界
		} else { // 否则
			hi = mid // 把 中点 写入 右边界
		}
	}
	return lo // 返回 左边界
}

// lengthOfLIS 是 Python 参考 solution_1 的忠实翻译（离散化 + 线段树区间最大值查询）。
func lengthOfLIS(nums []int, k int) int { // 定义函数/方法 lengthOfLIS
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	seen := map[int]bool{}   // 把 映射表[int]bool{} 写入 seen :
	vals := []int{}          // 把 []int{} 写入 vals :
	for _, x := range nums { // 同时取 _ 与 x 遍历
		if !seen[x] { // 若 取反 已见集合[x]
			seen[x] = true         // 把 true 写入 seen[x]
			vals = append(vals, x) // 把 append(vals, x) 写入 vals
		}
	}
	sort.Ints(vals)           // sort.Ints(vals)
	comp := make(map[int]int) // 把 make(映射表[int]int) 写入 comp :
	for i, v := range vals {  // 同时取 下标 i 与 值 遍历
		comp[v] = i // 把 下标 i 写入 comp[v]
	}
	m := len(vals) // 把 长度(vals) 写入 m :
	size := 1      // 把 1 写入 size :
	for size < m { // for 大小 小于 映射表 {
		size <<= 1 // 把 1 写入 size <<
	}
	tree := make([]int, 2*size) // 把 make([]int, 2 乘 大小) 写入 tree :

	update := func(pos, val int) { // 把 func(pos, 值 int) { 写入 update :
		pos += size          // pos累加 大小
		if val > tree[pos] { // 若 值 超过 tree[pos]
			tree[pos] = val // 把 值 写入 tree[pos]
		}
		pos >>= 1     // 把 1 写入 pos >>
		for pos > 0 { // for pos 超过 0 {
			tree[pos] = max2(tree[2*pos], tree[2*pos+1]) // 把 max2(tree[2 乘 pos], tree[2 乘 pos 加 1]) 写入 tree[pos]
			pos >>= 1                                    // 把 1 写入 pos >>
		}
	}
	query := func(l, r int) int { // 把 func(左指针, 右指针 int) int { 写入 query :
		l += size    // 左指针累加 大小
		r += size    // 右指针累加 大小
		res := 0     // 把 0 写入 res :
		for l <= r { // 把 右指针 { 写入 for l <
			if l&1 == 1 { // 若 左指针 按位与 1 等于 1
				if tree[l] > res { // 若 tree[左指针] 超过 结果
					res = tree[l] // 把 tree[左指针] 写入 结果
				}
				l++ // 左指针 加一
			}
			if r&1 == 0 { // 若 右指针 按位与 1 等于 0
				if tree[r] > res { // 若 tree[右指针] 超过 结果
					res = tree[r] // 把 tree[右指针] 写入 结果
				}
				r-- // 右指针 减一
			}
			l >>= 1 // 把 1 写入 l >>
			r >>= 1 // 把 1 写入 r >>
		}
		return res // 返回 结果
	}

	ans := 0                 // 把 0 写入 ans :
	for _, x := range nums { // 同时取 _ 与 x 遍历
		ci := comp[x]               // 把 comp[x] 写入 ci :
		lo := bisectLeft(vals, x-k) // 把 bisectLeft(vals, x 减 下标 k) 写入 lo :
		best := 0                   // 把 0 写入 best :
		if lo <= ci-1 {             // 若 左边界 不超过 ci 减 1
			best = query(lo, ci-1) // 把 query(左边界, ci 减 1) 写入 当前最优
		}
		cur := best + 1 // 把 当前最优 加 1 写入 cur :
		if cur > ans {  // 若 当前值 超过 答案
			ans = cur // 把 当前值 写入 答案
		}
		update(ci, cur) // update(ci, 当前值)
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		k    int   // 下标 k int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{4, 2, 1, 4, 3, 4, 5, 8, 15}, 3, 5},
		{[]int{3, 2, 1}, 2, 1},
		{[]int{5, 4, 3, 2, 1}, 1, 1},
		{[]int{1, 2, 3, 4, 5}, 2, 5},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := lengthOfLIS(c.nums, c.k); got != c.want { // 若 got : 赋值为 lengthOfLIS(字符.数组, 字符.下标 k); got 不等于 字符.want
			fmt.Printf("FAIL %v %d got=%d want=%d\n", c.nums, c.k, got, c.want) // 打印输出
			os.Exit(1)                                                          // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
