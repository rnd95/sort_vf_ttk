#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#

import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import tkinter.messagebox as messagebox
import shutil
import zipfile
import ui



_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = ui.SortVF_UI(_top1)
    root.mainloop()


class SortVF:
    def __init__(self, district_folders):
        self.district_folders = district_folders
    def Method_Bank(self, SheetNum): #Bank sort VF
        Error_Detect = False
        Message_FinishInfo = "Виконано"
        if not SheetNum:
            Message_FinishInfo = "Тип не вказано, сортування буде скасовано."
            print(Message_FinishInfo)
        else:
            print("Тип вiдомостi:", SheetNum)
        
        for district_folder in self.district_folders:
            zip_file = None
            temp_folder = None
            try:
                zip_files = [f for f in os.listdir(district_folder) if
                             os.path.isfile(os.path.join(district_folder, f)) and f.endswith('.zip')]
                if not zip_files:
                    print("Zip files is not detected in", district_folder)

                for zip_file in zip_files:
                    temp_folder = os.path.join(district_folder, 'temp')
                    os.makedirs(temp_folder, exist_ok=True)
                    with zipfile.ZipFile(os.path.join(district_folder, zip_file), 'r') as zip_ref:
                        zip_ref.extractall(temp_folder)
                        print("Unpacked zip: ", zip_file)


                    SheetType = "T"+str(SheetNum)+"_P01_VF"
                    bank_folder = os.path.join(temp_folder, 'verifikacia', 'DO', SheetType)
                    if not os.path.exists(bank_folder):
                        continue

                    bank_folders = [f for f in os.listdir(bank_folder) if os.path.isdir(os.path.join(bank_folder, f))]

                    for bank_code in bank_folders:
                        output_bank_folder = os.path.join("Sorted_VF_Bank", district_folder, SheetType, bank_code)
                        if not os.path.exists(output_bank_folder):
                            os.makedirs(output_bank_folder)
                        for item in os.listdir(os.path.join(bank_folder, bank_code)):
                            s = os.path.join(bank_folder, bank_code, item)
                            d = os.path.join(output_bank_folder, item)
                            if os.path.isdir(s):
                                shutil.copytree(s, d)
                            else:
                                shutil.copy2(s, d)

            except Exception as e:
                Error_Detect = True
                error_message = "Сталася помилка пiд час сортування банкiв:\n\n" + str(e) + "\n\nНазва файла: " +zip_file
                messagebox.showerror("Сортування банкiв", error_message)
                print(e)

            finally:
                if temp_folder and os.path.exists(temp_folder):
                    shutil.rmtree(temp_folder)
        if not Error_Detect:
            messagebox.showinfo("Сортування банкiв", Message_FinishInfo) 

    def Method_Post(self, SheetNum, MonthNum): #Post sort VF
        global Message_FinishInfo
        if not MonthNum:
            Message_FinishInfo = "Мiсяць не вказано, сортування буде скасовано."
            print(Message_FinishInfo)
        elif not SheetNum:
            Message_FinishInfo = "Тип вiдомостi не вказано, сортування буде скасовано."
            print(Message_FinishInfo)
        else:
            print("Мiсяць:", MonthNum)
            print("Тип вiдомостi:", SheetNum)

        Error_Detect = False
        for district_folder in self.district_folders:
            zip_file = None
            temp_folder = None
            try:
                zip_files = [f for f in os.listdir(district_folder) if
                             os.path.isfile(os.path.join(district_folder, f)) and f.endswith('.zip')]
                if not zip_files:
                    print("Zip files is not detected in", district_folder)
                for zip_file in zip_files:
                    temp_folder = os.path.join(district_folder, 'temp')
                    os.makedirs(temp_folder, exist_ok=True)
                    with zipfile.ZipFile(os.path.join(district_folder, zip_file), 'r') as zip_ref:
                        zip_ref.extractall(temp_folder)
                        print("Unpacked zip: ", zip_file)

                    SheetType = str(MonthNum) + "TP" + str(SheetNum)+ "P1_VF"
                
                    bank_folder = os.path.join(temp_folder, 'verifikacia', 'DO', SheetType)
                    if not os.path.exists(bank_folder):
                        continue

                    bank_folders = [f for f in os.listdir(bank_folder) if os.path.isdir(os.path.join(bank_folder, f))]

                    for bank_code in bank_folders:
                        output_bank_folder = os.path.join("Sorted_VF_Post", SheetType, bank_code)
                        if not os.path.exists(output_bank_folder):
                            os.makedirs(output_bank_folder)
                        for item in os.listdir(os.path.join(bank_folder, bank_code)):
                            s = os.path.join(bank_folder, bank_code, item)
                            d = os.path.join(output_bank_folder, item)
                            if os.path.isdir(s):
                                shutil.copytree(s, d)
                            else:
                                shutil.copy2(s, d)

            except Exception as e:
                Error_Detect = True
                error_message = "Сталася помилка під час сортування пошти:\n\n" + str(e) + "\n\nНазва файла: " +zip_file
                messagebox.showerror("Сортування пошти", error_message)
                print(e)
            finally:
                if temp_folder and os.path.exists(temp_folder):
                    shutil.rmtree(temp_folder)

        if not Error_Detect:
            messagebox.showinfo("Сортування пошти", Message_FinishInfo)

# Создаем объект класса с заданными районами
district_folders = [folder for folder in os.listdir('.') if os.path.isdir(folder)]
SortVF_dis = SortVF(district_folders)

Message_FinishInfo = "Виконано"

# Вызываем метод sort_files() из объекта
if __name__ == '__main__':
    ui.start_up()