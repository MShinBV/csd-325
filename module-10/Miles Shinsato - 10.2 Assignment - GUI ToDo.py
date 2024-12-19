# Miles Shinsato 12/13/2024 CSD325-A339 10.2 Assignment GUI To Do

# Import the Tkinter Library for GUI
import tkinter as tk
# Import message box for pop-up dialog
import tkinter.messagebox as msg

# Define Todo Class to inherit from tk.TK
class Todo(tk.Tk):

    # Initialize the parent class
    def __init__(self, tasks=None):
        super().__init__()

        # Initialize list to store tasks, use an empty list when no tasks are present
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Naming the window size and the title
        self.title("Shinsato-ToDo App")
        self.geometry("300x400")

        # Menu bar with Exit option setup to close the program
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.exit_program)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # Creating a canvas for the tasks with a vertical scrollbar
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Positioning where scrollbar should be
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Attaching the tasks frame to the canvas
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        # Text input box to add tasks
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instructions for users to know how to delete a task
        instructions = tk.Label(self, text="Right-click a task to delete it.", fg="blue", pady=5)
        instructions.pack(side=tk.TOP, fill=tk.X)

        # Initial task placeholder, also added function to delete with right click
        todol = tk.Label(self.tasks_frame, text="--- Add Items Here ---", bg="purple", fg="yellow", pady=10)
        todol.bind("<Button-3>", self.remove_task)
        self.tasks.append(todol)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Event bindings

        # Pressing 'Enter' will add a new task
        self.bind("<Return>", self.add_task)

        # Adjust scrollbar if window is resized
        self.bind("<Configure>", self.on_frame_configure)

        # Adjust the task width to the canvas size
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Adding event to scroll wheel on mouse wheel
        self.tasks_canvas.bind_all("<MouseWheel>", self.mouse_scroll)

        # Attaching event to scroll up
        self.bind_all("<Button-4>", self.mouse_scroll)

        # Attaching event to scroll down
        self.bind_all("<Button-5>", self.mouse_scroll)

        # Going with Purple and Yellow colour scheme to match Bellevue University Colors
        self.colour_schemes = [{"bg": "purple", "fg": "yellow"}, {"bg": "yellow", "fg": "purple"}]

    # Defining function add_task
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        # Check that input is not empty
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            # Set color for the new task
            self.set_task_colour(len(self.tasks), new_task)

            # Binding remove_task to the right click button
            new_task.bind("<Button-3>", self.remove_task)

            # Pack the new task into the tasks frame
            new_task.pack(side=tk.TOP, fill=tk.X)

            # Append task to the task list
            self.tasks.append(new_task)

        # Clear text input box after adding a task
        self.task_create.delete(1.0, tk.END)

    # Defining function remove_task
    def remove_task(self, event):

        # Get the clicked task
        task = event.widget

        # Ask for confirmation on deleting a task
        if msg.askyesno("Really, Delete?", "Delete " + task.cget("text") + "?"):

            # Remove task from the list
            self.tasks.remove(event.widget)

            # Delete the task widget
            event.widget.destroy()

            # Update the colour scheme
            self.recolour_tasks()

    # Define recolour_tasks function to update colors after task list changes
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    # Set the background and foreground color of tasks based on alternating
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"], fg=my_scheme_choice["fg"])

    # Adjust the scroll region to include the area to include all tasks
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    # Adjust the width of task frame to match canvas width
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    # Define the mouse_scroll function
    def mouse_scroll(self, event):
        # Check for platform and handle scroll accordingly
        if event.delta:  # For Windows and macOS (event.delta exists)
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:  # For Linux systems using Button-4 and Button-5
            if event.num == 4:  # Scroll up
                self.tasks_canvas.yview_scroll(-1, "units")
            elif event.num == 5:  # Scroll down
                self.tasks_canvas.yview_scroll(1, "units")

    # Define function exit_program to exit when clicked
    def exit_program(self):
        self.destroy()

# Call back to main
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
