import pyautogui
import pyperclip
from time import sleep

old_clip = pyperclip.paste()

print("Enter message then focus to telegram message input")
text = input("Message to send: ")
gap = int(input("How many symbols to type every step? (default:3) ")) or 3
print("Sleeping for 3 seconds...")
sleep(3)

i = 0
while True:
	old_gap = gap
	if i >= len(text): break
	to_write = text[i:i+gap]
	while to_write[-1] == ' ':
		gap += 1
		to_write = text[i:i+gap]
	pyperclip.copy(to_write)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')
	sleep(0.1)
	pyautogui.press('up')
	sleep(0.1)
	i += gap
	gap = old_gap

# restore clipboard
pyperclip.copy(old_clip)
