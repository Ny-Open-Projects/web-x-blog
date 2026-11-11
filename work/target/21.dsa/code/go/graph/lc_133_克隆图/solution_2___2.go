// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

// Node 对应 python ref 中的 Node
type Node struct { // 定义类型
	Val       int     // Val int
	Neighbors []*Node // Neighbors [] 乘 Node
}

// cloneGraph 忠实翻译 python ref（DFS 递归）
func cloneGraph(node *Node) *Node { // 定义函数/方法 cloneGraph
	if node == nil { // 若 节点 等于 nil
		return nil // 返回 nil
	}
	visited := make(map[*Node]*Node) // 把 make(映射表[ 乘 Node] 乘 Node) 写入 visited :
	var dfs func(n *Node) *Node      // var dfs func(元素个数 乘 Node) 乘 Node
	dfs = func(n *Node) *Node {      // 把 func(元素个数 乘 Node) 乘 Node { 写入 dfs
		if c, ok := visited[n]; ok { // 若 字符, ok : 赋值为 已访问集合[元素个数]; ok
			return c // 返回 字符
		}
		clone := &Node{Val: n.Val}             // 把 按位与 Node{Val: 元素个数.Val} 写入 clone :
		visited[n] = clone                     // 把 clone 写入 visited[n]
		for _, neighbor := range n.Neighbors { // 同时取 _ 与 neighbor 遍历
			clone.Neighbors = append(clone.Neighbors, dfs(neighbor)) // 把 append(clone.Neighbors, dfs(neighbor)) 写入 clone.Neighbors
		}
		return clone // 返回 clone
	}
	return dfs(node) // 定义函数/方法 dfs
}

// buildGraph 由邻接表（1-indexed）构图，返回 1 号节点
func buildGraph(adj [][]int) *Node { // 定义函数/方法 buildGraph
	if len(adj) == 0 { // 若 长度(邻接表) 等于 0
		return nil // 返回 nil
	}
	nodes := make([]*Node, len(adj)+1) // 把 make([] 乘 Node, 长度(邻接表) 加 1) 写入 nodes :
	for i := 1; i <= len(adj); i++ {   // 让 下标 i 从 1 开始计数
		nodes[i] = &Node{Val: i} // 把 按位与 Node{Val: 下标 i} 写入 nodes[i]
	}
	for i, nbrs := range adj { // 同时取 下标 i 与 nbrs 遍历
		for _, nb := range nbrs { // 同时取 _ 与 nb 遍历
			nodes[i+1].Neighbors = append(nodes[i+1].Neighbors, nodes[nb])
		}
	}
	return nodes[1] // 返回 nodes[1]
}

// graphSignature 对应 python ref 的 graph_signature
func graphSignature(node *Node) map[int][]int { // 定义函数/方法 graphSignature
	visited := make(map[int][]int) // 把 make(映射表[int][]int) 写入 visited :
	var dfs func(n *Node)          // var dfs func(元素个数 乘 Node)
	dfs = func(n *Node) {          // 把 func(元素个数 乘 Node) { 写入 dfs
		if _, ok := visited[n.Val]; ok { // 若 _, ok : 赋值为 已访问集合[元素个数.Val]; ok
			return // return
		}
		vals := make([]int, 0, len(n.Neighbors)) // 把 make([]int, 0, 长度(元素个数.Neighbors)) 写入 vals :
		for _, x := range n.Neighbors {          // 同时取 _ 与 x 遍历
			vals = append(vals, x.Val) // 把 append(vals, x.Val) 写入 vals
		}
		sort.Ints(vals)                 // sort.Ints(vals)
		visited[n.Val] = vals           // 把 vals 写入 visited[n.Val]
		for _, x := range n.Neighbors { // 同时取 _ 与 x 遍历
			dfs(x) // dfs(x)
		}
	}
	if node != nil { // 若 节点 不等于 nil
		dfs(node) // dfs(节点)
	}
	return visited // 返回 已访问集合
}

func sigEqual(a, b map[int][]int) bool { // 定义函数/方法 sigEqual
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for k, va := range a { // 同时取 下标 k 与 va 遍历
		vb, ok := b[k]                 // 把 b[下标 k] 写入 vb, ok :
		if !ok || len(va) != len(vb) { // 若 取反 ok 或 长度(va) 不等于 长度(vb
			return false // 返回 false
		}
		for i := range va { // 把 range va { 写入 for i :
			if va[i] != vb[i] { // 若 va[下标 i] 不等于 vb[下标 i]
				return false // 返回 false
			}
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :

	// case1 normal: [[2,4],[1,3],[2,4],[1,3]] -> want {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
	c1 := cloneGraph(buildGraph([][]int{{2, 4}, {1, 3}, {2, 4}, {1, 3}}))
	want1 := map[int][]int{1: {2, 4}, 2: {1, 3}, 3: {2, 4}, 4: {1, 3}}
	if got := graphSignature(c1); !sigEqual(got, want1) { // 若 got : 赋值为 graphSignature(c1); 取反 sigEqual(got, want1
		ok = false                                            // 把 false 写入 ok
		fmt.Printf("FAIL case1 got %v want %v\n", got, want1) // 打印输出
	}

	// case2 boundary: 单节点无邻居 [[]] -> want {1:[]}
	c2 := cloneGraph(buildGraph([][]int{{}}))             // 把 cloneGraph(buildGraph([][]int{{}})) 写入 c2 :
	want2 := map[int][]int{1: {}}                         // 把 映射表[int][]int{1: {}} 写入 want2 :
	if got := graphSignature(c2); !sigEqual(got, want2) { // 若 got : 赋值为 graphSignature(c2); 取反 sigEqual(got, want2
		ok = false                                            // 把 false 写入 ok
		fmt.Printf("FAIL case2 got %v want %v\n", got, want2) // 打印输出
	}

	// case3 boundary: 两节点互连 [[2],[1]] -> want {1:[2],2:[1]}
	c3 := cloneGraph(buildGraph([][]int{{2}, {1}}))       // 把 cloneGraph(buildGraph([][]int{{2}, {1}})) 写入 c3 :
	want3 := map[int][]int{1: {2}, 2: {1}}                // 把 映射表[int][]int{1: {2}, 2: {1}} 写入 want3 :
	if got := graphSignature(c3); !sigEqual(got, want3) { // 若 got : 赋值为 graphSignature(c3); 取反 sigEqual(got, want3
		ok = false                                            // 把 false 写入 ok
		fmt.Printf("FAIL case3 got %v want %v\n", got, want3) // 打印输出
	}

	// case4 boundary: 空图 nil -> nil
	if cloneGraph(nil) != nil { // 若 cloneGraph(nil) 不等于 nil
		ok = false                                       // 把 false 写入 ok
		fmt.Println("FAIL case4 cloneGraph(nil) != nil") // 打印输出
	}

	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
