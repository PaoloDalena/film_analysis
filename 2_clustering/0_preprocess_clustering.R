# pre-processing for clustering
films <- read.csv("film_dataset.csv", sep = ";", header = T, dec = ",", stringsAsFactors = T)
str(films)
films$year <- as.factor(films$year)
films$d_DiCaprio <- factor(films$d_DiCaprio,levels = 0:1, labels = c("n", "y"))
films$d_Bale <- factor(films$d_Bale, levels = 0:1, labels = c("n", "y"))
films$d_Pitt <- factor(films$d_Pitt, levels = 0:1, labels = c("n", "y"))
films$d_Damon <- factor(films$d_Damon, levels = 0:1, labels = c("n", "y"))
films$d_frombook <- factor(films$d_frombook, levels = 0:1, labels = c("n", "y"))
films$d_truestory <- factor(films$d_truestory, levels = 0:1, labels = c("n", "y"))
films$d_rewatched <- factor(films$d_rewatched, levels = 0:1, labels = c("n", "y"))
summary(films)
rownames(films) <- films$title
films <- films[, -1]
head(films)

# there could be problem with missing values => replace the NA's in marcello_score 
# for the imputation we assume that all the missing data are MAR
library(mice)
temp_1 <- mice(films, m = 5, method = "midastouch")
# let's see the imputed results
temp_1$imp$marcello_score
densityplot(temp_1) # unstable results
# other methods:
temp_2 <- mice(films, m = 5, method = "pmm")
temp_2$imp$marcello_score
densityplot(temp_2) # stable, but different
temp_3 <- mice(films, m = 5, method = "cart")
temp_3$imp$marcello_score
densityplot(temp_3) # good result
# not so much importance to this part, since it is not our main interest

films_clus <- complete(temp_3, 1)
# I've chosen iteration 1 beacuse it is the one with less extreme values

str(films_clus)
# hence, for the following cluster analysis, I'll use this dataset
save(films_clus, file = "films_clus.RData")

