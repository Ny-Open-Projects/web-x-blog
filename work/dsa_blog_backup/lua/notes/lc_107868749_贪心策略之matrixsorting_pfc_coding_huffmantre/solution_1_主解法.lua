-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
-- LeetCode 107868749. 贪心策略 — Lua 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
local function matrix_sort(matrix) -- local function matrix_sort(矩阵)
	local rows, cols = #matrix, #matrix[1] -- 把 #矩阵, #矩阵[1] 写入 local rows, cols
	for c = 1, cols do -- 让 字符 从 1 走到 列数（Lua 1 基）
		local col = {} -- 把 {} 写入 local col
		for r = 1, rows do
			col[r] = matrix[r][c]
		end -- 让 右指针 从 1 走到 行数（Lua 1 基）
		table.sort(col) -- 排序
		for r = 1, rows do
			matrix[r][c] = col[r]
		end -- 让 右指针 从 1 走到 行数（Lua 1 基）
	end -- 终点
	for r = 1, rows do -- 让 右指针 从 1 走到 行数（Lua 1 基）
		table.sort(matrix[r]) -- 排序
	end -- 终点
	return matrix -- 返回 矩阵
end -- 终点

-- 节点：{freq=..., sym=...} 叶子 或 {freq=..., left=..., right=...} 内部
local function build_huffman(freqs) -- local function build_huffman(freqs)
	local nodes = {} -- 把 {} 写入 local nodes
	for sym, f in pairs(freqs) do -- 遍历取 f
		nodes[#nodes + 1] = { freq = f, sym = sym } -- 把 { 频次表 赋值为 f, sym 赋值为 sym } 写入 nodes[#nodes + 1]
	end -- 终点
	table.sort(nodes, function(a, b)
		return a.freq < b.freq
	end) -- 排序
	while #nodes > 1 do -- while #nodes 超过 1 do
		local a = table.remove(nodes, 1) -- 把 table 弹出 nodes, 1) 写入 local a
		local b = table.remove(nodes, 1) -- 把 table 弹出 nodes, 1) 写入 local b
		local merged = { freq = a.freq + b.freq, left = a, right = b }
		local i = 1 -- 把 1 写入 local i
		while i <= #nodes and nodes[i].freq < merged.freq do
			i = i + 1
		end
		table.insert(nodes, i, merged) -- table 插入 nodes, 下标 i, merged)
	end -- 终点
	return nodes[1] -- 返回 nodes[1]
end -- 终点

local function huffman_codes(freqs) -- local function huffman_codes(freqs)
	local root = build_huffman(freqs) -- 把 build_huffman(freqs) 写入 local root
	local codes = {} -- 把 {} 写入 local codes
	local function walk(node, prefix) -- local function walk(节点, prefix)
		if node.sym ~= nil then -- 若 节点.sym ~ 赋值为 nil then
			codes[node.sym] = (prefix == "" and "0") or prefix -- 把 (prefix 等于 「」 and 「」) or prefix 写入 codes[node.sym]
		else -- 否则
			walk(node.left, prefix .. "0") -- walk(节点.左边界, prefix .. 「0」)
			walk(node.right, prefix .. "1") -- walk(节点.右边界, prefix .. 「1」)
		end -- 终点
	end -- 终点
	walk(root, "") -- walk(根节点, 「」)
	return codes -- 返回 codes
end -- 终点

local freqs = { A = 5, B = 9, C = 12, D = 13, E = 16, F = 45 }

-- case1: matrixSort
local mat = { { 5, 3, 4 }, { 1, 6, 2 }, { 7, 9, 8 } } -- 把 {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}} 写入 local mat
matrix_sort(mat) -- matrix_sort(mat)
local want_mat = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } } -- 把 {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}} 写入 local want_mat
for i = 1, 3 do -- 让 下标 i 从 1 走到 3（Lua 1 基）
	for j = 1, 3 do -- 让 下标 j 从 1 走到 3（Lua 1 基）
		assert(mat[i][j] == want_mat[i][j], "matrixSort mismatch") -- 断言校验
	end -- 终点
end -- 终点

-- case2: WPL
local codes = huffman_codes(freqs) -- 把 huffman_codes(freqs) 写入 local codes
local wpl = 0 -- 把 0 写入 local wpl
local code_list = {} -- 把 {} 写入 local code_list
for sym, f in pairs(freqs) do -- 遍历取 f
	local c = codes[sym] -- 把 codes[sym] 写入 local c
	wpl = wpl + f * #c -- 把 wpl 加 f 乘 #字符 存入 wpl
	code_list[#code_list + 1] = c -- 把 字符 写入 code_list[#code_list + 1]
end -- 终点
assert(wpl == 224, "WPL mismatch: " .. tostring(wpl)) -- 断言校验

-- case3: 前缀无关
local prefix_free = true -- 把 true 写入 local prefix_free
for i = 1, #code_list do -- 把 1, #code_list do 写入 for i
	for j = 1, #code_list do -- 把 1, #code_list do 写入 for j
		if i ~= j and code_list[j]:sub(1, #code_list[i]) == code_list[i] then
			prefix_free = false -- 把 false 存入 prefix_free
		end -- 终点
	end -- 终点
end -- 终点
assert(prefix_free, "codes not prefix-free") -- 断言校验

print("PASS") -- 全部用例通过，输出 PASS
