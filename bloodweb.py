import pyautogui
import time
import random


XX = None
YY = None

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

    prompt = "\nChoose one item to farm: (Ctrl+C to quit)\n"
    for item in item_lists.keys():
        prompt += f"- {item}\n"
    prompt += "> "

    while retries < max_retries:
        try:
            main_item = input(prompt).lower().strip()
            main_list = item_lists[main_item]
            return main_list
        except KeyError:
            print("\nItem not found!")
            retries += 1
        except KeyboardInterrupt:
            print("\nQuitting...")
            return None
    print("\nMax retries reached, learn how to type!")
    return None

def next_bloodweb():
    global XX, YY
    center_node = "Items/center-node.png"
    try:
        print("Changing Bloodweb...")
        location = pyautogui.locateOnScreen(center_node, confidence=0.8, grayscale=True)
        if location:
            center_x, center_y = pyautogui.center(location)
            XX, YY = center_x, center_y
            pyautogui.moveTo(center_x, center_y)
            pyautogui.mouseDown()
            time.sleep(random.uniform(0.8, 1.2))
            pyautogui.mouseUp()
            pyautogui.moveTo(0, 0)
            time.sleep(random.uniform(4.5, 5.5))
        else:
            print("Center node not found...")
            prestige()
    except pyautogui.ImageNotFoundException:
        print("Center node not found. Attempting prestige...")
        prestige()

def prestige():
    global XX, YY
    if XX is None or YY is None:
        print("No valid prestige coordinates. Skipping prestige.")
        return
    print("Clicking prestige button...")
    pyautogui.moveTo(XX, YY)
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.8, 1.2))
    pyautogui.mouseUp()
    pyautogui.moveTo(0, 0)
    time.sleep(random.uniform(3.5, 4.5))

def mouse_click_event():
    main_list = get_item_list()
    if main_list is None:
        print("No item selected. Exiting click event.")
        return
    main_list_length = len(main_list)
    print(main_list)

    print("\nScript starting...")
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
                location = pyautogui.locateOnScreen(item, confidence=0.75, grayscale=True)
                if location:
                    pyautogui.moveTo(location)
                    print("Item found!!!!")
                    pyautogui.mouseDown()
                    time.sleep(random.uniform(0.8, 1.2))
                    pyautogui.mouseUp()
                    pyautogui.moveTo(0, 0)
                    time.sleep(random.uniform(1.5, 2.5))
                else:
                    print("Item not found...")
            except pyautogui.ImageNotFoundException:
                print("Item not found...")
                time.sleep(0.5)
            index += 1
        next_bloodweb()
        index = 0

def main():
    pyautogui.FAILSAFE = True
    mouse_click_event()

if __name__ == "__main__":
    main()
