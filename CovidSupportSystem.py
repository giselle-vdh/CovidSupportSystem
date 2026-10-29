#show Stastics: random num between 1-9
#show Prevention
#show Symptoms: most common symptoms
#show Treatment: "If u feel sick"
#show Report Case: input: do you have any symptoms? Is ur temp above 38.5? which country r u selected in options below: 1. SA, 2. USA, 3. China, enter option(1/2/3): 2
#show Exit(end program)

#CovidSupportSystem
while True:
    print("---COVID SUPPORT SYSTEM---")
    print("1. Statistics")
    print("2. Prevention")
    print("3. Symptoms")
    print("4. Treatment")
    print("5. Report Case")
    print("6. Exit \n\n" )

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        print("--- COVID STATISTICS ---")
        print("Currently in South Africa, there are 27403 Confrimed cases.")
        print("Currently in USA, there are 1700000 Confrimed cases.")
        print("Currently in China, there are 82995 Confrimed cases.")

        answer = input("Would you like to see the Confrimed cases for a random country? y/n: ")
        
        if answer == "y":
            number =int(input("To select a random country, type a number from 0 to 9: "))
            countries = ["Australia", "UK", "Germany","Japan", "Italy","Brazil", "Spain", "India", "Niger"]
            
            print("Country:", countries[number])
            print("Cases: 50000")
        elif answer == "n":
            print("\n---Returning to menu...")

    elif choice == "2":
        print("\n---To prevent the spread of COVID-19:")
        print("CLEAN YOUR HANDS OFTEN. Use soap and water, or an alchol-based hand rub.")
        print("MAINTAIN SOCIAL DISTANCING.")
        print("DO NOT TOUCH YOUR FACE")
        print("STAY HOME WHEN UNWELL.")
        print("Cover your NOSE AND MOUTH with your ELBOW or with a TISSUE when coughing or sneezing.")
        print("If you have a fever, cough, difficukty breathing, SEEK MEDICAL ATTENTION.")
        print("Follw the directions of your local health authority!\n\n\n")

        
    elif choice == "3":
         print("---Most Common Sympyoms:")
         print("\nFever")
         print("Dry cough")
         print("Tiredness")

         print("---Less Common Symptoms:")
         print("\nAches and pains")
         print("Sore throat")
         print("Diarrhoea")
         print("Loss of taste or smell")

         print("---Serious Symptoms:")
         print("\nDifficulty breathing")
         print("Chest pain")
         print("Loss of speech or movement\n\n\n")
    
    elif choice =="4":
        print("\n---Treatment")
        print("If you feel sick you should rest and drink water. Clean and disinfect and social distance.\n\n\n")

    elif choice =="5":
        print("\n---Report Case")
        symptoms = input("Do you have any of the symptoms? y/n: ")
        temp = input("Is your temperature aboice 38,5? y/n: ")
        country = input("In which country are you? Select an option below:\n"
                        "1. South Africa\n"
                        "2. USA\n"
                        "3. China\n"
                        "Enter option (1/2/3): ")
        
        if symptoms == "y" and temp == "y":
            if country == "1":
                print("You have Covid-19, pls see Treatment (South Africa).")
            elif country == "2":
                print("u have corona, see treatment (USA).")
            elif country == "3":
                print("u hav corona, get treatment (China).")
            else:
                print("Invalid country option.")
        else:
            print("No Covid-19 detected based on your answers.")
    
    elif choice =="6":
        print("Exiting program...")
        break
    else:
        print("Input a vaild number.")