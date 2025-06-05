class Solution:
    def compress(self, chars):
        write = 0  # Position to write in the array
        read = 0  # Position to read in the array

        while read < len(chars):
            char = chars[read]  # Current character
            count = 0  # Count occurrences

            # Count how many times the character repeats
            while read < len(chars) and chars[read] == char:
                count += 1
                read += 1

            # Write the character to the new position
            chars[write] = char
            write += 1

            # If the count is greater than 1, write the digits
            if count > 1:
                for digit in str(count):  # Convert number to characters
                    chars[write] = digit
                    write += 1

        return write  # New length of the modified array

