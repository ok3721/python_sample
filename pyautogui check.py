import pyautogui
import time

# Image file path
image_path = 'image.png'

# Timeout in seconds
timeout = 10

start_time = time.time()
while time.time() - start_time < timeout:
    # Check if the image is present on the screen
    image_location = pyautogui.locateOnScreen(image_path)
    
    # If the image is present
    if image_location:
        # Perform the next action
        print("Image found, proceed to next action")
        break
    else:
        # Wait for a second before checking again
        print("Waiting for image to appear...")
        time.sleep(1)
else:
    print("Timeout: Image not found")
