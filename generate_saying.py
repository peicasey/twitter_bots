import random

def getStanleySaying():
    origin = ["Traveling is tons of fun!",
              "Remember you can register for a study abroad.",
              "Any suggestions for where I travel next?"
              "I think technically according to Twitter TOS, I'm too young to have an account.",
              "Remember that time I broke into a pyramid?",
              "Ngl, traveling in a giant packet is actually terrible",
              "UPS is better than FedEx when it comes to moving giant flat children.",
              "I have traveled many international borders today!",
              "I am a child who is flat.",
              "I got a concussion when that board flattened me.",
              "Reminder that I am not actually affiliated with the Flat Stanley book series.",
              "Italy is great! Can't wait to head back one day :D"]

    option = random.randint(0, 11)

    return origin[option] + "\n\n- Stanley"


