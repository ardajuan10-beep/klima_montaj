
import tkinter as tk
#import tkinter as ttk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date
from datetime import datetime
from datetime import timedelta
import data.data_karer as data_class
import pickle

class auto_allocation_popup:
  def popup(self):
    self.root = tk.Toplevel(self.karer_hmi.root)
    self.root.title("Otomatik Sipariş Yerleştirme")
    self.root.geometry("1000x500")
    self.root.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.root.iconphoto(False, p1)

    self.root.transient(self.karer_hmi.root)  # set to be on top of the main window
    self.root.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)

    if len(self.karer_hmi.calendar_data.all_teams_data) == 0:
      label = ttk.Label(self.root, text="Takım yok! Önce takımı yarat.", font=("Arial Bold", 12), background="Light Blue", foreground="Red", anchor="e", width=35)
      label.grid(row=0, column=0, pady=5, padx=5)
      return


    #COLUMN 0
    label = ttk.Label(self.root, text="Günlük Maksimum Sipariş Lefkoşa", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=0, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Minimum Sipariş Lefkoşa", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=1, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Maksimum Sipariş Batı", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=2, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Minimum Sipariş Batı", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=3, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Maksimum Sipariş Doğu", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=4, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Minimum Sipariş Doğu", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=5, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Maksimum Sipariş Girne", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=6, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Günlük Minimum Sipariş Girne", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=7, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Atlanacak günler", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=8, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="Atlanacak tarihler", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=9, column=0, pady=5, padx=5)

    label = ttk.Label(self.root, text="İşlemin Süreceği gün sayısı", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=35)
    label.grid(row=10, column=0, pady=5, padx=5)

    # COLUMN 1
    reg_digits = self.root.register(text_entry_rules.callback_digits)

    self.entry_daily_max_Nicosia = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_max_Nicosia.grid(row=0, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_max_Nicosia.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_max_Nicosia.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_nicosia))

    self.entry_daily_min_Nicosia = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_min_Nicosia.grid(row=1, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_min_Nicosia.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_min_Nicosia.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_nicosia))

    self.entry_daily_max_West = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_max_West.grid(row=2, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_max_West.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_max_West.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_west))

    self.entry_daily_min_West = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_min_West.grid(row=3, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_min_West.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_min_West.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_west))

    self.entry_daily_max_East = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_max_East.grid(row=4, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_max_East.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_max_East.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_east))

    self.entry_daily_min_East = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_min_East.grid(row=5, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_min_East.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_min_East.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_east))

    self.entry_daily_max_Kyrenia = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_max_Kyrenia.grid(row=6, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_max_Kyrenia.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_max_Kyrenia.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_kyrenia))

    self.entry_daily_min_Kyrenia = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_daily_min_Kyrenia.grid(row=7, column=1, pady=5, padx=5, sticky='w')
    self.entry_daily_min_Kyrenia.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_daily_min_Kyrenia.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_kyrenia))

    #prep booleans for the checkboxes
    self.bool_avoid_monday = tk.BooleanVar()
    self.bool_avoid_monday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[0]))
    self.bool_avoid_tuesday = tk.BooleanVar()
    self.bool_avoid_tuesday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[1]))
    self.bool_avoid_wednesday = tk.BooleanVar()
    self.bool_avoid_wednesday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[2]))
    self.bool_avoid_thursday = tk.BooleanVar()
    self.bool_avoid_thursday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[3]))
    self.bool_avoid_friday = tk.BooleanVar()
    self.bool_avoid_friday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[4]))
    self.bool_avoid_saturday = tk.BooleanVar()
    self.bool_avoid_saturday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[5]))
    self.bool_avoid_sunday = tk.BooleanVar()
    self.bool_avoid_sunday.set((self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[6]))

    #prep canvas for the checkboxes
    canvas_days_to_avoid = tk.Canvas(self.root, bd=0, highlightthickness=0, bg="Light Blue", width=100, height=1)
    canvas_days_to_avoid.grid(row=8, column=1, pady=5, padx=5, sticky='w')

    #PLace the checkboxes
    # , variable=self.bool_avoid_monday, onvalue=1, offvalue=0)
    cb_monday = tk.Checkbutton(canvas_days_to_avoid, text="Pazartesi", command=lambda: self.__toggle_checkbox(self.bool_avoid_monday))
    cb_monday.grid(row=0, column=0, pady=5, padx=0, sticky='w')
    if self.bool_avoid_monday.get() == True: cb_monday.select()

    cb_tuesday = tk.Checkbutton(canvas_days_to_avoid, text="Salı", command=lambda: self.__toggle_checkbox(self.bool_avoid_tuesday))
    cb_tuesday.grid(row=0, column=1, pady=5, padx=5, sticky='w')
    if self.bool_avoid_tuesday.get() == True: cb_tuesday.select()

    cb_wednesday = tk.Checkbutton(canvas_days_to_avoid, text="Çarşamba", command=lambda: self.__toggle_checkbox(self.bool_avoid_wednesday))
    cb_wednesday.grid(row=0, column=2, pady=5, padx=5, sticky='w')
    if self.bool_avoid_wednesday.get() == True: cb_wednesday.select()

    cb_thursday = tk.Checkbutton(canvas_days_to_avoid, text="Perşembe", command=lambda: self.__toggle_checkbox(self.bool_avoid_thursday))
    cb_thursday.grid(row=0, column=3, pady=5, padx=5, sticky='w')
    if self.bool_avoid_thursday.get() == True: cb_thursday.select()

    cb_friday = tk.Checkbutton(canvas_days_to_avoid, text="Cuma", command=lambda: self.__toggle_checkbox(self.bool_avoid_friday))
    cb_friday.grid(row=0, column=4, pady=5, padx=5, sticky='w')
    if self.bool_avoid_friday.get() == True: cb_friday.select()

    cb_saturday = tk.Checkbutton(canvas_days_to_avoid, text="Cumartesi", command=lambda: self.__toggle_checkbox(self.bool_avoid_saturday))
    cb_saturday.grid(row=0, column=5, pady=5, padx=5, sticky='w')
    if self.bool_avoid_saturday.get() == True: cb_saturday.select()

    cb_sunday = tk.Checkbutton(canvas_days_to_avoid, text="Pazar", command=lambda: self.__toggle_checkbox(self.bool_avoid_sunday))
    cb_sunday.grid(row=0, column=6, pady=5, padx=5, sticky='w')
    if self.bool_avoid_sunday.get() == True: cb_sunday.select()



    self.entry_dates_to_avoid = ttk.Entry(self.root, width=100, font=("Arial", 12))
    self.entry_dates_to_avoid.grid(row=9, column=1, pady=5, padx=5, sticky='w')
    str_dates_to_avoid = ""
    for i in range(len(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.dates_to_avoid)):
      if i == len(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.dates_to_avoid) - 1: #if it is the last element of the array
        str_dates_to_avoid = str_dates_to_avoid + str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.dates_to_avoid[i])
      else:
        str_dates_to_avoid = str_dates_to_avoid + str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.dates_to_avoid[i]) + ", "


    self.entry_dates_to_avoid.insert(tk.INSERT,str_dates_to_avoid)

    self.entry_total_days = ttk.Entry(self.root, width=7, font=("Arial", 12))
    self.entry_total_days.grid(row=10, column=1, pady=5, padx=5, sticky='w')
    self.entry_total_days.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_total_days.insert(tk.INSERT, str(self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.no_of_days_for_op))

    button_op = ttk.Button(self.root, text="İşlemi Gerçekleştir", command=self.__automatic_allocation_op)
    button_op.grid(row=11, column=1, pady=5, padx=5, sticky='w')

  def __automatic_allocation_op(self):
    label = ttk.Label(self.root, text="", font=("Arial Bold", 12), background="Light Blue", foreground="Red", anchor="w", width=75)
    label.grid(row=12, column=1, pady=5, padx=5, sticky='w')
    try:
      temp_daily_max_order_nicosia = int(self.entry_daily_max_Nicosia.get())
    except:
      label.configure(text="Günlük Maksimum Sipariş Lefkoşa karesi boş")
      return

    try:
      temp_daily_min_order_nicosia = int(self.entry_daily_min_Nicosia.get())
    except:
      label.configure(text="Günlük Minimum Sipariş Lefkoşa karesi boş")
      return

    try:
      temp_daily_max_order_west = int(self.entry_daily_max_West.get())
    except:
      label.configure(text="Günlük Maksimum Sipariş Batı karesi boş")
      return

    try:
      temp_daily_min_order_west = int(self.entry_daily_min_West.get())
    except:
      label.configure(text="Günlük Minimum Sipariş Batı karesi boş")
      return

    try:
      temp_daily_max_order_east = int(self.entry_daily_max_East.get())
    except:
      label.configure(text="Günlük Maksimum Sipariş Doğu karesi boş")
      return

    try:
      temp_daily_min_order_east = int(self.entry_daily_min_East.get())
    except:
      label.configure(text="Günlük Minimum Sipariş Doğu karesi boş")
      return

    try:
      temp_daily_max_order_kyrenia = int(self.entry_daily_max_Kyrenia.get())
    except:
      label.configure(text="Günlük Maksimum Sipariş Girne karesi boş")
      return

    try:
      temp_daily_min_order_kyrenia = int(self.entry_daily_min_Kyrenia.get())
    except:
      label.configure(text="Günlük Minimum Sipariş Girne karesi boş")
      return

    try:
      temp_total_days = int(self.entry_total_days.get())
    except:
      label.configure(text="İşlemin Süreceği gün sayısı karesi bos")
      return

    try:
      temp_days_to_avoid = []
      arr_elem_str = ""
      for element in self.entry_dates_to_avoid.get():
        if element == ",": #if it is comma, add the string to the arr
          temp_days_to_avoid.append(datetime.strptime(arr_elem_str, '%Y-%m-%d').date())
          arr_elem_str = ""
        elif element != " ": #if it is space just avoid, if not space get the character
          arr_elem_str = arr_elem_str + element
      # end of foor loop, get the last character
      temp_days_to_avoid.append(datetime.strptime(arr_elem_str, '%Y-%m-%d').date())
      arr_elem_str = ""
    except:
      label.configure(text="Esgecilecek tarihler karesindeki girilenler formata uygun degil")
      return

    ##save these values to permanent vars
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_nicosia = temp_daily_max_order_nicosia
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_nicosia = temp_daily_min_order_nicosia
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_east = temp_daily_max_order_east
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_east = temp_daily_min_order_east
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_west = temp_daily_max_order_west
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_west = temp_daily_min_order_west
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_max_order_kyrenia = temp_daily_max_order_kyrenia
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.daily_min_order_kyrenia = temp_daily_min_order_kyrenia
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[0] = self.bool_avoid_monday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[1] = self.bool_avoid_tuesday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[2] = self.bool_avoid_wednesday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[3] = self.bool_avoid_thursday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[4] = self.bool_avoid_friday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[5] = self.bool_avoid_saturday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.days_to_avoid[6] = self.bool_avoid_sunday.get()
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.dates_to_avoid = []
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.dates_to_avoid = temp_days_to_avoid
    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].aut_alloc_vars.no_of_days_for_op = temp_total_days

    self.root.destroy()

    self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].auto_order_placement()

    self.karer_hmi.refresh_page()





  def __toggle_checkbox(self, var_to_toggle):
    var_to_toggle.set(not var_to_toggle.get())
    print("Checkbox value is now: " + str(var_to_toggle.get()))
    #print("cumartesi evet mi " + str(self.bool_avoid_saturday.get()))

  def __init__(self, hmi):
    self.karer_hmi = hmi

