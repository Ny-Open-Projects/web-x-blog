-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
-- LeetCode 108013114. 贪心策略之BST&BBST_hashtable+dictionary+map — Lua 版（贪心策略之 BST/BBST/哈希表：Kruskal 最小生成树（并查集 + 排序））
local function kruskal_mst(edges) -- local function kruskal_mst(边集)
	local sorted = {} -- 把 {} 写入 local sorted
	for i, e in ipairs(edges) do
		sorted[i] = e
	end -- 遍历取 e
	table.sort(sorted, function(a, b)
		return a[3] < b[3]
	end) -- 排序
	local parent = {} -- 把 {} 写入 local parent

	local function find(x) -- local function find(x)
		if parent[x] == nil then
			parent[x] = x
		end -- 若 parent[x] 等于 nil then parent[x] 赋值为 x 终点
		while parent[x] ~= x do -- 把 x do 写入 while parent[x] ~
			parent[x] = parent[parent[x]] -- 把 parent[parent[x]] 写入 parent[x]
			x = parent[x] -- 把 parent[x] 存入 x
		end -- 终点
		return x -- 返回 x
	end -- 终点

	local total = 0 -- 把 0 写入 local total
	for _, e in ipairs(sorted) do -- 遍历取 e
		local u, v, w = e[1], e[2], e[3] -- 把 e[1], e[2], e[3] 写入 local u, v, w
		local ru, rv = find(u), find(v) -- 把 find(节点 u), find(值) 写入 local ru, rv
		if ru ~= rv then -- 若 ru ~ 赋值为 rv then
			parent[ru] = rv -- 把 rv 写入 parent[ru]
			total = total + w -- 把 总和 加 权重 存入 总和
		end -- 终点
	end -- 终点
	return total -- 返回 总和
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ { { 0, 1, 10 }, { 0, 2, 6 }, { 0, 3, 5 }, { 1, 3, 15 }, { 2, 3, 4 } }, 19 },
	{ { { 0, 1, 1 }, { 1, 2, 2 }, { 2, 3, 3 }, { 3, 4, 4 } }, 10 },
	{ { { 0, 1, 2 }, { 1, 2, 3 } }, 5 },
	{ {}, 0 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = kruskal_mst(c[1]) -- 把 kruskal_mst(字符[1]) 写入 local got
	assert(got == c[2], string.format("case %d failed: got %d want %d", idx, got, c[2])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
