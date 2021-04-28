# PCBS Nicolas Beauvais project

I am doing my PCBS project on coding and Implicit Association task, which aim is to determine the speed of two-by-two association between items of two categories. 
The Implicit Association Task (IAT) is supposed to provide a way to observe our "implicit" thoughts -- automatic associations that we may not be aware of and that are hard to control. This IAT measures how fast you can put words related to COVID-19 together with words like dangerous and harmless.
The project will be realized in Python and use Expyriment.

The two categories will consists in words: first category is word-types => it opposes words related to Covid-19 (Coronavirus, Flue, Shortness of breath) to words related to random other things (Sun, Ice, Window)
The second category relates to risk => it will oppose words related to Harm (Harmful, Danger, Risky) to words related to Safety (Harmless, Peaceful, Safe).

There are two blocks in the experiment:

In Block 1, the participant must press 's' when words presented relate to Covid-19 or to Harm, and press 'k' when words relate to Other things or to Safety.

In Block 2, the participant must press 's' when words presented relate to Other things or to Harm, and press 'k' when words relate to Covid-19 or to Safety.

If the participant missassociates a word (e.g. presses 's' while the correct answer was 'k'), an audio buzzer is played, as a negative feedback.

For both blocks and for each trial, the response time between the moment the word is presented and the pressing of the key ('s' or 'k') is recorded. 
At the end of the experiment, the data (Subject number, word presented, response key pressed*, reaction time, correct/false response) is saved in a .xpd file, which can be read for example with R. 
*Response key labels: 115 = s, 107 = k

