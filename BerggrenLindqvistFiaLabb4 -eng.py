"""
Fia Berggren Lindqvist
Windows 10
"""

#Import Tkinter
import tkinter
import tkinter.messagebox

#Creates the main window, a label and a textbox made for input
main_window = tkinter.Tk()
label_text = "Fahrenheit to Celsius \n Enter the number of degrees to convert"
main_label = tkinter.Label(main_window, text = label_text, bg= "#dcdcdc", font = 35, \
                           height = 12, width = 50)
user_input = tkinter.Entry(main_window, width = 10)

#Calls the various functions to create the main window
def main():
    create_main_window()
    create_top_frame()
    create_bottom_frame()
    tkinter.mainloop()

#Main window function
def create_main_window():
    main_window.geometry("550x350+100+100")
    main_window.title("ID:INP - Temperatur converter")

#The screen is devided into two parts, and this is the upper part in the shape of
#informative text and also feedback
def create_top_frame():
    top_frame = tkinter.Frame(main_window, bg = "#b72a4d")
    top_frame.grid()
    main_label.grid(row = 0, rowspan = 1, column = 0, columnspan = 3)

#This is the lower part of the screen that has a label, a box for user input and a button
def create_bottom_frame():
    bottom_frame = tkinter.Frame(main_window, bg = "#adadad")
    create_second_label()
    create_input_box()
    create_button()

#This text belongs to the lower part of the main window
def create_second_label():
    second_label = tkinter.Label(main_window, text = "Enter the number of degrees ==>", font = 4)
    second_label.grid(row = 1, rowspan = 1, column = 0, columnspan = 1)

#The user input in the lower part of the main window
def create_input_box():
    user_input.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, pady = 20)

#Button that initiate execution of the conversion
def create_button():
    convert_button = tkinter.Button (main_window, text = "Convert", command = action, bg = "#7f9780")
    convert_button.grid(row = 1, rowspan = 1, column = 2, columnspan = 1)

#The function that does the conversion, with float to convert everything to
#decimal numbers, robust programs to provide feedback on the wrong type of input are provided and
#with the if-rate, it will change the look depending on what the result will be

def action():
    fahrenheit = user_input.get()
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
        if celsius > 0 and fahrenheit != 1337:
            celsius = str("{:.2f}".format(celsius))
            fahrenheit = str(fahrenheit)
            label_message = ("The temperature in Celsius is " + celsius)
            main_label.config(bg = "red", text = label_message)
        elif celsius < 0:
            celsius = str("{:.2f}".format(celsius))
            fahrenheit = str(fahrenheit)
            label_message = ("The temperature in Celsius is " + celsius)
            main_label.config(bg = "blue", text = label_message)
        else:
            celsius = str("{:.2f}".format(celsius))
            fahrenheit = str(fahrenheit)
            label_message = ("The temperature in Celsius is " + celsius)
            main_label.config(bg = "#dcdcdc", fg = "#000000", text = label_message)
    except ValueError:
            error_message = ("Wrong type of input, please enter numbers")
            main_label.config(text = error_message)
        

main()
