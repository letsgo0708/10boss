arr_y = [1, 2, 3, 5, 7]
fx_n = 0
total_n = 0
arr_fx = set()

print()
print("치역에 3이 없는 경우 : 중복 제외하고 합 = 7")
print()
for a in arr_y:
    for b in arr_y:
        for c in arr_y:
            for d in arr_y:
                arr_fx.add(a)
                arr_fx.add(b)
                arr_fx.add(c)
                arr_fx.add(d)

                if sum(list(arr_fx)) == 7:
                    if 3 not in list(arr_fx):
                        fx_n += 1
                        print(f"{fx_n}번째, {a}, {b}, {c}, {d}")
                arr_fx = set()

print()
print("치역에 3이 있는 경우 : 중복 제외하고 합 = 10")
print()
for a in arr_y:
    for b in arr_y:
        for c in arr_y:
            for d in arr_y:
                arr_fx.add(a)
                arr_fx.add(b)
                arr_fx.add(c)
                arr_fx.add(d)

                if sum(list(arr_fx)) == 10:
                    if 3 in list(arr_fx):
                        fx_n += 1
                        print(f"{fx_n}번째, {a}, {b}, {c}, {d}")
                arr_fx = set()
print(f"전체 수 : {fx_n}")

