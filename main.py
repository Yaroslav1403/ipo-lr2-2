n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_per_student = k // n 
remaining_apples = k % n
print(f"Каждому школьнику достанется {apples_per_student} яблок(а).")
print(f"В корзинке останется {remaining_apples} яблок(а).")
