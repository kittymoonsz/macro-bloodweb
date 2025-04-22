import pyautogui
from PIL import ImageGrab
import time
import cv2
import numpy as np
import screeninfo

CONFIDENCE = 0.6
CENTER_NODE = "Items/center-node.png"

toolbox_list = ["Items/toolbox-purple.png", "Items/toolbox-greenM.png", "Items/toolbox-yellow.png", "Items/toolbox-white.png"]
key_list = ["Items/key-red.png", "Items/key-purple.png", "Items/key-green.png"]
map_list = ["Items/map-red.png", "Items/map-green.png"]
medkit_list = ["Items/medkit-purple.png", "Items/medkit-green.png", "Items/medkit-yellow.png", "Items/medkit-white.png"]
flashlight_list = ["Items/flashlight-purple.png", "Items/flashlight-green.png", "Items/flashlight-yellow.png"]

def get_item_list():
    item_lists = {
        "flashlight": flashlight_list,
        "key": key_list,
        "map": map_list,
        "medkit": medkit_list,
        "toolbox": toolbox_list
    }

    max_retries = 3
    retries = 0

    prompt = "\nchoose one item to farm: (ctrl + c to quit)\n"
    for item in item_lists.keys():
        prompt += f"- {item}\n"
    prompt += "> "

    while retries < max_retries:
        try:
            main_item = input(prompt).lower().strip() 
            main_list = item_lists[main_item]
            return main_list
        except KeyError:
            print("\nitem not found!")
            retries += 1
        except KeyboardInterrupt:
            print("\nquitting...")
            return None
    print("\nmax retries reached, learn how to type!")
    return None

def mouse_click_event():
    main_list = get_item_list()
    try:
        main_list_length = len(main_list)
    except TypeError:
        return
    print(main_list)

    print("\nscript starting...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    
    index = 0
    while True:
        while index < main_list_length:
            item = main_list[index]
            try:
                location = pyautogui.locateOnScreen(item, confidence=0.75)
                if location:
                    pyautogui.moveTo(location)
                    print("item found!!!!")
                    pyautogui.mouseDown()
                    time.sleep(1)
                    pyautogui.mouseUp()
                    pyautogui.moveTo(0,0)
                    time.sleep(2)
                else:
                    print("item not found...")
            except pyautogui.ImageNotFoundException:
                print("item not found...")
                time.sleep(0.5)
            index += 1
        next_bloodweb()
        index = 0
        
def next_bloodweb():
    center_node = "Items/center-node.png"
    try:
        print("changing bloodweb...")
        pyautogui.moveTo(pyautogui.locateOnScreen(center_node, confidence=0.8))
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        pyautogui.moveTo(0, 0)
        time.sleep(5)
    except pyautogui.ImageNotFoundException:
        print("prestige?")
        return

def main():
    mouse_click_event()

if __name__ == "__main__":
    main()



