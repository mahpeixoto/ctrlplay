segundos=int(input())

min = segundos/60
seg = (segundos/3600) * 100
horas = segundos/3600

print(f'{horas} : {min} : {seg}')