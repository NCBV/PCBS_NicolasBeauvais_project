# PCBS Nicolas Beauvais project

My PCBS project is the coding of an Implicit Association task, which aim is to determine the speed of two-by-two association between items of two categories. 
The Implicit Association Task (IAT) is supposed to provide a way to observe our "implicit" thoughts -- automatic associations that we may not be aware of and that are hard to control. This IAT measures how fast you can put words related to COVID-19 together with words like dangerous and harmless. The underlying idea is that the more strongly you associate COVID-19 with a concept, the faster you can perform the task when those two concepts are paired in your response.
The project is realized in Python and uses Expyriment.

The two categories will consists in words: first category is word-types => it opposes words related to Covid-19 (Coronavirus, Flue, Shortness of breath) to words related to random other things (Sun, Ice, Window)
The second category relates to risk => it will oppose words related to Harm (Harmful, Danger, Risky) to words related to Safety (Harmless, Peaceful, Safe).

There are two blocks in the experiment:

In Block 1, the participant must press 's' when words presented relate to Covid-19 or to Harm, and press 'k' when words relate to Other things or to Safety.

In Block 2, the participant must press 's' when words presented relate to Other things or to Harm, and press 'k' when words relate to Covid-19 or to Safety.

If the participant missassociates a word (e.g. presses 's' while the correct answer was 'k'), an audio buzzer is played, as a negative feedback.

For both blocks and for each trial, the response time between the moment the word is presented and the pressing of the key ('s' or 'k') is recorded. 
At the end of the experiment, the data (Subject number, word presented, response key pressed*, reaction time, correct/false response) is saved in a .xpd file, which can be read for example with R. 
*Response key labels: 115 = s, 107 = k

# How to run the experiment:
Click on Code > Download ZIP and extract it on your computer. Then open a terminal, change the directory to where you saved the files, then type in: python Association-task-code_main.py
Then follow the instructions untill the end of the experiment. 

# Note: 
There is controversy about the IAT in the scientific literature, about its validity at external and internal levels. 
It is thought that implicit associations come from one's personal experiences and also society's views, this is also the case for COVID-19. It is important to realize that people's implicit thoughts do not always match what they say about themselves, and that this test isn't meant to diagnose anything about the participants.
The author of the code does not endorse any specific position regarding the IAT paradigm, this experiment is realized as a coding project for a programming course.  
For more details see https://en.wikipedia.org/wiki/Implicit-association_test and the criticism and controversies section.
If you are interested by IATs, and perhaps taking other tests, see https://implicit.harvard.edu/implicit/iatdetails.html

