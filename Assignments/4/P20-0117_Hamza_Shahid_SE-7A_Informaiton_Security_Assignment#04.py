import random

def generate_birthdays(num_people):
	# Generate random birthdays for a group of people
	birthdays = [random.randint(1, 365) for _ in range(num_people)]
	return birthdays
	
def has_shared_birthday(birthdays):
	# Check if there are shared birthdays in the group
	unique_birthdays = set(birthdays)
	return len(birthdays) != len(unique_birthdays)
	
def birthday_paradox_simulation(num_simulations, num_people):
	shared_birthday_count = 0
	for _ in range(num_simulations):
		birthdays = generate_birthdays(num_people)
		if has_shared_birthday(birthdays):
			shared_birthday_count += 1
			probability = shared_birthday_count / num_simulations
			return probability
	
# Number of simulations to run
num_simulations = 10000
# Number of people in each group
num_people = 23
probability = birthday_paradox_simulation(num_simulations, num_people)
print(f"Probability of at least two people sharing a birthday with {num_people} people:{probability:.2f}")
