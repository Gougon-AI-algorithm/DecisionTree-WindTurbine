import tkinter as tk
import Constant


def click_predict_button():
    print('a')


def append_label(text, order, is_output=False):
    order = order + 1
    label = tk.Label(window, text=text, font=Constant.FONT, height=1)
    label.place(x=Constant.LABEL_X, y=order * Constant.ROW_INTERVAL)
    if is_output:
        return label


def append_entry(order):
    order = order + 1
    entry = tk.Entry(window, show=None, font=Constant.FONT)
    entry.place(x=Constant.ENTRY_X, y=order * Constant.ROW_INTERVAL)
    entries.append(entry)


window = tk.Tk()
window.title(Constant.WINDOW_TITLE)
window.geometry(Constant.WINDOW_SIZE)

append_label(Constant.WS_LABEL, Constant.WS_ORDER)
append_label(Constant.RM_LABEL, Constant.RM_ORDER)
append_label(Constant.CM_LABEL, Constant.CM_ORDER)
append_label(Constant.RS_LABEL, Constant.RS_ORDER)
output = append_label(Constant.P_LABEL, Constant.P_ORDER, True)

entries = []
for row in range(4):
    append_entry(row)

predictButton = tk.Button(window, text=Constant.PREDICT_BUTTON_TEXT, font=Constant.FONT,
                          command=click_predict_button, width=Constant.BUTTON_WIDTH, height=Constant.BUTTON_HEIGHT)

window.mainloop()
