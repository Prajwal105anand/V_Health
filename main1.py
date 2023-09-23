import customtkinter 
import tkinter 


import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")
root.iconbitmap("D:/relay_code_project/medica_health_healthcare_sign_icon_143444.ico")
def login():    
    print("Test")



def close_main_window():
    root.destroy()  # Destroy the main window

#def close_sign_up():
    #root2.destory()

#Final page data -
def lead_to_final_page():
    #add login bypass only when correc password is entered

    #below final page UI
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()

            # configure window
            self.iconbitmap("D:/relay_code_project/medica_health_healthcare_sign_icon_143444.ico")
            self.title("V Health")
            self.geometry(f"{1100}x{580}")

            # configure grid layout (4x4)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure((2, 3), weight=0)
            self.grid_rowconfigure((0, 1, 2), weight=1)

            # create sidebar frame with widgets
            self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(4, weight=1)

            self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


            self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text=" Re-Login " ,command=self.sidebar_button_event)
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text=" Sign-out ", command=self.sidebar_button_event)
            self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
            self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text=" Reset " ,command=self.sidebar_button_event)
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
            


            self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
            self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))


            self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                        command=self.change_appearance_mode_event)
            self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
            self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
            self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
            self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=self.change_scaling_event)
            self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

            # create main entry and button
            # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
            # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

            # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
            # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

            # create textbox
            # self.textbox = customtkinter.CTkTextbox(self, width=250)
            # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            # create tabview
            self.tabview = customtkinter.CTkTabview(self, width=900)
            self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="W")
            self.tabview.add(" Profile ")
            self.tabview.add(" Doctor ")
            self.tabview.add(" Leave ")
            self.tabview.add(" Home Remedy ")
            self.tabview.tab(" Profile ").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
            self.tabview.tab(" Doctor ").grid_columnconfigure(0, weight=1)
            self.tabview.tab(" Leave ").grid_columnconfigure(0, weight=1)
            self.tabview.tab(" Home Remedy ").grid_columnconfigure(0, weight=1)

            self.regno_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Registration No.")
            self.regno_p.grid(row=0, column=0, padx=20, pady=(20, 10))

            self.namebox_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Name")
            self.namebox_p.grid(row=1, column=0, padx=20, pady=(20, 10))

            self.email_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Email")
            self.email_p.grid(row=2, column=0, padx=20, pady=(20, 10))

            self.hostel_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Hostel")
            self.hostel_p.grid(row=3, column=0, padx=20, pady=(20, 10))

            self.bloodgrp_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Blood Group")
            self.bloodgrp_p.grid(row=4, column=0, padx=20, pady=(20, 10))

            self.mess_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Mess Alloted")
            self.mess_p.grid(row=5, column=0, padx=20, pady=(20, 10))

            self.dob_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Date of Birth")
            self.dob_p.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.proct_id_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Proctor Details")
            self.proct_id_p.grid(row=1, column=1, padx=20, pady=(20, 10))

            self.phone_no_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Phone Number")
            self.phone_no_p.grid(row=2, column=1, padx=20, pady=(20, 10))

            self.phone_no_parent_p = customtkinter.CTkEntry(self.tabview.tab(" Profile "), placeholder_text="Parent's Phone Number")
            self.phone_no_parent_p.grid(row=3, column=1, padx=20, pady=(20, 10))


            #doctor choosing switches
            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab(" Doctor "), label_text="Select the doctor \n for booking appointment")
            self.scrollable_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure(0, weight=1)
            self.scrollable_frame_switches = []
            name=["haresh","jayesh","mrugesh","raj","simran","harsh","ayush","kunal","rahul","rohan","rishikesh","jayant","sameer","ishaan"]
            surname=["patel","singh","khurana","mandaliya","singh","chouhan","Singh","Kumar","Shah","Mehta","Joshi","Desai","Mishra","Verma"]
            doc_names=['Dr. haresh patel - 10:00 to 10:40', 'Dr. jayesh singh - 11:00 to 11:40', 'Dr. mrugesh khurana - 12:00 to 12:40', 'Dr. raj mandaliya - 13:00 to 13:40', 'Dr. simran singh - 14:00 to 14:40', 'Dr. harsh chouhan - 12:00 to 12:40', 'Dr. ayush Singh - 13:00 to 13:40', 'Dr. kunal Kumar - 11:00 to 11:40', 'Dr. rahul Shah - 14:00 to 14:40', 'Dr. rohan Mehta - 10:00 to 10:40', 'Dr. rishikesh Joshi - 14:00 to 14:40', 'Dr. jayant Desai - 13:00 to 13:40', 'Dr. sameer Mishra - 11:00 to 11:40', 'Dr. ishaan Verma - 10:00 to 10:40']
            # for j in range(14):
            #     doc_names.append("Dr. " + name[j]+ " " + surname[j])
            # print(doc_names)
            times=["10:00 to 10:40","11:00 to 11:40","12:00 to 12:40","13:00 to 13:40","14:00 to 14:40","15:00 to 15:40"]
            
            
            for i in range(14):
                switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f" {doc_names[i]}")
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                self.scrollable_frame_switches.append(switch)
            
            button = customtkinter.CTkButton (master=self.scrollable_frame, text="Confirm slot booking", command=lead_to_final_page)
            button.grid(row=6, column=0, padx=20, pady=(20, 10))

            #leave tab
            

            self.reason_p = customtkinter.CTkEntry(self.tabview.tab(" Leave "), placeholder_text="Reason of leave")
            self.reason_p.grid(row=0, column=0, padx=20, pady=(20, 10))

            self.startdate_p = customtkinter.CTkEntry(self.tabview.tab(" Leave "), placeholder_text=" Start date ")
            self.startdate_p.grid(row=1, column=0, padx=20, pady=(20, 10))

            self.enddate_p = customtkinter.CTkEntry(self.tabview.tab(" Leave "), placeholder_text=" End date ")
            self.enddate_p.grid(row=2, column=0, padx=20, pady=(20, 10))

            # self.slider_progressbar_frame = customtkinter.CTkFrame(self.tabview.tab(" Leave "), fg_color="transparent")
            # self.slider_progressbar_frame.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsew")
            self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab(" Leave "), text="Choose Leave duration")
            self.label_tab_2.grid(row=3, column=0, padx=20, pady=20)
            
            self.slider_1 = customtkinter.CTkSlider(self.tabview.tab(" Leave "), from_=0, to=1, number_of_steps=7)
            self.slider_1.grid(row=4, column=0, padx=(20, 10), pady=(20, 10), sticky="ew")

            self.checkbox_location = customtkinter.CTkCheckBox(self.tabview.tab(" Leave "),text=" Take location Data")
            self.checkbox_location.grid(row=5, column=0, padx=20, pady=(20, 10))

            #home remedy
            self.textbox = customtkinter.CTkTextbox(self.tabview.tab(" Home Remedy "), width=250)
            self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.textbox.insert("0.0", "CTkTextbox\n\n" + "Rest, hydration, over-the-counter cold remedies, pain relievers (e.g., acetaminophen, ibuprofen) \n" + "Rest, antiviral medications (prescribed by a doctor), fluids\n" + "Pain relievers (e.g., acetaminophen, ibuprofen), rest, hydration\n" + "Dietary changes, antacids, over-the-counter medications\n" + "Rest, hydration, fever-reducing medications (e.g., acetaminophen)\n" + "Antihistamines, avoiding allergens, allergy shots (for severe cases)\n" + "Rest, hydration, cough medicines (if recommended by a doctor)\n" + "Antibiotics (if bacterial), decongestants, saline nasal rinses\n" + "Topical creams, cleansers, oral medications (prescribed by a dermatologist)\n" + "Sleep hygiene practices, relaxation techniques, medication (as prescribed)\n" + "Moisturizers, topical corticosteroids, avoiding triggers\n" + "Pain relievers, migraine-specific medications (prescribed by a doctor), rest\n" + "Dietary changes (avoiding spicy or acidic foods), antacids, medications (prescribed by a doctor)\n" + "Lifestyle changes (diet, exercise), cholesterol-lowering medications (prescribed by a doctor)\n")
            # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Profile"), dynamic_resizing=False,
            #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
            # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
            # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
            #                                             values=["Value 1", "Value 2", "Value Long....."])
            # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
            # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
            #                                                 command=self.open_input_dialog_event)
            # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
            # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
            # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

            # create radiobutton frame
            # self.radiobutton_frame = customtkinter.CTkFrame(self)
            # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
            # self.radio_var = tkinter.IntVar(value=0)
            # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
            # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
            # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
            # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
            # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
            # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
            # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

            # create slider and progressbar frame
            # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
            # self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
            # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
            # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
            # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
            # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
            # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
            # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            # self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
            # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
            # self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
            # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

            # create scrollable frame
            # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
            # self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
            # self.scrollable_frame.grid_columnconfigure(0, weight=1)
            # self.scrollable_frame_switches = []
            # for i in range(100):
            #     switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            #     self.scrollable_frame_switches.append(switch)

            # create checkbox and switch frame
            # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
            # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
            # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
            # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
            # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
            # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
            # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
            # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

            # set default values
            # self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
            # self.checkbox_3.configure(state="disabled")
            # self.checkbox_1.select()
            # self.scrollable_frame_switches[0].select()
            # self.scrollable_frame_switches[4].select()
            # self.radio_button_3.configure(state="disabled")
            # self.appearance_mode_optionemenu.set("Dark")
            # self.scaling_optionemenu.set("100%")
            # self.optionmenu_1.set("CTkOptionmenu")
            # self.combobox_1.set("CTkComboBox")
            # self.slider_1.configure(command=self.progressbar_2.set)
            # self.slider_2.configure(command=self.progressbar_3.set)
            # self.progressbar_1.configure(mode="indeterminnate")
            # self.progressbar_1.start()
            # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
            # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
            # self.seg_button_1.set("Value 2")

        def open_input_dialog_event(self):
            dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
            print("CTkInputDialog:", dialog.get_input())

        def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)

        def change_scaling_event(self, new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)

        def sidebar_button_event(self):
            print("sidebar_button click")
    if __name__ == "__main__":
        app = App()
        app.mainloop()

