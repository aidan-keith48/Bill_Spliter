# 🧾 Bill Splitter with Lucky Feature 🎲  

## 📌 Project Overview  
This is a simple **bill-splitting program** that fairly divides a total bill among friends. It also includes a **"Who is Lucky?"** feature, which randomly selects one person who doesn't have to pay.  

## 🚀 Features  
- Accepts the **number of attendees** and their names.  
- Takes input for the **total bill amount**.  
- **Equally splits** the bill among all participants.  
- Offers a **"Who is Lucky?"** feature that randomly selects a person who **pays nothing**, while others cover the total bill.  
- Outputs the **final bill split** in a dictionary format.  

## 🛠️ How It Works  
1. The user enters the **number of friends** joining (including themselves).  
2. If the number is `0` or negative, the program exits with:  
3. Otherwise, the user inputs the **names** of all participants.  
4. The program asks for the **total bill value**.  
5. The user decides whether to enable the **"Who is Lucky?"** feature:  
- If **Yes**, one random participant gets to pay **nothing**, while others cover the bill.  
- If **No**, the bill is split evenly among everyone.  
6. The **final bill split** is displayed in a dictionary format.  

## 💻 Example Usage  
```bash
Enter the number of people attending:  
> 3  

Enter the name of every friend (including you), each on a new line:  
> Alice  
> Bob  
> Charlie  

Enter the total bill value:  
> 150  

Do you want to use the "Who is lucky?" feature? Write Yes/No:  
> Yes  

Charlie is the lucky one!  

{'Alice': 75.0, 'Bob': 75.0, 'Charlie': 0}
