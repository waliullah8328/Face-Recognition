from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =========================Variable ===============================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var__std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



        img = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student.jpg")
        img =img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1 = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student1.jpg")
        img1 =img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl =Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2 = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student2.jpg")
        img2 =img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        img3 = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Studen.png")
        img3 =img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg ="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student_hand_rising.jpg")
        img_left =img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl =Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #Current course
        Current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=10,y=135,width=720,height=115)
        dep_label = Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=17)
        dep_combo["values"]= ("Select Department","Computer","IT","Civil","Mechacanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
       
        course_label = Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=17)
        course_combo["values"]= ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
       
        year_label = Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=17)
        year_combo["values"]= ("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semister
       
        Semister_label = Label(Current_course_frame,text="Semister",font=("times new roman",12,"bold"),bg="white")
        Semister_label.grid(row=1,column=2,padx=10,sticky=W)

        Semister_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only",width=17)
        Semister_combo["values"]= ("Select Semister","Semister-1","Semister-2")
        Semister_combo.current(0)
        Semister_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

         #Class Student Information 
        Class_student_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("times new roman",12,"bold"))
        Class_student_course_frame.place(x=10,y=250,width=720,height=300)

        #Student ID

        student_Id_label = Label(Class_student_course_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_Id_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_Id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Student Name

        student_name_label = Label(Class_student_course_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var__std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

          
        #Student Division

        student_div_label = Label(Class_student_course_frame,text="Student Division",font=("times new roman",12,"bold"),bg="white")
        student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        student_div_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         
        

           
      

           
        #Student Roll No

        roll_no_label = Label(Class_student_course_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Student Gender

        gender_label = Label(Class_student_course_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

           
        #Student DOB

        dob_label = Label(Class_student_course_frame,text="Date of Birth",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #Student Email

        email_label = Label(Class_student_course_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

           
        #StudentPone no

        phone_no_label = Label(Class_student_course_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #Student Address

        address_label = Label(Class_student_course_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

           
        #Student Teacher Name

        Teacher_name_label = Label(Class_student_course_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        Teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_name_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        Teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Button
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(Class_student_course_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(Class_student_course_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button Frame
        btn_frame = Frame(Class_student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn =Button(btn_frame,text= "Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn =Button(btn_frame,text= "Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn =Button(btn_frame,text= "Delete",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn =Button(btn_frame,text= "Reset",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(Class_student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn =Button(btn_frame1,text= "Take a photo sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn =Button(btn_frame1,text= "Update photo sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)




        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)

        img_right = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student3.jpg")
        img_right =img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # +===============Search System==============
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=10,y=135,width=710,height=70)

        search_label = Label(Search_frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]= ("Select","Roll Number","Phone Number","")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn =Button(Search_frame,text= "Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn =Button(Search_frame,text= "Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # ====================table frame==================
        table_frame =Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=710,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","photos"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)  
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone no")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photos",text="Photos")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photos",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
    # ==================Function Declaration ====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var__std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fileds are required",parent = self.root)
        else:
            try:
                conn =mysql.connector.connect(host="localhost",user="root",password = "",database= "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("inser into student values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var__std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                    



                                                                                                                       ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Sudent Details has been added Successfully",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent = self.root)


    # =================generate photo sample=============
    #def generate_dataset(self):
        #pass
        
        



        




if __name__ == "__main__":
    root = Tk()
    obj =Student(root)
    root.mainloop()