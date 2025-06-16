while True:
    name = input("Hi! Please enter your character Senpai 😎: ")
    print(f'Hi {name}, welcome to our Anime Paradise Bot Services!\n')
    print("How can I help you in Anime Paradise?")
    print('Please select the desired option:\n')
    print("1. Help me pick an anime")
    print("2. Membership and Subscription")
    print("3. Language Change")
    print("4. Issue With Payment")
    print("5. Feedback")

    choice = input("Please enter the option (1-5): ")

    if choice == "1":
        print("\nWhen you don’t know what to watch, let your mood choose the remote.")
        print("Please select your interest:")
        print("1. Romantic")
        print("2. Comedy")
        print("3. Thrilling")
        print("4. Horror")
        print("5. Adventures")

        sub_Choice = input("Please select an option (1-5): ")

        if sub_Choice == "1":
            print("\n💖 Romantic Anime Recommendations:")
            print("• Your Lie in April\n• Toradora!\n• Clannad\n• Kaguya-sama\n• Horimiya")
            print("• Fruits Basket (2019)\n• The Quintessential Quintuplets\n• Lovely★Complex")
            print("• My Dress-Up Darling\n• ReLIFE")

        elif sub_Choice == "2":
            print("\n🤣 Comedy Anime Recommendations:")
            print("• Gintama\n• KonoSuba\n• The Disastrous Life of Saiki K.\n• Nichijou (My Ordinary Life)")
            print("• Grand Blue\n• One Punch Man\n• Asobi Asobase\n• Hinamatsuri")
            print("• Spy x Family\n• Detroit Metal City")

        elif sub_Choice == "3":
            print("\n😱 Thrilling Anime Recommendations:")
            print("• Death Note\n• Attack on Titan\n• Parasyte: The Maxim\n• Code Geass")
            print("• Psycho-Pass\n• Monster\n• Erased\n• Tokyo Ghoul\n• Future Diary")
            print("• Vinland Saga")

        elif sub_Choice == "4":
            print("\n👻 Horror Anime Recommendations:")
            print("• Another\n• Tokyo Ghoul\n• Parasyte\n• Higurashi no Naku Koro ni")
            print("• Shiki\n• Yamishibai\n• Elfen Lied\n• The Promised Neverland")
            print("• Hell Girl (Jigoku Shoujo)\n• Corpse Party: Tortured Souls")

        elif sub_Choice == "5":
            print("\n🌍 Adventure Anime Recommendations:")
            print("• Hunter x Hunter\n• One Piece\n• Made in Abyss\n• Magi: The Labyrinth of Magic")
            print("• Vinland Saga\n• Naruto / Naruto Shippuden\n• Samurai Champloo")
            print("• The Rising of the Shield Hero")

        else:
            print("Invalid sub-option. Please try again.")

    elif choice == "2":
        print("\n💳 Welcome to Membership and Subscription of Anime Paradise!")
        print("We have 3 subscription tiers for you:")
        print("✓ Paradise - $99:\n  • Stream on 1 device\n  • 5% off on selected products")
        print("✓ Mega Paradise - $149:\n  • Stream on up to 4 devices\n  • Offline viewing\n  • 10% off on selected products")
        print("✓ Ultimate Paradise - $499:\n  • Stream on up to 6 devices\n  • Offline viewing\n  • 15% off\n  • Access to Paradise Games")

    elif choice == "3":
        print("\n🌐 Language Change Options:")
        print("1. English\n2. Japanese\n3. Hindi")
        language = input("Please select an option (1-3): ")
        if language == "1":
            print("Language changed to English successfully!")
        elif language == "2":
            print("Language changed to Japanese successfully!")
        elif language == "3":
            print("Language changed to Hindi successfully!")
        else:
            print("Invalid language option. Please try again.")

    elif choice == "4":
        print("\n💸 Payment Support:")
        print("For payment-related issues, please email us at AnimeParadise@gmail.com")
        print("We'll get back to you within 24–48 hours.")
        print("Thank you for using Anime Paradise Services!")

    elif choice == "5":
        feedback = input("\nPlease let us know how we can improve: ")
        print("Thanks for your feedback! We appreciate your time. 💌")
        print(f'You said: "{feedback}"')

    else:
        print("Invalid option. Please enter a number between 1 and 5.")

    continue_choice = input("\nWould you like to continue? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("\nThank you for visiting Anime Paradise! Sayonara, Senpai 🌸👋")
        break
