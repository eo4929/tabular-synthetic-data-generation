from sdv.single_table import GaussianCopulaSynthesizer

preprocessed_customer = pd.read_csv('preprocessed_customer.csv')
preprocessed_customer = preprocessed_customer.drop( ['ID'], axis=1 )
print(preprocessed_customer.info())

from sdv.single_table import GaussianCopulaSynthesizer, TVAESynthesizer

#from sdv.tabular.copulas import GaussianCopula

from sdv import *

GaussianCopulaSynthesizer()

metadata1 = {
    "primary_key": "ID",
    "columns" : {
        "ID" : {"sdtype": "numerical", "computer_representation": "Int32"},
        "Year_Birth" : {"sdtype": "categorical"},
        "Education" : {"sdtype": "categorical"},
        "Marital_Status" : {"sdtype": "categorical"},
        "Income": {"sdtype": "numerical", "computer_representation": "Float"},
        "Kidhome" : {"sdtype": "categorical"},
        "Teenhome" : {"sdtype": "categorical"},
        "Dt_Customer": {"sdtype": "datetime", "datetime_format": "%d-%m-%Y"},
        "Recency": {"sdtype": "numerical", "computer_representation": "Float"},#
        "MntWines": {"sdtype": "numerical", "computer_representation": "Float"},
        "MntFruits": {"sdtype": "numerical", "computer_representation": "Float"},
        "MntMeatProducts": {"sdtype": "numerical", "computer_representation": "Float"},
        "MntFishProducts": {"sdtype": "numerical", "computer_representation": "Float"},
        "MntSweetProducts": {"sdtype": "numerical", "computer_representation": "Float"},
        "MntGoldProds": {"sdtype": "numerical", "computer_representation": "Float"},
        "NumDealsPurchases": {"sdtype": "numerical", "computer_representation": "Float"},
        "NumWebPurchases": {"sdtype": "numerical", "computer_representation": "Float"},
        "NumCatalogPurchases": {"sdtype": "numerical", "computer_representation": "Float"},
        "NumStorePurchases": {"sdtype": "numerical", "computer_representation": "Float"},
        "NumWebVisitsMonth": {"sdtype": "numerical", "computer_representation": "Float"},
        "AcceptedCmp3" : {"sdtype": "categorical"},
        "AcceptedCmp4" : {"sdtype": "categorical"},
        "AcceptedCmp5" : {"sdtype": "categorical"},
        "AcceptedCmp1" : {"sdtype": "categorical"},
        "AcceptedCmp2" : {"sdtype": "categorical"},
        "Complain" : {"sdtype": "categorical"},
        "Response" : {"sdtype": "categorical"}
    }
}

metadata2 = {
    "columns" : {
        'age' : {"sdtype": "categorical"},
        'workclass' : {"sdtype": "categorical"},
        'fnlwgt' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'education' : {"sdtype": "categorical"},
        'education.num' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'marital.status' : {"sdtype": "categorical"},
        'occupation' : {"sdtype": "categorical"},
        'relationship' : {"sdtype": "categorical"},
        'race' : {"sdtype": "categorical"},
        'marital.status' : {"sdtype": "categorical"},
        'sex' : {"sdtype": "categorical"},
        'capital.gain' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'capital.loss' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'hours.per.week' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'native.country' : {"sdtype": "categorical"},
        'income': {"sdtype": "categorical"}
    }
}


