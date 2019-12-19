import cpuinfo

#만약 OS가 windows 라면
print(cpuinfo.cpu.info[0]["ProcessorNameString"])
#else Linux라면
print(cpuinfo.cpu.info[0]["model_nam"])
