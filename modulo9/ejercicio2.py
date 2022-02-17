def mision(horaLazamiento, tiempoDeVuelo, destino, tanque_extra, tanque_principal):
    return f"""
    Destino a {destino}
    Total tiempo de viaje: {horaLazamiento + tiempoDeVuelo} minutes
    Total Disel Restante: {tanque_extra + tanque_principal} gallons
    """

print(mision(14, 51, "luna", 200000, 300000))

# Escribe tu nueva función de reporte considerando lo anterior

def mision2(destination, *minutes, **DepositoConbustible):
   #print(minutes)
   #print(DepositoConbustible)
    return f"""
    Destino a {destination}
    Total tiempo de viaje: {sum(minutes)} minutes
    Total Disel Restante: {sum(DepositoConbustible.values())}
    """

print(mision2("Luna", 10, 15, 51, tanque_principal=300000, tanque_extra=200000))




def mision3(destination, *minutes, **kwars):
    print(kwars)
    main_report = f"""
    Destino a {destination}
    Total tiempo de viaje: {sum(minutes)} minutes
    Total Disel: {sum(kwars.values())}
    """
    for tanque, litros in kwars.items():
        main_report += f"{tanque} Tanque --> {litros}\n"
    return main_report

print(mision3("Luna", 8, 11, 55, principal=300000, extra=200000))


