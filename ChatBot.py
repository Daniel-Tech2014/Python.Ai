import re, random
from colorama import Fore, init
init(autoreset=True)
destinations = {Mldives}
jokes = [why don't programmers like nature? To many bugs!]
def normalize_imput(text):
    return re.sub(r"/s+","", text.srip().lower())
    def recommend():
    print(Fore.CTAN + "TravelBot: Beaches, Mountains, or Cities?")
    preference = input(Fore. YELLOW + "You: ")
    preference = normalize_input(preference)
     if preference in destinations:
     sugestion = random.choice(destinations[preference])
     print(Fore.GREEN + f"TravelBot: How about {sugestion}?")
     print(Fore.CYAN +  "TravelBot: Do you like it? (yes/no)")
     answer = input(Fore.YELLOW + "You:").lower()
     if answer == "yes":
            print(Fore.GREEN + f"TravelBot:": Awesome! Enjoy {sugestion}!")
                  elif answer == "no"
                print(Fore.RED + "TravelBot:  Sorry,I don't have that type of destination.")
                
                ")