def N(v):
 m=min(v);M=max(v);return [(x-m)/(M-m) if M!=m else 1 for x in v]
def calcular_pesos(n):
 a=N([i.sc20 for i in n]);b=N([i.sc50 for i in n]);c=N([i.sc100 for i in n]);d=N([i.hist_ap for i in n]);e=N([i.atraso for i in n]);r=[]
 for k,x in enumerate(n): r.append(.3*a[k]+.25*b[k]+.2*c[k]+.15*d[k]+.1*e[k])
 s=sum(r)
 [setattr(x,'peso',p/s) for x,p in zip(n,r)]
 return sorted(n,key=lambda z:z.peso,reverse=True)
