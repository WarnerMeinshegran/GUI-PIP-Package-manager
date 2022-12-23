import PySimpleGUI as sg
import subprocess
from sys import exit as sysexit
from os import remove as remove_file
from webbrowser import open as open_link


"""
app created at:Nov26ᵗʰ, 2022
Todo: (! = done)
-!About package(pip show)
-Autocomplete 
-if about package is empty tell user that no package found
-!uninstall
"""


# Application Name related variables
ICON_BASE64 = b"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"
LONG_APP_NAME = "GUI Pip Package Manager"
SHORT_APP_NAME = "GUI PPM"

# Application vesrion related variables
__version__ = 1.0
LATEST_UPDATE_DATE = "Nov29ᵗʰ, 2022"

# about Application related variables
ABOUT_APP = f"""______|About|______
{LONG_APP_NAME}(short form:{SHORT_APP_NAME})
Version: {__version__} (released at {LATEST_UPDATE_DATE})
Description:
Easily manage the installed packages in your system."""

# Application license related variables
APP_LICENSE = f"{LONG_APP_NAME} is licensed under CC BY-SA 4.0.\nTo view a copy of this license,\nvisit http://creativecommons.org/licenses/by-sa/4.0/ or click me"
LICENSE_LINK = "http://creativecommons.org/licenses/by-sa/4.0/"
LICENSE_IMAGE = b"iVBORw0KGgoAAAANSUhEUgAAAFAAAAAPCAMAAABEF7i9AAAABGdBTUEAANbY1E9YMgAAAJZQTFRF////7u7u3d3dys7KzMzMyMzIxsrGxcbFur+6u7u7s7iyq7GqqqqqmZmZlJmTj5CPiIiIh4eHhoaGgICAfYJ9d3d3cnZxZ2tnZmZmW15bVVVVS0xLREREQ0NDQkJCQUJBOz07OTs5MzMzMTMxLjAuJygnJCUjIiIiISEhICAgGRkZERERDxAPDg4ODQ4NDQ0NDQ0MAAAADbeuvgAAAMNJREFUeNqtk9sSgiAQQJekslaNLpgZ3exiZWr7/z/XEI6N00spO/DCMocDywJZDiCwGhqIOpYkqiWVB4jOo7WfAQa5qA9RZ0R33hG4v36sOa0Q++tuwEIAT0kxRSkHdUR0Ju88gN5k5j/ABY0gjUHKjPkeyALRHZq8GfCvYUic6arEib6zzBHHg9rwd78vQxVlTPogy6ZhCyCWAryMIqYo6cHm1HjDVsDDzXKVg+e0Bm4vFv4hhjSreLt7106x3cuW4wXCCZ5As6hO5AAAAABJRU5ErkJggg=="
CREDITS="""______|Credits|______
blabla_lab  | Developer
PySimpleGUI | GUI library"""


# Variables
results_file_name = "results.txt"



# Functions
def run_command(command, save_output=False):
    result = subprocess.run([command], capture_output=True, text=True, shell=True).stdout # run command
    if save_output:
        with open(results_file_name, "w") as result_file:
            result_file.write(result)
    else:
        return result


try:
    # package_list = " | version: ".join(str(run_command("pip list --format freeze")).split("=="))

    # UI settings
    sg.theme('DarkAmber')   
    sg.theme_border_width(0)
    sg.set_options(font=(None,14), icon=ICON_BASE64, debug_win_size=1)

    # Window
    layout = [  [sg.Image(ICON_BASE64, subsample=2, k="-ICON CLICK-", enable_events=True), sg.Text(f"{SHORT_APP_NAME} {__version__}")],
                [sg.Text('Packages found in your system:')],
                [sg.Multiline(" | version: ".join(str(run_command("pip list --format freeze")).split("==")), size=(40,15), disabled=True, sbar_relief=sg.RELIEF_FLAT, auto_refresh=True, horizontal_scroll=True, k="-PACK-")],
                [sg.Text("Package Name:") ,sg.Input('', size=17, key='-p-')],
                [sg.B('Uninstall the package', k="-UNINSTALL BUTTON-"), sg.B("About the package"), sg.B('Quit'), sg.B("Refresh"), sg.T("READY", k="-STATS-", relief=sg.RELIEF_SUNKEN, border_width=3, background_color="Gray")],
                ]

    window = sg.Window(SHORT_APP_NAME, layout, debugger_enabled=False)
    
    
    
    # Event Loop
    while True:
        event, values = window.read()      
        if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
            sysexit(0)
            
        elif event == '-UNINSTALL BUTTON-': 
            window["-STATS-"].Update("UNINSTALLING")
            window["-UNINSTALL BUTTON-"].update(disabled=True)
            window.Refresh()
            window.perform_long_operation(lambda: run_command(f"pip uninstall {str(values['-p-']).lower()} -y -v --no-input", True), '-UNINSTALL COMPLETED-')
        
        elif event == "-UNINSTALL COMPLETED-":
            window["-STATS-"].Update("DONE")
            with open(results_file_name) as opened_file:
                sg.popup_scrolled(opened_file.read(), title="Output", size=(25,15))
            try:
                remove_file(results_file_name)
            except Exception:
                pass
            window["-UNINSTALL BUTTON-"].update(disabled=False)
            window["-STATS-"].Update("READY")
            
        elif event == "About the package":
            window["-STATS-"].Update("BUSY")
            sg.popup(run_command(f"pip show {str(values['-p-']).lower()}"), title="Output")
            window["-STATS-"].Update("READY")

        elif event == "Refresh":
            window["-PACK-"].update(" | version: ".join(str(run_command("pip list --format freeze")).split("==")))
        
        elif event == "-ICON CLICK-":
            about_layout = [
                            [sg.Image(ICON_BASE64, subsample=2, enable_events=True, k="-FULL ICON-"), sg.T(LONG_APP_NAME)],
                            [sg.Text(ABOUT_APP)],
                            [sg.Text(APP_LICENSE, enable_events=True, key="-ABOUT LICENSE LINK-")],
                            [sg.Image(LICENSE_IMAGE)],
                            [sg.B('Credits'), sg.B('Close')] ]
            
            about_window = sg.Window(f'About {SHORT_APP_NAME}', about_layout, debugger_enabled=False)
            
            while True:
                event, values = about_window.read()
                
                if event == sg.WIN_CLOSED or event == 'Close': 
                    break
                
                elif event == "-ABOUT LICENSE LINK-":
                    open_link(LICENSE_LINK)
                    
                elif event == "Credits":
                    sg.popup_ok(CREDITS, title="Credits")
                    
                elif event == "-FULL ICON-":
                    sg.popup("", image=ICON_BASE64)
            
            about_window.close()
            
            
    window.close()


except Exception as err:
    sg.popup_error(f"Error\n{err}")
    sysexit(1)
