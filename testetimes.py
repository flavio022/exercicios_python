arquivo = open('times.txt','r')
times =[]
for i in arquivo:
    linha = i.rstrip()
    times.append(linha)        
for t1 in range(len(times)):
    for t2 in range(t1-1, len(times)):
        print(times[t1],'x', times[t2])
        
