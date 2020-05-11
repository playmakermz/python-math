uang_budi = 420000 # silahkan di ganti
keperluan = 200000 + 200000

nisabnya = 73140

def persentasi(a,b):
    return a*b/100

total = uang_budi - keperluan

if total >= nisabnya:
    print(persentasi(total, 2.5))
    ab = persentasi(total, 2.5)
    print(total - ab)
    print('itu adalah sisahnnya')

else:
    print('maaf kurang cukup')
    