library(ggplot2)
library(gridExtra)
library(psych)
library(dplyr)

theme_set(theme_grey())

dlf <- read.delim("C:/Users/patwea/OneDrive - Bellevue University/BU/R/Data/DownloadFestival(No Outlier).dat"
                      , header=TRUE)


day1_hist <- dlf %>% 
  ggplot(
    aes(x=day1)
  ) + 
  geom_histogram(
    mapping = aes(y=..density..)
    , color = "black"
    , fill = "white"
    , binwidth = .1
  ) +
  labs(
    title = "Day 1 Histogram w/Normal Curve"
    , x = "Hygiene Score \n0(stanky) - 4(fresh)"
    , y = "Density"
  ) + 
  stat_function(
    fun = dnorm
    , args = list(
      mean = mean(dlf$day1, na.rm=TRUE)
      , sd = sd(dlf$day1, na.rm=TRUE)
    )
    , color = "blue"
    , size = 1
  )


day1_qq <- dlf %>%
  ggplot(aes(sample=day1)) +
  stat_qq_line(size=2, color="#4d4d4d") +
  stat_qq(size=3, color="blue", alpha=.2) + 
  labs(
    x = "Thoretical"
    , y = "Sample"
    , title = "Day 1 Q-Q Plot"
  )

day1_box <- dlf %>% 
  ggplot(aes(gender, day1)) +
  geom_boxplot() + 
  labs(
    x = "Gender"
    , y = "Hygiene"
  )
  

#################################
day2_hist <- dlf %>% 
  ggplot(
    aes(x=day2)
  ) +
  geom_histogram(
    mapping = aes(y=..density..)
    , color = "black"
    , fill = "white"
    , binwidth = .1
  ) +
  labs(
    title = "Day 2 Histogram w/Normal Curve"
    , x = "Hygiene Score \n0(stanky) - 4(fresh)"
    , y = "Density"
  ) + 
  stat_function(
    fun = dnorm
    , args = list(
      mean = mean(dlf$day2, na.rm=TRUE)
      , sd = sd(dlf$day2, na.rm=TRUE)
    )
    , color = "blue"
    , size = 1
  )

day2_qq <- dlf %>%
  ggplot(aes(sample=day2)) +
  stat_qq_line(size=2, color="#4d4d4d") +
  stat_qq(size=3, color="blue", alpha=.2) + 
  labs(
    x = "Thoretical"
    , y = "Sample"
    , title = "Day 2 Q-Q Plot"
  )

day2_box <- dlf %>% 
  ggplot(aes(gender, day2)) +
  geom_boxplot() + 
  labs(
    x = "Gender"
    , y = "Hygiene"
  )


#################################
day3_hist <- dlf %>% 
  ggplot(
    aes(x=day3)
  ) + 
  geom_histogram(
    mapping = aes(y=..density..)
    , color = "black"
    , fill = "white"
    , binwidth = .1
  ) +
  labs(
    title = "Day 3 Histogram w/Normal Curve"
    , x = "Hygiene Score \n0(stanky) - 4(fresh)"
    , y = "Density"
  ) +  
  stat_function(
    fun = dnorm
    , args = list(
      mean = mean(dlf$day3, na.rm=TRUE)
      , sd = sd(dlf$day3, na.rm=TRUE)
    )
    , color = "blue"
    , size = 1
  )

day3_qq <- dlf %>%
  ggplot(aes(sample=day3)) +
  stat_qq_line(size=2, color="#4d4d4d") +
  stat_qq(size=3, color="blue", alpha=.2) + 
  labs(
    x = "Thoretical"
    , y = "Sample"
    , title = "Day 3 Q-Q Plot"
  )

day3_box <- dlf %>% 
  ggplot(aes(gender, day3)) +
  geom_boxplot() + 
  labs(
    x = "Gender"
    , y = "Hygiene"
  )

#################################


grid.arrange(day1_hist, day2_hist, day3_hist
             , day1_qq, day2_qq, day3_qq
             , day1_box, day2_box, day3_box
             , ncol=3, nrow=3)

stat.desc(
  cbind("day1"=dlf$day1, "day2"=dlf$day2, "day3"=dlf$day3)
  , basic=FALSE
  , norm=TRUE
  ) %>% 
  round(3) %>% 
  data.frame()

  
