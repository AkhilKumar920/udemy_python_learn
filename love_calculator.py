name1 = input()
name2 = input()
cn = name1.lower() + name2.lower()
t = cn.count("t")
r = cn.count("r")
u = cn.count("u")
e = cn.count("e")
l = cn.count("l")
o = cn.count("o")
v = cn.count("v")
e = cn.count("e")
cnt = int(str(t+r+u+e)+str(l+o+v+e))
if cnt <10 or cnt >90:
    print(f"Your score is {cnt}, you go together like coke and mentos.")
elif cnt >40 and cnt<50:
    print(f"Your score is {cnt}, you are alright together.")
else:
    print(f"Your score is {cnt}.")
