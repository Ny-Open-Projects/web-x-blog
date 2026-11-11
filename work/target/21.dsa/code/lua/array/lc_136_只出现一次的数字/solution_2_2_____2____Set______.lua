-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105
-- LeetCode 136. 只出现一次的数字 — Lua 版（方案2）
local function single_number(nums)
	local x = 0
	for _, v in ipairs(nums) do
		x = x ~ v
	end
	return x
end
assert(single_number({ 2, 2, 1 }) == 1)
assert(single_number({ 4, 1, 2, 1, 2 }) == 4)
assert(single_number({ 1 }) == 1)
print("PASS") -- 全部用例通过，输出 PASS
