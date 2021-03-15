from tkinter import *

# splash screen 4 logo
splash_root = Tk()
splash_root.title("Splash Screen!")
splash_root.geometry("280x120")
splash_root.overrideredirect(True)
logo_splash = PhotoImage(file="EmotionDetectionLogo.png")
splash_lbl = Label(splash_root, image=logo_splash)
splash_lbl.pack()


# Initialize main window
def main_window():
    splash_root.destroy()
    root = Tk()
# window name
    root.title("Emotion Detection")

# window size
    root.geometry("480x320")

# Create Frames to organize layouts
# Top Frame
    top_frame = Frame(root)
    top_frame.pack()
    top_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# add label txt
    childID_lbl = Label(top_frame, text="Child ID: ", justify=CENTER, font=("Calibre", 14, "italic", UNDERLINE), fg="#87AFC7")
    childID_lbl.pack(side=TOP, padx=10)

# add textbox
    childID_entry = Entry(top_frame, width=20)
    childID_entry.pack(pady=10, side=TOP)



# onclick access -> open new window
    def access_win():
         root1 = Tk()
         root1.title("Home")
         root1.geometry("480x320")

    # Top Frame to centralized buttons
         top_frame2 = Frame(root1)
         top_frame2.pack(side=TOP)
         top_frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Left Frame for arrow
         left_frame = Frame(root1)
         left_frame.pack(side=LEFT)
         left_frame.place(relx=0.05, rely=0.08, anchor=N)


         def stop_win():
             root3 = Tk()
             root3.title("Detected Emotions")
             root3.geometry("480x320")
             detected_emotion_lbl = Label(root3, text="The Detected Emotion is: ", font=("Calibra", 14, "italic", UNDERLINE), justify=CENTER, fg="#87AFC7")
             detected_emotion_lbl.pack(side=LEFT, padx=80)

     # Start Button
         start_btn = Button(top_frame2, text="Start Recording", bg="#87AFC7", fg="white", borderwidth=2)
         start_btn.pack(side=LEFT, padx=10, pady=10)

     # Stop Button
         stop_btn = Button(top_frame2, text="Stop Recording", bg="#87AFC7", fg="white", borderwidth=2, command=stop_win)
         stop_btn.pack(side=LEFT, padx=10, pady=10)

        # end of stop window

    # end of access window


# onclick view -> open new window to view child emotions
    def view_win():
        root2 = Tk()
        root2.title("View")
        root2.geometry("480x320")


# View Button
    view_btn = Button(top_frame, text="  View   ", bg="#87AFC7", fg="white", borderwidth=2, command=view_win)
    view_btn.pack(side=LEFT, padx=10, pady=10)

# Access Button
    access_btn = Button(top_frame, text=" Access ", bg="#87AFC7", fg="white", borderwidth=2, command=access_win)
    access_btn.pack(side=RIGHT, padx=10, pady=10)
    # end of view window

# end of main window function

# splash screen timer
splash_root.after(1000, main_window)


mainloop()

