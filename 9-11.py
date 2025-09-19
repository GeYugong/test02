import math as m
esp = 1e-5  # esp表示给定精度
s = 0  # s表示sin值
x = float(input('输入角度值：'))
# --------begin-------
ang=m.pi*x/180
T=0
print(m.pi)
while True:

    deno=1
    for n in range(1,2*T+2):
        deno = deno*n


    if T%2==0:
        s = s + ((ang**(2*T+1))/deno)
    else:
        s = s - ((ang**(2*T+1))/deno)

    if abs(s-m.sin(ang))<=esp:
        break
    T+=1   

# ---------end--------
print('sin_self={:.6f}'.format(s))  
print('math.sin={:.6f}'.format(m.sin(ang)))