class details_popup:
  def __save_button(self, slot_data):

    ##save prepared values
    slot_data.region = self.value_inside_region.get()
    slot_data.address = self.entry_address.get()
    slot_data.person = self.entry_person.get()
    slot_data.tel = self.entry_tel.get()
    slot_data.order_details = self.entry_order_details.get()
    if self.value_inside_commissioned.get() == 'Evet':
      slot_data.commissioned = True
    else:
      slot_data.commissioned = False
    if self.value_inside_paid.get() == 'Evet':
      slot_data.paid = True
    else:
      slot_data.paid = False
    slot_data._9_kBtu_p_h_no = int(self.entry_9_btu_ac_no.get())
    slot_data._12_kBtu_p_h_no = int(self.entry_12_btu_ac_no.get())
    slot_data._18_kBtu_p_h_no = int(self.entry_18_btu_ac_no.get())
    slot_data._24_kBtu_p_h_no = int(self.entry_24_btu_ac_no.get())

    ##refresh ccolumn 2 for the saved data to appear
    self.__details_refresh_col2(slot_data)

    ##refresh main page
    self.karer_hmi.refresh_page()

  def __details_col1(self,slot_data):
    ##FIRST COLUMN
    label = ttk.Label(self.details_window, text="", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=0, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Sipariş alınma tarihi:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=1, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Bölge:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=2, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Adres:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=3, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Şahıs:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=4, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Telefon:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=5, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Sipariş Detayları:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=6, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Montaj Yapıldı mı?:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=7, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="Ödendi mi?:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=8, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="9 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=9, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="12 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=10, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="18 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=11, column=0, pady=5, padx=5)

    label = ttk.Label(self.details_window, text="24 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    label.grid(row=12, column=0, pady=5, padx=5)

  def __details_col2(self, slot_data):
    ##SECOND COLUMN
    label = ttk.Label(self.details_window, text="Anlık Sipariş Verisi", font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    label.grid(row=0, column=1, pady=5, padx=5)

    self.label_order_time = ttk.Label(self.details_window, text=str(slot_data.date_of_order), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_order_time.grid(row=1, column=1, pady=5, padx=5)

    self.label_region = ttk.Label(self.details_window, text=str(slot_data.region), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_region.grid(row=2, column=1, pady=5, padx=5)

    self.label_address = ttk.Label(self.details_window, text=str(slot_data.address), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_address.grid(row=3, column=1, pady=5, padx=5)

    self.label_person = ttk.Label(self.details_window, text=str(slot_data.person), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_person.grid(row=4, column=1, pady=5, padx=5)

    self.label_tel = ttk.Label(self.details_window, text=str(slot_data.tel), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_tel.grid(row=5, column=1, pady=5, padx=5)

    self.label_order_details = ttk.Label(self.details_window, text=str(slot_data.order_details), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_order_details.grid(row=6, column=1, pady=5, padx=5)

    if slot_data.commissioned:
      str_temp_com = "Evet"
    else:
      str_temp_com = "Hayır"
    self.label_commissioned = ttk.Label(self.details_window, text=str_temp_com, font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_commissioned.grid(row=7, column=1, pady=5, padx=5)

    if slot_data.paid:
      str_temp_paid = "Evet"
    else:
      str_temp_paid = "Hayır"
    self.label_paid = ttk.Label(self.details_window, text=str_temp_paid, font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_paid.grid(row=8, column=1, pady=5, padx=5)

    self.label_9_btu = ttk.Label(self.details_window, text=str(slot_data._9_kBtu_p_h_no), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_9_btu.grid(row=9, column=1, pady=5, padx=5)

    self.label_12_btu = ttk.Label(self.details_window, text=str(slot_data._12_kBtu_p_h_no), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_12_btu.grid(row=10, column=1, pady=5, padx=5)

    self.label_18_btu = ttk.Label(self.details_window, text=str(slot_data._18_kBtu_p_h_no), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_18_btu.grid(row=11, column=1, pady=5, padx=5)

    self.label_24_btu = ttk.Label(self.details_window, text=str(slot_data._24_kBtu_p_h_no), font=("Arial Bold", 12), background="Light Blue", anchor='c', width=25)
    self.label_24_btu.grid(row=12, column=1, pady=5, padx=5)

  def __details_del_col2(self):
    self.label_order_time.destroy()
    self.label_region.destroy()
    self.label_address.destroy()
    self.label_person.destroy()
    self.label_tel.destroy()
    self.label_order_details.destroy()
    self.label_commissioned.destroy()
    self.label_paid.destroy()
    self.label_9_btu.destroy()
    self.label_12_btu.destroy()
    self.label_18_btu.destroy()
    self.label_24_btu.destroy()

  def __details_refresh_col2(self, slot_data):
    self.__details_del_col2()
    self.__details_col2(slot_data)

  def __details_col3(self, slot_data):
    reg_digits = self.details_window.register(text_entry_rules.callback_digits)

    ##Third column
    label = ttk.Label(self.details_window, text="Yeni Sipariş Verisi", font=("Arial Bold", 12), background="Light Blue", width=25)
    label.grid(row=0, column=2, pady=5, padx=5, sticky="w")

    self.value_inside_region = tk.StringVar(self.details_window)
    self.value_inside_region.set(self.karer_hmi.calendar_data.regions[0])
    self.drop_region = ttk.OptionMenu(self.details_window, self.value_inside_region, self.karer_hmi.calendar_data.regions[0], *self.karer_hmi.calendar_data.regions)
    self.value_inside_region.set(slot_data.region)
    self.drop_region.config(width=15)
    self.drop_region.grid(row=2, column=2, pady=5, padx=5, sticky='w')

    self.entry_address = ttk.Entry(self.details_window, width=50, font=("Arial", 12))
    self.entry_address.grid(row=3, column=2, pady=5, padx=5, sticky='w')
    self.entry_address.insert(tk.INSERT, slot_data.address)

    self.entry_person = ttk.Entry(self.details_window, width=30, font=("Arial", 12))
    self.entry_person.grid(row=4, column=2, pady=5, padx=5, sticky='w')
    self.entry_person.insert(tk.INSERT, slot_data.person)

    self.entry_tel = ttk.Entry(self.details_window, width=30, font=("Arial", 12))
    self.entry_tel.grid(row=5, column=2, pady=5, padx=5, sticky='w')
    self.entry_tel.insert(tk.INSERT, slot_data.tel)

    self.entry_order_details = ttk.Entry(self.details_window, width=50, font=("Arial", 12))
    self.entry_order_details.grid(row=6, column=2, pady=5, padx=5, sticky='w')
    self.entry_order_details.insert(tk.INSERT, slot_data.order_details)

    self.yes_no = ['Evet', 'Hayır']

    self.value_inside_commissioned = tk.StringVar(self.details_window)
    self.drop_commissioned = ttk.OptionMenu(self.details_window, self.value_inside_commissioned, self.yes_no[0], *self.yes_no)
    if slot_data.commissioned:
      self.value_inside_commissioned.set(self.yes_no[0])
    else:
      self.value_inside_commissioned.set(self.yes_no[1])
    self.drop_commissioned.config(width=15)
    self.drop_commissioned.grid(row=7, column=2, pady=5, padx=5, sticky='w')

    self.value_inside_paid = tk.StringVar(self.details_window)
    self.drop_paid = ttk.OptionMenu(self.details_window, self.value_inside_paid, self.yes_no[0], *self.yes_no)
    if slot_data.paid:
      self.value_inside_paid.set(self.yes_no[0])
    else:
      self.value_inside_paid.set(self.yes_no[1])
    self.drop_paid.config(width=15)
    self.drop_paid.grid(row=8, column=2, pady=5, padx=5, sticky='w')

    self.entry_9_btu_ac_no = ttk.Entry(self.details_window, width=10, font=("Arial", 12))
    self.entry_9_btu_ac_no.grid(row=9, column=2, pady=5, padx=5, sticky='w')
    self.entry_9_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_9_btu_ac_no.insert(tk.INSERT, slot_data._9_kBtu_p_h_no)

    self.entry_12_btu_ac_no = ttk.Entry(self.details_window, width=10, font=("Arial", 12))
    self.entry_12_btu_ac_no.grid(row=10, column=2, pady=5, padx=5, sticky='w')
    self.entry_12_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_12_btu_ac_no.insert(tk.INSERT, slot_data._12_kBtu_p_h_no)

    self.entry_18_btu_ac_no = ttk.Entry(self.details_window, width=10, font=("Arial", 12))
    self.entry_18_btu_ac_no.grid(row=11, column=2, pady=5, padx=5, sticky='w')
    self.entry_18_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_18_btu_ac_no.insert(tk.INSERT, slot_data._18_kBtu_p_h_no)

    self.entry_24_btu_ac_no = ttk.Entry(self.details_window, width=10, font=("Arial", 12))
    self.entry_24_btu_ac_no.grid(row=12, column=2, pady=5, padx=5, sticky='w')
    self.entry_24_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.entry_24_btu_ac_no.insert(tk.INSERT, slot_data._24_kBtu_p_h_no)

  def __delete_order(self, is_allocated, alloc_col, alloc_row, unalloc_row):
    ##delete the slot
    if is_allocated:
      self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].remove_slot_from_the_team(alloc_col, alloc_row)
    else:
      self.karer_hmi.calendar_data.unallocated_orders.pop(unalloc_row)

    ##close the 2 window
    try:
      self.sure_to_delete_window.destroy()
    except:
      print("delete as part of moving")
    self.details_window.destroy()

    ##refresh main page
    self.karer_hmi.refresh_page()

  def __move_to_alloc_list(self, slot_data, is_allocated, alloc_col, alloc_row, unalloc_row):
    try:
      date = datetime.strptime(self.entry_moveto_date.get(), '%Y-%m-%d').date()
    except:
      label_format = ttk.Label(self.canvas_move_to_date, text='Siz doktor diilsiniz. Şırıngada hava boşluğu var. (Tarihin formatı uymadı) :)', font=("Arial Bold", 10), background="Light Blue",foreground="red", width=70)
      label_format.grid(row=0, column=3, pady=0, padx=5, sticky='w')
      return

    try:
      self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].add_slot_to_the_team(slot_data,date)
      self.__delete_order(is_allocated, alloc_col, alloc_row, unalloc_row)
    except:
      label_format = ttk.Label(self.canvas_move_to_date, text='Siz doktor diilsiniz. Şırıngada hava boşluğu var. (Takım yok) :)', font=("Arial Bold", 10), background="Light Blue", foreground="red", width=70)
      label_format.grid(row=0, column=3, pady=0, padx=5, sticky='w')
      return

  def __move_to_unalloc_list(self, slot_data, is_allocated, alloc_col, alloc_row, unalloc_row):
    self.karer_hmi.calendar_data.unallocated_orders.append(slot_data)
    self.__delete_order(is_allocated, alloc_col, alloc_row, unalloc_row)

  def __are_you_sure_to_delete(self, is_allocated, alloc_col, alloc_row, unalloc_row):
    self.sure_to_delete_window = tk.Toplevel(self.details_window)
    self.sure_to_delete_window.title("Son Kararın mı?")
    self.sure_to_delete_window.geometry('300x200')
    self.sure_to_delete_window.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.sure_to_delete_window.iconphoto(False, p1)

    self.sure_to_delete_window.transient(self.details_window)  # set to be on top of the main window
    self.sure_to_delete_window.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)

    label = ttk.Label(self.sure_to_delete_window, text="Sipariş Silinsin mi?", font=("Arial Bold", 12), background="Light Blue", width=25)
    label.grid(row=0, column=0, pady=5, padx=5, sticky="w")

    yes_delete_button = ttk.Button(self.sure_to_delete_window, text="Evet", command=lambda: self.__delete_order(is_allocated, alloc_col, alloc_row, unalloc_row))
    yes_delete_button.grid(row=1, column=0, pady=5, padx=5, sticky='w')

  def datails_main_screen(self, slot_data, is_allocated, alloc_col, alloc_row, unalloc_row):
    print('Order placed at: ' + str(slot_data.date_of_order))
    print('Region: ' + str(slot_data.region))
    print('Address: ' + str(slot_data.address))
    print('Person: ' + str(slot_data.person))
    print('Telefon: ' + str(slot_data.tel))
    print('Order details: ' + str(slot_data.order_details))
    print('Commissioned: ' + str(slot_data.commissioned))
    print('Paid: ' + str(slot_data.paid))
    print('9 kbtu no: ' + str(slot_data._9_kBtu_p_h_no))
    print('12 kbtu no: ' + str(slot_data._12_kBtu_p_h_no))
    print('18 kbtu no: ' + str(slot_data._18_kBtu_p_h_no))
    print('24 kbtu no: ' + str(slot_data._24_kBtu_p_h_no))

    self.details_window = tk.Toplevel(self.karer_hmi.root)
    self.details_window.title("Detaylar")
    self.details_window.geometry('1200x600')
    self.details_window.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.details_window.iconphoto(False, p1)

    self.details_window.transient(self.karer_hmi.root)  # set to be on top of the main window
    self.details_window.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)



    self.__details_col1(slot_data)
    self.__details_col2(slot_data)
    self.__details_col3(slot_data)

    save_button = ttk.Button(self.details_window, text="Yeni Sipariş Detaylarını Kaydet", command=lambda: self.__save_button(slot_data))
    save_button.grid(row=13, column=2, pady=5, padx=5, sticky='w')

    delete_button = ttk.Button(self.details_window, text="Siparişi Sil", command=lambda: self.__are_you_sure_to_delete(is_allocated, alloc_col, alloc_row, unalloc_row))
    delete_button.grid(row=14, column=2, pady=5, padx=5, sticky='w')

    # Constructing the first frame, frame1
    self.canvas_move_to_date = tk.Canvas(self.details_window, bd=0, highlightthickness=0, width=30, height=1, bg="Light Blue")
    self.canvas_move_to_date.grid(row=15, column=2, pady=5, padx=5, sticky='w')

    self.entry_moveto_date = ttk.Entry(self.canvas_move_to_date, width=12, font=("Arial", 12))
    self.entry_moveto_date.grid(row=0, column=0, pady=0, padx=0, sticky='w')
    self.entry_moveto_date.insert(tk.INSERT, str(date.today()))

    label_format = ttk.Label(self.canvas_move_to_date, text='(yıl-ay-gün)', font=("Arial Bold", 12), background="Light Blue", width=10)
    label_format.grid(row=0, column=1, pady=0, padx=5, sticky='w')

    print(self.entry_moveto_date.get())
    #date_temp = datetime.strptime(self.entry_moveto_date.get(),'%y-%m-%d').date()
    move_to_date_btn = ttk.Button(self.canvas_move_to_date, text="gününe aktar", command=lambda: self.__move_to_alloc_list(slot_data, is_allocated, alloc_col, alloc_row,unalloc_row))
    move_to_date_btn.grid(row=0, column=2, pady=0, padx=5, sticky='w')

    move_to_unalloc_btn = ttk.Button(self.details_window, text="Tahsis Edilmemiş Sipariş Listesine aktar", command=lambda: self.__move_to_unalloc_list(slot_data, is_allocated, alloc_col, alloc_row, unalloc_row))
    move_to_unalloc_btn.grid(row=16, column=2, pady=5, padx=5, sticky='w')


  def __init__(self, hmi):
    self.karer_hmi = hmi


class text_entry_rules:

  #def reg_digits(self):
  #  return self.window.register(self.callback_digits)

  @staticmethod
  def callback_digits(input):
    if input.isdigit():
      print(input)
      return True

    elif input == "":
      print(input)
      return True

    else:
      print(input)
      return False

class manage_teams_popup:
  def __change_team_name(self,index):
    self.karer_hmi.calendar_data.all_teams_data[index].team_name = self.new_team_name_text.get()
    self.ammend_team.destroy()
    self.__list_team_names()
    #self.karer_hmi.present_team_name()
    #self.karer_hmi.place_dates_and_allocated_orders()
    self.karer_hmi.refresh_page()


  def __delete_team(self,index):
    #self.__clear_the_team_names_from_the_list()
    self.karer_hmi.calendar_data.all_teams_data.pop(index)
    self.ammend_team.destroy()
    self.__list_team_names()
    if self.karer_hmi.current_team_index >= len(self.karer_hmi.calendar_data.all_teams_data):
      self.karer_hmi.current_team_index = len(self.karer_hmi.calendar_data.all_teams_data) - 1
    if self.karer_hmi.current_team_index < 0:
      self.karer_hmi.current_team_index = 0

    print('simdiki takim: ' + str(self.karer_hmi.current_team_index))
    #self.karer_hmi.present_team_name()
    #self.karer_hmi.place_dates_and_allocated_orders()
    self.karer_hmi.refresh_page()

    #destroy question window
    self.sure_to_del_win.destroy()

  def __are_you_sure_to_delete(self,index):
    self.sure_to_del_win = tk.Toplevel(self.ammend_team)
    self.sure_to_del_win.title("Emin misin?")
    self.sure_to_del_win.geometry('600x200')
    self.sure_to_del_win.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.sure_to_del_win.iconphoto(False, p1)

    self.sure_to_del_win.transient(self.ammend_team)  # set to be on top of the main window
    self.sure_to_del_win.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)

    label_are_you_sure = ttk.Label(self.sure_to_del_win, text=str(index + 1) + ". " + self.karer_hmi.calendar_data.all_teams_data[index].team_name + ' takımını silmek istediğinden eminsin?', font=("Arial", 12), background="Light Blue")
    label_are_you_sure.grid(row=0, column=0, pady=5, padx=5)

    delete_Team = ttk.Button(self.sure_to_del_win, text="Evet", command=lambda: self.__delete_team(index))
    delete_Team.grid(row=1, column=0, pady=5, padx=5)

  def __select_team(self,index):
    self.karer_hmi.current_team_index = index
    self.ammend_team.destroy()
    #self.team_window.destroy()
    #self.karer_hmi.present_team_name()
    #self.karer_hmi.place_dates_and_allocated_orders()
    self.karer_hmi.refresh_page()


  def __delete_or_select_team(self,team_index):
    self.ammend_team = tk.Toplevel(self.team_window)
    self.ammend_team.title("Takımı Düzenle")
    self.ammend_team.geometry('700x300')
    self.ammend_team.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.ammend_team.iconphoto(False, p1)

    self.ammend_team.transient(self.team_window)  # set to be on top of the main window
    self.ammend_team.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)

    lbl_team = ttk.Label(self.ammend_team, text=str(team_index + 1) + ". " + self.karer_hmi.calendar_data.all_teams_data[team_index].team_name, font=("Arial", 12))
    lbl_team.place(x=20, y=20)

    self.new_team_name_text = ttk.Entry(self.ammend_team, width=15, font=("Arial", 12))
    self.new_team_name_text.place(x=20, y=100)
    self.new_team_name_text.insert(tk.INSERT, self.karer_hmi.calendar_data.all_teams_data[team_index].team_name)

    add_Team = ttk.Button(self.ammend_team, text="Takım adını degiştir", command=lambda index=team_index: self.__change_team_name(index))
    add_Team.place(x=20, y=125)

    delete_Team = ttk.Button(self.ammend_team, text="Takımı sil", command=lambda index=team_index: self.__are_you_sure_to_delete(index))
    delete_Team.place(x=200, y=125)

    select_team = ttk.Button(self.ammend_team, text="Takımı seç", command=lambda index=team_index: self.__select_team(index))
    select_team.place(x=400, y=125)



  def __list_team_names(self):
    self.lbl_team_header = ttk.Label(self.team_window, text="Takımlar", font=("Arial Bold", 12))
    self.lbl_team_header.place(x=20, y=10)

    for i in range(len(self.lbl_team_list)):
      try:
        self.lbl_team_list[i].after(10, self.lbl_team_list[i].destroy())
      except:
        print("list teams err")

    self.lbl_team_list = []  # empty list

    for i in range(len(self.karer_hmi.calendar_data.all_teams_data)):
      self.lbl_team_list.append(ttk.Button(self.team_window, text= str(i+1) + ". " + self.karer_hmi.calendar_data.all_teams_data[i].team_name, command=lambda team_index=i: self.__delete_or_select_team(team_index)))
      self.lbl_team_list[i].place(x=20, y=40 + i * 25)

  def __add_team(self):
    self.karer_hmi.calendar_data.add_team(self.team_to_add_text.get())
    self.__list_team_names()
    #self.karer_hmi.present_team_name()
    #self.karer_hmi.place_dates_and_allocated_orders()
    self.karer_hmi.refresh_page()

  def __manage_teams_window(self):
    self.team_window = tk.Toplevel(self.karer_hmi.root)
    self.team_window.title("Karer Takım Penceresi")
    self.team_window.geometry('700x300')
    self.team_window.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.team_window.iconphoto(False, p1)

    self.team_window.transient(self.karer_hmi.root)  # set to be on top of the main window
    #self.team_window.wait_visibility()
    self.team_window.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)

    self.__list_team_names()

    self.team_to_add_text = ttk.Entry(self.team_window, width=15, font=("Arial",12))
    self.team_to_add_text.place(x=200,y=40)
    self.team_to_add_text.insert(tk.INSERT, 'Yeni Takım')

    add_Team = ttk.Button(self.team_window, text="Takımı Ekle", command=self.__add_team)
    add_Team.place(x=200, y=65)

  def teams_button(self):
    Teams = ttk.Button(self.karer_hmi.window_header, text="Takımlar", command=self.__manage_teams_window)
    Teams.place(x=350, y=30)

  def __init__(self, hmi):
    self.karer_hmi = hmi

    self.lbl_team_list = []  # empty list

class add_order_popup:
  def __add_the_order(self):

    if self.text_adr.get() != "" and \
            self.text_Person.get() != "" and \
            self.text_tel.get() != "" and \
            self.text_order_details.get() != "" and \
            self.text_9_btu_ac_no.get() != "" and \
            self.text_12_btu_ac_no.get() != "" and \
            self.text_18_btu_ac_no.get() != "" and \
            self.text_24_btu_ac_no.get() != "":
      try:
        self.karer_hmi.calendar_data.add_an_unallocated_slot(region=self.value_inside_region.get(),
                                                             address=self.text_adr.get(),
                                                             person=self.text_Person.get(),
                                                             tel=self.text_tel.get(),
                                                             order_details=self.text_order_details.get(),
                                                             btu_9_no=int(self.text_9_btu_ac_no.get()),
                                                             btu_12_no=int(self.text_12_btu_ac_no.get()),
                                                             btu_18_no=int(self.text_18_btu_ac_no.get()),
                                                             btu_24_no=int(self.text_24_btu_ac_no.get()))

        self.take_order_window.destroy()
        self.karer_hmi.refresh_page()
      except:
        current_team_label = ttk.Label(self.take_order_window, text="Klima sayısı nümerik olmalı", font=("Arial Bold", 12),background="Light Blue", foreground="Red")
        current_team_label.grid(row=10, column=1, sticky='w')



    else:
      current_team_label = ttk.Label(self.take_order_window, text="Bütün boşlukları doldurunuz", font=("Arial Bold", 12), background="Light Blue", foreground= "Red")
      current_team_label.grid(row=10, column=1, sticky='w')


  def __take_order(self):
    self.take_order_window = tk.Toplevel(self.karer_hmi.root)
    self.take_order_window.title("Sipariş Al")
    self.take_order_window.geometry('800x400')
    self.take_order_window.config(background="Light Blue")

    # photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.take_order_window.iconphoto(False, p1)

    self.take_order_window.transient(self.karer_hmi.root)  # set to be on top of the main window
    #self.take_order_window.wait_visibility()
    self.take_order_window.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)

    reg_digits = self.take_order_window.register(text_entry_rules.callback_digits)

    current_team_label = ttk.Label(self.take_order_window, text="Bölge:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=0, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="Adres:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=1, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="Şahıs:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=2, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="Telefon:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=3, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="Sipariş Detayları:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=4, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="9 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=5, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="12 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=6, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="18 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=7, column=0, pady=5, padx=5)

    current_team_label = ttk.Label(self.take_order_window, text="24 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=8, column=0, pady=5, padx=5)

    #text_region = Text(take_order_window, width=30, height=1, font=("Arial",12))
    #text_region.grid(row=0, column=1)
    # Create Dropdown menu
    # datatype of menu text
    self.value_inside_region = tk.StringVar(self.take_order_window)
    self.value_inside_region.set(self.karer_hmi.calendar_data.regions[0])
    self.drop_region = ttk.OptionMenu(self.take_order_window, self.value_inside_region, self.karer_hmi.calendar_data.regions[0], *self.karer_hmi.calendar_data.regions)
    self.drop_region.config(width= 30)
    self.drop_region.grid(row=0, column=1, sticky='w')

    self.text_adr = ttk.Entry(self.take_order_window, width=60, font=("Arial",12))
    self.text_adr.grid(row=1, column=1, sticky='w')

    self.text_Person = ttk.Entry(self.take_order_window, width=30, font=("Arial",12))
    self.text_Person.grid(row=2, column=1, sticky='w')

    self.text_tel = ttk.Entry(self.take_order_window, width=30, font=("Arial",12))
    self.text_tel.grid(row=3, column=1, sticky='w')

    self.text_order_details = ttk.Entry(self.take_order_window, width=60, font=("Arial",12))
    self.text_order_details.grid(row=4, column=1, sticky='w')

    self.text_9_btu_ac_no = ttk.Entry(self.take_order_window, width=10,font=("Arial", 12))
    self.text_9_btu_ac_no.grid(row=5, column=1, sticky='w')
    self.text_9_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.text_9_btu_ac_no.insert(tk.INSERT, "0")

    self.text_12_btu_ac_no = ttk.Entry(self.take_order_window, width=10, font=("Arial", 12))
    self.text_12_btu_ac_no.grid(row=6, column=1, sticky='w')
    self.text_12_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.text_12_btu_ac_no.insert(tk.INSERT, "0")

    self.text_18_btu_ac_no = ttk.Entry(self.take_order_window, width=10, font=("Arial", 12))
    self.text_18_btu_ac_no.grid(row=7, column=1, sticky='w')
    self.text_18_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.text_18_btu_ac_no.insert(tk.INSERT, "0")

    self.text_24_btu_ac_no = ttk.Entry(self.take_order_window, width=10, font=("Arial", 12))
    self.text_24_btu_ac_no.grid(row=8, column=1, sticky='w')
    self.text_24_btu_ac_no.config(validate="key", validatecommand=(reg_digits, '%P'))
    self.text_24_btu_ac_no.insert(tk.INSERT, "0")

    take_order = ttk.Button(self.take_order_window, text="Onayla", command=self.__add_the_order)
    take_order.grid(row=9, pady=5, padx=5, column=1, sticky='w')

  def take_order_button(self):
    take_order = ttk.Button(self.karer_hmi.window_header, text="Sipariş Al", command=self.__take_order)
    take_order.place(x=250, y=30)

  def __init__(self, hmi):
    self.karer_hmi = hmi

class drag_n_drop:
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        # Label(win, text="Arda", font=("Arial Bold", 15), background="Light Blue", width=20).place(x=600,y=600)
        # widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        self.x_coordinates_of_button_click = event.x
        self.y_coordinates_of_button_click = event.y

        #Find which unallocated order canvas has been moved
        self.unallocated_order_found = False
        self.unallocated_order_found_no = 0
        for i in range(len(self.karer_hmi.unallocated_order_canv)):
          if self.karer_hmi.unallocated_order_canv[i] == event.widget:
            print("Unallocated Order " + str(i) + " is being moved")
            self.unallocated_order_found = True
            self.unallocated_order_found_no = i

        # Find which allocated order canvas has been moved
        self.allocated_order_found = False
        allocated_order_canvas_found_no = 0
        self.allocated_order_found_no = 0
        self.allocated_order_found_date = 0
        if self.unallocated_order_found == False:
          for i in range(len(self.karer_hmi.allocated_order_canv)):
            if self.karer_hmi.allocated_order_canv[i] == event.widget:
              self.allocated_order_found = True
              allocated_order_canvas_found_no = i

        #Map allocated order canvas to the data
        slot_arr = []
        inspected_allocated_order = 0
        if self.allocated_order_found:
          for col in range(self.karer_hmi.no_of_days):
            try:
              slot_arr = self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].get_slots_for_the_day(self.karer_hmi.dates_arr[col])
            except:
              print("no team present")

            for row in range(len(slot_arr)):
              if allocated_order_canvas_found_no == inspected_allocated_order:
                print("Allocated Order day " + str(self.karer_hmi.dates_arr[col]) + " row " + str(row) + " is being moved.")
                self.allocated_order_found_no = row
                self.allocated_order_found_date = self.karer_hmi.dates_arr[col]
              inspected_allocated_order = inspected_allocated_order + 1


        # print("started")
        pass

    def on_drag(self, event):

        event.widget.place(
            x=self.window.winfo_pointerx() - self.window.winfo_rootx() - self.x_coordinates_of_button_click,
            y=self.window.winfo_pointery() - self.window.winfo_rooty() - self.y_coordinates_of_button_click)
        print(self.window.winfo_pointerx() - self.window.winfo_rootx() - self.x_coordinates_of_button_click + 90)

    def on_drop(self, event):
        # find the widget under the cursor
        print("dropped")
        allocated_start_x = 170
        allocated_gap_x = 180
        canvas_last_x_coordinate = self.window.winfo_pointerx() - self.window.winfo_rootx() - self.x_coordinates_of_button_click + allocated_gap_x/2
        unallocated_start_x = 1450
        unallocated_gap_x = 180

        destination_is_allocated = False
        destination_allocated_day = 0
        destination_is_unallocated = False


        ##CHECK IF THE DESTINATION IS IN ALLOCATED REGION
        for col in range(self.karer_hmi.no_of_days):
          if canvas_last_x_coordinate > allocated_start_x + col * allocated_gap_x and canvas_last_x_coordinate <= allocated_start_x + (col+1) * allocated_gap_x:
            print('Moving the slot to day ' + str(self.karer_hmi.dates_arr[col]))
            destination_is_allocated = True
            destination_allocated_day = self.karer_hmi.dates_arr[col]

        ##CHECK IF THE DESTINATION IS IN UNALLOCATED REGION
        if destination_is_allocated == False:
          if canvas_last_x_coordinate > unallocated_start_x and canvas_last_x_coordinate <= unallocated_start_x + unallocated_gap_x:
            destination_is_unallocated = True

        if len(self.karer_hmi.calendar_data.all_teams_data) != 0:
          if (self.allocated_order_found or self.unallocated_order_found) and (destination_is_allocated or destination_is_unallocated):
            ##PREPARE THE SLOT TO BE MOVED and delete the dragged slot
            if self.allocated_order_found == True:
              slot_to_move = self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].remove_slot_from_the_team(self.allocated_order_found_date,self.allocated_order_found_no)
            elif self.unallocated_order_found == True:
              slot_to_move = self.karer_hmi.calendar_data.unallocated_orders.pop(self.unallocated_order_found_no)
            else:
              return

            ##Move the DRAGGED SLOT TO ITS NEW LOCATION
            if destination_is_allocated == True:
              self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].add_slot_to_the_team(slot_to_move,destination_allocated_day)
            elif destination_is_unallocated == True:
              self.karer_hmi.calendar_data.unallocated_orders.append(slot_to_move)
            else:
              return


        self.karer_hmi.refresh_page()

    def __init__(self,win,hmi):
        self.window = win
        self.karer_hmi = hmi

class karer_Calendar_HMI:

  def place_canvas(self, x_axis, y_axis, slot_data, is_allocated, alloc_col, alloc_row, unalloc_row):
    rect_w = 160
    rect_h = 80
    canvas_out = tk.Canvas(self.window, width=rect_w, height=rect_h, bg="Beige", bd=0, highlightthickness=0, )
    canvas_out.place(x=x_axis, y=y_axis)
    self.drag.add_dragable(canvas_out)
    label = ttk.Label(canvas_out, text=slot_data.person + "\n" + slot_data.region, font=("Arial", 11), background="Beige")
    label.place(x=5, y=5)
    button = ttk.Button(canvas_out, text="Detaylar", command=lambda: self.dtls_popup.datails_main_screen(slot_data, is_allocated, alloc_col, alloc_row, unalloc_row))
    button.place(x=40, y=50)

    #determine if the canvas needs to be reconfigured
    if y_axis + rect_h > self.required_height:
      self.required_height = y_axis + rect_h + 10

    return canvas_out

  def place_unallocated_orders(self):

    start_x_rec = 1450
    start_y_rec = 10

    label_offset = 85

    lbl_unalloc_order = ttk.Label(self.window_header, text= "Tahsis Edilmemiş\nSiparişler", font=("Arial Bold", 15), background = "Light Blue", width= 20)
    lbl_unalloc_order.configure(anchor="w")
    lbl_unalloc_order.place(x=start_x_rec,y=95)

    for i in range(len(self.unallocated_order_canv)):
      try:
        self.unallocated_order_canv[i].destroy()
      except:
        print("table setroy err")


    self.unallocated_order_canv = []



    for i in range(len(self.calendar_data.unallocated_orders)):
      self.unallocated_order_canv.append(self.place_canvas(x_axis = start_x_rec,
                                                           y_axis = start_y_rec + i * label_offset,
                                                           slot_data = self.calendar_data.unallocated_orders[i],
                                                           is_allocated = False,
                                                           alloc_col = 0,
                                                           alloc_row = 0,
                                                           unalloc_row = i))

  def __place_in_table(self, row, column, content, back):
    start_x = 170
    start_y = 95
    gap_x = 180
    gap_y = 30
    width_x = 12
    try:
      self.lbl_table_header[row][column].destroy()
    except:
      print("table setroy err")
    self.lbl_table_header[row][column] = ttk.Label(self.window_header, width= width_x, text=content, font=("Arial Bold", 15), background = back)
    self.lbl_table_header[row][column].place(x=start_x + gap_x * column, y=start_y + gap_y * row)

  def __place_logo(self):
    ## PUT THE IMAGE ON THE TOP LEFT CORNER
    # Load the image
    image_karer = Image.open('logo_karer.png')
    # Resize the image in the given (width, height)
    image_karer_R = image_karer.resize((150, 75))
    # Conver the image in TkImage
    my_img_karer = ImageTk.PhotoImage(image_karer_R)
    # Display the image with label
    lbl_karer = ttk.Label(self.window_header, image=my_img_karer)
    lbl_karer.place(x=10, y=10)
    lbl_karer.image = my_img_karer

  def __place_the_days_of_week(self):
    self.__place_in_table(0, 0, "Pazartesi", "Light Blue")
    self.__place_in_table(0, 1, "Salı", "Light Blue")
    self.__place_in_table(0, 2, "Çarşamba", "Light Blue")
    self.__place_in_table(0, 3, "Perşembe", "Light Blue")
    self.__place_in_table(0, 4, "Cuma", "Light Blue")
    self.__place_in_table(0, 5, "Cumartesi", "Light Blue")
    self.__place_in_table(0, 6, "Pazar", "Light Blue")

  def __place_the_allocated_orders_for_the_week(self):


    start_x = 170
    start_y = 10
    gap_x = 180
    gap_y = 85

    for temp in self.allocated_order_canv:
      try:
        temp.destroy()
      except:
        print("couldnt destroy allocated canvas")

    #empty the allocated order arr
    self.allocated_order_canv = []

    #finally place the canvases one by one
    for col in range(self.no_of_days):
      try:
        slot_arr = self.calendar_data.all_teams_data[self.current_team_index].get_slots_for_the_day(self.dates_arr[col])
        for row in range(len(slot_arr)):
          self.allocated_order_canv.append(self.place_canvas(x_axis=start_x + col * gap_x,
                                                             y_axis=start_y + row * gap_y,
                                                             slot_data=slot_arr[row],
                                                             is_allocated=True,
                                                             alloc_col=self.dates_arr[col],
                                                             alloc_row=row,
                                                             unalloc_row=0))
      except:
        print("no team present")

  def place_dates_and_allocated_orders(self):
    for i in range(self.no_of_days):
      if self.dates_arr[i] == date.today():
        self.__place_in_table(1, i, self.dates_arr[i], "light green")
      else:
        self.__place_in_table(1, i, self.dates_arr[i], "Light Blue")

    self.__place_the_allocated_orders_for_the_week()

  def __refresh_everything_according_to_today(self):
    ##FIND TODAYS DATE
    days_arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = date.today()
    which_day_is_today = 0
    ##SPOT WHAT DAY IS TODAY
    for i in range(self.no_of_days):
      if today.strftime('%A') == days_arr[i]:
        which_day_is_today = i
    ##PLACE THE DATES TO 1st COLUMN
    for i in range(self.no_of_days):
      self.dates_arr[i] = today + timedelta(days=i - which_day_is_today)

    #self.place_dates_and_allocated_orders()
    self.refresh_page()

  def __go_one_week_back(self):

    for i in range(self.no_of_days):
      self.dates_arr[i] = self.dates_arr[i] - timedelta(days= 7)

    self.place_dates_and_allocated_orders()

  def __go_one_week_forward(self):


    for i in range(self.no_of_days):
      self.dates_arr[i] = self.dates_arr[i] + timedelta(days=7)

    self.place_dates_and_allocated_orders()

  def __forward_backward_today_buttons(self):
    Backwards = ttk.Button(self.window_header, text="<", command = self.__go_one_week_back)
    Backwards.place(x=500, y=30)

    Today = ttk.Button(self.window_header, text="Bu gün", command=self.__refresh_everything_according_to_today)
    Today.place(x=600, y=30)

    Forwards = ttk.Button(self.window_header, text=">", command=self.__go_one_week_forward)
    Forwards.place(x=700, y=30)



  def present_team_name(self):
    try:
      text_temp = "Seçilen takım: " + str(self.current_team_index + 1) + ". " + self.calendar_data.all_teams_data[self.current_team_index].team_name
    except:
      text_temp = "Takım yok"

    try:
      self.current_team_label.destroy()
    except:
      print("presented team err")
    self.current_team_label = ttk.Label(self.window_header, text=text_temp, font=("Arial Bold", 12), background= "Light Blue")
    self.current_team_label.place(x=800, y=30)



  def refresh_page(self):
    self.required_height = 0

    self.place_unallocated_orders()
    self.place_dates_and_allocated_orders()
    self.present_team_name()

    print("required height is " + str(self.required_height))

    if self.required_height > 1000:
      self.window.config(height=self.required_height)
    else:
      self.window.config(height=1000)

    file_pi = open('data.pkl', 'wb')
    pickle.dump(self.calendar_data, file_pi)



  def on_canvas_configure(self,event):
    self.canvas.config(scrollregion=self.canvas.bbox("all"))

  def on_mousewheel(self,event):
    self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

  def on_canvas_configure_horizontal(self,event):
    self.canvas.config(scrollregion=self.canvas.bbox("all"))

  def on_mousewheel_horizontal(self,event):
    self.canvas.xview_scroll(-1 * (event.delta // 120), "units")

  def on_canvas_configure_header(self,event):
    self.canvas_header.config(scrollregion=self.canvas_header.bbox("all"))

  def on_mousewheel_header(self,event):
    self.canvas_header.yview_scroll(-1 * (event.delta // 120), "units")

  def on_canvas_configure_horizontal_header(self,event):
    self.canvas_header.config(scrollregion=self.canvas_header.bbox("all"))

  def on_mousewheel_horizontal_header(self,event):
    self.canvas_header.xview_scroll(-1 * (event.delta // 120), "units")

  def combine_xview(self, *args):
    self.canvas_header.xview(*args)
    self.canvas.xview(*args)


  def __make_scrollable_page(self):
    self.root = tk.Tk()
    self.root.title("Karer Montaj Takvimi")
    self.root.geometry("800x600")

    #photo
    p1 = tk.PhotoImage(file='logo_karer_top_left.png')
    # Setting icon of master window
    self.root.iconphoto(False, p1)

    self.canvas_header = tk.Canvas(self.root, bd=0, highlightthickness=0, bg="Light Blue", scrollregion=(0, 0, 800, 600), width=2000, height=155)  # width=2000, height=1300,
    self.canvas_header.grid(row=0, column=0, sticky="nsew")

    # Create a Canvas widget with scrollbars
    self.canvas = tk.Canvas(self.root, bd=0, highlightthickness=0, bg="Light Blue", scrollregion=(0, 0, 800, 600), width=2000, height=1000)  # width=2000, height=1300,
    self.canvas.grid(row=1, column=0, sticky="nsew")


    v_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
    v_scrollbar.grid(row=0, column=1, rowspan=2, sticky="ns")
    self.canvas.config(yscrollcommand=v_scrollbar.set)
    #self.canvas_header.config(yscrollcommand=v_scrollbar.set)

    #HORIZONTAL SCROLLBAR REMOVED!!!!!!
    h_scrollbar = tk.Scrollbar(self.root, orient="horizontal", command=self.combine_xview)
    h_scrollbar.grid(row=2, column=0, sticky="ew")
    self.canvas.config(xscrollcommand=h_scrollbar.set)
    self.canvas_header.config(xscrollcommand=h_scrollbar.set)


    # Add widgets to the canvas
    frame = tk.Frame(self.canvas, bg="lightblue")
    self.canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas_new = tk.Canvas(frame,bd=0, highlightthickness=0, width=2000, height=1000, bg="Light Blue")
    canvas_new.grid(row=0, column=0, sticky="nw")
    self.window = canvas_new

    # Add widgets to the header canvas
    frame_head = tk.Frame(self.canvas_header, bg="lightblue")
    self.canvas_header.create_window((0, 0), window=frame_head, anchor="nw")
    canvas_new_head = tk.Canvas(frame_head, bd=0, highlightthickness=0, width=2000, height=155, bg="Light Blue")
    canvas_new_head.grid(row=0, column=0, sticky="nw")
    self.window_header = canvas_new_head


    # Bind events for scrolling
    self.canvas.bind("<Configure>", self.on_canvas_configure)
    self.canvas.bind("<MouseWheel>", self.on_mousewheel)
    self.canvas.bind("<Configure>", self.on_canvas_configure_horizontal, add="+")
    self.canvas.bind("<Shift-MouseWheel>", self.on_mousewheel_horizontal)

    self.canvas_header.bind("<Configure>", self.on_canvas_configure_header)
    self.canvas_header.bind("<MouseWheel>", self.on_mousewheel_header)
    self.canvas_header.bind("<Configure>", self.on_canvas_configure_horizontal_header, add="+")
    self.canvas_header.bind("<Shift-MouseWheel>", self.on_mousewheel_horizontal_header)

    # Make the GUI resizable
    self.root.columnconfigure(0, weight=1)
    #self.root.rowconfigure(0, weight=1)
    self.root.rowconfigure(1, weight=1)

    #self.root.mainloop()

  def __auto_alloc_button(self):
    btn_auto_alloc = ttk.Button(self.window_header, text="Otomatik Sipariş Yerleştirme", command=self.auto_allocation_popup.popup)
    btn_auto_alloc.place(x=1100, y=30)

  def __init__(self):

    try:
      filehandler = open('data.pkl', 'rb')
      self.calendar_data = pickle.load(filehandler)
      print('file exists')
    except:
      print('its the first time ever, file doesnt exist')
      self.calendar_data = data_class.karer_data()


    #self.window = Tk()
    #self.window.title("Karer Montaj Takvimi")
    #self.window.geometry("800x600")
    #self.window.config(background="Light Blue")


    self.__make_scrollable_page()

    self.auto_allocation_popup = auto_allocation_popup(self)

    self.mng_teams_popup = manage_teams_popup(self)

    self.dtls_popup = details_popup(self)

    self.drag = drag_n_drop(self.window, self)

    self.add_ordr_popup = add_order_popup(self)

    self.current_team_index = 0

    self.__place_logo()

    ##INITIALISE THE TABLE
    self.no_of_days = 7
    self.total_col_header = 7
    self.total_row_header = 2
    self.lbl_table_header = [[0 for x in range(self.total_col_header)] for y in range(self.total_row_header)]
    self.dates_arr = [0 for x in range(self.no_of_days)]


    self.unallocated_order_canv = []
    self.allocated_order_canv = []

    #self.place_unallocated_orders()

    self.__place_the_days_of_week()

    self.__refresh_everything_according_to_today()

    self.__forward_backward_today_buttons()

    self.__auto_alloc_button()

    self.mng_teams_popup.teams_button()

    #self.present_team_name()

    #self.refresh_page()

    self.add_ordr_popup.take_order_button()

    self.root.mainloop()


