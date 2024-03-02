from django.shortcuts import render,redirect
import pywhatkit as kit
import wikipedia

def homepage(request):  
    
    a=['36 Farmhouse', 'Hai Tujhe Salaam India', 'Badhaai Do', 'A Thursday', 'Love Hostel', 'Jhund', 'Toolsidas Junior', 'Radhe Shyam', 'The Kashmir Files', 'Sharmaji Namkeen', 'Attack Part 1', 'Kaun Pravin Tambe', 'Cobalt Blue', 'Dasvi', 'Hurdang', 'Jersey', 'Runway 34', 'Heropanti 2', 'Mere Desh Ki Dharti', 'Jayeshbhai Jordaar', 'Bhool Bhulaiyaa 2', 'Dhaakad', 'Anek', 'Dehati Disco', 'Haemolymph', 'Janhit Mein Jaari', 'Ardh', 'Nikamma', 'Sherdil', 'Forensic', 'Rocketry The Nambi Effect', 'Khuda Haafiz Chapter 2', 'Judaa Hoke Bhi', 'Shabaash Mithu', 'Good Luck Jerry', 'Odd Couple', 'Laal Singh Chaddha', 'Dobaaraa', 'Liger', 'Holy Cow', 'Cuttputlli', 'Brahmāstra Part One – Shiva', 'Jahaan Chaar Yaar', 'Jogi', 'Matto Ki Saikil', 'Saroj Ka Rishta', 'Siya', 'Atithi Bhooto Bhava', 'Babli Bouncer', 'Chup: Revenge of the Artist', 'Dhokha: Round D Corner', 'Ishq Pashmina', 'Plan A Plan B', 'Vikram Vedha']
    j=0
    ios=[] 
    ides=[]
    for i in a:

        loc="static/pics/"+i+".jpg"
        ios.append([i,loc])
        j+=1
        if j==8:   # splits the data into sets of 8
            ides.append(ios)
            j=0
            ios=[]
    return render(request,"hp.html",{"ids":ides})

def searchpage(request):
    a=['36 Farmhouse', 'Hai Tujhe Salaam India', 'Badhaai Do', 'A Thursday', 'Love Hostel', 'Jhund', 'Toolsidas Junior', 'Radhe Shyam', 'The Kashmir Files', 'Sharmaji Namkeen', 'Attack Part 1', 'Kaun Pravin Tambe', 'Cobalt Blue', 'Dasvi', 'Hurdang', 'Jersey', 'Runway 34', 'Heropanti 2', 'Mere Desh Ki Dharti', 'Jayeshbhai Jordaar', 'Bhool Bhulaiyaa 2', 'Dhaakad', 'Anek', 'Dehati Disco', 'Haemolymph', 'Janhit Mein Jaari', 'Ardh', 'Nikamma', 'Sherdil', 'Forensic', 'Rocketry The Nambi Effect', 'Khuda Haafiz Chapter 2', 'Judaa Hoke Bhi', 'Shabaash Mithu', 'Good Luck Jerry', 'Odd Couple', 'Laal Singh Chaddha', 'Dobaaraa', 'Liger', 'Holy Cow', 'Cuttputlli', 'Brahmāstra Part One – Shiva', 'Jahaan Chaar Yaar', 'Jogi', 'Matto Ki Saikil', 'Saroj Ka Rishta', 'Siya', 'Atithi Bhooto Bhava', 'Babli Bouncer', 'Chup: Revenge of the Artist', 'Dhokha: Round D Corner', 'Ishq Pashmina', 'Plan A Plan B', 'Vikram Vedha']
    b=[]
    if request.GET.get('mov'):
        key=request.GET.get('mov')
        for i in a:
            if i.lower().find(key.lower())>=0 :
                loc="/static/pics/"+i+".jpg"
                b.append([i,loc])
    print(b)
    return render (request,"search.html",{"ids":b})

def infopage(request,name):
    loc="/static/pics/"+name+".jpg"
    query=name+" movie story"
    data=wikipedia.summary(query,3)
    print(data)
    return render(request,"info.html",{"name":name,"loc":loc,"data":data})

def play_yt(request,name):
    query=name+" movie trailer"
    kit.playonyt(query)
    return redirect("/")