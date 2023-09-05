#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_path = "Input/Names/invited_names.txt"
letter_path = "Input\Letters\starting_letter.txt"

with open(name_path, "r") as n:
    names = [name.strip() for name in n.readlines()]

with open(letter_path, "r") as l:
    letter_template = l.read()

for na in names:
    personalized_letter = letter_template.replace("[name]", na)

    with open(f"Output/ReadyToSend/letter_for_{na}.txt", "w") as send:
        send.write(personalized_letter)


