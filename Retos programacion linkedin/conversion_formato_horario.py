horario_formato12h = input("Ingrese la hora en formato hh:mm AM/PM: ")
horas_24h = int(horario_formato12h[0:2])
if horario_formato12h[-1:-3:-1].lower() == "mp":
    horas_24h += 12
horario_formato24h = horario_formato12h.replace(horario_formato12h[0:2],str(horas_24h))
print(horario_formato24h[0:5])