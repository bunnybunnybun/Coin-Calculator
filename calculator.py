import FreeSimpleGUI as sg
import os

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "coin.png")
sg.theme('NeonBlue1')

layout = [
    [sg.Text("Calculate how many coins ya have with this calculator + currency converter, so that you don't have to use your brain!", font="default 11")],
    [sg.Text("Calculator:                                                                                      "), sg.Text(" Currency converter:")],
    [sg.Input(key = "input1", size=15), sg.Image(background_color="white", zoom=2, size=(30, 30), source=image_path), sg.Spin(['Plus', 'Minus', 'Multiplied by', 'Divided by'], size=10, key = "spin"), sg.Input( key = "input2", size=15), sg.Image(background_color="white", zoom=2, size=(30, 30), source=image_path), sg.Text(""), sg.Input(key="cinput", size=30), sg.Spin(["USD", "CAD", "EUR"], key="ctype1"), sg.Text("to:", font=("default 11")), sg.Spin(["USD", "CAD", "EUR"], key="ctype2")],
    [sg.Button("Calculate!!!", button_color=('white','green'), font='default 11 bold', key = "calculate"), sg.Text("Result:", font="default 11", size=37, key = "result"), sg.Button("Calculate!!!", button_color=('white','green'), font='default 11 bold', key = "convcalculate"), sg.Text("Result:", font="default 11", key = "convresult")],
    [sg.Text("History:", font="default 11")],
    [sg.Text("Do a calculation for it to show up in your history!", size=45, text_color=("grey"), key = "history1")],
    [sg.Text("Empty", text_color="grey", size=45, key = "history2")],
    [sg.Text("Empty", text_color="grey", size=45, key = "history3")],
    [sg.Text("Empty", text_color="grey", size=45, key = "history4")],
    [sg.Text("Empty", text_color="grey", size=45, key = "history5")]
]

window = sg.Window('Calculator', layout)

result = "AAAHHH"
convresult = "AAAHHH"
didcalculate = False
his1 = "Empty"
his2 = "Empty"
his3 = "Empty"
his4 = "Empty"
his5 = "Empty"

while True:
    event, values = window.read()
    #f"{float(values["cinput"]) * 1.3967}"
    if event == "convcalculate":
        didcalculate = True
        ctype1 = str(values["ctype1"])
        ctype2 = str(values["ctype2"])
        try:
            if ctype1 == "USD" and ctype2 == "USD":
                window["convresult"].update(f"{float(values["cinput"])}")
                calculation = f"{float(values["cinput"])} USD to USD = {float(values["cinput"])} USD"
            elif ctype1 == "USD" and ctype2 == "CAD":
                window["convresult"].update(f"{float(values["cinput"]) * 1.3967}")
                calculation = f"{float(values["cinput"])} USD to CAD = {float(values["cinput"]) * 1.3967} CAD"
            elif ctype1 == "CAD" and ctype2 == "CAD":
                window["convresult"].update(f"{float(values["cinput"])}")
                calculation = f"{float(values["cinput"])} CAD to CAD = {float(values["cinput"])} CAD"
            elif ctype1 == "CAD" and ctype2 == "USD":
                window["convresult"].update(f"{float(values["cinput"]) * 0.7160}")
                calculation = f"{float(values["cinput"])} CAD to USD = {float(values["cinput"]) * 0.7160} USD"
            elif ctype1 == "USD" and ctype2 == "EUR":
                window["convresult"].update(f"{float(values["cinput"]) * 0.8520}")
                calculation = f"{float(values["cinput"])} USD to EUR = {float(values["cinput"]) * 0.8520} EUR"
            elif ctype1 == "EUR" and ctype2 == "USD":
                window["convresult"].update(f"{float(values["cinput"]) * 1.1738}")
                calculation = f"{float(values["cinput"])} EUR to USD = {float(values["cinput"]) * 1.1738} USD"
            elif ctype1 == "CAD" and ctype2 == "EUR":
                window["convresult"].update(f"{float(values["cinput"]) * 0.6100}")
                calculation = f"{float(values["cinput"])} CAD to EUR = {float(values["cinput"]) * 0.6100} EUR"
            elif ctype1 == "EUR" and ctype2 == "CAD":
                window["convresult"].update(f"{float(values["cinput"]) * 1.6393}")
                calculation = f"{float(values["cinput"])} EUR to CAD = {float(values["cinput"]) * 1.6393} CAD"
            elif ctype1 == "EUR" and ctype2 == "EUR":
                window["convresult"].update(f"{float(values["cinput"])}")
                calculation = f"{float(values["cinput"])} EUR to EUR = {float(values["cinput"])} EUR"
            else:
                window["convresult"].update("A critical error has occurred :(")
                didcalculate = False
        except ValueError:
            window["convresult"].update("Result: Please enter valid numbers")
            didcalculate = False

    if event == "calculate":
        try:
            didcalculate = True
            input1 = float(values["input1"])
            input2 = float(values["input2"])
            if values["spin"] == "Plus":
                result = float(input1) + float(input2)
                calculation = f"{float(input1)} + {float(input2)} = {result}" # calculation is used for the history
            elif values["spin"] == "Minus":
                result = float(input1) - float(input2)
                calculation = f"{float(input1)} - {float(input2)} = {result}"
            elif values["spin"] == "Multiplied by":
                result = float(input1) * float(input2)
                calculation = f"{float(input1)} * {float(input2)} = {result}"
            elif values["spin"] == "Divided by":
                result = float(input1) / float(input2)
                calculation = f"{float(input1)} / {float(input2)} = {result}"
            else:
                result = "A critical error has occurred :("
                didcalculate = False
            window["result"].update(f"Result: {result}")
            
        except ValueError:
            window["result"].update("Result: Please enter valid numbers")
            didcalculate = False

    if result != "A critical error has occurred :(" and convresult != "A critical error has occurred :(" and didcalculate == True:
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
        if his1 != "Empty":
            window["history1"].update(text_color=("white"))
        if his2 != "Empty":
            window["history2"].update(text_color=("white"))
        if his3 != "Empty":
            window["history3"].update(text_color=("white"))
        if his4 != "Empty":
            window["history4"].update(text_color=("white"))
        if his5 != "Empty":
            window["history5"].update(text_color=("white"))

    didcalculate = False

    if event == sg.WIN_CLOSED:
        break
    
window.close()