# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:44:57 2019

@author: Jayanth
"""
#from sys import stdout
import sys
#To create inverted index
def pos_doc(tex,did):
    result = {}
    for doc_id,doc in zip(did,tex):
        for word in (set(doc.split())):
            result.setdefault(word,[]).append(doc_id)
    return result

#To get postings list
def get_query_postings(query,b):
    post={}
    q=query
    z=q.split()
    for i in z:
        r=(b.get(i))
        for j in r:
            post.setdefault(i,[]).append(j)
    return post

#To find out document 
def doc_freq(b):
    df={}
    for i in b:
        df[i]=len(b.get(i))
    return df

#To find max element for or
def max_no_list(li):
    large=0
    for i in range(len(li)):
        if(len(li[i])>large):
            large=len(li[i])
    return large

#To find max element for and
def max_no_dict(m):
    large=0
    for i in m:
        if(len(m.get(i))>large):
            large=len(m.get(i))
    return large

#Daat AND
def daat_and(post):
    new_doc=[]
    count_daat_and=0
    abc=0
    i=0
    max_val=max_no_dict(post)
    while (i<len(post)*max_val): 
        for z in post:
            if(len(post.get(z))==0):
                return(count_daat_and,new_doc)
        start=next(iter(post))
        start_val=post.get(start)[0]
        for j in post:
            if j==start:
                remove=post.get(j)[0]
                continue
            if(post.get(j)[0]<start_val):
                start_val=post.get(j)[0]
                count_daat_and+=1
                abc=1
                remove=post.get(j)[0]
            elif(post.get(j)[0]==start_val):
                count_daat_and+=1
            else:
                abc=1
                count_daat_and+=1
        for k in post:
            if(post.get(k)[0]==remove):
                post.get(k).pop(0)
        i+=1
        if(abc==0):
            new_doc.append(start_val)
        abc=0
    return(count_daat_and,new_doc)

#Daat OR
def daat_or(li):
    new_doc=[]
    temp_doc=[]
    count_daat_or=0
    length=len(li)
    abc=0
    i=0
    q=0
    max_val=max_no_list(li)
    while (i<length*max_val):
        q=0
        while q<len(li):
            if(len(li[q])==0):
                li.pop(q)
                q=0
            else:
                q+=1  
        if(len(li)==1):
            for k in range(len(li[0])):
                temp_doc.append(li[0][k])
            temp_doc.sort()
            new_doc.extend(temp_doc)
            return(count_daat_or,new_doc) 
        else:
            if(len(li)!=0):
                start_val=li[0][0]
                for j in range(len(li)):
                    if j==0:
                        remov=li[j][0]
                        continue
                    if(li[j][0]<start_val):
                        start_val=li[j][0]
                        count_daat_or+=1
                        abc=1
                        remov=li[j][0]
                    elif(li[j][0]==start_val):
                        count_daat_or+=1
                    else:
                        abc=1
                        count_daat_or+=1
                new_doc.append(remov)
                for k in range(len(li)):
                    if(li[k][0]==remov):
                        li[k].pop(0)
                i+=1
                abc=0
            else:
                return(count_daat_or,new_doc)

#For each term count in each document
def tf(g,tex):
    outer={}
    inner={}
    ctr=0
    for i in g:
        for k in range(len(g.get(i))):
            f=g.get(i)[k]
            ctr=0
            for j in tex:
                if(int(j[0])==f):
                    for doc in j[1].split():
                        if(i==doc):
                            ctr+=1
                    break
            inner[f]=ctr
        outer[i]=inner
        inner={}
    return outer

#Total terms in a document
def tot_terms_in_doc(doc):
    tot_terms_in_doc={}
    ctr=0
    for i in range(len(doc)):
        for j in ((doc[i][1].split())):
            ctr+=1
        tot_terms_in_doc[doc[i][0]]=ctr
        ctr=0
    return tot_terms_in_doc



if __name__ == "__main__":

    input_file=sys.argv[1]
    output_file=sys.argv[2]
    input_query=sys.argv[3]
    text=[]
    with open(input_file) as file:
       for i in file:
           text.append(i.strip().split("\t"))
    
    temp1=[]
    for i in range(len(text)):
        temp1.append(text[i][1])
            
    temp2=[]
    for i in range(len(text)):
        temp2.append(int(text[i][0]))
        
        
    a={}
    for i in range(len(text)):
        a=pos_doc(temp1,temp2)
        
    c={}
    c=doc_freq(a)
    
    b={}
    b=tf(a,text)
            
    h={}
    h=tot_terms_in_doc(text)

    with open(input_query) as f:
        for i in f:
            d1=get_query_postings(i,a)
            d2=get_query_postings(i,a)
    
            dic=d1.copy()
            list1=[]    
            for value in d2.values():
                list1.append(value)
    
            y_and=daat_and(dic)
            y_or=daat_or(list1)
            
            print(y_and)
            print(y_or)
            #for tf-idf



            
  
    
 