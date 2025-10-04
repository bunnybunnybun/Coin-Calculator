import FreeSimpleGUI as sg

layout = [
    [sg.Text("Calculate how many coins ya have with this calculator, so that you don't have to use your brain!", font="default 11", text_color=('black'), background_color='#FFFFFF')],
    [sg.Input(key = "input1", size=15), sg.Spin(['Plus', 'Minus', 'Multiplied by', 'Divided by'], key = "spin"), sg.Input( key = "input2", size=15)],
    [sg.Button("Calculate!!!", button_color=('white','green'), font='default 11 bold', key = "calculate"), sg.Text("Result:", font="default 11", text_color=('black'), background_color=('white'), key = "result")],
    [sg.Text("History:", font="default 11", text_color=("black"), background_color=("white"))],
    [sg.Text("Do a calculation for it to show up in your history!", size=45, text_color=("grey"), background_color=("#ebebeb"), key = "history1")],
    [sg.Text("Empty", background_color=("#ebebeb"), text_color="grey", size=45, key = "history2")],
    [sg.Text("Empty", background_color=("#ebebeb"), text_color="grey", size=45, key = "history3")],
    [sg.Text("Empty", background_color=("#ebebeb"), text_color="grey", size=45, key = "history4")],
    [sg.Text("Empty", background_color=("#ebebeb"), text_color="grey", size=45, key = "history5")]
]

window = sg.Window('Calculator', layout, background_color='#FFFFFF')

his1 = "Empty"
his2 = "Empty"
his3 = "Empty"
his4 = "Empty"
his5 = "Empty"

while True:
    event, values = window.read()

    if event == "calculate":
        try:
            input1 = float(values["input1"])
            input2 = float(values["input2"])
            if values["spin"] == "Plus":
                result = float(input1) + float(input2)
                calculation = f"{float(input1)} + {float(input2)} = {result}" # calculation is used for the history
            elif values["spin"] == "Minus":
                result = float(input1) - float(input2)
                calculation = f"{float(input1)} + {float(input2)} = {result}"
            elif values["spin"] == "Multiplied by":
                result = float(input1) * float(input2)
                calculation = f"{float(input1)} + {float(input2)} = {result}"
            elif values["spin"] == "Divided by":
                result = float(input1) / float(input2)
                calculation = f"{float(input1)} + {float(input2)} = {result}"
            else:
                result = "A critical error occurred :("
            window["result"].update(f"Result: {result}")
            if result != "A critical error occurred :(":
                window["history5"].update(f"{his4}")
                his5 = his4
                window["history4"].update(f"{his3}")
                his4 = his3
                window["history3"].update(f"{his2}")
                his3 = his2
                window["history2"].update(f"{his1}")
                his2 = his1
                window["history1"].update(f"{calculation}")
                his1 = calculation
        except ValueError:
            window["result"].update("Result: Please enter valid numbers")


    if event == sg.WIN_CLOSED:
        break
    
window.close()