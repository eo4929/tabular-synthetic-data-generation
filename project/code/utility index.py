# for utility index 

from tqdm.notebook import tqdm
from sdmetrics.reports.single_table import QualityReport
report = QualityReport()

preprocessed_customer = pd.read_csv('preprocessed_customer.csv')
preprocessed_customer.drop(labels='Unnamed: 0', axis=1, inplace=True)

syn_customer_1 = pd.read_csv('syn_data_customer_2217.csv')
syn_customer_2 = pd.read_csv('syn_data_customer_3000.csv')
syn_customer_3 = pd.read_csv('syn_data_customer_10000.csv')

#print(preprocessed_customer.shape)
#print(syn_customer_3000.shape)
#print(preprocessed_customer.head())
#print(syn_customer_3000.head())

ctgan_syn_customer_1 = pd.read_csv('ctgan_syn_customer_2217.csv')
ctgan_syn_customer_1.drop(labels='Unnamed: 0', axis=1, inplace=True)
ctgan_syn_customer_2 = pd.read_csv('ctgan_syn_customer_3000.csv')
ctgan_syn_customer_2.drop(labels='Unnamed: 0', axis=1, inplace=True)
ctgan_syn_customer_3 = pd.read_csv('ctgan_syn_customer_10000.csv')
ctgan_syn_customer_3.drop(labels='Unnamed: 0', axis=1, inplace=True)

syn_customer_1 = pd.concat([preprocessed_customer['ID'], syn_customer_1], axis=1)
syn_customer_2 = pd.concat([preprocessed_customer['ID'], syn_customer_2], axis=1)
syn_customer_3 = pd.concat([preprocessed_customer['ID'], syn_customer_3], axis=1)

#ctgan_syn_customer_1 = pd.concat([preprocessed_customer['ID'], ctgan_syn_customer_1], axis=1)
#ctgan_syn_customer_2 = pd.concat([preprocessed_customer['ID'], ctgan_syn_customer_2], axis=1)
#ctgan_syn_customer_3 = pd.concat([preprocessed_customer['ID'], ctgan_syn_customer_3], axis=1)

#print(ctgan_syn_customer_1.info())

#print(syn_customer_3000.shape)

preprocessed_cencus = pd.read_csv('preprocessed_adult.csv')
syn_cencus1 = pd.read_csv('syn_data_adult_1.csv')
syn_cencus2 = pd.read_csv('syn_data_adult_2.csv')
syn_cencus3 = pd.read_csv('syn_data_adult_3.csv')

ctgan_syn_cencus1 = pd.read_csv('ctgan_syn_cencus_1.csv')
ctgan_syn_cencus1.drop(labels='Unnamed: 0', axis=1, inplace=True)
ctgan_syn_cencus2 = pd.read_csv('ctgan_syn_cencus_2.csv')
ctgan_syn_cencus2.drop(labels='Unnamed: 0', axis=1, inplace=True)
ctgan_syn_cencus3 = pd.read_csv('ctgan_syn_cencus_3.csv')
ctgan_syn_cencus3.drop(labels='Unnamed: 0', axis=1, inplace=True)
#print(ctgan_syn_cencus1.info())

preprocessed_bitcoin = pd.read_csv('preprocessed_bitcoin.csv')
syn_bitcoin1 = pd.read_csv('syn_data_bitcoin_1.csv')
syn_bitcoin2 = pd.read_csv('syn_data_bitcoin_2.csv')
syn_bitcoin3 = pd.read_csv('syn_data_bitcoin_3.csv')

ctgan_syn_bitcoin1 = pd.read_csv('ctgan_syn_bitcoin_1.csv')
ctgan_syn_bitcoin2 = pd.read_csv('ctgan_syn_bitcoin_2.csv')
ctgan_syn_bitcoin3 = pd.read_csv('ctgan_syn_bitcoin_3.csv')



# customer 데이터
print('1. customer data')
print('- - - - CART - - - ')
print('same size')
res = report.generate(preprocessed_customer, syn_customer_1, metadata1)
print(res)
print('1.5 size')
res = report.generate(preprocessed_customer, syn_customer_2, metadata1)
print(res)
print('3 size')
res = report.generate(preprocessed_customer, syn_customer_3, metadata1)
print(res)
print('- - - - CTGAN - - - ')
print('same size')
res = report.generate(preprocessed_customer, ctgan_syn_customer_1, metadata1)
print(res)
print('1.5 size')
res = report.generate(preprocessed_customer, ctgan_syn_customer_2, metadata1)
print(res)
print('3 size')
res = report.generate(preprocessed_customer, ctgan_syn_customer_3, metadata1)
print(res)

print(' - - - - ')
print(' - - - - ')

print('2. cencus data')
print('- - - - CART - - - ')
print('same size')
res = report.generate(preprocessed_cencus, syn_cencus1, metadata2)
print(res)
print('1.5 size')
res = report.generate(preprocessed_cencus, syn_cencus2, metadata2)
print(res)
print('3 size')
res = report.generate(preprocessed_cencus, syn_cencus3, metadata2)
print(res)
print('- - - - CTGAN - - - ')
print('same size')
res = report.generate(preprocessed_cencus, ctgan_syn_cencus1, metadata2)
print(res)
print('1.5 size')
res = report.generate(preprocessed_cencus, ctgan_syn_cencus2, metadata2)
print(res)
print('3 size')
res = report.generate(preprocessed_cencus, ctgan_syn_cencus3, metadata2)
print(res)

print(' - - - - ')
print(' - - - - ')


print('3. bitcoin data')
print('- - - - CART - - - ')

print('same size')
res = report.generate(preprocessed_bitcoin, syn_bitcoin1, metadata3)
print(res)
print('1.5 size')
res = report.generate(preprocessed_bitcoin, syn_bitcoin2, metadata3)
print(res)
print('3 size')
res = report.generate(preprocessed_bitcoin, syn_bitcoin3, metadata3)
print(res)
print('- - - - CTGAN - - - ')
print('same size')
res = report.generate(preprocessed_bitcoin, ctgan_syn_bitcoin1, metadata3)
print(res)
print('1.5 size')
res = report.generate(preprocessed_bitcoin, ctgan_syn_bitcoin2, metadata3)
print(res)
print('3 size')
res = report.generate(preprocessed_bitcoin, ctgan_syn_bitcoin3, metadata3)
print(res)

