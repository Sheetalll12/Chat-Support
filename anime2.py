import random
while True:
    try:
        name = input("Hi! Please enter your character, Senpai 😎: ")
        print(f'Hi {name}, welcome to our Anime Paradise Bot Services!\n')
        print("How can I help you in Anime Paradise?")
        def Choice_Menu():
            return f' 1. Help me pick an anime,\n 2. Membership and Subscription,\n 3. Language Change, \n 4. Issue With Payment, \n 5. Feedback'
        print(Choice_Menu())
        Choice_Menu = input("Select it")
        if Choice_Menu == "1":
            print("Hey Do you have any mood Buddy???, No Prob buddy i've got your back i have some amazing choice please Let me your type\n Movie or Web Series")
            def interest():
                return f"1. Movie 2. Web Series"
            print(interest())
            interest = input("Please Select your Choice:  ")
            if interest == "1":
                print("We have 1.Romantics, 2.Comedy, 3.Horror" )
                jk = input("Please Select your genre:")
                if jk == "1":
                    print("If you are single then this is dream for you or if you are mingle then it is time make your bond strong")
                    Romantics_anime = ["your Name.", "Weathering with You", "I Want to Eat Your Pancreas"]
                    Rom_Anime = random.choice(Romantics_anime)
                    print(Rom_Anime)
                    if Rom_Anime == "Your Name. ":
                        print("Rating - 8.9/10 \n Platform - Cruncyroll / Netflix \n Released on - 2016 \n Duration - 1h 50mind")
                    elif Rom_Anime == "Weathering with You":
                        print("Rating - 7.5 / 10 \n Platform - Cruncyroll / Prime Video \n Released on - 2019 \n Duration - 1h 54mins")
                    elif Rom_Anime == "I Want to Eat Your Pancreas":
                        print("Rating - 8.1 / 10 \n Platform - Cruncyroll / Netflix \n Released on - 2018 \n Duration - 1h 48mins")
                elif jk == "2":
                    print("Oh!! you have selected for Comedy")
                    Comedy_Anime=["Coco","Soul","Ratatouille","Monsters University","Surf's Up","Finding Nemo","Cloudy with a Chance of Meatballs"]
                    Com_Anime =random.choice(Comedy_Anime)
                    print(Com_Anime)
                    if Com_Anime == "Coco":
                        print("Rating: 8.4/10 \n Platform: Disney+ \n Released on -2017 \n Duration: 1 hr 45 mins")
                    elif Com_Anime == "Soul":
                        print("Rating: 8.0/10 \n Platform: Disney+ \n Released on -2020 \n Duration: 1 hr 40 mins")
                    elif Com_Anime == "Ratatouille":
                        print("Rating: 8.1/10,\n Platform: Disney+,\nReleased on -2007 \n Duration: 1 hr 51 mins")
                    elif Com_Anime =="Monsters University":
                        print("Rating: 7.2/10 \n Platform: Disney+ \nReleased on -2013\n Duration: 1 hr 44 mins")
                    elif Com_Anime ==  "Surf's Up":
                        print("Rating: 6.7/10 \n Platform -Amazon Prime / Netflix \n Released -2007 \n Duration: 1 hr 25 mins")
                    elif Com_Anime == " Finding Nemo":
                        print("Rating: 8.2/10 \n Platform: Disney+ \n Released -2003 \n Duration: 1 hr 40 mins")
                    elif Com_Anime == "Cloudy with a Chance of Meatballs":
                        print("Rating: 6.9/10 \n Platform: Netflix / Amazon Prime \n Released - 2009 \n Duration: 1 hr 30 mins ")
                elif jk == "3":
                    print("Are we seriously, cause fear is only the Beginning")
                    Horror_Anime = ["Perfect Blue","Paprika","Vampire Hunter D: Bloodlust","Belladonna of Sadness","The Empire of Corpses"]
                    Hor_Anime = random.choice(Horror_Anime)
                    print(Hor_Anime)
                    if Hor_Anime == "Perfect Blue":
                        print("Rating: 8.6/10 \nPlatform: Amazon Prime / YouTube \n Released on -1998 \nDuration: 1 hr 21 mins")
                    elif Hor_Anime =="Paprika":
                        print("Rating: 7.7/10 \nPlatform: Netflix \n Released on -2006 \nDuration: 1 hr 30 mins")
                    elif Hor_Anime == "Vampire Hunter D: Bloodlust":
                        print("Rating: 7.6/10 \nPlatform: Amazon Prime, YouTube \nReleased -2000 \nDuration: 1 hr 42 mins")
                    elif Hor_Anime == "Belladonna of Sadness":
                        print("Rating: 7.4/10 \nPlatform -YouTube \nReleased -1973 \nDuration: 1 hr 26 mins")
                else:
                    print("Invalid input, Please Select the Correct the choice")
            elif interest == "2":
                print("Ooooh, you're an anime web series soul too?😎 Respect. Welcome to the binge-watching dojo!😝")
                print("Please Select Your Mood: 1.Adventure🤺 2.Comedy😂 3.Horror😱 4.Action🔫 5.Fantasy🎭")
                ik = input("Pleaseeee the make your Choice: (1-5)")
                if ik == "1":
                    print("Adventure, huh? Bro’s ready to risk emotional damage, trauma arcs, and god-tier betrayals—just for plot. I respect that.")
                    Adv_Anime = [" Alice in Borderland","Midnight Diner: Tokyo Stories","Switched (スイッチ)","Followers","Erased"]
                    adv_ani = random.choice(Adv_Anime)
                    print(adv_ani)
                    if adv_ani == "Alice in Borderland":
                        print("Rating: 8.2/10 \n Platform: Netflix \n Release Date:2020\nDuration: 2 seasons, ~50 min/ep")
                    elif adv_ani == "Midnight Diner: Tokyo Stories":
                        print("Rating: 8.4/10 \nPlatform: Netflix\nRelease Date: 2009\nDuration: 5 seasons, ~25 min/ep")
                    elif adv_ani == "Switched (スイッチ)":
                        print("Rating: 7.5/10\n Platform: Netflix\nRelease Date:2018\nDuration: 6 episodes, ~40 min/ep")
                    elif adv_ani == "Followers":
                        print(" Rating: 6.7/10 \nPlatform: Netflix\nRelease Date - 2020\nDuration: 9 episodes, ~45 min/ep")
                    elif adv_ani == " Erased":
                        print("Rating: 7.9/10\nPlatform: Netflix\nRelease Date-2017\nDuration: 12 episodes, ~30 min/ep")
                elif ik == "2":
                    print("Ohh Comedy Mood? No problem we make you laugh at loud!!")
                    Comeddy_Anime = ["Kantaro: The Sweet Tooth Salaryman","The Naked Director","Good Morning Call","Samurai Gourmet","Ossan’s Love"]
                    cod_anime = random.choice(Comeddy_Anime)
                    print(cod_anime)
                    if cod_anime == "Kantaro: The Sweet Tooth Salaryman":
                        print("Rating: 7.7/10\n Platform: Netflix\nRelease Date:2017\nDuration: 12 episodes, ~24 min/ep")
                    elif cod_anime == "The Naked Director":
                        print("Rating: 7.7/10\nPlatform: Netflix\nRelease Date:2019\nDuration: 2 seasons, ~50 min/ep")
                    elif cod_anime == "Good Morning Call":
                        print("Rating: 7.5/10\nPlatform: Netflix\nRelease Date :2016\nDuration: 2 seasons, ~45 min/ep")
                    elif cod_anime =="Samurai Gourmet":
                        print("Rating: 8.0/10\nPlatform: Netflix\nRelease Date :2017\n Duration: 12 episodes, ~20 min/ep")
                    elif cod_anime == "Ossan’s Love":
                        print("Rating: 8.2/10\nPlatform: Viki\nRelease Date: April 2018\nDuration: 7 episodes, ~45 min/ep")
                elif ik == "3":
                    print("Brace yourself for chills, thrills, and things that go bump in the night! 😱")
                    anime_hor= ["JU-ON: Origins","Crow’s Blood","Yamishibai: Japanese Ghost Stories","Tokyo Vampire Hotel","Re:Mind",]
                    anime_Horror = random.choice(anime_hor)
                    print(anime_Horror)
                    if anime_Horror == "JU-ON: Origins":
                        print("Rating: 7.1/10\nPlatform: Netflix\n Released-2020\nDuration: 6 Episodes ~26–31 min/ep")
                    elif anime_Horror == "Crow’s Blood":
                        print("Rating: 7.5/10\n Platform: Hulu Japan\nReleased-2016\nDuration: 6 episode ~30–40 min /ep")
                    elif anime_Horror == "Yamishibai: Japanese Ghost Stories":
                        print("Rating: 7.9/10\n Platform: TV Tokyo\nReleased - 2020 \n Duration: 10 episode, ~40 min/ep ")
                    elif anime_Horror == "Tokyo Vampire Hotel":
                        print("Rating: 7.2/10\nPlatform: Amazon Prime Video\nReleased -2017\n Duration :10 episode ~40–45 min/ep")
                    elif anime_Horror == "Re:Mind":
                        print("Rating: 7.1/10\nPlatform: Netflix\nRelease Date:2017\nDuration-13 Episode,~25 min/ep")
                elif ik =="4":
                    print("Welcome to the world of ACTION anime—where battles shake the heavens, and the weak become legends. 🚀⚔️")
                    action_anime = ["Attack on Titan","Demon Slayer","Jujutsu Kaisen","Fullmetal Alchemist: Brotherhood","Vinland Saga"]
                    anime_action= random.choice(action_anime)
                    print(anime_action)
                    if anime_action == "Attack on Titan":
                        print("Rating: 9.0/10\nPlatform: Netflix / Crunchyroll / Prime Video\nReleased -2013\nDuration: 4 Seasons, 87 episodes ~24 min/ep")
                    elif anime_action == "Demon Slayer":
                        print("Rating: 8.7/10\nPlatform: Netflix / Crunchyroll / Prime Video\nRelease Date:2019\nDuration: Duration: 4 Seasons, 55 episodes ~23 min / ep")
                    elif anime_action == "Jujutsu Kaisen":
                        print("Rating: 8.6/10\nPlatform: Netflix / Crunchyroll\nRelease Date:2020\nDuration:Duration: 2 Seasons, 47 episodes,~23 min / ep")
                    elif anime_action == "Fullmetal Alchemist: Brotherhood":
                        print("Rating: 9.1/10\nPlatform: Netflix / Crunchyroll / Prime Video\nRelease Date:2009\nDuration: 64 episodes ~24 min/ep")
                    elif anime_action == "Vinland Saga":
                        print("Rating: 8.8/10\nPlatform: Netflix / Prime Video / Crunchyroll\nRelease Date :2019\nDuration: 2 Seasons, 48 episodes ~24 min/ep")
                elif ik == "5":
                    print("The Phoenix Feather 🪶")
                    Fan_anime=["Made in Abyss","Mushoku Tensei: Jobless Reincarnation","The Rising of the Shield Hero","Fate/Zero","Natsume’s Book of Friends"]
                    anime_fan = random.choice(Fan_anime)
                    print(anime_fan)
                    if anime_fan == "Made in Abyss":
                        print("Rating: 8.4/10\nPlatform: Prime Video\nRelease Date:2017\nDuration: 2 Seasons 25 Episode ~25 min/ep ")
                    elif anime_fan == "Mushoku Tensei: Jobless Reincarnation":
                        print("Rating: 8.4/10\nPlatform: Crunchyroll / Netflix\nRelease Date:2021\nDuration: 2 Parts (Season 1 = 23 eps, Season 2 = 25 eps ongoing) ~23 min / ep")
                    elif anime_fan =="The Rising of the Shield Hero":
                        print("Rating: 8.0/10\nPlatform: Netflix, Crunchyroll\nRelease Date: 2019\nDuration: 3 Seasons (Season 1 = 25 eps, others ~13 eps)~23 min /ep")
                    elif anime_fan == "Fate/Zero":
                        print("Rating: 8.2/10\nPlatform: Netflix, Crunchyroll\nDuration: 2 Seasons (25 eps total)~25 min/ep\nRelease Date: Oct 1, 2011")
                    elif anime_fan =="Natsume’s Book of Friends":
                        print(" Rating: 8.5/10\nPlatform: Crunchyroll\nRelease Date: July 7, 2008\nDuration: 6 Seasons (74 eps total)~23 min / ep")
                else:
                    print("Invalid Input Please Select the correct choice.")
            else:
                print("Invalid Choice, Please Select the correct choice")
        elif Choice_Menu == "2":
            print("Hello Welcome",name," to our Membership and Subscription")
            print("1. View Membership Plans 💼\n2. Subscribe to a Plan 🔐\n3. Cancel Membership ❌\n4. Upgrade/Downgrade Plan 🔄\n5. Payment & Billing Info 💳\n6. Back to Main Menu 🔙")
            pay_sub = input("Please Make choice between 1-6")
            if pay_sub == "1":
                print("\n👑 Available Membership Plans:\n"
                      "🥉 Basic Plan – ₹199/month – Access to 720p, Subbed Only\n"
                      "🥈 Premium Plan – ₹399/month – 1080p, Dubbed + Subbed + Offline\n"
                      "🥇 Ultra Otaku Plan – ₹599/month – 4K, All Languages, Early Access, No Ads")
            elif pay_sub =="2":
                selected = input("Enter the plan name to subscribe (Basic/Premium/Ultra Otaku): ").strip().lower()
                if selected in ["Basic", "Premium", "Ultra otaku"]:
                    print(f"\n✅ Success! You have subscribed to the {selected.title()} Plan.\nEnjoy your anime ride 🚀")
                else:
                    print("❗ That’s not a valid plan. Please try again.")
            elif pay_sub == "3":
                confirm = input("Are you sure you want to cancel your membership? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("❌ Your membership has been cancelled. We'll miss you 💔")
                else:
                    print("No worries 😌 You're still in the anime club!")
            elif pay_sub == 4:
                current_plan = input("Enter your current plan (Basic/Premium/Ultra Otaku): ").strip().lower()
                new_plan = input("Enter the plan you'd like to switch to: ").strip().lower()
                if current_plan == new_plan:
                    print("You're already on this plan! Nothing changed 😅")
                elif new_plan in ["basic", "premium", "ultra otaku"]:
                    print(f"🔄 Switched from {current_plan.title()} to {new_plan.title()}!")
                else:
                    print("❗ Invalid new plan. Please enter a valid plan name.")
            elif pay_sub == "5":
                print("\n💳 Payment Details:")
                print("• Card Ending: **** **** **** 2456")
                print("• Next Billing Date: 15th July 2025")
                print("• Billing Method: Auto Debit")
                change = input("Do you want to update payment info? (yes/no): ").strip().lower()
                if change == "yes":
                    print("Redirecting to secure billing portal 🔐 (pretend link)")
                else:
                    print("Got it. Your billing info stays the same.")
            elif pay_sub == 6:
                print("🔙 Returning to Main Menu...\n")
                continue
            else:
                print("❗ Invalid option. Please choose a number from 1 to 6.\n")
        elif Choice_Menu == "3":
            print("Hey your current Language is 'English'")
            print("\nDo you want to change the Language?")
            io = input("Yes or No")
            if io.lower() in ["yes", "y", "1"]:
                print("which language do you want?\n1.Hindi\n2.Japanese\n3.Korean")
                lan = input("Please make your choice (1-3 or name): ").strip().lower()

                if lan in ["1", "hindi"]:
                    print("सफलतापूर्वक! भाषा हिंदी में बदल गई है\n")
                elif lan in ["2", "japanese"]:
                    print("成功しました！言語が日本語に変更されました\n")
                elif lan in ["3", "korean"]:
                    print("성공적으로 언어가 한국어로 변경되었습니다.\n")
                else:
                    print("Invalid choice. Your language is still English.\n")
            else:
                print("Boom!! wrong Choice, Please Try again")
        elif Choice_Menu == "4":
            print("\n💰 Payment Issue Menu:\n1. Payment Failed ❌\n2. Refund Status 🔄\n3.Talk to Support 👨‍💻")
            ip = input("Please Make your choice is here: ")
            if ip == "1":
                print("\n❗ It seems your payment failed.")
                print("🔍 Please check your bank balance, internet connection, or card validity.")
                print("You can also retry the payment later\n")
            elif ip == "2":
                print("\n🔄 Refund Status Check:")
                print("• Refunds are usually processed within 3–7 business days.")
                print("• If you've waited longer, contact support with your transaction ID.\n")
            elif ip == "3":
                print("\n👨‍💻 Connecting you to an AnimeBot Support Agent...")
                print("📞 Support ID: #A94X-77B")
                print("📨 You can also call our executive @+917503439826 for human help.\n")
            elif ip == "6":
                print("🔙 Returning to Main Menu...\n")
            else:
                print("❗ Invalid input. Please enter a number between 1-3.\n")
        elif Choice_Menu == "5":
            feedback=input("We'd love to hear from you, please give your suggestion to improve us")
            print("Thanks for your feedback! We appreciate you 💖Sayonara Saiyan")
            break
        else:
            print("Wrong Choice Anime Worrier , please select again!!")
    except ValueError:
        print("Boom!! Wrong Choice Buddy!!😿")