def solution(phone_book):   
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]: #앞, 뒤만 비교
            return False        
    return True
