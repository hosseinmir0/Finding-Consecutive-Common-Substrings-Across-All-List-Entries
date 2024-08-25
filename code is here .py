
print ("Made by : hossein_mir0 \nTelegram id is: hossein_mir0 \n ")
#==============================================================================#
inputs = ['flower','flow','flight']# => Fl
# inputs = ['flow','floj','fli']# => Fl
# inputs = ['126','23']# => No match found
# inputs = ['ajzad','azada','azadi']# => Zad
# inputs = ['asd','wer','iop'] #=> NO match found
# inputs = ['dog','fldogw','flightdog','sibdog']# => Dog
#==============================================================================
substrings = []
all_substrings = []
#==============================================================================
for word in inputs:
    start = 0
    end = 1
    for char in word:
        for s in range(len(word)):
            all_substrings.append(word[start:end])

            while '' in all_substrings:
                all_substrings.remove('')
            end += 1
        start += 1
        end = 1
#==============================================================================
for substring in all_substrings:
    common_string = ''
    if len(substring) > 1 and all_substrings.count(substring) == len(inputs):
        common_string += str(substring)
        substrings.append(common_string)
        str(substrings)
        set(substrings)
        substrings.sort(key=len, reverse=True)
#==============================================================================
if substrings == []:
    print ("no match found".capitalize())
else:
    print (f"The common substring is \"{substrings[0]}\"".capitalize())
