#Input birthday date and print out how many seconds old
import datetime
print("Lets See How Many Days, Hours, and Second you lived in Mother Earth")

print("Enter Your Birthday Year")
Years =int(input("Years: "))

print("Enter Your Birthday Month") 
Months = int(input("Months: "))

print("Enter Your Day of Birth")
Days = int(input("Days: "))

Seconds = Years * 24 *60 *60 *365 + Months * 30 *60 + Days *60

print("You have lived in mother earth", Seconds, "Seconds chilling in this pandemic life")