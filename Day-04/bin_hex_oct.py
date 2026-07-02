def main():
    a=10
    b=[10,20,30]
    print(a,id(a),type(a))
    print(b,id(b),type(b))
    print(b[0],id(b[0]),type(b[0]))
    print(bin(id(b)))
    print(hex(id(b)))
    print(oct(id(b)))

if __name__=='__main__':
    main()