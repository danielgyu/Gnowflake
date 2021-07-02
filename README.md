# What is Gnowflake?
Gnowflake is a clone of Twitter's unique ID generator, Snowflake.  
The idea is to design a generator that can create a unique id  
that is capable of distributed systems scalability.  

# How to Run
- python3 snowflake.py (optional: give 2 arguments for datacenter number and machine number)

# Description
- The ID is split into 5 parts.
- The second part, epoch, is determined by subtracting current epoch from Twitter's default epoch(in milliseconds).
- Every 3 seconds, the sequence number is refreshed.


Read more about Twitter's Snowflake:  
https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake
