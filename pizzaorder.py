s = input()
p = input()
c = input()
if s == "S":
    pr = 15
    if p == "Y":
        pr = pr+2
    else:
        pr = pr
    if c == "Y":
        pr = pr+1
    else:
        pr = pr
elif s == "M":
    pr = 20
    if p == "Y":
        pr = pr + 3
    else:
        pr = pr
    if c == "Y":
        pr = pr + 1
    else:
        pr = pr
elif s == "L":
    pr = 25
    if p == "Y":
        pr = pr + 3
    else:
        pr = pr
    if c == "Y":
        pr = pr + 1
    else:
        pr = pr
print(f"Thank you for choosing Python Pizza Deliveries!Your final bill is: ${pr}.")
