// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type Node struct { // 定义类型
	Val   int   // Val int
	Left  *Node // Left 乘 Node
	Right *Node // Right 乘 Node
	Next  *Node // Next 乘 Node
}

func buildNode(vals []interface{}) *Node { // 定义函数/方法 buildNode
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &Node{Val: vals[0].(int)} // 把 按位与 Node{Val: vals[0].(int)} 写入 root :
	q := []*Node{root}                // 把 [] 乘 Node{根节点} 写入 q :
	i := 1                            // 把 1 写入 i :
	for len(q) > 0 && i < len(vals) { // 定义函数/方法 len
		node := q[0]                         // 把 节点[0] 写入 node :
		q = q[1:]                            // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Left = &Node{Val: vals[i].(int)} // 把 按位与 Node{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)              // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                  // 下标 i 加一
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Right = &Node{Val: vals[i].(int)} // 把 按位与 Node{Val: vals[下标 i].(int)} 写入 node.Right
			q = append(q, node.Right)              // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

// 方案2：使用已建立的 next 指针（O(1) 额外空间，逐层串接）
func connect(root *Node) *Node { // 定义函数/方法 connect
	if root == nil { // 若 根节点 等于 nil
		return nil // 返回 nil
	}
	leftmost := root      // 把 根节点 写入 leftmost :
	for leftmost != nil { // 把 nil { 写入 for leftmost !
		cur := leftmost           // 把 leftmost 写入 cur :
		var nextStart, prev *Node // var nextStart, 前一个 乘 Node
		for cur != nil {          // 把 nil { 写入 for cur !
			for _, ch := range []*Node{cur.Left, cur.Right} { // 同时取 _ 与 字符 遍历
				if ch != nil { // 若 字符 不等于 nil
					if prev == nil { // 若 前一个 等于 nil
						nextStart = ch // 把 字符 写入 nextStart
					} else { // 否则
						prev.Next = ch // 把 字符 写入 prev.Next
					}
					prev = ch // 把 字符 写入 前一个
				}
			}
			cur = cur.Next // 把 当前值.Next 写入 当前值
		}
		leftmost = nextStart // 把 nextStart 写入 leftmost
	}
	return root // 返回 根节点
}

func collectLevels(root *Node) [][]int { // 定义函数/方法 collectLevels
	var res [][]int                          // var 结果 [][]int
	for leftmost := root; leftmost != nil; { // 把 根节点; leftmost 不等于 nil; { 写入 for leftmost :
		var level []int                                   // var level []int
		for cur := leftmost; cur != nil; cur = cur.Next { // 把 leftmost; 当前值 不等于 nil; 当前值 赋值为 当前值.Next { 写入 for cur :
			level = append(level, cur.Val) // 把 append(level, 当前值.Val) 写入 level
		}
		res = append(res, level) // 把 append(结果, level) 写入 结果
		leftmost = leftmost.Left // 把 leftmost.Left 写入 leftmost
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	root := buildNode([]interface{}{1, 2, 3, 4, 5, nil, 7}) // 把 buildNode([]interface{}{1, 2, 3, 4, 5, nil, 7}) 写入 root :
	connect(root)                                           // connect(根节点)
	got := collectLevels(root)                              // 把 collectLevels(根节点) 写入 got :
	want := [][]int{{1}, {2, 3}, {4, 5, 7}}                 // 把 [][]int{{1}, {2, 3}, {4, 5, 7}} 写入 want :
	if !reflect.DeepEqual(got, want) {                      // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	// 空树与单枝边界
	if connect(nil) != nil { // 若 connect(nil) 不等于 nil
		fmt.Println("FAIL connect(nil) != nil") // 打印输出
		os.Exit(1)                              // os.Exit(1)
	}
	single := &Node{Val: 9} // 把 按位与 Node{Val: 9} 写入 single :
	connect(single)         // connect(single)
	if len(collectLevels(single)) != 1 || collectLevels(single)[0][0] != 9 {
		fmt.Println("FAIL single") // 打印输出
		os.Exit(1)                 // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
