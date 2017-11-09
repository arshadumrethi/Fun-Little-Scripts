from itertools import permutations
import pandas as pd

#Permutes all the letters in my name
perms = [''.join(p) for p in permutations(['a', 'r', 's', 'h', 'a', 'd' ])]

#Gives the number of permutations
print len(perms)

#Saving the list in a dataframe
df = pd.DataFrame(perms)

#Writing the dataframe to a csv file for further analysis.
df.to_csv('name.csv')
