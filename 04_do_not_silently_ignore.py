import sys

def print_output_file_name(output_file=sys.stdout, **kwargs):
   # silently ignore if keywords other than "output_file" are present
   print(output_file)
   do_nothing(**kwargs)

def do_nothing(*args, **kwargs):
   return

print_output_file_name(outputfile='foo.out')
# print_output_file_name(output_file='foo.out')


# def print_output_file_name__fixed(output_file=sys.stdout, do_nothing_kwargs={}):
#    # silently ignore if keywords other than "output_file" are present
#    print(output_file)
#    do_nothing(**do_nothing_kwargs)

# print_output_file_name__fixed(outputfile='foo.out')
