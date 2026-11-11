// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
package main // 引入依赖

import (
	"fmt" // 「fmt」
)

func contains(s []int, v int) bool { // 定义函数/方法 contains
	for _, x := range s { // 同时取 _ 与 x 遍历
		if x == v { // 若 x 等于 值
			return true // 返回 true
		}
	}
	return false // 返回 false
}

func nthSuperUglyNumber(n int, primes []int) int { // 定义函数/方法 nthSuperUglyNumber
	res := []int{1}    // 把 []int{1} 写入 res :
	i := 2             // 把 2 写入 i :
	for len(res) < n { // for 长度(结果) 小于 元素个数 {
		l := 0                   // 把 0 写入 l :
		for j := 0; j < i; j++ { // 让 下标 j 从 0 开始计数
			if i%j == 0 && !contains(primes, j) { // 若 下标 i 对…取模 下标 j 等于 0 且 取反 contains(primes, 下标 j
				break // 跳出循环
			}
			l++ // 左指针 加一
		}
		if l == 0 { // 若 左指针 等于 0
			if contains(primes, i) { // 定义函数/方法 contains
				res = append(res, i) // 把 append(结果, 下标 i) 写入 结果
			}
		} else { // 否则
			res = append(res, i) // 把 append(结果, 下标 i) 写入 结果
		}
		i++ // 下标 i 加一
	}
	return res[n-1] // 返回 结果[元素个数 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n      int   // 元素个数 int
		primes []int // primes []int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{1, nil, 1},
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
