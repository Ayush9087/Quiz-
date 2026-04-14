# SSC CGL Maths Quiz in Hinglish (Corrected Answer Keys)

quiz = {
    "Ek aadmi ek vastu ₹720 mein kharidta hai aur use 10% loss par bechta hai. Selling Price kya hoga?":
        [["A. ₹648", "B. ₹650", "C. ₹660", "D. ₹670"], "A"],  # Correct: 648

    "Ek parivaar mein 5 members ki average age 21 years hai. Agar sabse chhote member ki age 5 years hai, toh baaki 4 members ki average age kya hogi?":
        [["A. 25", "B. 26", "C. 27", "D. 28"], "A"],  # Correct: 25

    "Ek train 150 m lambi hai aur ek 250 m lamba bridge 40 seconds mein cross karti hai. Train ki speed km/hr mein kya hogi?":
        [["A. 36", "B. 40", "C. 45", "D. 54"], "A"],  # Correct: 36

    "₹5000 par 10% per annum ke hisaab se 2 saal ka Simple Interest aur Compound Interest ka difference kitna hoga?":
        [["A. ₹50", "B. ₹100", "C. ₹200", "D. ₹250"], "A"],  # Correct: 50

    "A aur B ki age ka ratio 3:5 hai aur unki age ka difference 6 years hai. Toh A ki age kya hogi?":
        [["A. 9", "B. 12", "C. 15", "D. 18"], "C"],  # Correct: 15

    "Ek shopkeeper 20% discount deta hai aur phir bhi 25% profit banata hai. Agar marked price ₹1000 hai, toh cost price kya hogi?":
        [["A. ₹600", "B. ₹625", "C. ₹650", "D. ₹700"], "B"],  # Correct: 625

    "Pehle 20 odd numbers ka sum kya hoga?":
        [["A. 200", "B. 210", "C. 400", "D. 420"], "C"],  # Correct: 400

    "A 12 din mein kaam kar sakta hai, B 15 din mein. Agar dono 5 din saath kaam karein, toh kitna kaam bacha hoga?":
        [["A. 1/4", "B. 1/3", "C. 1/5", "D. 1/6"], "B"],  # Correct: 1/3

    "7 consecutive numbers ka average 20 hai. Toh sabse bada number kya hoga?":
        [["A. 23", "B. 24", "C. 25", "D. 26"], "A"],  # Correct: 23

    "₹10,000 par 10% per annum ke hisaab se 2 saal ka Compound Interest kitna hoga?":
        [["A. ₹2000", "B. ₹2100", "C. ₹2200", "D. ₹2300"], "B"]  # Correct: 2100
}

score = 0

print("Welcome to SSC CGL Maths Quiz (Hinglish)!\n")

for question, data in quiz.items():
    print(question)
    for option in data[0]:
        print(option)
    
    answer = input("Apna answer dijiye (A/B/C/D): ").upper()
    
    if answer == data[1]:
        print("✅ Sahi jawab!\n")
        score += 1
    else:
        print(f"❌ Galat! Sahi jawab hai {data[1]}\n")

print(f"Aapka final score hai {score}/{len(quiz)}")