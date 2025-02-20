from datetime import datetime

def clean_and_sort_data():
    n = int(input())
    data = []
    
    for _ in range(n):
        row = input().strip()
        fields = row.split(",")
        
        if len(fields) < 5:
            continue  
        
        fields = fields[:5]
        
        if any(not field.strip() for field in fields):
            continue  
        
        try:
            date_obj = datetime.strptime(fields[0], "%Y-%m-%d")
            
            open_price = float(fields[1])
            high_price = float(fields[2])
            low_price = float(fields[3])
            close_price = float(fields[4])
            
            data.append((date_obj, fields[0], open_price, high_price, low_price, close_price))
        except ValueError:
            continue  
    
    data.sort()
    for row in data:
        print(f"{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")

clean_and_sort_data()
