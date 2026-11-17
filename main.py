import json,os,urllib.request as U
def P(p,d):return json.load(U.urlopen(U.Request(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(d).encode(),{'Content-Type':'application/json'})))
D={'P':(-10,-20,-11,-9),'N':(-8,-12,-19,-21,8,12,19,21),'B':(-11,-9,11,9),'R':(-10,-1,1,10),'Q':(-11,-9,11,9,-10,-1,1,10)}
D['K']=D['Q']
T={}
for p,m in zip('PNBRQK',(100,300,330,500,900,60000)):
 T[p]=[m+[6*(5-r)+3*min(c,7-c),7*e-3,3*e,10*(r==1),e,10*(r>5)-6*e][' PNBRQK'.find(p)-1]if 0<(i%10)<9 and 1<i//10<10 else 0 for i in range(120)for r,c in[(i//10-2,i%10-1)]for e in[min(c,7-c)+min(r,7-r)]]
def G(b):
 for i,p in enumerate(b):
  if p.isupper():
   for d in D[p]:
    j=i
    while 1:
     j+=d;q=b[j]
     if q==' 'or q.isupper():break
     if p=='P'and(d in(-10,-20)and(q!='.'or d==-20 and(i<81 or b[i-10]!='.'))or d in(-11,-9)and q=='.'):break
     yield i,j
     if p in'PNK'or q.islower():break
def mk(b,s,i,j):
 p=b[i];q=b[j];v=T[p][j]-T[p][i]
 if q.islower():v+=T[q.upper()][119-j]
 if p=='P'and j<29:p='Q';v+=T['Q'][j]-T['P'][j]
 b=b[:i]+'.'+b[i+1:];b=b[:j]+p+b[j+1:]
 return b[::-1].swapcase(),-(s+v)
H={}
class X(Exception):0
def S(b,s,d,a,B):
 global n
 n+=1
 if n>L:raise X
 if s<=-3e4:return s-d
 o=a;q=d<1;m=0
 if q:
  if s>=B:return s
  a=max(a,s);r=s
 else:
  r=-9e4;e=H.get(b)
  if d>2 and s>=B:
   v=-S(b[::-1].swapcase(),-s,d-3,-B,1-B)
   if v>=B:return v
  if e:
   m=e[3]
   if e[0]>=d and(e[1]<1 or e[1]==1 and e[2]>=B or e[1]>1 and e[2]<=a):return e[2]
 K=[]
 for i,j in G(b):
  if q and b[j]=='.':continue
  c,t=mk(b,s,i,j);K.append((c!=m,t,c))
 for _,t,c in sorted(K):
  v=-S(c,t,d-1,-B,-a)
  if v>r:r=v;m=c
  a=max(a,r)
  if a>=B:break
 if not q:H[b]=(d,(r>=B)+2*(r<=o),r,m)
 return r
def ev(b):return sum(T[p][i]if p.isupper()else-T[p.upper()][119-i]for i,p in enumerate(b)if p not in' .')
def pick(g,seen):
 global n,L
 f=g['fen'].split();b=' '*20
 for R in f[0].split('/'):
  b+=' '
  for ch in R:b+='.'*int(ch)if ch.isdigit()else ch
  b+=' '
 b+=' '*20
 w=f[1]=='w'
 if not w:b=b[::-1].swapcase()
 def sq(u):
  k=21+(8-int(u[1]))*10+ord(u[0])-97
  return k if w else 119-k
 C=[]
 for u in g['legal_moves']:
  i=sq(u[:2]);j=sq(u[2:4]);x=list(b);p=x[i]
  if p=='K'and abs(i-j)==2:
   d=(j-i)//2;k=j+d
   while x[k]=='.':k+=d
   x[k]='.';x[i+d]='R'
  if p=='P'and x[j]=='.'and(i-j)%10:x[j+10]='.'
  x[i]='.';x[j]=u[4:].upper()or p
  c=''.join(x)[::-1].swapcase();C.append([u,c,ev(c)])
 for d in range(1,30):
  n=0;L=30000;a=-9e4;N=[]
  try:
   for u,c,t in C:
    v=-S(c,t,d-1,-9e4,-a)
    if c in seen:v=min(v,0)
    N.append((v,u,c,t))
    a=max(a,v)
  except X:break
  N.sort(key=lambda x:-x[0]);C=[x[1:]for x in N];
  if N[0][0]>3e4:break
 seen.add(C[0][1])
 return C[0][0]
def main():
 g=P('/game',{});s=set();k=0
 if len(H)>9**6:H.clear()
 while g.get('status')!='done':
  if g['game']!=k:k=g['game'];s=set()
  if g['status']=='your_move':g=P('/move',{'game':k,'move':pick(g,s)})
  else:g=P('/game',{})
main()
