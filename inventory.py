from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('inventory_db')


def populate_list():
    # reset previous list from 0 to end
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if '' in [model_text.get(), brand_text.get(), size_text.get(), color_text.get(), gender_text.get(), type_text.get(), shape_text.get(), style_text.get()] or 0 in [stock_text.get(), price_text.get()]:
        messagebox.showerror('Require Fields', 'Please fill in fields')
        return

    # item = [model_text.get(), brand_text.get(), size_text.get(), color_text.get(), stock_text.get(
    # ), price_text.get(), gender_text.get(), type_text.get(), shape_text.get(), style_text.get()]
    db.insert(model_text.get(), brand_text.get(), size_text.get(), color_text.get(), stock_text.get(
    ), price_text.get(), gender_text.get(), type_text.get(), shape_text.get(), style_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (model_text.get(), brand_text.get(), size_text.get(), color_text.get(), stock_text.get(
    ), price_text.get(), gender_text.get(), type_text.get(), shape_text.get(), style_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    # ARG: click event
    # OUTPUT: selected item in list box
    # try/except to handle IndexError
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        # Delete current textfield entry and set click items entry onClick
        print(selected_item)
        clear_text()
        model_entry.insert(END, selected_item[1])
        brand_entry.insert(END, selected_item[2])
        size_entry.insert(END, selected_item[3])
        color_entry.insert(END, selected_item[4])
        stock_entry.insert(END, selected_item[5])
        gender_entry.insert(END, selected_item[6])
        shape_entry.insert(END, selected_item[7])
        type_entry.insert(END, selected_item[8])
        style_entry.insert(END, selected_item[9])
        price_entry.insert(END, selected_item[10])
    except IndexError:
        pass


def remove_item():
    # grab index and remove
    db.remove(selected_item[0])

    populate_list()


def update_item():
    db.update(selected_item[0], model_text.get(), brand_text.get(), size_text.get(), color_text.get(), stock_text.get(
    ), price_text.get(), gender_text.get(), type_text.get(), shape_text.get(), style_text.get())
    populate_list()


def clear_text():
    model_entry.delete(0, END)
    brand_entry.delete(0, END)
    size_entry.delete(0, END)
    color_entry.delete(0, END)
    stock_entry.delete(0, END)
    price_entry.delete(0, END)
    gender_entry.delete(0, END)
    type_entry.delete(0, END)
    shape_entry.delete(0, END)
    style_entry.delete(0, END)


# create window object
app = Tk()

# Change title & window size
app.title('Store Inventory')
app.geometry('1200x550')
# ===================================================
# Buildign parts for gui
# Part - Brand

# initalize a string_var - use this to store entry
brand_text = StringVar()
# Creating a Label; placing Label on a grid
brand_label = Label(app, text='Brand', font=('bold', 14), pady=20, padx=10)
brand_label.grid(row=0, column=0, sticky=W)
# Create Entry widget
brand_entry = Entry(app, textvariable=brand_text)
brand_entry.grid(row=0, column=1)

# Part - Model
model_text = StringVar()
model_label = Label(app, text='Model', font=('bold', 14), padx=10)
model_label.grid(row=0, column=2, sticky=W)
model_entry = Entry(app, textvariable=model_text)
model_entry.grid(row=0, column=3)

# Part - size
size_text = StringVar()
size_label = Label(app, text='Size', font=('bold', 14), padx=10)
size_label.grid(row=1, column=0, sticky=W)
size_entry = Entry(app, textvariable=size_text)
size_entry.grid(row=1, column=1)

# Part - Colors; 001,002,003
color_text = StringVar()
color_label = Label(app, text='Color', font=('bold', 14), padx=10)
color_label.grid(row=2, column=0, sticky=W)
color_entry = Entry(app, textvariable=color_text)
color_entry.grid(row=2, column=1)

# Part - Type; sunglasses, eyeglasses, contact lenses
type_text = StringVar()
type_label = Label(app, text='Type', font=('bold', 14), padx=10)
type_label.grid(row=3, column=0, sticky=W)
type_entry = Entry(app, textvariable=type_text)
type_entry.grid(row=3, column=1)

# Part - Shape; square, circle, rectangle, star, oval
shape_text = StringVar()
shape_label = Label(app, text='shape', font=('bold', 14), padx=10)
shape_label.grid(row=4, column=0, sticky=W)
shape_entry = Entry(app, textvariable=shape_text)
shape_entry.grid(row=4, column=1)

# Part - Style; metal, titanium, plastic, glasses, wood
style_text = StringVar()
style_label = Label(app, text='Style', font=('bold', 14), padx=10)
style_label.grid(row=5, column=0, sticky=W)
style_entry = Entry(app, textvariable=style_text)
style_entry.grid(row=5, column=1)

# Part - Gender; female, male, children both
gender_text = StringVar()
gender_label = Label(app, text='Gender', font=('bold', 14), padx=10)
gender_label.grid(row=1, column=2, sticky=W)
gender_entry = Entry(app, textvariable=gender_text)
gender_entry.grid(row=1, column=3)

# Part - Stock Quantity; INT
stock_text = IntVar()
stock_label = Label(app, text='Stock', font=('bold', 14), padx=10)
stock_label.grid(row=6, column=0, sticky=W)
stock_entry = Entry(app, textvariable=stock_text)
stock_entry.grid(row=6, column=1)

# Part - Price  DECIMAL
price_text = DoubleVar()
price_label = Label(app, text='Price', font=('bold', 14), padx=10)
price_label.grid(row=7, column=0, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=7, column=1)

# Parts List (Listbox) - to store history of data
parts_list = Listbox(app, height=8, width=120)
parts_list.grid(row=10, column=0, columnspan=3,
                rowspan=5, pady=20, padx=20)
# Create scrollbar for llistbox;
scrollbar = Scrollbar(app)
scrollbar.grid(row=10, column=3)
# Bind select_item to list
parts_list.bind('<<ListboxSelect>>', select_item)

# set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# =========================================================
# Adding Buttons - add, remove. update, clear
add_btn = Button(app, text='Add item', width=10, command=add_item)
add_btn.grid(row=9, column=0, pady=20)

remove_btn = Button(app, text='Remove item', width=10, command=remove_item)
remove_btn.grid(row=9, column=1)

update_btn = Button(app, text='Update item', width=10, command=update_item)
update_btn.grid(row=9, column=2)

clear_btn = Button(app, text='Clear', width=10, command=clear_text)
clear_btn.grid(row=9, column=3)

populate_list()

# Start program
app.mainloop()
