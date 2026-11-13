-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442
-- LeetCode 926. 将字符串翻转到单调递增 — Lua 版（方案1）
local function min_flips_mono_incr(s) -- local function min_flips_mono_incr(字符串)
	local ones, flips = 0, 0 -- 把 0, 0 写入 local ones, flips
	for i = 1, #s do -- 把 1, #字符串 do 写入 for i
		local c = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local c
		if c == "1" then
			ones = ones + 1 -- 若 字符 等于 「1」 then ones 赋值为 ones 加 1
		else -- 否则
			flips = flips + 1 -- 把 flips 加 1 存入 flips
			if ones < flips then
				flips = ones
			end -- 若 ones 小于 flips then flips 赋值为 ones 终点
		end -- 终点
	end -- 终点
	return flips -- 返回 flips
end -- 终点
assert(min_flips_mono_incr("00110") == 1) -- 断言校验
assert(min_flips_mono_incr("010110") == 2) -- 断言校验
assert(min_flips_mono_incr("00011000") == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
