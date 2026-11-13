-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618
-- LeetCode 2042. 检查句子中的数字是否递增 — Lua 版（方案1）
local function are_numbers_ascending(s) -- local function are_numbers_ascending(字符串)
	local prev = -1 -- 把 减 1 写入 local prev
	for tok in s:gmatch("%S+") do -- for tok in 字符串:gmatch(「 对…取模 S 加 」) do
		local c = tok:sub(1, 1) -- 把 tok:sub(1, 1) 写入 local c
		if c >= "0" and c <= "9" then -- 若 字符 不低于 「0」 and 字符 不超过 「0」 then
			local num = tonumber(tok) -- 把 tonumber(tok) 写入 local num
			if num <= prev then
				return false
			end -- 若 num 不超过 前一个 then return false 终点
			prev = num -- 把 num 存入 前一个
		end -- 终点
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles") == true) -- 断言校验
assert(are_numbers_ascending("hello world 5 x 5") == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
