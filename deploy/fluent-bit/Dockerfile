FROM fluent/fluent-bit:4.0.6-debug

USER root

# 安装 Lua 和 LuaSocket
RUN apt-get update && apt-get install -y \
    lua5.1 \
    liblua5.1-dev \
    luarocks \
    build-essential
RUN luarocks install luasocket \
    && luarocks install lua-cjson

ENTRYPOINT ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent-bit.conf"]
