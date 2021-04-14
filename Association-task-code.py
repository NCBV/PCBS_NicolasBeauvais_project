# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:55:21 2021

Project PCBS NBeauvais - Implicit Association Task

@author: nicol
NicolasBeauvais
"""

#libraries
import random
from expyriment import design, control, stimuli

MAX_RESPONSE_DELAY = 2000
TARGETS = ["Coronavirus", "Flue", "Shortness of breath",
           "Harmful", "Danger", "Disease",
           "Sun", "Window", "Ice",
           "Peaceful", "Safe", "Harmless"]
random.shuffle(TARGETS)

RESPONSE_key1 = 's'
RESPONSE_key2 = 'l'

exp = design.Experiment(name="Implicit Association Task", text_size=20)
control.initialize(exp)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("INSTRUCTIONS",
    f"""When you'll see a word, your task is to decide, 
    as quickly as possible,
    to which category it belongs.
    if it is related to COVID-19 (Coronavirus, Flue, Shortness of breath)
    or to Harm (Harmful, Danger, Disease), press '{RESPONSE_key1}'
    if it is related to Other categories (Sun, Window, Ice,)
    or to Harmless (Harmless, Peaceful, Safe), press '{RESPONSE_key2}'

    There will be {len(TARGETS)} trials in total.
    Press the space bar to start.""", position=None, heading_font= None,
    heading_size=40, heading_bold=True, text_justification=1)

# prepare the stimuli
trials = []
for word in TARGETS:
    trials.append((word, stimuli.TextLine(str(word))))


exp.add_data_variable_names(['number', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    t[1].present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([t[0],  key, rt])

control.end()


### When you'll see a word, your task is to decide, as quickly as possible,
   # to which category it belongs.

   # if it is related to COVID-19 (Coronavirus, Flue, Shortness of breath)
   # or to Harm (Harmful, Danger, Disease), press '{RESPONSE_1}'

    #if it is related to Other categories (Sun, Window, Ice,)
    #or to Harmless (Harmless, Peaceful, Safe), press '{RESPONSE_2}'

 #   There will be {len(TARGETS)} trials in total.
#    Press the space bar to start.