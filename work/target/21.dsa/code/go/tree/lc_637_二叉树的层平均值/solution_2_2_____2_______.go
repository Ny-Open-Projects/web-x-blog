// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091296
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func averageOfLevels(root *TreeNode) []float64 { // 定义函数/方法 averageOfLevels
	result := []float64{}      // 把 []float64{} 写入 result :
	level := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 level :
	for len(level) > 0 {       // for 长度(level) 超过 0 {
		total := 0                   // 把 0 写入 total :
		nxt := []*TreeNode{}         // 把 [] 乘 TreeNode{} 写入 nxt :
		for _, node := range level { // 同时取 _ 与 节点 遍历
			total += node.Val     // 总和累加 节点.Val
			if node.Left != nil { // 若 节点.Left 不等于 nil
				nxt = append(nxt, node.Left) // 把 append(nxt, 节点.Left) 写入 nxt
			}
			if node.Right != nil { // 若 节点.Right 不等于 nil
				nxt = append(nxt, node.Right) // 把 append(nxt, 节点.Right) 写入 nxt
			}
		}
		result = append(result, float64(total)/float64(len(level))) // 把 append(结果, float64(总和) 除以 float64(长度(level))) 写入 结果
		level = nxt                                                 // 把 nxt 写入 level
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	root := &TreeNode{Val: 3}            // 把 按位与 TreeNode{Val: 3} 写入 root :
	root.Left = &TreeNode{Val: 9}        // 把 按位与 TreeNode{Val: 9} 写入 root.Left
	root.Right = &TreeNode{Val: 20}      // 把 按位与 TreeNode{Val: 20} 写入 root.Right
	root.Right.Left = &TreeNode{Val: 15} // 把 按位与 TreeNode{Val: 15} 写入 root.Right.Left
	root.Right.Right = &TreeNode{Val: 7} // 把 按位与 TreeNode{Val: 7} 写入 root.Right.Right
	got := averageOfLevels(root)         // 把 averageOfLevels(根节点) 写入 got :
	want := []float64{3, 14.5, 11}       // 把 []float64{3, 14.5, 11} 写入 want :
	ok := len(got) == len(want)          // 把 长度(got) 等于 长度(want) 写入 ok :
	for i := range want {                // 把 range want { 写入 for i :
		if i >= len(got) || (got[i]-want[i]) > 1e-9 || (want[i]-got[i]) > 1e-9 {
			ok = false // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
