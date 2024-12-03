class MultipleFunctions:
        def Subfields():
            FieldsInAI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            print("Sub-fields in AI are:")
            for temp in FieldsInAI:
             print(temp)
        def OddEven():
            Number=int(input("Enter a number:"))
            if(Number%2==0):
                print(Number,"is Even number")
            else:
                print(Number,"is Odd number")
        def Elegible():
            Gender=input("Your Gender:")
            Age=int(input("Your Age"))
            if(Gender=="Male" and Age>=21):
                print("ELIGIBLE")
            elif(Gender=="Female" and Age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        def percentage():
            S1=int(input("Subject1="))
            S2=int(input("Subject2="))
            S3=int(input("Subject3="))
            S4=int(input("Subject4="))
            S5=int(input("Subject5="))
            Total=S1+S2+S3+S4+S5
            print("Total :",Total)
            Percentage=((Total/500)*100)
            print("Percentage :",Percentage)
        def triangleArea():
            Height=int(input("Height:"))
            Breadth=int(input("Breadth:"))
            AreaOfTriangle=(Height*Breadth)/2
            print("Area of Triangle:",AreaOfTriangle)
        def trianglePerimeter():
            Height1=int(input("Height1:")) 
            Height2=int(input("Height2:"))
            Breadth1=int(input("Breadth:"))
            Perimeter=Height1+Height2+Breadth1
            print("Perimeter of Triangle:",Perimeter)  
            