'''
 Логические операции
'''
f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n\n")
'''
 Побитовые операции
'''
j = 7
k = 20
print("j = %d; j в двоичном формате: %s" % (j, bin(j) ) )
print("k = %d; k в двоичном формате: %s" % (k, bin(k) ) )
print("j & k: %d; двоичный: %s" % (j & k, bin(j & k)  ) )
# побитовое AND
print("j | k: %d; двоичный: %s" % (j | k, bin(j | k)  ) )
# побитовое OR
print("j ^ k: %d; двоичный: %s" % (j ^ k, bin(j ^ k)  ) )
# побитовое XOR
print("~k: %d; двоичный: %s" % (~k, bin(~k)) ) # инверсия двоичного числа
print("k>>1: %d; двоичный: %s" % (k>>1, bin(k>>1)) ) # сдвиг на один бит вправо
print("k<<1: %d; двоичный: %s" % (k<<1, bin(k<<1)) ) # сдвиг на один бит влево
print("\n\n")


A = 1
B = 2
C = True
D = False


print(f"C={C}, D={D}\n\
¬(C∧D)=\t\t{not(C and D)}\n\
C∧D∨¬(C∧D)=\t{(C and D) or not(C and D)}\n\
¬C∨D=\t\t{not C or D}\n")


print(f"A = {A}, B = {B}\n\
A<=B\t\tis {A<=B}\n\
A>B ∨ A==B\tis {A>B or A==B}\n\
¬(A<B)\t\tis {not (A<B)}\n")


s = 154
p = 6


print(f"s={s}\t\t\t\tp={p}\n\
bin(s)={bin(s)}\tbin(p)={bin(p)}\n")


s = s | p
print(f"(s or p)=%d\nbin(s or p)=%s\n\
s>>2=%d\t\t\t\tp>>2=%d\
" %(s | p, bin(s | p), s>>2, p>>2))
