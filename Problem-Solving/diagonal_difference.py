a = np.arange(9) 
a = a.reshape(3,3)
l_d = 0
r_d = 0
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if i == j:
            l_d += a[i][j]
        if j == (a.shape[1] - i - 1):
            r_d += a[i][j]
output = abs(l_d-r_d)
print(output)

# ans = 0
# for i in range(len(c)):
#     ans += c[i][i]
#     ans -= c[i][len(c)-1-i]
    
# ans
    
