import numpy as np
import datetime
class slot_data:

    def __init__(self,):
        self.date_of_order = datetime.datetime.today()
        self.region = ""
        self.address = ""
        self.person = ""
        self.tel = ""
        self.order_details = ""
        self._9_kBtu_p_h_no = 0
        self._12_kBtu_p_h_no = 0
        self._18_kBtu_p_h_no = 0
        self._24_kBtu_p_h_no = 0
        self.commissioned = False
        self.paid = False

class day_data:

    def __init__(self, date, first_slot):
        self.slot_arr = []
        self.slot_arr.append(first_slot)
        self.date_of_data = date

class auto_alloc_vars:
    def __init__(self):
        self.daily_max_order_nicosia = 6
        self.daily_min_order_nicosia = 2
        self.daily_max_order_west = 6
        self.daily_min_order_west = 2
        self.daily_max_order_east = 6
        self.daily_min_order_east = 2
        self.daily_max_order_kyrenia = 6
        self.daily_min_order_kyrenia = 2
        self.dates_to_avoid = [ datetime.datetime.strptime('2024-10-29', '%Y-%m-%d').date(),
                                datetime.datetime.strptime('2024-05-19', '%Y-%m-%d').date(),
                                datetime.datetime.strptime('2024-04-23', '%Y-%m-%d').date()]
        self.days_to_avoid = [False, False, False, False, False, False, True] #ONLY AVOID SUNDAY
        self.no_of_days_for_op = 10

