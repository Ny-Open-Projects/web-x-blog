-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389
-- LeetCode 198. 打家劫舍 — Lua 版（方案9）
local function rob(nums)
	local a, b = 0, 0
	for _, v in ipairs(nums) do
		a, b = b, math.max(b, a + v)
	end
	return b
end
assert(rob({ 1, 2, 3, 1 }) == 4)
assert(rob({ 2, 7, 9, 3, 1 }) == 12)
print("PASS") -- 全部用例通过，输出 PASS
