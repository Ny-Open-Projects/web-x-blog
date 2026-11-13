// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func shellSort(lst []int) []int { // 定义函数/方法 shellSort
	length := len(lst) // 把 长度(lst) 写入 length :
	gap := length / 2  // 把 长度 除以 2 写入 gap :
	for gap > 0 {      // for gap 超过 0 {
		for i := gap; i < length; i++ { // 把 gap; 下标 i 小于 长度; 下标 i 加一 { 写入 for i :
			tmp := lst[i]                        // 把 lst[下标 i] 写入 tmp :
			p := i                               // 把 下标 i 写入 p :
			for p-gap >= 0 && lst[p-gap] > tmp { // 把 0 且 lst[节点 减 gap] 超过 临时变量 { 写入 for p-gap >
				lst[p] = lst[p-gap] // 把 lst[节点 减 gap] 写入 lst[p]
				p -= gap            // 节点累减 gap
			}
			lst[p] = tmp // 把 临时变量 写入 lst[p]
		}
		gap /= 2 // 把 2 写入 gap /
	}
	return lst // 返回 lst
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{9, 12, 1, 3, -1, 22, 22, 31, 1, 0}, []int{-1, 0, 1, 1, 3, 9, 12, 22, 22, 31}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := append([]int{}, c.in...)                             // 把 append([]int{}, 字符.in...) 写入 in :
		if got := shellSort(in); !reflect.DeepEqual(got, c.want) { // 若 got : 赋值为 shellSort(in); 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL shellSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
