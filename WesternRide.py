# Introduction
print()
print()
print("     ######################")
print("     |                    |")
print("     |     Western Ride   |")
print("     |                    |")
print("     ######################")
print()
print()

name = input("What is your name, outlaw?\n")
print("Howdy, " + name + ". Let's get the loot back to the homestead!")

print()
answer = input("Would you like to play Western Ride? (yes/no) ")

if answer == "yes":
#Start of game
    
    print("Well that's great, let's ride!")
    print()
    answer = input(
        "You're an outlaw on the run for robbing a bank! You reach a trail head. One leads to the forest and the other to the desert, which one do you take? (forest/desert) ")

    # PATH 1
    if answer == "forest":
        print("You ride your trusty steed on the path towards the forest but it begins to get dark.")
        print()
        answer = input("Do you stop and set up camp or keep going? (camp/go) ")

        if answer == "camp":
            print("You stop and begin to set up camp but the law catch up to you! Game Over.")
        elif answer == "go":
            print(
                "You continue on as it begins to get dark, using a lamp to light your way into the forest. As you ride into the forest you come upon an abandoned cabin. ")
            print()
            answer = input("Rest out at the cabin for the night or keep going? (cabin/go) ")

            if answer == "cabin":
                print(
                    "You tie your horse up and head inside to make a fire and rest for the night...You are then awoke by a man holding a revolver at your face.")
                print()
                answer = input("Raise your hands and surrender or attempt to take his gun? (surrender/gun) ")

                if answer == "surrender":
                    print(
                        "The man grabs your gun and ties you up, taking you to the sheriff to collect the bounty on your head. Game Over. ")
                elif answer == "gun":
                    print("You try and grab his gun but you're not quick enough, he shoots. Game Over. ")
                else:
                    print("That's not allowed partner, Game Over.")
            elif answer == "go":
                print("As you ride on into the forest you're attacked by a bear! ")
                print()
                answer = input("Shoot the bear or try to outrun it? (shoot/run) ")

                if answer == "shoot":
                    print(
                        "You shoot at the bear with your revolver, hitting it but it keeps charging and strikes you and your horse down. Game Over. ")

                elif answer == "run":
                    print(
                        "Your trusty steed is faster than most, outrunning the bear and and moving safely out the forest, heading into the prairie. ")
                    print()
                    answer = input(
                        "In the prairie you see two lawmen headed your way. Do you shoot first or hope they don't recognize you? (shoot/sneak) ")

                    if answer == "sneak":
                        print(
                            "As you try and sneak past them on the prairie trail, one of the recognizes you and they both draw their gun. Game Over. ")

                    elif answer == "shoot":
                        print(
                            "As they apporach, they recognize you but it's too late, being the gun slinging outlaw you are, you take them both out! ")
                        print()
                        answer = input(
                            "You ride on, getting closer to your hideout but being tired and exhausted from riding, you forget if it's a left or right to your homstead. Which one? (right/left) ")

                        if answer == "right":
                            print(
                                "You went the wrong way and ended up riding straight towards the sheriff and his deputies! Game Over. ")

                        elif answer == "left":
                            print(
                                "You made the right call and made it home with a whopping $100,000. Congratulations " + name + ", you win! ")
                        else:
                         print("That's not allowed partner, Game Over.")
                    else:
                     print("That's not allowed partner, Game Over.")
                else:
                 print("That's not allowed partner, Game Over.")
            else:
             print("That's not allowed partner, Game Over.")
        else:
         print("That's not allowed partner, Game Over.")

    # PATH 2
    elif answer == "desert":
        print(
            "You ride your trusty steed on the path into the desert but it begins to get dark. You notice an abandoned mine shaft up ahead ")
        print()
        answer = input("Keep going into the dark or stop and rest at the mine? (go/mine) ")

        if answer == "mine":
            answer = input(
                "You light a torch and head into the dark, dingy mine. before going in too deep, you find some old TNT, take it as it could be usefull in the future or leave it? (take/leave) ")

            if answer == "take":
                print(
                    "Bending down to grab the TNT off the ground, a spark from the torch drops and lands in the pile of old, unstable TNT, blowing the mine to smithereens. Game Over. ")

            elif answer == "leave":
                print(
                    "Holding a torch in your hand and knowing old TNT can be unstable, you decide it's not worth it and continue on. You find a nice spot and rest for a few hours till morning.")
                print()
                answer = input(
                    "Morning comes and you pack up your gear and hit the trail. While on the trail you have two choices, continue on the long path or take a short cut through town? (path/town) ")

                if answer == "town":
                    print(
                        "You want to get home quick so you take the short cut, bad choice, the townsfolk recognize you and get the sheriff, who arrests you on sight. Game Over. ")

                elif answer == "path":
                    print(
                        "You decide to play it safe and take the long route. You ride for hours until you come upon an overturned wagon on the path. ")
                    print()
                    answer = input("Do you stop and investigate or keep going? (stop/go) ")

                    if answer == "stop":
                        print(
                            "You hop off your horse and approach the wagon. As you walk towards it, you see movment inside and stop walking, unholstering your pistol. You point it at the wagon. ")
                        print()
                        answer = input("Do you just shoot or yell for the person to come out? (shoot/yell) ")

                        if answer == "yell":
                            print(
                                "You yell at whoever or whatever to reveal itself. Out come to bandits, long guns in hand pointing them at you. They tell you to drop your weapon and you do. They rob you and take your horse. Game Over. ")

                        elif answer == "shoot":
                            print(
                                "You start unloading into the wagon. Once you're all out, gun still smoking, you walk over to open the curtain on the wagon revealing two dead bandits who had set up an ambush. ")
                            print()
                            answer = input(
                                "You take some of their loot and continue on the trail. After an hour or two more of riding, you exit the desert and reach a pasture. In the pasture, you see the marshall, standing, waiting for you. You approach and hop of your horse. Shoot at him or talk? (shoot/talk)")

                            if answer == "shoot":
                                print(
                                    "You reach for your gone to shoot at the marshall but you aren't quick enough, you're shot in the chest. Game Over.")

                            elif answer == "talk":
                                print("The marshall gives you the option to be brought in warm or brought in cold. ")
                                print()
                                answer = input("Surrender or duel with the Marshall? (surrender/duel) ")


                                if answer == "surrender":
                                    print(
                                        "You lay down your weapons and raise your hands in the air, the Marshall walks over and cuffs you, off to jail you go. Game Over.")

                                elif answer == "duel":
                                    print(
                                        "You and the Marshall get into an intense stand off, both watching closley at one another and any movment. You quickly reach for your gun but before you could get a shot off the Marshall had already got you in the chest. Game Over")
                                else:
                                 print("That's not allowed partner, Game Over.")
                            else:
                             print("That's not allowed partner, Game Over.")
                        else:
                         print("That's not allowed partner, Game Over.")
                    else:
                     print("That's not allowed partner, Game Over.")
                else:
                 print("That's not allowed partner, Game Over.")
            else:
             print("That's not allowed partner, Game Over.")
        elif answer == "go":
            print(
                "You notice the mine but keep on going not wanting to stop. It grows darker and you begin to noice you are being followed. ")
            print()
            answer = input("You are surronded by a pack of coyotes! Do you run or shoot? (run/shoot) ")
            if answer == "run":
                print(
                    "you attempt to outrun them on your horse but the pack is too fast and there are too many of them. Your horse is bitten and falls, taking you down with him! You are eaten, Game Over.")

            elif answer == "shoot":
                print(
                    "You unholster your revolver and shoot in the air twice, scaring away the pack. However, it attracts the attenton of a bounty hunter who is after you. ")
                print()

                answer = input(
                    "Gun still in hand, you have to make the choice, shoot him or attempt to ride away? (shoot/ride) ")
                if answer == "ride":
                    print(
                        "You try and out run the bounty hunter but he keeps up, you have no where to run. Eventually your horse gets tired and the bounty hunter captures you. Game Over.")

                elif answer == "shoot":
                    print(
                        "With your gun already out, you know you have the upper hand, you take the shot and take out the bounty hunter. He falls off his saddle as his horse rides on. ")
                    print()

                    answer = input(
                        "Looking around seeing no one following you, you head back on the trail. You come upon an intersection. Due to being tired from not stopping to rest, you can't remember, left or right? (left/right) ")
                    if answer == "left":
                        print(
                            "You travel along the trail for hours, not realizing you chose the wrong path, you and your horse die due to exhaustion. Game Over. ")

                    elif answer == "right":
                        print(
                            "You ride along the path for another hour until you reach a prairie. You and your horse are exhausted from riding all night and you see someone has a camp set up not too far ahead. ")
                        print()

                        answer = input(
                            "Head over and ask if you can rest for a few hours or keep your head down and keep pushing? (rest/go) ")
                        if answer == "go":
                            print(
                                "You decided to make the foolish choice and continue on. Becoming dehydrated, hungry and tired, you and your horse don't make it far before collapsing, vultures fly overhead. Game Over.")
                        elif answer == "rest":
                            print(
                                "You decide it's best to give you and your horse a few hours rest. You ask the camper if it's okay and he says yes. You rest for a few hours and wake up to him having made you a meal.")
                            print()

                            answer = input(
                                "With you and your horse feeling fresh and ready, you thank the man and continue on. Right before making the final turn to head to your homestead, you're not sure if you're being followed. Go straight home, I'm being paranoid or take the long way? (home/longway) ")
                            if answer == "longway":
                                print(
                                    "Your gut feeling was right! You were being followed by the man from the camp. He noticed the money bags you had with you and thought following you could have led to more! You lead him away and loose him on the trail. You made the right call and made it home with a whopping $100,000. Congratulations " + name + ", you win!")
                            elif answer == "home":
                                print(
                                    "You decide to go straight home to hide the stolen cash. Unfortunately the man from the camp followed you and held you at gun point to steal your money. Game Over.")
                            else:
                             print("That's not allowed partner, Game Over.")
                        else:
                         print("That's not allowed partner, Game Over.")
                    else:
                     print("That's not allowed partner, Game Over.")
                else:
                 print("That's not allowed partner, Game Over.")
            else:
             print("That's not allowed partner, Game Over.")
        else:
         print("That's not allowed partner, Game Over.")
    else:
     print("That's not allowed partner, Game Over.")
elif answer == "no":
    print("That's too bad partner, maybe next time.")
else:
 print("That's not allowed partner, Game Over.")