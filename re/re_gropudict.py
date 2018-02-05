import re

line =  '5143420588.000000 file tensorflow/core/framework/log_memory.cc:41] __LOG_MEMORY__ MemoryLogTensorDeallocation { allocation_id: 2 allocator_name: "cpu" }'
tensor_deallocation_regex = re.compile("""allocation_id: (?P<allocation_id>\d+).*allocator_name: \"(?P<allocator_name>[^"]+)\".*""")
m = tensor_deallocation_regex.search(line)
print m.groupdict()
