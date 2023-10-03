#install.packages("synthpop")

library("synthpop")

#help(package = synthpop)
?syn

real_data_customer <- read.csv("C:/Users/Dae-Young Park/Documents/preprocessed_customer.csv", header=T)
syn_data_customer_3500 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_3500.csv", header=T)
#syn_data_customer <- syn(real_data_customer, method = "cart", maxfaclevels=700, minnumlevels=9, m=1, k=13500, smoothing = NULL)

#summary(syn_data_customer)

#filename <- "syn_data_customer"
#write.syn(syn_data_customer, filename, filetype = c("csv"))


# syn data utility evaluation

#syn_data_customer_3500 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_3500.csv", header=T)
#syn_data_customer_10000 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_10000.csv", header=T)
#syn_data_customer_3 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_13500.csv", header=T)


?utility.tab
?utility.gen
options(max.print = 6e+23)

result1 <- utility.gen(syn_data_customer_3500, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result1, print.zscores = TRUE, zthresh = 1, digits = 5)

#result2 <- utility.gen(syn_data_customer_10000, real_data_customer)
#print(result2, print.zscores = TRUE, zthresh = 1, digits = 5)

#result <- utility.tab(syn_data_customer_3500, real_data_customer, vars= c("ID", "Year_Birth", "Education", "Marital_Status" , "Income", "Kidhome", "Teenhome", "Dt_Customer" , "Recency", "MntWines" ,"MntFruits", "MntMeatProducts" ,"MntFishProducts" ,"MntSweetProducts" ,"MntGoldProds" ,"NumDealsPurchases", "NumWebPurchases" ,"NumCatalogPurchases" , "NumStorePurchases", "NumWebVisitsMonth" , "AcceptedCmp3" ,"AcceptedCmp4" ,"AcceptedCmp5" , "AcceptedCmp1" , "AcceptedCmp2", "Complain", "Response") , max.table = 1e+06, print.tables = FALSE)
#result <- utility.tab(syn_data_customer_3500, real_data_customer, vars=NULL, max.table = 50000)
#print(u2, print.tables = TRUE, print.zdiff = TRUE)


real_data_adult <- read.csv("C:/Users/Dae-Young Park/Documents/preprocessed_adult.csv", header=T)

syn_data_adult_1 <- syn(real_data_adult, method = "cart", maxfaclevels=400, minnumlevels=5, m=1, k=32534, smoothing = NULL)

#summary(syn_data_adult_1)

filename <- "syn_data_adult_1"
write.syn(syn_data_adult_1, filename, filetype = c("csv"))


syn_data_adult_2 <- syn(real_data_adult, method = "cart", maxfaclevels=400, minnumlevels=5, m=1, k=65000, smoothing = NULL)
syn_data_adult_3 <- syn(real_data_adult, method = "cart", maxfaclevels=400, minnumlevels=5, m=1, k=120000, smoothing = NULL)

filename <- "syn_data_adult_2"
write.syn(syn_data_adult_2, filename, filetype = c("csv"))
filename <- "syn_data_adult_3"
write.syn(syn_data_adult_3, filename, filetype = c("csv"))



real_data_bitcoin <- read.csv("C:/Users/Dae-Young Park/Documents/preprocessed_bitcoin.csv", header=T)
syn_data_bitcoin <- syn(real_data_bitcoin, method = "cart", maxfaclevels=500, minnumlevels=5, m=1, k=20000, smoothing = NULL)

#filename <- "syn_data_bitcoin_3"
#write.syn(syn_data_bitcoin, filename, filetype = c("csv"))


# pMSE
real_data_customer <- read.csv("C:/Users/Dae-Young Park/Documents/preprocessed_customer.csv", header=T)
syn_data_customer_1 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_2217.csv", header=T)
syn_data_customer_2 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_3000.csv", header=T)
syn_data_customer_3 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_customer_10000.csv", header=T)
ctgan_syn_data_customer_1 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_customer_2217.csv", header=T)
ctgan_syn_data_customer_2 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_customer_3000.csv", header=T)
ctgan_syn_data_customer_3 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_customer_10000.csv", header=T)

lst_customer <- list(syn_data_customer_1, syn_data_customer_2, syn_data_customer_3, ctgan_syn_data_customer_1, ctgan_syn_data_customer_2, ctgan_syn_data_customer_3)

result1 <- utility.gen(syn_data_customer_1, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result1, print.zscores = TRUE, zthresh = 1, digits = 5)
result2 <- utility.gen(syn_data_customer_2, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result2, print.zscores = TRUE, zthresh = 1, digits = 5)
result3 <- utility.gen(syn_data_customer_3, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result3, print.zscores = TRUE, zthresh = 1, digits = 5)

result4 <- utility.gen(ctgan_syn_data_customer_1, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result4, print.zscores = TRUE, zthresh = 1, digits = 5)
result5 <- utility.gen(ctgan_syn_data_customer_2, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result5, print.zscores = TRUE, zthresh = 1, digits = 5)
result6 <- utility.gen(ctgan_syn_data_customer_3, real_data_customer, print.stats = c("pMSE", "SPECKS"))
print(result6, print.zscores = TRUE, zthresh = 1, digits = 5)


