// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345965
package main // 引入依赖

import (
	"fmt"       // 「fmt」
	"math/rand" // 「math 除以 rand」
	"os"        // 「os」
	"reflect"   // 「reflect」
	"sort"      // 「sort」
)

type Solution struct { // 定义类型
	nums     []int // 数组 []int
	original []int // original []int
}

func Constructor(nums []int) *Solution { // 定义函数/方法 Constructor
	s := &Solution{ // 把 按位与 Solution{ 写入 s :
		nums:     make([]int, len(nums)),
		original: make([]int, len(nums)),
	}
	copy(s.nums, nums)     // copy(字符串.数组, 数组)
	copy(s.original, nums) // copy(字符串.original, 数组)
	return s               // 返回 字符串
}

func (this *Solution) Reset() []int { // 定义函数/方法 Reset
	copy(this.nums, this.original) // copy(this.数组, this.original)
	return this.nums               // 返回 this.数组
}

func (this *Solution) Shuffle() []int { // 定义函数/方法 Shuffle
	shuffled := make([]int, len(this.nums))  // 把 make([]int, 长度(this.数组)) 写入 shuffled :
	copy(shuffled, this.nums)                // copy(shuffled, this.数组)
	for i := len(shuffled) - 1; i > 0; i-- { // 把 长度(shuffled) 减 1; 下标 i 超过 0; 下标 i 减一 { 写入 for i :
		j := rand.Intn(i + 1)                               // 把 rand.Intn(下标 i 加 1) 写入 j :
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i] // 把 shuffled[下标 j], shuffled[下标 i] 写入 shuffled[i], shuffled[j]
	}
	this.nums = shuffled // 把 shuffled 写入 数组
	return this.nums     // 返回 this.数组
}

func isPermutation(a, b []int) bool { // 定义判定函数 isPermutation
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	sa := append([]int{}, a...)      // 把 append([]int{}, 数组...) 写入 sa :
	sb := append([]int{}, b...)      // 把 append([]int{}, b...) 写入 sb :
	sort.Ints(sa)                    // sort.Ints(sa)
	sort.Ints(sb)                    // sort.Ints(sb)
	return reflect.DeepEqual(sa, sb) // 返回 reflect.DeepEqual(sa, sb)
}

func main() { // 程序入口：跑内嵌自测用例
	s := Constructor([]int{1, 2, 3})        // 把 Constructor([]int{1, 2, 3}) 写入 s :
	ok := true                              // 把 true 写入 ok :
	sh := s.Shuffle()                       // 把 字符串.Shuffle() 写入 sh :
	if !isPermutation(sh, []int{1, 2, 3}) { // 若 取反 isPermutation(sh, []int{1, 2, 3}
		ok = false                                                         // 把 false 写入 ok
		fmt.Printf("FAIL Shuffle()=%v not a permutation of [1 2 3]\n", sh) // 打印输出
	}
	r := s.Reset()                             // 把 字符串.Reset() 写入 r :
	if !reflect.DeepEqual(r, []int{1, 2, 3}) { // 若 取反 reflect.DeepEqual(右指针, []int{1, 2, 3}
		ok = false                                      // 把 false 写入 ok
		fmt.Printf("FAIL Reset()=%v want [1 2 3]\n", r) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
