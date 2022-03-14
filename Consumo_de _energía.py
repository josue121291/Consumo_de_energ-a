consumo_energia = {
    'Coca Codo Sinclair': {
        'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
        'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
    },
}
op = 0
def menu():
    print()
    print()
    print("OPCIONES DISPONIBLES:")
    print('<1> TOTAL DE MWH POR DICHA PLANTA Y CIUDAD.')
    print('<2> TOTAL DE MWH POR CADA PLANTA')
    print('<3> TOTAL DE DINERO RECAUDADO POR CADA REGION')
    print('<4> SALIR')

while op!= 1:
    menu()
    ops = int(input('INGRESE UNA OPCION:'))
    if ops == 1 :
      while op != 1:
          print()
          print('PLANTAS: COCA CODO SINCLAIR / SOPLADORA')
          print()
          print('CIUDADES: GUAYAQUIL / QUITO / LOJA')
          print()


          p = str(input('Ingrese el nombre de la planta(mayus): '))
          c = str(input('Ingrese el nombre de la ciudad(mayus): '))
          if p == 'COCA CODO SINCLAIR' and c =='QUITO':
            #COCA QUITO
            tarifa_coca_quito = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
            print('Consumo total:', sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos']),'MWh')
            break 
         

          elif p == 'COCA CODO SINCLAIR' and c == 'GUAYAQUIL':
            #COCA GUAYAQUIL
            tarifa_coca_guayaquil = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']
            print('Consumo total:', sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']),'MWh')
            break
         

          elif p == 'SOPLADORA' and c == 'GUAYAQUIL':
            #SOPLADORA GUAYAQUIL
            tarifa_sopladora_guayaquil = consumo_energia['Sopladora']['Guayaquil']['tarifa']
            print('Consumo total:', sum(consumo_energia['Sopladora']['Guayaquil']['consumos']),'MWh')
            break
          

          elif p == 'SOPLADORA' and c == 'QUITO':
            #SOPLADORA QUITO
            tarifa_sopladora_quito = consumo_energia['Sopladora']['Quito']['tarifa']
            print('Consumo total:', sum(consumo_energia['Sopladora']['Quito']['consumos']),'MWh')
            break
          

          elif p == 'SOPLADORA' and c == 'LOJA':
            #SOPLADORA LOJA
            tarifa_sopladora_loja = consumo_energia['Sopladora']['Loja']['tarifa']
            print('Consumo total:', sum(consumo_energia['Sopladora']['Loja']['consumos']),'MWh')
            break
          

          else:
           print('¡DATOS ERRONEOS!\nINGRESE NUEVAMENTE LOS DATOS DE LA PLANTA Y LA CIUDAD')
      

    elif ops == 2:

      while op !=2:
        print()
        print('QUITO / GUAYAQUIL / LOJA')
        print()

          
        plantas = {
        'Quito': ('Coca Codo Sinclair', 'Sopladora'),
        'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
        'Loja': ('Sopladora')
        }
        c = str(input('Ingrese el nombre de la ciudad(mayus): '))
        if c == 'QUITO':
            print('Las plantas que producen energia en esta ciudad son', plantas['Quito'])
            print('COCA CODO SINCLAIR:', sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos']),'MWh')
            print('SOPLADORA:', sum(consumo_energia['Sopladora']['Quito']['consumos']),'MWh')
            break
        elif c == 'GUAYAQUIL':
            print('Las plantas que producen energia en esta ciudad son', plantas['Guayaquil'])
            print('COCA CODO SINCLAIR:', sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']),'MWh')
            print('SOPLADORA:', sum(consumo_energia['Sopladora']['Guayaquil']['consumos']),'MWh')
            break    
        elif c == 'LOJA':
            print('Las plantas que producen energia en esta ciudad son', plantas['Loja'])
            print('SOPLADORA:', sum(consumo_energia['Sopladora']['Loja']['consumos']),'MWh')
            break
        else:
             print('¡LA CIUDAD DE LA QUE DESEA OBTENER INFORMACION NO ENTREGA ENERGIA!')
        
    elif ops == 3:
     while op!=4:
        print()
        print('REGIONES: COSTA / SIERRA / ORIENTE')
        print()
        informacion = {
        'costa': ('Guayaquil', 'Manta'),
        'sierra': ('Quito', 'Ambato', 'Loja'),
        'oriente': ('Tena', 'Nueva Loja')
        }
        r = str(input('Ingrese el nombre de una region(mayus): '))
        if r == 'SIERRA':
              q_c_a = sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos'])
              q_c_b = sum(consumo_energia['Sopladora']['Quito']['consumos'])
              q_t_a = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
              q_t_b = consumo_energia['Sopladora']['Quito']['tarifa']
              l_c_a = sum(consumo_energia['Sopladora']['Loja']['consumos'])
              l_t_a = consumo_energia['Sopladora']['Loja']['tarifa']
              print('LOS INGRESOS DE LA REGION SIERRA:', '$',((q_c_a*q_t_a) + (q_c_b*q_t_b)) + (l_c_a*l_t_a))
              break
        elif r == 'COSTA':
             g_c_a = sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])
             g_c_b = sum(consumo_energia['Sopladora']['Guayaquil']['consumos'])
             g_t_a = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']
             g_t_b = consumo_energia['Sopladora']['Guayaquil']['tarifa']
             print('LOA INGRESOS DE LA REGION COSTA:',((g_c_a * g_t_a) + (g_c_b * g_t_b)))
             break
        else :
            print('LA REGION ASIGNADA NO CONSTA EN EL SISTEMA.')

    elif ops == 4:
        quit()