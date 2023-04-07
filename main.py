# ----------------------------------------------------------------------------
#   Comparing different approaches to get the contents
# ----------------------------------------------------------------------------
# Remember that we previously closed the file so we need to open it again
fobj = open(SRCFILE, mode='r')
# Contents using `.read`
#cnts = fobj.read()
cnts = ''
print(f"First 20 characters in cnts: '{cnts[:20]}'")

# Start with an empty string
cnts_copy = ''
# Iterate over each line of fobj # <comment>
for line in fobj:
    # Add this line to the string `cnts_copy` # <comment>
    cnts_copy += line

# Print the result
print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")

# close the file
fobj.close()