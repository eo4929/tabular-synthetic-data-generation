# GU
def check_uniqueness(origin_data, synthetic_data, lst_quasi_identifier):
  unique_origin_data = origin_data.drop_duplicates(subset=lst_quasi_identifier)
  unique_origin_data_qi = unique_origin_data[ lst_quasi_identifier ]

  unique_synthetic_data = synthetic_data.drop_duplicates(subset=lst_quasi_identifier)
  unique_synthetic_data_qi = unique_synthetic_data[ lst_quasi_identifier ]

  denominator = len(unique_origin_data_qi)
  numerator = 0
  val_uniqueness = 0

  if denominator == 0:
    print('uniqueness(0.0~1.0) : ', val_uniqueness)
    return val_uniqueness

  for i in unique_origin_data_qi.values:
     for j in unique_synthetic_data_qi.values:
       if np.array_equal(i,j):
         numerator += 1
         break

  print(denominator)
  print(numerator)

  if denominator == 0:
    return val_uniqueness

  val_uniqueness = numerator / denominator

  print('uniqueness(0.0~1.0) : ', val_uniqueness)
  return val_uniqueness


# TCAP (itertuples version)

def WEAP( synthetic_data, lst_key_variables, lst_target_variables, adjust_alpha_val_WEAP_j):
  synthetic_data_WEAP_1 = synthetic_data.copy()
  #key_var_synthetic_data = synthetic_data[ lst_key_variables ]
  #target_var_synthetic_data = synthetic_data[ lst_target_variables ]

  denominator = 0
  numerator = 0

  for series_j in synthetic_data.itertuples():
    denominator = 0
    numerator = 0

    for series_i in synthetic_data.itertuples():
      #print(series_i.Index)
      if series_i.Index == series_j.Index:
        continue
      #elif series_j.Education == series_j.Education and series_j.Marital_Status == series_j.Marital_Status:
      elif series_j.education == series_i.education and series_j.workclass == series_i.workclass and series_j.occupation == series_i.occupation and series_j.race == series_i.race :
        denominator +=1
        #if series_j.Income == series_j.Income and series_j.Year_Birth == series_j.Year_Birth :
        if series_j.age == series_i.age and series_j.sex == series_i.sex :
          numerator +=1

    if denominator == 0:
      synthetic_data_WEAP_1.drop( [series_j.Index], axis=0, inplace=True)
      continue


    WEAP_j = numerator / denominator
    #print('idx_j : ', idx_j)
    #print('WEAP_j : ' , WEAP_j)
    if WEAP_j < adjust_alpha_val_WEAP_j:
      synthetic_data_WEAP_1.drop( [series_j.Index], inplace=True)
    #else:
    #  print('idx_j: ', idx_j)

  return synthetic_data_WEAP_1


def TCAP(origin_data, synthetic_data_WEAP_alpha, key_lst_syn, target_lst_syn):
  lst_TCAP_j = [] 

  denominator = 0
  numerator = 0

  for origin_series_j in origin_data.itertuples():
    denominator = 0
    numerator = 0
    #print(origin_series_j)
    for syn_series_j in synthetic_data_WEAP_alpha.itertuples():
      #if origin_series_j.Education == syn_series_j.Education and origin_series_j.Marital_Status == syn_series_j.Marital_Status:
      if origin_series_j.education == syn_series_j.education and origin_series_j.workclass == syn_series_j.workclass and origin_series_j.occupation == syn_series_j.occupation and origin_series_j.race == syn_series_j.race :
        denominator +=1
        #if origin_series_j.Year_Birth == syn_series_j.Year_Birth and origin_series_j.Income == syn_series_j.Income:
        if origin_series_j.age == syn_series_j.age and origin_series_j.sex == syn_series_j.sex:
          numerator +=1

    if denominator == 0:
      continue


    TCAP_j = numerator / denominator
    #print('TCAP_j : ' , TCAP_j)
    lst_TCAP_j.append(TCAP_j)
    #else:
    #  print('idx_j: ', idx_j)

  return sum(lst_TCAP_j) / len(lst_TCAP_j)

ctgan_syn_cencus3_WEAP = WEAP(ctgan_syn_cencus3, ['Education', 'Income', 'Marital_Status'], ['Year_Birth'],0.9)
#print(preprocessed_customer.shape)
print(ctgan_syn_cencus3_WEAP.shape)

res_val = TCAP(preprocessed_cencus, ctgan_syn_cencus3_WEAP, ['Education', 'Income', 'Marital_Status'], ['Year_Birth'])
print('TCAP(ctgan_syn_cencus3_WEAP) : ')
print(res_val)


print('GU')
print('1. customer')
print()

