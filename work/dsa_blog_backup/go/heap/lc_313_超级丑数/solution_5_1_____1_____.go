// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
package main // 引入依赖

import (
	"fmt" // 「fmt」
)

func nthSuperUglyNumber(n int, primes []int) int { // 定义函数/方法 nthSuperUglyNumber
	dp := make([]int, n+1)     // 把 make([]int, 元素个数 加 1) 写入 dp :
	m := len(primes)           // 把 长度(primes) 写入 m :
	pointers := make([]int, m) // 把 make([]int, 映射表) 写入 pointers :
	nums := make([]int, m)     // 把 make([]int, 映射表) 写入 nums :
	for j := 0; j < m; j++ {   // 让 下标 j 从 0 开始计数
		nums[j] = 1 // 把 1 写入 nums[j]
	}
	for i := 1; i <= n; i++ { // 让 下标 i 从 1 开始计数
		minNum := nums[0]        // 把 数组[0] 写入 minNum :
		for j := 1; j < m; j++ { // 让 下标 j 从 1 开始计数
			if nums[j] < minNum { // 若 数组[下标 j] 小于 minNum
				minNum = nums[j] // 把 数组[下标 j] 写入 minNum
			}
		}
		dp[i] = minNum           // 把 minNum 写入 dp[i]
		for j := 0; j < m; j++ { // 让 下标 j 从 0 开始计数
			if nums[j] == minNum { // 若 数组[下标 j] 等于 minNum
				pointers[j]++                         // pointers[下标 j] 加一
				nums[j] = dp[pointers[j]] * primes[j] // 把 DP 表[pointers[下标 j]] 乘 primes[下标 j] 写入 nums[j]
			}
		}
	}
	return dp[n] // 返回 DP 表[元素个数]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n      int   // 元素个数 int
		primes []int // primes []int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{12, []int{2, 7, 13, 19}, 32},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := nthSuperUglyNumber(c.n, c.primes) // 把 nthSuperUglyNumber(字符.元素个数, 字符.primes) 写入 got :
		if got != c.want {                       // 若 got 不等于 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%d want=%d\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
