import pylink
jlink = pylink.Jlink()
jlink.open(STM32F407)
out = jlink.read(0x0,0x100)
print(out)