-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
-- LeetCode 350. 两个数组的交集 II — Lua 版（方案1）
local function intersect(nums1, nums2) -- local function intersect(数组1, 数组2)
	local a, b = nums1, nums2 -- 把 数组1, 数组2 写入 local a, b
	if #a > #b then
		a, b = b, a
	end -- 若 #数组 超过 #b then 数组, b 赋值为 b, 数组 终点
	local mp = {} -- 把 {} 写入 local mp
	for _, v in ipairs(a) do
		mp[v] = (mp[v] or 0) + 1
	end -- 遍历取 值
	local res = {} -- 把 {} 写入 local res
	for _, v in ipairs(b) do -- 遍历取 值
		if mp[v] and mp[v] > 0 then -- 若 mp[值] and mp[值] 超过 0 then
			res[#res + 1] = v -- 把 值 写入 res[#res + 1]
			mp[v] = mp[v] - 1 -- 把 mp[值] 减 1 写入 mp[v]
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
assert(eq(intersect({ 1, 2, 2, 1 }, { 2, 2 }), { 2, 2 })) -- 断言校验
assert(eq(intersect({ 4, 9, 5 }, { 9, 4, 9, 8, 4 }), { 9, 4 })) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
