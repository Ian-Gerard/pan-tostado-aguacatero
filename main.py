def main():
    print("greeting") #WIP
    while True:
    # Menu interactivo para acceder a todas las funciones del programa.
        user_input= input("""Select an option: 
 _____________________________________________
|
|1): Peak hour traffic volume
|
|2): Daily Traffic volume
|
|3): Weather related accidents
|
|4): Shared Ride Demand
|
|5):Exit
|
|_____________________________________________: """)
        
    #Es importante que las funciones sean llamadas desde su propio archivo.
    #Acción ocurrida dependiendo del input:
        match user_input:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Goodbye :)") #Rompe el while loop
                break
main()
