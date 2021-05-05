# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:55:21 2021

Project PCBS NBeauvais - Implicit Association Task

@author: nicol
NicolasBeauvais
"""

# Libraries
import random
from expyriment import design, control, stimuli, misc 

RESPONSE_key1 = misc.constants.K_s
RESPONSE_key2 = misc.constants.K_k 
BUZZER = 'wrong-answer.ogg'

MAX_RESPONSE_DELAY = 3000
TARGETS = ["Coronavirus", "Flue", "Shortness of breath",
           "Harmful", "Danger", "Risky",
           "Sun", "Window", "Ice",
           "Peaceful", "Safe", "Harmless"] * 2
random.shuffle(TARGETS)

dict_block1 = {"Coronavirus": RESPONSE_key1, "Flue":RESPONSE_key1, "Shortness of breath": RESPONSE_key1,
           "Harmful":RESPONSE_key1, "Danger":RESPONSE_key1, "Risky":RESPONSE_key1,
           "Sun":RESPONSE_key2, "Window":RESPONSE_key2, "Ice":RESPONSE_key2,
           "Peaceful":RESPONSE_key2, "Safe":RESPONSE_key2, "Harmless":RESPONSE_key2}

dict_block2 = {"Coronavirus": RESPONSE_key2, "Flue":RESPONSE_key2, "Shortness of breath": RESPONSE_key2,
           "Harmful":RESPONSE_key1, "Danger":RESPONSE_key1, "Risky":RESPONSE_key1,
           "Sun":RESPONSE_key1 ,"Window":RESPONSE_key1, "Ice":RESPONSE_key1,
           "Peaceful":RESPONSE_key2, "Safe":RESPONSE_key2, "Harmless":RESPONSE_key2}


exp = design.Experiment(name="Implicit Association Task", text_size=20)

control.initialize(exp)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions1 = stimuli.TextScreen("INSTRUCTIONS",
    f"""Words will be displayed at the center of the screen.
    When you see the word, your task is to decide, as quickly as possible,
    to which category it belongs. There will be two blocks.
    
    BLOCK 1:
    If the word is related to COVID-19 (Coronavirus, Flue, Shortness of breath)
    or to HARM (Harmful, Danger, Risky), press '{chr(RESPONSE_key1)}'
    
    If it is related to OTHER CATEGORIES (Sun, Window, Ice,)
    or to SAFETY (Harmless, Peaceful, Safe), press '{chr(RESPONSE_key2)}'

    There will be {len(TARGETS)} trials in each block.
    A Buzzer sound will be displayed if you answer wrong, 
    make sure your volume isn't too high.
    Press any key to start.""", position= None, heading_font = None,
    heading_size=40, heading_bold=True, text_justification=1)

instructions2 = stimuli.TextScreen("INSTRUCTIONS",
    f"""Good job ! Continue like this, and try to respond as quickly as possible. 
    WATCH OUT: THE ASSOCIATED CATEGORIES ARE NOW DIFFERENT:
    
    BLOCK 2:
    If the word is related to OTHER CATEGORIES (Sun, Window, Ice,) 
    or to HARM (Harmful, Danger, Risky), press '{chr(RESPONSE_key1)}'
    
    If it is related to COVID-19 (Coronavirus, Flue, Shortness of breath)
    or to SAFETY (Harmless, Peaceful, Safe), press '{chr(RESPONSE_key2)}'

    There will be {len(TARGETS)} trials in the block.
    Press any key to start.""", position= None, heading_font = None,
    heading_size=40, heading_bold=True, text_justification=1)
    
# Prepare the stimuli
trials = []
for word in TARGETS:
    trials.append((word, stimuli.TextLine(str(word))))


exp.add_data_variable_names(['word', 'respkey', 'RT', 'correct association'])

########## Start the experiment ##########
control.start(skip_ready_screen=True)

### Block 1 ###
instructions1.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    t[1].present()
    key, rt = exp.keyboard.wait([RESPONSE_key1, RESPONSE_key2],duration=MAX_RESPONSE_DELAY)
    is_correct = dict_block1[t[0]] == key
    if dict_block1[t[0]] != key:
        negative_feedback = stimuli.Audio(BUZZER)
        negative_feedback.play()
        print('Wrong answer')
    exp.data.add([t[0],  key, rt, is_correct])

### Block 2 ###
print('Block 2:')
exp.data.add('Block2')
instructions2.present() 
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    t[1].present()
    key, rt = exp.keyboard.wait([RESPONSE_key1, RESPONSE_key2], duration=MAX_RESPONSE_DELAY)
    is_correct2 = dict_block2[t[0]] == key
    if dict_block2[t[0]] != key:
        negative_feedback = stimuli.Audio(BUZZER)
        negative_feedback.play()
        print('Wrong answer')
    exp.data.add([t[0], key, rt, is_correct2])
    
control.end()


### END ###
