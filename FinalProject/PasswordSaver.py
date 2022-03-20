import csv
import sys

#The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


#The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

#The encryption key for the caesar cypher
encryptionKey = 16

#Caesar Cypher Encryption
def passwordEncrypt (unencryptedMessage, key):

    #We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)



while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Delete a password from the list.")
    print(" 7. Replace old password with new password.")
    print(" 8. Quit program")
    print("Please enter a number (1-8)")
    choice = input()

    if(choice == '1'): #Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'): #Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

    ##### YOUR CODE HERE ######
        for i in range(len(passwords)):  # this looks through the entire list of passwords
            if passwordToLookup == passwords[i][0]:  # This checks if the Website you chose is in the list.
                print(passwords[i][1])  # This prints the encrypted password
                print("Please enter the encryption key.")  # I know the lesson did not ask for it, but I figured I would add another layer of security.
                decryptkey = int(input())  # asks for an interger for the key.
                if decryptkey == encryptionKey:  # checks if the decrypt key matches the encryptionKey.
                    decryptedpassword = passwordEncrypt(passwords[i][1], -16)  # decrypts the password if the above is true.
                    print(decryptedpassword)  # prints the decrypted password.
                else:
                    print("That is incorrect.")  # else, it just kicks you back if it is incorrect.
            else:
                i +=1
                if i >= len(passwords):
                    print("That is not in the list.")
    #You will need to find the password that matches the website
        #You will then need to decrypt the password

        #
        #1. Create a loop that goes through each item in the password list
        #  You can consult the reading on lists in Week 5 for ways to loop through a list
        #
        #2. Check if the name is found.  To index a list of lists you use 2 square backet sets
        #   So passwords[0][1] would mean for the first item in the list get it's 2nd item (remember, lists start at 0)
        #   So this would be 'XqffoZeo' in the password list given what is predefined at the top of the page.
        #   If you created a loop using the syntax described in step 1, then i is your 'iterator' in the list so you
        #   will want to use i in your first set of brackets.
        #
        #3. If the name is found then decrypt it.  Decrypting is that exact reverse operation from encrypting.  Take a look at the
        # caesar cypher lecture as a reference.  You do not need to write your own decryption function, you can reuse passwordEncrypt
        #
        #  Write the above one step at a time.  By this I mean, write step 1...  but in your loop print out every item in the list
        #  for testing purposes.  Then write step 2, and print out the password but not decrypted.  Then write step 3.  This way
        #  you can test easily along the way.
        #


        ####### YOUR CODE HERE ######


    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()
        # This forces the user to make there password more secure by being over 5 characters (I picked that at random)
        # it also sees if it is all lowercase, all letters and numbers, all letters, or even if it is all uppercase.
        # if one of the options is not true, it forces the user to reeneter the password, and then checks it all again.
        while len(unencryptedPassword) <= 5 and unencryptedPassword.islower() and unencryptedPassword.isalpha and unencryptedPassword.isalnum() and unencryptedPassword.isupper():
            if len(unencryptedPassword) <= 5:
                print("That password is shorter than 5 letters, it will better if it is longer.")
                unencryptedPassword = input()
            if unencryptedPassword.islower():
                print("You should include at least one uppercase letter.")
                unencryptedPassword = input()
            if unencryptedPassword.isupper():
                print("You should not have all uppercase letters.")
                unencryptedPassword = input()
            if unencryptedPassword.isalpha():
                print("Adding a number or two can make your password safer.")
                unencryptedPassword = input()
            if unencryptedPassword.isalnum():
                print("Adding a special character can make your password more difficult to crack.")
                unencryptedPassword = input()
        print("That password is quite strong")
            ####### YOUR CODE HERE ######
        encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)  # calls the encryptedPassword function on the entered info.
        info = [website, encryptedPassword]  # saves the values to the info keyword.
        passwords.append(info)  # adds the info to the end of the passwords list.
        #You will need to encrypt the password and store it in the list of passwords

        #The encryption function is already written for you
        #Step 1: You can say encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)]
        #the encryptionKey variable is defined already as 16, don't change this
        #Step 2: create a list of size 2, first item the website name and the second item the password.
        #Step 3: append the list from Step 2 to the password list


        ####### YOUR CODE HERE ######

    if(choice == '4'): #Save the passwords to a file
            savePasswordFile(passwords,passwordFileName)


    if(choice == '5'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))


    if(choice == '6'):
        print("Please select the website that has the password you want to delete.")
        for keyvalue in passwords:  # I figured I would just reuse the code that was used to list the websites above.
            print(keyvalue[0])
        passwordToLookup = input()
        for i in range(len(passwords)):  # I also reused some code from the look up the passwords code.
            if passwordToLookup == passwords[i][0]:  # checks for the password
                print("Are you sure you want to delete it?")  # asks the user if they actually want to delete the website.
                print(" 1. Yes")
                print(" 2. No")
                answer = input()  # user picks one of the above choices.
                if answer == "1":  # if the user picks "1" then the item is deleted, if they pick "2" it kicks them back to the menu.
                    del passwords[i]  # deletes the website and password, by iterating to the particular list in the list.
            else:
                i += 1  # if the iteration doesn't match, then it ups it by one until it does.
                if i >= len(passwords):
                    print("That is not on the list.")
    if(choice == '7'):
        print("Please select the website that you want to change the password on.")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()
        for i in range(len(passwords)):  # I also reused some code from the look up the passwords code.
            if passwordToLookup == passwords[i][0]:
                print("Please enter the old password.")  # I figured I would add a safeguard to make sure you know the password.
                OldPassword = input()
                if OldPassword == passwordEncrypt(passwords[i][1], -16):  # checks if what you entered matches the websites decrypted password.
                    print("Please enter the new password.")
                    Newpassword = input()  # Adds the new password.
                    passwords[i][1] = passwordEncrypt(Newpassword, encryptionKey)  # replaces old password with new one.
                else:
                    print("That is incorrect please try again.")
            else:
                i += 1
                if i >= len(passwords):
                    print("That is not in the list.")
    if(choice == '8'):  #quit our program
        sys.exit()

    print()
    print()
