# Bitwise Operators &, |, ^
number1 = 8                      # 1 0 0 0
number2 = 4                      # 0 1 0 0
result1 = number1 & number2      # 0 0 0 0
result2 = number1 | number2      # 1 1 0 0
result3 = number1 ^ number2      # 1 1 0 0

print('result1:', result1)
print('result2:', result2)
print('result3:', result3)

# Shift Operators >>, <<
number3 = 8         # 0 0 0 0 1 0 0 0  -> 8
number4 = 2         # 0 0 0 0 0 0 1 0  -> 8>>2 -> 2
result4 = number3 >> number4 # 8 >> 2  right shift

 # 0 0 0 0 1 0 0 0  << 2
 # 0 0 1 0 0 0 0 0 -> 8 << 2 -> 32
result5 = number3 << number4 # 8 << 2
print('result5:', result5) # -> 32 

data = 12
key = 2     
send_data_to_fionna = data >> key  # 12/2power3 Encryption
print('send_data_to_fionna:', send_data_to_fionna)
data_received_by_fionna = send_data_to_fionna << key  #Decryption
print('data_received_by_fionna:', data_received_by_fionna)

#even : >> : number1/2power number2