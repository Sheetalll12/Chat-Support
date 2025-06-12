l bawliwhile True:
    name = input("Hi! please enter your character Senpie😎: ")
    print(f'Hi {name}, Welcome to our Anime Paradise Bot Services')
    print("How Can i help you in Anime Paradise")
    print(' Please select the desired option:\n')
    print(" 1.Help me pick an anime\n", "2.Membership and Subsripition\n", "3.Language Change\n","4.Issue With Payment\n","5.Feedback\n")
    choice = input("Please enter the option (1-5):")

    if choice == "1":
        print("When you don’t know what to watch, let your mood choose the remote.")
        print("Please Select your desired interest to watch")
        print("1.Romantic", "2. Comedy", "3.Thrilling", "4.Horror", "5.Adventures")
        sub_Choice = input("Please Select option (1-5): \n")
Shhetal
        if sub_Choice == "1":
            print("I gotta list amazing Romantic Anime curated for you only:\n")
            print("*.Your Lie in April \n"
                  "*.Toradora! \n"
                  "*.Clannad \n"
                  "*.Kaguya-sama \n"
                  "*.Horimiya \n"
                  "*.Fruits Basket(2019) \n"
                  "*.The Quintessential Quintuplets \n"
                  "*.Lovely★Complex \n"
                  "*.My Dress-Up Darling \n"
                  "*.ReLIFE \n")

        elif sub_Choice == "2":
            print("Mood for Comedy, hold your horses :)")
            print("*.Gintama \n"
                  "*.KonoSuba \n"
                  "*.Saiki Kusuo no Psi-nan (The Disastrous Life of Saiki K.) \n"
                  "*.Nichijou (My Ordinary Life) \n"
                  "*.Grand Blue \n"
                  "*.One Punch Man \n"
                  "*.Asobi Asobase \n"
                  "*.Hinamatsuri \n"
                  "*.Spy x Family \n"
                  "*.Detroit Metal City \n")

        elif sub_Choice == "3":
            print("Mood for Thrill?? We have Best of Best Thrilling Anime!!")
            print(
                "*. Death Note \n"
                "*.Attack on Titan \n"
                "*.Parasyte: The Maxim \n"
                "*.Code Geass \n"
                "*.Psycho-Pass \n"
                "*.Monster\n"
                "*.Erased .\n"
                "*.Tokyo Ghoul \n"
                "*.Future Diary (Mirai Nikki) \n"
                "*.Vinland Saga")

        elif sub_Choice == "4":
            print("Welcome to the dark side of anime—where the jump scares are real, the plots are twisted, and the psychological damage? Chef’s kiss.")
            print("Another:: Suspense + gore + final destination-style deaths.\n"
                  "Tokyo Ghoul\n"
                  "Parasyte\n"
                  "Higurashi no Naku Koro ni (When They Cry)\n"
                  "Shiki \n"
                  "Yamishibai\n"
                  "Elfen Lied\n"
                  "The Promised Neverland:Orphan kids\n"
                  "Hell Girl (Jigoku Shoujo)\n"
                  "Corpse Party: Tortured Souls.")

        elif sub_Choice == "5":
            print("Welcome to Adventure , Where others see danger, you see a story worth telling")
            print("Hunter x Hunter.\n"
                  "One Piece.\n"
                  "Made in Abyss.\n"
                  "Magi: The Labyrinth of Magic \n"
                  "Vinland Saga\n"
                  "Naruto / Naruto Shippuden \n"
                  "Samurai Champloo\n"
                  " The Rising of the Shield Hero")
        else:
            print("Invalid option. Please try again.")
    elif choice == "2":
        print ("Welcome to Membership and Scripition of Anime Paradise")
        print("We have 3 subscription for you ")
        print(f'✓ Paradise -> price: $99,\n * Stream on 1 device at a time \n * 5% off on selected products')
        print(f'✓ Mega Pradise -> price: $149,\n* Stream on upto 4 device at a time \n * Offline Veweing \n *10% off on selected products')
        print(f'✓ Ultimate Pradise -> Price $499 \n* Stream on upto 6 device at a time * Offline Veweing \n *15% off on selected products \n * Acsess Paradise Games' )
    elif choice == "3":
        print("For Language change ")
        print ("1. English, 2. Japanses 3.Hindi")
        Language = input("Please Select option (1-3): \n")
        if Language  == "1":
            print("Language change to English Sucessfully!")
        elif Language == "2":
            print("Language change to Japanese Sucessfully!")
        elif Language == "3":
            print("Language change to Hindi Sucessfully!")
        else:
            print("Invalid option. Please try again.")
    elif choice == "4":
        print("For the Payment related issues , Please write an Email: AnimePradise@gmail.com , will get back to you after 24-48 hours")
        print("Thank You for using Anime Pradise Service, Hope you a very wonderful Day!")
    elif choice == "5":
        feedback = input("Please let us know how can we improve.")
        print(feedback)
    else:
        print("Invalid option. Please try again.")
    continue_choice = input("Would you like to continue? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("\nThank you for visiting Anime Paradise! Sayonara, Senpai!")
        break
