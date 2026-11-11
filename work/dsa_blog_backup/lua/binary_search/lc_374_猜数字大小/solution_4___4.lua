-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238093
-- LeetCode 374. 猜数字大小 — Lua 版（方案4：迭代二分）
local pick = 6 -- 把 6 写入 local pick
local function guess(num) -- local function guess(num)
	if num == pick then
		return 0
	end -- 若 num 等于 pick then return 0 终点
	if num < pick then
		return 1
	end -- 若 num 小于 pick then return 1 终点
	return -1 -- 返回 减 1
end -- 终点
local function guess_number(n) -- local function guess_number(元素个数)
	local low, high = 1, n -- 把 1, 元素个数 写入 local low, high
	while low <= high do -- 把 high do 写入 while low <
		local mid = math.floor((low + high) / 2) -- 把 math.floor((low 加 high) 除以 2) 写入 local mid
		local res = guess(mid) -- 把 guess(中点) 写入 local res
		if res == 0 then
			return mid
		end -- 若 结果 等于 0 then return 中点 终点
		if res == 1 then
			low = mid + 1
		else
			high = mid - 1
		end -- 若 结果 等于 1 then low 赋值为 中点 加 1 else high 赋值为 中点 减 1 终点
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点
local cases = { { 10, 6 }, { 1, 1 }, { 5, 3 }, { 2, 2 } } -- 把 {{10, 6}, {1, 1}, {5, 3}, {2, 2}} 写入 local cases
for _, c in ipairs(cases) do -- 遍历取 字符
	pick = c[2] -- 把 字符[2] 存入 pick
	assert(guess_number(c[1]) == c[2], "n=" .. c[1] .. " pick=" .. c[2]) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
