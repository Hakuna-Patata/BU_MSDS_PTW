# Assignment: American Community Survey 2014
# Name: Weatherford, Patrick
# Date: 2021-09-13

library(dplyr)
library(readxl)
library(ggplot2)
library(psych)
library(pastecs)

theme_set(theme_gray())

setwd("C:/Users/patwea/OneDrive - Bellevue University/BU/DSC 520 - Statistics for Data Science/Patrick.Weatherford-DSC520/R")

acs_data <- read.csv("data/acs-14-1yr-s0201.csv", stringsAsFactors = FALSE)


# i. What are the elements in your data:
str(acs_data)
summary(acs_data)


# ii. Provide the output from str(), nrow(), ncol()
# str()
str(acs_data)
# nrow()
nrow(acs_data)
# ncol()
ncol(acs_data)


# iii. Create histogram of HSDegree variable.
acs_data %>% 
  ggplot(
    aes(x=HSDegree)
  ) +
  geom_histogram(mapping = aes(y =..density..), binwidth = 1, color="darkgreen", fill="lightgreen", alpha=0.5) + 
  ggtitle("High School Graduation Rate Frequency") +
  xlab("Graduation Rate") + 
  ylab("Density")


# iv. Details about the histogram.
##    1. Yes, the data is unimodal meaning there is only 1 peak.
##    2. No, the data is skewed and is not approximately symmetrical. 
##    3. No, the data is skewed and is not approximately bell-shaped. 
##    4. No, the data is skewed and is not approximately normal
##    5. Yes, the data is negatively skewed meaning the mode is to the right of the mean and median.
##    6. Include a normal curve to the histogram.

acs_data %>% 
  ggplot(
    aes(x=HSDegree)
  ) +
  geom_histogram(mapping = aes(y =..density..), binwidth = 1, color="darkgreen", fill="lightgreen", alpha=0.5) + 
  geom_density(size = 1.2, aes(color = "Density")) + 
  stat_function(fun = dnorm,
                args = list(mean = mean(acs_data$HSDegree, na.rm=TRUE)
                            , sd = sd(acs_data$HSDegree, na.rm=TRUE))
                , aes(color = "Normal Curve")
                , size = 1.2
  ) + 
  ggtitle("High School Graduation Rate Frequency") +
  labs(
    x = "Graduation Rate"
    , y = "Density"
  ) +
  scale_color_manual("Legend", values = c("darkgrey", "purple"))

##    7. No, a normal distribution should not be used as a model for the data for the below reasons.
####    7a) Data is negatively skewed, has positivie kurtosis, and p-value is high. This should be used if sample size is very large though. 
          stat.desc(acs_data$HSDegree, basic=FALSE, norm=TRUE)
####    7b) Looking visually at the histogram compared to the normal curve, it is obvious that the bins do not align with the normal curve.

          
# V. Create a probability plot of HSDegree variable.
qqnorm(acs_data$HSDegree); qqline(acs_data$HSDegree)

##    1. 