metadata3 = {
    "columns" : {
        'Address' : {"sdtype": "categorical"},
        'FLAG' : {"sdtype": "boolean"},
        'Avg_min_between_sent_tnx' : {"sdtype": "numerical", "computer_representation": "Float"},
        'Avg_min_between_received_tnx' : {"sdtype": "numerical", "computer_representation": "Float"},
        'Time_Diff_between_first_and_last_(Mins)' : {"sdtype": "numerical", "computer_representation": "Float"},
        'Sent_tnx' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'Received_Tnx' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'Number_of_Created_Contracts' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'Unique_Received_From_Addresses' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'Unique_Sent_To_Addresses' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'min_value_received' : {"sdtype": "numerical", "computer_representation": "Float"},
        'max_value_received ' : {"sdtype": "numerical", "computer_representation": "Float"},
        'avg_val_received' : {"sdtype": "numerical", "computer_representation": "Float"},
        'min_val_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'max_val_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'avg_val_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'min_value_sent_to_contract' : {"sdtype": "numerical", "computer_representation": "Float"},
        'max_val_sent_to_contract' : {"sdtype": "numerical", "computer_representation": "Float"},
        'avg_value_sent_to_contract' : {"sdtype": "numerical", "computer_representation": "Float"},
        'total_transactions' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'total_Ether_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'total_ether_received' : {"sdtype": "numerical", "computer_representation": "Float"},
        'total_ether_sent_contracts' : {"sdtype": "numerical", "computer_representation": "Float"},
        'total_ether_balance' : {"sdtype": "numerical", "computer_representation": "Float"}, #here
        'Total_ERC20_tnxs' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'ERC20_total_Ether_received' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_total_ether_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_total_Ether_sent_contract' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_uniq_sent_addr' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'ERC20_uniq_rec_addr' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'ERC20_uniq_sent_addr.1' :{"sdtype": "numerical", "computer_representation": "Int32"} ,
        'ERC20_uniq_rec_contract_addr' : {"sdtype": "numerical", "computer_representation": "Int32"},
        'ERC20_avg_time_between_sent_tnx' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_avg_time_between_rec_tnx' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_avg_time_between_rec_2_tnx' : {"sdtype": "numerical", "computer_representation": "Float"} ,
        'ERC20_avg_time_between_contract_tnx' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_min_val_rec' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_max_val_rec' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_avg_val_rec' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_min_val_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_max_val_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_avg_val_sent' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_min_val_sent_contract' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_max_val_sent_contract'	: {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_avg_val_sent_contract' : {"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_uniq_sent_token_name' :{"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_uniq_rec_token_name':{"sdtype": "numerical", "computer_representation": "Float"},
        'ERC20_most_sent_token_type':{"sdtype": "categorical"},
        'ERC20_most_rec_token_type':{"sdtype": "categorical"}
    }
}

synthesizer1 = GaussianCopulaSynthesizer(metadata1)
synthesizer1.fit(preprocessed_customer)
data_synthesizer1 = synthesizer.sample(num_rows=2217)
data_synthesizer1.to_csv('copula_syn_customer_1.csv')

synthesizer1 = TVAESynthesizer(metadata1)
synthesizer1.fit(preprocessed_customer)
data_synthesizer1 = synthesizer.sample(num_rows=2217)
data_synthesizer1.to_csv('vae_syn_customer_1.csv')

synthesizer2 = GaussianCopulaSynthesizer(metadata2)
synthesizer2.fit(preprocessed_customer)
data_synthesizer2 = synthesizer.sample(num_rows=32535)
data_synthesizer2.to_csv('copula_syn_cencus_1.csv')

synthesizer2 = TVAESynthesizer(metadata2)
synthesizer2.fit(preprocessed_customer)
data_synthesizer2 = synthesizer.sample(num_rows=32535)
data_synthesizer2.to_csv('vae_syn_cencus_1.csv')

synthesizer3 = GaussianCopulaSynthesizer(metadata3)
synthesizer3.fit(preprocessed_bitcoin)
data_synthesizer2 = synthesizer.sample(num_rows=8982)
data_synthesizer2.to_csv('copula_syn_bitcoin_1.csv')

synthesizer3 = TVAESynthesizer(metadata3)
synthesizer3.fit(preprocessed_bitcoin)
data_synthesizer3 = synthesizer.sample(num_rows=8982)
data_synthesizer3.to_csv('vae_syn_bitcoin_1.csv')


from ctgan import CTGAN

print(preprocessed_bitcoin.columns)

discrete_columns = [
    "Year_Birth",
        "Education",
        "Marital_Status",
        "Kidhome",
        "Teenhome",
    "Dt_Customer",
    "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
        "AcceptedCmp1",
        "AcceptedCmp2",
        "Complain",
        "Response"]

discrete_columns = ['age', 'workclass', 'education', 'education.num', 'marital.status', 'occupation', 'relationship', 'race', 'sex', 'native.country', 'income']

discrete_columns = ['Address',
    ' Total ERC20 tnxs' , 'FLAG' , 'Sent tnx' , 'Received Tnx' , 'Number of Created Contracts' ,
    'Unique Received From Addresses' , 'Unique Sent To Addresses' , 'total transactions (including tnx to create contract',
    ' ERC20 total Ether sent contract',	' ERC20 uniq sent addr', ' ERC20 uniq rec addr' ,
    ' ERC20 uniq sent addr.1'	, ' ERC20 uniq rec contract addr' , ' ERC20 most sent token type' , ' ERC20_most_rec_token_type']

ctgan = CTGAN(embedding_dim = 128, generator_dim=(256, 256),  discriminator_dim =(256,256) ,generator_lr = 2e-4, discriminator_lr = 2e-4, epochs = 300, pac = 10, cuda=True)
ctgan.fit(preprocessed_bitcoin, discrete_columns)

# Create synthetic data
ctgan_syn_bitcoin_1 = ctgan.sample(8981)
ctgan_syn_bitcoin_1.to_csv('ctgan_syn_bitcoin_1.csv')

ctgan_syn_bitcoin_2 = ctgan.sample(12500)
ctgan_syn_bitcoin_2.to_csv('ctgan_syn_bitcoin_2.csv')

ctgan_syn_bitcoin_3 = ctgan.sample(20000)
ctgan_syn_bitcoin_3.to_csv('ctgan_syn_bitcoin_3.csv')