# Function to open a new window
def open_new_window():
    root2=customtkinter.CTk()
    new_window = customtkinter.CTkToplevel(root2)
      # Create a new window
    new_window.title("New Window")
    root2.iconbitmap("D:/relay_code_project/medica_health_healthcare_sign_icon_143444.ico")
    #sign up page data-

    frame2 = customtkinter.CTkFrame (master=new_window)
    frame2.pack (pady=20, padx=60, fill="both", expand=True)

    label1 = customtkinter.CTkLabel(master=frame2, text="Sign Up System")
    label1.pack(pady=12, padx=10)

    regno_p_reg = customtkinter.CTkEntry(master=frame2, placeholder_text="Registration No.")
    regno_p_reg.pack(pady=12, padx=10)

    namebox_p_reg = customtkinter.CTkEntry(master=frame2, placeholder_text="Name")
    namebox_p_reg.pack(pady=12, padx=10)

    email_p_reg = customtkinter.CTkEntry(master=frame2, placeholder_text="Email")
    email_p_reg.pack(pady=12, padx=10)

    hostel_p_reg = customtkinter.CTkEntry(master=frame2, placeholder_text="hostel")
    hostel_p_reg.pack(pady=12, padx=10)

    bloodgrp_p_reg = customtkinter.CTkEntry(master=frame2, placeholder_text="Blood Group")
    bloodgrp_p_reg.pack(pady=12, padx=10)

    password_reg = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter New Password", show="*")
    password_reg.pack(pady=12, padx=10)

    button2 = customtkinter.CTkButton (master=frame2, text="Sign Up", command=revert_to_login)
    button2.pack(pady=12, padx=10)

    namebox_p_reg_data=namebox_p_reg.get()
    email_p_reg_data=email_p_reg.get()
    hostel_p_reg_data=hostel_p_reg.get()
    bloodgrp_p_reg_data=bloodgrp_p_reg.get()
    password_reg_data=password_reg.get()

    root.destroy()

def revert_to_login():
    #add database adition below

    #reverting to login page
    root = customtkinter.CTk()
    root.geometry("500x350")
    root.iconbitmap("D:/relay_code_project/medica_health_healthcare_sign_icon_143444.ico")
    new_window2= customtkinter.CTkToplevel(root)
    frame1 = customtkinter.CTkFrame (master=new_window2)
    frame1.pack (pady=20, padx=60, fill="both", expand=True)



    label = customtkinter.CTkLabel(master=frame1, text="Login System")
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry (master=frame1, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton (master=frame1, text="Login", command=lead_to_final_page)
    button.pack(pady=12, padx=10)

    #close_sign_up()

frame1 = customtkinter.CTkFrame (master=root)
frame1.pack (pady=20, padx=60, fill="both", expand=True)



label = customtkinter.CTkLabel(master=frame1, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry (master=frame1, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton (master=frame1, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox (master=frame1, text="Remember Me")
checkbox.pack(pady=12, padx=10)

button_for_singup= customtkinter.CTkButton (master=frame1, text="Sign Up",command=open_new_window)
button_for_singup.pack(pady=12, padx=10)





root.mainloop()
root2.mainloop()


