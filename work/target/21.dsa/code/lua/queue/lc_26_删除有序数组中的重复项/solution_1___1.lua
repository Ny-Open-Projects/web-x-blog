-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
-- LeetCode 26. 删除有序数组中的重复项 — Lua 版

-- 方案1：k 指针 —— 相邻比较，不同元素逐个写入前 k 个位置
local function remove_duplicates(nums) -- local function remove_duplicates(数组)
	if #nums == 0 then
		return 0
	end -- 若 #数组 等于 0 then return 0 终点
	local k = 2 -- TS 中 k 从 1（0 基）开始，对应 Lua 1 基下标 2
	for i = 2, #nums do -- 把 2, #数组 do 写入 for i
		if nums[i] ~= nums[i - 1] then -- 若 数组[下标 i] ~ 赋值为 数组[下标 i 减 1] then
			nums[k] = nums[i] -- 把 数组[下标 i] 写入 nums[k]
			k = k + 1 -- 把 下标 k 加 1 存入 下标 k
		end -- 终点
	end -- 终点
	return k - 1 -- 返回 下标 k 减 1
end -- 终点

local function eq_arr(a, b) -- local function eq_arr(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do -- 把 1, #数组 do 写入 for i
		if a[i] ~= b[i] then
			return false
		end -- 若 数组[下标 i] ~ 赋值为 b[下标 i] then return false 终点
	end -- 终点
	return true -- 返回 true
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local cases = { -- 把 { 写入 local cases
	{ input = { 1, 1, 2 }, k = 2, pre = { 1, 2 } },
	{ input = { 1, 2, 3 }, k = 3, pre = { 1, 2, 3 } },
	{ input = {}, k = 0, pre = {} },
}
for _, c in ipairs(cases) do -- 遍历取 字符
	local nums = {} -- 把 {} 写入 local nums
	for i, v in ipairs(c.input) do
		nums[i] = v
	end -- 遍历取 值
	local got = remove_duplicates(nums) -- 把 remove_duplicates(数组) 写入 local got
	local prefix = {} -- 把 {} 写入 local prefix
	for i = 1, got do
		prefix[i] = nums[i]
	end -- 让 下标 i 从 1 走到 got（Lua 1 基）
	assert(got == c.k and eq_arr(prefix, c.pre), string.format("FAIL removeDuplicates k=%d", got)) -- 把 对…取模 d", got)) 写入 string.format("FAIL removeDuplicates k
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
