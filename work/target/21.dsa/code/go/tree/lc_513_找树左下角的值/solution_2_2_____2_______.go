// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145368911
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

func findBottomLeftValue(root *TreeNode) int { // 定义函数/方法 findBottomLeftValue
	ret := 0                   // 把 0 写入 ret :
	queue := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 queue :
	for len(queue) > 0 {       // for 长度(队列) 超过 0 {
		p := queue[0]       // 把 队列[0] 写入 p :
		queue = queue[1:]   // 把 队列[1:] 写入 队列
		if p.Right != nil { // 若 节点.Right 不等于 nil
			queue = append(queue, p.Right) // 把 append(队列, 节点.Right) 写入 队列
		}
		if p.Left != nil { // 若 节点.Left 不等于 nil
			queue = append(queue, p.Left) // 把 append(队列, 节点.Left) 写入 队列
		}
		ret = p.Val // 把 节点.Val 写入 ret
	}
	return ret // 返回 ret
}

func buildTree(vals []int) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == -1 { // 若 长度(vals) 等于 0 或 vals[0] 等于 减 1
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0]} // 把 按位与 TreeNode{Val: vals[0]} 写入 root :
	q := []*TreeNode{root}          // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                          // 把 1 写入 i :
	for i < len(vals) {             // for 下标 i 小于 长度(vals) {
		node := q[0]                        // 把 节点[0] 写入 node :
		q = q[1:]                           // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Left = &TreeNode{Val: vals[i]} // 把 按位与 TreeNode{Val: vals[下标 i]} 写入 node.Left
			q = append(q, node.Left)            // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                 // 下标 i 加一
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Right = &TreeNode{Val: vals[i]} // 把 按位与 TreeNode{Val: vals[下标 i]} 写入 node.Right
			q = append(q, node.Right)            // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func main() { // 程序入口：跑内嵌自测用例
	root := buildTree([]int{1, 2, 3, 4, 5, -1, 6}) // 把 buildTree([]int{1, 2, 3, 4, 5, 减 1, 6}) 写入 root :
	if findBottomLeftValue(root) != 4 {            // 若 findBottomLeftValue(根节点) 不等于 4
		fmt.Println("FAIL want=4") // 打印输出
		os.Exit(1)                 // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
