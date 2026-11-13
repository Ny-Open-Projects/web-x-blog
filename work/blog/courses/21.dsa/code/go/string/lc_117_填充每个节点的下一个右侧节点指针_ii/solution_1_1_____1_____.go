// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type Node struct { // 定义类型
	Val   int   // Val int
	Left  *Node // Left 乘 Node
	Right *Node // Right 乘 Node
	Next  *Node // Next 乘 Node
}

func connect(root *Node) *Node { // 定义函数/方法 connect
	if root == nil { // 若 根节点 等于 nil
		return nil // 返回 nil
	}
	queue := []*Node{root} // 把 [] 乘 Node{根节点} 写入 queue :
	for len(queue) > 0 {   // for 长度(队列) 超过 0 {
		n := len(queue)          // 把 长度(队列) 写入 n :
		var prev *Node           // var 前一个 乘 Node
		for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
			node := queue[0]  // 把 队列[0] 写入 node :
			queue = queue[1:] // 把 队列[1:] 写入 队列
			if prev != nil {  // 若 前一个 不等于 nil
				prev.Next = node // 把 节点 写入 prev.Next
			}
			prev = node           // 把 节点 写入 前一个
			if node.Left != nil { // 若 节点.Left 不等于 nil
				queue = append(queue, node.Left) // 把 append(队列, 节点.Left) 写入 队列
			}
			if node.Right != nil { // 若 节点.Right 不等于 nil
				queue = append(queue, node.Right) // 把 append(队列, 节点.Right) 写入 队列
			}
		}
	}
	return root // 返回 根节点
}

func main() { // 程序入口：跑内嵌自测用例
	root := &Node{Val: 1}                                 // 把 按位与 Node{Val: 1} 写入 root :
	root.Left = &Node{Val: 2}                             // 把 按位与 Node{Val: 2} 写入 root.Left
	root.Right = &Node{Val: 3}                            // 把 按位与 Node{Val: 3} 写入 root.Right
	root.Left.Left = &Node{Val: 4}                        // 把 按位与 Node{Val: 4} 写入 root.Left.Left
	root.Left.Right = &Node{Val: 5}                       // 把 按位与 Node{Val: 5} 写入 root.Left.Right
	root.Right.Right = &Node{Val: 7}                      // 把 按位与 Node{Val: 7} 写入 root.Right.Right
	connect(root)                                         // connect(根节点)
	ok := true                                            // 把 true 写入 ok :
	if root.Left.Next == nil || root.Left.Next.Val != 3 { // 若 根节点.Left.Next 等于 nil 或 根节点.Left.Next.Val 不等于 3
		ok = false                      // 把 false 写入 ok
		fmt.Println("FAIL level1 next") // 打印输出
	}
	if root.Left.Left.Next == nil || root.Left.Left.Next.Val != 5 { // 若 根节点.Left.Left.Next 等于 nil 或 根节点.Left.Left.Next.Val 不等于 5
		ok = false                   // 把 false 写入 ok
		fmt.Println("FAIL level2 a") // 打印输出
	}
	if root.Left.Left.Next.Next == nil || root.Left.Left.Next.Next.Val != 7 {
		ok = false                   // 把 false 写入 ok
		fmt.Println("FAIL level2 b") // 打印输出
	}
	if connect(nil) != nil { // 若 connect(nil) 不等于 nil
		ok = false              // 把 false 写入 ok
		fmt.Println("FAIL nil") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
