-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
-- LeetCode 1. 两数之和 — Lua 版（方案1：暴力双循环）
local function two_sum(nums, target) -- local function two_sum(数组, 目标值)
	local n = #nums -- 把 #数组 写入 local n
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = i + 1, n do -- 把 下标 i 加 1, 元素个数 do 写入 for j
			if nums[i] + nums[j] == target then -- 若 数组[下标 i] 加 数组[下标 j] 等于 目标值 then
				return { i - 1, j - 1 } -- 返回 {下标 i 减 1, 下标 j 减 1}
			end -- 终点
		end -- 终点
	end -- 终点
	return {} -- 返回 {}
end -- 终点
local function eq(a, b) -- local function eq(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do
		if a[i] ~= b[i] then
			return false
		end
	end
	return true -- 返回 true
end -- 终点
assert(eq(two_sum({ 2, 7, 11, 15 }, 9), { 0, 1 })) -- 断言校验
assert(eq(two_sum({ 3, 2, 4 }, 6), { 1, 2 })) -- 断言校验
assert(eq(two_sum({ 3, 3 }, 6), { 0, 1 })) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
