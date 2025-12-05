


def hex_to_rgb(hex_color):
    # 去除可能的'#'字符
    hex_color = hex_color.lstrip('#')
    # 将十六进制颜色转换为RGB值
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b