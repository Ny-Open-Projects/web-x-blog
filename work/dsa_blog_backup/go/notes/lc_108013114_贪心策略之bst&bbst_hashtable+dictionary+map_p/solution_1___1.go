// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// BST 二叉搜索树
type bstNode struct { // 定义类型
	val         int      // 值 int
	left, right *bstNode // 左边界, 右边界 乘 bstNode
}

type BST struct { // 定义类型
	root *bstNode // 根节点 乘 bstNode
}

func (t *BST) insert(val int) { // 定义函数/方法 insert
	if t.root == nil { // 若 另一字符串.根节点 等于 nil
		t.root = &bstNode{val: val} // 把 按位与 bstNode{值: 值} 写入 根节点
		return                      // return
	}
	cur := t.root // 把 另一字符串.根节点 写入 cur :
	for {         // for {
		if val < cur.val { // 若 值 小于 当前值.值
			if cur.left == nil { // 若 当前值.左边界 等于 nil
				cur.left = &bstNode{val: val} // 把 按位与 bstNode{值: 值} 写入 左边界
				return                        // return
			}
			cur = cur.left // 把 当前值.左边界 写入 当前值
		} else if val > cur.val { // 否则，若 值 超过 当前值.值
			if cur.right == nil { // 若 当前值.右边界 等于 nil
				cur.right = &bstNode{val: val} // 把 按位与 bstNode{值: 值} 写入 右边界
				return                         // return
			}
			cur = cur.right // 把 当前值.右边界 写入 当前值
		} else { // 否则
			return // return
		}
	}
}

func (t *BST) search(val int) bool { // 定义函数/方法 search
	cur := t.root    // 把 另一字符串.根节点 写入 cur :
	for cur != nil { // 把 nil { 写入 for cur !
		if val == cur.val { // 若 值 等于 当前值.值
			return true // 返回 true
		}
		if val < cur.val { // 若 值 小于 当前值.值
			cur = cur.left // 把 当前值.左边界 写入 当前值
		} else { // 否则
			cur = cur.right // 把 当前值.右边界 写入 当前值
		}
	}
	return false // 返回 false
}

// kruskalMST Kruskal 最小生成树
func kruskalMST(edges [][3]int) int { // 定义函数/方法 kruskalMST
	parent := map[int]int{}  // 把 映射表[int]int{} 写入 parent :
	var find func(int) int   // var find func(int) int
	find = func(x int) int { // 把 func(x int) int { 写入 find
		if _, ok := parent[x]; !ok { // 若 _, ok : 赋值为 parent[x]; 取反 ok
			parent[x] = x // 把 x 写入 parent[x]
		}
		for parent[x] != x { // 把 x { 写入 for parent[x] !
			parent[x] = parent[parent[x]] // 把 parent[parent[x]] 写入 parent[x]
			x = parent[x]                 // 把 parent[x] 写入 x
		}
		return x // 返回 x
	}
	union := func(a, b int) bool { // 把 func(数组, b int) bool { 写入 union :
		ra, rb := find(a), find(b) // 把 find(数组), find(b) 写入 ra, rb :
		if ra == rb {              // 若 ra 等于 rb
			return false // 返回 false
		}
		parent[ra] = rb // 把 rb 写入 parent[ra]
		return true     // 返回 true
	}
	// 按权重排序
	sorted := make([][3]int, len(edges)) // 把 make([][3]int, 长度(边集)) 写入 sorted :
	copy(sorted, edges)                  // copy(sorted, 边集)
	for i := 0; i < len(sorted); i++ {   // 让 下标 i 从 0 开始计数
		for j := i + 1; j < len(sorted); j++ { // 把 下标 i 加 1; 下标 j 小于 长度(sorted); 下标 j 加一 { 写入 for j :
			if sorted[j][2] < sorted[i][2] { // 若 sorted[下标 j][2] 小于 sorted[下标 i][2]
				sorted[i], sorted[j] = sorted[j], sorted[i] // 把 sorted[下标 j], sorted[下标 i] 写入 sorted[i], sorted[j]
			}
		}
	}
	total := 0                 // 把 0 写入 total :
	for _, e := range sorted { // 同时取 _ 与 e 遍历
		if union(e[0], e[1]) { // 定义函数/方法 union
			total += e[2] // 总和累加 e[2]
		}
	}
	return total // 返回 总和
}

func main() { // 程序入口：跑内嵌自测用例
	bst := &BST{}                            // 把 按位与 BST{} 写入 bst :
	for _, v := range []int{5, 3, 7, 1, 9} { // 同时取 _ 与 值 遍历
		bst.insert(v) // bst 插入 值)
	}
	if !bst.search(7) { // 若 取反 bst.search(7
		fmt.Println("FAIL search 7") // 打印输出
		os.Exit(1)                   // os.Exit(1)
	}
	if bst.search(4) { // 若 bst.search(4
		fmt.Println("FAIL search 4") // 打印输出
		os.Exit(1)                   // os.Exit(1)
	}
	mst := kruskalMST([][3]int{{0, 1, 4}, {0, 2, 3}, {1, 2, 1}, {1, 3, 2}})
	if mst != 6 { // 若 mst 不等于 6
		fmt.Printf("FAIL mst=%d want=6\n", mst) // 打印输出
		os.Exit(1)                              // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
