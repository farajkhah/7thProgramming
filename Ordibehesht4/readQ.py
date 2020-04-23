def read_q(file, count):
    output = []
    address_pic = ''
    g_list = ['a', 'b', 'c', 'd']
    s = file.readline()
    if s == '':
        return "NULL", "", ""
    tot = s[s.find("{") + 1:s.find("}")]
    qs = tot[0:tot.find("?") + 1]
    gz = tot[tot.find("?") + 1:]
    sp = gz.split(":")
    last_g = sp[-1].split("@")[0]
    address_pic = sp[-1].split("@")[1]
    sp[-1] = last_g
    t = 0
    output.append("{}-{}".format(count, qs))
    for i in range(4):
        if sp[i + 1][0] == '=':
            t = i + 1
            output.append("{}){}".format(g_list[i], sp[i + 1][1:]))
        else:
            output.append("{}){}".format(g_list[i], sp[i + 1]))
    return output, t, address_pic
