import pyautogui
import time
import pyperclip
import supervision as sv
import opbr_colour_module as cm
import random

def get_result_info(results, view=False):
    """
    Extracts information from YOLOv5 detection results.

    Args:
        results (List): List of detection results.
        view (bool, optional): Whether to display the detection image. Defaults to False.

    Returns:
        int: Class ID of the detected object.
        int: X-coordinate of the detected object.
        int: Y-coordinate of the detected object.
        list: List of class names.
    """
    try:
        if results is not None:
            for result in results:
                boxes = result.boxes
                speed = result.speed
                classes = result.names

                if len(boxes.cls) > 0:
                    c_id = int(boxes.cls[0])
                    x1, y1, x2, y2 = (boxes.xyxy)[0].numpy()
                    mx = int(round((x1 + x2) / 2, 0))
                    my = int(round((y1 + y2) / 2, 0))

                    if view:
                        npimage = result.plot()
                        midpoint = sv.Point(mx, my)
                        npimage = sv.draw_text(scene=npimage, text="XOXO", text_anchor=midpoint, text_thickness=5)
                        sv.plot_image(image=npimage, size=(10, 7))

                    return c_id, mx, my, classes
    except Exception as e:
        print(f"Error occurred -> {e}")

    return None, None, None, None

def check_cache(counter, class_cache_buffer):
    """
    Checks the cache for consistent detection issues.

    Args:
        counter (int): The current processing counter.
        class_cache_buffer (list): List of detected class IDs.

    Returns:
        list: Updated class_cache_buffer.
    """
    iterations = 10
    repeat_value = class_cache_buffer[-1]
    repeat_value_count = class_cache_buffer.count(repeat_value)

    threshold = int(iterations * 0.7)
    exceptions = ["combat", "punch"]

    if repeat_value_count >= threshold and repeat_value not in exceptions:
        if repeat_value_count == "next":
            handle_next_button()
        print(f"{cm.RED}Warning: Consistent Detection Issue, Initiating Home Button Action!{cm.RESET}")
        pyautogui.press('esc')
        class_cache_buffer.clear()
    
    return class_cache_buffer

def handle_next_button():
    """
    Handles the 'next' button action.
    """
    for i in range(6):
        print("triggering handle_next_button")
        pyautogui.press('esc')




def automate_clicks(c_id, mx, my, classes, class_cache_buffer, flag=True):
    """
    Performs automated clicks based on detected class IDs.

    Args:
        c_id (int): Class ID of the detected object.
        mx (int): X-coordinate of the detected object.
        my (int): Y-coordinate of the detected object.
        classes (list): List of class names.
        class_cache_buffer (list): List of detected class IDs.
        flag (bool, optional): Flag for bot operation. Defaults to True.

    Returns:
        list: Updated class_cache_buffer.
        bool: Updated flag.
    """
    # Define combat_listclass IDs and mouse click coordinates
    combat_list= [22, 23, 32, 33, 34]
    pass_list = [16, 25, 35]
    combat_mxy_list = [(770, 430), (791, 332), (871, 301), (227, 375)]

    if len(class_cache_buffer) >= 10:
        class_cache_buffer.pop(0)

        if c_id in range(0,len(classes)):

            if c_id == 0: #title 
                pyautogui.click(x=159, y=36,duration=.5, button='left', clicks=1, interval=0.25)


            elif c_id == 7:   #change_party                
                #slot2
                pyautogui.moveTo(659, 154,1)
                pyautogui.dragTo(541, 190, duration=1)

                #ok button
                pyautogui.click(x=504, y=344,duration=1, button='left', clicks=1, interval=0.25)

                #slot1
                pyautogui.moveTo(659, 154,1)
                pyautogui.dragTo(296,190 , duration=1)

                #ok button
                pyautogui.click(x=504, y=344,duration=1, button='left', clicks=1, interval=0.25)

                #home button
                pyautogui.click(x=159, y=36,duration=.5, button='left', clicks=1, interval=0.25)

            

            elif c_id == 8: #claimed
                #time.sleep(3) 
                pyautogui.click(x=mx, y=my,duration=.5, button='left', clicks=1, interval=0.25)
                #time.sleep(5) 


            elif c_id == 10: #edit_party
                my -= 25
                pyautogui.click(x=mx, y=my,duration=.5, button='left', clicks=1, interval=0.25)


            elif c_id == 12: #finger down
                my += 25
                pyautogui.click(x=mx, y=my,duration=.5, button='left', clicks=1, interval=0.25)


            elif c_id == 13: #free button
                my += 30
                pyautogui.click(x=mx, y=my,duration=.5, button='left', clicks=1, interval=0.25)


            elif c_id == 14: #home 
                pyautogui.click(x=mx, y=my,duration=.5, button='left', clicks=1, interval=0.25)
                pyautogui.click(x=150, y=35,duration=.5, button='left', clicks=1, interval=0.25)

            elif c_id in combat_list:
                ran_mxy = random.choice(mxy_list)
                pyautogui.click(x=ran_mxy[0], y=ran_mxy[1],duration=.5, button='left', clicks=1, interval=0.25)
                time.sleep(1)

            elif c_id == 18 : #name
                #ok 510,340
                pyautogui.click(x=501, y=183,duration=.5, button='left', clicks=1, interval=0.25) #click name      
                pyautogui.click(x=94, y=450, duration=.5, button='left', clicks=1, interval=0.25) #click keyboard
                pyautogui.write('naka', interval=0.25)#keyboard
                pyautogui.click(x=910, y=450, duration=1, button='left', clicks=1, interval=0.25)#ok button
                pyautogui.click(x=517, y=351, duration=.5, button='left', clicks=1, interval=0.25)#ok button
                pyautogui.click(x=662, y=352, duration=.5, button='left', clicks=1, interval=0.25)#ok button

            elif c_id == 24: #commend 
                my += 34
                mx += -2
                pyautogui.click(x=mx, y=my,duration=.5, button='left', clicks=1, interval=0.25)


            elif c_id in pass_list: #battle loading, loading
                pass
                     

            elif c_id == 27: #profile
                #close button
                pyautogui.click(x=70, y=36,duration=.5, button='left', clicks=1, interval=0.25)


            elif c_id == 31: #already claimed
                #home button
                pyautogui.click(x=159, y=36,duration=.5, button='left', clicks=1, interval=0.25)
                time.sleep(2)
                print(f"{cm.LIME}Tutorial is completed. Registering account now...{cm.RESET}")
                register_account()
                print("Account registered successfully! Terminating the bot...")
                flag = False


            elif c_id == 36: #profile
                #close button
                pyautogui.click(x=159, y=36,duration=.5, button='left', clicks=1, interval=0.25)

            
            else: #home button
                pyautogui.click(x=mx, y=my,duration=.75, button='left', clicks=1, interval=0.25)
                #time.sleep(.5)
            class_cache_buffer.append(c_id)

        else: 
            print(f"Process counter : {counter}, no class detected!")
            #pyautogui.press('esc')
            class_cache_buffer.append(None)
        
    return class_cache_buffer, flag

