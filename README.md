# What is Gnowflake?
Gnowflake is a personal clone of Twitter's unique ID generator, Snowflake.
The idea is to design a generator that can create a unique id that is capable of distributed systems scalability.  
This mini clone was done after reading Chapter 7 of `System Design: Insider's guide`.

# How to Run
- python3 snowflake.py (optional: give 2 arguments for datacenter number and machine number)

# Description
- The ID is split into 5 parts:
  1. 1 sign bit (for future use, currently remains 0)
  2. 41 bit Timestamp: determined by subtracting Twitter's default epoch from current epoch time(measured in milliseconds)
  3. 5 bit datacenter ID
  4. 5 bit machine ID
  5. Sequence number (refresehd every 3 seconds, 1 millisecond for Twitter)


Read more about Twitter's Snowflake:  
https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake
