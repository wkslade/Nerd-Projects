import time
from datetime import datetime
from datetime import timedelta

current_date_and_time = datetime.now()
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
#the following are important globlal variables for when we are calculateing their times for each of my classes
Math_time = timedelta(0)
Math_start = timedelta(0)
math_button_press = False
Ecen_250_time = timedelta(0)
Ecen_250_start = timedelta(0)
Ecen_250_button_press = False
Ecen_240_time = timedelta(0)
Ecen_240_start = timedelta(0)
Ecen_240_button_press = False
Cse_121c_time = timedelta(0)
Cse_121c_start = timedelta(0)
Cse_121c_button_press = False
Cse_210_time = timedelta(0)
Cse_210_start = timedelta(0)
Cse_210_button_press = False
Rel_time = timedelta(0)
Rel_start = timedelta(0)
Rel_button_press = False
Total_home_work_time = timedelta(0)











def main():

        # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Class Timer")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()



# def proof_of_consept_stopwatch():
#     input("hit enter to start stopwatch")
#     start_time = get_time()
#     #print(start_time)
#     time.sleep(5)
#     input("hit enter to end stopwatch")
#     end_time = get_time()
#     #print(end_time)
#     time = calculate_time(start_time, end_time)
#     return time
    

def get_time():
    """this funtion when called will return the exact date and time from when it is called."""
    start_time = datetime.now()
    #start_time = time.time()
    return start_time

def calculate_time(start_time, end_time):
    """this funtion is given a start time and an end time and will subtract the two to find the time ellapesed"""
    time = end_time - start_time
    return time
