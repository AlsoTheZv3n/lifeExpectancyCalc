def calculate_life_expectancy():
    print("Welcome to the Life Expectancy Calculator!")
    print("Please answer the following questions to calculate your life expectancy.\n")

    age = int(input("What is your current age? "))
    smoking = input("Do you smoke? (yes/no) ").lower()
    exercise_frequency = int(input("How often do you exercise per week? (days per week) "))
    exercise_type = input("What type of exercise do you do? (e.g., running, weightlifting, cycling, etc.) ")
    alcohol = input("Do you consume alcohol regularly? (yes/no) ").lower()
    diet = input("Do you maintain a healthy diet? (yes/no) ").lower()
    steroids = input("Do you take steroids for bodybuilding or TRT? (yes/no) ").lower()
    stimulating_drugs = input("Do you use stimulating drugs? (yes/no) ").lower()
    sedating_drugs = input("Do you use sedating drugs? (yes/no) ").lower()
    health_conditions = input("Do you have any health conditions? (asthma, high blood pressure, auto-immune disease, AIDS, cancer, Alzheimer's, etc.) (yes/no) ").lower()
    job = input("What is your job? (e.g., office, construction, dangerous jobs, fitness trainer, gardener, etc.) ")
    stress_level = int(input("On a scale of 1 to 10, how would you rate your stress level? (1 being low, 10 being high) "))
    weight_lifting = input("Do you engage in weightlifting? (yes/no) ").lower()
    endurance = input("Do you engage in endurance exercises? (yes/no) ").lower()
    supplements = input("Do you take any supplements? (yes/no) ").lower()

    life_expectancy = 80  # Default life expectancy

    if age < 0 or age > 120:
        print("Invalid age entered. Please enter a valid age.")
        return

    # Adjust life expectancy based on user input
    if smoking == "yes":
        life_expectancy -= 10
    if exercise_frequency >= 5:
        life_expectancy += exercise_frequency  # Add years for exercising frequently
    if exercise_type.lower() == "running":
        life_expectancy += 2
    elif exercise_type.lower() == "weightlifting":
        if weight_lifting == "yes":
            life_expectancy += 3
    elif exercise_type.lower() == "cycling":
        life_expectancy += 1
    # Add or subtract years based on other factors
    if alcohol == "yes":
        life_expectancy -= 5
    if diet == "no":
        life_expectancy -= 5
    if steroids == "yes":
        life_expectancy -= 7
    if stimulating_drugs == "yes":
        life_expectancy -= 3
    if sedating_drugs == "yes":
        life_expectancy -= 2
    if health_conditions == "yes":
        life_expectancy -= 10
    if job.lower() == "office":
        life_expectancy -= 2
    elif job.lower() == "construction":
        life_expectancy -= 5
    elif job.lower() == "dangerous jobs":
        life_expectancy -= 7
    elif job.lower() == "fitness trainer" or job.lower() == "gardener":
        life_expectancy += 3
    if stress_level >= 7:
        life_expectancy -= 5
    if endurance == "yes":
        life_expectancy += 2
    if supplements == "yes":
        life_expectancy += 1

    print("\nBased on your inputs, your life expectancy is approximately {} years.".format(life_expectancy))


if __name__ == "__main__":
    calculate_life_expectancy()
