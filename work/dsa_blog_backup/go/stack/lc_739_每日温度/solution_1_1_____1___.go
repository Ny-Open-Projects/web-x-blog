// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354164
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func dailyTemperatures(temperatures []int) []int { // 定义函数/方法 dailyTemperatures
	length := len(temperatures)    // 把 长度(temperatures) 写入 length :
	ans := make([]int, length)     // 把 make([]int, 长度) 写入 ans :
	nextWarmer := make([]int, 101) // 把 make([]int, 101) 写入 nextWarmer :
	for i := range nextWarmer {    // 把 range nextWarmer { 写入 for i :
		nextWarmer[i] = 1 << 30 // 把 1 小于 小于 30 写入 nextWarmer[i]
	}
	for i := length - 1; i >= 0; i-- { // 把 长度 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		warmerIndex := 1 << 30                   // 把 1 小于 小于 30 写入 warmerIndex :
		t := temperatures[i]                     // 把 temperatures[下标 i] 写入 t :
		for temp := t + 1; temp <= 100; temp++ { // 把 另一字符串 加 1; 临时变量 不超过 100; 临时变量 加一 { 写入 for temp :
			if nextWarmer[temp] < warmerIndex { // 若 nextWarmer[临时变量] 小于 warmerIndex
				warmerIndex = nextWarmer[temp] // 把 nextWarmer[临时变量] 写入 warmerIndex
			}
		}
		if warmerIndex < 1<<30 { // 若 warmerIndex 小于 1 小于 小于 30
			ans[i] = warmerIndex - i // 把 warmerIndex 减 下标 i 写入 ans[i]
		}
		nextWarmer[t] = i // 把 下标 i 写入 nextWarmer[t]
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{73, 74, 75, 71, 69, 72, 76, 73}, []int{1, 1, 4, 2, 1, 1, 0, 0}},
		{[]int{30, 40, 50, 60}, []int{1, 1, 1, 0}},
		{[]int{30, 60, 90}, []int{1, 1, 0}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := dailyTemperatures(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL dailyTemperatures(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