def calculate_the_total_time(time1, time2, time3, time4, time5, time6):
    total_home_work_time = time1 + time2 + time3 + time4 + time5 + time6
    return total_home_work_time

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, and 7 buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_math_time = Label(frm_main, text=f"Math: {Math_time}")
    lbl_250_time = Label(frm_main, text=f"250 {Ecen_250_time}")
    lbl_240_time = Label(frm_main, text=f"240 {Ecen_240_time}")
    lbl_Rel_time = Label(frm_main, text=f"Rel {Rel_time}")
    lbl_121c_time = Label(frm_main, text=f"121c {Cse_121c_time}")
    lbl_210_time = Label(frm_main, text=f"210 {Cse_210_time}")
    lbl_clear_time = Label(frm_main, text="click to clear")
    lbl_total_hw_time = Label(frm_main, text=f"Total time = {Total_home_work_time}")


    def total_hw_time():
        """this funtion is called at the end of every _stopwatch funtion to update the total time"""
        global Math_time 
        global Ecen_250_time 
        global Ecen_240_time 
        global Cse_121c_time 
        global Cse_210_time 
        global Rel_time 
        global Total_home_work_time
        Total_home_work_time = calculate_the_total_time(Math_time, Ecen_240_time, Ecen_250_time, Cse_121c_time,Cse_210_time, Rel_time)
        lbl_total_hw_time.config(text=str(Total_home_work_time))
    

    # Create an integer entry box where the user will enter her age.
    #ent_age = IntEntry(frm_main, width=4, lower_bound=12, upper_bound=90)

    # Create a label that displays "years"
    #lbl_age_units = Label(frm_main, text="years")

    # Create a label that displays "Rates:"
    #lbl_rates = Label(frm_main, text="Rates:")

    # Create labels that will display the results.
    #lbl_slow = Label(frm_main, width=3)
    #lbl_fast = Label(frm_main, width=3)
    #lbl_rate_units = Label(frm_main, text="beats/minute")

    # Create the Clear button. and buttoons for all of the Classes
    btn_clear = Button(frm_main, text="Clear")
    btn_ecen250 = Button(frm_main, text="Ecen 250")
    btn_ecen240 = Button(frm_main, text="Ecen 240")
    btn_cse210 = Button(frm_main, text="CSE 210")
    btn_cse121c = Button(frm_main, text="CSE 121c")
    btn_math = Button(frm_main, text="Math")
    btn_rel = Button(frm_main, text="Rel")

    
    # Layout all the labels, entry boxes, and buttons in a grid.
    
    btn_clear.grid(row=1, column=1, padx=3, pady=2, columnspan=1, sticky="w")
    lbl_clear_time.grid(      row=1, column=2, padx=3, pady=3)
    btn_ecen250.grid(row=1, column=3, padx=3, pady=2, columnspan=1, sticky="w")
    lbl_250_time.grid(      row=1, column=4, padx=3, pady=3)
    btn_ecen240.grid(row=1, column=5, padx=3, pady=2, columnspan=1, sticky="w")
    lbl_240_time.grid(      row=1, column=6, padx=3, pady=3)
    btn_cse210.grid(row=2, column=1, padx=3, pady=2, columnspan=1, sticky="w")
    lbl_210_time.grid(      row=2, column=2, padx=3, pady=3)
    btn_cse121c.grid(row=2, column=3, padx=3, pady=2, columnspan=1, sticky="w")
    lbl_121c_time.grid(      row=2, column=4, padx=3, pady=3)
    btn_math.grid(row=2, column=5, padx=3, pady=2, columnspan=1, sticky="w")  
    lbl_math_time.grid(      row=2, column=6, padx=3, pady=3)
    btn_rel.grid(row=3, column=1, padx=3, pady=2, columnspan=1, sticky="w")  
    lbl_Rel_time.grid(      row=3, column=2, padx=3, pady=3)
    lbl_total_hw_time.grid(      row=3, column=4, padx=3, pady=3)
    # This function will be called each time the user releases a key.

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        
        lbl_math_time.config(text=timedelta(0))

        lbl_Rel_time.config(text=timedelta(0))
        lbl_250_time.config(text=timedelta(0))
        lbl_240_time.config(text=timedelta(0))
        lbl_121c_time.config(text=timedelta(0))
        lbl_210_time.config(text=timedelta(0))
        total_hw_time()
    def math_stopwatch():
        "this funtion will set a timer when the Math button is pressed and then will stop it when it is pressed again. It will also call the calcualate funtions to update the time spent on homework"
        global math_button_press
        global Math_start
        global Math_time
        if math_button_press == False:
            math_button_press = True
            Math_start = get_time()

            btn_math.config(text="Push")
        elif math_button_press == True:
            btn_math.config(text="Math")
            math_button_press = False
            end_time = get_time()
            time = calculate_time(Math_start, end_time)
            Math_time += time
            lbl_math_time.config(text=str(Math_time)) 
        total_hw_time()
    def ecen250_stopwatch():
        "this funtion will set a timer when the Ecen 250 button is pressed and then will stop it when it is pressed again. It will also call the calcualate funtions to update the time spent on homework"
        global Ecen_250_button_press
        global Ecen_250_start
        global Ecen_250_time
        if Ecen_250_button_press == False:
            Ecen_250_button_press = True
            Ecen_250_start = get_time()

            btn_ecen250.config(text="5Push")
        elif Ecen_250_button_press == True:
            btn_ecen250.config(text="250")
            Ecen_250_button_press = False
            end_time = get_time()
            time = calculate_time(Ecen_250_start, end_time)
            Ecen_250_time += time
            lbl_250_time.config(text=str(Ecen_250_time)) 
        total_hw_time()
    def ecen240_stopwatch():
        "this funtion will set a timer when the ecen 240 button is pressed and then will stop it when it is pressed again. It will also call the calcualate funtions to update the time spent on homework"
        global Ecen_240_button_press
        global Ecen_240_start
        global Ecen_240_time
        if Ecen_240_button_press == False:
            Ecen_240_button_press = True
            Ecen_240_start = get_time()

            btn_ecen240.config(text="5Push")
        elif Ecen_240_button_press == True:
            btn_ecen240.config(text="250")
            Ecen_240_button_press = False
            end_time = get_time()
            time = calculate_time(Ecen_240_start, end_time)
            Ecen_240_time += time
            lbl_240_time.config(text=str(Ecen_240_time))
        total_hw_time()
    def cse121c_stopwatch():
        "this funtion will set a timer when the cse 121c button is pressed and then will stop it when it is pressed again. It will also call the calcualate funtions to update the time spent on homework"
        global Cse_121c_button_press
        global Cse_121c_start
        global Cse_121c_time
        if Cse_121c_button_press == False:
            Cse_121c_button_press = True
            Cse_121c_start = get_time()

            btn_cse121c.config(text="cPush")
        elif Cse_121c_button_press == True:
            btn_cse121c.config(text="121c")
            Cse_121c_button_press = False
            end_time = get_time()
            time = calculate_time(Cse_121c_start, end_time)
            Cse_121c_time += time
            lbl_121c_time.config(text=str(Cse_121c_time))
        total_hw_time()
    def cse210_stopwatch():
        "this funtion will set a timer when the ecen 210 button is pressed and then will stop it when it is pressed again. It will also call the calcualate funtions to update the time spent on homework"
        global Cse_210_button_press
        global Cse_210_start
        global Cse_210_time
        if Cse_210_button_press == False:
            Cse_210_button_press = True
            Cse_210_start = get_time()

            btn_cse210.config(text="cPush")
        elif Cse_210_button_press == True:
            btn_cse210.config(text="121c")
            Cse_210_button_press = False
            end_time = get_time()
            time = calculate_time(Cse_210_start, end_time)
            Cse_210_time += time
            lbl_210_time.config(text=str(Cse_210_time))
        total_hw_time()
    def rel_stopwatch():
        "this funtion will set a timer when the rel button is pressed and then will stop it when it is pressed again. It will also call the calcualate funtions to update the time spent on homework"
        global Rel_button_press
        global Rel_start
        global Rel_time
        if Rel_button_press == False:
            Rel_button_press = True
            Rel_start = get_time()

            btn_rel.config(text="cPush")
        elif Rel_button_press == True:
            btn_rel.config(text="121c")
            Rel_button_press = False
            end_time = get_time()
            time = calculate_time(Rel_start, end_time)
            Rel_time += time
            lbl_Rel_time.config(text=str(Rel_time))
        total_hw_time()
    # Bind the lables functions to the buttons so it will calculate the time
    
    lbl_math_time.bind("<KeyRelease>", calculate_time)
    lbl_121c_time.bind("<KeyRelease>", calculate_time)
    lbl_210_time.bind("<KeyRelease>", calculate_time)
    lbl_240_time.bind("<KeyRelease>", calculate_time)
    lbl_250_time.bind("<KeyRelease>", calculate_time)
    lbl_Rel_time.bind("<KeyRelease>", calculate_time)
    
    # Bind the functions to the buttons so
    # that the computer will call the functions
    # when the user clicks the clear buttons.
    btn_clear.config(command=clear)

        
    btn_math.config(command=math_stopwatch)
    btn_ecen250.config(command=ecen250_stopwatch)
    btn_ecen240.config(command=ecen240_stopwatch)
    btn_cse121c.config(command=cse121c_stopwatch)
    btn_cse210.config(command=cse210_stopwatch)
    btn_rel.config(command=rel_stopwatch)

    


if __name__ == "__main__":
    main()
