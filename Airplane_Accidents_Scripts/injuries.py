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

#print(aviation_dict_list[0:2])

#Build monthly injuries dictionary

inj_dict={}
for index in range(0, len(aviation_dict_list)):
    mth=aviation_dict_list[index]['Event Date'][-10:-8]
    if mth=='':
        mth='None'
    try:
        fatal=int(aviation_dict_list[index]['Total Fatal Injuries'])        
    except:
        fatal=0
    try:
        serious=int(aviation_dict_list[index]['Total Serious Injuries'])
    except:
        serious=0    
        
    if mth in inj_dict:  #if mth exists in dict
        inj_dict[mth]['fatal']=inj_dict[mth]['fatal']+fatal
        inj_dict[mth]['serious']=inj_dict[mth]['serious']+serious
    else:                #create new mth in dict
        inj_dict[mth]={}      
        inj_dict[mth]['fatal']=fatal
        inj_dict[mth]['serious']=serious

#save injury totals to dict     
for mont in ['01','02','03','04','05','06','07','08','09','10','11','12']:
    inj_dict[mont]['total']=sum(inj_dict[mont].values())

#display results
print('Mth','Total','Fatal','Serious')

for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
    print(m,':',inj_dict[m]['total'],inj_dict[m]['fatal'],inj_dict[m]['serious'])



