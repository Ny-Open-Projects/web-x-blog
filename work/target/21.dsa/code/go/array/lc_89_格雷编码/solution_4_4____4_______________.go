// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func grayCode(n int) []int { // 定义函数/方法 grayCode
	ret := []int{}                  // 把 []int{} 写入 ret :
	for i := 0; i < (1 << n); i++ { // 让 下标 i 从 0 开始计数
		ret = append(ret, (i>>1)^i) // 把 append(ret, (下标 i 超过 超过 1) 按位异或 下标 i) 写入 ret
	}
	return ret // 返回 ret
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n    int   // 元素个数 int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{1, []int{0, 1}},
		{2, []int{0, 1, 3, 2}},
		{3, []int{0, 1, 3, 2, 6, 7, 5, 4}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := grayCode(c.n); !reflect.DeepEqual(got, c.want) {
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL grayCode(%v)=%v want %v\n", c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
