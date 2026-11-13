// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type Node struct { // 定义类型
	Val   int   // Val int
	Left  *Node // Left 乘 Node
	Right *Node // Right 乘 Node
	Next  *Node // Next 乘 Node
}

func connect(root *Node) *Node { // 定义函数/方法 connect
	if root == nil { // 若 根节点 等于 nil
		return root // 返回 根节点
	}
	queue := []*Node{root} // 把 [] 乘 Node{根节点} 写入 queue :
	for len(queue) > 0 {   // for 长度(队列) 超过 0 {
		size := len(queue)          // 把 长度(队列) 写入 size :
		var prev *Node              // var 前一个 乘 Node
		for i := 0; i < size; i++ { // 让 下标 i 从 0 开始计数
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

func collectLevels(root *Node) [][]int { // 定义函数/方法 collectLevels
	var levels [][]int // var levels [][]int
	if root == nil {   // 若 根节点 等于 nil
		return levels // 返回 levels
	}
	head := root      // 把 根节点 写入 head :
	for head != nil { // 把 nil { 写入 for head !
		var row []int    // var row []int
		cur := head      // 把 头节点 写入 cur :
		for cur != nil { // 把 nil { 写入 for cur !
			row = append(row, cur.Val) // 把 append(row, 当前值.Val) 写入 row
			cur = cur.Next             // 把 当前值.Next 写入 当前值
		}
		levels = append(levels, row) // 把 append(levels, row) 写入 levels
		nxt := head                  // 把 头节点 写入 nxt :
		nextHead := (*Node)(nil)     // 把 ( 乘 Node)(nil) 写入 nextHead :
		for nxt != nil {             // 把 nil { 写入 for nxt !
			if nxt.Left != nil { // 若 nxt.Left 不等于 nil
				nextHead = nxt.Left // 把 nxt.Left 写入 nextHead
				break               // 跳出循环
			}
			if nxt.Right != nil { // 若 nxt.Right 不等于 nil
				nextHead = nxt.Right // 把 nxt.Right 写入 nextHead
				break                // 跳出循环
			}
			nxt = nxt.Next // 把 nxt.Next 写入 nxt
		}
		head = nextHead // 把 nextHead 写入 头节点
	}
	return levels // 返回 levels
}

func buildNode(vals []int) *Node { // 定义函数/方法 buildNode
	if len(vals) == 0 || vals[0] == -1 { // 若 长度(vals) 等于 0 或 vals[0] 等于 减 1
		return nil // 返回 nil
	}
	root := &Node{Val: vals[0]} // 把 按位与 Node{Val: vals[0]} 写入 root :
	q := []*Node{root}          // 把 [] 乘 Node{根节点} 写入 q :
	i := 1                      // 把 1 写入 i :
	for i < len(vals) {         // for 下标 i 小于 长度(vals) {
		node := q[0]                        // 把 节点[0] 写入 node :
		q = q[1:]                           // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Left = &Node{Val: vals[i]} // 把 按位与 Node{Val: vals[下标 i]} 写入 node.Left
			q = append(q, node.Left)        // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                 // 下标 i 加一
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Right = &Node{Val: vals[i]} // 把 按位与 Node{Val: vals[下标 i]} 写入 node.Right
			q = append(q, node.Right)        // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func main() { // 程序入口：跑内嵌自测用例
	root := buildNode([]int{1, 2, 3, 4, 5, -1, 7}) // 把 buildNode([]int{1, 2, 3, 4, 5, 减 1, 7}) 写入 root :
	connect(root)                                  // connect(根节点)
	got := collectLevels(root)                     // 把 collectLevels(根节点) 写入 got :
	want := [][]int{{1}, {2, 3}, {4, 5, 7}}        // 把 [][]int{{1}, {2, 3}, {4, 5, 7}} 写入 want :
	if !reflect.DeepEqual(got, want) {             // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
