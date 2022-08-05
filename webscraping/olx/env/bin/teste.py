import pandas as pd

client_dictionary = {'name': ['Michael | Smith', 'Ana | Kors', 'Sean | Bill', 'Carl | Jonson', 'Bob | Evan'], 
                     'grade': [['A', 'A'], ['C'], ['A', 'C', 'B'], [], ['F']], 
                     'age': ['19', '19', '17', '18', '-'],
                     'group': ['class 1', 'class 2', 'class 2', 'class 1', 'class 2'],
                     'suspended': [True, False, True, False, True]
                    }
df = pd.DataFrame(client_dictionary)

name_split = df['name'].str.split('|', n=1, expand=True)

df["nome"] = name_split[0]
df["sobrenome"] = name_split[1]

nome = name_split[0]
sobrenome = name_split[0][1]

print(df)
#texto = df['name'].split

