package.path = package.path .. ";/fluent-bit/etc/?.lua"
local mpid = require("mpid")

function gtm(tag, timestamp, record)
  local ip = record["src_ip"]
  if ip == nil then
    return -1, timestamp, record
  end
  local mpid = mpid.get_mpid(record["src_ip"])
  record["mpid"] = tonumber(mpid)
  if mpid == nil then
    record["mpid"] = 0
  end
  return 1, timestamp, record
end