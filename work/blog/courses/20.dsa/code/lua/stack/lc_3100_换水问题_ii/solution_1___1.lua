-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
-- LeetCode 3100. 换水问题 II — Lua 版（方案1）
local function max_bottles_drunk(num_bottles, num_exchange) -- local function max_bottles_drunk(num_bottles, num_exchange)
	local drunk = num_bottles -- 把 num_bottles 写入 local drunk
	local empty = num_bottles -- 把 num_bottles 写入 local empty
	while empty >= num_exchange do -- 把 num_exchange do 写入 while empty >
		empty = empty - num_exchange -- 把 empty 减 num_exchange 存入 empty
		num_exchange = num_exchange + 1 -- 把 num_exchange 加 1 存入 num_exchange
		drunk = drunk + 1 -- 把 drunk 加 1 存入 drunk
		empty = empty + 1 -- 把 empty 加 1 存入 empty
	end -- 终点
	return drunk -- 返回 drunk
end -- 终点
assert(max_bottles_drunk(10, 3) == 13) -- 断言校验
assert(max_bottles_drunk(1, 2) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
