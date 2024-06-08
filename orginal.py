import  os
from colorama import Fore
import time
os.system('cls')
os.system("color 0b")
print('''In the name of God, the Most Gracious, the Most Merciful
I, Amir Mahdi Zare, a 10th grade math student at Dr. Mehdi Torkzadeh High School,
am honored to present this program for calculating heat, heat capacity, and specific heat
based on the heat formula from Chapter 4 of 10th grade physics.
''')
        # time.sleep(2)
print("Instructor: Mr. Hassanzadeh Moghadam")
print("Programmer: Amir Mahdi Zare")
class HeatCalculator:
    def __init__(self):
        pass

    def calculate_c(self, Q, m, delta_T):
        return Q / (m * delta_T)

    def calculate_Q(self, c, m, delta_T):
        return c * m * delta_T
    
    def calculate_m(self, Q, c, delta_T):
        return Q / (c * delta_T)
    
    def calculate_delta_T(self, Q, c, m):
        return Q / (c * m)
    
    def calculate_T2(self, Q, m, c, T1):
        return (Q / (c * m))+T1

        

    def run(self):
        while True:
            try:

                print(Fore.LIGHTYELLOW_EX+"برای محاسبه ظرفیت گرمایی ویژه (c) : c")
                print("برای محاسبه گرما (Q) : ًq")
                print("برای محاسبه جرم (m) : m")
                print("برای محاسبه تفاوت دما (ΔT):  t")
                print("برای محاسبه دمای دوم (T2) : t2")
                print("برای خروج از exit  استفاده کنبد.")
                choice = input("انتخاب شما ==>>  ").lower()

                os.system("cls") 
                os.system("color 0b")
                if choice == 'exit':
                    print("خداحافظ!")
                    break

                elif choice == 'c':
                    Q = float(input("لطفا مقدار حرارت (Q) را وارد کنید (به واحد جول): "))
                    m = float(input("لطفا مقدار جرم (m) را وارد کنید (به واحد کیلوگرم): "))
                    delta_T = float(input("لطفا مقدار تغییر دما (ΔT) را وارد کنید (به واحد درجه سلسیوس): "))
                    
                    c = self.calculate_c(Q, m, delta_T)
                    print(f"گرمای ویژه (c) برابر است با: {c} جول بر کیلوگرم بر درجه سلسیوس")
                
                elif choice == 'q':
                    c = float(input("لطفا مقدار گرمای ویژه (c) را وارد کنید (به واحد جول بر کیلوگرم بر درجه سلسیوس): "))
                    m = float(input("لطفا مقدار جرم (m) را وارد کنید (به واحد کیلوگرم): "))
                    delta_T = float(input("لطفا مقدار تغییر دما (ΔT) را وارد کنید (به واحد درجه سلسیوس): "))
                    
                    Q = self.calculate_Q(c, m, delta_T)
                    print(f"حرارت (Q) برابر است با: {Q} جول")
                
                elif choice == 'm':
                    Q = float(input("لطفا مقدار حرارت (Q) را وارد کنید (به واحد جول): "))
                    c = float(input("لطفا مقدار گرمای ویژه (c) را وارد کنید (به واحد جول بر کیلوگرم بر درجه سلسیوس): "))
                    delta_T = float(input("لطفا مقدار تغییر دما (ΔT) را وارد کنید (به واحد درجه سلسیوس): "))

                    m = self.calculate_m(Q, c, delta_T)
                    print(f"جرم (m) برابر است با: {m}  کیلوگرم")

                elif choice == 't':
                    Q = float(input("لطفا مقدار حرارت (Q) را وارد کنید (به واحد جول): "))
                    c = float(input("لطفا مقدار گرمای ویژه (c) را وارد کنید (به واحد جول بر کیلوگرم بر درجه سلسیوس): "))
                    m = float(input("لطفا مقدار جرم (m) را وارد کنید (به واحد کیلوگرم): "))

                    delta_T = self.calculate_delta_T(Q, c, m)
                    print(f"تغیر دما ( ΔT) برابر است با: {delta_T}  بر حسب سانتی گراد و کلوین")


                elif choice == 't2':
                    Q = float(input("لطفا مقدار حرارت (Q) را وارد کنید (به واحد جول): "))
                    c = float(input("لطفا مقدار گرمای ویژه (c) را وارد کنید (به واحد جول بر کیلوگرم بر درجه سلسیوس): "))
                    m = float(input("لطفا مقدار جرم (m) را وارد کنید (به واحد کیلوگرم): "))
                    T1 = float(input("لطفا مقدار دما اول (T1) را وارد کنید (به واحد درجه سلسیوس): "))

                    T2 = self.calculate_delta_T(Q, c, m, T1)
                    print(" دمااول (T2) برابر است با: {T2}  بر حسب سانتی گراد و کلوین")

                else:
                    print(Fore.LIGHTRED_EX+"ورودی نامعتبر! لطفا فقط 'c', 'q' یا 'exit' را وارد کنید.")
                
                
            except ValueError:
                print(Fore.LIGHTRED_EX+"ورودی نامعتبر! لطفا مقادیر عددی صحیح وارد کنید.")


# برنامه اصلی
if __name__ == "__main__":
    calculator = HeatCalculator()
    calculator.run()
