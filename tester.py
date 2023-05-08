from colorama import Fore
from DAA_Problem_2_Lachi_Presidente_PCC import *
from test_cases_generator import generator

algorithm = {"1" : solution1, "2" : solution2}
generator = {"1" : generator}

print("Solutions:")
print("1: First Aproximation", "2: Second Aproximation", "3: Third Aproximation")
algo1 = input("Choose the first algorithm \n")
algo2 = input("Choose the second algorithm \n")

gen = input("Choose the generator algorithm \n")

test_cases_number = int(input("How many test cases you want to generate? \n"))

test_cases = generator[gen](test_cases_number)

if algo1 == algo2:
    for case in test_cases:
        print(algorithm[algo1](case))

else:
    wrong_cases = 0

    for case in test_cases:
        answer1 = algorithm[algo1](case)
        answer2 = algorithm[algo2](case)
        match = answer1 == answer2

        printSolution(case)

        if match:
            print(Fore.GREEN, f"answer1:{answer1}, answer2:{answer2}, good")
            print(Fore.RESET, "\n")

        else:
            wrong_cases += 1
            print(Fore.RED, f"answer1:{answer1}, answer2:{answer2}, bad")
            print(Fore.RESET, "\n")

    print(f"Number of wrong cases: {wrong_cases} \n")
