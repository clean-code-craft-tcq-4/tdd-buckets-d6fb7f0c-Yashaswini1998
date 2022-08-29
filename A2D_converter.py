# def A2D_converter(input_array):
A2D_MAX_LIMIT_12Bit = 4094
A2D_MIN_LIMIT_12Bit = 0
MAX_AMPERE_READING_12Bit = 10

#-------------------Extension: Current-sensing at high fidelity---------------#

def Is_12bit_SensorInputOk(sensorReading):
    if sensorReading in range(A2D_MIN_LIMIT_12Bit,A2D_MAX_LIMIT_12Bit+1): #added one to include A2D_MAX_LIMIT in vailid range
        return True
    else:
        print("ERROR: Invalid sensor reading : ", sensorReading)
        return False

def A2D_Converter(input_array):
    if len(input_array) == 12:
        return Convert_12bit_to_Ampere(input_array)
    elif len(input_array) == 10:
        return Convert_10bit_to_Ampere(input_array)
    else:
        return "Invalid Input!"

def Convert_12bit_to_Ampere(input_array):
    joined_12_bit_number = ''.join(str(i) for i in input_array)
    dec_value = int(joined_12_bit_number, 2)
    if dec_value >= 4095:
        return "Error!!!"
    else:
        ampere = int(round((dec_value*10)/ 4094,0))
        return ampere

def Convert_10bit_to_Ampere(input_array):
    joined_10_bit_number = ''.join(str(i) for i in input_array)
    dec_value = int(joined_10_bit_number, 2)
    if dec_value > 1023:
        return "Error!!!"
    else:
        ampere = int(round(((dec_value*30)/ 1022)-15,0))
    return ampere
