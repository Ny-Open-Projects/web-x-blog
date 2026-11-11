-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098
-- LeetCode 937. 重新排列日志文件 — Lua 版（方案1）
local function reorder_log_files(logs) -- local function reorder_log_files(logs)
	local function is_digit(s) -- local function is_digit(字符串)
		local c = s:sub(1, 1) -- 把 字符串:sub(1, 1) 写入 local c
		return c >= "0" and c <= "9" -- 返回 字符 不低于 「0」 and 字符 不超过 「0」
	end -- 终点
	local letter, digit = {}, {} -- 把 {}, {} 写入 local letter, digit
	for _, log in ipairs(logs) do -- 遍历取 log
		local content = log:match(" (.+)$") -- 把 log:match(「 (. 加 )$」) 写入 local content
		if is_digit(content) then
			digit[#digit + 1] = log
		else
			letter[#letter + 1] = log
		end
	end -- 终点
	table.sort(letter, function(a, b) -- 排序
		local ca = a:match(" (.+)$") -- 把 数组:match(「 (. 加 )$」) 写入 local ca
		local cb = b:match(" (.+)$") -- 把 b:match(「 (. 加 )$」) 写入 local cb
		if ca ~= cb then
			return ca < cb
		end -- 若 ca ~ 赋值为 cb then return ca 小于 cb 终点
		return a < b -- 返回 数组 小于 b
	end) -- 终点)
	for _, d in ipairs(digit) do
		letter[#letter + 1] = d
	end -- 遍历取 d
	return letter -- 返回 letter
end -- 终点
local got = reorder_log_files({ "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo" })
assert(#got == 5) -- 断言校验
assert(
	got[1] == "g1 act car"
		and got[2] == "a8 act zoo"
		and got[3] == "ab1 off key dog"
		and got[4] == "a1 9 2 3 1"
		and got[5] == "zo4 4 7"
) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