class team_data:


    def __init__(self,unalloc_orders):
        self.unallocated_orders = unalloc_orders
        self.day_arr = []
        self.team_name = ""
        self.aut_alloc_vars = auto_alloc_vars()

        self.nicosia = 0
        self.kyrenia = 1
        self.west = 2
        self.east = 3
        self.bi_city = 4
        self.no_city = 5
        self.regions = ["Lefkoşa", "Girne", "Batı", "Doğu"]

    def __determine_no_of_unalloc_orders_for_each_city(self):


        self.no_of_unallocated_nicosia_orders = 0
        self.no_of_unallocated_kyrenia_orders = 0
        self.no_of_unallocated_west_orders = 0
        self.no_of_unallocated_east_orders = 0

        for slots_in_ualloc_orders in self.unallocated_orders:
            if slots_in_ualloc_orders.region == self.regions[self.nicosia]:
                self.no_of_unallocated_nicosia_orders = self.no_of_unallocated_nicosia_orders + 1
            elif slots_in_ualloc_orders.region == self.regions[self.kyrenia]:
                self.no_of_unallocated_kyrenia_orders = self.no_of_unallocated_kyrenia_orders + 1
            elif slots_in_ualloc_orders.region == self.regions[self.west]:
                self.no_of_unallocated_west_orders = self.no_of_unallocated_west_orders + 1
            elif slots_in_ualloc_orders.region == self.regions[self.east]:
                self.no_of_unallocated_east_orders = self.no_of_unallocated_east_orders + 1

        print("Unalloc no of orders nicosia " + str(self.no_of_unallocated_nicosia_orders))
        print("Unalloc no of orders kyrenia " + str(self.no_of_unallocated_kyrenia_orders))
        print("Unalloc no of orders west " + str(self.no_of_unallocated_west_orders))
        print("Unalloc no of orders east " + str(self.no_of_unallocated_east_orders))

    def auto_order_placement(self):


        remaining_days = self.aut_alloc_vars.no_of_days_for_op
        day_of_operation = datetime.date.today()

        while remaining_days != 0:
            remaining_days = remaining_days - 1
            day_of_operation = day_of_operation + datetime.timedelta(days=1)
            if self.__is_the_day_to_be_skipped(day_of_operation) == False:
                self.__determine_no_of_unalloc_orders_for_each_city()

                slots_for_the_days = self.get_slots_for_the_day(day_of_operation)
                city_status_for_the_day = self.no_city
                for slots_temp in slots_for_the_days:
                    if slots_temp.region == self.regions[self.nicosia] and city_status_for_the_day == self.no_city:
                        city_status_for_the_day = self.nicosia
                    elif slots_temp.region == self.regions[self.kyrenia] and city_status_for_the_day == self.no_city:
                        city_status_for_the_day = self.kyrenia
                    elif slots_temp.region == self.regions[self.west] and city_status_for_the_day == self.no_city:
                        city_status_for_the_day = self.west
                    elif slots_temp.region == self.regions[self.east] and city_status_for_the_day == self.no_city:
                        city_status_for_the_day = self.east
                    elif slots_temp.region == self.regions[self.nicosia] and city_status_for_the_day != self.nicosia:
                        city_status_for_the_day = self.bi_city
                    elif slots_temp.region == self.regions[self.kyrenia] and city_status_for_the_day != self.kyrenia:
                        city_status_for_the_day = self.bi_city
                    elif slots_temp.region == self.regions[self.west] and city_status_for_the_day != self.west:
                        city_status_for_the_day = self.bi_city
                    elif slots_temp.region == self.regions[self.east] and city_status_for_the_day != self.east:
                        city_status_for_the_day = self.bi_city
                print("City status for " + str(day_of_operation) + " is " + str(city_status_for_the_day))

                if self.no_of_unallocated_nicosia_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_nicosia and city_status_for_the_day == self.nicosia:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation,city_status_for_the_day,self.aut_alloc_vars.daily_max_order_nicosia - len(slots_for_the_days))
                elif self.no_of_unallocated_kyrenia_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_kyrenia and city_status_for_the_day == self.kyrenia:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, city_status_for_the_day, self.aut_alloc_vars.daily_max_order_kyrenia - len(slots_for_the_days))
                elif self.no_of_unallocated_east_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_east and city_status_for_the_day == self.east:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, city_status_for_the_day, self.aut_alloc_vars.daily_max_order_east - len(slots_for_the_days))
                elif self.no_of_unallocated_west_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_west and city_status_for_the_day == self.west:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, city_status_for_the_day, self.aut_alloc_vars.daily_max_order_west - len(slots_for_the_days))
                elif self.no_of_unallocated_nicosia_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_nicosia and city_status_for_the_day == self.no_city:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, self.nicosia, self.aut_alloc_vars.daily_max_order_nicosia - len(slots_for_the_days))
                elif self.no_of_unallocated_kyrenia_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_kyrenia and city_status_for_the_day == self.no_city:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, self.kyrenia, self.aut_alloc_vars.daily_max_order_kyrenia - len(slots_for_the_days))
                elif self.no_of_unallocated_east_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_east and city_status_for_the_day == self.no_city:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, self.east, self.aut_alloc_vars.daily_max_order_east - len(slots_for_the_days))
                elif self.no_of_unallocated_west_orders + len(slots_for_the_days) >= self.aut_alloc_vars.daily_min_order_west and city_status_for_the_day == self.no_city:
                    self.__move_unallocated_orders_from_one_region_to_a_day(day_of_operation, self.west, self.aut_alloc_vars.daily_max_order_west - len(slots_for_the_days))


    def __is_the_day_to_be_skipped(self,day):
        bool_to_return = False

        # if any of the dates to be avoided is equal to the day of operation
        for day_to_avoid in self.aut_alloc_vars.dates_to_avoid:
            if day == day_to_avoid:
                bool_to_return = True

        # if the day of the week the day of operation is at is to be avoided, avoid the day
        if self.aut_alloc_vars.days_to_avoid[day.weekday()] == True:
            bool_to_return = True

        return bool_to_return


    def __move_unallocated_orders_from_one_region_to_a_day(self, day, region_selection, no_of_remaining_slots):
        if no_of_remaining_slots >= 0:
            for i in range(no_of_remaining_slots):
                for j in range(len(self.unallocated_orders)):
                    if self.unallocated_orders[j].region == self.regions[region_selection]:
                        temp_slot_to_move = self.unallocated_orders.pop(j)
                        self.add_slot_to_the_team(temp_slot_to_move, day)
                        break



    def remove_slot_from_the_team(self, date, date_index):
        for i in range(len(self.day_arr)):
            if date == self.day_arr[i].date_of_data:  # same date is reached, now attempt to delete
                try:
                    return self.day_arr[i].slot_arr.pop(date_index)
                except:
                    print('Thing to delete doesnt exist')
                return

        print('Thing to delete doesnt exist')
        return

    def add_slot_to_the_team(self, slot_data_to_insert, date):

        for i in range(len(self.day_arr)):
            if date < self.day_arr[i].date_of_data:  # date is already passed, insert the day date object, after that add the slot
                temp_day = day_data(date, slot_data_to_insert)
                self.day_arr.insert(i, temp_day)
                return
            elif date == self.day_arr[i].date_of_data:  # same date is reached, the date object already exist, just add the slot
                self.day_arr[i].slot_arr.append(slot_data_to_insert)  # add the slot when the correct date is reached
                return
        # if it comes here, it means that the date is bigger than all the dates in the array
        temp_day = day_data(date, slot_data_to_insert)
        self.day_arr.append(temp_day)

    def get_slots_for_the_day(self, date):
        for temp in self.day_arr:
            if date == temp.date_of_data:  # same date is reached, the date object already exist, just add the slot
                return temp.slot_arr
        return []




class karer_data:

    def add_team(self,team_name):
        temp_team_data = team_data(self.unallocated_orders)
        temp_team_data.team_name = team_name #decide team name
        self.all_teams_data.append(temp_team_data)

    def remove_team(self, index):
        try:
            self.all_teams_data.pop(index)
        except:
            print("out of bounds")

    def add_an_unallocated_slot(self,region,address,person,tel,order_details,btu_9_no,btu_12_no,btu_18_no,btu_24_no):
        temp_day = slot_data()
        temp_day.date_of_order = datetime.datetime.today()
        temp_day.region = region
        temp_day.address = address
        temp_day.person = person
        temp_day.tel = tel
        temp_day.order_details = order_details
        temp_day.commissioned = False
        temp_day.paid = False
        temp_day._9_kBtu_p_h_no = btu_9_no
        temp_day._12_kBtu_p_h_no = btu_12_no
        temp_day._18_kBtu_p_h_no = btu_18_no
        temp_day._24_kBtu_p_h_no = btu_24_no
        self.unallocated_orders.append(temp_day)



    def __init__(self):
        self.all_teams_data = []
        self.unallocated_orders = []

        self.regions = ["Lefkoşa", "Girne", "Batı", "Doğu"]


