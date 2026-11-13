-- 来源：https://blog.csdn.net/tyro_java/article/details/107490876
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案7：八皇后位置对列表）
local function n_queens_simple(n) -- local function n_queens_simple(元素个数)
	local positions = {} -- { {row, col}, ... }
	local solutions = {} -- 把 {} 写入 local solutions

	local function safe(r, c) -- local function safe(右指针, 字符)
		for _, p in ipairs(positions) do -- 遍历取 节点
			if p[1] == r or math.abs(p[1] - r) == math.abs(p[2] - c) then
				return false -- 返回 false
			end -- 终点
		end -- 终点
		return true -- 返回 true
	end -- 终点

	local function solve(col) -- local function solve(col)
		if col == n then -- 若 col 等于 元素个数 then
			local snap = {} -- 把 {} 写入 local snap
			for i, p in ipairs(positions) do
				snap[i] = p[1]
			end -- 遍历取 节点
			solutions[#solutions + 1] = snap -- 把 snap 写入 solutions[#solutions + 1]
			return -- return
		end -- 终点
		for r = 0, n - 1 do -- 让 右指针 从 0 走到 元素个数（Lua 1 基）
			if safe(r, col) then -- 若 safe(右指针, col) then
				positions[#positions + 1] = { r, col } -- 把 {右指针, col} 写入 positions[#positions + 1]
				solve(col + 1) -- solve(col 加 1)
				table.remove(positions) -- table 弹出 positions)
			end -- 终点
		end -- 终点
	end -- 终点

	solve(0) -- solve(0)
	return solutions -- 返回 solutions
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ 8, 92, { 0, 4, 7, 5, 2, 6, 1, 3 } },
	{ 1, 1, { 0 } },
	{ 2, 0, nil },
	{ 4, 2, { 1, 3, 0, 2 } },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local sols = n_queens_simple(c[1]) -- 把 n_queens_simple(字符[1]) 写入 local sols
	assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols) -- 断言校验
	if c[3] then -- 若 字符[3] then
		for j = 1, #c[3] do -- 把 1, #字符[3] do 写入 for j
			assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch") -- 断言校验
		end -- 终点
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
