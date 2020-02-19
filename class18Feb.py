file = open("quize.mhd", "rt")
s = file.readline()
count = 0
while True:
    count += 1
    tot = s[s.find("{")+1:s.find("}")]
    qs = tot[0:tot.find("?")+1]
    gz = tot[tot.find("?")+1:]
    gozine = []
    sp = gz.split(":")
    print(str(count) + "-" + qs)
    t = 0
    for i in range(4):
        if sp[i+1][0] == ';':
            t = i+1
            print(sp[i+1][1:])
        else:
            print(sp[i+1])
    print("javabe dorost barabar as ba : ", t)
    s = file.readline()
    if s == '':
        break
