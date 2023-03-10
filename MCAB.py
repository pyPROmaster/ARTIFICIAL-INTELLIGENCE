from time import sleep
import pyautogui
import pydirectinput
import pyttsx3

# WALKERS : TO WALK

def walk_forward (duration=1, key='w') :
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def walk_backward (duration=1, key='s') :
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def walk_right (duration=1, key='d') :
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def walk_left (duration=1, key='a') :
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

# SPRINTER AND JUMP SPRINTERS : TO FAST WALK AND JUMP SPRINT 

def sprint_walk (duration=1, key='w') :
    pydirectinput.press(key)
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

#  JUMPERS AND CROUCHERS : TO JUMP AND CROUCH

def jump (key='Space') :
    pydirectinput.press(key)

def crouch (key='c') :
    pydirectinput.press(key)

# PLACERS AND DESTROYERS : TO PLACE AND DESTROY BLOCKS

def place_block (right_click='yes', key_to_place_block='y') :
    if right_click == 'yes' :
        pydirectinput.rightClick()
        
    else :
        pydirectinput.press(key_to_place_block)

def mine_block (duration_to_mine='1', key_to_mine_block='x') :
    pydirectinput.keyDown(key_to_mine_block)
    sleep(duration_to_mine)
    pydirectinput.keyUp(key_to_mine_block)

# EXTRA : PRESS 'Esc' or SPEAK

def speak (what_to_say) :
    engine = pyttsx3.init()
    engine.say(what_to_say)
    engine.runAndWait()

def press_Esc_to_start_game () :
    pydirectinput.press('Esc')