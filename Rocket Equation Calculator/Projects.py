import math

print("Rocket Equation Calculator")
print("Version 1.0")
print("Created by Eyad")
print("--------------------------")

print("Enter the symbol of the Quantity You would Like to measure")
print("Ex: Delta-v,m0,mf,ISP,and g0")
print("Type help to understand the symbols or Type quit to exit")

g0 = 9.80665

symbol = input("Symbol: ")
symbol=symbol.lower()

if symbol == "help":
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("Delta-v, the change in velocity that an object (such as a spacecraft or rocket) needs or can "
          "achieve after applying a force.")
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("ISP, otherwise known as the specific impulse,is the measure of how efficiently a rocket "
          "engine uses fuel. It represents how much thrust is produced per unit of propellant")
    print("consumed, measured in seconds")
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("g0, The standard acceleration due to Earth's gravity at sea level, equal to 9.80665 m/s². "
          "It is used to convert specific impulse into exhaust velocity.")
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("ln, also known as natural logarithm,Is the mathematical function that describes exponential "
          "relationships. In the rocket equation, it represents how changes in mass ratio affect "
          "achievable delta-v.")
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("m0, (Initial mass) Is the total mass of the rocket before the burn begins, including fuel,"
          " structure, engines, and payload.")
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("m_f, (Final mass) Is the mass of the rocket after the burn is complete, with fuel removed "
          "or mostly consumed. It includes the dry mass and payload.")
    print("--------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------")
    print("m0/m_f, (Mass ratio) The ratio between the rocket's starting mass and its final mass."
          " It shows how much of the rocket's mass is propellant compared to what remains after burning.")

elif symbol == "delta-v" or symbol == "deltav":

    ISP=input("Enter Specific Impulse(ISP) of your engine(in seconds):  ")
    ISP=float(ISP)

    initial_mass=input("What is the Initial mass of the Rocket: ")
    initial_mass=float(initial_mass)

    final_mass=input("What is the Final mass of the Rocket: ")
    final_mass=float(final_mass)

    if final_mass >= initial_mass:
        print("Error: Final mass must be less than initial mass.")
        exit()

    delta_v = ISP * g0 * math.log(initial_mass / final_mass)
    delta_v=round(delta_v,2)

    print(f"Your Change in Velocity(Delta-v) is {delta_v} m/s")


elif symbol == "m0":
    ISP = input("Enter Specific Impulse(ISP) of your engine(in seconds):  ")
    ISP = float(ISP)
    final_mass = input("What is the Final mass of the Rocket: ")
    final_mass = float(final_mass)
    delta_v= input("What is the Change in Velocity(Delta-v) of your engine: ")
    delta_v = float(delta_v)
    initial_mass = final_mass * math.exp(delta_v / (ISP * g0))
    initial_mass = round(initial_mass, 2)
    print(f"The Initial Mass of the Rocket is {initial_mass} kg ")
    if final_mass >= initial_mass:
        print("Error: Final mass must be less than initial mass.")
        exit()
elif symbol == "mf" or symbol == "m_f":

    ISP = input("Enter Specific Impulse(ISP) of your engine(in seconds):  ")
    ISP = float(ISP)

    initial_mass = input("What is the Initial mass of the Rocket: ")
    initial_mass = float(initial_mass)

    delta_v = input("What is the Change in Velocity(Delta-v) of your engine: ")
    delta_v = float(delta_v)


    final_mass = initial_mass / math.exp(delta_v / (ISP * g0))
    final_mass = round(final_mass, 2)

    print(f"The Final Mass of the Rocket is {final_mass} kg")


elif symbol == "isp" or symbol == "specific impulse" or symbol == "specific_impulse":
    initial_mass = input("What is the Initial mass of the Rocket: ")
    initial_mass = float(initial_mass)

    final_mass = input("What is the Final mass of the Rocket: ")
    final_mass = float(final_mass)

    delta_v = input("What is the Change in Velocity(Delta-v) of your engine: ")
    delta_v = float(delta_v)

    if final_mass >= initial_mass:
        print("Error: Final mass must be less than initial mass.")
        exit()

    ISP = delta_v / (g0 * math.log(initial_mass / final_mass))
    ISP=round(ISP, 3)

    print(f"The specific Impulse of the engine is {ISP} seconds")


elif symbol == "g0":
    print(f"Standard gravity (g0) is {g0} m/s²")

elif symbol == "quit":
    print("Goodbye")
    exit()

else:
    print("Please enter a valid symbol")
    exit()

























