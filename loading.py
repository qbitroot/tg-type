import pyautogui
import pyperclip
from time import sleep

old_clip = pyperclip.paste()

print("Sleeping for 3 seconds...")
sleep(3)

def enter(text):
	pyperclip.copy(text)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')
	sleep(0.2)

lim = 10 #*2 = 20
for i in range(lim):
	enter(f"[{('█'*i*2).ljust(lim*2, '░')}]")
	pyautogui.press('up')

enter(f"[{'█'*lim*2}]")
pyautogui.press('up')
enter(f"[{'█'*(lim-6) + '▓▒░ DONE ░▒▓' + '█'*(lim-6)}]")

# restore clipboard
pyperclip.copy(old_clip)
