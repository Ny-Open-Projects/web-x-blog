// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func getValue(data map[string]interface{}, path []string) int { // 定义函数/方法 getValue
	node := interface{}(data)  // 把 interface{}(data) 写入 node :
	for _, key := range path { // 同时取 _ 与 key 遍历
		m, ok := node.(map[string]interface{}) // 把 节点.(映射表[string]interface{}) 写入 m, ok :
		if !ok {                               // 若 取反 ok
			return -1 // 返回 减 1
		}
		v, ok := m[key] // 把 映射表[key] 写入 v, ok :
		if !ok {        // 若 取反 ok
			return -1 // 返回 减 1
		}
		node = v // 把 值 写入 节点
	}
	iv, ok := node.(int) // 把 节点.(int) 写入 iv, ok :
	if !ok {             // 若 取反 ok
		return -1 // 返回 减 1
	}
	return iv // 返回 iv
}

func main() { // 程序入口：跑内嵌自测用例
	data := map[string]interface{}{ // 把 映射表[string]interface{}{ 写入 data :
		"a": map[string]interface{}{ // 「数组」: 映射表[string]interface{}{
			"b": map[string]interface{}{ // 「b」: 映射表[string]interface{}{
				"c": 1,
			},
		},
		"d": map[string]interface{}{ // 「d」: 映射表[string]interface{}{
			"e": 2,
		},
	}
	cases := []struct { // 把 []struct { 写入 cases :
		path []string // 当前路径 []string
		want int      // want int
	}{ // }{
		{[]string{"a", "b", "c"}, 1},
		{[]string{"d", "e"}, 2},
		{[]string{"a", "x"}, -1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := getValue(data, c.path) // 把 getValue(data, 字符.当前路径) 写入 got :
		if got != c.want {            // 若 got 不等于 字符.want
			ok = false                                                  // 把 false 写入 ok
			fmt.Printf("FAIL %v got %d want %d\n", c.path, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
