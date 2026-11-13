// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func grayCode(n int) []int { // 定义函数/方法 grayCode
	result := []int{0, 1}    // 把 []int{0, 1} 写入 result :
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		for j := len(result) - 1; j >= 0; j-- { // 把 长度(结果) 减 1; 下标 j 不低于 0; 下标 j 减一 { 写入 for j :
			result = append(result, (1<<i)+result[j]) // 把 append(结果, (1 小于 小于 下标 i) 加 结果[下标 j]) 写入 结果
		}
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n    int   // 元素个数 int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{1, []int{0, 1}},
		{2, []int{0, 1, 3, 2}},
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
