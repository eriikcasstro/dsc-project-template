# Capstone


## Introduction

Increment Instagram influence

This project is probably one of the most ambitious projects I have worked so far. There are different goals, firstly we need to understand what makes a person engage with an Instagram account, this will be specific for the theme I have chosen.
Secondly, this can be used to help someone already stablished with an Instagram account to further improve their engage with their audience and increment their followers 
However, the main goal is to use the recommendations given at the end of the study and get an Instagram account as far as possible. 
There is going to be involved Natural Language Processing, Time Series analysis (as a bench mark) , Machine learning for Classification and finally some AWS using EC2 and Lambda to run the scripts at certain times. 

## Business Problem

- Learn the practices that make an Instagram account popular. 
- This can benefit anyone that wants to build a presence in this social network platform.
- The goal of this study is to use the study to create an Instagram page and follow the recommendations  to grow an audience

## Findings 
### Exploratory Analysis
![image](https://user-images.githubusercontent.com/36000513/118202660-4ac9f700-b452-11eb-8010-b27925249dd0.png)

Within my data there were four different Instagram accounts, these accounts however, had the same theme. A theme: is a type of content that the Instagram account owner posts about. For example: cars, motorbikes, country. 
The theme I have chosen was a city : London. 
Getting the average, we can appreciate that the Instagram users that follow this kind of Instagram pages are more active Friday, Saturday and Sunday. 




Looking at each Instagram account individually we can differentiate how their followers react to their posts. 

![image](https://user-images.githubusercontent.com/36000513/118202734-70ef9700-b452-11eb-822a-ace5f2b0c22d.png)

Exploring London: gets more likes on Fridays, Saturday and Sundays.

![image](https://user-images.githubusercontent.com/36000513/118202780-86fd5780-b452-11eb-94a2-9016837bbd90.png)

Moving to London: gets more likes on Sundays, Tuesdays and Wednesdays 

![image](https://user-images.githubusercontent.com/36000513/118202786-89f84800-b452-11eb-9626-716d3ef62646.png)

Londonbeautifullife: on Fridays, Saturdays and Sundays

![image](https://user-images.githubusercontent.com/36000513/118202792-8cf33880-b452-11eb-9e42-5490994e20dd.png)

Lastly, Visit London: Saturday, Thursday and Wednesdays are where the average likes are higher.

I will now look at the what times are best to post:

![image](https://user-images.githubusercontent.com/36000513/118202923-d774b500-b452-11eb-8f7b-c2a6454c7c5a.png)

We can further Explore within the day, the time of the day with a higher average of likes, 
Due to the time constrain I will not be able to go through all the Instagram pages. However, Exploring London will serve as an example. 
We can see that posting on Monday at either 05am, 12pm or 21 gets the account more likes on average. 
Friday in the other hand, 13:00 and 14:.00 gets the most likes


### Caption Exploratory analysis
![image](https://user-images.githubusercontent.com/36000513/118202966-f2472980-b452-11eb-8656-8f6416ff5783.png)

![image](https://user-images.githubusercontent.com/36000513/118202970-f5421a00-b452-11eb-824b-f4f8640c99b8.png)

I conducted some text classification in the caption of the posts.  This allowed me to generate the best captions for the pictures. 
We can see the top 30 words used in the captions of the pictures.  For my surprise Hackney is number 30. 

### Time Series Analysis

![image](https://user-images.githubusercontent.com/36000513/118203067-30444d80-b453-11eb-8f7e-65b308be3f65.png)

I created this time series analysis to see where the Instagram pages will be in the future if they kept posting in a similar manner as they have had all this time. 
We can see that towards the end of the year the account tends to get more likes. We can appreciate that this happens in the predictions. However, the further the predictions are the less reliable it is


### Image Classification 

![image](https://user-images.githubusercontent.com/36000513/118203108-47833b00-b453-11eb-8f55-d188726af022.png)

Image classification was done with a totally different dataset, this dataset constituted of images of New York. The machine learning model was trained on this data but it was later used on my main London dataset. 
I had to manually classify 6.5k following a criteria. The model that performed better was Logistic Regression. We can see that the F1 score and the test Recall are higher than in the other models. Therefore, I decided to create my final model using Logistic Regression. 

## Recommendations

Post heavily on Fridays, Saturdays and Sundays.
On the weekends, post between 12:00 and 15:00, also between 19:00 and 21:00
Use top 30 Hashtags found on the post's captions. These are: 
London, thisislondon, shot, city, ldn, towerbridge, londoneye, Westminster, nottinghill, Instagram, bigben, photography, coventgarden, picadillycircus, stpaulscathedral, Camden, mayfair, theshard, southbank, soho, canarywharf, shreditch, buckinghampalace, trafalgarsquare, skyline, chinatown, leicestersquare, centrallondon,riverthames and hackney 


## Results 

![image](https://user-images.githubusercontent.com/36000513/118203166-684b9080-b453-11eb-8b46-137d324d3ec6.png)

![image](https://user-images.githubusercontent.com/36000513/118203173-6b468100-b453-11eb-9a49-ab07c2cc78e0.png)

I have included the results as an extra slide, I created an Instagram page and followed my recommendations. I used the 30 hashtags, posted +4 pictures each day on Friday, Saturday and Sunday. I posted other days as well, but not with the same intensity as on the weekend. 
I also followed some people, to make it look more genuine and evade Instagram from blocking my account 

![image](https://user-images.githubusercontent.com/36000513/118203209-7dc0ba80-b453-11eb-98cc-f37f4508e2fb.png)

![image](https://user-images.githubusercontent.com/36000513/118203227-84e7c880-b453-11eb-8b82-31772e0ff2f7.png)

![image](https://user-images.githubusercontent.com/36000513/118203232-87e2b900-b453-11eb-8a06-dbf0ca620c38.png)


We can see that these pictures show the amount of likes on each picture, we have a progressive increase on them. First picture was posted at the beginning of February with 3,218 likes, second picture was posted at the end of February and has 4,885 likes. Last picture was on March and it had 5,755 likes. This means that following the recommendations will help this particular Instagram themed to increase their engage and their followers. 
To Finalize this project I decided to sell this account, this was done smoothly and at a really good price. 




