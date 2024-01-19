import pandas as pd

states = ["California", "Florida", "Texas", "New York"]
population = [3961493, 21944577, 29730311, 19299981]

# Here, we are creating the primary key of our dataset!
dict_states = {'States':states, 'Population':population}

#We are creating a dataframe here, with the dictionary created from above^
df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)

df_states.to_csv('states.csv', index=False)


# print(states[0])

# for state in states:
   #  if states == "Florida":
   #      print(state)

# with open('test.txt','w') as file:
#     file.write("Data successfully scraped!")
