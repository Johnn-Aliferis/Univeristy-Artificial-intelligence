import numpy as np
import random


def population_generation():
    for i in range(0, 10):
        random.shuffle(cits)
        population[i] = np.asarray(cits)
    return population


def fitness_function(array):
    cost = 0
    for i in range(0, 10):
        for j in range(0, 4):
            if (array[i][j] == 'A') and (array[i][j+1]) == 'B':
                cost = cost + 4
            elif (array[i][j] == 'A') and (array[i][j+1]) == 'C':
                cost = cost + 4
            elif (array[i][j] == 'A') and (array[i][j+1]) == 'D':
                cost = cost + 7
            elif (array[i][j] == 'A') and (array[i][j+1]) == 'E':
                cost = cost + 3
            elif (array[i][j] == 'B') and (array[i][j+1]) == 'A':
                cost = cost + 4
            elif (array[i][j] == 'B') and (array[i][j+1]) == 'C':
                cost = cost + 2
            elif (array[i][j] == 'B') and (array[i][j+1]) == 'D':
                cost = cost + 3
            elif (array[i][j] == 'B') and (array[i][j+1]) == 'E':
                cost = cost + 5
            elif (array[i][j] == 'C') and (array[i][j+1]) == 'A':
                cost = cost + 4
            elif (array[i][j] == 'C') and (array[i][j+1]) == 'B':
                cost = cost + 2
            elif (array[i][j] == 'C') and (array[i][j+1]) == 'D':
                cost = cost + 2
            elif (array[i][j] == 'C') and (array[i][j+1]) == 'E':
                cost = cost + 3
            elif (array[i][j] == 'D') and (array[i][j+1]) == 'A':
                cost = cost + 7
            elif (array[i][j] == 'D') and (array[i][j+1]) == 'B':
                cost = cost + 3
            elif (array[i][j] == 'D') and (array[i][j+1]) == 'C':
                cost = cost + 2
            elif (array[i][j] == 'D') and (array[i][j+1]) == 'E':
                cost = cost + 6
            elif (array[i][j] == 'E') and (array[i][j+1]) == 'A':
                cost = cost + 3
            elif (array[i][j] == 'E') and (array[i][j+1]) == 'B':
                cost = cost + 5
            elif (array[i][j] == 'E') and (array[i][j+1]) == 'C':
                cost = cost + 3
            elif (array[i][j] == 'E') and (array[i][j+1]) == 'D':
                cost = cost + 6
            costs[i] = cost
        cost = 0
    return costs


def sorting(array1, array2):
    for i in range(0, 10):
        for j in range(0, 9):
            if array2[j] > array2[j+1]:
                temp = array2[j]
                array2[j] = array2[j+1]
                array2[j+1] = temp
                temp1 = array1[j]
                array1[j] = array1[j+1]
                array1[j+1] = temp1
    return array1, array2


def selection_and_reproduction(population, new_population):
    # array1 is for current population, array 2 for our half top population !
    for i in range(0, 5):  # The top half of our current population!
        new_population[i] = population[i]
    # doing crossover !
    for i in range(0, 4):
        number = random.randint(0, 5)
        number2 = random.randint(0, 5)
        index = [0, 1]
        first_parent = np.delete(population[number], index)
        removed_element_1 = population[number][0]
        removed_element_2 = population[number][1]
        second_parent = np.setdiff1d(population[number2], first_parent)
        offspring = np.append(second_parent, first_parent)
        crossover[i] = offspring
        # Now we have created 40 new offsprings !
    # Creating now another 10 mutations !
    for i in range(0, 1):
        number = random.randint(0, 5)
        index = [0, 2]
        removed = np.delete(population[number], index)
        removed_element_1 = population[number][0]
        removed_element_2 = population[number][2]
        mutated_first = np.insert(removed, 0, removed_element_2)
        mutated = np.insert(mutated_first, 2, removed_element_1)
        mutation[i] = mutated
        # Now we have created our mutations!
    # Now we need to impelement the top 50 (new population), crossovers and mutations to the first array of population
    # Now we hve removed half of the previous population (with the worst fitness)
    # Appending new population, crossover and mutation and sorting the newly created population again!
    new_population_and_crossovers = np.concatenate([new_population, crossover])
    new_population_and_crossovers_and_mutation = np.concatenate([new_population_and_crossovers, mutation])
    for i in range(0, 10):
        population[i] = new_population_and_crossovers_and_mutation[i]
    return population, new_population, crossover,


mut = [None]*1
cross = [None]*4
new = [None]*5
cts = [None]*10
pop = [None]*10
population = np.array(pop)
new_population = np.array(new)
costs = np.array(cts)
crossover = np.array(cross)
mutation = np.array(mut)
cits = ['A', 'B', 'C', 'D', 'E']
cities = np.array(cits)
population_generation()
for i in range(0, 100):
    fitness_function(population)
    sorting(population, costs)
    selection_and_reproduction(population, new_population)
    sorting(population, costs)
    print("Generation number :" + str(i))
    print("Top solution  : " + str(population[0]) + " with cost : " + str(costs[0]))