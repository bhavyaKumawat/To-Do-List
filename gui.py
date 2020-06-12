import tkinter
import DatePicker
import ToDoList 

class GUI:
    def __init__(self , conn):
        self.parent = tkinter.Tk()
        self.conn = conn
        tkinter.Button(self.parent, text ="Add Activity", command = self.activity_window).grid(row = 0, column = 0)
        self.load_pending_activities()
        self.parent.mainloop()
        
    def add_activity(self , activity , startDate , dueDate , frame):
        ToDoList.add_activity(self.conn , activity.get() , startDate.get(), dueDate.get())
        frame.destroy()
        self.load_pending_activities()
    
    def activity_window(self):
        frame = tkinter.Toplevel()
        frame.geometry("300x300")
        
        tkinter.Label( frame, text="Activity" ).pack()
        activity = tkinter.StringVar()
        tkinter.Entry(frame , textvariable = activity).pack()
        

        top1 = tkinter.Frame(frame, pady =15, padx=15)
        top1.pack()
        tkinter.Label( top1, text="Start Date" ).pack()
        startDate = tkinter.StringVar()
        DatePicker.Datepicker(top1 , datevar = startDate).pack(anchor="w")
        
        
        top2 = tkinter.Frame(frame, pady =15, padx=15)
        top2.pack()
        tkinter.Label( top2, text="Due Date" ).pack()
        dueDate = tkinter.StringVar()
        DatePicker.Datepicker(top2 , datevar = dueDate).pack(anchor="w")
        
        
        tkinter.Button(frame, text ="OK", command = lambda: self.add_activity(  activity, startDate , dueDate , frame )).pack()
        tkinter.Button(frame, text ="Cancel", command = frame.destroy).pack()
    
    def show_activity(self ,Button, index , id , activity , start_date , due_date , created_at):
        frame = self.parent
        
        if Button:
            tkinter.Button(frame, text ="X", command = lambda: self.delete_activity(id) ).grid(row = index, column = 0 , padx= 10)
        tkinter.Label( frame, text=id ).grid(row = index, column = 1 , padx= 10)
        tkinter.Label( frame, text=activity ).grid(row = index, column = 2 , padx= 10)
        tkinter.Label( frame, text=start_date).grid(row = index, column = 3 , padx= 10)
        tkinter.Label( frame, text= due_date  ).grid(row = index, column = 4 , padx= 10)
        tkinter.Label( frame, text= created_at ).grid(row = index, column = 5 , padx= 10)
        

    def load_pending_activities(self):
        rows = ToDoList.pending_activities(self.conn)
        self.show_activity( False, 1,  "Id" , "Activity" , "Start Date" , "Due Date" , "Created at")
        for index , row in enumerate(rows):
            self.show_activity( True, index+2  , *row)


    def delete_activity(self , id):
        ToDoList.delete_activity(self.conn , id )
        
    
        