print('GU_syn_customer (total) : ', )
check_uniqueness(preprocessed_customer, syn_customer_1, ['Education', 'Income', 'Marital_Status', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, syn_customer_2, ['Education', 'Income', 'Marital_Status', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, syn_customer_3, ['Education', 'Income', 'Marital_Status', 'Year_Birth'] )
print('GU_syn_customer (parital) : ', )
check_uniqueness(preprocessed_customer, syn_customer_1, ['Education', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, syn_customer_2, ['Education', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, syn_customer_3, ['Education', 'Year_Birth'] )
print()
print('GU_ctgan_syn_customer (total) : ', )
check_uniqueness(preprocessed_customer, ctgan_syn_customer_1, ['Education', 'Income', 'Marital_Status', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, ctgan_syn_customer_2, ['Education', 'Income', 'Marital_Status', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, ctgan_syn_customer_3, ['Education', 'Income', 'Marital_Status', 'Year_Birth'] )
print('GU_syn_customer (parital) : ', )
check_uniqueness(preprocessed_customer, ctgan_syn_customer_1, ['Education', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, ctgan_syn_customer_2, ['Education', 'Year_Birth'] )
check_uniqueness(preprocessed_customer, ctgan_syn_customer_3, ['Education', 'Year_Birth'] )

print()
print('- - - - -')
print()


print('2. cencus')
print()

print('GU_syn_cencus (total) : ', )
check_uniqueness(preprocessed_cencus, syn_cencus_1,['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'education.num', 'marital.status', 'relationship'] )
check_uniqueness(preprocessed_cencus, syn_cencus_2,['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'education.num', 'marital.status', 'relationship'] )
check_uniqueness(preprocessed_cencus, syn_cencus_3,['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'education.num', 'marital.status', 'relationship'] )
print('GU_syn_cencus (parital) : ', )
check_uniqueness(preprocessed_cencus, syn_cencus_1,['age', 'workclass', 'education', 'race', 'sex'] )
check_uniqueness(preprocessed_cencus, syn_cencus_2,['age', 'workclass', 'education', 'race', 'sex'] )
check_uniqueness(preprocessed_cencus, syn_cencus_3,['age', 'workclass', 'education', 'race', 'sex'] )
print()
print('GU_syn_cencus (total) : ', )
check_uniqueness(preprocessed_cencus, ctgan_syn_cencus_1,['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'education.num', 'marital.status', 'relationship'] )
check_uniqueness(preprocessed_cencus, ctgan_syn_cencus_2,['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'education.num', 'marital.status', 'relationship'] )
check_uniqueness(preprocessed_cencus, ctgan_syn_cencus_3,['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'education.num', 'marital.status', 'relationship'] )
print('GU_syn_cencus (parital) : ', )
check_uniqueness(preprocessed_cencus, ctgan_syn_cencus_1,['age', 'workclass', 'education', 'race', 'sex'] )
check_uniqueness(preprocessed_cencus, ctgan_syn_cencus_2,['age', 'workclass', 'education', 'race', 'sex'] )
check_uniqueness(preprocessed_cencus, ctgan_syn_cencus_3,['age', 'workclass', 'education', 'race', 'sex'] )

print()
print('- - - - -')
print()


print('3. Ethereum')
print()

print('GU_syn_bitcoin (total) : ', )
check_uniqueness(preprocessed_bitcoin, syn_bitcoin_1, ['Address','total_ether_balance','total_transactions'] )
check_uniqueness(preprocessed_bitcoin, syn_bitcoin_2, ['Address','total_ether_balance','total_transactions'] )
check_uniqueness(preprocessed_bitcoin, syn_bitcoin_3, ['Address','total_ether_balance','total_transactions'] )
print('GU_syn_bitcoin (parital) : ', )
check_uniqueness(preprocessed_bitcoin, syn_bitcoin_1, ['Address','total_ether_balance'] )
check_uniqueness(preprocessed_bitcoin, syn_bitcoin_2, ['Address','total_ether_balance'] )
check_uniqueness(preprocessed_bitcoin, syn_bitcoin_3, ['Address','total_ether_balance'] )
print()
print('GU_syn_bitcoin (total) : ', )
check_uniqueness(preprocessed_bitcoin, ctgan_syn_bitcoin_1, ['Address','total_ether_balance','total_transactions'] )
check_uniqueness(preprocessed_bitcoin, ctgan_syn_bitcoin_2, ['Address','total_ether_balance','total_transactions'] )
check_uniqueness(preprocessed_bitcoin, ctgan_syn_bitcoin_3 , ['Address','total_ether_balance','total_transactions'] )
print('GU_syn_bitcoin (parital) : ', )
check_uniqueness(preprocessed_bitcoin, ctgan_syn_bitcoin_1, ['Address','total_ether_balance'] )
check_uniqueness(preprocessed_bitcoin, ctgan_syn_bitcoin_2, ['Address','total_ether_balance'] )
check_uniqueness(preprocessed_bitcoin, ctgan_syn_bitcoin_3, ['Address','total_ether_balance'] )
