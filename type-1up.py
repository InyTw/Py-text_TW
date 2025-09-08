import time

set_time = float(input("請輸入隔多久發送訊息?\n時間(建議0.0001): "))
user = input("\n請輸入要對說誰?\n名稱(落無請按空格建在按Enter): ")
txt = input("\n請輸入要說的話?\n要說甚麼: ")
times = int(input("\n請輸入要傳送的次數? (一定會有一次)\n次數: "))

for i in range(1, times):
    print(f"{i+1}: {user} {txt}")
    time.sleep(set_time)