def register_account():
    """
    Registers a game account.
    """
    # Perform actions to register an account

    time.sleep(4)

    pyautogui.click(x=998, y=89,duration=1, button='left', clicks=1, interval=0.25) # more details
    pyautogui.click(x=520, y=275,duration=.75, button='left', clicks=1, interval=0.25) # link data
    pyautogui.click(x=522, y=442,duration=1, button='left', clicks=1, interval=0.25)

    pyautogui.click(x=549, y=279,duration=1, button='left', clicks=1, interval=0.25)
    pyautogui.click(x=537, y=201,duration=1, button='left', clicks=1, interval=0.25) #password
    pyautogui.click(x=177, y=454,duration=1, button='left', clicks=1, interval=0.25) #key
    pyautogui.write('qwertyui', interval=0.15)#keyboard
    pyautogui.click(x=924, y=455,duration=1, button='left', clicks=1, interval=0.25) #ok
    time.sleep(1)
    pyautogui.click(x=509, y=286,duration=1, button='left', clicks=1, interval=0.25) #register
    time.sleep(1.5)
    pyautogui.click(x=793, y=315,duration=1, button='left', clicks=1, interval=0.25) #scroll
    #pyautogui.moveTo(x=793, y=387, duration = 1)
    pyautogui.dragTo(x=793, y=387, duration=1) #drag
    pyautogui.click(x=236, y=457,duration=1, button='left', clicks=1, interval=0.25) #conf
    screenshot = pyautogui.screenshot()

    pyautogui.click(x=684, y=163,duration=1, button='left', clicks=1, interval=0.25) #copy id
    user = pyperclip.paste()
    pyautogui.click(x=515, y=358,duration=1, button='left', clicks=1, interval=0.25) #close

    pyautogui.click(x=688, y=202,duration=1, button='left', clicks=1, interval=0.25) #copy pw
    pw = pyperclip.paste()
    pyautogui.click(x=515, y=358,duration=1, button='left', clicks=1, interval=0.25) #close
 
    # Save the screenshot as an image file

    screenshot.save('screenshot.png')
    with open("logger.txt", "a") as file:
        # Add a new line to the file
        file.write('\n' + user + ' -> ' + pw)
    print(f"Saved account/password in logger.txt \nUsername : {user}\nPassword : {pw}")
    pyautogui.click(x=513, y=452,duration=1, button='left', clicks=1, interval=0.25) #close


if __name__ == "__main__":
    # Example usage or testing code can be placed here.
    pass
