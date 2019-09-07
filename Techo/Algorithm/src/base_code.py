import six

def encode_base(bits):
    byte=0
    new_bit=[]
    for i in range(len(bits)-4):
        new_bit.append(0)
    for bit in bits:
        new_bit.append(bit)

    for i in range(len(new_bit)):
        byte+=new_bit[i]*2**(int(len(new_bit)-i-1)*2)
    return byte

def decode_base(bytes):
    code=['A','T','C','G']
    ba=list(str(bin(bytes))[2:])
    a=[]
    for i in range(8-len(ba)):
        a.append('0')
    for i in ba:
        a.append(i)

    seq=''
    for i in range(len(a)//2):
        seq+=code[int(''.join(a[i*2:i*2+2]),2)]
    return seq


def encode_seq(str,file):
    code={'A':0,'T':1,'C':2,'G':3}
    bits=[]
    for base in list(str):
        if not code.__contains__(base):
            raise Exception('Unsupport %s'%base)
        bits.append(code[base])
    byte_int=[]
    remain=len(bits)%4
    if remain==0:
        remain=4
    byte_int.append(remain)

    for i in range(len(bits)//4):
        byte_int.append(encode_base(bits[i*4:i*4+4]))
    byte_int.append(encode_base(bits[(len(bits)//4)*4:]))
    print(byte_int)
    bw=open(file,'wb')
    for byte in byte_int:
        bw.write(six.int2byte(byte))
    bw.close()

def decode_seq(file):
    seq=[]
    with open(file,'rb') as br:
        while True:
            block=br.read()
            if not block:
                break
            for byte in block:
                seq.append(byte)
    print(seq)
    remain_base=seq[0]
    sequen=''
    for bit_int in seq[1:-1]:
        sequen+=decode_base(bit_int)
    sequen+=decode_base(seq[-1])[-remain_base:]
    print(sequen)



def test():
    # print(add_bit([3,3]))
    encode_seq('ATCGATGCGGATATATATATTTTTATATTTGGGGGGAGGAGAGAGGAGACACACACC','seq.bin')
    decode_seq('seq.bin')
    # print(decode_base(255))
    # print(int('11',2))

if __name__=='__main__':
    test()
