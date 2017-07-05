pais1, pais2, anos = 80.000, 200.000, 0
cresA, cresB = 0.03, 0.015
while(pais1<pais2):
    anos +=1
    pais1 = pais1 + (pais1*cresA)
    pais2 = pais2 +(pais2*cresB)
    print("Apos %i anos o pais A ultrapassou o país B em números de habitantes." % anos)
    print("País A: %.0f" % pais1)
    print("País B: %.0f" % pais2)


