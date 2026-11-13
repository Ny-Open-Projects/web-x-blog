-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
-- LeetCode 1329. 将矩阵按对角线排序 — Lua 版

-- 方案2：优化版 —— 按 r-c 分组收集对角线（1 基下标偏移相同），升序排序，写回时按 shift 取队首
local function diagonal_sort(mat) -- local function diagonal_sort(mat)
	local rows, cols = #mat, #mat[1] -- 把 #mat, #mat[1] 写入 local rows, cols
	local diags = {} -- 把 {} 写入 local diags
	for r = 1, rows do -- 让 右指针 从 1 走到 行数（Lua 1 基）
		for c = 1, cols do -- 让 字符 从 1 走到 列数（Lua 1 基）
			local key = r - c -- 把 右指针 减 字符 写入 local key
			if not diags[key] then
				diags[key] = {}
			end -- 若 not diags[key] then diags[key] 赋值为 {} 终点
			diags[key][#diags[key] + 1] = mat[r][c] -- 把 mat[右指针][字符] 写入 diags[key][#diags[key] + 1]
		end -- 终点
	end -- 终点
	for _, arr in pairs(diags) do -- 遍历取 数组
		table.sort(arr) -- 排序
	end -- 终点
	local pos = {} -- 把 {} 写入 local pos
	for r = 1, rows do -- 让 右指针 从 1 走到 行数（Lua 1 基）
		for c = 1, cols do -- 让 字符 从 1 走到 列数（Lua 1 基）
			local key = r - c -- 把 右指针 减 字符 写入 local key
			if not pos[key] then
				pos[key] = 1
			end -- 若 not pos[key] then pos[key] 赋值为 1 终点
			mat[r][c] = diags[key][pos[key]] -- 把 diags[key][pos[key]] 写入 mat[r][c]
			pos[key] = pos[key] + 1 -- 把 pos[key] 加 1 写入 pos[key]
		end -- 终点
	end -- 终点
	return mat -- 返回 mat
end -- 终点

-- 深拷贝（等价于 TS 的 m.map(r => r.slice())）
local function clone_matrix(m) -- local function clone_matrix(映射表)
	local out = {} -- 把 {} 写入 local out
	for i = 1, #m do -- 把 1, #映射表 do 写入 for i
		local row = {} -- 把 {} 写入 local row
		for j = 1, #m[i] do
			row[j] = m[i][j]
		end -- 把 1, #映射表[下标 i] do row[下标 j] 赋值为 映射表[下标 i][下标 j] 终点 写入 for j
		out[i] = row -- 把 row 写入 out[i]
	end -- 终点
	return out -- 返回 out
end -- 终点

local function eq_matrix(a, b) -- local function eq_matrix(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do -- 把 1, #数组 do 写入 for i
		if #a[i] ~= #b[i] then
			return false
		end -- 若 #数组[下标 i] ~ 赋值为 #b[下标 i] then return false 终点
		for j = 1, #a[i] do -- 把 1, #数组[下标 i] do 写入 for j
			if a[i][j] ~= b[i][j] then
				return false
			end -- 若 数组[下标 i][下标 j] ~ 赋值为 b[下标 i][下标 j] then return false 终点
		end -- 终点
	end -- 终点
	return true -- 返回 true
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local m = { { 3, 3, 1, 1 }, { 2, 2, 1, 2 }, { 1, 1, 1, 2 } } -- 把 {{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}} 写入 local m
local got = diagonal_sort(clone_matrix(m)) -- 把 diagonal_sort(clone_matrix(映射表)) 写入 local got
local exp = { { 1, 1, 1, 1 }, { 1, 2, 2, 2 }, { 1, 2, 3, 3 } } -- 把 {{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}} 写入 local exp
assert(eq_matrix(got, exp), "FAILED") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
