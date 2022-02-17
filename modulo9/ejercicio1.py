def generate_report(tanque1, tanque2, tanque3):
    promedio = (tanque1 + tanque2 + tanque3) / 3
    return f""" Reporte de Combustible:
    Promedio: {promedio}%
    tanque1: {tanque1}%
    tanque2: {tanque2}%
    tanque3: {tanque3}% 
    """
#print(generate_report(80,100 , 100))
 
def promedio(*kwargs):
    total = sum(kwargs)
    items = len(kwargs)
    return total / items

 
 

def generate_report2(tanque1, tanque2, tanque3): 
    prom = promedio(tanque1, tanque2, tanque3) 

    return f"""Reporte de Combustible Con Funcion:
    promedio: {prom}%
    tanque1: {tanque1}%
    tanque2: {tanque2}%
    tanque3: {tanque3}% 
    """
print(generate_report2(80, 100, 100))
