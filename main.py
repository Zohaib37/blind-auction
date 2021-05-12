from replit import clear
import art

print(art.logo)
print("Welcome to the Secret Auctions Program\n")
to_continue = ""
auction = {}

while to_continue != "no":
  name = input("What's your name? ")
  bid = int(input("What's your bid? $"))
  auction[name] = bid
  to_continue = input("Are there any other bidders in the room? Type 'yes' or 'no.' ")
  if to_continue == "yes":
    clear()

highest = 0
winner = ""
for key in auction:
  if auction[key] > highest:
    highest = auction[key]
    winner = key
print(f"\nThe winner is {winner} with a bid of ${highest}.")

