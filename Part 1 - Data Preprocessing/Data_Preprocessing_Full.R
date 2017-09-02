# Data Preprocessing - Full 

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing data
dataset$Age = ifelse(test = is.na(dataset$Age), 
                     yes = mean(dataset$Age, na.rm = TRUE),
                     no = dataset$Age)

dataset$Salary = ifelse(test = is.na(dataset$Salary), 
                     yes = mean(dataset$Salary, na.rm = TRUE),
                     no = dataset$Salary)

# Encoding categorical data
dataset$Country = factor(dataset$Country,
                         levels = unique(dataset$Country),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                         levels = unique(dataset$Purchased),
                         labels = c(1, 2))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling 
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])