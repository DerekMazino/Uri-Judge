diasInicial=int(input())
years=int(diasInicial/365)
meses=int((diasInicial-years*365)/30)
dias=int(diasInicial-(years*365+meses*30))
print(str(years)+" ano(s)")
print(str(meses)+" mes(es)")
print(str(dias)+" dia(s)")