#Game Introduction

print("Welcome, Viget!\n")
print("My name is Boydie Maraj, and I am applying for the Winter 2020 Digital Analyst Apprenticeship position.\n\nI wanted to supplement my resume, cover letter, and article response with some additional materials... so I thought that I would create this simple game to show off some of my Python programming capabilities.\n\nI hope you enjoy! :)\n")

#Game variables
line_space = ("\n--------------------------------------")
health = 10

name = input("First, let's get some information. What is your name? ")
age = int(input("What is your age? "))

print(line_space)
print("\nPerfect. Thanks", name, "\nIt is really nice to meet you!")

if age >= 18:

    game_start = input("\nAre you ready to play? (yes/no) ").lower()
    if game_start == "yes":
        print(line_space)
        print("\nWonderful.\n\nYou are a lost 'Vigeter' and need to get back to your office.\n\nThis is a choose your own adventure game with many different endings.\nI hope you can explore all of them. Best of luck!")
        print("\nYou are starting with", health, "health.\n")
        
        #First Decision
        first_choice = input("First choice... left or right (left/right) ").lower()
        if first_choice == "left":
            
            #lake
            print(line_space)
            ans = input("\nYou follow the path to the left and reach a lake... Do you swim across or go around? (across/around)? ").lower()
            
            #Graveyard and cavern
            if ans == "around":
                print(line_space)
                print("\nYou went around and reached the other side of the lake.")
                ans = input("\nYou see a graveyard and a mysterious cavern. Which do you go to? (graveyard/cavern) ").lower()

                #Graveyard
                if ans == "graveyard": 
                    print(line_space)
                    print("\nYou approach the graveyard and read the first grave you see.\n\nIt says, ' Here lies", name,"'")
                    print("\nSuddenly, the ground begins to shake... You hear creatures from the beyond calling out to you. Hands reach from beneath the graves and pull you under the ground.")
                    print("\nYou lose all of your health.")
                    health = 0
                    
                    print("\nCurrent health:",health)
                    
                    if health <= 0:
                        print("\nYou lost.\nPlay again?")
                else: 
                    
                    #spooky cavern
                    print(line_space)
                    print("\nYou head towards the cavern. As you walk through the dimly-lit cavern, you see some light shining from the ceiling.")
                    ans = input("\nIt is shining on something below. Do you go to inspect the object or continue onwards? (inspect/continue) ").lower()
                    
                    #inspect
                    if ans == "inspect":
                        print(line_space)
                        print("\nAs you walk over and get a closer look, you step on a switch in the floor.\nA trap door opens beneath you.\n\nYou fall to the bottom and lose all of your health.")
                        health = 0
                        print("\nCurrent health:", health)
                        
                        if health <= 0:
                            print("\nYou lost.\nPlay again?")
                    else:
                        #VIGET
                        print(line_space)
                        print("\nYou continue along the path.\nYou see a light ahead.\n\n... you go through.\n\nYou emerge from the cavern and see the Viget sign!")
                        print("\nYou have found your way back!\n\nYou win!\n\nPlay again?")

            elif ans == "across": 
                
                print(line_space)
                print("\nYou managed to get across but were bit by a water snake and lost 5 health. OUCH!")
                health -= 5
                print("\nCurrent health:", health)
                if health <= 0:
                    print("\nYou lost.\nPlay again?")
                
                #House
                ans = input("\nYou come to a house. Do you go inside? (yes/no) \n")

                if ans == "yes":
                    print(line_space)
                    print("\nYou go to the house and are greeted by the owner.\nThe house is his restaurant.")
                
                    ans = input("\nHe asks you what you want to eat.\nWhich do you choose? (stew/cheese) ").lower()

                    if ans == "stew":
                        print(line_space)
                        print("\nYou burn your tongue on the stew and lose 5 health.")
                        health -= 5
                        print("\nCurrent health:", health)
                        
                        if health <= 0:
                            print("\nYou lost.\nPlay again?")
                    elif ans == "cheese":
                        print(line_space)
                        print("\nYou ate the cheese. It was more stinky than usual...\n\nYou pass out... and wake up to realize that you have been robbed and cannot pay for your food...\n")
                        print("\nYou stay indefinitely to work off your debts... and eat cheese.")
                        print("\nYou lost (sorta).\nPlay again?")

                else:
                     print(line_space)
                     print("\nWell that isn't very adventerous, now is it?\nYou lost.\nPlay again?")
            else:
                print("You lost.\nPlay again?")

        else:
            print(line_space)
            ans = input("\nYou take the path to the right and see a house and a river. Which do you go to? (river/house) ").lower()
            if ans == "house":

                #House
                print(line_space)
                print("\nYou go to the house and are greeted by the owner.\nThe house is his restaurant.")
                
                ans = input("\nHe asks you what you want to eat.\nWhich do you choose? (stew/cheese) ").lower()

                if ans == "stew":
                    print(line_space)
                    print("\nYou burn your tongue on the stew and lose 5 health.")
                    health -= 5
                    print("\nCurrent health:", health)
                    if health <= 0:
                        print("\nYou lost.\nPlay again?")
                    
                    print("\nYou see a nearby cavern and head towards it.As you walk through the dimly-lit cavern, you see some light shining from the ceiling.")
                    ans = input("\nIt is shining on something below. Do you go to inspect the object or continue onwards? (inspect/continue) ").lower()

                    if ans == "inspect":
                        print(line_space)
                        print("\nAs you walk over and get a closer look, you step on a switch in the floor.\nA trap door opens beneath you.\n\nYou fall to the bottom and lose all of your health.")
                        health = 0
                        print("\nCurrent health:", health)
                        
                        if health <= 0:
                            print("\nYou lost.\nPlay again?")
                    else:
                        print(line_space)
                        print("\nYou continue along the path.\nYou see a light ahead.\n\n... you go through.\n\nYou emerge from the cavern and see the Viget sign!")
                        print("\nYou have found your way back!\n\nYou win!")
                        print("\nPlay again?")
              
                elif ans == "cheese":
                    print(line_space)
                    print("\nYou ate the cheese. It was more stinky than usual...\n\nYou pass out... and wake up to realize that you have been robbed and cannot pay for your food...")
                    print("\nYou stay indefinitely to work off your debts... and eat cheese.")
                    print("\nYou lost (sorta).\nPlay again?")
                else:
                     print("\nYou lost.\nPlay again?")
            else:
                print(line_space)
                print("\nYou go to the river. As you get closer, your feet slip on the muddy riverbank and you fall in... losing 10 health.")
                health -= 10
                print("\nCurrent health:", health)
                if health <= 0:
                    print("\nYou lost.\nPlay again?")
    else:
        print(line_space)
        print("Okay... come back when you're ready to play!")

elif age >= 14:
    print(line_space)
    print("\nYou can play with adult supervision.\nRestart the program and enter in your parent's age.")
else:
    print(line_space)
    print("\nYou must be 14 years or older to play. You are not old enough to play...")
