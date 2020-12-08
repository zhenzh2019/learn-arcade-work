def main():
    #my_list = [101, 20, 10, 50, 60]
    # for item in my_list:
    #     print(item)
    #my_tupl=  (101, 20, 10, 50, 60)
    # for item in my_tupl:
    #     print(item)
    # my_dict = {'a':101, 'b':20, 'c':10, 'd':50, 'e':60}
    # for item in my_dict:
    # #         print(my_dict[item])
    # lst = [ 1, 1, 0]
    #
    # lst_set = set( lst )  #lst_set 为1 , 0
    #
    # tup = (2, 2, 1)
    #
    # tup_set = set( tup) # tup_set为2 , 1
    #
    # for item in lst_set:
    #     print (item)
    # print ("----------------")
    # for item in tup_set:
    #         print(item)
    # print ("----------------")
    # seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    # print(list(enumerate(seasons)))
    # list(enumerate(seasons, start=1))
    # i=0
    # for i,element in enumerate(seasons):
    #     print(i, element)
    # print("----------------")
    #
    # my_list = [[0,1]] * 100
    # print(my_list)
    # total=0
    # my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
    # print(my_list)
    # for i in range(len(my_list)):
    #     total= total + my_list[i]
    #     my_list[i]*=my_list[i]
    # print(my_list)
    # n=1
    # while n<=12 and n>0 :
    #     months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    #     n = int(input("Enter a month number: "))
    #     if n>0 and n<=12 :
    #         start_n=(n-1)*3
    #         end_n= start_n+3
    #         print(months[start_n:end_n])
    #     else:
    #         print("Wrong Number!")
    #         # break
    #     print("--------------------------")

    plain_text = "This is a test. ABC abc"

    for c in plain_text:
        print(c, end=" ")
        
if __name__ == '__main__':
    main()