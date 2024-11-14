def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                

# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,	                  #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################

def z_score(x, mu, sigma):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """
    
    # Hunter Franklin, Jonathan Jones, & Daniel Goncharov    

    # Our code:

    data_set = population2 # Change to any of the three data sets

    x = (-12) # Change this to any x-value on the given population data set

    mu = mean(data_set) # Calculates the mean of the data set

    sigma = stdev(data_set, mu) # Calculates the standard deviation (population) of the provided data set

    z_algorithm = (x - mu) / sigma # Z-Score formula

    
    return z_algorithm # Returned Z-Score


z_algorithm = z_score (0, 0, 0) # 0 values are placeholder arguments

print("Z-Score of Population 2: Value -12 =", z_algorithm) # Displayed Z-Score -- Change title to appropriate population number and x-value


# Delete both """ and change Run_Tests to True to test three x-values, one from each population data set - This took a while to make so I wanted to leave it.  

"""

Run_Tests = False

def z_score(x, mu, sigma):

    z = (x - mu) / sigma
    return z 

if Run_Tests:

    print("-" * 80)

    x_pop1 = 14
    mu_pop1 = mean(population1) # Random value chosen from Population1 data set
    sigma_pop1 = stdev(population1, mu_pop1) # Standard Deviation (Population) of Population2 given Mean
    z_pop1 = z_score(x_pop1, mu_pop1, sigma_pop1) # The Z-Score of this data value 14 given z_score function
    print("Z_Score for Population 1: Value 14 =", z_pop1) # Printing Z-Score

    print("-" * 80)

    x_pop1min = z_score(least(population1), mu_pop1, sigma_pop1) # Minimum value Z-Score in Population1
    print("Population 1 Minimum Value Z-Score =", x_pop1min)
    x_pop1max = z_score(greatest(population1), mu_pop1, sigma_pop1) # Maximum value Z-Score in Population1
    print("Population 1 Minimum Value Z-Score =", x_pop1max)
    
    x_pop1test = (x_pop1min + x_pop1max)
    print("Population 1: Test if Min and Max Z-Scores Equalling 0, the value =", x_pop1test)

    # Does not equal 0.0 becuase the data is not ditributed normally\

    print("-" * 80)

    x_pop2 = 20 # Random value chosen from Population2 data set
    mu_pop2 = mean(population2) # Mean of Population2
    sigma_pop2 = stdev(population2, mu_pop2) # Standard Deviation (Population) of Population2 given Mean
    z_pop2 = z_score(x_pop2, mu_pop2, sigma_pop2) # The Z-Score of this data value 14 given z_score function
    print("Z_Score for Population 2: Value 20 =", z_pop2) # Printing Z-Score

    print("-" * 80)

    x_pop2min = z_score(least(population2), mu_pop2, sigma_pop2) # Minimum value Z-Score in Population2
    print("Population 2 Minimum Value Z-Score =", x_pop2min)
    x_pop2max = z_score(greatest(population2), mu_pop2, sigma_pop2) # Maximum value Z-Score in Population2
    print("Population 2 Minimum Value Z-Score =", x_pop2max)
   
    x_pop2test = (x_pop2min + x_pop2max)
    print("Population 2: Test if Min and Max Z-Scores Equalling 0, the value =", x_pop2test)

    # Equals 0.0

    print("-" * 80)

    x_pop3 = 375 # Random value chosen from Population3 data set
    mu_pop3 = mean(population3) # Mean of Population2
    sigma_pop3 = stdev(population3, mu_pop3) # Standard Deviation (Population) of Population2 given Mean
    z_pop3 = z_score(x_pop3, mu_pop3, sigma_pop3) # The Z-Score of this data value 14 given z_score function
    print("Z_Score for Population 3: Value 375 =", z_pop3) # Printing Z-Score

    print("-" * 80)

    x_pop3min = z_score(least(population3), mu_pop3, sigma_pop3) # Minimum value Z-Score in Population3
    print("Population 3 Minimum Value Z-Score =", x_pop3min)
    x_pop3max = z_score(greatest(population3), mu_pop3, sigma_pop3) # Maximum value Z-Score in Population3
    print("Population 3 Minimum Value Z-Score =", x_pop3max)
    
    x_pop3test = (x_pop3min + x_pop3max)
    print("Population 3: Test if Min and Max Z-Scores Equalling 0, the value =", x_pop3test)

    # Equals 0.0

    print("-" * 80)

    # All input x-value results are accurate, to 11 sigfigs, my expected results that I made on Google Sheets.

"""




