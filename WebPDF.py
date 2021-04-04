import os
import subprocess
import datetime

path_to_file = './Data'
name_of_file = 'Yahoo.pdf'
page_to_open = 'http://www.yahoo.co.jp'

command_to_run = '"/Applications/Google Chrome.app" --headless --print-to-pdf="{0}{1}" {2}'.format(path_to_file, name_of_file, page_to_open)
print('launch:'+command_to_run)

subprocess.Popen(['open', command_to_run])
print("Done")
