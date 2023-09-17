1. Create a directory with multiple txt files in it having the messages
2. Create an output directory to save those files received

In the Sender_tmp.py code
> Insert the directory path (which you want to send) in the code

In the receiver_tmp.py code
> Insert the output directory path in the code

Brief Working of the code:

Since the assignment mentions to use your ow n publicly available approach as the attribute I choose to use file hash. Basically the receiver code calculates the file hash of the files in the directory and saves the benchmark and copies the data to itself. If any modifications are made to the file which means hash has changed, it will again copy the data to itself. It keeps on monitoring for any changes made. The code is currently working for existing files and the chanegs made into it. I am still figuring out to work on any new file create, since its throwing an error for any new file created.