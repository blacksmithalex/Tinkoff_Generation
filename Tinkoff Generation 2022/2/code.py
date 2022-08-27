p = [int(x) for x in input().split()]
n = int(input())

p_perl = [p[0] * 4, p[1] * 2, p[2], p[3] / 2]
m_perl = min(p_perl)
price = 0

if m_perl == p_perl[-1]:
    price += p[-1] * (n // 2)
    n %= 2
    m_perl = min(p_perl[:-1])

ind_m_perl = p_perl.index(m_perl)
if ind_m_perl == 0:
    price += n * 4 * p[0]
elif ind_m_perl == 1:
    price += n * 2 * p[1]
else:
    price += n * p[2]

print(price)









