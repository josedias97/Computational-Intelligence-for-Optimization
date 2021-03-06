from random import randint, sample, shuffle, randrange


def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = \
         individual[mut_points[1]], individual[mut_points[0]]

    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    mut_points = sample(range(len(individual)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    individual[mut_points[0]:mut_points[1]] = \
         individual[mut_points[0]:mut_points[1]][::-1]

    return individual

def scramble(individual):
    ''' select a random swath and scramble the cities in it'''
    # select random window
    l,r = sorted(sample(range(0, len(individual)), 2))
    swath = individual[l:r]

    # shuffle random window
    shuffle(swath)
    individual[l:r] = swath
    return individual

def insert(individual):
    ''' randomly extract a city and insert 
    it in a randomly selected position'''
    
    old_spot = randint(0,len(individual)-1)
    new_spot = randint(0,len(individual)-1)
    while new_spot == old_spot:
        # Re-randomize new slot if it' the same as the old one
        new_spot = randint(0,len(individual)-1)
    # Stores the item to be moved
    old_local = individual[old_spot]

    if new_spot > old_spot:
        # If the new spot is further ahead than the old spot, 
        #shift every item between the two spots, including the
        #item current in the new spot, one position back
        individual[old_spot:new_spot] = \
            individual[old_spot + 1:new_spot + 1]
        

    else:
        # If the old spot is further ahead than the new spot, 
        #shift every item between the two spots, including the
        #item current in the new spot, one position forward
        individual[new_spot + 1:old_spot + 1] = \
            individual[new_spot:old_spot]

    # Puts the item in it new spot 
    individual[new_spot] = old_local

    return individual

if __name__ == '__main__':
    test = [6, 1, 3, 5, 2, 4, 7]
    test = inversion_mutation(test)

