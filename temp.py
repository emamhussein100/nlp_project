from nltk.tokenize import word_tokenize
from tkinter import *

root=Tk()

root.geometry("800x600")



name_var=StringVar()


def submit():
    

    q1 = 'ما هى مؤلفات'
    q2 = 'من هو مؤلف'
    q3 = 'ما هو ملخص'
    q4 = 'ما هى فئه'
    q5 = 'ما هو رابط تحميل'
    q6 = 'ما هى ملخصات'
    q7 = 'ما هى لغه كتاب شوقي PDF'
    q8 = "كم عدد صفحات"
    q9 = 'ما هو حجم تحميل'
    q10 = 'ما هى دار نشر'
    q11 = 'دار النشر المسؤله عن'
    q12 = 'من هو مؤلف و ملخصه و فئته'
    
    
    q_list = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
    
    #query = 'ما هى مؤلفات الله عز وجل'
    query = name_var.get()
    
    cosine_list = []
    
    
    for q in q_list:
        X_list = word_tokenize(q) 
        Y_list = word_tokenize(query)
        
        X_set = {w for w in X_list} 
        Y_set = {w for w in Y_list}
        
        l1 =[];l2 =[]
    
        rvector = X_set.union(Y_set) 
        for w in rvector:
            if w in X_set: l1.append(1) # create a vector
            else: l1.append(0)
            if w in Y_set: l2.append(1)
            else: l2.append(0)
        c = 0
      
        # cosine formula 
        for i in range(len(rvector)):
            c+= l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)
        cosine_list.append(cosine)
        
    print(cosine_list)
    
    max_value = max(cosine_list)
    max_index = cosine_list.index(max_value)
    
    print(max_index)
    
    correct_q = q_list[max_index]
    
    print(correct_q)
    
    X_list = word_tokenize(correct_q) 
    Y_list = word_tokenize(query)
    
    print(X_list)
    print(Y_list)
    
    for word in X_list:
        query = query.replace(word, '')
        
    print(query)
    
    print(query)
    
    query = query.lstrip()
    
    print(query)
    
    import pandas as pd 
    
    df = pd.read_csv('books_info.csv')
    
    lists = []
    if max_index == 0:
        df = df.loc[df['Author'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][1])
    elif max_index == 1:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][0])
    elif max_index == 2:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][2])
    elif max_index == 3:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][7])
    elif max_index == 4:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][8])
    elif max_index == 5:
        df = df.loc[df['Author'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][2])
    elif max_index == 6:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][3])
    elif max_index == 7:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
           
            lists.append(df.iloc[i][4])
    elif max_index == 8:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
           
            lists.append(df.iloc[i][6])
    elif max_index == 9:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][5])
    elif max_index == 10:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            
            lists.append(df.iloc[i][5])
    elif max_index == 11:
        df = df.loc[df['title'] == query]
        count_row = df.shape[0]
        count_row
        for i in range(count_row):
            print("المؤلف : "+df.iloc[i][0])
            print("الملخص : "+df.iloc[i][2])
            print("الفئه : "+df.iloc[i][7])
    
    
    
    
    lists_to_String = "\n".join(lists)
    
    print(lists_to_String)
    Q_label2 = Label(root,  text = lists_to_String).place(x = 250,y = 200)
                                             
    
	
Q_label = Label(root,  text = "Put Here...").place(x = 250,
                                              y = 70) 

name_entry = Entry(root,textvariable = name_var,justify='right', font=('calibre',10,'normal')).place(x = 200,y = 100)

sub_btn=Button(root,text = 'Submit', command = submit).place(x = 250,y = 150)


def Reset():
    name_var.set("")
    
    sub_btn=Button(root,text = 'Submit', command = submit).place(x = 250,y = 150)

def Exit():
    root.destroy()

sub_btn1=Button(root,text = 'Reset', command = Reset).place(x = 100,y = 150)





root.mainloop()