real_data_cencus <- read.csv("C:/Users/Dae-Young Park/Documents/preprocessed_cencus.csv", header=T)
syn_data_cencus_1 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_cencus_1.csv", header=T)
syn_data_cencus_2 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_cencus_2.csv", header=T)
syn_data_cencus_3 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_cencus_3.csv", header=T)
ctgan_syn_data_cencus_1 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_cencus_1.csv", header=T)
ctgan_syn_data_cencus_2 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_cencus_2.csv", header=T)
ctgan_syn_data_cencus_3 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_cencus_3.csv", header=T)

lst_cencus <- list(syn_data_cencus_1, syn_data_cencus_2, syn_data_cencus_3, ctgan_syn_data_cencus_1, ctgan_syn_data_cencus_2, ctgan_syn_data_cencus_3)

result1 <- utility.gen(syn_data_cencus_1, real_data_cencus, print.stats = c("pMSE", "SPECKS"))
print(result1, print.zscores = TRUE, zthresh = 1, digits = 5)
result2 <- utility.gen(syn_data_cencus_2, real_data_cencus, print.stats = c("pMSE", "SPECKS"))
print(result2, print.zscores = TRUE, zthresh = 1, digits = 5)
result3 <- utility.gen(syn_data_cencus_3, real_data_cencus, print.stats = c("pMSE", "SPECKS"))
print(result3, print.zscores = TRUE, zthresh = 1, digits = 5)

result4 <- utility.gen(ctgan_syn_data_cencus_1, real_data_cencus, print.stats = c("pMSE", "SPECKS"))
print(result4, print.zscores = TRUE, zthresh = 1, digits = 5)
result5 <- utility.gen(ctgan_syn_data_cencus_2, real_data_cencus, print.stats = c("pMSE", "SPECKS"))
print(result5, print.zscores = TRUE, zthresh = 1, digits = 5)
result6 <- utility.gen(ctgan_syn_data_cencus_3, real_data_cencus, print.stats = c("pMSE", "SPECKS"))
print(result6, print.zscores = TRUE, zthresh = 1, digits = 5)


real_data_bitcoin <- read.csv("C:/Users/Dae-Young Park/Documents/preprocessed_bitcoin.csv", header=T)
syn_data_bitcoin_1 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_bitcoin_1.csv", header=T)
syn_data_bitcoin_2 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_bitcoin_2.csv", header=T)
syn_data_bitcoin_3 <- read.csv("C:/Users/Dae-Young Park/Documents/syn_data_bitcoin_3.csv", header=T)
ctgan_syn_data_bitcoin_1 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_bitcoin_1.csv", header=T)
ctgan_syn_data_bitcoin_2 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_bitcoin_2.csv", header=T)
ctgan_syn_data_bitcoin_3 <- read.csv("C:/Users/Dae-Young Park/Documents/ctgan_syn_bitcoin_3.csv", header=T)

lst_bitcoin <- list(syn_data_bitcoin_1, syn_data_bitcoin_2, syn_data_bitcoin_3, ctgan_syn_data_bitcoin_1, ctgan_syn_data_bitcoin_2, ctgan_syn_data_bitcoin_3)


result1 <- utility.gen(syn_data_bitcoin_1, real_data_bitcoin, print.stats = c("pMSE", "SPECKS"))
print(result1, print.zscores = TRUE, zthresh = 1, digits = 5)
result2 <- utility.gen(syn_data_bitcoin_2, real_data_bitcoin, print.stats = c("pMSE", "SPECKS"))
print(result2, print.zscores = TRUE, zthresh = 1, digits = 5)
result3 <- utility.gen(syn_data_bitcoin_3, real_data_bitcoin, print.stats = c("pMSE", "SPECKS"))
print(result3, print.zscores = TRUE, zthresh = 1, digits = 5)

result4 <- utility.gen(ctgan_syn_data_bitcoin_1, real_data_bitcoin, print.stats = c("pMSE", "SPECKS"))
print(result4, print.zscores = TRUE, zthresh = 1, digits = 5)
result5 <- utility.gen(ctgan_syn_data_bitcoin_2, real_data_bitcoin, print.stats = c("pMSE", "SPECKS"))
print(result5, print.zscores = TRUE, zthresh = 1, digits = 5)
result6 <- utility.gen(ctgan_syn_data_bitcoin_3, real_data_bitcoin, print.stats = c("pMSE", "SPECKS"))
print(result6, print.zscores = TRUE, zthresh = 1, digits = 5)


print('customer')
print('')

for(syn_data_customer in lst_customer){
  result1 <- utility.gen(syn_data_customer, real_data_customer, print.stats = c("pMSE", "SPECKS"))
  print(result1, print.zscores = TRUE, zthresh = 1, digits = 5)
}
