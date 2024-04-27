#As a DevOps engineer, it is crucial to monitor the health and performance of servers.
#->Write a Python program to monitor the health of the CPU. Few pointers to be noted:
#->The program should continuously monitor the CPU usage of the local machine.
#->If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
#->The program should run indefinitely until interrupted.
#->The program should include appropriate error handling to handle exceptions that 
#may arise during the monitoring process.
import psutil

class Runstats:
     def CPUHealthstats(self):
      z=psutil.cpu_percent(5)
      while(z <= 100):   
        if z>= 80:
          print("Alert! CPU usage exceeds threshold: ", z) 
        else:
          print("Monitoring CPU usage, current CPU utilization is: ", z) 
       
Y=Runstats()
Y.CPUHealthstats() 







