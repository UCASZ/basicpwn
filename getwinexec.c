#include <windows.h>

typedef int (__cdecl *MYPROC)(LPTSTR);

int main() {
  HINSTANCE Kernel32Addr;
  MYPROC WinExecAddr;

  Kernel32Addr = GetModuleHandle("kernel32.dll");
  printf("KERNEL32 address in memory: 0x%08p\n", Kernel32Addr);

  WinExecAddr = (MYPROC)GetProcAddress(Kernel32Addr, "WinExec");

  printf("WinExec address in memory is: 0x%08p\n", WinExecAddr );
  getchar();  
  return 0;
}
