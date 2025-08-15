-- 加载 luasocket 库
local http = require("socket.http")
local ltn12 = require("ltn12")
local cjson = require("cjson")




-- 定义模块内容
local M = {}

-- 定义一个函数，用于获取 MPID
M.get_mpid = function(ip)
    -- 创建一个表来存储响应内容
    -- 定义要请求的 URL
    local url = "http://mpid-server:8000/api/v1/mpid/ip/"
    local response = {}

    -- 发送 HTTP GET 请求
    local ok, code, headers, status = http.request{
        url = url .. ip,
        method = "GET",
        headers = {
            ["Content-Type"] = "application/json",
            ["User-Agent"] = "LuaSocket"
        },
        sink = ltn12.sink.table(response)
    }
    if code == 200 then
        local data = cjson.decode(table.concat(response))
        if data["code"] == 0 then
            return data["data"]["mpid"]
        else
            return nil
        end
    else
        return nil
    end
end

-- 返回模块表
return M