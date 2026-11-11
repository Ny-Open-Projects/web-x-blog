-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368
-- LeetCode 349. 两个数组的交集 — Lua 版（方案17）
local function intersection(nums1, nums2) -- local function intersection(数组1, 数组2)
	local s1 = {} -- 把 {} 写入 local s1
	for _, v in ipairs(nums1) do
		s1[v] = true
	end -- 遍历取 值
	local seen = {} -- 把 {} 写入 local seen
	local res = {} -- 把 {} 写入 local res
	for _, v in ipairs(nums2) do -- 遍历取 值
		if s1[v] and not seen[v] then -- 若 s1[值] and not 已见集合[值] then
			res[#res + 1] = v -- 把 值 写入 res[#res + 1]
			seen[v] = true -- 把 true 写入 seen[v]
		end -- 终点
	end -- 终点
	return res -- 返回 结果
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
assert(eq(intersection({ 1, 2, 2, 1 }, { 2, 2 }), { 2 })) -- 断言校验
assert(eq(intersection({ 4, 9, 5 }, { 9, 4, 9, 8, 4 }), { 9, 4 })) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
