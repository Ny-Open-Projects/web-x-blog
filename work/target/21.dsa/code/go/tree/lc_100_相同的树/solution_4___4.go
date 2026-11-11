// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func buildTree(vals []interface{}) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0].(int)} // 把 按位与 TreeNode{Val: vals[0].(int)} 写入 root :
	q := []*TreeNode{root}                // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                                // 把 1 写入 i :
	for len(q) > 0 && i < len(vals) {     // 定义函数/方法 len
		node := q[0]                         // 把 节点[0] 写入 node :
		q = q[1:]                            // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)                  // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                  // 下标 i 加一
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Right = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Right
			q = append(q, node.Right)                  // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func isSameTree(p, q *TreeNode) bool { // 定义判定函数 isSameTree
	if p == nil && q == nil { // 若 节点 等于 nil 且 节点 等于 nil
		return true // 返回 true
	}
	if p == nil || q == nil { // 若 节点 等于 nil 或 节点 等于 nil
		return false // 返回 false
	}
	if p.Val != q.Val { // 若 节点.Val 不等于 节点.Val
		return false // 返回 false
	}
	queue1 := []*TreeNode{p}                 // 把 [] 乘 TreeNode{节点} 写入 queue1 :
	queue2 := []*TreeNode{q}                 // 把 [] 乘 TreeNode{节点} 写入 queue2 :
	for len(queue1) > 0 && len(queue2) > 0 { // for 长度(queue1) 超过 0 且 长度(queue2) 超过 0 {
		pTop := queue1[0]         // 把 queue1[0] 写入 pTop :
		queue1 = queue1[1:]       // 把 queue1[1:] 写入 queue1
		qTop := queue2[0]         // 把 queue2[0] 写入 qTop :
		queue2 = queue2[1:]       // 把 queue2[1:] 写入 queue2
		if pTop.Val != qTop.Val { // 若 pTop.Val 不等于 qTop.Val
			return false // 返回 false
		}
		pLeft, pRight := pTop.Left, pTop.Right // 把 pTop.Left, pTop.Right 写入 pLeft, pRight :
		qLeft, qRight := qTop.Left, qTop.Right // 把 qTop.Left, qTop.Right 写入 qLeft, qRight :
		if (pLeft != nil) != (qLeft != nil) {  // 若 pLeft 不等于 nil) 不等于 (qLeft 不等于 nil
			return false // 返回 false
		}
		if (pRight != nil) != (qRight != nil) { // 若 pRight 不等于 nil) 不等于 (qRight 不等于 nil
			return false // 返回 false
		}
		if pLeft != nil { // 若 pLeft 不等于 nil
			queue1 = append(queue1, pLeft) // 把 append(queue1, pLeft) 写入 queue1
		}
		if pRight != nil { // 若 pRight 不等于 nil
			queue1 = append(queue1, pRight) // 把 append(queue1, pRight) 写入 queue1
		}
		if qLeft != nil { // 若 qLeft 不等于 nil
			queue2 = append(queue2, qLeft) // 把 append(queue2, qLeft) 写入 queue2
		}
		if qRight != nil { // 若 qRight 不等于 nil
			queue2 = append(queue2, qRight) // 把 append(queue2, qRight) 写入 queue2
		}
	}
	return len(queue1) == 0 && len(queue2) == 0 // 返回 长度(queue1) 等于 0 且 长度(queue2) 等于 0
}

type tc struct { // 定义类型
	p    *TreeNode // 节点 乘 TreeNode
	q    *TreeNode // 节点 乘 TreeNode
	want bool      // want bool
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []tc{ // 把 []tc{ 写入 cases :
		{buildTree(nil), buildTree(nil), true},
		{buildTree([]interface{}{1}), buildTree([]interface{}{1}), true},
		{buildTree([]interface{}{1, 2, 3}), buildTree([]interface{}{1, 2, 3}), true},
		{buildTree([]interface{}{1, 2, 3}), buildTree([]interface{}{1, 2, nil, 3}), false},
		{buildTree([]interface{}{1}), buildTree([]interface{}{2}), false},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		got := isSameTree(c.p, c.q) // 把 isSameTree(字符.节点, 字符.节点) 写入 got :
		if got != c.want {          // 若 got 不等于 字符.want
			fmt.Printf("case %d failed: got %v want %v\n", idx, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
