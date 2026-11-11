// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Greatest Slice - 方案3: Divide and Conquer (O(n log n))
func maxSubArrayDC(arr []int) int { // 定义函数/方法 maxSubArrayDC
	var helper func(int, int) (int, int, int, int)   // var helper func(int, int) (int, int, int, int)
	helper = func(lo, hi int) (int, int, int, int) { // 把 func(左边界, 右边界 int) (int, int, int, int) { 写入 helper
		// 返回 (best, prefix, suffix, total)
		if hi-lo == 1 { // 若 右边界 减 左边界 等于 1
			v := arr[lo]      // 把 数组[左边界] 写入 v :
			return v, v, v, v // 返回 值, 值, 值, 值
		}
		mi := (lo + hi) / 2                       // 把 (左边界 加 右边界) 除以 2 写入 mi :
		lBest, lPre, lSuf, lSum := helper(lo, mi) // 把 helper(左边界, mi) 写入 lBest, lPre, lSuf, lSum :
		rBest, rPre, rSuf, rSum := helper(mi, hi) // 把 helper(mi, 右边界) 写入 rBest, rPre, rSuf, rSum :
		crossing := lSuf + rPre                   // 把 lSuf 加 rPre 写入 crossing :
		best := lBest                             // 把 lBest 写入 best :
		if rBest > best {                         // 若 rBest 超过 当前最优
			best = rBest // 把 rBest 写入 当前最优
		}
		if crossing > best { // 若 crossing 超过 当前最优
			best = crossing // 把 crossing 写入 当前最优
		}
		prefix := lPre          // 把 lPre 写入 prefix :
		if lSum+rPre > prefix { // 若 lSum 加 rPre 超过 prefix
			prefix = lSum + rPre // 把 lSum 加 rPre 写入 prefix
		}
		suffix := rSuf          // 把 rSuf 写入 suffix :
		if rSum+lSuf > suffix { // 若 rSum 加 lSuf 超过 suffix
			suffix = rSum + lSuf // 把 rSum 加 lSuf 写入 suffix
		}
		return best, prefix, suffix, lSum + rSum // 返回 当前最优, prefix, suffix, lSum 加 rSum
	}
	if len(arr) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	b, _, _, _ := helper(0, len(arr)) // 把 helper(0, 长度(数组)) 写入 b, _, _, _ :
	return b                          // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{-2, 1, -3, 4, -1, 2, 1}, 6},
		{[]int{-1}, -1},
		{[]int{1}, 1},
		{[]int{-2, -1}, -1},
		{[]int{}, 0},
		{[]int{5, 4, -1, 7, 8}, 23},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxSubArrayDC(c.in); got != c.want { // 若 got : 赋值为 maxSubArrayDC(字符.in); got 不等于 字符.want
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL maxSubArrayDC(%v)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
