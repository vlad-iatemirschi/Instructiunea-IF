xa=int(input("bile albe si mici sunt"))
xr=int(input("bile rosii si mici sunt"))
xv=int(input("bile verzi si mici sunt"))
ya=int(input("bile albe si mari sunt"))
yr=int(input("bile rosii si mari sunt"))
yv=int(input("bile verzi si mari sunt"))
xt=xa+xr+xv
yt=ya+yr+yv
print("in total sunt",xt+yt,"bile")
if xt>yt:
    print("sunt",xt,"bile mici")
if yt>xt:
    print("sunt",yt,"bile mari")
ta=xa+ya
tr=xr+yr
tv=xv+yv
if ta>tr and ta>tv:
    print("sunt",ta,"bile albe")
if tr>ta and tr>tv:
    print("sunt",tr,"bile rosii")
if tv>ta and tv>tr:
    print("sunt",tv,"bile verzi") 
if ta==tr==tv:
    print("sunt egale")                   