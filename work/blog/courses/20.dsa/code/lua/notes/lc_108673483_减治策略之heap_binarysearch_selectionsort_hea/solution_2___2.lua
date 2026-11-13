-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
-- LeetCode 108673483. 减治策略 — Lua 版（方案2：快速选择求第 k 小，k 从 0 起）
local function select_k(a, lo, hi, k) -- local function select_k(数组, 左边界, 右边界, 下标 k)
	if lo == hi then
		return a[lo]
	end -- 若 左边界 等于 右边界 then return 数组[左边界] 终点
	local pivot = a[hi] -- 把 数组[右边界] 写入 local pivot
	local i = lo -- 把 左边界 写入 local i
	for j = lo, hi - 1 do -- 把 左边界, 右边界 减 1 do 写入 for j
		if a[j] <= pivot then -- 若 数组[下标 j] 不超过 pivot then
			a[i], a[j] = a[j], a[i] -- 把 数组[下标 j], 数组[下标 i] 写入 a[i], a[j]
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
	end -- 终点
	a[i], a[hi] = a[hi], a[i] -- 把 数组[右边界], 数组[下标 i] 写入 a[i], a[hi]
	if i == k then
		return a[i]
	end -- 若 下标 i 等于 下标 k then return 数组[下标 i] 终点
	if i > k then
		return select_k(a, lo, i - 1, k)
	end
	return select_k(a, i + 1, hi, k) -- 返回 select_k(数组, 下标 i 加 1, 右边界, 下标 k)
end -- 终点

local function quick_select(arr, k) -- local function quick_select(数组, 下标 k)
	local a = {} -- 把 {} 写入 local a
	for i, v in ipairs(arr) do
		a[i] = v
	end -- 遍历取 值
	return select_k(a, 1, #a, k + 1) -- 内部 1 基
end -- 终点

local base = { 3, 1, 4, 1, 5, 9, 2, 6 } -- 把 {3, 1, 4, 1, 5, 9, 2, 6} 写入 local base
local cases = { { 2, 2 }, { 3, 3 }, { 0, 1 }, { 7, 9 } } -- 把 {{2, 2}, {3, 3}, {0, 1}, {7, 9}} 写入 local cases
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = quick_select(base, c[1]) -- 把 quick_select(base, 字符[1]) 写入 local got
	assert(got == c[2], string.format("case %d failed: got %d want %d", idx, got, c[2])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
