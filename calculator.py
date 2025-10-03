import FreeSimpleGUI as sg

layout = [
    [sg.Text("Calculate how many coins ya got with this calculator, so that you don't have to use your brain!", font="default 11", text_color=('black'), background_color='#FFFFFF')],
    [sg.Input(key = "input1", size=15), sg.Spin(['Plus', 'Minus', 'Multiplied by', 'Divided by'], key = "spin"), sg.Input( key = "input2", size=15)],
    [sg.Button("Calculate!!!", button_color=('white','green'), font='default 11 bold', key = "calculate"), sg.Text("Result:", font="default 11", text_color=('black'), background_color=('white'), key = "result")]
]

window = sg.Window('Calculator', layout, background_color='#FFFFFF')

while True:
    event, values = window.read()

    if event == "calculate":
        try:
            input1 = float(values["input1"])
            input2 = float(values["input2"])
            if values["spin"] == "Plus":
                result = float(input1) + float(input2)
            elif values["spin"] == "Minus":
                result = float(input1) - float(input2)
            elif values["spin"] == "Multiplied by":
                result = float(input1) * float(input2)
            elif values["spin"] == "Divided by":
                result = float(input1) / float(input2)
            else:
                result = "A critical error occurred :("
            window["result"].update(f"Result: {result}")
        except ValueError:
            window["result"].update("Result: Please enter valid numbers")


    if event == sg.WIN_CLOSED:
        break
    
window.close()