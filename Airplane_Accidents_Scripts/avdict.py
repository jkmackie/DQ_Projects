f=open('AviationData.txt')
aviation_data=f.readlines()

aviation_dict_list=[]

#create header list:  dict_keys
dict_keys=aviation_data[0].split(' | ')

#create list of dictionaries: aviation_dict_list
for row in aviation_data[1:]:
    row_dict={}
    row=row.split(' | ')
    #enumerate the list dict_keys
    for idx, header in enumerate(dict_keys):
        value=row[idx].strip()
        row_dict[header]=value
    aviation_dict_list.append(row_dict)

lax_dict=[]
for entry in aviation_dict_list:
    if 'LAX94LA336' in entry.values():
        lax_dict.append(entry)
#print('lax_dict:', lax_dict)

#It was a bit harder searching the dictionary since the key was unknown

state_accidents={}
#Build location dictionary.  Iterate through all indices.
for index in range(0,len(aviation_dict_list)):
    state=aviation_dict_list[index]['Location'][-2:]
    if state in state_accidents:
        state_accidents[state]=state_accidents[state]+1
    else:
        state_accidents[state]=1
        
state_lst=[(v,k) for k, v in state_accidents.items()]
state_lst=sorted(state_lst, reverse=True)

top_val_and_state=state_lst[0]
print('State with most accidents:',top_val_and_state[1])








    
    