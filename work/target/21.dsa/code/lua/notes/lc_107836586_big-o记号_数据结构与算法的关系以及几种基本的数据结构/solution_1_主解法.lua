-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
-- LeetCode 107836586. Big-O 记号 — Lua 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）
local function classify(coeffs) -- local function classify(coeffs)
	for deg = #coeffs, 1, -1 do -- 把 #coeffs, 1, 减 1 do 写入 for deg
		if coeffs[deg] ~= 0 then -- 若 coeffs[deg] ~ 赋值为 0 then
			local d = deg - 1 -- 转 0 基次数
			if d > 1 then -- 若 d 超过 1 then
				return string.format("O(n^%d)", d) -- 返回 string.format(「O(元素个数 按位异或 对…取模 d)」, d)
			elseif d == 1 then -- 把 赋值为 1 then 写入 elseif d
				return "O(n)" -- 返回 「O(元素个数)」
			else -- 否则
				return "O(1)" -- 返回 「O(1)」
			end -- 终点
		end -- 终点
	end -- 终点
	return "O(1)" -- 返回 「O(1)」
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ { 1, 0, 0, 0 }, "O(1)" },
	{ { 0, 0, 0, 35 }, "O(n^3)" },
	{ { 0, 0, 1, 0 }, "O(n^2)" },
	{ { 0, 1, 0, 0 }, "O(n)" },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = classify(c[1]) -- 把 classify(字符[1]) 写入 local got
	assert(got == c[2], string.format("case %d failed: got %s want %s", idx, got, c[2])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
