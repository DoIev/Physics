import tkinter

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700


class MainApplication(tkinter.Frame):
    """this class represents our main TTK window/Frame"""
    def __init__(self, window):
        super().__init__()
        self.main_window = window
        self.main_window.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.main_window.resizable(width=False, height=False)
        self.main_window.title(string="gravity simulator")
        self.config(bg="gray10")

        # defining dark mode button and placing it
        self.button_dark_mode = tkinter.Button(self, height=2, width=20, text="Light Mode", bg="#F0F0F0", fg="gray10", command=self.dark_mode)
        self.button_dark_mode.place(x=0, y=0)

        # graph panel
        self.graph_panel = tkinter.Frame(self, height= 250, width= 250, bg="firebrick3")
        self.graph_panel_text = tkinter.Label(text="graph", font=("bold", 20), fg="#F0F0F0", bg="firebrick3")
        self.graph_panel.place(x=900, y=50)
        self.graph_panel_text.place(x=WINDOW_WIDTH - self.graph_panel["width"] - 50 , y=70)

        # console panel
        self.console_panel = tkinter.Frame(self, height=250, width=250, bg="black")
        self.console_panel_text = tkinter.Label(text="console", font=("bold", 20), fg="#F0F0F0", bg="black")
        self.console_listbox = tkinter.Listbox(self, width=37, height=11, bg="black", fg="red", borderwidth=0, highlightthickness=0)
        self.console_panel.place(x=600, y=50)
        self.console_listbox.insert(0, "-> Program opened")
        self.console_panel_text.place(x=WINDOW_WIDTH - self.console_panel["width"] - 350, y=70)
        self.console_listbox.place(x=610, y=115)

        # entries panel
        self.entries_panel = tkinter.Frame(self, height=250, width=250, bg="firebrick4")
        self.entries_panel_text = tkinter.Label(text="entries", font=("bold", 20), fg="#F0F0F0", bg="firebrick4")
        self.entries_panel.place(x=600, y=350)
        self.entries_panel_text.place(x=WINDOW_WIDTH - self.entries_panel["width"] - 350, y=70+300)

        # defining experiment entries
        self.entry_ball_color = tkinter.Entry(self, width=35)
        self.entry_ball_color.place(x=WINDOW_WIDTH - self.entries_panel["width"] - 340, y=420)
        self.entry_ball_color.insert(0, "Ball Color (string)")

        self.entry_ball_radius = tkinter.Entry(self, width=35)
        self.entry_ball_radius.place(x=WINDOW_WIDTH-self.entries_panel["width"] - 340, y=450)
        self.entry_ball_radius.insert(0, "Ball's Radius (M)")

        self.entry_ball_mass = tkinter.Entry(self, width=35)
        self.entry_ball_mass.place(x=WINDOW_WIDTH - self.entries_panel["width"] - 340, y=480)
        self.entry_ball_mass.insert(0, "Ball's Mass (KG)")

        self.entry_planet_mass = tkinter.Entry(self, width=35)
        self.entry_planet_mass.place(x=WINDOW_WIDTH - self.entries_panel["width"] - 340, y=570)
        self.entry_planet_mass.insert(0, "Planet Mass (KG)")

        self.entry_ball_electric_charge = tkinter.Entry(self, width=35)
        self.entry_ball_electric_charge.place(x=WINDOW_WIDTH - self.entries_panel["width"] - 340, y=510)
        self.entry_ball_electric_charge.insert(0, "Ball's Electric Charge (C)")

        self.entry_electric_field = tkinter.Entry(self, width=35)
        self.entry_electric_field.place(x=WINDOW_WIDTH - self.entries_panel["width"] - 340, y=540)
        self.entry_electric_field.insert(0, "Electric Field (N/C)")

    def dark_mode(self):
        """this method will switch the color of the background of the frame (white or black)"""

        # if the user pressed the button and the current background is dark gray then
        # switch it to black, and change the button's text and color
        # if not, do the opposite action

        if self.cget('bg') == "gray10":
            self.config(bg="#F0F0F0")
            self.button_dark_mode.config(bg="gray10", text="Dark Mode", fg="#F0F0F0")

        else:
            self.config(bg="gray10")
            self.button_dark_mode.config(bg="#F0F0F0", text="Light Mode", fg="gray10")


class Ball(object):
    """this class represents the ball in the simulator."""

    # Constructor
    def __init__(self, _altitude: float = 100, _color: str = "green", _radius: float = 1, _mass: float = 1,
                 _electric_charge: float = 0, _planet_mass: float = 6*10**24, _electric_field: float = 0):
        self.velocity = 0
        self.on_ground = False
        self.altitude = _altitude
        self.color = _color
        self.radius = _radius
        self.mass = _mass
        self.electric_charge = _electric_charge

        self.planet_mass = _planet_mass
        self.electric_field = _electric_field

    def get_current_acceleration(self):
        # according to newton's second low - sigma(F)=ma
        if self.electric_charge == 0 and self.electric_field == 0:
            # F = ma, so mg=ma -> a=g
            # g = G*M/r^2

            self.velocity += ((6.67*10**-11) * self.planet_mass) / ((WINDOW_HEIGHT - self.altitude)**2)
            # to be continued


def main():
    root = tkinter.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
