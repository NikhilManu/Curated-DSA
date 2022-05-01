# Time O(Digits) | Space O(1)

dic = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
}
def intToWods(num):
    if num == 0: return 'Zero'
    billion, million = 1000000000, 1000000
    res = []
    if num >= billion:
        res.extend([convert(num // billion), 'Billion'])
        num %= billion
        
    if num >= million:
        res.extend([convert(num // million), 'Million'])
        num %= million
        
    if num >= 1000:
        res.extend([convert(num // 1000), 'Thousand'])
        num %= 1000
    
    if num > 0:
        res.append(convert(num))
        
    return ' '.join(res)
    
def convert(num):
    res = []
    if num >= 100:
        HundredthPlace = num // 100
        res.extend([dic[HundredthPlace], 'Hundred'])
        num %= 100
    
    if num > 0:
        if num <= 20:
            res.append(dic[num])
        else:
            TensPlace = num // 10
            OnesPlace = num % 10
            res.append(dic[TensPlace * 10])
            if OnesPlace > 0:
                res.append(dic[OnesPlace])

    return ' '.join(res)