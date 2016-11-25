# An adventure game
health  = 5
from random import randint

def room1():
    global health
    print("You find yourself in a dark mysterious dungeon , but you realise that some thing is wiggling underneith your skin!")
    print("Anyway... You get up and start walking and you see two red glowing doors with a note on the ground, you sprint toward the doors.you get a sudden pain stinging un your stomach")
    room2()

def room2():
    print("As you approach the two doors,you see a big ogre standing near the second door you quickly dash to the huge rock right next to you but you dont know what to do next")
    print("A. Do you run as fast as you can to door one?")
    print("B. Do you fling rocks at the ogre to distract him?")
    answer = input("Which do you choose? A or B:")

    if answer.lower() == "a":
        print("The ogre notices and you get smashed up by his hammer.")
        print ("game over,you lose.")
        room1()
    if answer.lower() == "b":
        print("You distract the ogre and he walks off you quickly go to room three.")
        room3()

def room3():
    print("as you open the door there is a huge crate behind it filled with guns,crisps,cakes,and new clothes and a backpack")
    print("A.Do you take some of the stuff in the crate")
    print("B.Do you just take clothes and one gun")
    print("C.Do you just take everthing even the crate")
    answer  = input("What will you choose? A or B or C:")

    if answer.lower() == "a":
        print ("you go to the next room peacefully")
        print ("great next room")
        room4()

    if answer.lower() == "b":
        print("you accidently shot yourself in the head when reloading the rifle")
        print("game over you lose")
        room1()

    if answer.lower() == "c":
        print("you collapse and break your spine under all the pressure")
        print("you just got crushed game over")
        room1()

def room4():
    print("while your in the next room you see a very small midget selling potions and some sort of old books")
    print("he asks you if you want to be a mage?")
    print("HELL YEAH I DO")
    print("very well young sir")
    print("A.do you try and persuade the little midget to give you one")
    print("B.do you just kick the midget in the face and take the books and potions")
    print("C.do you just not say anything and walk off")
    answer = input("what will you do A or B or C:")

    if answer.lower() == "a":
         print("he shouts and says i only take gold coins")
         print("you get killed by the little midget")
         print("game over nice try")
         room1()

    if answer.lower() == "b":
         print("you kill the midget in one boot to the face and steal the stuff")
         print("you take the stuff and go to the next room")
         room5()

    if answer.lower() == "c":
         print("the midget wont let you go away and he traps you in a pit of snakes")
         print("you die due to all the venom running through your system")
         print("you died sorry")
         room1()


def room5():
    print("when you get insaide the next room,there is a huge triangular object with a missive eye in the middle of it")
    print("you see a bunch of people with metal masks on with three triangular shaped holes in them with sharp metal teeth")
    print("they start to chase you and you all of a sudden get invisable arms stretch out you back but you cant feel them they cut up and smash the people/mutants all over and you have been covered in blood")
    print("you hear a strange voice shout those are your secret arms and they only come out when your in danger")
    print("A.do you try and run up to the masive triangle and quistion it")
    print("B.do you smash your way through with the secret arms inside your back")
    answer = input("A or B:")

    if answer.lower() == "a":
         print("as you quistion the thing a secret passage opens up and you walk through")
         print("you get inside the huge triangle")
         room6()

    if answer.lower() == "b":
        print("you try to smash your way through and a huge rock falls on you and kills you immediatly")
        print("you died")
        room1()

def room6():
     print("as you creepily walk through you see a woman?")
     print("you say to the woman,what are youdoing down here")
     print("she says i got taken here a long long time ago")
     print("il help you if you want me to?")
     print("she says that would be awfully kind of you")
     print("no bother")
     print("you see a massive mutant with the triangular shaped head as the one your in now")
     print("you say its the same as the building?")
     print("A.do you use your secret arms to kill the man")
     print("B.do you try and attempt to get around the the thing?")
     answer = input("A or B")

     if answer.lower() == "a":
         print("you kill it succesfully game won")

    if answer.lower() == "b":
        print("you die peacfully when he crushes your heart with his own bare hands")
     
        
         

    
         
       
        
    
    
    

    
 

    

    
         

    
         
         
    
          

    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
