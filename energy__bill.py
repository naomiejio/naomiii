def parameter1():
    previous = int(input("Enter the previous meter reading: "))
    return previous


def parameter2():
    current = int(input("Enter the current meter reading: "))
    return current


def  parameter3():
    value = int(input("Enter the calofiric value: "))
    return value



def units_used(current, previous):
    units = (current - previous)
    return units


def calc_kwh(units, value):
    kwh = (units * 1.022 * value) / 3.6
    return kwh


def energybill(kwh, energy):
    bill = (kwh * energy)
    return bill
    



def main():
    previous = parameter1()
    current = parameter2()
    value = parameter3()
    units = units_used(current, previous)
    print("The units used is", units)
    kwh = calc_kwh(units, value)
    print("The KWh is =", kwh)
    energy = 2.84
    bill = energybill(kwh, energy)
    print("The Energy bill is", bill)





main()
